import unittest
from tests.subprocess_utils import assert_python_ok
class T(unittest.TestCase):
    def test_packet_validator(self): assert_python_ok(self,['tools/validators/validate_hydrology_manual_review_packet.py'])
