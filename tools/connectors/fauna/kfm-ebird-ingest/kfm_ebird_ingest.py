#!/usr/bin/env python3
"""Scaffold CLI for KFM eBird ingest Layer 1."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

FIELD_MAPPING = {
    "sampling_event_identifier": "kfm:dataset_key",
    "observation_date": "occurrenceDate",
    "latitude": "decimalLatitude",
    "longitude": "decimalLongitude",
    "observation_count": "individualCount",
    "species_taxon_id": "taxonKey",
    "basisOfRecord": "HumanObservation",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(2)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="kfm-ebird-ingest",
        description="Layer 1 scaffold for KFM eBird ingest adapter.",
    )
    parser.add_argument("--ebd-file", required=True, help="Path to eBird EBD file")
    parser.add_argument(
        "--source-uri",
        help="Optional source URI. Defaults to file://<ebd-file>",
    )
    parser.add_argument("--filter", required=True, dest="predicate", help="Filter predicate")
    parser.add_argument(
        "--aggregate",
        required=True,
        choices=("county", "huc12"),
        help="Aggregation grain",
    )
    parser.add_argument(
        "--suppression",
        type=int,
        default=10,
        help="Suppression threshold (minimum 10)",
    )
    parser.add_argument("--emit", required=True, help="Output path for scaffold artifact")
    parser.add_argument("--dry-run", action="store_true", help="Emit scaffold EvidenceBundle only")
    return parser.parse_args(argv)


def canonical_json(value: dict[str, Any]) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def compute_spec_hash(spec: dict[str, Any]) -> str:
    digest = hashlib.sha256(canonical_json(spec).encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def build_spec(args: argparse.Namespace, source_uri: str) -> dict[str, Any]:
    return {
        "adapter": "kfm-ebird-ingest",
        "aggregate": args.aggregate,
        "mapping": FIELD_MAPPING,
        "query_predicate": args.predicate,
        "source_uri": source_uri,
        "suppression": args.suppression,
        "version": "v1",
    }


def build_evidence_bundle(spec: dict[str, Any], spec_hash: str) -> dict[str, Any]:
    return {
        "schema_version": "v1",
        "object_type": "EvidenceBundle",
        "source_uri": spec["source_uri"],
        "query_predicate": spec["query_predicate"],
        "mapping": spec["mapping"],
        "kfm:spec_hash": spec_hash,
    }


def main() -> None:
    args = parse_args(sys.argv[1:])
    if args.suppression < 10:
        fail("--suppression must be >= 10")

    source_uri = args.source_uri or Path(args.ebd_file).resolve().as_uri()

    if not args.dry_run:
        fail("Layer 1 scaffold supports --dry-run only; full ingest not implemented")

    spec = build_spec(args, source_uri)
    spec_hash = compute_spec_hash(spec)
    bundle = build_evidence_bundle(spec, spec_hash)

    emit_path = Path(args.emit)
    emit_path.parent.mkdir(parents=True, exist_ok=True)
    emit_path.write_text(json.dumps(bundle, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote dry-run EvidenceBundle scaffold: {emit_path}")


if __name__ == "__main__":
    main()
