#!/usr/bin/env python3
"""Capture or replay the USCRN daily soil pilot into the existing private lifecycle store.

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
from connectors.noaa.src.noaa.uscrn_daily_capture import Capture, capture, capture_keys, object_limit
from pipelines.domains.soil.uscrn_daily_normalize import normalize_capture
from pipelines.domains.soil.uscrn_daily_validate import validate_candidate
from tools.local_data.file_io import read_regular
from tools.local_data.manage import external_root, init_store, store_lock
from tools.local_data.water_pilot import immutable

DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
LANE = "noaa-uscrn-daily"
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
            immutable(root / "data/work/soil" / LANE / short / "candidate.json", canonical_bytes(candidate))
            immutable(root / "data/receipts/validation/soil" / short / "validation.json", canonical_bytes(validation))
            outcome, reason, candidate_id = "CANDIDATE_READY", "REVIEW_REQUIRED", candidate["candidate_id"]
            counts = {"stations": len(candidate["stations"]), "observations": len(candidate["observations"]),
                      "withheld": validation["withheld"], "coverage": candidate["coverage"]}
        receipt = {"profile": "kfm.uscrn-daily-pilot-run/v1", "run_id": run, "capture_id": manifest["capture_id"],
                   "candidate_id": candidate_id, "outcome": outcome, "reason_code": reason, "counts": counts,
                   "source_admitted": False, "promoted": False, "released": False, "published": False}
        name = candidate_id.split(":")[1] if candidate_id else "quarantined"
        immutable(root / "data/receipts/ingest" / LANE / run / (name + ".json"), canonical_bytes(receipt))
    return receipt


def replay(root: Path, capture_id: str) -> dict:
    if not isinstance(capture_id, str) or not DIGEST.fullmatch(capture_id):
        raise ValueError("INVALID_CAPTURE_ID")
    path = root / "data/quarantine" / LANE / "runs" / capture_id.split(":")[1] / "manifest.json"
    manifest = decode_object(read_regular(path, MANIFEST_BYTES), limit=MANIFEST_BYTES)
    if manifest.get("capture_id") != capture_id:
        raise ValueError("CAPTURE_PATH_ID_MISMATCH")
    pages = manifest.get("pages")
    try:
        keys = capture_keys(manifest.get("end"))
    except ValueError:
        raise ValueError("CAPTURE_PAGE_CHAIN_MISMATCH") from None
    if not isinstance(pages, list) or [p.get("key") for p in pages if isinstance(p, dict)] != keys:
        raise ValueError("CAPTURE_PAGE_CHAIN_MISMATCH")
    objects = {page["sha256"]: read_regular(object_path(root, page["sha256"]), object_limit(page["key"])) for page in pages}
    return stage(root, Capture(manifest, objects))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    sub = parser.add_subparsers(dest="operation", required=True)
    acquire = sub.add_parser("capture")
    acquire.add_argument("--end", required=True, help="last observation day, YYYY-MM-DD (the window is the 30 days ending here)")
    repeat = sub.add_parser("replay")
    repeat.add_argument("--capture-id", required=True)
    args = parser.parse_args(argv)
    try:
        root = external_root(args.root)
        init_store(root)
        result = stage(root, capture(args.end)) if args.operation == "capture" else replay(root, args.capture_id)
    except (OSError, ValueError, KeyError, TypeError):
        print('{"outcome":"ERROR","reason_code":"PILOT_OPERATION_FAILED"}')
        return 1
    print(canonical_bytes(result).decode())
    return 0 if result["outcome"] == "CANDIDATE_READY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
