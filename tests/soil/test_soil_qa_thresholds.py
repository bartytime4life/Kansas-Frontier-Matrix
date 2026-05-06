from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools/validators/soil/qa_thresholds.py"
FIXTURE_ROOT = ROOT / "tests/fixtures/soil"


def run_validator(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(path)],
        check=False,
        capture_output=True,
        text=True,
    )


def test_soil_qa_pass_fixture_exits_zero() -> None:
    result = run_validator(FIXTURE_ROOT / "valid/run_receipt_pass.json")
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["decision"] == "pass"


def test_soil_qa_invalid_fixtures_exit_nonzero() -> None:
    invalid_fixtures = [
        "invalid/run_receipt_quarantine_zscore.json",
        "invalid/run_receipt_quarantine_residual.json",
        "invalid/run_receipt_fail_masked_pct.json",
    ]
    for fixture in invalid_fixtures:
        result = run_validator(FIXTURE_ROOT / fixture)
        assert result.returncode != 0, fixture
