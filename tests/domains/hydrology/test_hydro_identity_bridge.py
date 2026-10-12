from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/domains/hydrology/validate_hydro_identity_bridge.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/hydrology/hydro_identity_bridge.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/domains/hydrology/hydro_identity_bridge"

spec = importlib.util.spec_from_file_location("validate_hydro_identity_bridge", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


@pytest.mark.parametrize(
    ("name", "packet_outcome"),
    [
        ("exact_answer", "ANSWER"),
        ("legacy_relabel_denied", "DENY"),
        ("merge_abstain", "ABSTAIN"),
        ("operational_error", "ERROR"),
        ("split_abstain", "ABSTAIN"),
        ("unresolved_abstain", "ABSTAIN"),
    ],
)
def test_valid_finite_outcomes(name: str, packet_outcome: str) -> None:
    result = validator.validate_file(FIXTURES / "valid" / f"{name}.json")
    assert result.ok, result.findings
    assert result.packet_outcome == packet_outcome
    assert not result.operational_error


@pytest.mark.parametrize(
    ("name", "code"),
    [
        ("answer_with_split", "OUTCOME_RELATIONSHIP_MISMATCH"),
        ("answer_without_join_receipt", "ANSWER_JOIN_RECEIPT_REQUIRED"),
        ("crosswalk_release_mismatch", "CROSSWALK_RELEASE_BASIS_MISMATCH"),
        ("noncanonical_evidence_refs", "EVIDENCE_REFS_NOT_CANONICAL"),
        ("relabel_not_denied", "LEGACY_ID_RELABEL_NOT_DENIED"),
        ("request_not_bound", "REQUEST_NOT_BOUND_TO_LEGACY_ID"),
        ("spec_hash_mismatch", "SPEC_HASH_MISMATCH"),
    ],
)
def test_invalid_packets_fail_closed(name: str, code: str) -> None:
    result = validator.validate_file(FIXTURES / "invalid" / f"{name}.json")
    assert not result.ok
    assert code in {item.code for item in result.findings}
    assert not result.operational_error


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)


def test_identity_is_stable_across_mapping_key_order() -> None:
    payload = json.loads((FIXTURES / "valid/exact_answer.json").read_text(encoding="utf-8"))
    reordered = {key: payload[key] for key in reversed(list(payload))}
    assert validator.canonical_spec_hash(reordered) == payload["spec_hash"]
    assert validator.expected_bridge_id(reordered) == payload["bridge_id"]


def test_unknown_member_is_denied_by_schema() -> None:
    payload = json.loads((FIXTURES / "valid/exact_answer.json").read_text(encoding="utf-8"))
    payload["unexpected"] = True
    result = validator.validate_payload(payload)
    assert not result.ok
    assert "SCHEMA_INVALID" in {item.code for item in result.findings}


def test_duplicate_key_is_operational_error(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.json"
    path.write_text('{"bridge_id":"a","bridge_id":"b"}', encoding="utf-8")
    result = validator.validate_file(path)
    assert result.operational_error
    assert result.findings == (validator.Finding("JSON_DUPLICATE_KEY", "/"),)


def test_nonfinite_number_is_operational_error(tmp_path: Path) -> None:
    path = tmp_path / "nonfinite.json"
    path.write_text('{"value":NaN}', encoding="utf-8")
    result = validator.validate_file(path)
    assert result.operational_error
    assert result.findings == (validator.Finding("JSON_NONFINITE_NUMBER", "/"),)


def test_symlink_input_is_denied(tmp_path: Path) -> None:
    target = tmp_path / "target.json"
    target.write_text("{}", encoding="utf-8")
    link = tmp_path / "link.json"
    link.symlink_to(target)
    result = validator.validate_file(link)
    assert result.operational_error
    assert result.findings == (validator.Finding("INPUT_SYMLINK_DENIED", "/"),)


def test_validator_has_no_network_client_import() -> None:
    source = VALIDATOR_PATH.read_text(encoding="utf-8")
    forbidden = ("import requests", "import httpx", "import aiohttp", "import socket", "from urllib")
    assert not any(token in source for token in forbidden)


def test_cli_emits_bounded_answer_for_valid_packet() -> None:
    completed = subprocess.run(
        [sys.executable, str(VALIDATOR_PATH), str(FIXTURES / "valid/exact_answer.json")],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    payload = json.loads(completed.stdout)
    assert payload["outcome"] == "PASS"
    assert payload["packet_outcome"] == "ANSWER"
    assert payload["findings"] == []
    assert set(payload["authority"].values()) == {False}


def test_cli_returns_fail_for_contradictory_packet() -> None:
    completed = subprocess.run(
        [sys.executable, str(VALIDATOR_PATH), str(FIXTURES / "invalid/relabel_not_denied.json")],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 1
    payload = json.loads(completed.stdout)
    assert payload["outcome"] == "FAIL"
    assert any(item["code"] == "LEGACY_ID_RELABEL_NOT_DENIED" for item in payload["findings"])
