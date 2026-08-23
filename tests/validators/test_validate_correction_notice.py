from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators import validate_correction_notice as compatibility
from tools.validators.correction.validate_correction_notice import (
    FIXTURES_ROOT,
    SCHEMA_PATH,
    validate_path,
)


class CorrectionNoticeValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_valid_minimal_fixture_passes(self) -> None:
        self.assertEqual((), validate_path(FIXTURES_ROOT / "valid/minimal.json"))

    def test_missing_id_fails_schema(self) -> None:
        findings = validate_path(FIXTURES_ROOT / "invalid/missing_id.json")
        self.assertIn("SCHEMA_INVALID", findings)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"id":"one","id":"two"}', encoding="utf-8")
            self.assertEqual(("JSON_DUPLICATE_KEY",), validate_path(path))

    def test_non_object_root_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "array.json"
            path.write_text('["correction"]', encoding="utf-8")
            self.assertEqual(("JSON_ROOT_INVALID",), validate_path(path))

    def test_nonfinite_number_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nan.json"
            path.write_text('{"id":"one","value":NaN}', encoding="utf-8")
            self.assertEqual(("JSON_INVALID",), validate_path(path))

    def test_compatibility_entry_point_preserves_behavior(self) -> None:
        path = FIXTURES_ROOT / "valid/minimal.json"
        self.assertEqual(SCHEMA_PATH, compatibility.SCHEMA_PATH)
        self.assertEqual(validate_path(path), compatibility.validate_path(path))

    def test_both_cli_entry_points_are_no_network_and_pass(self) -> None:
        for script in (
            "tools/validators/correction/validate_correction_notice.py",
            "tools/validators/validate_correction_notice.py",
        ):
            result = subprocess.run(
                [sys.executable, script, "--fixtures"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertIn("CORRECTION_NOTICE_FIXTURES_VALID", result.stdout)
            self.assertIn("no_network=true", result.stdout)
            self.assertIn("non_publisher=true", result.stdout)


if __name__ == "__main__":
    unittest.main()
