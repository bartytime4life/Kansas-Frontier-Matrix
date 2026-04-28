from __future__ import annotations

import json
from pathlib import Path

import pytest


RUNTIME_PARITY_DIR = Path(__file__).resolve().parent
FIXTURES_DIR = RUNTIME_PARITY_DIR / "fixtures"
EXPECTED_DIR = RUNTIME_PARITY_DIR / "expected"

FINITE_OUTCOMES = {"ANSWER", "ABSTAIN", "DENY", "ERROR"}
ALLOWED_EVIDENCE_STATES = {"resolved", "missing", "unknown", "stale", "restricted"}


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _case_ids() -> list[str]:
    return sorted(path.name.replace(".input.json", "") for path in FIXTURES_DIR.glob("*.input.json"))


@pytest.mark.parametrize("case_id", _case_ids())
def test_runtime_parity_case_shapes(case_id: str) -> None:
    fixture = _load_json(FIXTURES_DIR / f"{case_id}.input.json")
    expected = _load_json(EXPECTED_DIR / f"{case_id}.runtime_response.json")

    assert fixture["case_id"] == case_id
    assert fixture["expected_runtime_outcome"] in FINITE_OUTCOMES
    assert fixture["evidence_state"] in ALLOWED_EVIDENCE_STATES
    assert "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json" in fixture["contract_refs"]

    assert expected["kind"] == "RuntimeResponseEnvelope"
    assert expected["outcome"] == fixture["expected_runtime_outcome"]
    assert set(fixture["reason_codes"]).issubset(set(expected["reason_codes"]))
    assert set(fixture["obligation_codes"]).issubset(set(expected["obligation_codes"]))
    assert expected["audit_ref"].startswith(f"audit:runtime_parity:{case_id}")


def test_runtime_parity_fixture_expected_file_sets_match() -> None:
    fixture_case_ids = {path.name.replace(".input.json", "") for path in FIXTURES_DIR.glob("*.input.json")}
    expected_case_ids = {path.name.replace(".runtime_response.json", "") for path in EXPECTED_DIR.glob("*.runtime_response.json")}

    assert fixture_case_ids == expected_case_ids
