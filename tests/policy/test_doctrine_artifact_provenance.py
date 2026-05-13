import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_doctrine_artifact_provenance_check_passes_for_registry():
    cmd = [sys.executable, str(ROOT / "scripts" / "maintenance" / "check_doctrine_artifact_provenance.py")]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["check"] == "required_doctrine_artifact_provenance"
    assert payload["entry_count"] == 3
    assert payload["result"] == "pass"


def test_doctrine_artifact_provenance_check_writes_receipt(tmp_path: Path):
    out = tmp_path / "provenance_check.json"
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_doctrine_artifact_provenance.py"),
        "--output",
        str(out),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    written = json.loads(out.read_text(encoding="utf-8"))
    assert written["result"] == "pass"
