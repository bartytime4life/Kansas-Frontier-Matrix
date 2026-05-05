#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

def _canon(v: Any) -> str:
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def _hash(v: Any) -> str:
    return f"sha256:{hashlib.sha256(_canon(v).encode()).hexdigest()}"

def compute_spec_hash(doc: dict[str, Any]) -> str:
    stable = {k: v for k, v in doc.items() if k != "created_at"}
    for key in ["aggregate_ids", "geoprivacy_receipt_refs", "dataset_keys", "taxa", "geographies", "limitations"]:
        if key in stable and isinstance(stable[key], list):
            stable[key] = sorted(stable[key], key=lambda x: _canon(x))
    return _hash(stable)

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--aggregates", required=True)
    ap.add_argument("--receipt", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    aggs = json.loads(Path(args.aggregates).read_text())
    receipt = json.loads(Path(args.receipt).read_text())
    if not isinstance(aggs, list) or not aggs:
        raise SystemExit("aggregates must be non-empty list")
    rref = receipt.get("receipt_id", "")
    groups: dict[tuple[str, str, str], list[dict[str, Any]]] = {}
    for a in aggs:
        key = (a["source_evidence_bundle_id"], a["download_key"], a["query_predicate_hash"])
        groups.setdefault(key, []).append(a)
    out = []
    for (bundle, dkey, qhash), grp in groups.items():
        rights = grp[0].get("rights_posture", "restricted")
        sens = grp[0].get("sensitivity_posture", "restricted")
        release = "public_candidate" if rights == "public_allowed" and sens != "restricted" else "blocked"
        entry = {
            "catalog_entry_id": f"gbif-catalog-{dkey.lower()}-{qhash.split(':')[-1][:12]}",
            "domain": "fauna",
            "source_system": "GBIF",
            "artifact_type": "public_occurrence_aggregate",
            "lifecycle_state": "CATALOG",
            "source_evidence_bundle_id": bundle,
            "download_key": dkey,
            "query_predicate_hash": qhash,
            "aggregate_ids": sorted({g["aggregate_id"] for g in grp}),
            "geoprivacy_receipt_refs": sorted({(x.get("geoprivacy_receipt_ref") or rref) for x in grp}),
            "dataset_keys": sorted({g.get("dataset_key", "") for g in grp if g.get("dataset_key")}),
            "taxa": sorted([{"taxon_key": g["taxon_key"], "scientific_name": g["scientific_name"]} for g in grp], key=lambda x: (x["taxon_key"], x["scientific_name"])),
            "geographies": sorted([{"aggregation_unit": g["aggregation_unit"], "geography_id": g["geography_id"], "display_name": g["display_name"]} for g in grp], key=lambda x: (x["aggregation_unit"], x["geography_id"])),
            "rights_posture": rights,
            "sensitivity_posture": sens,
            "release_posture": release,
            "kfm:spec_hash": "",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "limitations": grp[0].get("limitations", []),
        }
        entry["kfm:spec_hash"] = compute_spec_hash(entry)
        out.append(entry)
    Path(args.output).write_text(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
