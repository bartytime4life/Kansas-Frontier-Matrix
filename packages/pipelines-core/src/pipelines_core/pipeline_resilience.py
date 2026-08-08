"""Deterministic, side-effect-free pipeline resilience planning primitives.

The public planner composes trigger admission, idempotency, bounded retry,
backpressure, circuit breaking, replay-safe delivery, and kill-switch decisions.
It performs no network, filesystem, workflow, database, policy-engine, secret,
release, or publication action.
"""

from __future__ import annotations

from typing import Any, Mapping

from ._pipeline_resilience_admission import _retry_decision, _trigger_decision
from ._pipeline_resilience_common import (
    PLANNER_VERSION,
    PipelineResiliencePlanError,
    _CONTRACT_VERSION,
    _PIPELINE_ID,
    _STEP_ID,
    _canonical_json,
    _dedupe_codes,
    _hash,
    _require_identifier,
    _require_mapping,
)
from ._pipeline_resilience_delivery import (
    _delivery_decision,
    _kill_switch_decision,
)
from ._pipeline_resilience_flow import (
    _backpressure_decision,
    _breaker_decision,
)

def _aggregate_decision(
    *,
    trigger: Mapping[str, Any],
    retry: Mapping[str, Any],
    backpressure: Mapping[str, Any],
    breaker: Mapping[str, Any],
    delivery: Mapping[str, Any],
    kill_switch: Mapping[str, Any],
) -> tuple[str, list[str]]:
    groups = [
        list(trigger["reason_codes"]),
        list(retry["reason_codes"]),
        list(backpressure["reason_codes"]),
        list(breaker["reason_codes"]),
        list(delivery["reason_codes"]),
        list(kill_switch["reason_codes"]),
    ]
    reasons = _dedupe_codes(*groups)

    if trigger["decision"] == "DENY" or kill_switch["decision"] == "DENY":
        return "DENY", reasons
    if backpressure["decision"] == "DENY" or delivery["decision"] == "DENY":
        return "DENY", reasons
    if retry["classification"] == "POLICY_DENIED":
        return "DENY", reasons
    if retry["decision"] == "QUARANTINE" or delivery["decision"] == "QUARANTINE":
        return "QUARANTINE", reasons
    if retry["decision"] == "OPERATOR_REQUIRED" or delivery["decision"] == "HOLD":
        return "OPERATOR_REQUIRED", reasons
    if kill_switch["decision"] in {"PAUSE_NEW_STARTS", "STOP_ALL"}:
        return "PAUSE", reasons
    if breaker["decision"] in {"DENY", "PROBE"}:
        return "PAUSE", reasons
    if backpressure["decision"] in {"THROTTLE", "SHED", "HOLD"}:
        return "PAUSE", reasons
    if delivery["decision"] == "REPLAY":
        return "ALLOW_REPLAY", reasons
    if retry["decision"] == "RETRY":
        return "ALLOW_RETRY", reasons
    if retry["classification"] == "DETERMINISTIC":
        return "NO_ACTION", reasons
    if retry["decision"] == "STOP":
        return "NO_ACTION", reasons
    return "ALLOW_START", reasons


def _receipt_requirements(
    *,
    retry: Mapping[str, Any],
    backpressure: Mapping[str, Any],
    breaker: Mapping[str, Any],
    delivery: Mapping[str, Any],
    kill_switch: Mapping[str, Any],
) -> list[str]:
    receipts = {"terminal_receipt"}
    if retry["decision"] == "RETRY":
        receipts.add("attempt_receipt")
    if backpressure["decision"] != "ACCEPT":
        receipts.add("backpressure_decision_receipt")
    if breaker["current_state"] != breaker["next_state"]:
        receipts.add("circuit_breaker_transition_receipt")
    if delivery["decision"] == "REPLAY":
        receipts.add("dead_letter_replay_receipt")
    if kill_switch["mode"] != "RUNNING" or kill_switch["previous_mode"] != "RUNNING":
        receipts.add("kill_switch_state_receipt")
    return sorted(receipts)


def plan_pipeline_resilience(request: Mapping[str, Any]) -> dict[str, Any]:
    """Return a deterministic planning-only pipeline resilience decision."""

    request = _require_mapping(
        request,
        "/",
        {
            "pipeline_id",
            "step_id",
            "contract_version",
            "trigger",
            "input_manifest",
            "retry_context",
            "queue",
            "breaker",
            "delivery",
            "kill_switch",
            "policy",
        },
    )

    pipeline_id = _require_identifier(
        request["pipeline_id"],
        "/pipeline_id",
        _PIPELINE_ID,
        "PIPELINE_ID_INVALID",
    )
    step_id = _require_identifier(
        request["step_id"], "/step_id", _STEP_ID, "STEP_ID_INVALID"
    )
    contract_version = _require_identifier(
        request["contract_version"],
        "/contract_version",
        _CONTRACT_VERSION,
        "CONTRACT_VERSION_INVALID",
    )

    trigger_request = _require_mapping(
        request["trigger"],
        "/trigger",
        {
            "type",
            "environment",
            "authorization_ref",
            "environment_gate_ref",
            "concurrency_group",
            "secret_scope",
        },
    )
    retry_context = _require_mapping(
        request["retry_context"],
        "/retry_context",
        {
            "error_class",
            "attempt_number",
            "elapsed_seconds",
            "retry_after_seconds",
            "jitter_unit",
        },
    )
    queue = _require_mapping(
        request["queue"],
        "/queue",
        {
            "partition",
            "depth",
            "oldest_age_seconds",
            "in_flight",
            "isolated_outputs",
            "public_side_effects",
            "contracts_match_production",
            "schemas_match_production",
            "policies_match_production",
        },
    )
    breaker = _require_mapping(
        request["breaker"],
        "/breaker",
        {
            "state",
            "consecutive_failures",
            "cooldown_elapsed",
            "probe_succeeded",
        },
    )
    delivery = _require_mapping(
        request["delivery"],
        "/delivery",
        {
            "emits_event",
            "durability_mode",
            "atomic_commit_verified",
            "consumer_idempotency_verified",
            "dead_letter",
        },
    )
    kill_switch = _require_mapping(
        request["kill_switch"],
        "/kill_switch",
        {
            "previous_mode",
            "mode",
            "activation_receipt_ref",
            "reenable_review_ref",
            "in_flight_policy",
        },
    )
    policy = _require_mapping(
        request["policy"],
        "/policy",
        {"retry", "backpressure", "breaker"},
    )
    retry_policy = _require_mapping(
        policy["retry"],
        "/policy/retry",
        {
            "max_attempts",
            "base_delay_seconds",
            "multiplier",
            "max_delay_seconds",
            "deadline_seconds",
            "jitter_fraction",
            "idempotency_retention_seconds",
        },
    )
    backpressure_policy = _require_mapping(
        policy["backpressure"],
        "/policy/backpressure",
        {
            "max_queue_depth",
            "max_oldest_age_seconds",
            "max_in_flight",
            "shed_allowed",
        },
    )
    breaker_policy = _require_mapping(
        policy["breaker"],
        "/policy/breaker",
        {"failure_threshold"},
    )

    input_manifest = request["input_manifest"]
    if not isinstance(input_manifest, Mapping) or not input_manifest:
        raise PipelineResiliencePlanError(
            "INPUT_MANIFEST_EMPTY_OR_INVALID", "/input_manifest"
        )
    _canonical_json(input_manifest, field="/input_manifest")

    trigger_plan = _trigger_decision(trigger_request)
    retry_plan = _retry_decision(retry_context, retry_policy)
    backpressure_plan = _backpressure_decision(queue, backpressure_policy)
    breaker_plan = _breaker_decision(breaker, breaker_policy)
    delivery_plan = _delivery_decision(delivery)
    kill_switch_plan = _kill_switch_decision(kill_switch)

    idempotency_payload = {
        "pipeline_id": pipeline_id,
        "step_id": step_id,
        "contract_version": contract_version,
        "trigger": {
            "type": trigger_plan["type"],
            "environment": trigger_plan["environment"],
            "concurrency_group": trigger_plan["concurrency_group"],
        },
        "input_manifest": input_manifest,
    }
    idempotency_key = _hash(_canonical_json(idempotency_payload))
    spec_hash = _hash(_canonical_json(request))
    plan_id = (
        f"pipeline-resilience:{pipeline_id}:{step_id}:"
        f"{idempotency_key.removeprefix('sha256:')[-16:]}"
    )

    decision, reason_codes = _aggregate_decision(
        trigger=trigger_plan,
        retry=retry_plan,
        backpressure=backpressure_plan,
        breaker=breaker_plan,
        delivery=delivery_plan,
        kill_switch=kill_switch_plan,
    )
    required_receipts = _receipt_requirements(
        retry=retry_plan,
        backpressure=backpressure_plan,
        breaker=breaker_plan,
        delivery=delivery_plan,
        kill_switch=kill_switch_plan,
    )

    return {
        "plan_id": plan_id,
        "planner_version": PLANNER_VERSION,
        "pipeline_id": pipeline_id,
        "step_id": step_id,
        "contract_version": contract_version,
        "spec_hash": spec_hash,
        "idempotency_key": idempotency_key,
        "decision": decision,
        "reason_codes": reason_codes,
        "trigger": trigger_plan,
        "retry": retry_plan,
        "backpressure": backpressure_plan,
        "circuit_breaker": breaker_plan,
        "delivery": delivery_plan,
        "kill_switch": kill_switch_plan,
        "required_receipts": required_receipts,
        "observability_requirements": [
            "breaker_state",
            "oldest_queue_age_seconds",
            "queue_depth",
            "retry_attempt_count",
            "time_to_drain_seconds",
        ],
        "authority": {
            "network_fetch": False,
            "artifact_write": False,
            "workflow_mutation": False,
            "database_mutation": False,
            "secret_access": False,
            "policy_evaluation": False,
            "promotion": False,
            "release": False,
            "publication": False,
        },
        "write_authority": False,
    }


