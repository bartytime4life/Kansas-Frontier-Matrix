import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.validators.source.validate_doctrine_preflight_summary_consistency import validate

ROOT = Path(__file__).resolve().parents[2]


def _normalized_summary() -> dict:
    return {
        "artifact_paths": {
            "check_receipt": "check.json",
            "provenance_sync_receipt": "provenance.json",
            "presence_output": None,
        },
        "artifact_digests": {
            "check_receipt": "1" * 64,
            "provenance_sync_receipt": "2" * 64,
            "presence_output": None,
        },
    }


@pytest.mark.parametrize("name", ["artifact_paths", "artifact_digests"])
def test_normalized_only_rejects_missing_map(name):
    summary = _normalized_summary()
    del summary[name]
    assert validate(summary, True) == [f"{name} must be an object"]


@pytest.mark.parametrize("name", ["artifact_paths", "artifact_digests"])
@pytest.mark.parametrize("value", [None, [], ["entry"], "", "entry", 0, False])
def test_normalized_only_rejects_non_object_map(name, value):
    summary = _normalized_summary()
    summary[name] = value
    assert validate(summary, True) == [f"{name} must be an object"]


@pytest.mark.parametrize("name", ["artifact_paths", "artifact_digests"])
@pytest.mark.parametrize("key", ["check_receipt", "provenance_sync_receipt", "presence_output"])
def test_normalized_only_requires_each_map_key_even_when_nullable(name, key):
    summary = _normalized_summary()
    del summary[name][key]
    assert validate(summary, True) == [f"{name} missing keys: {key}"]


@pytest.mark.parametrize("name", ["artifact_paths", "artifact_digests"])
def test_normalized_only_rejects_unregistered_map_key(name):
    summary = _normalized_summary()
    summary[name]["unregistered"] = None
    assert validate(summary, True) == [f"{name} unexpected keys: unregistered"]


@pytest.mark.parametrize("strict", [False, True])
@pytest.mark.parametrize("summary", [None, [], ["entry"], "entry", 0, False])
def test_consistency_rejects_non_object_summary(summary, strict):
    assert validate(summary, strict) == ["summary must be an object"]


@pytest.mark.parametrize("name", ["artifact_paths", "artifact_digests"])
def test_compatibility_rejects_non_object_map_without_raising(name):
    summary = _normalized_summary()
    summary[name] = ["entry"]
    assert validate(summary) == [f"{name} must be an object"]


def test_normalized_only_keeps_explicit_optional_nulls():
    assert validate(_normalized_summary(), True) == []


def test_compatibility_map_absence_retains_historical_semantics():
    # Full summary shape remains the separate schema validator's responsibility.
    assert validate({}) == []


@pytest.mark.parametrize("summary", [{}, {"artifact_paths": {}, "artifact_digests": {}}, []])
def test_normalized_only_cli_returns_finite_failure_for_missing_structure(tmp_path, summary):
    path = tmp_path / "summary.json"
    path.write_text(json.dumps(summary), encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools/validators/source/validate_doctrine_preflight_summary_consistency.py"),
         "--require-normalized-only", str(path)],
        cwd=ROOT, capture_output=True, text=True,
    )
    assert result.returncode == 1
    assert result.stderr == ""
    payload = json.loads(result.stdout)
    assert payload["check"] == "doctrine_preflight_summary_consistency"
    assert payload["result"] == "fail"
    assert payload["errors"]


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


def test_normalized_only_preflight_output_passes_normalized_only_validator(tmp_path: Path):
    summary_path = tmp_path / "summary.json"
    run_cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--stable-filenames",
        "--emit-normalized-only",
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
        "--require-normalized-only",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["result"] == "pass"
