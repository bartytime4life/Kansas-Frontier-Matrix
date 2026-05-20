#!/usr/bin/env python3
"""Validate minimum KFM PMTiles header/metadata publication requirements.

This is a conservative scaffold. It validates PMTiles v3 magic/version and attempts
metadata JSON extraction only when directory offsets are readable. Projects may
replace parsing with an approved PMTiles library while preserving fail-closed exits.
"""
from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from pathlib import Path

SHA256_RE = re.compile(r"^sha256:[a-fA-F0-9]{64}$")


def fail(msg: str) -> int:
    print(f"DENY: {msg}", file=sys.stderr)
    return 1


def read_header(path: Path) -> bytes:
    data = path.read_bytes()[:127]
    if len(data) < 127:
        raise ValueError("file is too small to contain PMTiles v3 header")
    return data


def parse_minimal_header(header: bytes) -> dict:
    if header[:7] != b"PMTiles":
        raise ValueError("missing PMTiles magic")
    version = header[7]
    if version != 3:
        raise ValueError(f"unsupported PMTiles version: {version}")

    # PMTiles v3 header uses little-endian uint64 offset/length fields after magic/version.
    fields = struct.unpack("<14Q", header[8:8 + (14 * 8)])
    names = [
        "root_offset", "root_length", "json_metadata_offset", "json_metadata_length",
        "leaf_directory_offset", "leaf_directory_length", "tile_data_offset", "tile_data_length",
        "addressed_tiles_count", "tile_entries_count", "tile_contents_count",
        "clustered", "internal_compression", "tile_compression",
    ]
    return dict(zip(names, fields)) | {"version": version}


def load_metadata(path: Path, header_info: dict) -> dict:
    offset = int(header_info["json_metadata_offset"])
    length = int(header_info["json_metadata_length"])
    if offset <= 0 or length <= 0:
        raise ValueError("metadata offset/length missing")
    with path.open("rb") as f:
        f.seek(offset)
        raw = f.read(length)
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f"metadata is not valid UTF-8 JSON: {exc}") from exc


def extract_spec_hash(metadata: dict) -> str | None:
    candidates = [
        metadata.get("spec_hash"),
        metadata.get("kfm", {}).get("spec_hash") if isinstance(metadata.get("kfm"), dict) else None,
    ]
    for value in candidates:
        if isinstance(value, str):
            return value
    return None


def validate(path: Path) -> int:
    try:
        header = read_header(path)
        info = parse_minimal_header(header)
        metadata = load_metadata(path, info)
        spec_hash = extract_spec_hash(metadata)
    except Exception as exc:  # noqa: BLE001
        return fail(f"{path}: {exc}")

    if not spec_hash:
        return fail(f"{path}: missing metadata spec_hash")
    if not SHA256_RE.match(spec_hash):
        return fail(f"{path}: malformed spec_hash {spec_hash!r}")
    if info["tile_data_length"] <= 0:
        return fail(f"{path}: tile_data_length must be positive")

    print(f"ALLOW: {path}: PMTiles header and spec_hash present")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pmtiles", nargs="+", type=Path)
    args = parser.parse_args()
    status = 0
    for item in args.pmtiles:
        status |= validate(item)
    return status


if __name__ == "__main__":
    raise SystemExit(main())
