#!/usr/bin/env python3
"""Capture/replay public Kansas climate normals to private QUARANTINE/WORK.

This command never admits the source, approves evidence, activates a release,
serves clients, or writes to the standalone Site. A complete candidate still
requires independent source, rights, sensitivity, evidence and release review.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from connectors.noaa.src.noaa.climate_normals_capture import Capture, canonical_bytes, capture  # noqa: E402
from connectors.noaa.src.noaa.climate_normals import NormalsError  # noqa: E402
from pipelines.domains.atmosphere.noaa_normals import normalize_capture, project_station_points  # noqa: E402
from tools.local_data.file_io import read_regular, write_new  # noqa: E402
from tools.local_data.manage import external_root, init_store, store_lock  # noqa: E402

DIGEST = re.compile(r"sha256:[0-9a-f]{64}\Z")
MAX_MANIFEST_BYTES = 512 * 1024
MAX_OBJECT_BYTES = 2 * 1024 * 1024
MAX_CANDIDATE_BYTES = 2 * 1024 * 1024


def _object_path(root: Path, digest: str) -> Path:
    if not isinstance(digest, str) or not DIGEST.fullmatch(digest):
        raise ValueError("OBJECT_DIGEST")
    return root / "data/quarantine/noaa-climate-normals/objects/sha256" / digest[7:] / "payload"


def _immutable(path: Path, raw: bytes) -> None:
    try:
        write_new(path, raw)
    except FileExistsError:
        if read_regular(path, max(len(raw), 1)) != raw:
            raise ValueError("IMMUTABLE_CONFLICT") from None


def stage(root: Path, acquired: Capture) -> dict:
    from hashlib import sha256
    manifest = acquired.manifest
    unsigned = {key: value for key, value in manifest.items() if key != "capture_id"}
    if manifest.get("capture_id") != "sha256:" + sha256(canonical_bytes(unsigned)).hexdigest():
        raise ValueError("CAPTURE_ID")
    run = manifest["capture_id"][7:]
    with store_lock(root):
        for digest, raw in acquired.objects.items():
            if len(raw) > MAX_OBJECT_BYTES or "sha256:" + sha256(raw).hexdigest() != digest:
                raise ValueError("OBJECT_INTEGRITY")
            _immutable(_object_path(root, digest), raw)
        _immutable(root / "data/quarantine/noaa-climate-normals/runs" / run / "manifest.json",
                   canonical_bytes(manifest))
        candidate_id = None
        try:
            candidate = normalize_capture(manifest, acquired.objects)
            candidate_id = candidate["candidate_id"]
            _immutable(root / "data/work/atmosphere/noaa-climate-normals" / candidate_id[7:] / "candidate.json",
                       canonical_bytes(candidate))
            outcome, reason = "CANDIDATE_READY", "REVIEW_REQUIRED"
        except (ValueError, KeyError, TypeError, NormalsError):
            outcome, reason = "QUARANTINED", "CAPTURE_OR_NORMALIZATION_INVALID"
        receipt = {"profile": "kfm.noaa-monthly-normals-run/v1", "capture_id": manifest["capture_id"],
                   "candidate_id": candidate_id, "expected_stations": manifest["expected_stations"],
                   "captured_stations": manifest["captured_stations"], "outcome": outcome,
                   "reason_code": reason, "source_admitted": False, "reviewed": False,
                   "released": False, "published": False}
        _immutable(root / "data/receipts/ingest/noaa-climate-normals" / run / "receipt.json",
                   canonical_bytes(receipt))
    return receipt


def replay(root: Path, capture_id: str) -> dict:
    import json
    if not DIGEST.fullmatch(capture_id):
        raise ValueError("CAPTURE_ID")
    manifest = json.loads(read_regular(root / "data/quarantine/noaa-climate-normals/runs"
                                       / capture_id[7:] / "manifest.json", MAX_MANIFEST_BYTES))
    refs = [manifest["inventory"], *manifest["station_objects"]]
    objects = {ref["sha256"]: read_regular(_object_path(root, ref["sha256"]), MAX_OBJECT_BYTES)
               for ref in refs}
    return stage(root, Capture(manifest, objects))


def map_preview(root: Path, candidate_id: str, month: int, variable: str) -> dict:
    """Materialize an unreleased station-point review artifact in WORK."""
    import json
    from hashlib import sha256
    if not DIGEST.fullmatch(candidate_id):
        raise ValueError("CANDIDATE_ID")
    raw = read_regular(root / "data/work/atmosphere/noaa-climate-normals" /
                       candidate_id[7:] / "candidate.json", MAX_CANDIDATE_BYTES)
    candidate = json.loads(raw)
    unsigned = {key: value for key, value in candidate.items() if key != "candidate_id"}
    if (candidate.get("candidate_id") != candidate_id or raw != canonical_bytes(candidate)
            or "sha256:" + sha256(canonical_bytes(unsigned)).hexdigest() != candidate_id):
        raise ValueError("CANDIDATE_INTEGRITY")
    preview = project_station_points(candidate, month=month, variable=variable)
    projection = canonical_bytes(preview)
    projection_id = "sha256:" + sha256(projection).hexdigest()
    with store_lock(root):
        _immutable(root / "data/work/atmosphere/noaa-climate-normals" /
                   candidate_id[7:] / "map-previews" / projection_id[7:] / "features.geojson", projection)
    return {"profile": preview["profile"], "candidate_id": candidate_id,
            "projection_id": projection_id, "month": month, "variable": variable,
            "feature_count": len(preview["features"]), "outcome": "REVIEW_PREVIEW_READY",
            "released": False, "published": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    sub = parser.add_subparsers(dest="operation", required=True)
    sub.add_parser("capture")
    replay_cmd = sub.add_parser("replay")
    replay_cmd.add_argument("--capture-id", required=True)
    preview_cmd = sub.add_parser("map-preview")
    preview_cmd.add_argument("--candidate-id", required=True)
    preview_cmd.add_argument("--month", type=int, required=True)
    preview_cmd.add_argument("--variable", choices=("temperature_f", "precipitation_in"), required=True)
    args = parser.parse_args(argv)
    try:
        root = external_root(args.root)
        init_store(root)
        if args.operation == "capture":
            receipt = stage(root, capture())
        elif args.operation == "replay":
            receipt = replay(root, args.capture_id)
        else:
            receipt = map_preview(root, args.candidate_id, args.month, args.variable)
    except (OSError, ValueError, KeyError, TypeError):
        print('{"outcome":"ERROR","reason_code":"NORMALS_OPERATION_FAILED"}')
        return 1
    print(canonical_bytes(receipt).decode().strip())
    return 0 if receipt["outcome"] in {"CANDIDATE_READY", "REVIEW_PREVIEW_READY"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
