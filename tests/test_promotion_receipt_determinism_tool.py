import subprocess
import unittest


class PromotionReceiptDeterminismToolTests(unittest.TestCase):
    def test_determinism_tool(self):
        self.assertEqual(subprocess.run(["python", "tools/check_promotion_receipt_determinism.py"]).returncode, 0)
