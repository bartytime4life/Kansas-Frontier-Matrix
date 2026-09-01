from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.validators._common.jsonschema_runner import load_validator
from tools.validators.domains.atmosphere.validate_evidence_bundle import (
    FIXTURES_DIR,
    SCHEMA_PATH,
)

ROOT = Path(__file__).resolve().parents[4]
DOMAIN_SCHEMA = ROOT / "schemas/contracts/v1/domains/atmosphere/evidence_bundle.schema.json"
SHARED_SCHEMA = ROOT / "schemas/contracts/v1/evidence/evidence_bundle.schema.json"
SHARED_FIXTURES = ROOT / "fixtures/contracts/v1/evidence/evidence_bundle"
PROJECTION_VALIDATOR = ROOT / "tools/validators/validate_atmosphere_evidence_bundle_projection.py"


class AtmosphereEvidenceBundleSchemaConvergenceTests(unittest.TestCase):
    def load(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_domain_projection_delegates_shape_to_shared_schema(self) -> None:
        schema = self.load(DOMAIN_SCHEMA)
        self.assertEqual(schema["$ref"], "../../evidence/evidence_bundle.schema.json")
        self.assertEqual(schema["x-kfm"]["authority"], "projection")
        self.assertEqual(schema["x-kfm"]["independent_fields"], "DENY")
        self.assertFalse(schema["x-kfm"]["public_release_authority"])
        self.assertFalse(schema["x-kfm"]["emergency_alert_authority"])
        self.assertNotIn("properties", schema)
        self.assertNotIn("required", schema)
        self.assertNotIn("additionalProperties", schema)

    def test_projection_metadata_matches_domain_adapter_paths(self) -> None:
        schema = self.load(DOMAIN_SCHEMA)
        resolved_ref = (DOMAIN_SCHEMA.parent / schema["$ref"]).resolve()

        self.assertEqual(SCHEMA_PATH, DOMAIN_SCHEMA)
        self.assertEqual(FIXTURES_DIR, SHARED_FIXTURES)
        self.assertEqual(resolved_ref, SHARED_SCHEMA.resolve())
        self.assertEqual(
            schema["x-kfm"]["canonical_shape"],
            SHARED_SCHEMA.relative_to(ROOT).as_posix(),
        )
        self.assertEqual(
            schema["x-kfm"]["fixtures_root"],
            f"{SHARED_FIXTURES.relative_to(ROOT).as_posix()}/",
        )

    def test_shared_contract_keeps_closed_claim_scope_shape(self) -> None:
        schema = self.load(SHARED_SCHEMA)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["required"], ["bundle_id", "claim_scope", "evidence_refs", "source_records", "citations", "rights", "sensitivity", "transforms", "checksums", "spec_hash"])

    def test_domain_projection_accepts_and_rejects_shared_fixtures(self) -> None:
        validator = load_validator(DOMAIN_SCHEMA)
        valid = self.load(SHARED_FIXTURES / "valid/valid_1.json")
        invalid = self.load(SHARED_FIXTURES / "invalid/invalid_1.json")
        self.assertEqual(list(validator.iter_errors(valid)), [])
        self.assertNotEqual(list(validator.iter_errors(invalid)), [])

    def test_declared_projection_validator_delegates_from_unrelated_directory(self) -> None:
        schema = self.load(DOMAIN_SCHEMA)
        self.assertEqual(
            schema["x-kfm"]["validator"],
            "tools/validators/validate_atmosphere_evidence_bundle_projection.py",
        )

        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(PROJECTION_VALIDATOR), "--fixtures"],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK ", result.stdout)
        self.assertIn("EXPECTED_FAIL ", result.stdout)

    def test_declared_projection_validator_is_directly_executable(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [str(PROJECTION_VALIDATOR), "--fixtures"],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK ", result.stdout)
        self.assertIn("EXPECTED_FAIL ", result.stdout)

    def test_declared_projection_validator_inherits_domain_argument_guard(self) -> None:
        invalid_fixture = SHARED_FIXTURES / "invalid/invalid_1.json"

        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    sys.executable,
                    str(PROJECTION_VALIDATOR),
                    "--fixtures",
                    str(invalid_fixture),
                ],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn(
            "Cannot combine --fixtures with explicit files",
            result.stderr,
        )

    def test_declared_projection_validator_requires_an_input_mode(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(PROJECTION_VALIDATOR)],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn("No files provided", result.stderr)

    def test_declared_projection_validator_preserves_explicit_file_polarity(self) -> None:
        cases = (
            (SHARED_FIXTURES / "valid/valid_1.json", 0, "OK"),
            (SHARED_FIXTURES / "invalid/invalid_1.json", 1, "FAIL"),
        )

        for path, expected_status, expected_label in cases:
            with self.subTest(path=path):
                with tempfile.TemporaryDirectory() as directory:
                    result = subprocess.run(
                        [sys.executable, str(PROJECTION_VALIDATOR), str(path)],
                        cwd=directory,
                        check=False,
                        capture_output=True,
                        text=True,
                    )

                self.assertEqual(
                    result.returncode,
                    expected_status,
                    result.stdout + result.stderr,
                )
                self.assertIn(f"{expected_label} {path}", result.stdout)


if __name__ == "__main__":
    unittest.main()
