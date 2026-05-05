#!/usr/bin/env python3
"""Emit a deterministic catalog validation receipt from validator decisions."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--catalog-matrix", required=True)
    parser.add_argument("--release-manifest", required=True)
    parser.add_argument("--stac-decision", required=True, choices=["ALLOW", "DENY", "ERROR"])
    parser.add_argument("--dcat-decision", required=True, choices=["ALLOW", "DENY", "ERROR"])
    parser.add_argument("--matrix-decision", required=True, choices=["ALLOW", "DENY", "ERROR"])
    parser.add_argument("--closure-decision", required=True, choices=["ALLOW", "DENY", "ERROR"])
    parser.add_argument("--out", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    decisions = {
        "stac": args.stac_decision,
        "dcat": args.dcat_decision,
        "catalog_matrix": args.matrix_decision,
        "release_catalog_closure": args.closure_decision,
    }

    if any(value == "ERROR" for value in decisions.values()):
        decision = "ERROR"
    elif all(value == "ALLOW" for value in decisions.values()):
        decision = "PASS"
    else:
        decision = "DENY"

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "schema": "kfm.catalog.validation_report.v1",
        "validator": "tools/validators/catalog/emit_catalog_validation_receipt.py",
        "decision": decision,
        "checked_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "release_id": args.release_id,
        "inputs": {
            "catalog_matrix": args.catalog_matrix,
            "release_manifest": args.release_manifest,
        },
        "checks": decisions,
    }

    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE: {out_path}")


if __name__ == "__main__":
    main()
