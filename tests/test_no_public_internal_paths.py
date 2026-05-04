import unittest

from tests.subprocess_utils import assert_python_ok


class NoPublicInternalPathsTests(unittest.TestCase):
    def test_check_no_public_internal_paths(self):
        assert_python_ok(self, ["tools/check_no_public_internal_paths.py"])
