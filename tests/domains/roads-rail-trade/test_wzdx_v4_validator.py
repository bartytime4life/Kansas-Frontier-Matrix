"""Roads/Rail/Trade WZDx v4.x validation stays held until WZDx ingest exists.

Planned intent (docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md): WZDx v4.x roadworks validator and transformer (fail-closed schema gate).

ingest_wzdx_v4.py holds with WZDX_INGEST_NOT_IMPLEMENTED and no WZDx validator
exists. The hold fails as soon as either changes, so validator tests land with it.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
STAGE = "pipelines/domains/roads-rail-trade/ingest_wzdx_v4.py"
STAGE_REASON = "WZDX_INGEST_NOT_IMPLEMENTED"
ABSENT_GLOB = "tools/validators/**/*wzdx*"


def test_ingest_wzdx_v4_stage_still_holds() -> None:
    completed = subprocess.run(
        [sys.executable, str(REPO_ROOT / STAGE)], capture_output=True, text=True, check=False, timeout=10,
    )
    assert completed.returncode == 2, "WZDX_V4_VALIDATOR_NOT_IMPLEMENTED: the stage no longer holds; write the real tests for it."
    assert json.loads(completed.stdout)["reason_code"] == STAGE_REASON


def test_wzdx_validator_is_not_implemented_yet() -> None:
    found = sorted(p.relative_to(REPO_ROOT).as_posix() for p in REPO_ROOT.glob(ABSENT_GLOB))
    assert found == [], "WZDX_V4_VALIDATOR_NOT_IMPLEMENTED: " + ", ".join(found) + " now exists; replace this hold with its tests."
