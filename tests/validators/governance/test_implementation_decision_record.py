from __future__ import annotations

import copy
import json
import os
import socket
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest import mock

import pytest
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.governance.validate_implementation_decision_record import (
    EXIT_ERROR,
    EXIT_HOLD,
    FIXTURE_PATH,
    SCHEMA_PATH,
    evaluate_document,
    evaluate_paths,
    render_markdown,
    run_fixture_suite,
)


def _cases() -> dict[str, dict[str, object]]:
    payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    return {case["name"]: case["document"] for case in payload["cases"]}


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)


def test_fixture_manifest_has_exact_polarity() -> None:
    ok, payload = run_fixture_suite()
    assert ok, payload
    assert payload == {
        "authority": "NONE",
        "outcome": "PASS",
        "cases": 5,
        "mismatches": [],
    }


def test_ready_record_is_non_authoritative() -> None:
    record = _cases()["ready-local-review"]
    evaluation = evaluate_document(record)
    assert evaluation.outcome == "READY"
    assert evaluation.findings == ()
    assert set(record["permissions"].values()) == {False}


def test_backfill_draft_holds_without_validation() -> None:
    evaluation = evaluate_document(_cases()["hold-draft-without-validation"])
    assert evaluation.outcome == "HOLD"
    assert [finding.code for finding in evaluation.findings] == ["RECORD_DRAFT"]


def test_authority_significant_record_requires_adr() -> None:
    evaluation = evaluate_document(_cases()["hold-authority-significant-without-adr"])
    assert evaluation.outcome == "HOLD"
    assert [finding.code for finding in evaluation.findings] == ["ADR_REQUIRED"]


def test_permission_overreach_is_error() -> None:
    evaluation = evaluate_document(_cases()["error-permission-overreach"])
    assert evaluation.outcome == "ERROR"
    assert any(finding.code == "SCHEMA_INVALID" for finding in evaluation.findings)


def test_noncanonical_support_order_is_error() -> None:
    evaluation = evaluate_document(_cases()["error-unsorted-support"])
    assert evaluation.outcome == "ERROR"
    assert any(finding.code == "CANONICAL_ORDER_REQUIRED" for finding in evaluation.findings)


def test_cross_component_significance_requires_multiple_roots() -> None:
    record = copy.deepcopy(_cases()["ready-local-review"])
    record["governance"]["significance"] = "CROSS_COMPONENT"
    record["scope"]["paths"] = ["contracts/governance/example.md"]
    evaluation = evaluate_document(record)
    assert evaluation.outcome == "ERROR"
    assert any(finding.code == "SIGNIFICANCE_SCOPE_MISMATCH" for finding in evaluation.findings)


def test_private_reasoning_or_person_profile_is_denied() -> None:
    record = copy.deepcopy(_cases()["ready-local-review"])
    record["decision"]["rationale"] = "Store a hidden reasoning transcript."
    evaluation = evaluate_document(record)
    assert evaluation.outcome == "ERROR"
    assert any(finding.code == "PRIVATE_REASONING_OR_PROFILE_DENIED" for finding in evaluation.findings)


def test_renderer_is_deterministic_and_mechanical() -> None:
    first = _cases()["ready-local-review"]
    second = copy.deepcopy(first)
    second["record_id"] = "kfm:implementation-decision:review-context:0003"
    second["title"] = "Second deterministic decision"
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        a = root / "a.json"
        b = root / "b.json"
        a.write_text(json.dumps(second), encoding="utf-8")
        b.write_text(json.dumps(first), encoding="utf-8")
        payload, records = evaluate_paths([a, b])
        rendered_a = render_markdown(records)
        payload_again, records_again = evaluate_paths([b, a])
        rendered_b = render_markdown(records_again)
    assert payload["outcome"] == payload_again["outcome"] == "READY"
    assert rendered_a == rendered_b
    assert rendered_a.index(":0001") < rendered_a.index(":0003")
    assert "creates no evidence" in rendered_a
    assert "Store free-form session transcripts" in rendered_a


def test_duplicate_record_ids_are_error() -> None:
    record = _cases()["ready-local-review"]
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        a = root / "a.json"
        b = root / "b.json"
        a.write_text(json.dumps(record), encoding="utf-8")
        b.write_text(json.dumps(record), encoding="utf-8")
        payload, _ = evaluate_paths([a, b])
    assert payload["outcome"] == "ERROR"
    assert {finding["code"] for finding in payload["findings"]} == {"DUPLICATE_RECORD_ID"}


def test_duplicate_json_keys_fail_closed() -> None:
    script = REPO_ROOT / "tools/validators/governance/validate_implementation_decision_record.py"
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "duplicate.json"
        path.write_text('{"schema_version":"1.0.0","schema_version":"1.0.0"}', encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(script), str(path)],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    assert result.returncode == EXIT_ERROR
    assert json.loads(result.stdout)["findings"][0]["code"] == "INPUT_JSON_INVALID"


def test_hold_cli_uses_exit_three() -> None:
    record = _cases()["hold-draft-without-validation"]
    script = REPO_ROOT / "tools/validators/governance/validate_implementation_decision_record.py"
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "hold.json"
        path.write_text(json.dumps(record), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(script), str(path)],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    assert result.returncode == EXIT_HOLD
    assert json.loads(result.stdout)["outcome"] == "HOLD"


def test_fixture_suite_is_no_network() -> None:
    with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
        ok, payload = run_fixture_suite()
    assert ok, payload


def test_cases_cli_output_is_deterministic() -> None:
    script = REPO_ROOT / "tools/validators/governance/validate_implementation_decision_record.py"
    env = dict(os.environ)
    env["KFM_NO_NETWORK"] = "1"
    command = [sys.executable, str(script), "--cases"]
    first = subprocess.run(command, cwd=REPO_ROOT, env=env, check=False, capture_output=True, text=True)
    second = subprocess.run(command, cwd=REPO_ROOT, env=env, check=False, capture_output=True, text=True)
    assert first.returncode == second.returncode == 0
    assert first.stdout == second.stdout
