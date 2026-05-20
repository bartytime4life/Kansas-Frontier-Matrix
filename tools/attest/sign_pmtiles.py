#!/usr/bin/env python3
"""Create a development PMSIG payload shell for PMTiles artifacts.

This does not perform production signing. Wire this to repository-approved COSE
signing and private-key custody before using for publication.
"""
from __future__ import annotations

import argparse
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
    p.add_argument("--pmidx", required=True, type=Path)
    p.add_argument("--spec-hash", required=True)
    p.add_argument("--key-id", default="NEEDS_VERIFICATION")
    p.add_argument("--out", required=True, type=Path)
    args = p.parse_args()

    pmidx = json.loads(args.pmidx.read_text(encoding="utf-8"))
    payload = {
        "schema_version": "kfm.pmsig.v1",
        "subject": {
            "pmtiles_sha256": sha256_file(args.pmtiles),
            "pmidx_merkle_root": pmidx["merkle"]["root"],
            "spec_hash": args.spec_hash,
        },
        "key_id": args.key_id,
        "signature": "DEVELOPMENT_PLACEHOLDER_NOT_A_VALID_COSE_SIGNATURE",
    }
    args.out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
