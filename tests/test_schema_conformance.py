import unittest

from tests.subprocess_utils import assert_python_ok


class SchemaConformanceTests(unittest.TestCase):
    def test_validate_schema_conformance(self):
        assert_python_ok(self, ["tools/validate_schema_conformance.py"])
