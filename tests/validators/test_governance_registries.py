from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = (
    ROOT
    / "tools"
    / "validators"
    / "governance"
    / "validate_governance_registries.py"
)


def test_governance_registries_are_structurally_valid() -> None:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "all"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "GOVERNANCE_REGISTRY_VALID" in result.stdout
