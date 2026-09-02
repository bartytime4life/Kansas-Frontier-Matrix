from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
DOMAIN_SCRIPT = ROOT / "tools/validators/domains/people-dna-land/validate_source_descriptor.py"
SHARED_SCRIPT = ROOT / "tools/validators/sources/validate_source_descriptor.py"


class PeopleDnaLandSourceDescriptorEntrypointTests(unittest.TestCase):
    def run_validator(
        self, script: Path, *args: str
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(script), *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_shared_fixture_polarity_is_preserved(self) -> None:
        shared = self.run_validator(SHARED_SCRIPT, "--fixtures")
        domain = self.run_validator(DOMAIN_SCRIPT, "--fixtures")

        self.assertEqual(shared.returncode, 0, shared.stdout + shared.stderr)
        self.assertEqual(domain.returncode, 0, domain.stdout + domain.stderr)
        self.assertEqual(domain.stdout, shared.stdout)
        self.assertIn("OK ", domain.stdout)
        self.assertIn("EXPECTED_FAIL ", domain.stdout)

    def test_no_input_fails_closed(self) -> None:
        result = self.run_validator(DOMAIN_SCRIPT)
        self.assertEqual(result.returncode, 2)
        self.assertIn("No files provided", result.stderr)

    def test_fixture_mode_rejects_explicit_candidates(self) -> None:
        result = self.run_validator(
            DOMAIN_SCRIPT, "--fixtures", "explicit-candidate.json"
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn(
            "Cannot combine --fixtures with explicit SourceDescriptor files",
            result.stderr,
        )


    def test_abbreviated_fixture_options_fail_closed(self) -> None:
        for length in range(3, len("--fixtures")):
            abbreviation = "--fixtures"[:length]
            with self.subTest(abbreviation=abbreviation):
                result = self.run_validator(
                    DOMAIN_SCRIPT, abbreviation, "explicit-candidate.json"
                )
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn(
                    f"Abbreviated --fixtures option is not allowed: {abbreviation}",
                    result.stderr,
                )


if __name__ == "__main__":
    unittest.main()
