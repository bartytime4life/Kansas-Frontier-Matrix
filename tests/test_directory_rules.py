import unittest

from tests.subprocess_utils import assert_python_ok


class DirectoryRulesTests(unittest.TestCase):
    def test_check_directory_rules(self):
        assert_python_ok(self, ["tools/check_directory_rules.py"])
