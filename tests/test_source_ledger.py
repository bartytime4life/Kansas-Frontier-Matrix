import subprocess
import sys
import unittest


class SourceLedgerTests(unittest.TestCase):
    def test_source_ledger_check(self):
        result = subprocess.run(
            [sys.executable, "tools/check_source_ledger.py"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
