#!/usr/bin/env python3
"""Regression tests for public-safe FlowObservation aggregation semantics."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import Finding  # noqa: E402
from tools.validators.domains.hydrology.validate_public_safe_flow_fixture import (  # noqa: E402
    validate_candidate,
)


VALID_FIXTURE = (
    REPO_ROOT
    / "fixtures/domains/hydrology/public_safe_flow/valid/public_safe_flow.json"
)


def _candidate() -> dict[str, object]:
    return json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))


def test_public_safe_flow_profile_is_explicitly_instantaneous() -> None:
    candidate = _candidate()
    assert candidate["temporal_scope"]["aggregation_window"] == "instant"  # type: ignore[index]
    assert validate_candidate(candidate) == []


@pytest.mark.parametrize(
    "value",
    ["daily_mean", "period_statistic", "forecast", "", None, 60],
)
def test_noninstant_aggregation_windows_fail_closed(value: object) -> None:
    candidate = copy.deepcopy(_candidate())
    candidate["temporal_scope"]["aggregation_window"] = value  # type: ignore[index]
    assert Finding(
        "AGGREGATION_WINDOW_INVALID", "$.temporal_scope.aggregation_window"
    ) in validate_candidate(candidate)


def test_missing_aggregation_window_fails_closed() -> None:
    candidate = copy.deepcopy(_candidate())
    candidate["temporal_scope"].pop("aggregation_window")  # type: ignore[index]
    assert Finding(
        "AGGREGATION_WINDOW_INVALID", "$.temporal_scope.aggregation_window"
    ) in validate_candidate(candidate)
