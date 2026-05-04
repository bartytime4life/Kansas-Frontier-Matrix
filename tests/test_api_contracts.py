import subprocess
import sys
import unittest


class ApiContractTests(unittest.TestCase):
    def test_api_contracts(self):
        self.assertEqual(subprocess.run([sys.executable, "tools/validate_api_contracts.py"]).returncode, 0)
