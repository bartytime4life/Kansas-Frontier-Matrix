#!/usr/bin/env python3
"""Deterministic tests for Atmosphere observed-versus-modeled separation.

The fixtures are synthetic and no-network. These tests prove only the bounded
profile: object discrimination, source/evidence posture, time and unit fields,
model-run identity, DERIVED_FROM lineage, uncertainty, explicit abstention,
and denial of observation/model collapse or false release state.
"""

from __future__ import annotations

import contextlib
import copy
import io
import json
import socket
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    MAX_FIXTURE_BYTES,
    Finding,
)
from tools.validators.domains.atmosphere.validate_observed_modeled_separation import (  # noqa: E402
    ValidationResult,
    main,
    validate_candidate,
    validate_file,
)


FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/atmosphere/observed_modeled_separation"
VALID_DIR = FIXTURE_ROOT / "valid"
INVALID_DIR = FIXTURE_ROOT / "invalid"
SCHEMA_ROOT = REPO_ROOT / "schemas/contracts/v1/domains/atmosphere"
OBS_SCHEMA = SCHEMA_ROOT / "air_observation.schema.json"
MODEL_SCHEMA = SCHEMA_ROOT / "forecast_context.schema.json"

VALID_OUTCOMES = {
    "air_observation_bound.json": "PASS",
    "air_observation_unresolved.json": "ABSTAIN",
    "forecast_context_bound.json": "PASS",
}
INVALID_FINDINGS = {
    "air_observation_false_release.json": (
        Finding("RELEASE_POSTURE_DENIED", "$.release_posture"),
    ),
    "air_observation_missing_station.json": (
        Finding("AIR_STATION_REF_MISSING", "$.air_station_ref"),
    ),
    "air_observation_missing_unit.json": (
        Finding("MEASUREMENT_UNIT_INVALID", "$.measurement.unit"),
    ),
    "air_observation_model_character.json": (
        Finding("OBSERVATION_CHARACTER_INVALID", "$.knowledge_character"),
    ),
    "air_observation_model_run_ref.json": (
        Finding("MODEL_AS_OBSERVATION_DENIED", "$.model_run_ref"),
    ),
    "forecast_context_false_release.json": (
        Finding("RELEASE_POSTURE_DENIED", "$.release_posture"),
    ),
    "forecast_context_missing_lineage.json": (
        Finding("MODEL_LINEAGE_REQUIRED", "$.lineage"),
    ),
    "forecast_context_missing_model_run.json": (
        Finding("MODEL_RUN_REF_MISSING", "$.model_run_ref"),
    ),
    "forecast_context_missing_uncertainty.json": (
        Finding("UNCERTAINTY_REQUIRED", "$.uncertainty"),
    ),
    "forecast_context_observed_at.json": (
        Finding("OBSERVATION_AS_MODEL_DENIED", "$.observed_at"),
    ),
    "forecast_context_observed_character.json": (
        Finding("MODEL_CHARACTER_INVALID", "$.knowledge_character"),
    ),
    "forecast_context_reversed_time.json": (
        Finding("TEMPORAL_ORDER_INVALID", "$.temporal_scope"),
    ),
}


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


class AtmosphereObservedModeledSeparationTests(unittest.TestCase):
    def setUp(self) -> None:
        denied = RuntimeError("network access is forbidden in Atmosphere profile tests")
        self.network_mocks: list[mock.Mock] = []
        for patcher in (
            mock.patch.object(socket.socket, "connect", side_effect=denied),
            mock.patch.object(socket.socket, "connect_ex", side_effect=denied),
            mock.patch.object(socket, "create_connection", side_effect=denied),
            mock.patch.object(socket, "getaddrinfo", side_effect=denied),
            mock.patch.object(urllib.request, "urlopen", side_effect=denied),
        ):
            self.network_mocks.append(patcher.start())
            self.addCleanup(patcher.stop)

    def test_fixture_inventory_is_explicit(self) -> None:
        self.assertEqual(
            {path.name for path in VALID_DIR.glob("*.json")},
            set(VALID_OUTCOMES),
        )
        self.assertEqual(
            {path.name for path in INVALID_DIR.glob("*.json")},
            set(INVALID_FINDINGS),
        )

    def test_valid_fixture_outcomes_are_exact(self) -> None:
        for name, outcome in VALID_OUTCOMES.items():
            with self.subTest(name=name):
                result = validate_file(VALID_DIR / name)
                self.assertEqual(result.outcome, outcome)
                fixture = _load(VALID_DIR / name)
                self.assertEqual(fixture["_fixture_meta"]["expected_outcome"], outcome)  # type: ignore[index]

    def test_unresolved_candidate_abstains_for_exact_reasons(self) -> None:
        result = validate_file(VALID_DIR / "air_observation_unresolved.json")
        self.assertEqual(result.outcome, "ABSTAIN")
        self.assertEqual(
            result.findings,
            (
                Finding("EVIDENCE_UNRESOLVED", "$.evidence_resolution_status"),
                Finding("QA_NOT_REVIEWED", "$.qa_state"),
                Finding("RIGHTS_UNRESOLVED", "$.rights_status"),
                Finding("SOURCE_UNRESOLVED", "$.source_resolution_status"),
            ),
        )

    def test_invalid_fixture_findings_are_exact(self) -> None:
        for name, expected in INVALID_FINDINGS.items():
            with self.subTest(name=name):
                result = validate_file(INVALID_DIR / name)
                self.assertEqual(result, ValidationResult("DENY", expected))

    def test_valid_fixture_metadata_is_synthetic_no_network_and_public_safe(self) -> None:
        for path in sorted(VALID_DIR.glob("*.json")):
            fixture = _load(path)
            meta = fixture["_fixture_meta"]
            self.assertEqual(meta["network_status"], "no_network_required")  # type: ignore[index]
            self.assertIs(meta["sensitive_data"], False)  # type: ignore[index]
            self.assertEqual(fixture["release_posture"], "not_released")
            self.assertIs(fixture["not_for_life_safety"], True)

    def test_observation_and_model_cannot_substitute_for_each_other(self) -> None:
        observation = _load(VALID_DIR / "air_observation_bound.json")
        observation["object_type"] = "ForecastContext"
        findings = validate_candidate(observation)
        self.assertIn(Finding("MODEL_CONTEXT_ID_MISSING", "$.model_context_id"), findings)
        self.assertIn(Finding("MODEL_CHARACTER_INVALID", "$.knowledge_character"), findings)

        model = _load(VALID_DIR / "forecast_context_bound.json")
        model["object_type"] = "AirObservation"
        findings = validate_candidate(model)
        self.assertIn(Finding("OBSERVATION_ID_MISSING", "$.observation_id"), findings)
        self.assertIn(Finding("OBSERVATION_CHARACTER_INVALID", "$.knowledge_character"), findings)

    def test_temporal_boundaries_are_ordered(self) -> None:
        observation = _load(VALID_DIR / "air_observation_bound.json")
        observation["temporal_scope"] = {
            "observed_at": "2026-08-03T12:05:01Z",
            "retrieved_at": "2026-08-03T12:05:00Z",
        }
        self.assertIn(
            Finding("TEMPORAL_ORDER_INVALID", "$.temporal_scope"),
            validate_candidate(observation),
        )

        model = _load(VALID_DIR / "forecast_context_bound.json")
        model["temporal_scope"] = {
            "generated_at": "2026-08-03T12:00:00Z",
            "valid_at": "2026-08-03T14:00:00Z",
            "valid_until": "2026-08-03T13:59:59Z",
        }
        self.assertIn(
            Finding("TEMPORAL_ORDER_INVALID", "$.temporal_scope"),
            validate_candidate(model),
        )

    def test_measurement_rejects_boolean_and_nonfinite_values(self) -> None:
        for value in (True, False, float("nan"), float("inf")):
            candidate = _load(VALID_DIR / "air_observation_bound.json")
            candidate["measurement"]["value"] = value  # type: ignore[index]
            self.assertIn(
                Finding("MEASUREMENT_VALUE_INVALID", "$.measurement.value"),
                validate_candidate(candidate),
            )

    def test_low_cost_sensor_requires_caveat_and_confidence(self) -> None:
        candidate = _load(VALID_DIR / "air_observation_bound.json")
        candidate["source_role"] = "low_cost_sensor"
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding("CONFIDENCE_STATEMENT_REQUIRED", "$.confidence_statement"),
                Finding("LOW_COST_SENSOR_CAVEAT_REQUIRED", "$.low_cost_sensor_caveat"),
            ],
        )

    def test_closed_shapes_and_deterministic_order(self) -> None:
        candidate = _load(VALID_DIR / "forecast_context_bound.json")
        candidate["zeta"] = "synthetic"
        candidate["alpha"] = "synthetic"
        expected = [
            Finding("UNDECLARED_TOP_LEVEL_FIELD", "$.alpha"),
            Finding("UNDECLARED_TOP_LEVEL_FIELD", "$.zeta"),
        ]
        self.assertEqual(validate_candidate(candidate), expected)
        reordered = dict(reversed(list(copy.deepcopy(candidate).items())))
        self.assertEqual(validate_candidate(reordered), expected)

    def test_parser_rejects_duplicate_nonfinite_and_nonobject_json(self) -> None:
        cases = (
            b'{"object_type":"AirObservation","object_type":"ForecastContext"}',
            b'{"object_type":"AirObservation","measurement":{"value":NaN}}',
            b"[]",
        )
        expected = (
            ValidationResult("ERROR", (Finding("FIXTURE_JSON_INVALID", "$"),)),
            ValidationResult("ERROR", (Finding("FIXTURE_JSON_INVALID", "$"),)),
            ValidationResult("DENY", (Finding("CANDIDATE_NOT_OBJECT", "$"),)),
        )
        with tempfile.TemporaryDirectory() as directory:
            for index, (content, wanted) in enumerate(zip(cases, expected, strict=True)):
                path = Path(directory) / f"case-{index}.json"
                path.write_bytes(content)
                self.assertEqual(validate_file(path), wanted)

    def test_file_size_is_bounded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "large.json"
            path.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(
                validate_file(path),
                ValidationResult("ERROR", (Finding("FIXTURE_TOO_LARGE", "$"),)),
            )

    def test_cli_status_exit_codes_and_non_echoing_output(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            self.assertEqual(main([str(VALID_DIR / "air_observation_bound.json")]), 0)
            self.assertEqual(main([str(VALID_DIR / "air_observation_unresolved.json")]), 0)
            self.assertEqual(main([str(INVALID_DIR / "forecast_context_missing_lineage.json")]), 1)
            self.assertEqual(main([]), 2)
        output = stdout.getvalue()
        self.assertIn('"status":"PASS"', output)
        self.assertIn('"status":"ABSTAIN"', output)
        self.assertIn('"status":"DENY"', output)
        self.assertNotIn("fixture://model-input/atmosphere/alpha", output)
        self.assertIn("at least one fixture file is required", stderr.getvalue())

    def test_schema_files_are_closed_and_role_discriminated(self) -> None:
        observation = _load(OBS_SCHEMA)
        model = _load(MODEL_SCHEMA)
        self.assertIs(observation["additionalProperties"], False)
        self.assertIs(model["additionalProperties"], False)
        self.assertEqual(
            observation["properties"]["knowledge_character"]["const"],  # type: ignore[index]
            "OBSERVED_SENSOR",
        )
        self.assertEqual(
            model["properties"]["knowledge_character"]["const"],  # type: ignore[index]
            "ATMOSPHERIC_MODEL_FIELD",
        )
        self.assertEqual(
            model["properties"]["lineage"]["properties"]["relationship"]["const"],  # type: ignore[index]
            "DERIVED_FROM",
        )
        self.assertNotIn("released", observation["properties"]["release_posture"]["enum"])  # type: ignore[index]
        self.assertNotIn("released", model["properties"]["release_posture"]["enum"])  # type: ignore[index]

    def test_camelcase_schema_paths_are_one_way_mirrors(self) -> None:
        observation_alias = _load(SCHEMA_ROOT / "AirObservation.schema.json")
        model_alias = _load(SCHEMA_ROOT / "ForecastContext.schema.json")
        self.assertEqual(observation_alias["$ref"], "./air_observation.schema.json")
        self.assertEqual(model_alias["$ref"], "./forecast_context.schema.json")
        self.assertEqual(observation_alias["x-kfm"]["status"], "MIRROR")  # type: ignore[index]
        self.assertEqual(model_alias["x-kfm"]["status"], "MIRROR")  # type: ignore[index]

    def test_all_schema_json_parses(self) -> None:
        for path in (OBS_SCHEMA, MODEL_SCHEMA, SCHEMA_ROOT / "AirObservation.schema.json", SCHEMA_ROOT / "ForecastContext.schema.json"):
            with self.subTest(path=path.name):
                self.assertIsInstance(_load(path), dict)

    def test_validation_never_attempts_network_access(self) -> None:
        for path in sorted(VALID_DIR.glob("*.json")) + sorted(INVALID_DIR.glob("*.json")):
            validate_file(path)
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()


try:
    from jsonschema import Draft202012Validator, FormatChecker
except ModuleNotFoundError:
    Draft202012Validator = None  # type: ignore[assignment]
    FormatChecker = None  # type: ignore[assignment]


@unittest.skipIf(Draft202012Validator is None, "jsonschema dependency unavailable")
class AtmosphereObservedModeledJsonSchemaTests(unittest.TestCase):
    def test_canonical_schemas_accept_positive_and_abstain_fixtures(self) -> None:
        validators = {
            "AirObservation": Draft202012Validator(_load(OBS_SCHEMA), format_checker=FormatChecker()),
            "ForecastContext": Draft202012Validator(_load(MODEL_SCHEMA), format_checker=FormatChecker()),
        }
        for path in sorted(VALID_DIR.glob("*.json")):
            candidate = _load(path)
            errors = list(validators[candidate["object_type"]].iter_errors(candidate))
            self.assertFalse(errors, f"{path.name}: {[error.message for error in errors]}")

    def test_shape_negative_fixtures_fail_their_schema(self) -> None:
        validators = {
            "AirObservation": Draft202012Validator(_load(OBS_SCHEMA), format_checker=FormatChecker()),
            "ForecastContext": Draft202012Validator(_load(MODEL_SCHEMA), format_checker=FormatChecker()),
        }
        for path in sorted(INVALID_DIR.glob("*.json")):
            if path.name == "forecast_context_reversed_time.json":
                continue
            candidate = _load(path)
            errors = list(validators[candidate["object_type"]].iter_errors(candidate))
            self.assertTrue(errors, f"negative fixture unexpectedly passed: {path.name}")

    def test_cross_field_time_order_is_a_validator_boundary(self) -> None:
        candidate = _load(INVALID_DIR / "forecast_context_reversed_time.json")
        schema = Draft202012Validator(_load(MODEL_SCHEMA), format_checker=FormatChecker())
        self.assertFalse(list(schema.iter_errors(candidate)))
        self.assertEqual(
            validate_candidate(candidate),
            [Finding("TEMPORAL_ORDER_INVALID", "$.temporal_scope")],
        )

    def test_cross_family_substitution_fails_both_schemas(self) -> None:
        observation = _load(VALID_DIR / "air_observation_bound.json")
        model = _load(VALID_DIR / "forecast_context_bound.json")
        observation_validator = Draft202012Validator(_load(OBS_SCHEMA), format_checker=FormatChecker())
        model_validator = Draft202012Validator(_load(MODEL_SCHEMA), format_checker=FormatChecker())
        self.assertTrue(list(model_validator.iter_errors(observation)))
        self.assertTrue(list(observation_validator.iter_errors(model)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
