"""Tests for the no-network Kansas Mesonet station-health boundary."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[5]
MODULE_PATH = REPO_ROOT / (
    "pipelines/domains/soil/mesonet_station_health/evaluate_fixture.py"
)
SCHEMA_PATH = REPO_ROOT / (
    "schemas/contracts/v1/domains/soil/mesonet_station_health.schema.json"
)
FIXTURE_PATH = REPO_ROOT / (
    "fixtures/domains/soil/mesonet_station_health/valid/healthy_batch.json"
)

SPEC = importlib.util.spec_from_file_location("kfm_mesonet_station_health", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
evaluate_fixture = MODULE.evaluate_fixture

SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
Draft202012Validator.check_schema(SCHEMA)
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def _fixture() -> dict[str, object]:
    value = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _assert_schema_valid(value: dict[str, object]) -> None:
    errors = sorted(
        VALIDATOR.iter_errors(value),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    assert errors == []


def test_healthy_batch_is_deterministic_and_schema_valid() -> None:
    candidate = _fixture()

    first = evaluate_fixture(candidate)
    second = evaluate_fixture(candidate)

    assert first == second
    assert first.ok
    assert first.outcome == "HEALTHY_FIXTURE"
    assert first.reason_code == "MESONET_HEALTH_FIXTURE_ACCEPTED"
    assert first.assessment is not None
    _assert_schema_valid(first.assessment)
    assert first.assessment["summary"] == {
        "total_stations": 10,
        "fresh_stations": 10,
        "degraded_stations": 0,
        "anomalous_stations": 0,
        "untriaged_anomalies": 0,
        "coverage_fraction": 1.0,
        "degraded_fraction": 0.0,
    }
    assert first.assessment["decision"] == {
        "outcome": "HEALTHY_FIXTURE",
        "reason_codes": [],
    }
    assert first.assessment["governance"]["promotion_eligible"] is False


def test_exact_ten_percent_roster_loss_holds() -> None:
    candidate = _fixture()
    candidate["assessment_id"] = "mesonet-health-fixture-roster-loss"
    candidate["stations"][0]["last_reported_at"] = "2026-04-02T11:45:00Z"
    candidate["stations"][0]["samples"][0]["observed_at"] = "2026-04-02T11:45:00Z"

    result = evaluate_fixture(candidate)

    assert result.ok
    assert result.outcome == "HOLD"
    assert result.assessment is not None
    _assert_schema_valid(result.assessment)
    assert result.assessment["summary"]["coverage_fraction"] == 0.9
    assert result.assessment["summary"]["degraded_fraction"] == 0.1
    assert result.assessment["decision"] == {
        "outcome": "HOLD",
        "reason_codes": ["ROSTER_DEGRADED_THRESHOLD"],
    }


def test_untriaged_z_score_or_relative_jump_holds() -> None:
    candidate = _fixture()
    candidate["assessment_id"] = "mesonet-health-fixture-untriaged-anomaly"
    sample = candidate["stations"][3]["samples"][0]
    sample["z_score"] = 4.5
    sample["relative_jump_fraction"] = 0.50
    sample["triage_state"] = "UNTRIAGED"

    result = evaluate_fixture(candidate)

    assert result.ok
    assert result.outcome == "HOLD"
    assert result.assessment is not None
    _assert_schema_valid(result.assessment)
    station = result.assessment["stations"][3]
    assert station["station_state"] == "ANOMALOUS_UNTRIAGED"
    assert station["reason_codes"] == [
        "RELATIVE_JUMP",
        "UNTRIAGED_ANOMALY",
        "Z_SCORE_OUTLIER",
    ]
    assert result.assessment["decision"]["reason_codes"] == [
        "UNTRIAGED_ANOMALIES_PRESENT"
    ]


def test_precise_station_location_is_denied() -> None:
    candidate = _fixture()
    candidate["assessment_id"] = "mesonet-health-fixture-precise-location-denied"
    candidate["stations"][0]["spatial_support"]["latitude"] = 38.5

    result = evaluate_fixture(candidate)

    assert result.outcome == "DENY"
    assert result.assessment is None
    assert MODULE.Finding(
        "PRECISE_LOCATION_FIELD_FORBIDDEN",
        "/stations/0/spatial_support/latitude",
    ) in result.findings


def test_non_object_input_fails_closed() -> None:
    result = evaluate_fixture([])

    assert result.outcome == "ERROR"
    assert result.reason_code == "MESONET_HEALTH_INPUT_ERROR"
    assert result.assessment is None
    assert result.findings == (MODULE.Finding("CANDIDATE_NOT_OBJECT", "/"),)
