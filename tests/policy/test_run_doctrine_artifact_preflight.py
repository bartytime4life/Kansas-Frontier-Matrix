import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_preflight_runner_produces_presence_input_with_missing_artifacts(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    outdir = tmp_path / "receipts"

    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n  - filename: b.pdf\n    doc_id: kfm://doc/b\n    status: missing\n""",
        encoding="utf-8",
    )

    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
        "--output-dir",
        str(outdir),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["check_returncode"] == 1
    assert payload["render_returncode"] == 0
    assert payload["presence_input"] == {"present": {"a.pdf": False, "b.pdf": False}}
    assert (outdir / "check_required_doctrine_artifacts.json").exists()


def test_preflight_runner_strict_mode_fails_when_artifacts_missing(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()

    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n""",
        encoding="utf-8",
    )

    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
        "--strict",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
