#!/usr/bin/env python3
"""Capture or replay the NOAA Storm Events Kansas pilot into the existing private lifecycle store.

Writes immutable quarantine bytes, receipts, and WORK candidates. Never writes
PROCESSED/PUBLISHED or an active-release pointer, and never marks review approved.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes
from connectors.noaa.src.noaa.storm_events_capture import LISTING_KEY, Capture, capture, object_limit, object_url
from pipelines.domains.hazards.storm_events_normalize import normalize_capture
from pipelines.domains.hazards.storm_events_validate import validate_candidate
from tools.local_data.file_io import read_regular
from tools.local_data.manage import external_root, init_store, store_lock
from tools.local_data.water_pilot import immutable

DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
LANE = "noaa-storm-events"
MANIFEST_BYTES = 64 * 1024


def object_path(root: Path, digest: str) -> Path:
    if not isinstance(digest, str) or not DIGEST.fullmatch(digest):
        raise ValueError("INVALID_OBJECT_DIGEST")
    return root / "data/quarantine" / LANE / "objects/sha256" / digest.split(":")[1] / "payload"


def _check_object_closure(manifest: dict, objects: dict) -> None:
    """Objects must be exactly the manifest's pages, each hashing to its key and within its limit."""
    pages = manifest.get("pages")
    try:
        expected = {page["sha256"]: object_limit(page["key"]) for page in pages}
    except (KeyError, TypeError):
        raise ValueError("CAPTURE_OBJECT_CLOSURE_INVALID") from None
    if (not isinstance(objects, dict) or set(objects) != set(expected) or len(expected) != len(pages)
            or any(not isinstance(raw, bytes) or not 0 < len(raw) <= expected[digest] or digest_bytes(raw) != digest
                   for digest, raw in objects.items())):
        raise ValueError("CAPTURE_OBJECT_CLOSURE_INVALID")


def stage(root: Path, acquired: Capture) -> dict:
    manifest = acquired.manifest
    # Checked before any write: the quarantine store is immutable and digest-addressed.
    _check_object_closure(manifest, acquired.objects)
    manifest_bytes = canonical_bytes(manifest)
    if len(manifest_bytes) > MANIFEST_BYTES:
        raise ValueError("CAPTURE_MANIFEST_BYTE_LIMIT")
    run = str(manifest.get("capture_id", "")).removeprefix("sha256:")
    if not re.fullmatch(r"[0-9a-f]{64}", run):
        raise ValueError("INVALID_CAPTURE_ID")
    # Quarantine runs are digest-addressed: the manifest must hash to its id before anything is written.
    if digest_bytes(canonical_bytes({k: v for k, v in manifest.items() if k != "capture_id"})) != manifest["capture_id"]:
        raise ValueError("CAPTURE_DIGEST_MISMATCH")
    with store_lock(root):
        for digest, raw in acquired.objects.items():
            object_path(root, digest)
            immutable(object_path(root, digest), raw)
        immutable(root / "data/quarantine" / LANE / "runs" / run / "manifest.json", manifest_bytes)
        try:
            candidate = normalize_capture(manifest, acquired.objects)
            validation = validate_candidate(candidate)
        except (ValueError, KeyError, TypeError):
            outcome, reason, candidate_id, counts = "QUARANTINED", "CAPTURE_OR_NORMALIZATION_INVALID", None, {}
        else:
            short = candidate["candidate_id"].split(":")[1]
            immutable(root / "data/work/hazards" / LANE / short / "candidate.json", canonical_bytes(candidate))
            immutable(root / "data/receipts/validation/hazards" / short / "validation.json", canonical_bytes(validation))
            outcome, reason, candidate_id = "CANDIDATE_READY", "REVIEW_REQUIRED", candidate["candidate_id"]
            counts = {"data_year": candidate["data_year"], "source_file": candidate["source_file"],
                      "observations": len(candidate["observations"]), "withheld": validation["withheld"],
                      "freshness": candidate["freshness_at_capture"], "coverage": candidate["coverage"]}
        receipt = {"profile": "kfm.storm-events-pilot-run/v1", "run_id": run, "capture_id": manifest["capture_id"],
                   "candidate_id": candidate_id, "outcome": outcome, "reason_code": reason, "counts": counts,
                   "source_admitted": False, "promoted": False, "released": False, "published": False}
        name = candidate_id.split(":")[1] if candidate_id else "quarantined"
        immutable(root / "data/receipts/ingest" / LANE / run / (name + ".json"), canonical_bytes(receipt))
    return receipt


def load_capture(root: Path, capture_id: str) -> Capture:
    """Read a staged capture back from the quarantine store; writes nothing."""
    if not isinstance(capture_id, str) or not DIGEST.fullmatch(capture_id):
        raise ValueError("INVALID_CAPTURE_ID")
    path = root / "data/quarantine" / LANE / "runs" / capture_id.split(":")[1] / "manifest.json"
    manifest = decode_object(read_regular(path, MANIFEST_BYTES), limit=MANIFEST_BYTES)
    if manifest.get("capture_id") != capture_id:
        raise ValueError("CAPTURE_PATH_ID_MISMATCH")
    pages = manifest.get("pages")
    # Exactly the listing and one allowlisted details file, so stored paths are never read from free keys.
    if (not isinstance(pages, list) or len(pages) != 2 or not all(isinstance(p, dict) for p in pages)
            or pages[0].get("key") != LISTING_KEY or pages[1].get("key") == LISTING_KEY):
        raise ValueError("CAPTURE_PAGE_CHAIN_MISMATCH")
    try:
        object_url(pages[1].get("key"))
    except ValueError:
        raise ValueError("CAPTURE_PAGE_CHAIN_MISMATCH") from None
    objects = {page["sha256"]: read_regular(object_path(root, page["sha256"]), object_limit(page["key"])) for page in pages}
    _check_object_closure(manifest, objects)
    return Capture(manifest, objects)


def replay(root: Path, capture_id: str) -> dict:
    return stage(root, load_capture(root, capture_id))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    sub = parser.add_subparsers(dest="operation", required=True)
    acquire = sub.add_parser("capture")
    acquire.add_argument("--year", required=True, type=int, help="data year; the newest details file NCEI lists for it is captured")
    repeat = sub.add_parser("replay")
    repeat.add_argument("--capture-id", required=True)
    args = parser.parse_args(argv)
    try:
        root = external_root(args.root)
        init_store(root)
        result = stage(root, capture(args.year)) if args.operation == "capture" else replay(root, args.capture_id)
    except (OSError, ValueError, KeyError, TypeError):
        print('{"outcome":"ERROR","reason_code":"PILOT_OPERATION_FAILED"}')
        return 1
    print(canonical_bytes(result).decode())
    return 0 if result["outcome"] == "CANDIDATE_READY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
