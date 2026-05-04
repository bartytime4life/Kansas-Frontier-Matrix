import subprocess
import unittest


class ApiContractTests(unittest.TestCase):
    def test_api_contracts(self):
        self.assertEqual(subprocess.run(["python", "tools/validate_api_contracts.py"]).returncode, 0)
