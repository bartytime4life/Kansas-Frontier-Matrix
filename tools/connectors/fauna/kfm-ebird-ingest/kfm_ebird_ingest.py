#!/usr/bin/env python3
"""Scaffold CLI for KFM eBird ingest Layer 2."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from typing import Any

from packages.evidence.evidencebundle_hash import compute_spec_hash

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
    parser = argparse.ArgumentParser(prog="kfm-ebird-ingest", description="Layer 2 scaffold for KFM eBird ingest adapter.")
    parser.add_argument("--ebd-file", required=True, help="Path to eBird EBD file")
    parser.add_argument("--source-uri", help="Optional source URI. Defaults to file://<ebd-file>")
    parser.add_argument("--filter", required=True, dest="predicate", help="Filter predicate")
    parser.add_argument("--aggregate", required=True, choices=("county", "huc12"), help="Aggregation grain")
    parser.add_argument("--suppression", type=int, default=10, help="Suppression threshold (minimum 10)")
    parser.add_argument("--emit", required=True, help="Output path for scaffold artifact")
    parser.add_argument("--dry-run", action="store_true", help="Emit scaffold EvidenceBundle only")
    return parser.parse_args(argv)


def build_evidence_bundle(args: argparse.Namespace, source_uri: str) -> dict[str, Any]:
    bundle: dict[str, Any] = {
        "schema_version": "v1",
        "object_type": "EvidenceBundle",
        "domain": "fauna",
        "source": "ebird",
        "source_uri": source_uri,
        "query_predicate": args.predicate,
        "aggregate": args.aggregate,
        "suppression_min_n": args.suppression,
        "mapping": FIELD_MAPPING,
    }
    bundle["kfm:spec_hash"] = compute_spec_hash(bundle)
    return bundle


def main() -> None:
    args = parse_args(sys.argv[1:])
    if args.suppression < 10:
        fail("--suppression must be >= 10")

    source_uri = args.source_uri or Path(args.ebd_file).resolve().as_uri()

    if not args.dry_run:
        fail("Layer scaffold supports --dry-run only; full ingest not implemented")

    bundle = build_evidence_bundle(args, source_uri)

    emit_path = Path(args.emit)
    emit_path.parent.mkdir(parents=True, exist_ok=True)
    emit_path.write_text(json.dumps(bundle, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote dry-run EvidenceBundle scaffold: {emit_path}")


if __name__ == "__main__":
    main()
