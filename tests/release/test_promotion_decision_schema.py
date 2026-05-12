import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_promotion_decision_fixtures_validate():
    cmd = [sys.executable, str(ROOT / "tools/validators/release/validate_promotion_decision.py"), "--fixtures"]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0, res.stdout + res.stderr
