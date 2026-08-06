"""Deterministic tests for the inactive Soil time-caveat profile."""

from __future__ import annotations

import copy
import hashlib
import json
import socket
import subprocess
import sys
from pathlib import Path

import pytest

from tools.validators.domains.soil.time_caveat.validate_time_caveat_profile import (
    PROFILE_PATH,
    REPO_ROOT,
    assess_candidate,
    validate_path,
    validate_profile,
)


FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/soil/time_caveat"


def _load(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_profile_hash_and_governance_are_closed() -> None:
    profile = _load(PROFILE_PATH)
    canonical = json.dumps(
        {key: value for key, value in profile.items() if key != "spec_hash"},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")

    assert profile["spec_hash"] == "sha256:" + hashlib.sha256(canonical).hexdigest()
    assert validate_profile(profile) == ()
    assert profile["status"] == "PROPOSED_INACTIVE"
    assert set(profile["governance"].values()) == {False, None}


@pytest.mark.parametrize(
    ("lane", "name", "expected"),
    [
        ("pass", "static_survey.json", "PASS"),
        ("pass", "fresh_station.json", "PASS"),
        ("hold", "stale_station.json", "HOLD"),
        ("deny", "static_as_current.json", "DENY"),
        ("deny", "satellite_as_station.json", "DENY"),
        ("error", "missing_evaluated_at.json", "ERROR"),
    ],
)
def test_fixture_outcomes_are_exact(
    lane: str, name: str, expected: str
) -> None:
    result = validate_path(FIXTURE_ROOT / lane / name)
    assert result.outcome == expected


def test_assessment_is_replay_deterministic_and_does_not_mutate() -> None:
    profile = _load(PROFILE_PATH)
    candidate = _load(FIXTURE_ROOT / "pass/fresh_station.json")
    snapshot = copy.deepcopy(candidate)

    first = assess_candidate(candidate, profile)
    second = assess_candidate(candidate, profile)

    assert first == second
    assert candidate == snapshot


def test_missing_required_observation_time_holds() -> None:
    profile = _load(PROFILE_PATH)
    candidate = _load(FIXTURE_ROOT / "pass/fresh_station.json")
    candidate["time_basis"]["observed_at"] = None

    result = assess_candidate(candidate, profile)

    assert result.outcome == "HOLD"
    assert "TIME_AXIS_REQUIRED" in {finding.code for finding in result.findings}


def test_source_role_mismatch_denies() -> None:
    profile = _load(PROFILE_PATH)
    candidate = _load(FIXTURE_ROOT / "pass/fresh_station.json")
    candidate["source_role"] = "satellite_grid_measurement"

    result = assess_candidate(candidate, profile)

    assert result.outcome == "DENY"
    assert "SOURCE_ROLE_MISMATCH" in {
        finding.code for finding in result.findings
    }


def test_governance_authority_claim_denies_before_schema_error() -> None:
    profile = _load(PROFILE_PATH)
    candidate = _load(FIXTURE_ROOT / "pass/fresh_station.json")
    candidate["governance"]["release_authorized"] = True

    result = assess_candidate(candidate, profile)

    assert result.outcome == "DENY"
    assert [finding.code for finding in result.findings] == [
        "GOVERNANCE_AUTHORITY_CLAIM"
    ]


def test_reversed_validity_window_denies() -> None:
    profile = _load(PROFILE_PATH)
    candidate = _load(FIXTURE_ROOT / "deny/satellite_as_station.json")
    candidate["claim_kind"] = "satellite_grid_condition"
    candidate["time_basis"]["valid_from"] = "2026-04-15T13:00:00Z"
    candidate["time_basis"]["valid_to"] = "2026-04-15T11:00:00Z"

    result = assess_candidate(candidate, profile)

    assert result.outcome == "DENY"
    assert "TIME_ORDER_INVALID" in {finding.code for finding in result.findings}


def test_profile_validation_performs_no_network(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def denied(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("network access is not allowed")

    monkeypatch.setattr(socket, "socket", denied)
    result = validate_path(FIXTURE_ROOT / "pass/fresh_station.json")
    assert result.outcome == "PASS"


def test_fixture_cli_reports_all_four_outcomes() -> None:
    command = [
        sys.executable,
        str(
            REPO_ROOT
            / "tools/validators/domains/soil/time_caveat/"
            "validate_time_caveat_profile.py"
        ),
        "--fixtures",
    ]
    completed = subprocess.run(
        command,
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
    )

    assert completed.returncode == 0, completed.stderr
    report = json.loads(completed.stdout)
    assert report["outcome"] == "PASS"
    assert report["cases"] == 6
    assert report["counts"] == {
        "DENY": 2,
        "ERROR": 1,
        "HOLD": 1,
        "PASS": 2,
    }
    assert report["authority"] == "NONE"
