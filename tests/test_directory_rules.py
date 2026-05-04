import subprocess
import sys
import unittest


class DirectoryRulesTests(unittest.TestCase):
    def test_directory_rules(self):
        self.assertEqual(subprocess.run([sys.executable, "tools/check_directory_rules.py"]).returncode, 0)
