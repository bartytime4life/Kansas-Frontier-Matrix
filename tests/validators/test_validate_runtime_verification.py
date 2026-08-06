from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from tools.validators.runtime_verification.validate_runtime_verification import (
    FIXTURE_ROOT,
    REPO_ROOT,
    SCHEMA_ROOT,
    validate_path,
)


class RuntimeVerificationValidatorTests(unittest.TestCase):
    def test_schemas_are_valid_draft_2020_12(self) -> None:
        resources = {}
        for path in sorted(SCHEMA_ROOT.glob("*.schema.json")):
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            resources[schema["$id"]] = Resource.from_contents(schema)
        registry = Registry().with_resources(resources.items())
        self.assertEqual(4, len(resources))

        for path in sorted(SCHEMA_ROOT.glob("*.schema.json")):
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator(schema, registry=registry)

    def test_valid_fixtures_pass(self) -> None:
        files = sorted((FIXTURE_ROOT / "receipts/valid").glob("*.json"))
        files += sorted((FIXTURE_ROOT / "proofs/valid").glob("*.json"))
        self.assertEqual(7, len(files))
        for path in files:
            with self.subTest(path=path.name):
                result = validate_path(path)
                self.assertTrue(result.ok, result.findings)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        manifest = json.loads(
            (FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual(10, len(manifest))
        for relative, expected in sorted(manifest.items()):
            with self.subTest(path=relative):
                result = validate_path(FIXTURE_ROOT / relative)
                self.assertFalse(result.ok)
                self.assertEqual(
                    sorted(expected),
                    sorted({finding.code for finding in result.findings}),
                )

    def test_fixture_cli_profile_passes(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "tools/validators/runtime_verification/validate_runtime_verification.py",
                "--fixtures",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"RuntimeVerificationReceipt",'
                '"object_type":"RuntimeVerificationProof"}',
                encoding="utf-8",
            )
            result = validate_path(path)
        self.assertEqual(
            ["JSON_DUPLICATE_KEY"],
            sorted({finding.code for finding in result.findings}),
        )

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_path(path)
        self.assertEqual(
            ["JSON_NONFINITE_NUMBER"],
            sorted({finding.code for finding in result.findings}),
        )

    def test_unknown_kind_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "unknown.json"
            path.write_text('{"object_type":"Unknown"}', encoding="utf-8")
            result = validate_path(path)
        self.assertEqual(
            ["UNKNOWN_KIND"],
            sorted({finding.code for finding in result.findings}),
        )

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        marker = "synthetic-secret-must-not-echo"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "untrusted.json"
            path.write_text(
                json.dumps(
                    {
                        "object_type": "RuntimeVerificationProof",
                        "unexpected": marker,
                    }
                ),
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/validators/runtime_verification/validate_runtime_verification.py",
                    str(path),
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(1, result.returncode)
        self.assertNotIn(marker, result.stdout + result.stderr)
        self.assertIn("SCHEMA_INVALID", result.stdout)


if __name__ == "__main__":
    unittest.main()
