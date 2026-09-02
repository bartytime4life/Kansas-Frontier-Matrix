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
from pathlib import Path

from tools.validators._common.public_safe_fixture import Finding
from tools.validators.domains.atmosphere.validate_air_observation import (
    ValidationResult,
    main,
    validate_candidate,
    validate_file,
)


REPO_ROOT = Path(__file__).resolve().parents[4]
VALIDATOR = (
    REPO_ROOT / "tools/validators/domains/atmosphere/validate_air_observation.py"
)
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/atmosphere/observed_modeled_separation"
VALID_DIR = FIXTURE_ROOT / "valid"
INVALID_DIR = FIXTURE_ROOT / "invalid"


class AirObservationValidatorEntrypointTests(unittest.TestCase):
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
