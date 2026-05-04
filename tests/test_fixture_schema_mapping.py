import subprocess
import sys
import unittest


class FixtureSchemaMappingTests(unittest.TestCase):
    def test_fixture_schema_mapping(self):
        self.assertEqual(subprocess.run([sys.executable, "tools/validate_fixture_schema_mapping.py"]).returncode, 0)
