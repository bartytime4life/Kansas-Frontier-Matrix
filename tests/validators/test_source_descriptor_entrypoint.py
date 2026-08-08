#!/usr/bin/env python3
"""Regression tests for the generic SourceDescriptor validator entrypoint."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = REPO_ROOT / "tools/validators/validate_source_descriptor.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/source/source_descriptor"
VALID_FIXTURE = FIXTURE_ROOT / "valid/valid_1.json"
INVALID_FIXTURE = FIXTURE_ROOT / "invalid/invalid_1.json"


class SourceDescriptorEntrypointTests(unittest.TestCase):
    """Prove path independence and fail-closed fixture behavior."""

    def _run(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            return subprocess.run(
                [sys.executable, str(VALIDATOR), *arguments],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )

    def test_valid_fixture_passes_from_unrelated_working_directory(self) -> None:
        result = self._run(str(VALID_FIXTURE))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK ", result.stdout)

    def test_invalid_fixture_fails_closed_from_unrelated_working_directory(self) -> None:
        result = self._run(str(INVALID_FIXTURE))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("FAIL ", result.stdout)

    def test_fixture_inventory_checks_positive_and_negative_cases(self) -> None:
        result = self._run("--fixtures")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK ", result.stdout)
        self.assertIn("EXPECTED_FAIL ", result.stdout)

    def test_missing_arguments_is_usage_error(self) -> None:
        result = self._run()
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("No files provided", result.stderr)


if __name__ == "__main__":
    unittest.main()
