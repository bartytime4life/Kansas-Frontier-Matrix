import unittest

from tests.subprocess_utils import assert_python_ok


class FixtureSchemaMappingTests(unittest.TestCase):
    def test_validate_fixture_schema_mapping(self):
        assert_python_ok(self, ["tools/validate_fixture_schema_mapping.py"])
