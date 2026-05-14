import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SCRIPT = ROOT / "scripts" / "maintenance" / "enforce_doctrine_preflight_gates.sh"


def test_enforce_doctrine_preflight_gates_returns_nonzero_when_provenance_fails():
    cmd = [str(SCRIPT), "--stable-filenames"]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    assert '"provenance_returncode": 1' in res.stdout


def test_enforce_doctrine_preflight_gates_invokes_strict_gate_flags():
    script = SCRIPT.read_text(encoding="utf-8")
    assert "--strict" in script
    assert "--strict-provenance" in script
    assert "--require-consumer-readiness" in script
    assert '"$@"' in script
