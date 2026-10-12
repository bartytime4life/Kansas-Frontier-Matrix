from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
SCRIPT = ROOT / "tools/validators/domains/people-dna-land/validate_evidence_bundle.py"


class PeopleDnaLandEvidenceBundleEntrypointTests(unittest.TestCase):
    def run_validator(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_shared_fixture_polarity_is_exercised(self) -> None:
        result = self.run_validator("--fixtures")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK ", result.stdout)
        self.assertIn("EXPECTED_FAIL ", result.stdout)

    def test_no_input_fails_closed(self) -> None:
        result = self.run_validator()
        self.assertEqual(result.returncode, 2)
        self.assertIn("No files provided", result.stderr)

    def test_fixture_mode_rejects_explicit_candidates(self) -> None:
        result = self.run_validator("--fixtures", "explicit-candidate.json")
        self.assertEqual(result.returncode, 2)
        self.assertIn(
            "Cannot combine --fixtures with explicit EvidenceBundle files",
            result.stderr,
        )


    def test_abbreviated_fixture_options_fail_closed(self) -> None:
        for length in range(3, len("--fixtures")):
            abbreviation = "--fixtures"[:length]
            with self.subTest(abbreviation=abbreviation):
                result = self.run_validator(abbreviation, "explicit-candidate.json")
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn(
                    f"Abbreviated --fixtures option is not allowed: {abbreviation}",
                    result.stderr,
                )


if __name__ == "__main__":
    unittest.main()
