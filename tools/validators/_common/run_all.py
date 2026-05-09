import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    scripts = sorted(root.glob("validate_*.py"))
    for script in scripts:
        cmd = [sys.executable, str(script), "--fixtures"]
        result = subprocess.run(cmd)
        if result.returncode != 0:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
