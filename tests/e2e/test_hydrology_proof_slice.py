"""End-to-end run of the synthetic Hydrology proof slice through its readiness lane."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_proof_slice_lane_passes_from_a_fresh_process() -> None:
    completed = subprocess.run(
        [sys.executable, "tools/readiness/run_lane.py", "proof-slice"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=180,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    result = json.loads(completed.stdout)
    assert result["status"] == "PASS"
    assert result["reason"] == "SYNTHETIC_PROOF_SLICE_PASSED"
    assert result["cases"] == 14
    assert set(result["effects"].values()) == {False}
