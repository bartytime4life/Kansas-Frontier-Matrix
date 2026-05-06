from __future__ import annotations

import json
from pathlib import Path


def write_layer_manifest(path: Path, candidate: dict) -> None:
    manifest = {
        "layer_id": candidate["layer_id"],
        "source_id": candidate["source_id"],
        "source_role": candidate["source_role"],
        "crs": candidate["crs"],
        "status": "candidate",
    }
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
