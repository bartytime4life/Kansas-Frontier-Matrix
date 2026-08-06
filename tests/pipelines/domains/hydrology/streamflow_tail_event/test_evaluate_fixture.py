"""Tests for the no-network seasonal streamflow tail evaluator."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[5]
MODULE_PATH = REPO_ROOT / (
    "pipelines/domains/hydrology/streamflow_tail_event/evaluate_fixture.py"
)
SCHEMA_PATH = REPO_ROOT / (
    "schemas/contracts/v1/domains/hydrology/streamflow_tail_event.schema.json"
)
FIXTURE_PATH = REPO_ROOT / (
    "fixtures/domains/hydrology/streamflow_tail_event/valid/no_event.json"
)

SPEC = importlib.util.spec_from_file_location("kfm_streamflow_tail", MODULE_PATH)
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


def _evaluate(candidate: dict[str, object]):
    result = evaluate_fixture(candidate)
    assert result.assessment is not None
    errors = sorted(
        VALIDATOR.iter_errors(result.assessment),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    assert errors == []
    return result


def test_within_range_is_no_event() -> None:
    result = _evaluate(_fixture())

    assert result.ok
    assert result.outcome == "NO_EVENT"
    assert result.reason_code == "WITHIN_SEASONAL_RANGE"
    assert result.assessment["summary"]["candidate_state"] == "NONE"


def test_single_tail_excursion_holds_for_persistence() -> None:
    candidate = _fixture()
    candidate["assessment_id"] = "streamflow-tail-single-spike-hold"
    candidate["readings"][-1]["discharge_cfs"] = 120.0

    result = _evaluate(candidate)

    assert result.ok
    assert result.outcome == "HOLD"
    assert result.reason_code == "PERSISTENCE_NOT_MET"
    assert result.assessment["summary"]["consecutive_tail_readings"] == 1


def test_three_consecutive_high_readings_create_answer_candidate() -> None:
    candidate = _fixture()
    candidate["assessment_id"] = "streamflow-tail-persistent-high-candidate"
    candidate["readings"] = [
        {"observed_at": "2026-04-02T09:00:00Z", "discharge_cfs": 110.0, "qualifiers": []},
        {"observed_at": "2026-04-02T10:00:00Z", "discharge_cfs": 120.0, "qualifiers": []},
        {"observed_at": "2026-04-02T11:00:00Z", "discharge_cfs": 130.0, "qualifiers": []},
    ]

    result = _evaluate(candidate)

    assert result.ok
    assert result.outcome == "ANSWER_CANDIDATE"
    assert result.reason_code == "PERSISTENT_HIGH_FLOW"
    assert result.assessment["summary"]["consecutive_tail_readings"] == 3
    assert result.assessment["governance"]["operational_alert_authority"] is False


def test_stale_data_abstains() -> None:
    candidate = _fixture()
    candidate["readings"] = [
        {"observed_at": "2026-03-27T00:00:00Z", "discharge_cfs": 5.0, "qualifiers": []}
    ]

    result = _evaluate(candidate)

    assert result.outcome == "ABSTAIN"
    assert result.reason_code == "DATA_STALE"


def test_missing_percentiles_abstain() -> None:
    candidate = _fixture()
    candidate["baseline"] = None

    result = _evaluate(candidate)

    assert result.outcome == "ABSTAIN"
    assert result.reason_code == "PERCENTILES_MISSING"
    assert result.assessment["summary"]["p05_cfs"] is None


def test_unapproved_percentiles_deny() -> None:
    candidate = _fixture()
    candidate["baseline"]["status"] = "unapproved_fixture"

    result = _evaluate(candidate)

    assert result.outcome == "DENY"
    assert result.reason_code == "PERCENTILES_NOT_APPROVED"


def test_blocking_qualifier_abstains() -> None:
    candidate = _fixture()
    candidate["readings"][-1]["discharge_cfs"] = 5.0
    candidate["readings"][-1]["qualifiers"] = ["Ice"]

    result = _evaluate(candidate)

    assert result.outcome == "ABSTAIN"
    assert result.reason_code == "SENSOR_QUALIFIER_PRESENT"


def test_regulated_context_abstains() -> None:
    candidate = _fixture()
    candidate["site"]["regulation_context"] = "regulated_context_limited"
    candidate["readings"][-1]["discharge_cfs"] = 5.0

    result = _evaluate(candidate)

    assert result.outcome == "ABSTAIN"
    assert result.reason_code == "REGULATED_CONTEXT_LIMITED"


def test_precise_location_is_denied_without_emitting_assessment() -> None:
    candidate = _fixture()
    candidate["site"]["spatial_support"]["latitude"] = 38.5

    result = evaluate_fixture(candidate)

    assert result.outcome == "DENY"
    assert result.assessment is None
    assert MODULE.Finding(
        "PRECISE_LOCATION_FIELD_FORBIDDEN",
        "/site/spatial_support/latitude",
    ) in result.findings


def test_non_object_input_is_safe_error() -> None:
    result = evaluate_fixture([])

    assert result.outcome == "ERROR"
    assert result.reason_code == "STREAMFLOW_TAIL_INPUT_ERROR"
    assert result.assessment is None
