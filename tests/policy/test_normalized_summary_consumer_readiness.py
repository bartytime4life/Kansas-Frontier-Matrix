import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_normalized_summary_consumer_readiness_passes_for_repo_registry():
    cmd = [sys.executable, str(ROOT / "scripts" / "maintenance" / "check_normalized_summary_consumer_readiness.py")]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["check"] == "normalized_summary_consumer_readiness"
    assert payload["result"] == "pass"


def test_normalized_summary_consumer_readiness_detects_invalid_entry(tmp_path: Path):
    bad = tmp_path / "readiness.yaml"
    bad.write_text(
        """normalized_summary_consumers:\n  - consumer: a\n    owner: team\n    status: wrong\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_normalized_summary_consumer_readiness.py"),
        "--registry",
        str(bad),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    payload = json.loads(res.stdout)
    assert payload["result"] == "fail"
    assert payload["errors"]


def test_normalized_summary_consumer_readiness_require_all_validated_fails(tmp_path: Path):
    reg = tmp_path / "readiness.yaml"
    reg.write_text(
        """normalized_summary_consumers:\n  - consumer: a\n    owner: team\n    status: pending\n    validated_utc: 2026-05-13\n    evidence: ci\n    notes: n\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_normalized_summary_consumer_readiness.py"),
        "--registry",
        str(reg),
        "--require-all-validated",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    payload = json.loads(res.stdout)
    assert payload["require_all_validated"] is True
    assert any("non-validated consumers" in e for e in payload["errors"])
