import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_enforce_doctrine_preflight_gates_returns_nonzero_when_provenance_fails():
    cmd = [str(ROOT / "scripts" / "maintenance" / "enforce_doctrine_preflight_gates.sh"), "--stable-filenames"]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    assert '"provenance_returncode": 1' in res.stdout
