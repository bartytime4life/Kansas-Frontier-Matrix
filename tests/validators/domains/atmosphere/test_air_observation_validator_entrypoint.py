#!/usr/bin/env python3
"""Regression proof for the AirObservation-only validator entrypoint."""

from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import Finding
from tools.validators.domains.atmosphere.validate_air_observation import (
    SCHEMA_PATH,
    ValidationResult,
    main,
    validate_candidate,
    validate_file,
)


VALIDATOR = (
    REPO_ROOT / "tools/validators/domains/atmosphere/validate_air_observation.py"
)
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/atmosphere/observed_modeled_separation"
VALID_DIR = FIXTURE_ROOT / "valid"
INVALID_DIR = FIXTURE_ROOT / "invalid"


class AirObservationValidatorEntrypointTests(unittest.TestCase):
    def _bound_observation(self) -> dict[str, object]:
        return json.loads(
            (VALID_DIR / "air_observation_bound.json").read_text(encoding="utf-8")
        )

    def _run(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            return subprocess.run(
                [sys.executable, str(VALIDATOR), *arguments],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )

    def test_bound_observation_passes(self) -> None:
        result = validate_file(VALID_DIR / "air_observation_bound.json")
        self.assertEqual(result, ValidationResult("PASS", ()))

    def test_schema_metadata_points_to_air_observation_entrypoint(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

        self.assertEqual(
            schema["x-kfm"]["validator"],
            str(VALIDATOR.relative_to(REPO_ROOT)),
        )

    def test_schema_metadata_paths_resolve_to_governed_assets(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        expected_paths = {
            "contract_doc": REPO_ROOT
            / "contracts/domains/atmosphere/AirObservation.md",
            "profile_doc": REPO_ROOT
            / "docs/domains/atmosphere/OBSERVED_MODELED_SEPARATION.md",
            "fixtures_root": FIXTURE_ROOT,
            "validator": VALIDATOR,
        }

        self.assertLessEqual(set(expected_paths), set(schema["x-kfm"]))
        for field, expected_path in expected_paths.items():
            with self.subTest(field=field):
                declared_path = REPO_ROOT / schema["x-kfm"][field]
                self.assertEqual(declared_path.resolve(), expected_path.resolve())
                self.assertTrue(declared_path.exists())

    def test_declared_schema_rejects_short_observation_id(self) -> None:
        candidate = self._bound_observation()
        candidate["observation_id"] = "x"

        self.assertIn(
            Finding("AIR_OBSERVATION_SCHEMA_INVALID", "$.observation_id"),
            validate_candidate(candidate),
        )

    def test_declared_schema_rejects_non_object_fixture_metadata(self) -> None:
        candidate = self._bound_observation()
        candidate["_fixture_meta"] = 1

        self.assertIn(
            Finding("AIR_OBSERVATION_SCHEMA_INVALID", "$._fixture_meta"),
            validate_candidate(candidate),
        )

    def test_declared_schema_checks_date_time_formats(self) -> None:
        candidate = self._bound_observation()
        temporal_scope = deepcopy(candidate["temporal_scope"])
        self.assertIsInstance(temporal_scope, dict)
        temporal_scope["observed_at"] = "not-a-date-time"
        candidate["temporal_scope"] = temporal_scope

        self.assertIn(
            Finding(
                "AIR_OBSERVATION_SCHEMA_INVALID",
                "$.temporal_scope.observed_at",
            ),
            validate_candidate(candidate),
        )

    def test_adapter_preserves_temporal_unit_and_sensor_semantics(self) -> None:
        temporal_candidate = self._bound_observation()
        temporal_scope = deepcopy(temporal_candidate["temporal_scope"])
        self.assertIsInstance(temporal_scope, dict)
        temporal_scope["retrieved_at"] = "2000-01-01T00:00:00Z"
        temporal_candidate["temporal_scope"] = temporal_scope
        self.assertIn(
            Finding("TEMPORAL_ORDER_INVALID", "$.temporal_scope"),
            validate_candidate(temporal_candidate),
        )

        measurement_candidate = self._bound_observation()
        measurement = deepcopy(measurement_candidate["measurement"])
        self.assertIsInstance(measurement, dict)
        measurement["value"] = float("nan")
        measurement["unit"] = ""
        measurement_candidate["measurement"] = measurement
        measurement_findings = validate_candidate(measurement_candidate)
        self.assertIn(
            Finding("MEASUREMENT_VALUE_INVALID", "$.measurement.value"),
            measurement_findings,
        )
        self.assertIn(
            Finding("MEASUREMENT_UNIT_INVALID", "$.measurement.unit"),
            measurement_findings,
        )

        low_cost_candidate = self._bound_observation()
        low_cost_candidate["source_role"] = "low_cost_sensor"
        low_cost_findings = validate_candidate(low_cost_candidate)
        self.assertIn(
            Finding(
                "LOW_COST_SENSOR_CAVEAT_REQUIRED",
                "$.low_cost_sensor_caveat",
            ),
            low_cost_findings,
        )
        self.assertIn(
            Finding(
                "CONFIDENCE_STATEMENT_REQUIRED",
                "$.confidence_statement",
            ),
            low_cost_findings,
        )

    def test_unresolved_observation_preserves_abstain(self) -> None:
        result = validate_file(VALID_DIR / "air_observation_unresolved.json")
        self.assertEqual(result.outcome, "ABSTAIN")
        self.assertIn(
            Finding("SOURCE_UNRESOLVED", "$.source_resolution_status"),
            result.findings,
        )

    def test_invalid_observation_fails_closed(self) -> None:
        result = validate_file(INVALID_DIR / "air_observation_model_run_ref.json")
        self.assertEqual(result.outcome, "DENY")
        self.assertIn(
            Finding("MODEL_AS_OBSERVATION_DENIED", "$.model_run_ref"),
            result.findings,
        )

    def test_forecast_context_cannot_enter_air_observation_lane(self) -> None:
        path = VALID_DIR / "forecast_context_bound.json"
        result = validate_file(path)
        self.assertEqual(
            result,
            ValidationResult(
                "DENY",
                (Finding("AIR_OBSERVATION_REQUIRED", "$.object_type"),),
            ),
        )

    def test_nonobject_and_malformed_json_fail_closed(self) -> None:
        cases = {
            "array.json": "[]",
            "duplicate.json": '{"object_type":"AirObservation","object_type":"ForecastContext"}',
            "nonfinite.json": '{"object_type":"AirObservation","measurement":{"value":NaN}}',
        }
        expected = {
            "array.json": ValidationResult(
                "DENY",
                (Finding("CANDIDATE_NOT_OBJECT", "$"),),
            ),
            "duplicate.json": ValidationResult(
                "ERROR",
                (Finding("FIXTURE_JSON_INVALID", "$"),),
            ),
            "nonfinite.json": ValidationResult(
                "ERROR",
                (Finding("FIXTURE_JSON_INVALID", "$"),),
            ),
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, content in cases.items():
                with self.subTest(name=name):
                    path = root / name
                    path.write_text(content, encoding="utf-8")
                    self.assertEqual(validate_file(path), expected[name])

    def test_cli_batches_results_and_returns_failure(self) -> None:
        valid = VALID_DIR / "air_observation_bound.json"
        invalid = INVALID_DIR / "air_observation_model_run_ref.json"
        result = self._run(str(invalid), str(valid))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        payloads = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual([payload["file"] for payload in payloads], sorted((str(valid), str(invalid))))
        self.assertEqual({payload["status"] for payload in payloads}, {"PASS", "DENY"})
        self.assertTrue(all(payload["scope"] == "atmosphere-air-observation" for payload in payloads))

    def test_cli_is_path_independent_and_requires_input(self) -> None:
        valid = VALID_DIR / "air_observation_bound.json"
        result = self._run(str(valid))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('"status":"PASS"', result.stdout)

        missing = self._run()
        self.assertEqual(missing.returncode, 2, missing.stdout + missing.stderr)
        self.assertEqual(missing.stdout, "")
        self.assertIn("at least one AirObservation file is required", missing.stderr)

    def test_missing_file_is_error_and_main_returns_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.json"
            self.assertEqual(
                validate_file(path),
                ValidationResult(
                    "ERROR",
                    (Finding("FIXTURE_JSON_INVALID", "$"),),
                ),
            )
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main([str(path)]), 1)


if __name__ == "__main__":
    unittest.main()
