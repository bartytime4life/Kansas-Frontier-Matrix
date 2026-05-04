import unittest

from tests.subprocess_utils import assert_python_ok


class SourceLedgerTests(unittest.TestCase):
    def test_check_source_ledger(self):
        assert_python_ok(self, ["tools/check_source_ledger.py"])
