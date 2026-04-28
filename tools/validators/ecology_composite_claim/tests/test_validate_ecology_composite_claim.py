from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.validators.ecology_composite_claim.validate_ecology_composite_claim import (
    ValidationError,
    validate,
)


FIXTURE_ROOT = Path(__file__).resolve().parent.parent / "fixtures"


def _load(rel: str) -> dict:
    return json.loads((FIXTURE_ROOT / rel).read_text(encoding="utf-8"))


def test_validate_accepts_valid_cite_claim() -> None:
    doc = _load("valid/cite_resolved.json")
    warnings = validate(doc)
    assert warnings == []


def test_validate_rejects_single_domain() -> None:
    doc = _load("invalid/single_domain.json")
    with pytest.raises(ValidationError, match="at least two domains"):
        validate(doc)


def test_validate_rejects_cite_without_evidence() -> None:
    doc = _load("invalid/cite_missing_evidence.json")
    with pytest.raises(ValidationError, match="at least one evidence item"):
        validate(doc)


def test_cli_report_json_failure() -> None:
    cmd = [
        sys.executable,
        "-m",
        "tools.validators.ecology_composite_claim",
        str(FIXTURE_ROOT / "invalid" / "single_domain.json"),
        "--report-json",
    ]
    proc = subprocess.run(cmd, check=False, text=True, capture_output=True)
    assert proc.returncode == 1
    payload = json.loads(proc.stdout)
    assert payload["result"] == "fail"


def test_cli_allow_message_success() -> None:
    cmd = [
        sys.executable,
        "-m",
        "tools.validators.ecology_composite_claim",
        str(FIXTURE_ROOT / "valid" / "cite_resolved.json"),
    ]
    proc = subprocess.run(cmd, check=False, text=True, capture_output=True)
    assert proc.returncode == 0
    assert "ALLOW:" in proc.stdout
