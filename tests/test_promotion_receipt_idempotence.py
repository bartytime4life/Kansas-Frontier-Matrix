import hashlib
import unittest
from pathlib import Path

from tests.subprocess_utils import assert_python_ok

RECEIPT = Path("release/dry_runs/promotion_dry_run_receipt.json")


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class PromotionReceiptIdempotenceTests(unittest.TestCase):
    def test_receipt_is_stable_across_runs(self):
        assert_python_ok(self, ["tools/promotion_dry_run.py"])
        h1 = file_sha256(RECEIPT)
        assert_python_ok(self, ["tools/promotion_dry_run.py"])
        h2 = file_sha256(RECEIPT)
        self.assertEqual(h1, h2)
