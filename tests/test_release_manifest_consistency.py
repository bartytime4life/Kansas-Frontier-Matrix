import subprocess
import sys
import unittest


class ReleaseManifestConsistencyTests(unittest.TestCase):
    def test_release_manifest_consistency(self):
        result = subprocess.run(
            [sys.executable, "tools/validate_release_manifest_consistency.py"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
