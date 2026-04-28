from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/reproducibility/scripts/compare_receipts.py"
CASE = ROOT / "tests/reproducibility/cases/first_public_safe_receipt_rerun.json"
RECEIPT_A = ROOT / "tests/reproducibility/fixtures/valid/receipt_run_a.json"
RECEIPT_B = ROOT / "tests/reproducibility/fixtures/valid/receipt_run_b.json"
RECEIPT_DRIFT = ROOT / "tests/reproducibility/fixtures/invalid/receipt_spec_hash_drift.json"


def run_compare(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", str(SCRIPT), *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def test_allowed_drift_only_is_pass() -> None:
    result = run_compare(str(RECEIPT_A), str(RECEIPT_B), "--case", str(CASE))
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["decision"] == "PASS"
    assert payload["first_differing_field"] == "generated_at"


def test_required_field_drift_is_fail_closed() -> None:
    result = run_compare(str(RECEIPT_A), str(RECEIPT_DRIFT), "--case", str(CASE))
    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["decision"] == "FAIL_CLOSED"
    assert payload["first_differing_field"] == "generated_at"
    assert payload["required_mismatch_count"] == 1
