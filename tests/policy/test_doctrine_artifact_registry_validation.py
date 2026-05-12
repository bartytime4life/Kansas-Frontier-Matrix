import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_checker_fails_on_duplicate_filenames(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: dup.pdf\n    doc_id: kfm://doc/1\n    status: missing\n  - filename: dup.pdf\n    doc_id: kfm://doc/2\n    status: missing\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_required_doctrine_artifacts.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode != 0
    assert "duplicate filename" in (res.stderr + res.stdout)


def test_sync_fails_on_invalid_status(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: unknown_state\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "sync_doctrine_artifact_registry_status.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode != 0
    assert "invalid status" in (res.stderr + res.stdout)


def test_checker_fails_on_missing_doc_id(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: noid.pdf\n    status: missing\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_required_doctrine_artifacts.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode != 0
    assert "missing doc_id" in (res.stderr + res.stdout)
