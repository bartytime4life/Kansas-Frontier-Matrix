import json
import subprocess
import unittest
from pathlib import Path


class ReleaseDryRunTests(unittest.TestCase):
    def test_promotion_dry_run(self):
        self.assertEqual(subprocess.run(["python", "tools/promotion_dry_run.py"]).returncode, 0)

    def test_source_ledger_check(self):
        self.assertEqual(subprocess.run(["python", "tools/check_source_ledger.py"]).returncode, 0)

    def test_dry_run_receipt_written(self):
        subprocess.run(["python", "tools/promotion_dry_run.py"], check=True)
        receipt = json.loads(Path("release/dry_runs/promotion_dry_run_receipt.json").read_text())
        self.assertEqual(receipt["result"], "PASS")
        self.assertEqual(receipt["source_manifest"], "fixtures/release/release_manifest.valid.json")
        self.assertEqual(receipt["timestamp_utc"], "1970-01-01T00:00:00+00:00")
