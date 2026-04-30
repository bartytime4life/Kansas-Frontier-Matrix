#!/usr/bin/env python3
"""KFM eBird ingest Layer 3 CLI."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from packages.evidence.evidencebundle_hash import compute_spec_hash

GOVERNED_FILTER = "complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10"
FIELD_MAPPING = {
    "sampling_event_identifier": "kfm:dataset_key",
    "observation_date": "occurrenceDate",
    "latitude": "decimalLatitude",
    "longitude": "decimalLongitude",
    "observation_count": "individualCount",
    "species_taxon_id": "taxonKey",
    "basisOfRecord": "HumanObservation",
}
REQUIRED_COLUMNS = {
    "sampling_event_identifier": {"sampling_event_identifier", "sampling_event_id"},
    "observation_date": {"observation_date"},
    "latitude": {"latitude"},
    "longitude": {"longitude"},
    "observation_count": {"observation_count"},
    "protocol_type": {"protocol_type"},
    "duration_min": {"duration_min", "duration_minutes"},
    "distance_km": {"distance_km", "effort_distance_km"},
    "number_observers": {"number_observers"},
    "complete": {"complete", "all_species_reported"},
    "species_taxon_id": {"species_taxon_id"},
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(2)


def normalize_header(value: str) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", value.strip().lower())).strip("_")


def normalize_filter(predicate: str) -> str:
    p = predicate.lower().replace(" ", "")
    p = p.replace('"', "'")
    p = p.replace("all_species_reported", "complete")
    p = p.replace("duration_minutes", "duration_min")
    p = p.replace("effort_distance_km", "distance_km")
    return p


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="kfm-ebird-ingest", description="Layer 3 KFM eBird ingest adapter")
    parser.add_argument("--ebd-file")
    parser.add_argument("--source-uri")
    parser.add_argument("--filter", dest="predicate")
    parser.add_argument("--aggregate", required=True, choices=("county", "huc12"))
    parser.add_argument("--suppression", type=int, default=10)
    parser.add_argument("--emit")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--out")
    parser.add_argument("--quarantine")
    parser.add_argument("--manifest")
    parser.add_argument("--format", choices=("jsonl", "csv"), default="jsonl")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--strict", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--allow-nonstandard-columns", action="store_true")
    return parser.parse_args(argv)


def resolve_columns(headers: list[str]) -> tuple[dict[str, str], list[str], list[str]]:
    normalized = {normalize_header(h): h for h in headers}
    resolved, missing, present = {}, [], []
    for req, aliases in REQUIRED_COLUMNS.items():
        found = next((a for a in aliases if a in normalized), None)
        if found:
            resolved[req] = normalized[found]
            present.append(req)
        else:
            missing.append(req)
    return resolved, present, missing


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return f"sha256:{digest.hexdigest()}"


def main() -> None:
    args = parse_args(sys.argv[1:])
    if args.suppression < 10:
        fail("--suppression must be >= 10")
    if args.limit is not None and args.limit <= 0:
        fail("--limit must be positive")
    if not args.predicate:
        fail("--filter is required")
    if normalize_filter(args.predicate) != normalize_filter(GOVERNED_FILTER):
        fail("Only governed_ebird_checklist_qa_v1 predicate is executable")
    if not args.ebd_file or not args.emit:
        fail("--ebd-file and --emit are required")
    ebd = Path(args.ebd_file)
    if not ebd.exists():
        fail(f"Input file not found: {ebd}")

    if not args.dry_run:
        for opt in ("out", "quarantine", "manifest"):
            if not getattr(args, opt):
                fail(f"--{opt} is required for non-dry-run")
        for p in (Path(args.out), Path(args.quarantine)):
            if "data/published" in p.as_posix():
                fail(f"Restricted outputs cannot be under data/published: {p}")

    source_uri = args.source_uri or ebd.resolve().as_uri()
    bundle = {
        "schema_version": "v1", "object_type": "EvidenceBundle", "domain": "fauna", "source": "ebird",
        "source_uri": source_uri, "query_predicate": args.predicate, "aggregate": args.aggregate,
        "suppression_min_n": args.suppression, "mapping": FIELD_MAPPING,
    }
    bundle["kfm:spec_hash"] = compute_spec_hash(bundle)
    emit = Path(args.emit); emit.parent.mkdir(parents=True, exist_ok=True)
    emit.write_text(json.dumps(bundle, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.dry_run:
        print(f"Wrote dry-run EvidenceBundle scaffold: {emit}")
        return

    outp, quar, manifest = Path(args.out), Path(args.quarantine), Path(args.manifest)
    outp.parent.mkdir(parents=True, exist_ok=True); quar.parent.mkdir(parents=True, exist_ok=True); manifest.parent.mkdir(parents=True, exist_ok=True)
    counts = Counter()
    filter_counts = Counter()
    started = datetime.utcnow().isoformat() + "Z"
    rows_written = 0

    with ebd.open("r", encoding="utf-8", newline="") as f, outp.open("w", encoding="utf-8", newline="") as out_f, quar.open("w", encoding="utf-8", newline="") as q_f:
        reader = csv.DictReader(f, delimiter="\t")
        if not reader.fieldnames:
            fail("Missing EBD header row")
        resolved, present, missing = resolve_columns(reader.fieldnames)
        if missing and args.strict:
            fail(f"Missing required columns in strict mode: {', '.join(missing)}")

        for i, row in enumerate(reader, start=2):
            if args.limit and counts["rows_seen"] >= args.limit:
                break
            counts["rows_seen"] += 1
            reasons = []
            try:
                rec = {k: row.get(v, "") for k, v in resolved.items()}
                complete = str(rec.get("complete", "")).strip().lower() in {"1", "true", "yes", "y"}
                protocol = str(rec.get("protocol_type", "")).strip()
                dur = float(rec.get("duration_min") or 0)
                dist = float(rec.get("distance_km") or 0)
                party = int(float(rec.get("number_observers") or 0))
                lat = float(rec.get("latitude") or "nan")
                lon = float(rec.get("longitude") or "nan")
                dt = date.fromisoformat(str(rec.get("observation_date", "")).strip())
            except Exception:
                reasons.append("malformed_row")
                counts["rows_failed_malformed"] += 1
                filter_counts["malformed_row"] += 1
                q_f.write(json.dumps({"policy_label": "restricted", "raw_row_number": i, "reason_codes": reasons}) + "\n")
                counts["rows_quarantined"] += 1
                continue
            if not rec.get("sampling_event_identifier", "").strip(): reasons.append("missing_sampling_event_identifier")
            if not rec.get("species_taxon_id", "").strip(): reasons.append("missing_species_taxon_id")
            if not -90 <= lat <= 90: reasons.append("invalid_latitude")
            if not -180 <= lon <= 180: reasons.append("invalid_longitude")
            if not complete: reasons.append("incomplete_checklist")
            if protocol.lower() == "incidental": reasons.append("incidental_protocol")
            if dur < 5: reasons.append("duration_below_minimum")
            if dist > 5: reasons.append("distance_above_maximum")
            if party > 10: reasons.append("observers_above_maximum")

            obs_raw = str(rec.get("observation_count", "")).strip()
            individual = int(obs_raw) if obs_raw.isdigit() else None
            if individual is None:
                counts["observation_count_unknown"] += 1

            if reasons:
                counts["rows_failed_quality_filter"] += 1
                counts["rows_quarantined"] += 1
                for r in reasons: filter_counts[r] += 1
                q = {"policy_label": "restricted", "raw_row_number": i, "reason_codes": sorted(set(reasons))}
                for k in ("sampling_event_identifier", "observation_date", "species_taxon_id", "protocol_type", "duration_min", "distance_km", "number_observers", "complete"):
                    q[k] = rec.get(k)
                q_f.write(json.dumps(q) + "\n")
                continue

            out = {
                "schema_version": "v1", "object_type": "Occurrence", "domain": "fauna", "source": "ebird", "policy_label": "restricted",
                "basisOfRecord": "HumanObservation", "kfm:dataset_key": rec["sampling_event_identifier"], "occurrenceDate": dt.isoformat(),
                "decimalLatitude": lat, "decimalLongitude": lon, "individualCount": individual, "taxonKey": rec["species_taxon_id"],
                "observerEffort": {"protocolType": protocol, "durationMinutes": dur, "distanceKm": dist, "partySize": party},
                "evidence_bundle_uri": source_uri, "kfm:spec_hash": bundle["kfm:spec_hash"], "raw_row_number": i,
            }
            if individual is None:
                out["observation_count_raw"] = obs_raw
            out_f.write(json.dumps(out) + "\n")
            counts["rows_accepted"] += 1
            rows_written += 1

    counts["rows_failed_required_columns"] = 0
    manifest_obj = {
        "schema_version": "v1", "object_type": "IngestManifest", "domain": "fauna", "source": "ebird", "policy_label": "restricted",
        "source_uri": source_uri, "ebd_file": str(ebd), "input_sha256": sha256_file(ebd), "output_path": str(outp), "output_sha256": sha256_file(outp),
        "quarantine_path": str(quar), "quarantine_sha256": sha256_file(quar), "evidencebundle_path": str(emit), "evidencebundle_sha256": sha256_file(emit),
        "query_predicate": args.predicate, "aggregate": args.aggregate, "suppression_min_n": args.suppression, "kfm:spec_hash": bundle["kfm:spec_hash"],
        "started_at": started, "completed_at": datetime.utcnow().isoformat() + "Z", "counts": dict(counts), "filter_counts": dict(filter_counts),
        "required_columns_present": present, "required_columns_missing": missing, "executable_filter_name": "governed_ebird_checklist_qa_v1",
    }
    manifest.write_text(json.dumps(manifest_obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote accepted rows: {rows_written}; quarantine: {counts['rows_quarantined']}; manifest: {manifest}")


if __name__ == "__main__":
    main()
