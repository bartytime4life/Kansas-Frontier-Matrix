import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_doctrine_artifact_policy_exists_and_is_non_empty():
    policy_path = ROOT / "policy" / "source" / "doctrine_artifact_required.rego"
    text = policy_path.read_text(encoding="utf-8")
    assert "package" in text
    assert "deny" in text


def test_required_doctrine_artifact_check_fails_until_artifacts_admitted():
    cmd = [sys.executable, str(ROOT / "scripts" / "maintenance" / "check_required_doctrine_artifacts.py")]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    assert "missing_count" in res.stdout
