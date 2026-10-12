from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools/validators/genealogy/screen_living_persons.py"
FIXTURE_ROOT = (
    ROOT
    / "fixtures/contracts/v1/domains/people-dna-land"
    / "historical_person_place_event_resolution"
)


class LivingPersonScreenTests(unittest.TestCase):
    def run_screen(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_fixture_profile_preserves_historical_allow_and_living_deny(self) -> None:
        result = self.run_screen("--fixtures")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("historical_allowed=3", result.stdout)
        self.assertIn("living_denied=1", result.stdout)

    def test_synthetic_living_person_candidate_is_denied(self) -> None:
        path = FIXTURE_ROOT / "invalid" / "living_person_denied.json"
        result = self.run_screen(str(path))

        self.assertEqual(result.returncode, 1)
        self.assertIn("reason=LIVING_PERSON_DENIED", result.stdout)
        self.assertNotIn("fixture://person/alpha", result.stdout)

    def test_valid_historical_candidate_is_allowed(self) -> None:
        path = FIXTURE_ROOT / "valid" / "high_anchor.json"
        result = self.run_screen(str(path))

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("LIVING_PERSON_SCREEN_ALLOWED", result.stdout)
        self.assertIn("scope=historical_synthetic", result.stdout)


    def test_fixture_mode_rejects_abbreviated_option_names(self) -> None:
        exact = "--fixtures"
        for length in range(3, len(exact)):
            option = exact[:length]
            with self.subTest(option=option):
                result = self.run_screen(option)
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertIn("unrecognized arguments", result.stderr)


if __name__ == "__main__":
    unittest.main()
