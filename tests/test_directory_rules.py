import subprocess
import unittest


class DirectoryRulesTests(unittest.TestCase):
    def test_directory_rules(self):
        self.assertEqual(subprocess.run(["python", "tools/check_directory_rules.py"]).returncode, 0)
