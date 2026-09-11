from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/domains/hydrology/validate_living_waters_fixture_packet.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/hydrology/living_waters_fixture_packet.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/domains/hydrology/living_waters_fixture_packet"

spec = importlib.util.spec_from_file_location("validate_living_waters_fixture_packet", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


def _valid() -> dict[str, object]:
    return json.loads((FIXTURES / "valid/first_proof.json").read_text(encoding="utf-8"))


def test_schema_and_valid_fixture() -> None:
    Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))
    assert validator.validate_file(FIXTURES / "valid/first_proof.json") == ()


def test_ambiguous_reach_join_must_abstain() -> None:
    findings = validator.validate_file(FIXTURES / "invalid/ambiguous_join_answered.json")
    assert validator.Finding("SCENARIO_OUTCOME_INVALID", "/scenarios/ambiguous-reach") in findings


def test_finite_states_are_complete_and_distinct() -> None:
    payload = _valid()
    scenarios = {item["id"]: item for item in payload["scenarios"]}  # type: ignore[index]
    assert {item["state"] for item in scenarios.values()} == {"AVAILABLE", "STALE", "NO_RESULTS", "UNAVAILABLE", "ABSTAIN"}
    assert scenarios["no-results"]["state"] != scenarios["unavailable"]["state"]


def test_parameter_statistic_unit_and_qualifier_are_exact() -> None:
    mutations = {"parameter_code": "00065", "statistic_code": "00003", "unit_code": "m3/s", "qualifier_code": "A"}
    for field, value in mutations.items():
        payload = copy.deepcopy(_valid())
        payload["series"][field] = value  # type: ignore[index]
        assert validator.Finding("SCHEMA_INVALID", f"/series/{field}") in validator.validate_payload(payload)


def test_governance_cannot_claim_forbidden_effects() -> None:
    for field in ("source_admitted", "source_activated", "policy_evaluated", "released", "deployed", "published"):
        payload = copy.deepcopy(_valid())
        payload["governance"][field] = True  # type: ignore[index]
        assert validator.Finding("SCHEMA_INVALID", f"/governance/{field}") in validator.validate_payload(payload)


def test_hydrograph_times_are_strictly_ordered() -> None:
    payload = copy.deepcopy(_valid())
    payload["series"]["points"].reverse()  # type: ignore[index]
    assert validator.Finding("HYDROGRAPH_TIME_ORDER_INVALID", "/series/points") in validator.validate_payload(payload)


def test_validator_has_no_network_client_import() -> None:
    source = VALIDATOR_PATH.read_text(encoding="utf-8")
    assert not any(token in source for token in ("import requests", "import httpx", "import socket", "from urllib"))


def test_cli_receipt_is_explicitly_non_authorizing() -> None:
    result = subprocess.run([sys.executable, str(VALIDATOR_PATH), str(FIXTURES / "valid/first_proof.json")], cwd=REPO_ROOT, text=True, capture_output=True, check=False)
    assert result.returncode == 0
    receipt = json.loads(result.stdout)
    assert receipt["outcome"] == "PASS"
    assert set(receipt["authority"].values()) == {False}
