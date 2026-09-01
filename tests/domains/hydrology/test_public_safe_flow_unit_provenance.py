#!/usr/bin/env python3
"""Regression tests for public-safe FlowObservation unit provenance."""

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


def test_public_safe_flow_profile_declares_no_hidden_unit_transform() -> None:
    candidate = _candidate()
    measurement = candidate["measurement"]  # type: ignore[index]
    assert measurement["unit"] == "ft3/s"  # type: ignore[index]
    assert measurement["unit_transform_ref"] is None  # type: ignore[index]
    assert validate_candidate(candidate) == []


def test_missing_unit_transform_provenance_fails_closed() -> None:
    candidate = copy.deepcopy(_candidate())
    candidate["measurement"].pop("unit_transform_ref")  # type: ignore[index]
    assert Finding(
        "UNIT_TRANSFORM_REF_MISSING", "$.measurement.unit_transform_ref"
    ) in validate_candidate(candidate)


@pytest.mark.parametrize(
    "value",
    [
        "fixture://transforms/hydrology/unverified-normalization",
        "",
        False,
        0,
        {},
        [],
    ],
)
def test_unverified_unit_transform_refs_fail_closed(value: object) -> None:
    candidate = copy.deepcopy(_candidate())
    candidate["measurement"]["unit_transform_ref"] = value  # type: ignore[index]
    assert Finding(
        "UNIT_TRANSFORM_REF_UNSUPPORTED", "$.measurement.unit_transform_ref"
    ) in validate_candidate(candidate)
