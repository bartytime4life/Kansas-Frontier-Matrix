import json
import unittest
from pathlib import Path

from tests.subprocess_utils import assert_python_ok


class SyntheticReleaseDryRunTests(unittest.TestCase):
    def test_synthetic_release_dry_run_tool(self):
        assert_python_ok(self, ["tools/synthetic_release_dry_run.py"])

        receipt = json.loads(Path("release/dry_runs/synthetic_release_dry_run_receipt.json").read_text())
        self.assertEqual(receipt.get("publish_decision"), "REFUSE")
        self.assertEqual(receipt.get("reason"), "DRY_RUN_ONLY_REFUSES_PUBLISH")
        self.assertIn(receipt.get("result"), {"PASS", "FAIL"})
        self.assertTrue(receipt.get("gates"))


if __name__ == "__main__":
    unittest.main()
