"""Tests for the no-network synthetic Kansas Mesonet normalization boundary."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[5]
MODULE_PATH = REPO_ROOT / (
    "pipelines/domains/soil/mesonet_normalizer/fixture_normalizer.py"
)
FIXTURE_PATH = REPO_ROOT / (
    "fixtures/domains/soil/mesonet_normalizer/valid/native_station_record.json"
)

SPEC = importlib.util.spec_from_file_location("kfm_mesonet_fixture_normalizer", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
normalize_fixture = MODULE.normalize_fixture


def _fixture() -> dict[str, object]:
    value = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_valid_fixture_is_deterministic_and_preserves_native_context() -> None:
    candidate = _fixture()
    snapshot = copy.deepcopy(candidate)

    first = normalize_fixture(candidate)
    second = normalize_fixture(candidate)

    assert first == second
    assert candidate == snapshot
    assert first.ok
    assert first.outcome == "NORMALIZED_FIXTURE"
    assert first.reason_code == "MESONET_FIXTURE_NORMALIZED"
    assert first.findings == ()
    assert first.candidate is not None
    assert first.candidate["normalization_state"] == "fixture_only_normalized"
    assert first.candidate["support_type"] == "station_soil_moisture"
    assert first.candidate["station"]["station_health"] == "HEALTHY_FIXTURE"
    assert first.candidate["observation"]["depth_cm"] == 10
    assert first.candidate["observation"]["native_cadence_minutes"] == 5
    assert first.candidate["observation"]["output_cadence_minutes"] == 5
    assert first.candidate["observation"]["source_timezone"] == "America/Chicago"
    assert first.candidate["rights"] == {
        "rights_state": "fixture_only",
        "operator_consent_state": "fixture_only",
    }
    assert first.candidate["governance"]["release_state"] == "not_released"
    assert first.candidate["governance"]["public_use_allowed"] is False


def test_station_health_unknown_holds_without_emitting_candidate() -> None:
    candidate = _fixture()
    candidate["station"]["station_health"] = "UNKNOWN"

    result = normalize_fixture(candidate)

    assert result.outcome == "HOLD"
    assert result.reason_code == "MESONET_STATION_HEALTH_UNRESOLVED"
    assert result.candidate is None
    assert MODULE.Finding("STATION_HEALTH_HOLD", "/station/station_health") in result.findings


def test_deny_precedence_over_station_health_hold() -> None:
    candidate = _fixture()
    candidate["station"]["station_health"] = "UNKNOWN"
    candidate["support_type"] = "satellite_soil_moisture_grid"

    result = normalize_fixture(candidate)

    assert result.outcome == "DENY"
    assert result.reason_code == "MESONET_FIXTURE_NORMALIZATION_DENIED"
    assert result.candidate is None


def test_cadence_collapse_without_receipt_is_denied() -> None:
    candidate = _fixture()
    candidate["observation"]["output_cadence_minutes"] = 60

    result = normalize_fixture(candidate)

    assert result.outcome == "DENY"
    assert result.candidate is None
    assert MODULE.Finding(
        "CADENCE_COLLAPSE_WITHOUT_RECEIPT",
        "/observation/output_cadence_minutes",
    ) in result.findings


def test_cadence_change_with_explicit_receipt_remains_fixture_only() -> None:
    candidate = _fixture()
    candidate["observation"]["output_cadence_minutes"] = 60
    candidate["observation"]["aggregation_receipt_ref"] = (
        "receipt:synthetic-mesonet-hourly-aggregation-0001"
    )

    result = normalize_fixture(candidate)

    assert result.ok
    assert result.candidate is not None
    assert result.candidate["observation"]["native_cadence_minutes"] == 5
    assert result.candidate["observation"]["output_cadence_minutes"] == 60
    assert result.candidate["governance"]["promotion_eligible"] is False


def test_precise_location_field_is_denied() -> None:
    candidate = _fixture()
    candidate["station"]["spatial_support"]["latitude"] = 38.5

    result = normalize_fixture(candidate)

    assert result.outcome == "DENY"
    assert result.candidate is None
    assert MODULE.Finding(
        "PRECISE_LOCATION_FIELD_FORBIDDEN",
        "/station/spatial_support/latitude",
    ) in result.findings


def test_support_type_collapse_is_denied() -> None:
    candidate = _fixture()
    candidate["support_type"] = "satellite_soil_moisture_grid"

    result = normalize_fixture(candidate)

    assert result.outcome == "DENY"
    assert result.candidate is None
    assert MODULE.Finding("SUPPORT_TYPE_COLLAPSE", "/support_type") in result.findings


def test_unknown_rights_or_operator_consent_is_denied() -> None:
    candidate = _fixture()
    candidate["rights"] = {
        "rights_state": "unknown",
        "operator_consent_state": "unknown",
    }

    result = normalize_fixture(candidate)

    assert result.outcome == "DENY"
    assert result.candidate is None
    assert {finding.code for finding in result.findings} >= {
        "RIGHTS_NOT_FIXTURE_ONLY",
        "OPERATOR_CONSENT_NOT_FIXTURE_ONLY",
    }


def test_non_object_input_returns_safe_error() -> None:
    result = normalize_fixture([])

    assert result.outcome == "ERROR"
    assert result.reason_code == "MESONET_FIXTURE_INPUT_ERROR"
    assert result.candidate is None
    assert result.findings == (MODULE.Finding("CANDIDATE_NOT_OBJECT", "/"),)
