"""The candidate validator distinguishes documented identity fixtures."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
SCRIPT = ROOT / "tools/validators/domains/settlements-infrastructure/validate_domain_feature_identity.py"
FIXTURES = ROOT / "fixtures/domains/settlements-infrastructure/domain_feature_identity"


class IdentityValidatorTests(unittest.TestCase):
    def run_check(self, path: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(SCRIPT), str(path)], cwd=ROOT,
                              capture_output=True, text=True, check=False)

    def test_documented_fixtures(self) -> None:
        for name in ("valid_settlement.json", "valid_infrastructure_asset.json"):
            result = self.run_check(FIXTURES / name)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result = self.run_check(FIXTURES / "invalid_collapsed_object_family.json")
        self.assertEqual(result.returncode, 1)
        self.assertIn("OBJECT_FAMILY_NOT_DISTINGUISHABLE", result.stdout)

    def test_missing_source_role_and_time_are_rejected(self) -> None:
        value = json.loads((FIXTURES / "valid_settlement.json").read_text())
        del value["source_role"]
        value["temporal_scope"] = {}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(value))
            result = self.run_check(path)
        self.assertEqual(result.returncode, 1)
        self.assertIn("REQUIRED_TEXT_INVALID:source_role", result.stdout)
        self.assertIn("TEMPORAL_SCOPE_MISSING", result.stdout)

    def test_symlink_and_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            value = root / "candidate.json"
            value.write_text('{"id":"a","id":"b"}')
            duplicate = self.run_check(value)
            self.assertEqual(duplicate.returncode, 1)
            self.assertIn("INPUT_ERROR:ValueError", duplicate.stdout)
            link = root / "link.json"
            link.symlink_to(FIXTURES / "valid_settlement.json")
            linked = self.run_check(link)
            self.assertEqual(linked.returncode, 1)
            self.assertIn("INPUT_ERROR:ValueError", linked.stdout)


if __name__ == "__main__":
    unittest.main()
