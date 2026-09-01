#!/usr/bin/env python3
"""Regression proof for the Habitat EvidenceBundle validator entrypoint."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
VALIDATOR = REPO_ROOT / "tools/validators/domains/habitat/validate_evidence_bundle.py"
TOP_LEVEL_VALIDATOR = REPO_ROOT / "tools/validators/validate_habitat_evidence_bundle_projection.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/evidence/evidence_bundle"
VALID_FIXTURE = FIXTURE_ROOT / "valid/valid_1.json"
INVALID_FIXTURE = FIXTURE_ROOT / "invalid/invalid_1.json"


class HabitatEvidenceBundleEntrypointTests(unittest.TestCase):
    """Prove shared fixture polarity and fail-closed argument handling."""

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

    def test_fixture_profile_cannot_ignore_an_explicit_file(self) -> None:
        result = self._run("--fixtures", str(INVALID_FIXTURE))

        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn(
            "Cannot combine --fixtures with explicit files",
            result.stderr,
        )

    def test_explicit_valid_file_passes_from_unrelated_working_directory(self) -> None:
        result = self._run(str(VALID_FIXTURE))

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"OK {VALID_FIXTURE}", result.stdout)

    def test_explicit_invalid_file_fails_from_unrelated_working_directory(self) -> None:
        result = self._run(str(INVALID_FIXTURE))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(f"FAIL {INVALID_FIXTURE}", result.stdout)

    def test_mixed_explicit_files_fail_if_any_carrier_is_invalid(self) -> None:
        result = self._run(str(VALID_FIXTURE), str(INVALID_FIXTURE))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(f"OK {VALID_FIXTURE}", result.stdout)
        self.assertIn(f"FAIL {INVALID_FIXTURE}", result.stdout)

    def test_duplicate_keys_and_nonfinite_numbers_fail_before_schema_validation(self) -> None:
        malformed_instances = {
            "duplicate-key.json": '{"bundle_id":"first","bundle_id":"second"}',
            "nonfinite-number.json": '{"bundle_id":NaN}',
        }

        with tempfile.TemporaryDirectory() as directory:
            fixture_root = Path(directory)
            for name, fixture_content in malformed_instances.items():
                with self.subTest(name=name):
                    path = fixture_root / name
                    path.write_text(fixture_content, encoding="utf-8")
                    result = self._run(str(path))

                    self.assertEqual(
                        result.returncode,
                        1,
                        result.stdout + result.stderr,
                    )
                    self.assertIn(f"FAIL {path}", result.stdout)

    def test_top_level_compatibility_entrypoint_matches_domain_results(self) -> None:
        cases = [
            (),
            ("--fixtures",),
            ("--fixtures", str(INVALID_FIXTURE)),
            (str(VALID_FIXTURE),),
            (str(INVALID_FIXTURE),),
        ]

        for arguments in cases:
            with self.subTest(arguments=arguments):
                domain_result = self._run(*arguments)
                compatibility_result = self._run_validator(
                    TOP_LEVEL_VALIDATOR,
                    *arguments,
                )
                self.assertEqual(
                    compatibility_result.returncode,
                    domain_result.returncode,
                )
                self.assertEqual(compatibility_result.stdout, domain_result.stdout)
                self.assertEqual(compatibility_result.stderr, domain_result.stderr)

    def test_missing_arguments_is_usage_error(self) -> None:
        result = self._run()

        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn("No files provided", result.stderr)


if __name__ == "__main__":
    unittest.main()
