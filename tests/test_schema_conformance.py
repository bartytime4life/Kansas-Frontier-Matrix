import subprocess
import unittest


class SchemaConformanceTests(unittest.TestCase):
    def test_schema_conformance(self):
        self.assertEqual(subprocess.run(["python", "tools/validate_schema_conformance.py"]).returncode, 0)
