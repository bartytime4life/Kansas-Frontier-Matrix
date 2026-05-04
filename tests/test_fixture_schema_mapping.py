import subprocess
import unittest


class FixtureSchemaMappingTests(unittest.TestCase):
    def test_fixture_schema_mapping(self):
        self.assertEqual(subprocess.run(["python", "tools/validate_fixture_schema_mapping.py"]).returncode, 0)
