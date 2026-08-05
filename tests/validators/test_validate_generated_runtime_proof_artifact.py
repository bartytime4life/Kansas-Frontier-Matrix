from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.validate_generated_runtime_proof_artifact import (
    FIXTURE_ROOT,
    REPO_ROOT,
    SCHEMA_PATH,
    validate_artifact,
)


class GeneratedRuntimeProofArtifactValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_valid_fixtures_pass(self) -> None:
        files = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        self.assertGreaterEqual(len(files), 7)
        for path in files:
            with self.subTest(path=path.name):
                result = validate_artifact(path)
                self.assertTrue(result.ok, result.findings)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        lane = FIXTURE_ROOT / "invalid"
        manifest = json.loads(
            (lane / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
        self.assertGreaterEqual(len(manifest), 10)
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = validate_artifact(lane / name)
                self.assertFalse(result.ok)
                self.assertEqual(
                    sorted(set(expected)),
                    sorted({item.code for item in result.findings}),
                )

    def test_fixture_cli_profile_passes(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "tools/validators/validate_generated_runtime_proof_artifact.py",
                "--fixtures",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)
        self.assertNotIn("synthetic-secret-must-not-echo", result.stdout)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"GeneratedRuntimeProofArtifact",'
                '"object_type":"duplicate"}',
                encoding="utf-8",
            )
            result = validate_artifact(path)
        self.assertEqual(
            ["JSON_DUPLICATE_KEY"],
            sorted({item.code for item in result.findings}),
        )

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_artifact(path)
        self.assertEqual(
            ["JSON_NONFINITE_NUMBER"],
            sorted({item.code for item in result.findings}),
        )

    def test_missing_file_fails_closed(self) -> None:
        result = validate_artifact(Path("does-not-exist-runtime-proof-artifact.json"))
        self.assertEqual(
            ["FILE_NOT_FOUND"],
            sorted({item.code for item in result.findings}),
        )

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "secret.json"
            path.write_text(
                json.dumps(
                    {
                        "object_type": "GeneratedRuntimeProofArtifact",
                        "unexpected": "synthetic-secret-must-not-echo",
                    }
                ),
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/validators/validate_generated_runtime_proof_artifact.py",
                    str(path),
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(1, result.returncode)
        self.assertNotIn("synthetic-secret-must-not-echo", result.stdout)
        self.assertIn("SCHEMA_INVALID", result.stdout)


if __name__ == "__main__":
    unittest.main()
