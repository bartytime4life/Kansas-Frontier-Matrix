import hashlib
import subprocess
from pathlib import Path

RECEIPT = Path("release/dry_runs/promotion_dry_run_receipt.json")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    subprocess.run(["python", "tools/promotion_dry_run.py"], check=True)
    first = sha256(RECEIPT)
    subprocess.run(["python", "tools/promotion_dry_run.py"], check=True)
    second = sha256(RECEIPT)

    if first != second:
        print("FAIL", "promotion dry-run receipt is not deterministic")
        return 1

    print("PASS", "promotion dry-run receipt is deterministic")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
