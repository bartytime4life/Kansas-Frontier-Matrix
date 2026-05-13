import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_preflight_summary_consistency_validator_passes(tmp_path: Path):
    summary_path = tmp_path / "summary.json"
    run_cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--stable-filenames",
        "--output-dir",
        str(tmp_path / "receipts"),
    ]
    run = subprocess.run(run_cmd, cwd=ROOT, capture_output=True, text=True)
    assert run.returncode == 0
    summary_path.write_text(run.stdout, encoding="utf-8")

    cmd = [
        sys.executable,
        str(ROOT / "tools" / "validators" / "source" / "validate_doctrine_preflight_summary_consistency.py"),
        str(summary_path),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["result"] == "pass"


def test_preflight_summary_consistency_validator_fails_on_mismatch(tmp_path: Path):
    summary_path = tmp_path / "summary.json"
    summary = {
        "artifact_paths": {"check_receipt": "a", "provenance_sync_receipt": "b", "presence_output": None},
        "check_receipt": "x",
        "provenance_sync_receipt": "b",
        "presence_output": None,
        "artifact_digests": {"check_receipt": "1", "provenance_sync_receipt": "2", "presence_output": None},
        "check_receipt_sha256": "0",
        "provenance_sync_receipt_sha256": "2",
        "presence_output_sha256": None,
    }
    summary_path.write_text(json.dumps(summary), encoding="utf-8")

    cmd = [
        sys.executable,
        str(ROOT / "tools" / "validators" / "source" / "validate_doctrine_preflight_summary_consistency.py"),
        str(summary_path),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    payload = json.loads(res.stdout)
    assert payload["result"] == "fail"
    assert payload["errors"]


def test_preflight_summary_consistency_normalized_only_mode_fails_with_legacy_fields(tmp_path: Path):
    summary_path = tmp_path / "summary.json"
    summary = {
        "artifact_paths": {"check_receipt": "a", "provenance_sync_receipt": "b", "presence_output": None},
        "artifact_digests": {"check_receipt": "1", "provenance_sync_receipt": "2", "presence_output": None},
        "check_receipt": "a",
        "provenance_sync_receipt": "b",
        "presence_output": None,
        "check_receipt_sha256": "1",
        "provenance_sync_receipt_sha256": "2",
        "presence_output_sha256": None,
    }
    summary_path.write_text(json.dumps(summary), encoding="utf-8")
    cmd = [
        sys.executable,
        str(ROOT / "tools" / "validators" / "source" / "validate_doctrine_preflight_summary_consistency.py"),
        str(summary_path),
        "--require-normalized-only",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    payload = json.loads(res.stdout)
    assert payload["result"] == "fail"
    assert any("legacy fields present" in e for e in payload["errors"])


def test_preflight_summary_consistency_normalized_only_mode_passes_without_legacy_fields(tmp_path: Path):
    summary_path = tmp_path / "summary.json"
    summary = {
        "artifact_paths": {"check_receipt": "a", "provenance_sync_receipt": "b", "presence_output": None},
        "artifact_digests": {"check_receipt": "1", "provenance_sync_receipt": "2", "presence_output": None},
    }
    summary_path.write_text(json.dumps(summary), encoding="utf-8")
    cmd = [
        sys.executable,
        str(ROOT / "tools" / "validators" / "source" / "validate_doctrine_preflight_summary_consistency.py"),
        str(summary_path),
        "--require-normalized-only",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["result"] == "pass"
