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
def test_provenance_sync_changed_snapshot_matches_fixture(tmp_path: Path):
    expected = _load(
        ROOT
        / "fixtures"
        / "contracts"
        / "v1"
        / "source"
        / "doctrine_artifact_provenance_check"
        / "valid"
        / "sync_changed.expected.json"
    )
    registry = tmp_path / "registry.yaml"
    registry.write_text(
        """required_doctrine_artifact_provenance:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    source_url: https://sources.example/a.pdf\n    status: pending\n""",
        encoding="utf-8",
    )
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    (artifacts / "a.pdf").write_bytes(b"%PDF-1.4\n")

    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "sync_doctrine_artifact_provenance_status.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
        "--write",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    for k, v in expected.items():
        assert payload[k] == v
    rewritten = registry.read_text(encoding="utf-8")
    assert "status: verified" in rewritten
    assert "verified_at:" in rewritten
