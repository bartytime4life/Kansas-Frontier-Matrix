from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools/validators/soil/promotion_gate.py"
FIXTURE_ROOT = ROOT / "tests/fixtures/soil"


def run_gate(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(path)],
        check=False,
        capture_output=True,
        text=True,
    )


def test_soil_promotion_gate_pass_fixture() -> None:
    result = run_gate(FIXTURE_ROOT / "valid/run_receipt_pass.json")
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["promotion_allowed"] is True


def test_soil_promotion_gate_review_fixture_blocked() -> None:
    result = run_gate(FIXTURE_ROOT / "policy/run_receipt_review_masked_pct.json")
    assert result.returncode != 0
    payload = json.loads(result.stdout)
    assert payload["promotion_allowed"] is False


def test_soil_promotion_gate_quarantine_and_fail_fixtures_blocked() -> None:
    blocked_fixtures = [
        "invalid/run_receipt_quarantine_zscore.json",
        "invalid/run_receipt_quarantine_residual.json",
        "invalid/run_receipt_fail_masked_pct.json",
    ]
    for fixture in blocked_fixtures:
        result = run_gate(FIXTURE_ROOT / fixture)
        assert result.returncode != 0, fixture
