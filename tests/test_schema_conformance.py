import subprocess
import sys
import unittest


class SchemaConformanceTests(unittest.TestCase):
    def test_schema_conformance(self):
        self.assertEqual(subprocess.run([sys.executable, "tools/validate_schema_conformance.py"]).returncode, 0)
