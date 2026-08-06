from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.control_plane.validate_object_family_register import (
    FIXTURE_ROOT,
    REGISTER_PATH,
    REPO_ROOT,
    SCHEMA_PATH,
    validate_register,
)


class ObjectFamilyRegisterValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def test_valid_fixture_passes(self) -> None:
        files = sorted((FIXTURE_ROOT / "valid").glob("*.yaml"))
        self.assertEqual(1, len(files))
        self.assertTrue(validate_register(files[0], check_paths=False).ok)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        manifest = json.loads((FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(6, len(manifest))
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = validate_register(FIXTURE_ROOT / "invalid" / name, check_paths=False)
                self.assertFalse(result.ok)
                self.assertEqual(sorted(expected), sorted({finding.code for finding in result.findings}))

    def test_current_register_passes_with_verified_path_projection(self) -> None:
        register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as directory:
            projected = Path(directory)
            for entry in register["entries"]:
                for role in ("contract_paths","schema_paths","policy_paths","fixture_paths","validator_paths","test_paths","workflow_paths","emitter_paths"):
                    for relative in entry[role]:
                        target = projected / relative
                        if Path(relative).suffix:
                            target.parent.mkdir(parents=True, exist_ok=True)
                            target.write_text("placeholder\n", encoding="utf-8")
                        else:
                            target.mkdir(parents=True, exist_ok=True)
            result = validate_register(REGISTER_PATH, repo_root=projected, check_paths=True)
        self.assertTrue(result.ok, result.findings)

    def test_missing_declared_path_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = validate_register(REGISTER_PATH, repo_root=Path(directory), check_paths=True)
        self.assertIn("PATH_NOT_FOUND", {finding.code for finding in result.findings})

    def test_fixture_cli_profile_passes(self) -> None:
        result = subprocess.run([sys.executable,"tools/validators/control_plane/validate_object_family_register.py","--fixtures"], cwd=REPO_ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.yaml"
            path.write_text('{"version":"v1","version":"v2"}', encoding="utf-8")
            result = validate_register(path, check_paths=False)
        self.assertEqual(["JSON_DUPLICATE_KEY"], sorted({finding.code for finding in result.findings}))

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.yaml"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_register(path, check_paths=False)
        self.assertEqual(["JSON_NONFINITE_NUMBER"], sorted({finding.code for finding in result.findings}))

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        marker = "synthetic-secret-must-not-echo"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "untrusted.yaml"
            path.write_text(json.dumps({"unexpected": marker}), encoding="utf-8")
            result = subprocess.run([sys.executable,"tools/validators/control_plane/validate_object_family_register.py",str(path),"--skip-path-existence"], cwd=REPO_ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(1, result.returncode)
        self.assertNotIn(marker, result.stdout + result.stderr)
        self.assertIn("SCHEMA_INVALID", result.stdout)


if __name__ == "__main__":
    unittest.main()
