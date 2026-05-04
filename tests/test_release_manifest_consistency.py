import unittest

from tests.subprocess_utils import assert_python_ok


class ReleaseManifestConsistencyTests(unittest.TestCase):
    def test_validate_release_manifest_consistency(self):
        assert_python_ok(self, ["tools/validate_release_manifest_consistency.py"])
