"""Contract and CLI tests for the tracked MapLibre performance envelope."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators._common.jsonschema_runner import load_validator

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/maplibre/perf-envelope.schema.json"
CONFIG_PATH = REPO_ROOT / "configs/maplibre/perf-envelope.v1.json"
FIXTURE_ROOT = REPO_ROOT / "tests/fixtures/maplibre/perf-envelope"
VALIDATOR_PATH = REPO_ROOT / "tools/validators/maplibre/validate_perf_envelope.py"

EXPECTED_TOP_LEVEL_FIELDS = {
    "object_type",
    "schema_version",
    "domain",
    "policy_posture",
    "thresholds",
    "notes",
}
EXPECTED_THRESHOLD_FIELDS = {
    "avg_frame_ms",
    "p95_frame_ms",
    "idle_ms",
    "load_ms",
    "render_pixel_delta_ratio",
}
EXPECTED_VALID_FIXTURES = {
    "numeric-boundaries.json",
    "representative.json",
}
EXPECTED_INVALID_FIXTURES = {
    "duplicate-notes.json",
    "empty-notes.json",
    "missing-object-type.json",
    "missing-threshold.json",
    "negative-load-timing.json",
    "ratio-over-one.json",
    "unknown-threshold.json",
    "unknown-top-level-field.json",
    "wrong-domain.json",
    "wrong-object-type.json",
    "wrong-policy-posture.json",
    "wrong-threshold-type.json",
    "wrong-version.json",
    "zero-frame-timing.json",
}


def _load(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def _errors(payload: object) -> list[object]:
    return list(load_validator(SCHEMA_PATH).iter_errors(payload))


def _run_validator(*arguments: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR_PATH), *arguments],
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
    )


def test_schema_is_valid_draft_2020_12_and_closes_known_fields() -> None:
    schema = _load(SCHEMA_PATH)
    assert isinstance(schema, dict)
    Draft202012Validator.check_schema(schema)

    assert schema["additionalProperties"] is False
    assert set(schema["required"]) == EXPECTED_TOP_LEVEL_FIELDS
    assert set(schema["properties"]) == EXPECTED_TOP_LEVEL_FIELDS

    thresholds = schema["properties"]["thresholds"]
    assert thresholds["additionalProperties"] is False
    assert set(thresholds["required"]) == EXPECTED_THRESHOLD_FIELDS
    assert set(thresholds["properties"]) == EXPECTED_THRESHOLD_FIELDS


def test_tracked_configuration_satisfies_the_contract() -> None:
    assert _errors(_load(CONFIG_PATH)) == []


def test_fixture_inventory_is_explicit_and_has_correct_polarity() -> None:
    valid_paths = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
    invalid_paths = sorted((FIXTURE_ROOT / "invalid").glob("*.json"))

    assert {path.name for path in valid_paths} == EXPECTED_VALID_FIXTURES
    assert {path.name for path in invalid_paths} == EXPECTED_INVALID_FIXTURES
    assert all(_errors(_load(path)) == [] for path in valid_paths)
    assert all(_errors(_load(path)) for path in invalid_paths)


def test_identity_and_posture_are_exact_constants() -> None:
    payload = _load(CONFIG_PATH)
    assert isinstance(payload, dict)

    for field, invalid_value in {
        "object_type": "PerformanceEnvelope",
        "schema_version": "v2",
        "domain": "cesium",
        "policy_posture": "internal",
    }.items():
        candidate = {**payload, field: invalid_value}
        assert _errors(candidate), field


def test_timing_thresholds_are_numbers_strictly_greater_than_zero() -> None:
    payload = _load(CONFIG_PATH)
    assert isinstance(payload, dict)

    for field in ("avg_frame_ms", "p95_frame_ms", "idle_ms", "load_ms"):
        for invalid_value in (0, -0.001, "1", None, True):
            candidate = json.loads(json.dumps(payload))
            candidate["thresholds"][field] = invalid_value
            assert _errors(candidate), (field, invalid_value)


def test_pixel_delta_ratio_accepts_only_numbers_in_the_closed_unit_interval() -> None:
    payload = _load(CONFIG_PATH)
    assert isinstance(payload, dict)

    for valid_value in (0, 0.5, 1):
        candidate = json.loads(json.dumps(payload))
        candidate["thresholds"]["render_pixel_delta_ratio"] = valid_value
        assert _errors(candidate) == []

    for invalid_value in (-0.001, 1.001, "0.01", None, True):
        candidate = json.loads(json.dumps(payload))
        candidate["thresholds"]["render_pixel_delta_ratio"] = invalid_value
        assert _errors(candidate), invalid_value


def test_notes_are_nonempty_unique_bounded_and_control_free() -> None:
    payload = _load(CONFIG_PATH)
    assert isinstance(payload, dict)

    invalid_notes = (
        [],
        ["   "],
        ["duplicate", "duplicate"],
        ["x" * 501],
        ["line one\nline two"],
        [f"note {index}" for index in range(17)],
    )
    for notes in invalid_notes:
        candidate = {**payload, "notes": notes}
        assert _errors(candidate), notes


def test_cli_validates_explicit_files_and_fixtures_outside_repo_cwd(
    tmp_path: Path,
) -> None:
    explicit = _run_validator(str(CONFIG_PATH), cwd=tmp_path)
    fixtures = _run_validator("--fixtures", cwd=tmp_path)

    assert explicit.returncode == 0, explicit.stdout + explicit.stderr
    assert f"OK {CONFIG_PATH}" in explicit.stdout
    assert fixtures.returncode == 0, fixtures.stdout + fixtures.stderr
    assert fixtures.stdout.count("OK ") == len(EXPECTED_VALID_FIXTURES)
    assert fixtures.stdout.count("EXPECTED_FAIL ") == len(
        EXPECTED_INVALID_FIXTURES
    )


def test_cli_rejects_duplicate_keys_nonfinite_numbers_and_missing_inputs(
    tmp_path: Path,
) -> None:
    duplicate = tmp_path / "duplicate.json"
    duplicate.write_text(
        '{"object_type":"PerfEnvelope","object_type":"PerfEnvelope"}',
        encoding="utf-8",
    )
    nonfinite = tmp_path / "nonfinite.json"
    nonfinite.write_text('{"thresholds":{"avg_frame_ms":NaN}}', encoding="utf-8")

    duplicate_result = _run_validator(str(duplicate), cwd=tmp_path)
    nonfinite_result = _run_validator(str(nonfinite), cwd=tmp_path)
    missing_result = _run_validator(cwd=tmp_path)

    assert duplicate_result.returncode == 1
    assert "duplicate JSON object key" in duplicate_result.stdout
    assert nonfinite_result.returncode == 1
    assert "non-finite JSON number" in nonfinite_result.stdout
    assert missing_result.returncode == 2
    assert "No files provided" in missing_result.stderr
