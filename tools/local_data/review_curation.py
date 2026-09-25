#!/usr/bin/env python3
"""Inspect one explicit, device-local KFM curation candidate package.

This command reads only. It does not admit, install, serve, release, or publish
source material, and it does not scan or copy the external raw archive.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from pathlib import Path

SCHEMA = "kfm-local-layer-candidate-reconciliation/v1"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_CHECKSUM_LINES = 1000
MAX_CHECKSUM_BYTES = 256 * 1024
SHA_LINE = re.compile(r"^([0-9a-f]{64})  ([^\r\n]+)$")
BUNDLE_NAME = re.compile(r"^kfm-store-reconciliation-[0-9]{8}(?:T[0-9]{6}Z)?$")
COLLECTIONS = {
    "KFM Historic County Township Maps", "KFM Past Published County Maps",
    "Kansas Road Maps", "KFM County Roadways", "KFM Urban Roadways",
    "Kansas bridges", "TIGER data", "kansas-wind-all-airports-1932-2026",
    "ftp.ncdc.noaa.gov", "PRISM data",
}
LAYER_IDS = {
    "kdot_county_future_functional_class_candidates",
    "kdot_urban_future_functional_class_candidates",
    "kdot_bridge_label_search_anchors",
    "historic_map_sheet_geometry_review",
    "prism_completed_grid_review",
}


class Held(Exception):
    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


def _read_json(path: Path) -> dict:
    try:
        with path.open("rb") as handle:
            payload = handle.read(MAX_JSON_BYTES + 1)
    except OSError as exc:
        raise Held("MISSING_OR_UNREADABLE_METADATA") from exc
    if len(payload) > MAX_JSON_BYTES:
        raise Held("METADATA_TOO_LARGE")
    try:
        value = json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Held("INVALID_METADATA_JSON") from exc
    if not isinstance(value, dict):
        raise Held("INVALID_METADATA_SHAPE")
    return value


def _inside(base: Path, relative: str, *, file: bool = True) -> Path:
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise Held("UNSAFE_ARTIFACT_PATH")
    try:
        target = (base / relative).resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        raise Held("MISSING_ARTIFACT") from exc
    if not target.is_relative_to(base):
        raise Held("UNSAFE_ARTIFACT_PATH")
    if file and not target.is_file():
        raise Held("MISSING_ARTIFACT")
    return target


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for block in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(block)
    except OSError as exc:
        raise Held("UNREADABLE_ARTIFACT") from exc
    return digest.hexdigest()


def _checksum_index(bundle: Path, processed: Path) -> dict[str, str]:
    try:
        relative = (bundle / "checksums.sha256").relative_to(processed).as_posix()
    except ValueError as exc:
        raise Held("UNSAFE_CHECKSUM_PATH") from exc
    checksums = _inside(processed, relative)
    if checksums.parent != bundle:
        raise Held("UNSAFE_CHECKSUM_PATH")
    try:
        if checksums.stat().st_size > MAX_CHECKSUM_BYTES:
            raise Held("INVALID_CHECKSUM_MANIFEST")
        lines = checksums.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as exc:
        raise Held("INVALID_CHECKSUM_MANIFEST") from exc
    if not 1 <= len(lines) <= MAX_CHECKSUM_LINES:
        raise Held("INVALID_CHECKSUM_MANIFEST")
    expected: dict[str, str] = {}
    for line in lines:
        match = SHA_LINE.fullmatch(line)
        if not match or match.group(2) in expected:
            raise Held("INVALID_CHECKSUM_MANIFEST")
        expected[match.group(2)] = match.group(1)
    return expected


def _verify_checksums(bundle: Path, processed: Path) -> dict[str, str]:
    expected = _checksum_index(bundle, processed)
    for relative, digest in expected.items():
        target = _inside(bundle, relative)
        if _sha256(target) != digest:
            raise Held("CHECKSUM_MISMATCH")
    return expected


def inspect(root: Path, bundle_name: str) -> dict:
    if not BUNDLE_NAME.fullmatch(bundle_name):
        raise Held("INVALID_BUNDLE_NAME")
    try:
        root = root.resolve(strict=True)
        processed = (root / "data/processed").resolve(strict=True)
        bundle = (processed / bundle_name).resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        raise Held("MISSING_LOCAL_STORE") from exc
    if not bundle.is_dir() or bundle.parent != processed:
        raise Held("INVALID_BUNDLE_LOCATION")
    if root.is_relative_to(Path(__file__).resolve().parents[2]):
        raise Held("STORE_INSIDE_REPOSITORY")

    checksums = _verify_checksums(bundle, processed)
    required = {"validation.json", "inventory/summary.json", "layers/layer_manifest.json",
                "cleanup_plan.json", "maps/georeference_review.json"}
    if not required.issubset(checksums):
        raise Held("INCOMPLETE_BUNDLE_CHECKSUMS")
    validation = _read_json(bundle / "validation.json")
    inventory = _read_json(bundle / "inventory/summary.json")
    manifest = _read_json(bundle / "layers/layer_manifest.json")
    cleanup = _read_json(bundle / "cleanup_plan.json")
    georef = _read_json(bundle / "maps/georeference_review.json")
    source_validation = validation.get("source_inventory")
    if (validation.get("passed") is not True or
            not isinstance(source_validation, dict) or
            source_validation.get("passed") is not True or
            source_validation.get("all_collections_accounted") is not True or
            source_validation.get("all_nonmutable_files_hashed") is not True or
            source_validation.get("all_prior_maps_present") is not True):
        raise Held("BUNDLE_VALIDATION_FAILED")
    if manifest.get("schema") != SCHEMA or not isinstance(manifest.get("layers"), list):
        raise Held("UNSUPPORTED_LAYER_MANIFEST")
    if (not isinstance(inventory.get("files"), int) or
            inventory["files"] != source_validation.get("source_files") or
            not isinstance(inventory.get("collections"), dict) or
            set(inventory["collections"]) != COLLECTIONS):
        raise Held("INVENTORY_COUNT_MISMATCH")
    if cleanup.get("source_deletions_in_this_run") != 0 or cleanup.get("approved_for_deletion") != []:
        raise Held("UNREVIEWED_SOURCE_DELETION")

    layers = []
    identities = set()
    for layer in manifest["layers"]:
        if not isinstance(layer, dict) or not isinstance(layer.get("id"), str):
            raise Held("INVALID_LAYER_ENTRY")
        identity = layer["id"]
        status = layer.get("status", "")
        if identity in identities or not (isinstance(status, str) and
                                          (status.startswith("local_unadmitted_") or status == "review_queue")):
            raise Held("INVALID_LAYER_STATUS")
        if not all(isinstance(layer.get(key), str) and layer[key]
                   for key in ("domain", "geometry", "time_mode", "claim_limit")):
            raise Held("INVALID_LAYER_ENTRY")
        identities.add(identity)
        artifact = layer.get("artifact")
        if not isinstance(artifact, str) or not artifact or Path(artifact).is_absolute():
            raise Held("UNSAFE_ARTIFACT_PATH")
        target = _inside(bundle, artifact) if not artifact.startswith("../") else _inside(processed, f"{bundle_name}/{artifact}")
        if target.is_relative_to(bundle):
            relative = target.relative_to(bundle).as_posix()
            if relative not in checksums:
                raise Held("UNHASHED_LAYER_ARTIFACT")
        else:
            sibling = target.relative_to(processed).parts[0]
            sibling_bundle = processed / sibling
            sibling_checksums = _checksum_index(sibling_bundle, processed)
            relative = target.relative_to(sibling_bundle).as_posix()
            if relative not in sibling_checksums or _sha256(target) != sibling_checksums[relative]:
                raise Held("CHECKSUM_MISMATCH")
        layers.append({"id": identity, "domain": layer.get("domain"),
                       "status": status, "geometry": layer.get("geometry"),
                       "time_mode": layer.get("time_mode"),
                       "feature_count": layer.get("feature_count"),
                       "artifact": artifact})
    if identities != LAYER_IDS:
        raise Held("UNEXPECTED_LAYER_SET")
    return {"status": "LOCAL_CANDIDATE_REVIEW", "bundle": bundle_name,
            "snapshot_completed_utc": inventory.get("completed_utc"),
            "source_files_at_snapshot": inventory["files"],
            "map_sheets": georef.get("map_sheets"),
            "county_clipped_fragments": validation.get("county_clipped_fragments"),
            "urban_map_strokes": validation.get("urban_vector_lines"),
            "verified_bundle_files": len(checksums),
            "layers": layers,
            "limits": ["No source admission, release, deployment, or publication",
                       "Package checksums prove local byte integrity, not provider authenticity",
                       "PRISM and other live source folders can change after the snapshot"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=os.environ.get("KFM_DATA_ROOT"),
                        help="External KFM_DATA_ROOT (or set KFM_DATA_ROOT)")
    parser.add_argument("--bundle", required=True, help="Explicit processed review bundle name")
    args = parser.parse_args()
    if not args.root:
        result = {"status": "HELD", "reason": "MISSING_LOCAL_STORE"}
        print(json.dumps(result, sort_keys=True))
        return 1
    try:
        result = inspect(Path(args.root), args.bundle)
    except Held as exc:
        result = {"status": "HELD", "reason": exc.code}
        print(json.dumps(result, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
