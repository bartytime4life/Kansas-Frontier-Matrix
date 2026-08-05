"""Fixture-driven runtime proof for the synthetic soil-moisture profile."""

from __future__ import annotations

import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from .runtime_mapper import build_soil_moisture_runtime_response


REPOSITORY_ROOT = Path(__file__).resolve().parents[5]
VALID_FIXTURE = REPOSITORY_ROOT / (
    "fixtures/domains/soil/soil_moisture/valid/station_series.json"
)
DUPLICATE_FIXTURE = REPOSITORY_ROOT / (
    "fixtures/domains/soil/soil_moisture/invalid/duplicate_reading.json"
)
RUNTIME_SCHEMA = REPOSITORY_ROOT / (
    "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json"
)
EVIDENCE_SCHEMA = REPOSITORY_ROOT / (
    "schemas/contracts/v1/evidence/evidence_ref.schema.json"
)
FIXED_TIME = "2026-08-05T21:40:00Z"
FORBIDDEN_KEYS = {
    "payload",
    "readings",
    "station_id",
    "source_descriptor_ref",
    "run_receipt_ref",
    "governance",
    "proof_bundle",
    "catalog_entry",
    "promotion_decision",
    "release_manifest",
    "publication",
}


def _load(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _validator() -> Draft202012Validator:
    runtime_schema = _load(RUNTIME_SCHEMA)
    evidence_schema = _load(EVIDENCE_SCHEMA)
    registry = Registry().with_resource(
        evidence_schema["$id"], Resource.from_contents(evidence_schema)
    )
    return Draft202012Validator(
        runtime_schema,
        registry=registry,
        format_checker=FormatChecker(),
    )


def _assert_schema_valid(value: dict[str, object]) -> None:
    errors = sorted(
        _validator().iter_errors(value),
        key=lambda error: list(error.absolute_path),
    )
    assert errors == []


def test_valid_fixture_abstains_because_it_is_not_released() -> None:
    result = build_soil_moisture_runtime_response(
        _load(VALID_FIXTURE), issued_at=FIXED_TIME
    )

    _assert_schema_valid(result)
    assert result["outcome"] == "ABSTAIN"
    assert result["reason_code"] == "SOIL_MOISTURE_FIXTURE_NOT_RELEASED"
    assert result["policy_state"] == "fixture_only_not_released"
    assert result["freshness"] == "fixture_only"
    assert result["evidence_refs"] == [
        {
            "ref": "evidence:synthetic-soil-moisture-series",
            "kind": "measurement",
        }
    ]


def test_duplicate_reading_is_denied_without_candidate_leakage() -> None:
    result = build_soil_moisture_runtime_response(
        _load(DUPLICATE_FIXTURE), issued_at=FIXED_TIME
    )

    _assert_schema_valid(result)
    assert result["outcome"] == "DENY"
    assert result["reason_code"] == "SOIL_MOISTURE_VALIDATION_DENIED"
    assert result["evidence_refs"] == []
    assert FORBIDDEN_KEYS.isdisjoint(result)


def test_missing_evidence_support_abstains() -> None:
    candidate = _load(VALID_FIXTURE)
    candidate["evidence_refs"] = []

    result = build_soil_moisture_runtime_response(candidate, issued_at=FIXED_TIME)

    _assert_schema_valid(result)
    assert result["outcome"] == "ABSTAIN"
    assert result["reason_code"] == "SOIL_MOISTURE_SUPPORT_INCOMPLETE"
    assert result["evidence_refs"] == []


def test_non_object_input_returns_safe_error() -> None:
    result = build_soil_moisture_runtime_response([], issued_at=FIXED_TIME)

    _assert_schema_valid(result)
    assert result["outcome"] == "ERROR"
    assert result["reason_code"] == "SOIL_MOISTURE_INPUT_ERROR"
    assert result["evidence_refs"] == []
    assert FORBIDDEN_KEYS.isdisjoint(result)


def test_mapping_is_replay_deterministic_and_never_answers_fixture_data() -> None:
    candidate = _load(VALID_FIXTURE)
    snapshot = copy.deepcopy(candidate)

    first = build_soil_moisture_runtime_response(candidate, issued_at=FIXED_TIME)
    second = build_soil_moisture_runtime_response(candidate, issued_at=FIXED_TIME)

    assert first == second
    assert candidate == snapshot
    assert first["outcome"] != "ANSWER"
    assert FORBIDDEN_KEYS.isdisjoint(first)
