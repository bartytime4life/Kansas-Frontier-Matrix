import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    cmd = [sys.executable, str(ROOT / "tools/validate_fixtures.py")]
    result = subprocess.run(cmd, cwd=ROOT)
    if result.returncode != 0:
        print("FAIL fixture validation")
        return result.returncode
    print("PASS fixture validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
