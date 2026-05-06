from __future__ import annotations

import json
from pathlib import Path


def write_catalog_refs(path: Path, candidate: dict) -> None:
    refs = {
        "collection": "habitat",
        "item_id": candidate["layer_id"],
        "source_id": candidate["source_id"],
    }
    path.write_text(json.dumps(refs, indent=2) + "\n", encoding="utf-8")
