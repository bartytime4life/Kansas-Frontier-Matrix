"""Parser and diagnostic safety tests for path aliases."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.validators.directory_governance.path_alias_model import REPO_ROOT
from tools.validators.directory_governance.validate_path_alias_register import validate_register


class PathAliasSafetyCases(unittest.TestCase):
    def test_duplicate_keys_fail_closed_as_validator_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.yaml"
            path.write_text('{"version":"v1","version":"v2"}', encoding="utf-8")
            result = validate_register(path, check_repository=False, enforce_projection_binding=False)
        self.assertEqual("ERROR_VALIDATOR", result.outcome)
        self.assertEqual(["JSON_DUPLICATE_KEY"], sorted({item.code for item in result.findings}))

    def test_nonfinite_numbers_fail_closed_as_validator_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.yaml"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_register(path, check_repository=False, enforce_projection_binding=False)
        self.assertEqual("ERROR_VALIDATOR", result.outcome)
        self.assertEqual(["JSON_NONFINITE_NUMBER"], sorted({item.code for item in result.findings}))

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        marker = "synthetic-secret-must-not-echo"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "untrusted.yaml"
            path.write_text(json.dumps({"unexpected": marker}), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/validators/directory_governance/validate_path_alias_register.py",
                    str(path),
                    "--skip-repository",
                    "--skip-projection-binding",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(1, result.returncode)
        self.assertNotIn(marker, result.stdout + result.stderr)
        self.assertIn("SCHEMA_INVALID", result.stdout)
