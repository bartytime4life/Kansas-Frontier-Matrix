from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[4]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/governance/validate_governed_run_chain.py"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/governance/governed_run_chain"

spec = importlib.util.spec_from_file_location("validate_governed_run_chain", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


@pytest.mark.parametrize("name", ["promotable", "quarantined", "held", "error"])
def test_valid_outcomes(name: str) -> None:
    result = validator.validate_file(FIXTURES / "valid" / f"{name}.json")
    assert result.ok, result.findings
    assert not result.operational_error


@pytest.mark.parametrize(
    ("name", "code"),
    [
        ("spec_hash_mismatch", "QUARANTINE_SPEC_HASH_MISMATCH"),
        ("promotion_bypasses_quarantine", "OUTCOME_PROMOTION_FORBIDDEN"),
    ],
)
def test_invalid_linkage_fails_closed(name: str, code: str) -> None:
    result = validator.validate_file(FIXTURES / "invalid" / f"{name}.json")
    assert not result.ok
    assert code in {finding.code for finding in result.findings}
    assert not result.operational_error


def test_policy_family_must_be_promotion() -> None:
    payload = json.loads((FIXTURES / "valid" / "promotable.json").read_text())
    payload["policy_decision"]["policy_family"] = "access"
    result = validator.validate_payload(payload)
    assert "POLICY_FAMILY_NOT_PROMOTION" in {f.code for f in result.findings}


def test_unknown_member_is_denied_by_schema() -> None:
    payload = json.loads((FIXTURES / "valid" / "promotable.json").read_text())
    payload["unexpected"] = True
    result = validator.validate_payload(payload)
    assert not result.ok
    assert "SCHEMA_INVALID" in {f.code for f in result.findings}


def test_duplicate_json_key_is_operational_error(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.json"
    path.write_text('{"chain_id":"a","chain_id":"b"}', encoding="utf-8")
    result = validator.validate_file(path)
    assert not result.ok
    assert result.operational_error
    assert result.findings[0].code == "JSON_DUPLICATE_KEY"


def test_nonfinite_json_number_is_operational_error(tmp_path: Path) -> None:
    path = tmp_path / "nonfinite.json"
    path.write_text('{"value":NaN}', encoding="utf-8")
    result = validator.validate_file(path)
    assert not result.ok
    assert result.operational_error
    assert result.findings[0].code == "JSON_NONFINITE_NUMBER"


def test_cli_emits_finite_no_network_result() -> None:
    completed = subprocess.run(
        [sys.executable, str(VALIDATOR_PATH), str(FIXTURES / "valid" / "promotable.json")],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    payload = json.loads(completed.stdout)
    assert payload["outcome"] == "ANSWER"
    assert payload["authority"] == {
        "lifecycle_write": False,
        "network_fetch": False,
        "policy_evaluation": False,
        "promotion": False,
        "publication": False,
        "release": False,
        "source_activation": False,
    }


def test_cli_invalid_chain_returns_deny() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(VALIDATOR_PATH),
            str(FIXTURES / "invalid" / "promotion_bypasses_quarantine.json"),
        ],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 1
    payload = json.loads(completed.stdout)
    assert payload["outcome"] == "DENY"
