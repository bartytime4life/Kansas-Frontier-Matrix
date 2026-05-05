#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return f"sha256:{hashlib.sha256(canonical(value).encode()).hexdigest()}"


def compute_spec_hash(doc: dict[str, Any]) -> str:
    stable = {k: v for k, v in doc.items() if k != "created_at"}
    return digest(stable)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--aggregation-unit", choices=["county", "huc12", "grid"], required=True)
    ap.add_argument("--suppression-threshold", type=int, default=10)
    ap.add_argument("--output", required=True)
    ap.add_argument("--receipt-output", required=True)
    args = ap.parse_args()

    bundle = json.loads(Path(args.input).read_text())
    rows = bundle["outputs"]["normalized_records"]
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[(row.get("taxonKey", "unknown"), row["scientificName"])].append(row)

    aggregates = []
    suppressed = 0
    for (taxon_key, name), grp in groups.items():
        n = len(grp)
        if n < args.suppression_threshold:
            suppressed += 1
            continue
        dates = sorted((g["occurrenceDate"][:10] for g in grp))
        agg = {
            "aggregate_id": f"gbif-agg-{bundle['download_key'].lower()}-{taxon_key}",
            "source_system": "GBIF",
            "source_evidence_bundle_id": bundle["evidence_bundle_id"],
            "download_key": bundle["download_key"],
            "query_predicate_hash": digest(bundle["query_predicate"]),
            "aggregation_unit": args.aggregation_unit,
            "taxon_key": str(taxon_key),
            "scientific_name": name,
            "observation_count": n,
            "record_count": n,
            "date_range": {"start": dates[0], "end": dates[-1]},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[-99.0, 37.0], [-94.0, 37.0], [-94.0, 40.0], [-99.0, 40.0], [-99.0, 37.0]]]
            },
            "geometry_role": "generalized_public_area",
            "rights_posture": "public_allowed" if bundle.get("rights_posture") in {"PUBLIC_CANDIDATE", "INTERNAL_OK"} else "restricted",
            "sensitivity_posture": "restricted" if bundle.get("sensitivity_posture") == "SENSITIVE_PRESENT" else "public_generalized",
            "geoprivacy_receipt_ref": "",
            "limitations": ["GBIF occurrence aggregates are observational signals, not confirmed species presence without review posture."]
        }
        agg["kfm:spec_hash"] = compute_spec_hash(agg)
        aggregates.append(agg)

    receipt = {
        "receipt_id": f"geoprivacy-{bundle['download_key'].lower()}",
        "source_evidence_bundle_id": bundle["evidence_bundle_id"],
        "transform_name": "kfm_gbif_public_aggregate",
        "transform_version": "v1",
        "input_record_count": len(rows),
        "output_aggregate_count": len(aggregates),
        "suppressed_count": suppressed,
        "suppression_threshold": args.suppression_threshold,
        "removed_fields": ["decimalLatitude", "decimalLongitude"],
        "generalized_geometry": True,
        "reviewer_required": True,
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    receipt["kfm:spec_hash"] = compute_spec_hash(receipt)

    for agg in aggregates:
        agg["geoprivacy_receipt_ref"] = receipt["receipt_id"]

    Path(args.output).write_text(json.dumps(aggregates, indent=2))
    Path(args.receipt_output).write_text(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
