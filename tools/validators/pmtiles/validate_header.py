#!/usr/bin/env python3
"""Inspect the bounded structural parts of a KFM PMTiles v3 archive.

The reusable API returns header fields and the embedded ``spec_hash``.  It does
not parse tile directories, establish source truth, or authorize release.
"""
from __future__ import annotations

import argparse
import gzip
import io
import json
import math
import re
import struct
import sys
from dataclasses import dataclass
from pathlib import Path

HEADER_BYTES = 127
MAX_METADATA_BYTES = 1024 * 1024
SHA256_RE = re.compile(r"^sha256:[a-f0-9]{64}$")
INTERNAL_COMPRESSION = frozenset({0, 1, 2, 3, 4})
TILE_COMPRESSION = frozenset({0, 1, 2, 3, 4})
TILE_TYPES = frozenset({0, 1, 2, 3, 4, 5, 6})


class HeaderValidationError(ValueError):
    """A finite, non-echoing PMTiles structural finding."""

    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


class _DuplicateKeyError(ValueError):
    pass


class _NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True)
class HeaderInfo:
    version: int
    root_offset: int
    root_length: int
    json_metadata_offset: int
    json_metadata_length: int
    leaf_directory_offset: int
    leaf_directory_length: int
    tile_data_offset: int
    tile_data_length: int
    addressed_tiles_count: int
    tile_entries_count: int
    tile_contents_count: int
    clustered: int
    internal_compression: int
    tile_compression: int
    tile_type: int
    min_zoom: int
    max_zoom: int
    min_lon_e7: int
    min_lat_e7: int
    max_lon_e7: int
    max_lat_e7: int
    center_zoom: int
    center_lon_e7: int
    center_lat_e7: int


@dataclass(frozen=True)
class ArchiveInspection:
    header: HeaderInfo
    metadata: dict[str, object]
    spec_hash: str
    archive_bytes: int


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise _DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise _NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise _NonFiniteNumberError
    return parsed


def _parse_header(header: bytes) -> HeaderInfo:
    if len(header) != HEADER_BYTES:
        raise HeaderValidationError("HEADER_TRUNCATED")
    if header[:7] != b"PMTiles":
        raise HeaderValidationError("HEADER_MAGIC_INVALID")
    if header[7] != 3:
        raise HeaderValidationError("HEADER_VERSION_UNSUPPORTED")

    values = struct.unpack_from("<11Q", header, 8)
    return HeaderInfo(
        version=header[7],
        root_offset=values[0],
        root_length=values[1],
        json_metadata_offset=values[2],
        json_metadata_length=values[3],
        leaf_directory_offset=values[4],
        leaf_directory_length=values[5],
        tile_data_offset=values[6],
        tile_data_length=values[7],
        addressed_tiles_count=values[8],
        tile_entries_count=values[9],
        tile_contents_count=values[10],
        clustered=header[96],
        internal_compression=header[97],
        tile_compression=header[98],
        tile_type=header[99],
        min_zoom=header[100],
        max_zoom=header[101],
        min_lon_e7=struct.unpack_from("<i", header, 102)[0],
        min_lat_e7=struct.unpack_from("<i", header, 106)[0],
        max_lon_e7=struct.unpack_from("<i", header, 110)[0],
        max_lat_e7=struct.unpack_from("<i", header, 114)[0],
        center_zoom=header[118],
        center_lon_e7=struct.unpack_from("<i", header, 119)[0],
        center_lat_e7=struct.unpack_from("<i", header, 123)[0],
    )


def _validate_regions(info: HeaderInfo, archive_bytes: int) -> None:
    required = (
        (info.root_offset, info.root_length),
        (info.json_metadata_offset, info.json_metadata_length),
        (info.tile_data_offset, info.tile_data_length),
    )
    if any(length <= 0 for _, length in required):
        raise HeaderValidationError("HEADER_REGION_MISSING")
    if info.root_offset + info.root_length > 16_384:
        raise HeaderValidationError("HEADER_ROOT_DIRECTORY_TOO_LARGE")

    regions = [
        (info.root_offset, info.root_length),
        (info.json_metadata_offset, info.json_metadata_length),
        (info.leaf_directory_offset, info.leaf_directory_length),
        (info.tile_data_offset, info.tile_data_length),
    ]
    nonempty: list[tuple[int, int]] = []
    for offset, length in regions:
        if length == 0:
            continue
        end = offset + length
        if offset < HEADER_BYTES or end < offset or end > archive_bytes:
            raise HeaderValidationError("HEADER_REGION_OUT_OF_BOUNDS")
        nonempty.append((offset, end))

    nonempty.sort()
    if any(current[0] < previous[1] for previous, current in zip(nonempty, nonempty[1:])):
        raise HeaderValidationError("HEADER_REGION_OVERLAP")


def _validate_header_values(info: HeaderInfo) -> None:
    # PMTiles v3 uses zero to mean an unknown count. Compare only known pairs.
    if (
        info.tile_contents_count
        and info.tile_entries_count
        and info.tile_contents_count > info.tile_entries_count
    ) or (
        info.tile_entries_count
        and info.addressed_tiles_count
        and info.tile_entries_count > info.addressed_tiles_count
    ):
        raise HeaderValidationError("HEADER_COUNT_INVALID")
    if info.clustered not in {0, 1}:
        raise HeaderValidationError("HEADER_CLUSTERED_INVALID")
    if (
        info.internal_compression not in INTERNAL_COMPRESSION
        or info.tile_compression not in TILE_COMPRESSION
        or info.tile_type not in TILE_TYPES
    ):
        raise HeaderValidationError("HEADER_ENUM_INVALID")
    if info.min_zoom > info.max_zoom:
        raise HeaderValidationError("HEADER_ZOOM_INVALID")
    if not (
        -1_800_000_000 <= info.min_lon_e7 <= info.max_lon_e7 <= 1_800_000_000
        and -900_000_000 <= info.min_lat_e7 <= info.max_lat_e7 <= 900_000_000
        and -1_800_000_000 <= info.center_lon_e7 <= 1_800_000_000
        and -900_000_000 <= info.center_lat_e7 <= 900_000_000
    ):
        raise HeaderValidationError("HEADER_BOUNDS_INVALID")


def _bounded_gzip_decompress(raw: bytes) -> bytes:
    try:
        with gzip.GzipFile(fileobj=io.BytesIO(raw), mode="rb") as stream:
            decoded = stream.read(MAX_METADATA_BYTES + 1)
    except (OSError, EOFError) as exc:
        raise HeaderValidationError("METADATA_DECOMPRESSION_INVALID") from exc
    if len(decoded) > MAX_METADATA_BYTES:
        raise HeaderValidationError("METADATA_TOO_LARGE")
    return decoded


def _load_metadata(path: Path, info: HeaderInfo) -> dict[str, object]:
    if info.json_metadata_length > MAX_METADATA_BYTES:
        raise HeaderValidationError("METADATA_TOO_LARGE")
    try:
        with path.open("rb") as stream:
            stream.seek(info.json_metadata_offset)
            raw = stream.read(info.json_metadata_length)
    except OSError as exc:
        raise HeaderValidationError("INPUT_UNREADABLE") from exc
    if len(raw) != info.json_metadata_length:
        raise HeaderValidationError("METADATA_TRUNCATED")

    if info.internal_compression == 2:
        raw = _bounded_gzip_decompress(raw)
    elif info.internal_compression != 1:
        raise HeaderValidationError("METADATA_COMPRESSION_UNSUPPORTED")

    try:
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except _DuplicateKeyError as exc:
        raise HeaderValidationError("METADATA_JSON_DUPLICATE_KEY") from exc
    except _NonFiniteNumberError as exc:
        raise HeaderValidationError("METADATA_JSON_NONFINITE_NUMBER") from exc
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise HeaderValidationError("METADATA_JSON_INVALID") from exc
    except (RecursionError, ValueError) as exc:
        raise HeaderValidationError("METADATA_JSON_COMPLEXITY_LIMIT") from exc
    if not isinstance(value, dict):
        raise HeaderValidationError("METADATA_ROOT_INVALID")
    return value


def _extract_spec_hash(metadata: dict[str, object]) -> str:
    candidates: list[object] = []
    if "spec_hash" in metadata:
        candidates.append(metadata["spec_hash"])
    nested = metadata.get("kfm")
    if isinstance(nested, dict) and "spec_hash" in nested:
        candidates.append(nested["spec_hash"])
    if not candidates:
        raise HeaderValidationError("SPEC_HASH_MISSING")

    normalized_values: list[str] = []
    for value in candidates:
        if not isinstance(value, str):
            raise HeaderValidationError("SPEC_HASH_INVALID")
        normalized = value.lower()
        if not SHA256_RE.fullmatch(normalized):
            raise HeaderValidationError("SPEC_HASH_INVALID")
        normalized_values.append(normalized)
    if len(set(normalized_values)) != 1:
        raise HeaderValidationError("SPEC_HASH_MISMATCH")
    return normalized_values[0]


def inspect_archive(path: Path) -> ArchiveInspection:
    """Return bounded PMTiles structure or raise ``HeaderValidationError``."""

    try:
        if path.is_symlink():
            raise HeaderValidationError("INPUT_SYMLINK_DENIED")
        if not path.is_file():
            raise HeaderValidationError("INPUT_NOT_FILE")
        archive_bytes = path.stat().st_size
        with path.open("rb") as stream:
            header = stream.read(HEADER_BYTES)
    except HeaderValidationError:
        raise
    except OSError as exc:
        raise HeaderValidationError("INPUT_UNREADABLE") from exc

    info = _parse_header(header)
    _validate_regions(info, archive_bytes)
    _validate_header_values(info)
    metadata = _load_metadata(path, info)
    return ArchiveInspection(
        header=info,
        metadata=metadata,
        spec_hash=_extract_spec_hash(metadata),
        archive_bytes=archive_bytes,
    )


def validate(path: Path) -> int:
    """Compatibility wrapper for the existing CLI contract."""

    try:
        inspect_archive(path)
    except HeaderValidationError as exc:
        print(f"DENY: code={exc.code}", file=sys.stderr)
        return 1
    print("STRUCTURAL_PASS: PMTiles v3 header and metadata")
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
