import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_sync_doctrine_artifact_provenance_status_no_change_when_artifacts_missing(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    registry.write_text(
        """required_doctrine_artifact_provenance:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    source_url: https://sources.example/a.pdf\n    status: pending\n""",
        encoding="utf-8",
    )
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()

    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "sync_doctrine_artifact_provenance_status.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["result"] == "no_change"
    assert payload["changed_count"] == 0


def test_sync_doctrine_artifact_provenance_status_write_marks_verified(tmp_path: Path):
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
    assert payload["result"] == "changed"
    content = registry.read_text(encoding="utf-8")
    assert "status: verified" in content
    assert "verified_at:" in content
