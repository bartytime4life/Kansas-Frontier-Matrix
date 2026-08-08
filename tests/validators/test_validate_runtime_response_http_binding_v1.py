from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = ROOT / "tools/validators/runtime/validate_runtime_response_http_binding_v1.py"
VALID_FIXTURE = ROOT / "fixtures/contracts/v1/runtime/runtime_response_http_binding_v1/valid/answer.json"
INVALID_FIXTURE = ROOT / "fixtures/contracts/v1/runtime/runtime_response_http_binding_v1/invalid/abstain_as_deny.json"

SPEC = importlib.util.spec_from_file_location("runtime_http_binding", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def base(status: int, outcome: str, failure: str) -> dict[str, object]:
    return {
        "object_type": "RuntimeResponseHttpBinding",
        "profile_version": "v1",
        "http_status": status,
        "outcome": outcome,
        "failure_class": failure,
        "envelope_body_required": True,
        "governance": MODULE._authority(),
    }


def test_all_v1_mappings_pass() -> None:
    cases = [
        (200, "ANSWER", "NONE"),
        (403, "DENY", "POLICY_OR_GOVERNANCE_DENIAL"),
        (422, "ABSTAIN", "INSUFFICIENT_EVIDENCE_OR_CONTEXT"),
        (500, "ERROR", "INTERNAL_RUNTIME_FAILURE"),
        (503, "ERROR", "DEPENDENCY_UNAVAILABLE"),
    ]
    for status, outcome, failure in cases:
        result = MODULE.validate_payload(base(status, outcome, failure))
        assert result["status"] == "PASS"
        assert result["findings"] == []
        assert all(value is False for value in result["authority"].values())


def test_abstain_cannot_be_collapsed_to_deny() -> None:
    value = json.loads(INVALID_FIXTURE.read_text(encoding="utf-8"))
    result = MODULE.validate_payload(value)
    assert result["status"] == "DENY"
    assert {item["code"] for item in result["findings"]} == {"HTTP_OUTCOME_MISMATCH"}


def test_bare_status_semantics_cannot_be_claimed() -> None:
    value = base(200, "ANSWER", "NONE")
    value["envelope_body_required"] = False
    result = MODULE.validate_payload(value)
    assert result["status"] == "ERROR"
    assert {item["code"] for item in result["findings"]} == {"SCHEMA_INVALID"}


def test_authority_overclaim_fails_schema() -> None:
    value = base(403, "DENY", "POLICY_OR_GOVERNANCE_DENIAL")
    value["governance"]["publication_authorized"] = True
    result = MODULE.validate_payload(value)
    assert result["status"] == "ERROR"


def test_valid_fixture_passes() -> None:
    value = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
    assert MODULE.validate_payload(value)["status"] == "PASS"
