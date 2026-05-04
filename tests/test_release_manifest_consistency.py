import subprocess
import unittest


class ReleaseManifestConsistencyTests(unittest.TestCase):
    def test_release_manifest_consistency(self):
        self.assertEqual(subprocess.run(["python", "tools/validate_release_manifest_consistency.py"]).returncode, 0)
