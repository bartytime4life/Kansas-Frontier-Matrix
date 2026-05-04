import json
import unittest
from pathlib import Path

from tests.subprocess_utils import assert_python_ok, run_python


class ReleaseDryRunTests(unittest.TestCase):
    def test_promotion_dry_run(self):
        assert_python_ok(self, ["tools/promotion_dry_run.py"])

    def test_source_ledger_check(self):
        assert_python_ok(self, ["tools/check_source_ledger.py"])

    def test_dry_run_receipt_written(self):
        result = run_python(["tools/promotion_dry_run.py"])
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        receipt = json.loads(Path("release/dry_runs/promotion_dry_run_receipt.json").read_text())
        self.assertEqual(receipt["result"], "PASS")
        self.assertEqual(receipt["source_manifest"], "fixtures/release/release_manifest.valid.json")
        self.assertEqual(receipt["timestamp_utc"], "1970-01-01T00:00:00+00:00")
