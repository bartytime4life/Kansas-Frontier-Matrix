import subprocess
import unittest


class ReleaseDryRunTests(unittest.TestCase):
    def test_promotion_dry_run(self):
        self.assertEqual(subprocess.run(["python", "tools/promotion_dry_run.py"]).returncode, 0)

    def test_source_ledger_check(self):
        self.assertEqual(subprocess.run(["python", "tools/check_source_ledger.py"]).returncode, 0)
