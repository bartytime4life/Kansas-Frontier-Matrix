#!/usr/bin/env python3
"""Build a minimal KFM PMTiles run receipt."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--pmtiles", required=True, type=Path)
    p.add_argument("--spec-hash", required=True)
    p.add_argument("--builder-id", default="NEEDS_VERIFICATION")
    p.add_argument("--out", required=True, type=Path)
    args = p.parse_args()

    now = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    receipt = {
        "schema_version": "kfm.runreceipt.pmtiles.v1",
        "type": "https://slsa.dev/provenance/v1",
        "subject": [{"name": str(args.pmtiles), "digest": {"sha256": sha256_file(args.pmtiles).split(":", 1)[1]}}],
        "predicate": {
            "buildDefinition": {
                "buildType": "kfm/pmtiles/build@v1",
                "externalParameters": {"spec_hash": args.spec_hash},
            },
            "runDetails": {
                "builder": {"id": args.builder_id},
                "metadata": {"finishedOn": now},
            },
        },
    }
    args.out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
