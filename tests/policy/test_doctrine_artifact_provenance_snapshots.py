import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_provenance_check_placeholder_snapshot_matches_fixture():
    expected = _load(
        ROOT
        / "fixtures"
        / "contracts"
        / "v1"
        / "source"
        / "doctrine_artifact_provenance_check"
        / "invalid"
        / "placeholder_urls.expected.json"
    )
    cmd = [sys.executable, str(ROOT / "scripts" / "maintenance" / "check_doctrine_artifact_provenance.py")]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    payload = json.loads(res.stdout)
    for k, v in expected.items():
        assert payload[k] == v


def test_provenance_sync_no_change_snapshot_matches_fixture():
    expected = _load(
        ROOT
        / "fixtures"
        / "contracts"
        / "v1"
        / "source"
        / "doctrine_artifact_provenance_check"
        / "valid"
        / "sync_no_change.expected.json"
    )
    cmd = [sys.executable, str(ROOT / "scripts" / "maintenance" / "sync_doctrine_artifact_provenance_status.py")]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    for k, v in expected.items():
        assert payload[k] == v
