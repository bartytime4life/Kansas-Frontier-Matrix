import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_doctrine_registry_alignment_passes_for_current_registries():
    cmd = [sys.executable, str(ROOT / "scripts" / "maintenance" / "check_doctrine_registry_alignment.py")]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["check"] == "doctrine_registry_alignment"
    assert payload["result"] == "pass"


def test_doctrine_registry_alignment_detects_missing_and_extra(tmp_path: Path):
    req = tmp_path / "required.yaml"
    prov = tmp_path / "prov.yaml"
    req.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n""",
        encoding="utf-8",
    )
    prov.write_text(
        """required_doctrine_artifact_provenance:\n  - filename: b.pdf\n    doc_id: kfm://doc/b\n    source_url: https://sources.example/b.pdf\n    status: pending\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_doctrine_registry_alignment.py"),
        "--required-registry",
        str(req),
        "--provenance-registry",
        str(prov),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    payload = json.loads(res.stdout)
    assert payload["missing_in_provenance"] == ["a.pdf"]
    assert payload["extra_in_provenance"] == ["b.pdf"]
