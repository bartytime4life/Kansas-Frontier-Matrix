from __future__ import annotations

import importlib.util
from datetime import datetime, timezone
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = (
    ROOT
    / "tools"
    / "validators"
    / "repository_control"
    / "check_currentness.py"
)
SPEC = importlib.util.spec_from_file_location(
    "repository_control_currentness", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

SHA_A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
SHA_B = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"


def projection(*, status: str = "CONFIRMED", sha: str = SHA_A) -> dict[str, object]:
    return {
        "projection_status": status,
        "base": {
            "current_main_sha": sha,
            "observed_at": "2026-09-21T00:00:00Z",
        },
    }


def test_matching_confirmed_projection_is_current() -> None:
    MODULE.check_currentness(
        projection(),
        observed_main_sha=SHA_A,
        max_age_days=1,
        now=datetime(2026, 9, 21, 12, tzinfo=timezone.utc),
    )


def test_other_main_head_is_stale() -> None:
    with pytest.raises(MODULE.CurrentnessError, match="STALE_MAIN"):
        MODULE.check_currentness(projection(), observed_main_sha=SHA_B)


def test_superseded_projection_cannot_be_reactivated_by_matching_sha() -> None:
    with pytest.raises(MODULE.CurrentnessError, match="PROJECTION_SUPERSEDED"):
        MODULE.check_currentness(
            projection(status="SUPERSEDED"), observed_main_sha=SHA_A
        )


def test_age_limit_is_fail_closed() -> None:
    with pytest.raises(MODULE.CurrentnessError, match="STALE_AGE"):
        MODULE.check_currentness(
            projection(),
            observed_main_sha=SHA_A,
            max_age_days=1,
            now=datetime(2026, 9, 23, tzinfo=timezone.utc),
        )
