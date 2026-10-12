from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = (
    ROOT
    / "tools"
    / "validators"
    / "security"
    / "validate_security_scan_receipt.py"
)
FIXTURE = ROOT / "fixtures" / "security" / "scan_receipts" / "valid.json"
COMMIT = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def test_valid_security_scan_receipt() -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(VALIDATOR),
            str(FIXTURE),
            "--expected-commit",
            COMMIT,
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "SECURITY_SCAN_RECEIPT_VALID" in result.stdout


def test_security_scan_receipt_rejects_other_commit() -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(VALIDATOR),
            str(FIXTURE),
            "--expected-commit",
            "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2
    assert "SUBJECT_MISMATCH" in result.stdout
