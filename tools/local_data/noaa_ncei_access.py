#!/usr/bin/env python3
"""Plan, capture and replay NCEI Access JSON in a private quarantine store.

No API key, admission, promotion, active pointer, or publication. Plan/products
are offline; capture makes exactly one bounded provider request.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
import uuid

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "packages/connectors-core/src"))

from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes
from connectors.noaa.src.noaa import ncei_access as api
from tools.local_data.file_io import read_regular, write_new
from tools.local_data.manage import external_root, init_store, store_lock

LANE = "noaa-ncei-access"
MANIFEST_BYTES = 512 * 1024
DIGEST = re.compile(r"sha256:[0-9a-f]{64}\Z")


def immutable(path: Path, raw: bytes) -> None:
    try:
        write_new(path, raw)
    except FileExistsError:
        if read_regular(path, max(len(raw), 1)) != raw:
            raise ValueError("IMMUTABLE_OBJECT_CONFLICT")


def _digest(value):
    if not isinstance(value, str) or DIGEST.fullmatch(value) is None:
        raise ValueError("CAPTURE_ID_INVALID")
    return value.split(":")[1]


def object_path(root: Path, digest: str) -> Path:
    return root / "data/quarantine" / LANE / "objects/sha256" / _digest(digest) / "payload.json"


def stage(root: Path, acquired: api.Capture) -> dict:
    summary = api.verify_capture(acquired)
    manifest = acquired.manifest
    raw_manifest = canonical_bytes(manifest)
    if len(raw_manifest) > MANIFEST_BYTES:
        raise ValueError("CAPTURE_MANIFEST_BYTE_LIMIT")
    short = _digest(manifest["capture_id"])
    receipt = {"profile": "kfm.ncei-access-ingest/v1", "capture_id": manifest["capture_id"],
               "source_id": manifest["source_id"], "dataset": manifest["parameters"]["dataset"],
               "source_role": manifest["source_role"], "baseline_period": manifest["baseline_period"],
               "bytes": len(acquired.raw), "row_count": summary["row_count"],
               "outcome": "QUARANTINED", "reason_code": "REVIEW_REQUIRED",
               "review_state": "pending", "source_admitted": False, "promoted": False,
               "released": False, "published": False}
    with store_lock(root):
        payload = object_path(root, manifest["response"]["sha256"])
        immutable(payload, acquired.raw)
        if read_regular(payload, manifest["max_bytes"]) != acquired.raw:
            raise ValueError("STORED_PAYLOAD_READBACK_MISMATCH")
        path = root / "data/quarantine" / LANE / "runs" / short / "manifest.json"
        immutable(path, raw_manifest)
        if read_regular(path, MANIFEST_BYTES) != raw_manifest:
            raise ValueError("STORED_MANIFEST_READBACK_MISMATCH")
        immutable(root / "data/receipts/ingest" / LANE / short / "receipt.json", canonical_bytes(receipt))
    return receipt


def load_capture(root: Path, capture_id: str) -> api.Capture:
    short = _digest(capture_id)
    path = root / "data/quarantine" / LANE / "runs" / short / "manifest.json"
    manifest = decode_object(read_regular(path, MANIFEST_BYTES), limit=MANIFEST_BYTES)
    if manifest.get("capture_id") != capture_id:
        raise ValueError("CAPTURE_PATH_ID_MISMATCH")
    # Never let a tampered manifest choose an unbounded read or an arbitrary path.
    limit = manifest.get("max_bytes")
    if type(limit) is not int or not 1 <= limit <= api.MAX_BYTES:
        raise ValueError("CAPTURE_BYTE_LIMIT_INVALID")
    raw = read_regular(object_path(root, manifest["response"]["sha256"]), limit)
    acquired = api.Capture(manifest, raw)
    api.verify_capture(acquired)
    return acquired


def acquire(root: Path, query: api.Query, *, fetcher=api.fetch) -> dict:
    plan = query.plan()
    raw = None
    started_at = api.utc_now()
    try:
        raw, meta = fetcher(query)
        acquired = api.capture(query, fetcher=lambda _query: (raw, meta))
    except (OSError, ValueError) as exc:
        # A structurally invalid, bounded response remains inspectable in
        # quarantine. Failed requests have no payload and never become captures.
        attempt = uuid.uuid4().hex
        receipt = {"profile": "kfm.ncei-access-failed-attempt/v1", "attempt_id": attempt,
                   "plan": plan, "outcome": "ERROR", "reason_code": "CAPTURE_OR_INSPECTION_FAILED",
                   "started_at": started_at, "finished_at": api.utc_now(),
                   "provider_reason": str(exc) if str(exc) in {"REQUEST_REJECTED", "PRODUCT_NOT_FOUND",
                       "PROVIDER_RATE_LIMITED", "PROVIDER_HTTP_ERROR", "PROVIDER_UNAVAILABLE", "NETWORK_DISABLED"} else None,
                   "review_state": "pending", "source_admitted": False, "promoted": False,
                   "released": False, "published": False, "response_sha256": None}
        with store_lock(root):
            if isinstance(raw, bytes) and 0 < len(raw) <= query.max_bytes:
                receipt["response_sha256"] = digest_bytes(raw)
                immutable(object_path(root, receipt["response_sha256"]), raw)
            immutable(root / "data/receipts/ingest" / LANE / "failed" / attempt / "receipt.json", canonical_bytes(receipt))
        return receipt
    return stage(root, acquired)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="operation", required=True)
    sub.add_parser("products", help="list configured product profiles; no network")
    for operation in ("plan", "capture"):
        command = sub.add_parser(operation)
        command.add_argument("--dataset", required=True, choices=tuple(api.PRODUCTS))
        command.add_argument("--stations", default=",".join(api.PILOT_STATIONS))
        command.add_argument("--start")
        command.add_argument("--end")
        command.add_argument("--elements", help="comma-separated product-specific elements; defaults to profile")
        command.add_argument("--units", choices=("metric", "standard"), default="metric")
        command.add_argument("--max-bytes", type=int, required=True, help="stop limit, not an expected size; maximum 16 MiB")
        if operation == "capture":
            command.add_argument("--root", required=True, help="absolute private lifecycle-store path outside the repository")
    repeat = sub.add_parser("replay", help="verify stored bytes and receipt; no network")
    repeat.add_argument("--root", required=True)
    repeat.add_argument("--capture-id", required=True)
    args = parser.parse_args(argv)
    try:
        if args.operation == "products":
            result = {"endpoint": api.ENDPOINT, "documentation": api.DOCUMENTATION,
                      "api_key_required": False, "network": False,
                      "products": {key: {"source_role": p.role, "period_kind": p.period,
                                   "baseline_period": p.baseline, "elements": p.elements}
                                   for key, p in api.PRODUCTS.items()}}
        elif args.operation == "replay":
            root = external_root(args.root)
            result = stage(root, load_capture(root, args.capture_id))
        else:
            query = api.Query(args.dataset, tuple(args.stations.split(",")), args.start, args.end,
                              tuple(args.elements.split(",")) if args.elements else None, args.units, args.max_bytes)
            result = query.plan()
            if args.operation == "capture":
                root = external_root(args.root)
                init_store(root)
                result = acquire(root, query)
    except (OSError, ValueError, KeyError, TypeError):
        print('{"outcome":"ERROR","reason_code":"NCEI_OPERATION_FAILED"}')
        return 1
    print(canonical_bytes(result).decode())
    return 1 if result.get("outcome") == "ERROR" else 0


if __name__ == "__main__":
    raise SystemExit(main())
