from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def write_run_receipt(path: Path, candidate: dict) -> None:
    receipt = {
        "run_id": f"{candidate['layer_id']}-fixture",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_id": candidate["source_id"],
        "source_role": candidate["source_role"],
    }
    path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
