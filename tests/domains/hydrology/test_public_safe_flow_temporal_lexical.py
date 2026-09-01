#!/usr/bin/env python3
"""Regression tests for canonical public-safe Hydrology UTC timestamps."""

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


@pytest.mark.parametrize(
    "value",
    [
        "2026-08-02T12:00:00.000Z",
        "2026-08-02 12:00:00Z",
        "2026-W31-7T12:00:00Z",
        "20260802T120000Z",
        "2026-08-02T12:00Z",
        "2026-08-02T12:00:60Z",
    ],
)
def test_observed_at_requires_canonical_whole_second_utc(value: str) -> None:
    candidate = copy.deepcopy(_candidate())
    candidate["temporal_scope"]["observed_at"] = value  # type: ignore[index]
    assert Finding(
        "OBSERVED_TIME_INVALID", "$.temporal_scope.observed_at"
    ) in validate_candidate(candidate)


@pytest.mark.parametrize(
    "value",
    [
        "2026-08-02T12:05:00.000Z",
        "2026-08-02 12:05:00Z",
        "2026-W31-7T12:05:00Z",
        "20260802T120500Z",
        "2026-08-02T12:05Z",
        "2026-08-02T12:05:60Z",
    ],
)
def test_retrieved_at_requires_canonical_whole_second_utc(value: str) -> None:
    candidate = copy.deepcopy(_candidate())
    candidate["temporal_scope"]["retrieved_at"] = value  # type: ignore[index]
    assert Finding(
        "RETRIEVAL_TIME_INVALID", "$.temporal_scope.retrieved_at"
    ) in validate_candidate(candidate)


def test_canonical_whole_second_utc_fixture_remains_valid() -> None:
    assert validate_candidate(_candidate()) == []
