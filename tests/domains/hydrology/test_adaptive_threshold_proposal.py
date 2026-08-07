from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from tools.validators.domains.hydrology.validate_adaptive_threshold_proposal import (
    REPO_ROOT,
    SCHEMA_PATH,
    canonical_spec_hash,
    expected_proposal_id,
    validate_file,
)

FIXTURES = (
    REPO_ROOT
    / "fixtures/contracts/v1/domains/hydrology/adaptive_threshold_proposal"
)
VALID = FIXTURES / "valid"
INVALID = FIXTURES / "invalid"
VALIDATOR = (
    REPO_ROOT
    / "tools/validators/domains/hydrology/validate_adaptive_threshold_proposal.py"
)


def _paths(directory: Path) -> list[Path]:
    return sorted(directory.glob("*.json"))


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)


@pytest.mark.parametrize("path", _paths(VALID), ids=lambda path: path.name)
def test_valid_fixtures_pass(path: Path) -> None:
    result = validate_file(path)
    assert result.ok, result.findings


@pytest.mark.parametrize("path", _paths(INVALID), ids=lambda path: path.name)
def test_invalid_fixtures_fail_closed(path: Path) -> None:
    result = validate_file(path)
    assert not result.ok
    assert result.findings


@pytest.mark.parametrize("path", _paths(VALID), ids=lambda path: path.name)
def test_valid_fixtures_are_deterministically_bound(path: Path) -> None:
    packet = json.loads(path.read_text(encoding="utf-8"))
    assert packet["spec_hash"] == canonical_spec_hash(packet)
    assert packet["proposal_id"] == expected_proposal_id(packet)


def test_valid_outcomes_cover_review_states() -> None:
    outcomes = {
        json.loads(path.read_text(encoding="utf-8"))["assessment"]["outcome"]
        for path in _paths(VALID)
    }
    assert outcomes == {
        "KEEP_BASELINE",
        "REVIEW_RECALIBRATION",
        "HOLD",
        "ERROR",
    }


def test_proposal_never_carries_exact_threshold() -> None:
    for path in _paths(VALID):
        packet = json.loads(path.read_text(encoding="utf-8"))
        assert "recommended_threshold" not in packet["assessment"]
        assert packet["governance"]["exact_threshold_proposed"] is False
        assert packet["governance"]["configuration_mutated"] is False


def test_cli_returns_zero_for_valid_fixture() -> None:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(VALID / "review_recalibration.json")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    payload = json.loads(proc.stdout)
    assert proc.returncode == 0
    assert payload["outcome"] == "PASS"
    assert payload["packet_outcome"] == "REVIEW_RECALIBRATION"
    assert payload["authority"]["network_fetch"] is False
    assert payload["authority"]["threshold_computation"] is False
    assert payload["authority"]["configuration_mutation"] is False
    assert payload["authority"]["publication"] is False


def test_cli_returns_one_for_semantic_failure() -> None:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(INVALID / "review_without_baseline.json")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    payload = json.loads(proc.stdout)
    assert proc.returncode == 1
    assert payload["outcome"] == "FAIL"
    assert any(item["code"] == "REVIEW_REQUIRES_BASELINE" for item in payload["findings"])


def test_cli_returns_two_for_missing_input() -> None:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURES / "missing.json")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    payload = json.loads(proc.stdout)
    assert proc.returncode == 2
    assert payload["outcome"] == "ERROR"
    assert payload["findings"] == [{"code": "FILE_NOT_FOUND", "field": "/"}]
