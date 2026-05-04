import unittest

from tests.subprocess_utils import assert_python_ok


class ApiContractTests(unittest.TestCase):
    def test_validate_api_contracts(self):
        assert_python_ok(self, ["tools/validate_api_contracts.py"])
