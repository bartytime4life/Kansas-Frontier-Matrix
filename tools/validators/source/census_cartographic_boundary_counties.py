#!/usr/bin/env python3
"""Verify the exact 2025 Census county cartographic archive without network access.

The validator reads a caller-supplied ZIP and the proposed SourceDescriptor.  It
never fetches, extracts to disk, writes lifecycle state, emits evidence, admits a
source, or authorizes release.  Its output is a bounded inspection summary for
review and receipt generation.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import re
import struct
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_DESCRIPTOR_PATH = (
    REPO_ROOT
    / "data/registry/sources/settlements-infrastructure/"
    "census_cartographic_boundary_counties_2025_500k.source.json"
)
ARCHIVE_BASENAME = "cb_2025_us_county_500k"
EXPECTED_MEMBERS = frozenset(
    {
        f"{ARCHIVE_BASENAME}.shp.ea.iso.xml",
        f"{ARCHIVE_BASENAME}.shp.iso.xml",
        f"{ARCHIVE_BASENAME}.shp",
        f"{ARCHIVE_BASENAME}.shx",
        f"{ARCHIVE_BASENAME}.dbf",
        f"{ARCHIVE_BASENAME}.prj",
        f"{ARCHIVE_BASENAME}.cpg",
    }
)
EXPECTED_FIELDS = (
    "STATEFP",
    "COUNTYFP",
    "COUNTYNS",
    "GEOIDFQ",
    "GEOID",
    "NAME",
    "NAMELSAD",
    "STUSPS",
    "STATE_NAME",
    "LSAD",
    "ALAND",
    "AWATER",
)
EXPECTED_KANSAS_GEOIDS = tuple(f"20{county:03d}" for county in range(1, 210, 2))
MAX_ARCHIVE_BYTES = 32 * 1024 * 1024
MAX_UNCOMPRESSED_BYTES = 64 * 1024 * 1024
MAX_MEMBER_COUNT = 16
MAX_COMPRESSION_RATIO = 250.0


class ArchiveValidationError(ValueError):
    """A stable, non-value-bearing archive validation failure."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


@dataclass(frozen=True)
class ArchiveExpectations:
    """Expected product facts, overridable only by unit tests."""

    national_feature_count: int = 3235
    kansas_feature_count: int = 105
    kansas_geoids: tuple[str, ...] = EXPECTED_KANSAS_GEOIDS


@dataclass(frozen=True)
class ShapeRecord:
    number: int
    content: bytes
    bbox: tuple[float, float, float, float]


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _finite_bbox(values: Iterable[float]) -> tuple[float, float, float, float]:
    bbox = tuple(values)
    if len(bbox) != 4 or not all(math.isfinite(value) for value in bbox):
        raise ArchiveValidationError("SHP_BBOX_INVALID")
    west, south, east, north = bbox
    if west >= east or south >= north:
        raise ArchiveValidationError("SHP_BBOX_INVALID")
    return west, south, east, north


def _read_shape_header(payload: bytes, expected_type: int = 5) -> tuple[float, float, float, float]:
    if len(payload) < 100:
        raise ArchiveValidationError("SHP_HEADER_TRUNCATED")
    if struct.unpack(">i", payload[0:4])[0] != 9994:
        raise ArchiveValidationError("SHP_FILE_CODE_INVALID")
    declared_bytes = struct.unpack(">i", payload[24:28])[0] * 2
    if declared_bytes != len(payload):
        raise ArchiveValidationError("SHP_FILE_LENGTH_MISMATCH")
    if struct.unpack("<i", payload[28:32])[0] != 1000:
        raise ArchiveValidationError("SHP_VERSION_INVALID")
    if struct.unpack("<i", payload[32:36])[0] != expected_type:
        raise ArchiveValidationError("SHP_TYPE_INVALID")
    return _finite_bbox(struct.unpack("<4d", payload[36:68]))


def _read_shape_records(payload: bytes) -> tuple[tuple[float, float, float, float], tuple[ShapeRecord, ...]]:
    source_bbox = _read_shape_header(payload)
    records: list[ShapeRecord] = []
    cursor = 100
    expected_number = 1
    while cursor < len(payload):
        if cursor + 8 > len(payload):
            raise ArchiveValidationError("SHP_RECORD_HEADER_TRUNCATED")
        number, content_words = struct.unpack(">2i", payload[cursor : cursor + 8])
        content_length = content_words * 2
        cursor += 8
        if number != expected_number:
            raise ArchiveValidationError("SHP_RECORD_SEQUENCE_INVALID")
        if content_length < 36 or cursor + content_length > len(payload):
            raise ArchiveValidationError("SHP_RECORD_LENGTH_INVALID")
        content = payload[cursor : cursor + content_length]
        if struct.unpack("<i", content[0:4])[0] != 5:
            raise ArchiveValidationError("SHP_RECORD_TYPE_INVALID")
        bbox = _finite_bbox(struct.unpack("<4d", content[4:36]))
        records.append(ShapeRecord(number=number, content=content, bbox=bbox))
        cursor += content_length
        expected_number += 1
    if cursor != len(payload) or not records:
        raise ArchiveValidationError("SHP_RECORD_STREAM_INVALID")
    return source_bbox, tuple(records)


def _read_shx_record_count(payload: bytes) -> int:
    _read_shape_header(payload)
    if (len(payload) - 100) % 8 != 0:
        raise ArchiveValidationError("SHX_RECORD_LENGTH_INVALID")
    return (len(payload) - 100) // 8


def _read_dbf(payload: bytes) -> tuple[tuple[str, ...], tuple[dict[str, str], ...]]:
    if len(payload) < 33:
        raise ArchiveValidationError("DBF_HEADER_TRUNCATED")
    record_count = struct.unpack("<I", payload[4:8])[0]
    header_length = struct.unpack("<H", payload[8:10])[0]
    record_length = struct.unpack("<H", payload[10:12])[0]
    if header_length < 33 or header_length > len(payload) or record_length < 2:
        raise ArchiveValidationError("DBF_HEADER_INVALID")

    fields: list[tuple[str, int]] = []
    cursor = 32
    while cursor < header_length:
        if payload[cursor] == 0x0D:
            cursor += 1
            break
        if cursor + 32 > header_length:
            raise ArchiveValidationError("DBF_FIELD_DESCRIPTOR_TRUNCATED")
        descriptor = payload[cursor : cursor + 32]
        raw_name = descriptor[0:11].split(b"\x00", 1)[0]
        try:
            name = raw_name.decode("ascii")
        except UnicodeDecodeError as exc:
            raise ArchiveValidationError("DBF_FIELD_NAME_INVALID") from exc
        width = descriptor[16]
        if not name or width < 1:
            raise ArchiveValidationError("DBF_FIELD_DESCRIPTOR_INVALID")
        fields.append((name, width))
        cursor += 32
    if cursor != header_length or not fields:
        raise ArchiveValidationError("DBF_HEADER_LENGTH_MISMATCH")
    if sum(width for _, width in fields) + 1 != record_length:
        raise ArchiveValidationError("DBF_RECORD_LENGTH_MISMATCH")

    expected_end = header_length + record_count * record_length
    if expected_end > len(payload):
        raise ArchiveValidationError("DBF_RECORDS_TRUNCATED")
    trailing = payload[expected_end:]
    if trailing not in (b"", b"\x1a"):
        raise ArchiveValidationError("DBF_TRAILING_BYTES_INVALID")

    rows: list[dict[str, str]] = []
    for index in range(record_count):
        start = header_length + index * record_length
        record = payload[start : start + record_length]
        if record[0:1] != b" ":
            raise ArchiveValidationError("DBF_DELETED_OR_INVALID_RECORD")
        offset = 1
        row: dict[str, str] = {}
        for name, width in fields:
            raw_value = record[offset : offset + width]
            try:
                row[name] = raw_value.decode("utf-8").strip()
            except UnicodeDecodeError as exc:
                raise ArchiveValidationError("DBF_VALUE_ENCODING_INVALID") from exc
            offset += width
        rows.append(row)
    return tuple(name for name, _ in fields), tuple(rows)


def _load_zip_members(archive: Path) -> tuple[bytes, Mapping[str, bytes]]:
    if archive.is_symlink() or not archive.is_file():
        raise ArchiveValidationError("ARCHIVE_NOT_FILE")
    archive_size = archive.stat().st_size
    if archive_size < 1 or archive_size > MAX_ARCHIVE_BYTES:
        raise ArchiveValidationError("ARCHIVE_SIZE_INVALID")
    archive_bytes = archive.read_bytes()
    try:
        # Inspect the same immutable in-memory bytes that are hashed below. This
        # closes the path-level read/open race without extracting any member.
        with zipfile.ZipFile(io.BytesIO(archive_bytes)) as package:
            infos = package.infolist()
            if len(infos) > MAX_MEMBER_COUNT:
                raise ArchiveValidationError("ARCHIVE_MEMBER_COUNT_EXCEEDED")
            names: set[str] = set()
            total_size = 0
            members: dict[str, bytes] = {}
            for info in infos:
                path = PurePosixPath(info.filename)
                if (
                    info.is_dir()
                    or path.is_absolute()
                    or ".." in path.parts
                    or "\\" in info.filename
                    or info.filename in names
                ):
                    raise ArchiveValidationError("ARCHIVE_MEMBER_PATH_INVALID")
                names.add(info.filename)
                total_size += info.file_size
                if total_size > MAX_UNCOMPRESSED_BYTES:
                    raise ArchiveValidationError("ARCHIVE_EXPANDED_SIZE_EXCEEDED")
                if info.compress_size == 0 and info.file_size > 0:
                    raise ArchiveValidationError("ARCHIVE_COMPRESSION_INVALID")
                if info.compress_size and info.file_size / info.compress_size > MAX_COMPRESSION_RATIO:
                    raise ArchiveValidationError("ARCHIVE_COMPRESSION_RATIO_EXCEEDED")
                members[info.filename] = package.read(info)
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        raise ArchiveValidationError("ARCHIVE_INVALID") from exc
    if frozenset(members) != EXPECTED_MEMBERS:
        raise ArchiveValidationError("ARCHIVE_MEMBERS_MISMATCH")
    return archive_bytes, members


def _union_bbox(records: Sequence[ShapeRecord]) -> tuple[float, float, float, float]:
    if not records:
        raise ArchiveValidationError("KANSAS_GEOMETRY_MISSING")
    return (
        min(record.bbox[0] for record in records),
        min(record.bbox[1] for record in records),
        max(record.bbox[2] for record in records),
        max(record.bbox[3] for record in records),
    )


def inspect_archive(
    archive: Path,
    *,
    expectations: ArchiveExpectations = ArchiveExpectations(),
) -> dict[str, object]:
    """Inspect exact local bytes and return a deterministic public-safe summary."""
    archive_bytes, members = _load_zip_members(archive)
    if members[f"{ARCHIVE_BASENAME}.cpg"].decode("ascii").strip() != "UTF-8":
        raise ArchiveValidationError("CPG_ENCODING_INVALID")
    projection = members[f"{ARCHIVE_BASENAME}.prj"].decode("ascii").strip()
    if "GCS_North_American_1983" not in projection or "GRS_1980" not in projection:
        raise ArchiveValidationError("PRJ_CRS_INVALID")

    metadata = members[f"{ARCHIVE_BASENAME}.shp.iso.xml"].decode("utf-8")
    required_metadata = (
        "2025 Cartographic Boundary File (SHP), County and Equivalent for United States, 1:500,000",
        "urn:ogc:def:crs:EPSG::4269",
        f"<gco:Integer>{expectations.national_feature_count}</gco:Integer>",
        "<gco:Date>2026-05</gco:Date>",
    )
    if any(token not in metadata for token in required_metadata):
        raise ArchiveValidationError("ISO_METADATA_MISMATCH")

    source_bbox, shapes = _read_shape_records(members[f"{ARCHIVE_BASENAME}.shp"])
    shx_count = _read_shx_record_count(members[f"{ARCHIVE_BASENAME}.shx"])
    fields, rows = _read_dbf(members[f"{ARCHIVE_BASENAME}.dbf"])
    if fields != EXPECTED_FIELDS:
        raise ArchiveValidationError("DBF_FIELDS_MISMATCH")
    if not (len(shapes) == shx_count == len(rows) == expectations.national_feature_count):
        raise ArchiveValidationError("FEATURE_COUNT_MISMATCH")

    kansas_indexes = [index for index, row in enumerate(rows) if row["STATEFP"] == "20"]
    kansas_rows = [rows[index] for index in kansas_indexes]
    kansas_shapes = [shapes[index] for index in kansas_indexes]
    geoids = tuple(sorted(row["GEOID"] for row in kansas_rows))
    if len(kansas_rows) != expectations.kansas_feature_count:
        raise ArchiveValidationError("KANSAS_FEATURE_COUNT_MISMATCH")
    if geoids != expectations.kansas_geoids or len(set(geoids)) != len(geoids):
        raise ArchiveValidationError("KANSAS_GEOID_SET_MISMATCH")

    for row in kansas_rows:
        if (
            row["GEOID"] != row["STATEFP"] + row["COUNTYFP"]
            or row["STUSPS"] != "KS"
            or row["STATE_NAME"] != "Kansas"
            or not row["COUNTYNS"]
            or not row["NAME"]
            or not row["NAMELSAD"]
            or not re.fullmatch(r"\d+", row["ALAND"])
            or not re.fullmatch(r"\d+", row["AWATER"])
        ):
            raise ArchiveValidationError("KANSAS_IDENTITY_RECORD_INVALID")

    identity_projection = [
        {field: row[field] for field in EXPECTED_FIELDS}
        for row in sorted(kansas_rows, key=lambda item: item["GEOID"])
    ]
    identity_bytes = json.dumps(
        identity_projection,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    geometry_bytes = b"".join(
        struct.pack(">I", record.number) + record.content for record in kansas_shapes
    )

    return {
        "profile": "kfm.census.cartographic-boundary-counties.archive-inspection.v1",
        "archive_sha256": _sha256(archive_bytes),
        "archive_bytes": len(archive_bytes),
        "archive_member_count": len(members),
        "source_product": "2025 county and equivalent cartographic boundary file",
        "source_scale": "1:500,000",
        "source_crs": "EPSG:4269",
        "source_bbox": list(source_bbox),
        "national_feature_count": len(rows),
        "kansas_filter": "STATEFP=20",
        "kansas_feature_count": len(kansas_rows),
        "kansas_unique_geoid_count": len(set(geoids)),
        "kansas_first_geoid": geoids[0],
        "kansas_last_geoid": geoids[-1],
        "kansas_bbox": list(_union_bbox(kansas_shapes)),
        "kansas_identity_sha256": _sha256(identity_bytes),
        "kansas_shape_records_sha256": _sha256(geometry_bytes),
        "fields": list(fields),
        "source_payload_committed": False,
        "source_activation_authorized": False,
        "evidence_bundle_emitted": False,
        "public_release_allowed": False,
        "map_runtime_binding_allowed": False,
    }


def _load_json_object(path: Path) -> dict[str, object]:
    if path.is_symlink() or not path.is_file():
        raise ArchiveValidationError("DESCRIPTOR_NOT_FILE")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ArchiveValidationError("DESCRIPTOR_INVALID_JSON") from exc
    if not isinstance(value, dict):
        raise ArchiveValidationError("DESCRIPTOR_ROOT_INVALID")
    return value


def validate_bound_archive(archive: Path, descriptor_path: Path) -> dict[str, object]:
    """Bind the offline archive summary to the proposed descriptor identity."""
    descriptor = _load_json_object(descriptor_path)
    try:
        content_identity = descriptor["source_head"]["content_identity"]  # type: ignore[index]
        expected_digest = content_identity["content_sha256"]  # type: ignore[index]
        expected_length = content_identity["content_length"]  # type: ignore[index]
        public_allowed = descriptor["public_release"]["allowed"]  # type: ignore[index]
        activation_state = descriptor["connectors"]["activation_state"]  # type: ignore[index]
        release_state = descriptor["release_state"]
        review_state = descriptor["review_state"]
    except (KeyError, TypeError) as exc:
        raise ArchiveValidationError("DESCRIPTOR_BINDING_FIELDS_MISSING") from exc
    if (
        descriptor.get("source_id")
        != "kfm://source/us/census/cartographic-boundary/counties-2025-500k"
        or public_allowed is not False
        or activation_state != "disabled"
        or release_state != "not_released"
        or review_state != "needs_review"
    ):
        raise ArchiveValidationError("DESCRIPTOR_GOVERNANCE_POSTURE_INVALID")

    summary = inspect_archive(archive)
    if summary["archive_sha256"] != expected_digest:
        raise ArchiveValidationError("ARCHIVE_DIGEST_MISMATCH")
    if summary["archive_bytes"] != expected_length:
        raise ArchiveValidationError("ARCHIVE_LENGTH_MISMATCH")
    return {
        **summary,
        "source_id": descriptor["source_id"],
        "descriptor_ref": descriptor_path.relative_to(REPO_ROOT).as_posix(),
        "validation_outcome": "PASS",
        "validation_boundary": "offline identity and structure only; not admission, evidence, review, release, or publication",
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Previously downloaded Census ZIP")
    parser.add_argument(
        "--descriptor",
        type=Path,
        default=DEFAULT_DESCRIPTOR_PATH,
        help="Proposed SourceDescriptor to bind (default: repository candidate)",
    )
    args = parser.parse_args(argv)
    try:
        summary = validate_bound_archive(args.archive, args.descriptor.resolve())
    except ArchiveValidationError as exc:
        print(f"CENSUS_COUNTY_ARCHIVE_INVALID code={exc.code}", file=sys.stderr)
        return 1
    print(json.dumps(summary, separators=(",", ":"), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
