"""Roads/Rail/Trade STB Class I snapshot de-duplication stays held until STB ingest exists.

Planned intent (docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md): STB Class I snapshot-week de-duplication (Pass-10 C10-05 named tension).

ingest_stb_class1.py holds with STB_CLASS1_INGEST_NOT_IMPLEMENTED, so there are no
snapshots to de-duplicate. The hold fails as soon as the stage is implemented.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
STAGE = "pipelines/domains/roads-rail-trade/ingest_stb_class1.py"
STAGE_REASON = "STB_CLASS1_INGEST_NOT_IMPLEMENTED"


def test_ingest_stb_class1_stage_still_holds() -> None:
    completed = subprocess.run(
        [sys.executable, str(REPO_ROOT / STAGE)], capture_output=True, text=True, check=False, timeout=10,
    )
    assert completed.returncode == 2, "STB_SNAPSHOT_DEDUP_NOT_IMPLEMENTED: the stage no longer holds; write the real tests for it."
    assert json.loads(completed.stdout)["reason_code"] == STAGE_REASON
