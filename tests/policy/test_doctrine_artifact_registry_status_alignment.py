import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_registry_status_present_mismatch_fails(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts_dir = tmp_path / "artifacts"
    artifacts_dir.mkdir()
    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: sample.pdf\n    doc_id: kfm://doc/example\n    status: present\n""",
        encoding="utf-8",
    )

    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_required_doctrine_artifacts.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts_dir),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    payload = json.loads(res.stdout)
    assert payload["status_mismatches"] == ["sample.pdf"]
    assert payload["result"] == "fail"
