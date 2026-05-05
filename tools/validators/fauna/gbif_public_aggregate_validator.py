#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

REPO = Path(__file__).resolve().parents[3]
AGG_SCHEMA = json.loads((REPO / "schemas/fauna/gbif_public_aggregate.schema.json").read_text())
REC_SCHEMA = json.loads((REPO / "schemas/receipts/geoprivacy_receipt.schema.json").read_text())

def deny(msg: str) -> None:
    print(f"DENY: {msg}", file=sys.stderr)
    sys.exit(1)

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--aggregate", required=True)
    ap.add_argument("--receipt")
    args = ap.parse_args()
    aggs = json.loads(Path(args.aggregate).read_text())
    if not isinstance(aggs, list):
        deny("aggregate file must be a list")
    for agg in aggs:
        errs = list(Draft202012Validator(AGG_SCHEMA).iter_errors(agg))
        if errs: deny(errs[0].message)
        if "decimalLatitude" in agg or "decimalLongitude" in agg: deny("exact coordinate fields present")
        if agg.get("observation_count", 0) < 10: deny("observation_count < 10")
        if agg.get("rights_posture") != "public_allowed": deny("rights_posture not public_allowed")
        if agg.get("sensitivity_posture") == "restricted": deny("sensitivity_posture restricted")
        if not agg.get("source_evidence_bundle_id") or not agg.get("download_key"): deny("missing source_evidence_bundle_id/download_key")
        if not agg.get("geoprivacy_receipt_ref"): deny("missing geoprivacy receipt")
    if args.receipt:
        receipt = json.loads(Path(args.receipt).read_text())
        errs = list(Draft202012Validator(REC_SCHEMA).iter_errors(receipt))
        if errs: deny(errs[0].message)
    print("ALLOW")

if __name__ == "__main__":
    main()
