import subprocess
import sys
import unittest


class NoPublicInternalPathsTests(unittest.TestCase):
    def test_no_public_internal_paths(self):
        self.assertEqual(subprocess.run([sys.executable, "tools/check_no_public_internal_paths.py"]).returncode, 0)
