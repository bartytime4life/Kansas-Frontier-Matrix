import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_doctrine_artifact_test_bundle_script_passes():
    cmd = [str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_test_suite.sh")]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0, res.stdout + res.stderr
    assert "OK doctrine_artifact_preflight_summary fixtures" in res.stdout
