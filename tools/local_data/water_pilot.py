#!/usr/bin/env python3
"""Capture or replay the water pilot into the existing private lifecycle store.

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
from connectors.usgs.water_data.pilot_capture import Capture, capture, MAX_PAGE_BYTES
from pipelines.domains.hydrology.normalize import normalize_capture
from pipelines.domains.hydrology.validate import validate_candidate
from tools.generators.telemetry.water_operational_receipt import operational_receipt, source_health
from connectors.usgs.water_data.pilot_capture import STATIONS
from tools.local_data.file_io import read_regular, write_new
from tools.local_data.manage import external_root, init_store, store_lock

DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")


def immutable(path: Path, raw: bytes) -> None:
    try:
        write_new(path, raw)
    except FileExistsError:
        if read_regular(path, max(len(raw), 1)) != raw:
            raise ValueError("IMMUTABLE_OBJECT_CONFLICT")


def object_path(root: Path, digest: str) -> Path:
    if not isinstance(digest, str) or not DIGEST.fullmatch(digest):
        raise ValueError("INVALID_OBJECT_DIGEST")
    return root / "data/quarantine/usgs-nwis/objects/sha256" / digest.split(":")[1] / "payload"


def stage(root: Path, acquired: Capture) -> dict:
    manifest = acquired.manifest
    expected = digest_bytes(canonical_bytes({k: v for k, v in manifest.items() if k != "capture_id"}))
    if expected != manifest.get("capture_id"):
        raise ValueError("CAPTURE_DIGEST_MISMATCH")
    run = expected.split(":")[1]
    with store_lock(root):
        for digest, raw in acquired.objects.items():
            if len(raw) > MAX_PAGE_BYTES or digest_bytes(raw) != digest:
                raise ValueError("PAGE_DIGEST_MISMATCH")
            immutable(object_path(root, digest), raw)
        manifest_path = root / "data/quarantine/usgs-nwis/runs" / run / "manifest.json"
        immutable(manifest_path, canonical_bytes(manifest))
        candidate = validation = None
        try:
            candidate = normalize_capture(manifest, acquired.objects)
            validation = validate_candidate(candidate)
        except (ValueError, KeyError, TypeError):
            outcome, reason, candidate_id, counts = "QUARANTINED", "CAPTURE_OR_NORMALIZATION_INVALID", None, {}
        else:
            candidate_path = root / "data/work/hydrology/usgs-nwis" / candidate["candidate_id"].split(":")[1] / "candidate.json"
            immutable(candidate_path, canonical_bytes(candidate))
            immutable(root / "data/receipts/validation/hydrology" / candidate["candidate_id"].split(":")[1] / "validation.json",
                      canonical_bytes(validation))
            outcome, reason = "CANDIDATE_READY", "REVIEW_REQUIRED"
            candidate_id = candidate["candidate_id"]
            counts = {"stations": len(candidate["stations"]), "observations": len(candidate["observations"])}
        receipt = {"profile": "kfm.water-pilot-run/v1", "run_id": run,
                   "capture_id": expected, "candidate_id": candidate_id,
                   "outcome": outcome, "reason_code": reason, "counts": counts,
                   "source_admitted": False, "promoted": False, "released": False, "published": False}
        operational = operational_receipt(manifest, candidate if candidate_id else None, validation if candidate_id else None)
        immutable(root / "data/receipts/ingest/usgs-nwis" / run / "operational" / (operational["spec_hash"].split(":")[1] + ".json"), canonical_bytes(operational))
        for station_id in STATIONS:
            health = source_health(manifest, candidate if candidate_id else None, station_id=station_id)
            health_id = digest_bytes(canonical_bytes(health)).split(":")[1]
            immutable(root / "data/receipts/ingest/usgs-nwis" / run / "health" / (health_id + ".json"), canonical_bytes(health))
        receipt_name = candidate_id.split(":")[1] if candidate_id else "quarantined"
        immutable(root / "data/receipts/ingest/usgs-nwis" / run / (receipt_name + ".json"), canonical_bytes(receipt))
    return receipt


def replay(root: Path, capture_id: str) -> dict:
    if not DIGEST.fullmatch(capture_id):
        raise ValueError("INVALID_CAPTURE_ID")
    path = root / "data/quarantine/usgs-nwis/runs" / capture_id.split(":")[1] / "manifest.json"
    manifest = decode_object(read_regular(path, 256 * 1024), limit=256 * 1024)
    objects = {page["sha256"]: read_regular(object_path(root, page["sha256"]), MAX_PAGE_BYTES)
               for page in manifest["pages"]}
    return stage(root, Capture(manifest, objects))


def main(argv=None, *, allowed_operations=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    sub = parser.add_subparsers(dest="operation", required=True)
    acquire = sub.add_parser("capture")
    acquire.add_argument("--start", required=True)
    acquire.add_argument("--end", required=True)
    repeat = sub.add_parser("replay")
    repeat.add_argument("--capture-id", required=True)
    args = parser.parse_args(argv)
    if allowed_operations is not None and args.operation not in allowed_operations:
        parser.error("operation is not allowed by this worker")
    try:
        root = external_root(args.root)
        init_store(root)
        result = stage(root, capture(args.start, args.end)) if args.operation == "capture" else replay(root, args.capture_id)
    except (OSError, ValueError, KeyError, TypeError):
        print('{"outcome":"ERROR","reason_code":"PILOT_OPERATION_FAILED"}')
        return 1
    print(canonical_bytes(result).decode())
    return 0 if result["outcome"] == "CANDIDATE_READY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
