"""Deterministic, fixture-only CSV-to-GeoJSON normalization preflight.

The preflight produces a review candidate only. It performs no network access,
source activation, lifecycle write, evidence closure, policy decision, release,
or publication. All authoritative decisions and lifecycle handoffs remain with
their owning KFM responsibility roots.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import stat
import sys
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN
from pathlib import Path
from typing import Any, Mapping, Sequence

from hashing import compute_spec_hash

MAX_PROFILE_BYTES = 128_000
MAX_CSV_BYTES = 1_000_000
MAX_HEADERS = 64
MAX_CELL_CHARS = 2_048
MAX_FINDING_POINTER_CHARS = 256
PROFILE_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
ROW_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
FIELD_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]{0,63}$")
REFERENCE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:[^\s]{1,511}$")
CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
FORMULA_PREFIXES = ("=", "+", "@", "\t", "\r")


class PreflightError(ValueError):
    """A fail-closed, value-minimized preflight failure."""

    def __init__(self, reason_code: str, pointer: str, message: str) -> None:
        super().__init__(message)
        if not PROFILE_ID_RE.fullmatch(reason_code):
            raise ValueError("reason_code must be a stable bounded identifier")
        if not isinstance(pointer, str) or not pointer or len(pointer) > MAX_FINDING_POINTER_CHARS:
            raise ValueError("pointer must be a bounded non-empty string")
        self.reason_code = reason_code
        self.pointer = pointer

    def as_report(self) -> dict[str, object]:
        return {
            "outcome": "QUARANTINE_CANDIDATE",
            "reason_code": self.reason_code,
            "pointer": self.pointer,
            "authority_created": False,
            "lifecycle_write_allowed": False,
            "network_accessed": False,
            "publication_allowed": False,
        }


@dataclass(frozen=True, slots=True)
class Profile:
    profile_id: str
    source_event_ref: str
    source_descriptor_ref: str
    source_role: str
    id_field: str
    latitude_field: str
    longitude_field: str
    property_fields: tuple[str, ...]
    expected_headers: tuple[str, ...]
    coordinate_precision: int
    max_rows: int

    @classmethod
    def from_mapping(cls, raw: Mapping[str, object]) -> "Profile":
        expected_keys = {
            "profile_id",
            "source_event_ref",
            "source_descriptor_ref",
            "source_role",
            "id_field",
            "latitude_field",
            "longitude_field",
            "property_fields",
            "expected_headers",
            "coordinate_precision",
            "max_rows",
            "execution_mode",
            "geometry_policy",
        }
        if set(raw) != expected_keys:
            raise PreflightError(
                "PROFILE_FIELDS_INVALID",
                "/profile",
                "profile fields do not match the admitted fixture profile",
            )
        profile_id = _bounded_token(raw["profile_id"], "/profile/profile_id", PROFILE_ID_RE)
        source_event_ref = _bounded_reference(raw["source_event_ref"], "/profile/source_event_ref")
        source_descriptor_ref = _bounded_reference(
            raw["source_descriptor_ref"], "/profile/source_descriptor_ref"
        )
        source_role = _bounded_token(raw["source_role"], "/profile/source_role", PROFILE_ID_RE)
        id_field = _field_name(raw["id_field"], "/profile/id_field")
        latitude_field = _field_name(raw["latitude_field"], "/profile/latitude_field")
        longitude_field = _field_name(raw["longitude_field"], "/profile/longitude_field")
        property_fields = _field_name_list(raw["property_fields"], "/profile/property_fields")
        expected_headers = _field_name_list(raw["expected_headers"], "/profile/expected_headers")
        if not isinstance(raw["coordinate_precision"], int) or not 0 <= raw["coordinate_precision"] <= 8:
            raise PreflightError(
                "COORDINATE_PRECISION_INVALID",
                "/profile/coordinate_precision",
                "coordinate precision must be an integer within 0..8",
            )
        if not isinstance(raw["max_rows"], int) or not 1 <= raw["max_rows"] <= 10_000:
            raise PreflightError(
                "ROW_LIMIT_INVALID",
                "/profile/max_rows",
                "max_rows must be an integer within 1..10000",
            )
        if raw["execution_mode"] != "FIXTURE_ONLY":
            raise PreflightError(
                "EXECUTION_MODE_NOT_ADMITTED",
                "/profile/execution_mode",
                "only FIXTURE_ONLY execution is admitted",
            )
        if raw["geometry_policy"] != "PUBLIC_SAFE_SYNTHETIC_POINTS":
            raise PreflightError(
                "GEOMETRY_POLICY_NOT_ADMITTED",
                "/profile/geometry_policy",
                "only public-safe synthetic point geometry is admitted",
            )
        mandatory = (id_field, latitude_field, longitude_field)
        if len(set(mandatory)) != len(mandatory):
            raise PreflightError(
                "MAPPING_FIELDS_OVERLAP",
                "/profile",
                "identifier and coordinate fields must be distinct",
            )
        if any(field in mandatory for field in property_fields):
            raise PreflightError(
                "PROPERTY_FIELD_OVERLAP",
                "/profile/property_fields",
                "property fields must not duplicate identifier or coordinate fields",
            )
        required_order = mandatory + property_fields
        if expected_headers != required_order:
            raise PreflightError(
                "EXPECTED_HEADER_ORDER_INVALID",
                "/profile/expected_headers",
                "expected_headers must exactly follow mapping and property order",
            )
        return cls(
            profile_id=profile_id,
            source_event_ref=source_event_ref,
            source_descriptor_ref=source_descriptor_ref,
            source_role=source_role,
            id_field=id_field,
            latitude_field=latitude_field,
            longitude_field=longitude_field,
            property_fields=property_fields,
            expected_headers=expected_headers,
            coordinate_precision=raw["coordinate_precision"],
            max_rows=raw["max_rows"],
        )

    def public_projection(self) -> dict[str, object]:
        return {
            "profile_id": self.profile_id,
            "source_event_ref": self.source_event_ref,
            "source_descriptor_ref": self.source_descriptor_ref,
            "source_role": self.source_role,
            "mapping": {
                "id_field": self.id_field,
                "latitude_field": self.latitude_field,
                "longitude_field": self.longitude_field,
                "property_fields": list(self.property_fields),
            },
            "expected_headers": list(self.expected_headers),
            "coordinate_precision": self.coordinate_precision,
            "max_rows": self.max_rows,
            "execution_mode": "FIXTURE_ONLY",
            "geometry_policy": "PUBLIC_SAFE_SYNTHETIC_POINTS",
        }


def _bounded_token(value: object, pointer: str, pattern: re.Pattern[str]) -> str:
    if not isinstance(value, str) or pattern.fullmatch(value) is None:
        raise PreflightError("TOKEN_INVALID", pointer, "value is not an admitted bounded token")
    return value


def _bounded_reference(value: object, pointer: str) -> str:
    if not isinstance(value, str) or REFERENCE_RE.fullmatch(value) is None:
        raise PreflightError("REFERENCE_INVALID", pointer, "reference is not a bounded URI-like value")
    if CONTROL_RE.search(value):
        raise PreflightError("REFERENCE_INVALID", pointer, "reference contains control characters")
    return value


def _field_name(value: object, pointer: str) -> str:
    if not isinstance(value, str) or FIELD_NAME_RE.fullmatch(value) is None:
        raise PreflightError("FIELD_NAME_INVALID", pointer, "field name is not admitted")
    return value


def _field_name_list(value: object, pointer: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not value or len(value) > MAX_HEADERS:
        raise PreflightError("FIELD_LIST_INVALID", pointer, "field list is missing or too large")
    result = tuple(_field_name(item, f"{pointer}/{index}") for index, item in enumerate(value))
    if len(set(result)) != len(result):
        raise PreflightError("DUPLICATE_FIELD", pointer, "field list contains duplicates")
    return result


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key")
        result[key] = value
    return result


def _read_regular_file(path: Path, max_bytes: int, pointer: str) -> bytes:
    flags = os.O_RDONLY
    for flag_name in ("O_BINARY", "O_CLOEXEC", "O_NONBLOCK", "O_NOFOLLOW"):
        flags |= getattr(os, flag_name, 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as exc:
        raise PreflightError("INPUT_UNREADABLE", pointer, "input could not be opened safely") from exc
    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise PreflightError("INPUT_NOT_REGULAR", pointer, "input must be a regular file")
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = -1
            raw = stream.read(max_bytes + 1)
    finally:
        if descriptor >= 0:
            os.close(descriptor)
    if len(raw) > max_bytes:
        raise PreflightError("INPUT_TOO_LARGE", pointer, "input exceeds the configured byte limit")
    return raw


def load_profile(path: Path) -> Profile:
    raw = _read_regular_file(path, MAX_PROFILE_BYTES, "/profile")
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=_reject_duplicate_keys)
    except (UnicodeError, ValueError, json.JSONDecodeError) as exc:
        raise PreflightError("PROFILE_JSON_INVALID", "/profile", "profile is not safe UTF-8 JSON") from exc
    if not isinstance(value, dict):
        raise PreflightError("PROFILE_ROOT_INVALID", "/profile", "profile root must be an object")
    return Profile.from_mapping(value)


def _header_digest(headers: Sequence[str]) -> str:
    return compute_spec_hash({"headers": list(headers)})


def _content_digest(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _decimal_coordinate(
    value: str,
    *,
    pointer: str,
    minimum: Decimal,
    maximum: Decimal,
    precision: int,
) -> float:
    if value != value.strip() or not value:
        raise PreflightError("COORDINATE_INVALID", pointer, "coordinate is empty or padded")
    if len(value) > 64 or CONTROL_RE.search(value):
        raise PreflightError("COORDINATE_INVALID", pointer, "coordinate is unsafe or too large")
    try:
        parsed = Decimal(value)
    except InvalidOperation as exc:
        raise PreflightError("COORDINATE_INVALID", pointer, "coordinate is not decimal") from exc
    if not parsed.is_finite() or parsed < minimum or parsed > maximum:
        raise PreflightError("COORDINATE_OUT_OF_RANGE", pointer, "coordinate is outside the admitted range")
    quantum = Decimal(1).scaleb(-precision)
    normalized = parsed.quantize(quantum, rounding=ROUND_HALF_EVEN)
    if normalized == Decimal("-0"):
        normalized = Decimal("0")
    return float(normalized)


def _bounded_cell(value: str, pointer: str) -> str:
    if len(value) > MAX_CELL_CHARS or CONTROL_RE.search(value):
        raise PreflightError("CELL_INVALID", pointer, "cell is unsafe or too large")
    if value.startswith(FORMULA_PREFIXES):
        raise PreflightError("FORMULA_LIKE_CELL", pointer, "formula-like cell is not admitted")
    if value != value.strip():
        raise PreflightError("PADDED_CELL", pointer, "cell contains leading or trailing whitespace")
    return value


def _feature_identity(profile: Profile, row_id: str) -> str:
    subject = f"{profile.profile_id}\x1f{profile.source_descriptor_ref}\x1f{row_id}".encode("utf-8")
    return "kfm:csv-feature:sha256:" + hashlib.sha256(subject).hexdigest()


def normalize_csv(profile: Profile, raw_csv: bytes) -> dict[str, object]:
    if not raw_csv:
        raise PreflightError("CSV_EMPTY", "/csv", "CSV input is empty")
    if raw_csv.startswith(b"\xef\xbb\xbf"):
        raise PreflightError("CSV_BOM_NOT_ADMITTED", "/csv", "UTF-8 BOM is not admitted")
    try:
        text = raw_csv.decode("utf-8")
    except UnicodeError as exc:
        raise PreflightError("CSV_ENCODING_INVALID", "/csv", "CSV is not strict UTF-8") from exc
    stream = io.StringIO(text, newline="")
    try:
        reader = csv.reader(stream, strict=True)
        header = next(reader)
    except (StopIteration, csv.Error) as exc:
        raise PreflightError("CSV_PARSE_ERROR", "/csv", "CSV header could not be parsed") from exc
    if len(header) > MAX_HEADERS:
        raise PreflightError("CSV_HEADER_TOO_LARGE", "/csv/headers", "CSV has too many headers")
    if len(set(header)) != len(header):
        raise PreflightError("CSV_DUPLICATE_HEADER", "/csv/headers", "CSV contains duplicate headers")
    if tuple(header) != profile.expected_headers:
        raise PreflightError("CSV_HEADER_MISMATCH", "/csv/headers", "CSV headers do not match profile")

    features: list[tuple[str, dict[str, object]]] = []
    seen_ids: set[str] = set()
    row_count = 0
    for line_number, row in enumerate(reader, start=2):
        row_count += 1
        if row_count > profile.max_rows:
            raise PreflightError("CSV_ROW_LIMIT_EXCEEDED", "/csv", "CSV exceeds profile row limit")
        if len(row) != len(header):
            raise PreflightError(
                "CSV_COLUMN_COUNT_MISMATCH",
                f"/csv/rows/{line_number}",
                "CSV row column count does not match header",
            )
        values = dict(zip(header, row, strict=True))
        row_id_raw = values[profile.id_field]
        if row_id_raw != row_id_raw.strip() or ROW_ID_RE.fullmatch(row_id_raw) is None:
            raise PreflightError(
                "ROW_ID_INVALID", f"/csv/rows/{line_number}/{profile.id_field}", "row ID is invalid"
            )
        if row_id_raw in seen_ids:
            raise PreflightError(
                "DUPLICATE_ROW_ID",
                f"/csv/rows/{line_number}/{profile.id_field}",
                "row ID is duplicated",
            )
        seen_ids.add(row_id_raw)
        latitude = _decimal_coordinate(
            values[profile.latitude_field],
            pointer=f"/csv/rows/{line_number}/{profile.latitude_field}",
            minimum=Decimal("-90"),
            maximum=Decimal("90"),
            precision=profile.coordinate_precision,
        )
        longitude = _decimal_coordinate(
            values[profile.longitude_field],
            pointer=f"/csv/rows/{line_number}/{profile.longitude_field}",
            minimum=Decimal("-180"),
            maximum=Decimal("180"),
            precision=profile.coordinate_precision,
        )
        properties: dict[str, object] = {"source_row_id": row_id_raw}
        for field_name in profile.property_fields:
            properties[field_name] = _bounded_cell(
                values[field_name], f"/csv/rows/{line_number}/{field_name}"
            )
        feature_id = _feature_identity(profile, row_id_raw)
        features.append(
            (
                row_id_raw,
                {
                    "type": "Feature",
                    "id": feature_id,
                    "geometry": {"type": "Point", "coordinates": [longitude, latitude]},
                    "properties": properties,
                },
            )
        )
    if row_count == 0:
        raise PreflightError("CSV_NO_DATA_ROWS", "/csv", "CSV contains no data rows")

    feature_collection = {
        "type": "FeatureCollection",
        "features": [feature for _, feature in sorted(features, key=lambda item: item[0])],
    }
    candidate_base: dict[str, object] = {
        "contract": "kfm.source.csv-geojson-normalization-candidate.v1",
        "profile": profile.public_projection(),
        "input": {
            "media_type": "text/csv",
            "content_digest": _content_digest(raw_csv),
            "byte_length": len(raw_csv),
            "row_count": row_count,
            "header_digest": _header_digest(header),
        },
        "result": {
            "outcome": "NORMALIZED_CANDIDATE",
            "feature_count": row_count,
            "feature_collection_digest": compute_spec_hash(feature_collection),
            "feature_collection": feature_collection,
        },
        "governance": {
            "authority_created": False,
            "evidence_created": False,
            "fixture_only": True,
            "lifecycle_write_allowed": False,
            "network_accessed": False,
            "policy_decided": False,
            "publication_allowed": False,
            "release_created": False,
            "source_activated": False,
        },
    }
    spec_hash = compute_spec_hash(candidate_base)
    return {
        "candidate_id": "kfm:csv-geojson-normalization:" + spec_hash.removeprefix("sha256:")[:32],
        **candidate_base,
        "spec_hash": spec_hash,
    }


def normalize_files(profile_path: Path, csv_path: Path) -> dict[str, object]:
    profile = load_profile(profile_path)
    raw_csv = _read_regular_file(csv_path, MAX_CSV_BYTES, "/csv")
    return normalize_csv(profile, raw_csv)


def write_candidate(path: Path, candidate: Mapping[str, object]) -> None:
    if path.exists() or path.is_symlink():
        raise PreflightError("OUTPUT_ALREADY_EXISTS", "/output", "output path already exists")
    parent = path.parent
    parent.mkdir(parents=True, exist_ok=True)
    if parent.is_symlink():
        raise PreflightError("OUTPUT_PARENT_UNSAFE", "/output", "output parent is a symlink")
    payload = (json.dumps(candidate, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode(
        "utf-8"
    )
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    flags |= getattr(os, "O_CLOEXEC", 0)
    descriptor = os.open(path, flags, 0o600)
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Create a deterministic fixture-only CSV-to-GeoJSON review candidate."
    )
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--csv", dest="csv_path", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        candidate = normalize_files(args.profile, args.csv_path)
        write_candidate(args.output, candidate)
    except PreflightError as exc:
        print(json.dumps(exc.as_report(), sort_keys=True, separators=(",", ":")))
        return 2
    except Exception:  # noqa: BLE001 - emit a bounded non-secret operational result.
        print(
            json.dumps(
                {
                    "outcome": "ERROR",
                    "reason_code": "PREFLIGHT_INTERNAL_ERROR",
                    "authority_created": False,
                    "lifecycle_write_allowed": False,
                    "network_accessed": False,
                    "publication_allowed": False,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 1
    print(
        json.dumps(
            {
                "candidate_id": candidate["candidate_id"],
                "feature_count": candidate["result"]["feature_count"],
                "outcome": "NORMALIZED_CANDIDATE",
                "output": args.output.as_posix(),
                "spec_hash": candidate["spec_hash"],
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
