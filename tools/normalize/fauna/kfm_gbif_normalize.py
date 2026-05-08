#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ALLOWED_PUBLIC_LICENSES = {"CC0", "CC-BY"}
RESTRICTED_PUBLIC_LICENSES = {"CC-BY-NC"}
REQUIRED_FIELDS = {
    "gbifID", "datasetKey", "eventDate", "decimalLatitude", "decimalLongitude",
    "basisOfRecord", "coordinateUncertaintyInMeters", "license"
}


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def compute_spec_hash(bundle: dict[str, Any]) -> str:
    stable = dict(bundle.get("spec", {}))
    payload = _canonical_json(stable).encode("utf-8")
    return f"sha256:{hashlib.sha256(payload).hexdigest()}"


def _normalize_license(raw: str) -> str:
    v = (raw or "").upper().replace(" ", "")
    if "CC0" in v:
        return "CC0"
    if "CC-BY-NC" in v:
        return "CC-BY-NC"
    if "CC-BY" in v:
        return "CC-BY"
    return "UNKNOWN"


def normalize_rows(rows: list[dict[str, str]], publication_target: str = "internal", allow_nc_override: bool = False) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    out: list[dict[str, Any]] = []
    dataset_keys: set[str] = set()
    licenses: set[str] = set()
    sensitive_exact = False
    for idx, row in enumerate(rows, start=1):
        missing = [f for f in REQUIRED_FIELDS if not row.get(f)]
        if missing:
            raise ValueError(f"row {idx}: missing required fields: {','.join(sorted(missing))}")
        sci = row.get("scientificName") or row.get("acceptedScientificName")
        if not sci:
            raise ValueError(f"row {idx}: missing scientificName/acceptedScientificName")

        lic = _normalize_license(row.get("license", ""))
        if lic == "UNKNOWN":
            raise ValueError(f"row {idx}: unknown license")

        lat = float(row["decimalLatitude"])
        lon = float(row["decimalLongitude"])
        sensitive = str(row.get("isSensitive", "false")).lower() == "true"
        if publication_target == "public" and sensitive:
            sensitive_exact = True

        out.append({
            "object_type": "KfmGbifOccurrence",
            "gbifID": row["gbifID"],
            "scientificName": sci,
            "occurrenceDate": row["eventDate"],
            "geopoint": {"lat": round(lat, 2) if publication_target == "public" else lat, "lon": round(lon, 2) if publication_target == "public" else lon},
            "kfm:dataset_key": row["datasetKey"],
            "basisOfRecord": row["basisOfRecord"],
            "geospatialPrecision": float(row["coordinateUncertaintyInMeters"]),
            "abundance": int(row["individualCount"]) if row.get("individualCount") else None,
            "license": lic,
            "sensitive": sensitive,
            "evidence_review_posture": "unreviewed_occurrence_claim"
        })
        dataset_keys.add(row["datasetKey"])
        licenses.add(lic)

    rights_posture = "QUARANTINE"
    if licenses.issubset(ALLOWED_PUBLIC_LICENSES):
        rights_posture = "PUBLIC_CANDIDATE" if publication_target == "public" else "INTERNAL_OK"
    elif licenses.issubset(ALLOWED_PUBLIC_LICENSES | RESTRICTED_PUBLIC_LICENSES):
        rights_posture = "RESTRICTED_LICENSE"
        if publication_target == "public" and ("CC-BY-NC" in licenses) and not allow_nc_override:
            raise ValueError("public output blocked: CC-BY-NC requires explicit override")

    if publication_target == "public" and len(out) < 10:
        raise ValueError("public aggregate denied: n < 10")
    if publication_target == "public" and sensitive_exact:
        raise ValueError("public exact coordinates denied for sensitive taxa")

    gate = {
        "dataset_keys": sorted(dataset_keys),
        "license_summary": sorted(licenses),
        "rights_posture": rights_posture,
        "sensitivity_posture": "SENSITIVE_PRESENT" if any(r["sensitive"] for r in out) else "NOT_SENSITIVE",
        "geoprivacy_transform": {
            "method": "grid_0.01deg_rounding" if publication_target == "public" else "none",
            "receipt": f"geoprivacy://kfm/gbif/{publication_target}/v1",
            "suppression_min_n": 10,
        },
    }
    return out, gate


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--query-predicate", required=True)
    p.add_argument("--download-key", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--publication-target", choices=["internal", "public"], default="internal")
    p.add_argument("--allow-public-nc-override", action="store_true")
    args = p.parse_args()
    try:
        rows = list(csv.DictReader(Path(args.input).read_text(encoding="utf-8").splitlines()))
        normalized, gate = normalize_rows(rows, args.publication_target, args.allow_public_nc_override)
        query_predicate = json.loads(Path(args.query_predicate).read_text(encoding="utf-8"))
        bundle = {
            "evidence_bundle_id": f"gbif-{args.download_key.lower()}",
            "source_system": "GBIF",
            "source_uri": "https://www.gbif.org/occurrence/search",
            "download_key": args.download_key,
            "query_predicate": query_predicate,
            "records_count": len(normalized),
            "dataset_keys": gate["dataset_keys"],
            "license_summary": gate["license_summary"],
            "rights_posture": gate["rights_posture"],
            "sensitivity_posture": gate["sensitivity_posture"],
            "geoprivacy_transform": gate["geoprivacy_transform"],
            "created_at": datetime.now(timezone.utc).isoformat(),
            "inputs": {"input_csv": args.input},
            "outputs": {"normalized_records": normalized, "publication_target": args.publication_target},
            "limitations": ["GBIF occurrences are observational claims, not confirmed species truth without review."],
            "spec": {
                "source_system": "GBIF", "source_uri": "https://www.gbif.org/occurrence/search",
                "download_key": args.download_key, "query_predicate": query_predicate,
                "dataset_keys": gate["dataset_keys"], "license_summary": gate["license_summary"],
                "rights_posture": gate["rights_posture"], "sensitivity_posture": gate["sensitivity_posture"],
                "geoprivacy_transform": gate["geoprivacy_transform"], "records_count": len(normalized),
            },
        }
        bundle["kfm:spec_hash"] = compute_spec_hash(bundle)
        Path(args.output).write_text(json.dumps(bundle, indent=2), encoding="utf-8")
    except Exception as exc:
        print(f"DENY: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
