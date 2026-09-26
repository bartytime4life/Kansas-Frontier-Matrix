#!/usr/bin/env python3
"""Regression proof for the Geology EvidenceBundle validator entrypoint.

``validate_evidence_bundle.py`` is a compatibility wrapper; the authoritative
implementation is ``validate_schema.py`` (see
``test_evidence_bundle_schema_convergence.py``). This suite proves the wrapper
delegates unchanged arguments and produces identical results, and does not
introduce a second validation implementation or evidence authority.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
VALIDATOR = REPO_ROOT / "tools/validators/domains/geology/validate_evidence_bundle.py"
DOMAIN_VALIDATOR = REPO_ROOT / "tools/validators/domains/geology/validate_schema.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/evidence/evidence_bundle"
VALID_FIXTURE = FIXTURE_ROOT / "valid/valid_1.json"
INVALID_FIXTURE = FIXTURE_ROOT / "invalid/invalid_1.json"


class GeologyEvidenceBundleEntrypointTests(unittest.TestCase):
    """Prove shared fixture polarity and exact delegation to the domain implementation."""

    def _run_validator(
        self,
        validator: Path,
        *arguments: str,
    ) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            return subprocess.run(
                [sys.executable, str(validator), *arguments],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )

    def _run(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return self._run_validator(VALIDATOR, *arguments)

    def test_shared_fixture_profile_preserves_positive_and_negative_polarity(self) -> None:
        result = self._run("--fixtures")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK ", result.stdout)
        self.assertIn("EXPECTED_FAIL ", result.stdout)

    def test_explicit_valid_file_passes_from_unrelated_working_directory(self) -> None:
        result = self._run(str(VALID_FIXTURE))

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"OK {VALID_FIXTURE}", result.stdout)

    def test_explicit_invalid_file_fails_from_unrelated_working_directory(self) -> None:
        result = self._run(str(INVALID_FIXTURE))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(f"FAIL {INVALID_FIXTURE}", result.stdout)

    def test_missing_arguments_is_usage_error(self) -> None:
        result = self._run()

        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn("No files provided", result.stderr)

    def test_compatibility_entrypoint_matches_domain_implementation(self) -> None:
        cases = [
            (),
            ("--fixtures",),
            ("--fixtures", str(INVALID_FIXTURE)),
            (str(VALID_FIXTURE),),
            (str(INVALID_FIXTURE),),
        ]

        for arguments in cases:
            with self.subTest(arguments=arguments):
                compatibility_result = self._run(*arguments)
                domain_result = self._run_validator(DOMAIN_VALIDATOR, *arguments)
                self.assertEqual(
                    compatibility_result.returncode,
                    domain_result.returncode,
                )
                self.assertEqual(compatibility_result.stdout, domain_result.stdout)
                self.assertEqual(compatibility_result.stderr, domain_result.stderr)


if __name__ == "__main__":
    unittest.main()
