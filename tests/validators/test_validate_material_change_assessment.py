from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.validate_material_change_assessment import (
    FIXTURE_ROOT,
    REPO_ROOT,
    SCHEMA_PATH,
    validate_assessment,
)


class MaterialChangeAssessmentValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_valid_fixtures_pass(self) -> None:
        files = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        self.assertGreaterEqual(len(files), 5)
        for path in files:
            with self.subTest(path=path.name):
                self.assertTrue(validate_assessment(path).ok)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        lane = FIXTURE_ROOT / "invalid"
        manifest = json.loads((lane / "expected_findings_manifest.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(manifest), 5)
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = validate_assessment(lane / name)
                self.assertFalse(result.ok)
                self.assertEqual(sorted(set(expected)), sorted({item.code for item in result.findings}))

    def test_fixture_cli_profile_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "tools/validators/validate_material_change_assessment.py", "--fixtures"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)
        self.assertNotIn("kfm://source/example", result.stdout)

    def test_duplicate_keys_fail_closed_without_echo(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"object_type":"MaterialChangeAssessment","object_type":"x"}', encoding="utf-8")
            result = validate_assessment(path)
        self.assertEqual(["JSON_DUPLICATE_KEY"], sorted({item.code for item in result.findings}))

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_assessment(path)
        self.assertEqual(["JSON_NONFINITE_NUMBER"], sorted({item.code for item in result.findings}))

    def test_missing_file_fails_closed(self) -> None:
        result = validate_assessment(Path("does-not-exist-material-change.json"))
        self.assertEqual(["FILE_NOT_FOUND"], sorted({item.code for item in result.findings}))


if __name__ == "__main__":
    unittest.main()
