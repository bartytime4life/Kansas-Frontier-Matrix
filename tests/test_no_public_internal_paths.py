import subprocess
import unittest


class NoPublicInternalPathsTests(unittest.TestCase):
    def test_no_public_internal_paths(self):
        self.assertEqual(subprocess.run(["python", "tools/check_no_public_internal_paths.py"]).returncode, 0)
