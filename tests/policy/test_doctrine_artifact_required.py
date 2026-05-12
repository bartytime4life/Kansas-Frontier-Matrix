import json
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
    payload = json.loads(res.stdout)
    assert payload["check"] == "required_doctrine_artifacts"
    assert payload["missing_count"] >= 1
    assert payload["result"] == "fail"
    assert isinstance(payload["present"], dict)
    assert payload["status_mismatches"] == []


def test_required_doctrine_artifact_check_writes_receipt(tmp_path: Path):
    out = tmp_path / "doctrine_artifact_check.json"
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_required_doctrine_artifacts.py"),
        "--output",
        str(out),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    written = json.loads(out.read_text(encoding="utf-8"))
    assert written["check"] == "required_doctrine_artifacts"
    assert written["result"] == "fail"
    assert isinstance(written["present"], dict)
    assert isinstance(written["status_mismatches"], list)
