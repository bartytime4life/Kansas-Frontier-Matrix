from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.validators._common.jsonschema_runner import load_validator

ROOT = Path(__file__).resolve().parents[4]
DOMAIN_SCHEMA = ROOT / "schemas/contracts/v1/domains/geology/evidence_bundle.schema.json"
SHARED_SCHEMA = ROOT / "schemas/contracts/v1/evidence/evidence_bundle.schema.json"
SHARED_FIXTURES = ROOT / "fixtures/contracts/v1/evidence/evidence_bundle"
DOMAIN_VALIDATOR = ROOT / "tools/validators/domains/geology/validate_schema.py"


class GeologyEvidenceBundleSchemaConvergenceTests(unittest.TestCase):
    def load(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def run_domain_validator(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            return subprocess.run(
                [sys.executable, str(DOMAIN_VALIDATOR), *arguments],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )

    def test_domain_projection_delegates_shape_to_shared_schema(self) -> None:
        schema = self.load(DOMAIN_SCHEMA)
        self.assertEqual(schema["$ref"], "../../evidence/evidence_bundle.schema.json")
        self.assertEqual(schema["x-kfm"]["authority"], "projection")
        self.assertEqual(schema["x-kfm"]["independent_fields"], "DENY")
        self.assertFalse(schema["x-kfm"]["public_release_authority"])
        self.assertNotIn("properties", schema)
        self.assertNotIn("required", schema)
        self.assertNotIn("additionalProperties", schema)

    def test_shared_contract_keeps_closed_claim_scope_shape(self) -> None:
        schema = self.load(SHARED_SCHEMA)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            schema["required"],
            [
                "bundle_id",
                "claim_scope",
                "evidence_refs",
                "source_records",
                "citations",
                "rights",
                "sensitivity",
                "transforms",
                "checksums",
                "spec_hash",
            ],
        )

    def test_domain_projection_accepts_and_rejects_shared_fixtures(self) -> None:
        validator = load_validator(DOMAIN_SCHEMA)
        valid = self.load(SHARED_FIXTURES / "valid/valid_1.json")
        invalid = self.load(SHARED_FIXTURES / "invalid/invalid_1.json")

        self.assertEqual(list(validator.iter_errors(valid)), [])
        self.assertNotEqual(list(validator.iter_errors(invalid)), [])

    def test_domain_entrypoint_preserves_shared_fixture_polarity(self) -> None:
        result = self.run_domain_validator("--fixtures")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK ", result.stdout)
        self.assertIn("EXPECTED_FAIL ", result.stdout)

    def test_domain_entrypoint_requires_an_input(self) -> None:
        result = self.run_domain_validator()

        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn("No files provided", result.stderr)

    def test_fixture_profile_cannot_ignore_an_explicit_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "must_not_be_ignored.json"
            fixture.write_text("{}", encoding="utf-8")
            result = self.run_domain_validator("--fixtures", str(fixture))

        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn("Use exactly --fixtures", result.stderr)

    def test_fixture_profile_abbreviations_cannot_ignore_an_explicit_file(self) -> None:
        for length in range(3, len("--fixtures")):
            abbreviation = "--fixtures"[:length]
            with self.subTest(abbreviation=abbreviation):
                result = self.run_domain_validator(abbreviation, "/missing.json")

                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertIn("Use exactly --fixtures", result.stderr)

    def test_option_terminator_preserves_explicit_file_validation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "--fixtures"
            fixture.write_text(
                (SHARED_FIXTURES / "valid/valid_1.json").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(DOMAIN_VALIDATOR), "--", fixture.name],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK --fixtures", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_inline_exact_subsurface_location_is_rejected(self) -> None:
        payload = self.load(SHARED_FIXTURES / "valid/valid_1.json")
        payload["exact_subsurface_location"] = {
            "latitude": 12.345678,
            "longitude": -45.678901,
            "depth_m": 432.1,
        }

        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "inline_exact_location.json"
            fixture.write_text(json.dumps(payload), encoding="utf-8")
            result = self.run_domain_validator(str(fixture))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Additional properties are not allowed", result.stdout)
        self.assertIn("exact_subsurface_location", result.stdout)

    def test_duplicate_claim_scope_cannot_hide_exact_subsurface_scope(self) -> None:
        payload = self.load(SHARED_FIXTURES / "valid/valid_1.json")
        serialized = json.dumps(payload)
        duplicate = (
            '{"claim_scope":"synthetic exact subsurface coordinates",'
            + serialized[1:]
        )

        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "duplicate_claim_scope.json"
            fixture.write_text(duplicate, encoding="utf-8")
            result = self.run_domain_validator(str(fixture))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("duplicate JSON object key", result.stdout)


if __name__ == "__main__":
    unittest.main()
