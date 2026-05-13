import json
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
    assert res.returncode == 2
    payload = json.loads(res.stdout)
    assert payload["result"] == "error"
    assert "duplicate filename" in payload["error"]


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
    assert res.returncode == 2
    payload = json.loads(res.stdout)
    assert payload["result"] == "error"
    assert "invalid status" in payload["error"]


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
    assert res.returncode == 2
    payload = json.loads(res.stdout)
    assert payload["result"] == "error"
    assert "missing doc_id" in payload["error"]


def test_checker_fails_when_required_block_missing(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    registry.write_text("other_block:\n  - filename: a.pdf\n", encoding="utf-8")
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_required_doctrine_artifacts.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 2
    payload = json.loads(res.stdout)
    assert payload["result"] == "error"
    assert "required_doctrine_artifacts block" in payload["error"]


def test_checker_fails_when_required_block_empty(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    registry.write_text("required_doctrine_artifacts:\n", encoding="utf-8")
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_required_doctrine_artifacts.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 2
    payload = json.loads(res.stdout)
    assert payload["result"] == "error"
    assert "has no entries" in payload["error"]


def test_checker_accepts_comments_and_blank_lines(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    registry.write_text(
        """# comment\n\nrequired_doctrine_artifacts:\n  # entry\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n""",
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
    assert res.returncode == 1
    payload = json.loads(res.stdout)
    assert payload["result"] == "fail"


def test_checker_handles_missing_registry_file_as_structured_error(tmp_path: Path):
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    missing_registry = tmp_path / "nope.yaml"
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_required_doctrine_artifacts.py"),
        "--registry",
        str(missing_registry),
        "--artifacts-dir",
        str(artifacts),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 2
    payload = json.loads(res.stdout)
    assert payload["result"] == "error"
