"""Tests for the no-network vegetation connectivity gate validator."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import socket
import sys
from unittest import mock

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[5]
MODULE_PATH = REPO_ROOT / (
    "tools/validators/domains/agriculture/vegetation_connectivity_gate/"
    "validate_connectivity_gate.py"
)
FIXTURE_PATH = REPO_ROOT / "fixtures/domains/agriculture/vegetation_connectivity_gate/cases.json"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/agriculture/vegetation_connectivity_gate.schema.json"

SPEC = importlib.util.spec_from_file_location("kfm_vegetation_connectivity_gate", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _manifest() -> dict[str, object]:
    value = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _case(case_id: str) -> dict[str, object]:
    manifest = _manifest()
    selected = next(case for case in manifest["cases"] if case["case_id"] == case_id)
    return MODULE.materialize_case(manifest, selected)


def test_schema_is_valid_draft_2020_12() -> None:
    Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))


def test_fixture_manifest_has_exact_polarity() -> None:
    cases = _manifest()["cases"]
    assert len(cases) == 11
    assert sum(case["expected_outcome"] == "PASS" for case in cases) == 3
    assert sum(case["expected_outcome"] == "DENY" for case in cases) == 8


def test_candidate_and_hold_are_valid_contract_states() -> None:
    candidate = MODULE.validate_payload(_case("valid_candidate"))
    hold = MODULE.validate_payload(_case("valid_hold_area_threshold"))
    assert candidate.ok
    assert hold.ok
    assert _case("valid_candidate")["outcome"]["status"] == "PROPOSED_INDICATOR_CANDIDATE"
    assert _case("valid_hold_area_threshold")["outcome"]["status"] == "HOLD"


def test_threshold_equality_is_inclusive() -> None:
    payload = _case("valid_candidate")
    payload["components"][0]["area_m2"] = payload["thresholds"]["min_component_area_m2"]
    payload["components"][0]["present_observation_ids"] = ["obs-2026-08-01", "obs-2026-08-08"]
    payload["components"][0]["persistence_basis_points"] = 6667
    payload["components"][0]["qualifies"] = True
    payload["summary"] = {
        "component_count": 2,
        "qualifying_component_count": 1,
        "qualifying_area_m2": 250000,
        "largest_qualifying_component_area_m2": 250000,
    }
    subject = {key: value for key, value in payload.items() if key != "spec_hash"}
    payload["spec_hash"] = MODULE.compute_spec_hash(subject)
    assert MODULE.validate_payload(payload).ok


def test_persistence_is_derived_from_observation_membership() -> None:
    result = MODULE.validate_payload(_case("invalid_component_persistence"))
    assert result.findings == (
        MODULE.Finding("COMPONENT_PERSISTENCE_MISMATCH", "/components/0/persistence_basis_points"),
    )


def test_summary_and_decision_are_recomputed() -> None:
    summary = MODULE.validate_payload(_case("invalid_summary"))
    decision = MODULE.validate_payload(_case("invalid_decision"))
    assert summary.findings == (MODULE.Finding("SUMMARY_MISMATCH", "/summary"),)
    assert decision.findings == (
        MODULE.Finding("DECISION_OUTCOME_MISMATCH", "/outcome/status"),
        MODULE.Finding("DECISION_REASONS_MISMATCH", "/outcome/reasons"),
    )


def test_fixture_runner_is_exact_and_repeatable() -> None:
    assert MODULE.run_fixtures() == 0
    assert MODULE.run_fixtures() == 0


def test_spec_hash_is_stable() -> None:
    payload = _case("valid_candidate")
    subject = {key: value for key, value in payload.items() if key != "spec_hash"}
    assert payload["spec_hash"] == MODULE.compute_spec_hash(subject)
    assert payload["spec_hash"] == MODULE.compute_spec_hash(subject)


def test_validator_does_not_open_network() -> None:
    def denied(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("network access denied")

    with mock.patch.object(socket, "socket", denied), mock.patch.object(
        socket, "create_connection", denied
    ), mock.patch.object(socket, "getaddrinfo", denied):
        assert MODULE.validate_payload(_case("valid_candidate")).ok
        assert MODULE.run_fixtures() == 0


def test_governance_authority_is_schema_denied() -> None:
    result = MODULE.validate_payload(_case("invalid_governance_authority"))
    assert result.findings == (
        MODULE.Finding("SCHEMA_INVALID", "/governance/network_allowed"),
    )
