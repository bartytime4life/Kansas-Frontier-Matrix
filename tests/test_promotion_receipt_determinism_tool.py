import subprocess
import sys
import unittest


class PromotionReceiptDeterminismToolTests(unittest.TestCase):
    def test_determinism_tool(self):
        self.assertEqual(subprocess.run([sys.executable, "tools/check_promotion_receipt_determinism.py"]).returncode, 0)
