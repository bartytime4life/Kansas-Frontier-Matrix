from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from tools.validators.domains.geology.validate_production_material_change import (
    Finding,
    REPO_ROOT,
    SCHEMA_PATH,
    canonical_spec_hash,
    expected_assessment_id,
    validate_file,
    validate_payload,
)

FIXTURES = (
    REPO_ROOT
    / "fixtures/contracts/v1/domains/geology/production_material_change"
)
VALID = FIXTURES / "valid"
INVALID = FIXTURES / "invalid"
VALIDATOR = (
    REPO_ROOT
    / "tools/validators/domains/geology/validate_production_material_change.py"
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
    assert packet["assessment_id"] == expected_assessment_id(packet)


def test_valid_outcomes_cover_finite_watcher_states() -> None:
    outcomes = {
        json.loads(path.read_text(encoding="utf-8"))["assessment"]["outcome"]
        for path in _paths(VALID)
    }
    assert outcomes == {"NO_CHANGE", "REVIEW", "HOLD", "ERROR"}


def test_material_change_dimensions_are_exact() -> None:
    packet = json.loads(
        (VALID / "material_change_review.json").read_text(encoding="utf-8")
    )
    assert packet["assessment"]["change_dimensions"] == [
        "COVERAGE_END",
        "FOOTPRINT_DIGEST",
        "MANIFEST_DIGEST",
        "RECORD_COUNT",
    ]


def test_retrieval_time_regression_requires_hold() -> None:
    packet = json.loads(
        (VALID / "material_change_review.json").read_text(encoding="utf-8")
    )
    packet["current_snapshot"]["retrieved_at"] = "2026-03-31T12:00:00Z"
    packet["spec_hash"] = canonical_spec_hash(packet)
    packet["assessment_id"] = expected_assessment_id(packet)

    result = validate_payload(packet)
    assert Finding(
        "RETRIEVAL_TIME_REGRESSION_REQUIRES_HOLD",
        "/assessment/outcome",
    ) in result.findings

    packet["assessment"].update(
        outcome="HOLD",
        material_change=None,
        change_dimensions=[],
        reason_codes=["RETRIEVAL_TIME_REGRESSION"],
    )
    packet["spec_hash"] = canonical_spec_hash(packet)
    packet["assessment_id"] = expected_assessment_id(packet)
    result = validate_payload(packet)
    assert result.ok, result.findings

    packet["current_snapshot"]["rights_state"] = "UNKNOWN"
    packet["assessment"]["reason_codes"] = ["RIGHTS_STATE_UNRESOLVED"]
    packet["spec_hash"] = canonical_spec_hash(packet)
    packet["assessment_id"] = expected_assessment_id(packet)
    result = validate_payload(packet)
    assert result.findings == (
        Finding(
            "RETRIEVAL_TIME_REGRESSION_REASON_REQUIRED",
            "/assessment/reason_codes",
        ),
    )

    packet["assessment"]["reason_codes"] = [
        "RETRIEVAL_TIME_REGRESSION",
        "RIGHTS_STATE_UNRESOLVED",
    ]
    packet["spec_hash"] = canonical_spec_hash(packet)
    packet["assessment_id"] = expected_assessment_id(packet)
    result = validate_payload(packet)
    assert result.ok, result.findings


def test_operational_error_cannot_conceal_retrieval_time_regression() -> None:
    packet = json.loads(
        (VALID / "operational_error.json").read_text(encoding="utf-8")
    )
    packet["prior_snapshot"] = packet["current_snapshot"].copy()
    packet["prior_snapshot"]["snapshot_ref"] = "kgs-production-snapshot-prior"
    packet["prior_snapshot"]["retrieved_at"] = "2026-05-01T12:00:00Z"
    packet["current_snapshot"]["retrieved_at"] = "2026-04-30T12:00:00Z"
    packet["assessment"]["evidence_refs"] = sorted(
        set(packet["assessment"]["evidence_refs"])
        | set(packet["prior_snapshot"]["evidence_refs"])
    )
    packet["spec_hash"] = canonical_spec_hash(packet)
    packet["assessment_id"] = expected_assessment_id(packet)

    result = validate_payload(packet)
    assert result.findings == (
        Finding(
            "RETRIEVAL_TIME_REGRESSION_REQUIRES_HOLD",
            "/assessment/outcome",
        ),
    )


@pytest.mark.parametrize(
    ("fixture", "concealing_reason", "expected_finding"),
    (
        (
            "prior_missing_hold.json",
            "RIGHTS_STATE_UNRESOLVED",
            Finding("PRIOR_SNAPSHOT_REASON_REQUIRED", "/assessment/reason_codes"),
        ),
        (
            "rights_unresolved_hold.json",
            "PRIOR_SNAPSHOT_MISSING",
            Finding("RIGHTS_STATE_REASON_REQUIRED", "/assessment/reason_codes"),
        ),
        (
            "coverage_regression_hold.json",
            "RIGHTS_STATE_UNRESOLVED",
            Finding(
                "COVERAGE_REGRESSION_REASON_REQUIRED",
                "/assessment/reason_codes",
            ),
        ),
    ),
)
def test_hold_requires_every_applicable_blocker_reason(
    fixture: str,
    concealing_reason: str,
    expected_finding: Finding,
) -> None:
    packet = json.loads((VALID / fixture).read_text(encoding="utf-8"))
    packet["current_snapshot"]["rights_state"] = "UNKNOWN"
    packet["assessment"]["reason_codes"] = [concealing_reason]
    packet["spec_hash"] = canonical_spec_hash(packet)
    packet["assessment_id"] = expected_assessment_id(packet)

    result = validate_payload(packet)
    assert expected_finding in result.findings


def test_cli_returns_zero_for_valid_fixture() -> None:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(VALID / "material_change_review.json")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    payload = json.loads(proc.stdout)
    assert proc.returncode == 0
    assert payload["outcome"] == "PASS"
    assert payload["packet_outcome"] == "REVIEW"
    assert payload["authority"]["network_fetch"] is False
    assert payload["authority"]["publication"] is False


def test_cli_returns_one_for_semantic_failure() -> None:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(INVALID / "change_dimensions_mismatch.json")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    payload = json.loads(proc.stdout)
    assert proc.returncode == 1
    assert payload["outcome"] == "FAIL"
    assert any(item["code"] == "CHANGE_DIMENSIONS_MISMATCH" for item in payload["findings"])


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
