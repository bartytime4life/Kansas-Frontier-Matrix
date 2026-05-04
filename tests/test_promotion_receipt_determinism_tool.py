import unittest

from tests.subprocess_utils import assert_python_ok


class PromotionReceiptDeterminismToolTests(unittest.TestCase):
    def test_check_promotion_receipt_determinism(self):
        assert_python_ok(self, ["tools/check_promotion_receipt_determinism.py"])
