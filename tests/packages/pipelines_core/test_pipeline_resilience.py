from __future__ import annotations

import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/pipelines-core/src"
sys.path.insert(0, str(PACKAGE_SRC))

from pipelines_core.pipeline_resilience import (
    PipelineResiliencePlanError,
    plan_pipeline_resilience,
)

FIXTURES = (
    REPO_ROOT
    / "fixtures/contracts/v1/runtime/pipeline_resilience_plan"
)
CLI = REPO_ROOT / "scripts/plan_pipeline_resilience.py"
REQUEST_SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/runtime/pipeline_resilience_request.schema.json"
)
PLAN_SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/runtime/pipeline_resilience_plan.schema.json"
)


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _request(name: str = "allow_start") -> dict:
    return _load(FIXTURES / "valid" / f"{name}.request.json")


@pytest.mark.parametrize("schema_path", [REQUEST_SCHEMA, PLAN_SCHEMA])
def test_schema_is_valid_draft_2020_12(schema_path: Path) -> None:
    Draft202012Validator.check_schema(_load(schema_path))


@pytest.mark.parametrize(
    "name",
    [
        "allow_start",
        "allow_retry",
        "allow_replay",
        "pause_new_starts",
        "deny_canary",
    ],
)
def test_valid_fixture_matches_expected_plan(name: str) -> None:
    request = _request(name)
    expected = _load(FIXTURES / "valid" / f"{name}.expected.json")
    plan = plan_pipeline_resilience(request)
    assert plan == expected
    Draft202012Validator(_load(REQUEST_SCHEMA)).validate(request)
    Draft202012Validator(_load(PLAN_SCHEMA)).validate(plan)


def test_manifest_key_order_does_not_change_idempotency_identity() -> None:
    request = _request()
    reordered = deepcopy(request)
    reordered["input_manifest"] = {
        "parameters": {"period": "P1D", "state": "KS"},
        "source_head": {
            "retrieved_at": "2026-08-08T00:00:00Z",
            "etag": "\"fixture-etag\"",
        },
        "dataset_id": "usgs-nwis-kansas",
    }
    first = plan_pipeline_resilience(request)
    second = plan_pipeline_resilience(reordered)
    assert second["idempotency_key"] == first["idempotency_key"]
    assert second["plan_id"] == first["plan_id"]
    assert second["spec_hash"] == first["spec_hash"]


def test_operational_queue_state_changes_spec_not_idempotency_key() -> None:
    request = _request()
    overloaded = deepcopy(request)
    overloaded["queue"]["depth"] = 1200
    first = plan_pipeline_resilience(request)
    second = plan_pipeline_resilience(overloaded)
    assert second["idempotency_key"] == first["idempotency_key"]
    assert second["spec_hash"] != first["spec_hash"]
    assert second["decision"] == "PAUSE"
    assert second["backpressure"]["decision"] == "HOLD"


def test_transient_retry_is_bounded_and_deterministic() -> None:
    request = _request()
    request["retry_context"] = {
        "error_class": "TRANSIENT",
        "attempt_number": 2,
        "elapsed_seconds": 10,
        "retry_after_seconds": None,
        "jitter_unit": 0.75,
    }
    plan = plan_pipeline_resilience(request)
    assert plan["decision"] == "ALLOW_RETRY"
    assert plan["retry"]["delay_seconds"] == 4.5
    assert plan["retry"]["next_attempt"] == 3
    assert "attempt_receipt" in plan["required_receipts"]


def test_rate_limit_retry_honors_bounded_retry_after() -> None:
    request = _request("allow_retry")
    plan = plan_pipeline_resilience(request)
    assert plan["retry"]["classification"] == "RATE_LIMITED"
    assert plan["retry"]["delay_seconds"] == 22.5
    assert plan["retry"]["reason_codes"] == [
        "RATE_LIMIT_RETRY",
        "RETRY_AFTER_HONORED",
    ]


@pytest.mark.parametrize("error_class", ["DETERMINISTIC", "POLICY_DENIED"])
def test_non_retriable_failures_never_retry(error_class: str) -> None:
    request = _request()
    request["retry_context"]["error_class"] = error_class
    plan = plan_pipeline_resilience(request)
    assert plan["retry"]["decision"] == "STOP"
    assert plan["retry"]["next_attempt"] is None
    assert plan["retry"]["delay_seconds"] == 0.0
    assert plan["decision"] in {"NO_ACTION", "DENY"}


def test_retry_attempt_limit_stops_without_sleep() -> None:
    request = _request()
    request["retry_context"].update(
        {"error_class": "TRANSIENT", "attempt_number": 5}
    )
    plan = plan_pipeline_resilience(request)
    assert plan["retry"]["decision"] == "STOP"
    assert plan["retry"]["reason_codes"] == [
        "RETRY_ATTEMPT_LIMIT_REACHED"
    ]


def test_pull_request_cannot_target_production() -> None:
    request = _request()
    request["trigger"].update(
        {
            "type": "pull_request",
            "environment": "production",
            "environment_gate_ref": "kfm://decision/environment/prod-001",
        }
    )
    plan = plan_pipeline_resilience(request)
    assert plan["decision"] == "DENY"
    assert "DIRECT_CODE_TRIGGER_TO_PRODUCTION_DENIED" in (
        plan["trigger"]["reason_codes"]
    )


@pytest.mark.parametrize(
    "trigger_type",
    ["workflow_dispatch", "repository_dispatch", "external_webhook"],
)
def test_manual_or_external_trigger_requires_authorization(
    trigger_type: str,
) -> None:
    request = _request()
    request["trigger"]["type"] = trigger_type
    request["trigger"]["authorization_ref"] = None
    plan = plan_pipeline_resilience(request)
    assert plan["trigger"]["decision"] == "DENY"
    assert "TRIGGER_AUTHORIZATION_REQUIRED" in (
        plan["trigger"]["reason_codes"]
    )


def test_canary_requires_production_contract_schema_policy_parity() -> None:
    plan = plan_pipeline_resilience(_request("deny_canary"))
    assert plan["decision"] == "DENY"
    assert plan["backpressure"]["decision"] == "DENY"
    assert "CANARY_OUTPUT_ISOLATION_REQUIRED" in (
        plan["backpressure"]["reason_codes"]
    )
    assert "CANARY_PUBLIC_SIDE_EFFECTS_DENIED" in (
        plan["backpressure"]["reason_codes"]
    )


def test_overloaded_sheddable_queue_pauses_new_work() -> None:
    request = _request()
    request["queue"]["depth"] = 1001
    request["policy"]["backpressure"]["shed_allowed"] = True
    plan = plan_pipeline_resilience(request)
    assert plan["decision"] == "PAUSE"
    assert plan["backpressure"]["decision"] == "SHED"
    assert "backpressure_decision_receipt" in plan["required_receipts"]


def test_closed_breaker_opens_at_failure_threshold() -> None:
    request = _request()
    request["breaker"]["consecutive_failures"] = 5
    plan = plan_pipeline_resilience(request)
    assert plan["decision"] == "PAUSE"
    assert plan["circuit_breaker"]["next_state"] == "OPEN"
    assert plan["circuit_breaker"]["decision"] == "DENY"
    assert "circuit_breaker_transition_receipt" in (
        plan["required_receipts"]
    )


def test_open_breaker_moves_to_half_open_probe_after_cooldown() -> None:
    request = _request()
    request["breaker"].update(
        {
            "state": "OPEN",
            "consecutive_failures": 5,
            "cooldown_elapsed": True,
            "probe_succeeded": None,
        }
    )
    plan = plan_pipeline_resilience(request)
    assert plan["decision"] == "PAUSE"
    assert plan["circuit_breaker"]["next_state"] == "HALF_OPEN"
    assert plan["circuit_breaker"]["decision"] == "PROBE"


def test_event_delivery_without_atomicity_is_quarantined() -> None:
    request = _request()
    request["delivery"]["atomic_commit_verified"] = False
    plan = plan_pipeline_resilience(request)
    assert plan["decision"] == "QUARANTINE"
    assert plan["delivery"]["decision"] == "QUARANTINE"
    assert "ATOMIC_COMMIT_NOT_VERIFIED" in (
        plan["delivery"]["reason_codes"]
    )


def test_dead_letter_replay_requires_authorization_and_rechecks() -> None:
    request = _request("allow_replay")
    request["delivery"]["dead_letter"].update(
        {
            "authorization_ref": None,
            "admission_rechecked": False,
            "policy_rechecked": False,
        }
    )
    plan = plan_pipeline_resilience(request)
    assert plan["decision"] == "OPERATOR_REQUIRED"
    assert plan["delivery"]["decision"] == "HOLD"
    assert plan["delivery"]["reason_codes"] == [
        "DEAD_LETTER_ADMISSION_RECHECK_REQUIRED",
        "DEAD_LETTER_POLICY_RECHECK_REQUIRED",
        "DEAD_LETTER_REPLAY_AUTHORIZATION_REQUIRED",
    ]


def test_replay_under_new_contract_is_explicit_and_receipted() -> None:
    plan = plan_pipeline_resilience(_request("allow_replay"))
    assert plan["decision"] == "ALLOW_REPLAY"
    assert "DEAD_LETTER_CONTRACT_VERSION_CHANGED" in (
        plan["delivery"]["reason_codes"]
    )
    assert "dead_letter_replay_receipt" in plan["required_receipts"]


def test_pause_new_starts_preserves_in_flight_work() -> None:
    plan = plan_pipeline_resilience(_request("pause_new_starts"))
    assert plan["decision"] == "PAUSE"
    assert plan["kill_switch"]["decision"] == "PAUSE_NEW_STARTS"
    assert "kill_switch_state_receipt" in plan["required_receipts"]


def test_reenable_requires_review_reference() -> None:
    request = _request()
    request["kill_switch"].update(
        {
            "previous_mode": "PAUSE_NEW_STARTS",
            "mode": "RUNNING",
            "reenable_review_ref": None,
        }
    )
    plan = plan_pipeline_resilience(request)
    assert plan["decision"] == "DENY"
    assert plan["kill_switch"]["reason_codes"] == [
        "KILL_SWITCH_REENABLE_REVIEW_REQUIRED"
    ]


def test_emergency_stop_requires_explicit_cancel_policy() -> None:
    request = _request()
    request["kill_switch"].update(
        {
            "previous_mode": "RUNNING",
            "mode": "EMERGENCY_STOP",
            "activation_receipt_ref": "kfm://receipt/kill-switch/stop-001",
            "in_flight_policy": "CONTINUE",
        }
    )
    plan = plan_pipeline_resilience(request)
    assert plan["decision"] == "DENY"
    assert plan["kill_switch"]["reason_codes"] == [
        "EMERGENCY_STOP_MUST_CANCEL_IN_FLIGHT"
    ]


@pytest.mark.parametrize(
    ("fixture", "code"),
    [
        ("unsafe_pipeline_id.request.json", "PIPELINE_ID_INVALID"),
        ("inconsistent_delivery.request.json", "DELIVERY_NONE_SHAPE_INVALID"),
    ],
)
def test_invalid_semantic_fixtures_fail_closed(
    fixture: str, code: str
) -> None:
    with pytest.raises(PipelineResiliencePlanError) as exc:
        plan_pipeline_resilience(_load(FIXTURES / "invalid" / fixture))
    assert exc.value.code == code


def test_nonfinite_manifest_is_not_canonical_json() -> None:
    request = _request()
    request["input_manifest"]["bad"] = float("nan")
    with pytest.raises(PipelineResiliencePlanError) as exc:
        plan_pipeline_resilience(request)
    assert exc.value.code == "VALUE_NOT_CANONICAL_JSON"


def test_cli_emits_planning_only_answer() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(CLI),
            str(FIXTURES / "valid" / "allow_retry.request.json"),
        ],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    payload = json.loads(completed.stdout)
    assert payload["outcome"] == "ANSWER"
    assert payload["plan"]["decision"] == "ALLOW_RETRY"
    assert set(payload["authority"].values()) == {False}


def test_cli_schema_invalid_request_returns_deny() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(CLI),
            str(
                FIXTURES
                / "invalid"
                / "unsafe_pipeline_id.request.json"
            ),
        ],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 1
    payload = json.loads(completed.stdout)
    assert payload["outcome"] == "DENY"
    assert payload["plan"] is None
    assert any(
        item["code"] == "SCHEMA_INVALID"
        for item in payload["findings"]
    )


def test_cli_duplicate_key_is_operational_error(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.json"
    path.write_text(
        '{"pipeline_id":"a","pipeline_id":"b"}', encoding="utf-8"
    )
    completed = subprocess.run(
        [sys.executable, str(CLI), str(path)],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 1
    payload = json.loads(completed.stdout)
    assert payload["outcome"] == "ERROR"
    assert payload["findings"] == [
        {"code": "JSON_DUPLICATE_KEY", "path": "/"}
    ]
