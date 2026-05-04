import hashlib
import subprocess
import unittest
from pathlib import Path

RECEIPT = Path("release/dry_runs/promotion_dry_run_receipt.json")


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class PromotionReceiptIdempotenceTests(unittest.TestCase):
    def test_receipt_is_stable_across_runs(self):
        subprocess.run(["python", "tools/promotion_dry_run.py"], check=True)
        h1 = file_sha256(RECEIPT)
        subprocess.run(["python", "tools/promotion_dry_run.py"], check=True)
        h2 = file_sha256(RECEIPT)
        self.assertEqual(h1, h2)
