import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_sync_registry_marks_present_when_artifact_exists(tmp_path: Path):
    artifacts_dir = tmp_path / "artifacts"
    artifacts_dir.mkdir()
    (artifacts_dir / "a.pdf").write_text("x", encoding="utf-8")

    registry = tmp_path / "registry.yaml"
    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n  - filename: b.pdf\n    doc_id: kfm://doc/b\n    status: present\n""",
        encoding="utf-8",
    )

    output = tmp_path / "sync_receipt.json"
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "sync_doctrine_artifact_registry_status.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts_dir),
        "--output",
        str(output),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0

    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["changed_count"] == 2
    edited = registry.read_text(encoding="utf-8")
    assert "status: present" in edited
    assert "status: missing" in edited


def test_sync_dry_run_does_not_mutate_registry(tmp_path: Path):
    artifacts_dir = tmp_path / "artifacts"
    artifacts_dir.mkdir()
    (artifacts_dir / "a.pdf").write_text("x", encoding="utf-8")
    registry = tmp_path / "registry.yaml"
    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n""",
        encoding="utf-8",
    )
    before = registry.read_text(encoding="utf-8")
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "sync_doctrine_artifact_registry_status.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts_dir),
        "--dry-run",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["dry_run"] is True
    assert payload["changed_count"] == 1
    assert registry.read_text(encoding="utf-8") == before


def test_sync_fail_on_change_returns_one(tmp_path: Path):
    artifacts_dir = tmp_path / "artifacts"
    artifacts_dir.mkdir()
    registry = tmp_path / "registry.yaml"
    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: present\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "sync_doctrine_artifact_registry_status.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts_dir),
        "--dry-run",
        "--fail-on-change",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
