"""Deterministic, fixture-only SSURGO package drift review helper.

This module compares two frozen synthetic sidecars. It performs no network
access, does not fetch SSURGO, and cannot create lifecycle, receipt, proof,
promotion, release, or publication authority.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import stat
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence


PROFILE_ID = "kfm.ssurgo-watch.synthetic.v1"
SPATIAL_DIFF_PROFILE_ID = "kfm.ssurgo-watch.synthetic-spatial-diff.v1"
SPATIAL_CHANGE_CRS = "EPSG:5070"
SPATIAL_CHANGE_AREA_UNIT = "m2"
FIXTURE_SOURCE_DESCRIPTOR_REF = "fixture://source/nrcs-ssurgo"
FIXTURE_SURVEY_AREA_SYMBOL = "ZZ999"
PPM_DENOMINATOR = 1_000_000
MAX_FILE_BYTES = 262_144
MAX_AREA_M2 = 10**15
MAX_MAPUNITS = 5_000
MAX_TABLES = 64
MAX_COLUMNS_PER_TABLE = 512
REPO_ROOT = Path(__file__).resolve().parents[3]

SAFE_EXIT_OUTCOMES = frozenset({"NO_MATERIAL_CHANGE"})
BLOCKING_OUTCOMES = frozenset(
    {
        "PROPOSED_WORK_RECORD",
        "GEOMETRY_DRIFT",
        "STALE_INPUT",
        "ABSTAIN",
        "ERROR",
    }
)

ALLOWED_TOP_LEVEL_FIELDS = frozenset(
    {
        "profile_id",
        "spec_hash",
        "content_hash",
        "fixture_only",
        "source_descriptor_ref",
        "survey_area_symbol",
        "observed_at",
        "package_identifier",
        "publication_date",
        "package_sha256",
        "extraction_profile_hash",
        "geometry_profile_hash",
        "analysis_geometry_hash",
        "analysis_area_m2",
        "mapunit_areas_m2",
        "mapunit_geometry_hashes",
        "attribute_schema",
        "table_content_hashes",
        "materiality_profile",
    }
)
ALLOWED_PROFILE_FIELDS = frozenset({"mapunit_area_change_ppm"})
ALLOWED_COLUMN_FIELDS = frozenset(
    {"name", "type", "nullable", "primary_key", "references"}
)
ALLOWED_SPATIAL_DIFF_FIELDS = frozenset(
    {
        "profile_id",
        "fixture_only",
        "method",
        "crs",
        "area_unit",
        "geometry_profile_hash",
        "prior_content_hash",
        "current_content_hash",
        "prior_geometry_set_hash",
        "current_geometry_set_hash",
        "changed_label_area_m2",
        "content_hash",
    }
)
SPATIAL_CHANGE_METHOD = "synthetic_mapunit_partition_disagreement_v1"
ALLOWED_COLUMN_TYPES = frozenset({"boolean", "date", "integer", "number", "text"})

_SHA256 = re.compile(r"sha256:[0-9a-f]{64}\Z")
_UTC = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\Z")
_DATE = re.compile(r"\d{4}-\d{2}-\d{2}\Z")
_PACKAGE_ID = re.compile(r"[A-Z0-9][A-Z0-9_.-]{0,127}\Z")
_MAPUNIT_ID = re.compile(r"MU-FIX-[A-Z0-9][A-Z0-9_-]{0,63}\Z")
_SQL_NAME = re.compile(r"[a-z][a-z0-9_]{0,63}\Z")


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class LoadedSidecar:
    candidate: dict[str, object] | None
    findings: tuple[Finding, ...]


@dataclass(frozen=True)
class LoadedSpatialDiff:
    candidate: dict[str, object] | None
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    """Raised when JSON contains a duplicate object key."""


def _pairs_without_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _parse_bounded_int(raw: str) -> int:
    digits = raw[1:] if raw.startswith("-") else raw
    if len(digits) > len(str(MAX_AREA_M2)):
        raise ValueError("integer exceeds fixture profile bounds")
    value = int(raw)
    if abs(value) > MAX_AREA_M2:
        raise ValueError("integer exceeds fixture profile bounds")
    return value


def _reject_json_constant(raw: str) -> object:
    raise ValueError(f"non-finite JSON constant is denied: {raw}")


def canonical_bytes(candidate: Mapping[str, object]) -> bytes:
    return json.dumps(
        candidate,
        ensure_ascii=True,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def compute_spec_hash(candidate: Mapping[str, object]) -> str:
    payload = {
        field: candidate.get(field)
        for field in (
            "profile_id",
            "fixture_only",
            "source_descriptor_ref",
            "extraction_profile_hash",
            "geometry_profile_hash",
            "materiality_profile",
        )
    }
    return "sha256:" + hashlib.sha256(canonical_bytes(payload)).hexdigest()


def compute_content_hash(candidate: Mapping[str, object]) -> str:
    payload = dict(candidate)
    payload.pop("content_hash", None)
    return "sha256:" + hashlib.sha256(canonical_bytes(payload)).hexdigest()


def compute_geometry_set_hash(candidate: Mapping[str, object]) -> str:
    payload = {
        "geometry_profile_hash": candidate.get("geometry_profile_hash"),
        "analysis_geometry_hash": candidate.get("analysis_geometry_hash"),
        "analysis_area_m2": candidate.get("analysis_area_m2"),
        "mapunit_geometry_hashes": candidate.get("mapunit_geometry_hashes"),
    }
    return "sha256:" + hashlib.sha256(canonical_bytes(payload)).hexdigest()


def compute_spatial_diff_content_hash(candidate: Mapping[str, object]) -> str:
    payload = dict(candidate)
    payload.pop("content_hash", None)
    return "sha256:" + hashlib.sha256(canonical_bytes(payload)).hexdigest()


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code, path))


def _is_bounded_int(value: object, *, minimum: int, maximum: int) -> bool:
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
        and minimum <= value <= maximum
    )


def _is_hash(value: object) -> bool:
    return (
        isinstance(value, str)
        and _SHA256.fullmatch(value) is not None
        and value != "sha256:" + ("0" * 64)
    )


def _is_canonical_utc(value: object) -> bool:
    if not isinstance(value, str) or _UTC.fullmatch(value) is None:
        return False
    try:
        parsed = dt.datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return parsed.tzinfo == dt.timezone.utc


def _is_canonical_date(value: object) -> bool:
    if not isinstance(value, str) or _DATE.fullmatch(value) is None:
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _validate_mapunits(
    findings: set[Finding], mapunits: object, analysis_area_m2: object
) -> None:
    path = "$.mapunit_areas_m2"
    if not isinstance(mapunits, dict) or not mapunits:
        _add(findings, "MAPUNIT_AREAS_INVALID", path)
        return
    if len(mapunits) > MAX_MAPUNITS:
        _add(findings, "MAPUNIT_COUNT_EXCEEDED", path)
        return

    total = 0
    for mapunit_id, area_m2 in sorted(
        mapunits.items(), key=lambda item: (type(item[0]).__name__, repr(item[0]))
    ):
        item_path = f"{path}.{mapunit_id}"
        if not isinstance(mapunit_id, str) or _MAPUNIT_ID.fullmatch(mapunit_id) is None:
            _add(findings, "MAPUNIT_ID_INVALID", item_path)
        if not _is_bounded_int(area_m2, minimum=0, maximum=MAX_AREA_M2):
            _add(findings, "MAPUNIT_AREA_INVALID", item_path)
            continue
        total += area_m2

    if total == 0:
        _add(findings, "MAPUNIT_COVERAGE_ZERO", path)
    if _is_bounded_int(analysis_area_m2, minimum=1, maximum=MAX_AREA_M2):
        if total != analysis_area_m2:
            _add(findings, "MAPUNIT_COVERAGE_MISMATCH", path)


def _validate_mapunit_geometry_hashes(
    findings: set[Finding], geometry_hashes: object, mapunits: object
) -> None:
    path = "$.mapunit_geometry_hashes"
    if not isinstance(geometry_hashes, dict) or not geometry_hashes:
        _add(findings, "MAPUNIT_GEOMETRY_HASHES_INVALID", path)
        return
    if len(geometry_hashes) > MAX_MAPUNITS:
        _add(findings, "MAPUNIT_GEOMETRY_COUNT_EXCEEDED", path)
        return
    if isinstance(mapunits, dict) and set(geometry_hashes) != set(mapunits):
        _add(findings, "MAPUNIT_GEOMETRY_KEYSET_MISMATCH", path)
    for mapunit_id, geometry_hash in sorted(
        geometry_hashes.items(),
        key=lambda item: (type(item[0]).__name__, repr(item[0])),
    ):
        item_path = f"{path}.{mapunit_id}"
        if not isinstance(mapunit_id, str) or _MAPUNIT_ID.fullmatch(mapunit_id) is None:
            _add(findings, "MAPUNIT_GEOMETRY_ID_INVALID", item_path)
        if not _is_hash(geometry_hash):
            _add(findings, "MAPUNIT_GEOMETRY_HASH_INVALID", item_path)


def _validate_attribute_schema(findings: set[Finding], schema: object) -> None:
    path = "$.attribute_schema"
    if not isinstance(schema, dict) or not schema:
        _add(findings, "ATTRIBUTE_SCHEMA_INVALID", path)
        return
    if len(schema) > MAX_TABLES:
        _add(findings, "ATTRIBUTE_TABLE_COUNT_EXCEEDED", path)
        return

    for table_name, columns in sorted(
        schema.items(), key=lambda item: (type(item[0]).__name__, repr(item[0]))
    ):
        table_path = f"{path}.{table_name}"
        if not isinstance(table_name, str) or _SQL_NAME.fullmatch(table_name) is None:
            _add(findings, "ATTRIBUTE_TABLE_NAME_INVALID", table_path)
        if not isinstance(columns, list) or not columns:
            _add(findings, "ATTRIBUTE_COLUMNS_INVALID", table_path)
            continue
        if len(columns) > MAX_COLUMNS_PER_TABLE:
            _add(findings, "ATTRIBUTE_COLUMN_COUNT_EXCEEDED", table_path)
            continue

        seen_names: set[str] = set()
        ordered_names: list[str] = []
        for index, column in enumerate(columns):
            column_path = f"{table_path}[{index}]"
            if not isinstance(column, dict):
                _add(findings, "ATTRIBUTE_COLUMN_INVALID", column_path)
                continue
            undeclared = set(column) - ALLOWED_COLUMN_FIELDS
            missing = ALLOWED_COLUMN_FIELDS - set(column)
            for field in sorted(undeclared):
                _add(findings, "UNDECLARED_COLUMN_FIELD", f"{column_path}.{field}")
            for field in sorted(missing):
                _add(findings, "MISSING_COLUMN_FIELD", f"{column_path}.{field}")

            name = column.get("name")
            if not isinstance(name, str) or _SQL_NAME.fullmatch(name) is None:
                _add(findings, "ATTRIBUTE_COLUMN_NAME_INVALID", f"{column_path}.name")
            else:
                if name in seen_names:
                    _add(findings, "DUPLICATE_ATTRIBUTE_COLUMN", f"{column_path}.name")
                seen_names.add(name)
                ordered_names.append(name)

            column_type = column.get("type")
            if column_type not in ALLOWED_COLUMN_TYPES:
                _add(findings, "ATTRIBUTE_COLUMN_TYPE_INVALID", f"{column_path}.type")
            if not isinstance(column.get("nullable"), bool):
                _add(findings, "ATTRIBUTE_COLUMN_NULLABLE_INVALID", f"{column_path}.nullable")
            if not isinstance(column.get("primary_key"), bool):
                _add(findings, "ATTRIBUTE_PRIMARY_KEY_INVALID", f"{column_path}.primary_key")
            reference = column.get("references")
            if reference is not None:
                if not isinstance(reference, str) or reference.count(".") != 1:
                    _add(findings, "ATTRIBUTE_REFERENCE_INVALID", f"{column_path}.references")
                else:
                    referenced_table, referenced_column = reference.split(".", 1)
                    if (
                        _SQL_NAME.fullmatch(referenced_table) is None
                        or _SQL_NAME.fullmatch(referenced_column) is None
                    ):
                        _add(
                            findings,
                            "ATTRIBUTE_REFERENCE_INVALID",
                            f"{column_path}.references",
                        )

        if ordered_names != sorted(ordered_names):
            _add(findings, "ATTRIBUTE_COLUMNS_NOT_CANONICAL", table_path)

    for table_name, columns in sorted(schema.items()):
        if not isinstance(table_name, str) or not isinstance(columns, list):
            continue
        valid_columns = [column for column in columns if isinstance(column, dict)]
        if valid_columns and not any(
            column.get("primary_key") is True for column in valid_columns
        ):
            _add(findings, "ATTRIBUTE_PRIMARY_KEY_MISSING", f"{path}.{table_name}")
        for index, column in enumerate(valid_columns):
            column_path = f"{path}.{table_name}[{index}]"
            if column.get("primary_key") is True and column.get("nullable") is not False:
                _add(findings, "ATTRIBUTE_PRIMARY_KEY_NULLABLE", f"{column_path}.nullable")
            reference = column.get("references")
            if not isinstance(reference, str) or reference.count(".") != 1:
                continue
            referenced_table, referenced_column = reference.split(".", 1)
            target_columns = schema.get(referenced_table)
            if not isinstance(target_columns, list):
                _add(
                    findings,
                    "ATTRIBUTE_REFERENCE_TARGET_MISSING",
                    f"{column_path}.references",
                )
                continue
            target = next(
                (
                    candidate
                    for candidate in target_columns
                    if isinstance(candidate, dict)
                    and candidate.get("name") == referenced_column
                ),
                None,
            )
            if target is None:
                _add(
                    findings,
                    "ATTRIBUTE_REFERENCE_TARGET_MISSING",
                    f"{column_path}.references",
                )
                continue
            if target.get("primary_key") is not True:
                _add(
                    findings,
                    "ATTRIBUTE_REFERENCE_TARGET_NOT_PRIMARY_KEY",
                    f"{column_path}.references",
                )
            if column.get("type") != target.get("type"):
                _add(
                    findings,
                    "ATTRIBUTE_REFERENCE_TYPE_MISMATCH",
                    f"{column_path}.references",
                )


def _validate_table_content_hashes(
    findings: set[Finding], content_hashes: object, schema: object
) -> None:
    path = "$.table_content_hashes"
    if not isinstance(content_hashes, dict) or not content_hashes:
        _add(findings, "TABLE_CONTENT_HASHES_INVALID", path)
        return
    if isinstance(schema, dict) and set(content_hashes) != set(schema):
        _add(findings, "TABLE_CONTENT_KEYSET_MISMATCH", path)
    for table_name, content_hash in sorted(
        content_hashes.items(),
        key=lambda item: (type(item[0]).__name__, repr(item[0])),
    ):
        item_path = f"{path}.{table_name}"
        if not isinstance(table_name, str) or _SQL_NAME.fullmatch(table_name) is None:
            _add(findings, "TABLE_CONTENT_NAME_INVALID", item_path)
        if not _is_hash(content_hash):
            _add(findings, "TABLE_CONTENT_HASH_INVALID", item_path)


def validate_spatial_diff(candidate: object) -> list[Finding]:
    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("SPATIAL_DIFF_NOT_OBJECT", "$")]
    for field in sorted(set(candidate) - ALLOWED_SPATIAL_DIFF_FIELDS):
        _add(findings, "UNDECLARED_SPATIAL_DIFF_FIELD", f"$.{field}")
    for field in sorted(ALLOWED_SPATIAL_DIFF_FIELDS - set(candidate)):
        _add(findings, "MISSING_SPATIAL_DIFF_FIELD", f"$.{field}")
    if candidate.get("profile_id") != SPATIAL_DIFF_PROFILE_ID:
        _add(findings, "SPATIAL_DIFF_PROFILE_ID_INVALID", "$.profile_id")
    if candidate.get("fixture_only") is not True:
        _add(findings, "SPATIAL_DIFF_FIXTURE_ONLY_REQUIRED", "$.fixture_only")
    if candidate.get("method") != SPATIAL_CHANGE_METHOD:
        _add(findings, "SPATIAL_DIFF_METHOD_INVALID", "$.method")
    if candidate.get("crs") != SPATIAL_CHANGE_CRS:
        _add(findings, "SPATIAL_DIFF_CRS_INVALID", "$.crs")
    if candidate.get("area_unit") != SPATIAL_CHANGE_AREA_UNIT:
        _add(findings, "SPATIAL_DIFF_AREA_UNIT_INVALID", "$.area_unit")
    for field in (
        "geometry_profile_hash",
        "prior_content_hash",
        "current_content_hash",
        "prior_geometry_set_hash",
        "current_geometry_set_hash",
    ):
        if not _is_hash(candidate.get(field)):
            _add(findings, "SPATIAL_DIFF_HASH_INVALID", f"$.{field}")
    if not _is_bounded_int(
        candidate.get("changed_label_area_m2"), minimum=0, maximum=MAX_AREA_M2
    ):
        _add(findings, "SPATIAL_DIFF_AREA_INVALID", "$.changed_label_area_m2")
    content_hash = candidate.get("content_hash")
    if not _is_hash(content_hash):
        _add(findings, "SPATIAL_DIFF_CONTENT_HASH_INVALID", "$.content_hash")
    else:
        try:
            expected_hash = compute_spatial_diff_content_hash(candidate)
        except (TypeError, ValueError, UnicodeError, OverflowError):
            _add(findings, "SPATIAL_DIFF_CONTENT_HASH_INPUT_INVALID", "$.content_hash")
        else:
            if content_hash != expected_hash:
                _add(findings, "SPATIAL_DIFF_CONTENT_HASH_MISMATCH", "$.content_hash")
    return sorted(findings)


def _validate_materiality_profile(findings: set[Finding], profile: object) -> None:
    path = "$.materiality_profile"
    if not isinstance(profile, dict):
        _add(findings, "MATERIALITY_PROFILE_INVALID", path)
        return
    for field in sorted(set(profile) - ALLOWED_PROFILE_FIELDS):
        _add(findings, "UNDECLARED_MATERIALITY_FIELD", f"{path}.{field}")
    for field in sorted(ALLOWED_PROFILE_FIELDS - set(profile)):
        _add(findings, "MISSING_MATERIALITY_FIELD", f"{path}.{field}")
    if not _is_bounded_int(
        profile.get("mapunit_area_change_ppm"), minimum=1, maximum=PPM_DENOMINATOR
    ):
        _add(findings, "MAPUNIT_CHANGE_THRESHOLD_INVALID", f"{path}.mapunit_area_change_ppm")


def validate_sidecar(candidate: object) -> list[Finding]:
    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("SIDECAR_NOT_OBJECT", "$")]

    for field in sorted(set(candidate) - ALLOWED_TOP_LEVEL_FIELDS):
        _add(findings, "UNDECLARED_TOP_LEVEL_FIELD", f"$.{field}")
    for field in sorted(ALLOWED_TOP_LEVEL_FIELDS - set(candidate)):
        _add(findings, "MISSING_TOP_LEVEL_FIELD", f"$.{field}")

    if candidate.get("profile_id") != PROFILE_ID:
        _add(findings, "PROFILE_ID_INVALID", "$.profile_id")
    if candidate.get("fixture_only") is not True:
        _add(findings, "FIXTURE_ONLY_REQUIRED", "$.fixture_only")
    if candidate.get("source_descriptor_ref") != FIXTURE_SOURCE_DESCRIPTOR_REF:
        _add(findings, "FIXTURE_SOURCE_DESCRIPTOR_REF_INVALID", "$.source_descriptor_ref")
    if candidate.get("survey_area_symbol") != FIXTURE_SURVEY_AREA_SYMBOL:
        _add(findings, "FIXTURE_SURVEY_AREA_INVALID", "$.survey_area_symbol")
    if not _is_canonical_utc(candidate.get("observed_at")):
        _add(findings, "OBSERVED_AT_INVALID", "$.observed_at")
    if not _is_canonical_date(candidate.get("publication_date")):
        _add(findings, "PUBLICATION_DATE_INVALID", "$.publication_date")
    if (
        _is_canonical_utc(candidate.get("observed_at"))
        and _is_canonical_date(candidate.get("publication_date"))
        and str(candidate["publication_date"]) > str(candidate["observed_at"])[:10]
    ):
        _add(findings, "PUBLICATION_AFTER_OBSERVATION", "$.publication_date")

    package_identifier = candidate.get("package_identifier")
    if not isinstance(package_identifier, str) or _PACKAGE_ID.fullmatch(package_identifier) is None:
        _add(findings, "PACKAGE_IDENTIFIER_INVALID", "$.package_identifier")
    if not _is_hash(candidate.get("package_sha256")):
        _add(findings, "PACKAGE_SHA256_INVALID", "$.package_sha256")
    if not _is_hash(candidate.get("extraction_profile_hash")):
        _add(findings, "EXTRACTION_PROFILE_HASH_INVALID", "$.extraction_profile_hash")
    if not _is_hash(candidate.get("geometry_profile_hash")):
        _add(findings, "GEOMETRY_PROFILE_HASH_INVALID", "$.geometry_profile_hash")
    if not _is_hash(candidate.get("analysis_geometry_hash")):
        _add(findings, "ANALYSIS_GEOMETRY_HASH_INVALID", "$.analysis_geometry_hash")

    analysis_area_m2 = candidate.get("analysis_area_m2")
    if not _is_bounded_int(analysis_area_m2, minimum=1, maximum=MAX_AREA_M2):
        _add(findings, "ANALYSIS_AREA_INVALID", "$.analysis_area_m2")
    mapunit_areas = candidate.get("mapunit_areas_m2")
    _validate_mapunits(findings, mapunit_areas, analysis_area_m2)
    _validate_mapunit_geometry_hashes(
        findings, candidate.get("mapunit_geometry_hashes"), mapunit_areas
    )
    attribute_schema = candidate.get("attribute_schema")
    _validate_attribute_schema(findings, attribute_schema)
    _validate_table_content_hashes(
        findings, candidate.get("table_content_hashes"), attribute_schema
    )
    _validate_materiality_profile(findings, candidate.get("materiality_profile"))

    spec_hash = candidate.get("spec_hash")
    if not _is_hash(spec_hash):
        _add(findings, "SPEC_HASH_INVALID", "$.spec_hash")
    else:
        try:
            expected_hash = compute_spec_hash(candidate)
        except (TypeError, ValueError, UnicodeError, OverflowError):
            _add(findings, "SPEC_HASH_INPUT_INVALID", "$.spec_hash")
        else:
            if spec_hash != expected_hash:
                _add(findings, "SPEC_HASH_MISMATCH", "$.spec_hash")

    content_hash = candidate.get("content_hash")
    if not _is_hash(content_hash):
        _add(findings, "CONTENT_HASH_INVALID", "$.content_hash")
    else:
        try:
            expected_hash = compute_content_hash(candidate)
        except (TypeError, ValueError, UnicodeError, OverflowError):
            _add(findings, "CONTENT_HASH_INPUT_INVALID", "$.content_hash")
        else:
            if content_hash != expected_hash:
                _add(findings, "CONTENT_HASH_MISMATCH", "$.content_hash")

    return sorted(findings)


def _load_bounded_json(path: Path | str) -> tuple[object | None, tuple[Finding, ...]]:
    source = Path(path)
    try:
        flags = os.O_RDONLY
        for flag_name in ("O_BINARY", "O_CLOEXEC", "O_NOFOLLOW"):
            flags |= getattr(os, flag_name, 0)
        descriptor = os.open(source, flags)
        with os.fdopen(descriptor, "rb") as stream:
            metadata = os.fstat(stream.fileno())
            if not stat.S_ISREG(metadata.st_mode):
                return None, (Finding("FILE_TYPE_INVALID", "$"),)
            if metadata.st_size <= 0 or metadata.st_size > MAX_FILE_BYTES:
                return None, (Finding("FILE_SIZE_INVALID", "$"),)
            raw = stream.read(MAX_FILE_BYTES + 1)
            if len(raw) != metadata.st_size or len(raw) > MAX_FILE_BYTES:
                return None, (Finding("FILE_SIZE_INVALID", "$"),)
        text = raw.decode("utf-8")
        candidate = json.loads(
            text,
            object_pairs_hook=_pairs_without_duplicates,
            parse_int=_parse_bounded_int,
            parse_constant=_reject_json_constant,
        )
    except DuplicateKeyError:
        return None, (Finding("DUPLICATE_JSON_KEY", "$"),)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("DOCUMENT_LOAD_ERROR", "$"),)

    return candidate, ()


def load_sidecar(path: Path | str) -> LoadedSidecar:
    candidate, load_findings = _load_bounded_json(path)
    if load_findings:
        normalized = tuple(
            Finding(
                "SIDECAR_LOAD_ERROR"
                if finding.code == "DOCUMENT_LOAD_ERROR"
                else finding.code,
                finding.path,
            )
            for finding in load_findings
        )
        return LoadedSidecar(None, normalized)

    findings = tuple(validate_sidecar(candidate))
    return LoadedSidecar(
        candidate if isinstance(candidate, dict) and not findings else None,
        findings,
    )


def load_spatial_diff(path: Path | str) -> LoadedSpatialDiff:
    candidate, load_findings = _load_bounded_json(path)
    if load_findings:
        normalized = tuple(
            Finding(
                "SPATIAL_DIFF_LOAD_ERROR"
                if finding.code == "DOCUMENT_LOAD_ERROR"
                else finding.code,
                finding.path,
            )
            for finding in load_findings
        )
        return LoadedSpatialDiff(None, normalized)

    findings = tuple(validate_spatial_diff(candidate))
    return LoadedSpatialDiff(
        candidate if isinstance(candidate, dict) and not findings else None,
        findings,
    )


def _schema_signature(schema: object) -> str:
    assert isinstance(schema, dict)
    normalized: dict[str, list[dict[str, object]]] = {}
    for table_name, columns in sorted(schema.items()):
        assert isinstance(table_name, str) and isinstance(columns, list)
        normalized[table_name] = sorted(
            (dict(column) for column in columns if isinstance(column, dict)),
            key=lambda column: str(column.get("name")),
        )
    return "sha256:" + hashlib.sha256(canonical_bytes(normalized)).hexdigest()


def _report(
    *,
    prior_path: Path,
    current_path: Path,
    outcome: str,
    reason_codes: Sequence[str],
    checks: Mapping[str, object],
    prior: Mapping[str, object] | None,
    current: Mapping[str, object] | None,
    spatial_diff_path: Path | None = None,
    spatial_diff: Mapping[str, object] | None = None,
) -> dict[str, object]:
    report: dict[str, object] = {
        "tool": "ssurgo-watch",
        "report_profile": PROFILE_ID,
        "status": outcome,
        "inputs": {
            "prior_sidecar": prior_path.name,
            "current_sidecar": current_path.name,
        },
        "checks": dict(checks),
        "decision": {
            "outcome": outcome,
            "reason_codes": sorted(set(reason_codes)),
            "blocking": outcome in BLOCKING_OUTCOMES,
            "publication": False,
            "promotion_allowed": False,
            "steward_review_required": outcome != "NO_MATERIAL_CHANGE",
        },
        "next_review": [
            "confirm an admitted SSURGO SourceDescriptor and current rights posture",
            "confirm survey-area geometry, projection, package vintage, and schema interpretation",
            "obtain steward approval for any live materiality policy",
            "use connectors and pipelines of record for source capture and lifecycle mutation",
            (
                "do not promote or publish without evidence, policy, review, "
                "release, and rollback closure"
            ),
        ],
    }
    if prior is not None and current is not None:
        report["inputs"] = {
            "prior_sidecar": prior_path.name,
            "current_sidecar": current_path.name,
            "prior_content_hash": prior["content_hash"],
            "current_content_hash": current["content_hash"],
        }
        report["spec_hash"] = current["spec_hash"]
        report["source_descriptor_ref"] = current["source_descriptor_ref"]
        report["survey_area_symbol"] = current["survey_area_symbol"]
        report["publication_date"] = current["publication_date"]
    if spatial_diff_path is not None:
        inputs = report["inputs"]
        assert isinstance(inputs, dict)
        inputs["spatial_diff"] = spatial_diff_path.name
        if spatial_diff is not None:
            inputs["spatial_diff_content_hash"] = spatial_diff["content_hash"]
    return report


def _input_error_report(
    prior_path: Path,
    current_path: Path,
    prior: LoadedSidecar,
    current: LoadedSidecar,
    spatial_diff_path: Path | None = None,
    spatial_diff: LoadedSpatialDiff | None = None,
) -> dict[str, object]:
    reason_codes = {f"PRIOR_{finding.code}" for finding in prior.findings}
    reason_codes.update(f"CURRENT_{finding.code}" for finding in current.findings)
    if spatial_diff is not None:
        reason_codes.update(
            finding.code
            if finding.code.startswith("SPATIAL_DIFF_")
            else f"SPATIAL_DIFF_{finding.code}"
            for finding in spatial_diff.findings
        )
    if not reason_codes:
        reason_codes.add("SIDECAR_LOAD_ERROR")
    return _report(
        prior_path=prior_path,
        current_path=current_path,
        outcome="ERROR",
        reason_codes=sorted(reason_codes),
        checks={
            "source_scope": "not_evaluated",
            "chronology": "not_evaluated",
            "materiality_profile": "not_evaluated",
            "package_metadata": "not_evaluated",
            "analysis_geometry": "not_evaluated",
            "geometry_profile": "not_evaluated",
            "attribute_schema": "not_evaluated",
            "table_content": "not_evaluated",
            "spatial_diff": "not_evaluated",
            "mapunit_area_drift": "not_evaluated",
        },
        prior=None,
        current=None,
        spatial_diff_path=spatial_diff_path,
        spatial_diff=None,
    )


def compare_sidecars(
    prior_path: Path | str,
    current_path: Path | str,
    spatial_diff_path: Path | str | None = None,
) -> dict[str, object]:
    prior_file = Path(prior_path)
    current_file = Path(current_path)
    spatial_file = Path(spatial_diff_path) if spatial_diff_path is not None else None
    prior_loaded = load_sidecar(prior_file)
    current_loaded = load_sidecar(current_file)
    spatial_loaded = (
        load_spatial_diff(spatial_file)
        if spatial_file is not None
        else LoadedSpatialDiff(None, ())
    )
    if prior_loaded.findings or current_loaded.findings or spatial_loaded.findings:
        return _input_error_report(
            prior_file,
            current_file,
            prior_loaded,
            current_loaded,
            spatial_file,
            spatial_loaded,
        )

    prior = prior_loaded.candidate
    current = current_loaded.candidate
    spatial_diff = spatial_loaded.candidate
    assert prior is not None and current is not None

    def report(outcome: str, reason_codes: Sequence[str]) -> dict[str, object]:
        return _report(
            prior_path=prior_file,
            current_path=current_file,
            outcome=outcome,
            reason_codes=reason_codes,
            checks=checks,
            prior=prior,
            current=current,
            spatial_diff_path=spatial_file,
            spatial_diff=spatial_diff,
        )

    prior_mapunits = prior["mapunit_areas_m2"]
    current_mapunits = current["mapunit_areas_m2"]
    prior_mapunit_geometry = prior["mapunit_geometry_hashes"]
    current_mapunit_geometry = current["mapunit_geometry_hashes"]
    prior_schema = prior["attribute_schema"]
    current_schema = current["attribute_schema"]
    prior_table_content = prior["table_content_hashes"]
    current_table_content = current["table_content_hashes"]
    assert isinstance(prior_mapunits, dict)
    assert isinstance(current_mapunits, dict)
    assert isinstance(prior_mapunit_geometry, dict)
    assert isinstance(current_mapunit_geometry, dict)
    assert isinstance(prior_schema, dict)
    assert isinstance(current_schema, dict)
    assert isinstance(prior_table_content, dict)
    assert isinstance(current_table_content, dict)

    schema_changed = _schema_signature(prior_schema) != _schema_signature(current_schema)
    mapunit_geometry_changed = prior_mapunit_geometry != current_mapunit_geometry
    area_distribution_changed = prior_mapunits != current_mapunits
    table_content_changed = prior_table_content != current_table_content
    derived_state_changed = any(
        (
            schema_changed,
            mapunit_geometry_changed,
            area_distribution_changed,
            table_content_changed,
        )
    )
    changed_schema_tables = sorted(
        table
        for table in set(prior_schema) | set(current_schema)
        if prior_schema.get(table) != current_schema.get(table)
    )
    changed_mapunit_geometries = sorted(
        mapunit_id
        for mapunit_id in set(prior_mapunit_geometry) | set(current_mapunit_geometry)
        if prior_mapunit_geometry.get(mapunit_id)
        != current_mapunit_geometry.get(mapunit_id)
    )
    changed_table_contents = sorted(
        table
        for table in set(prior_table_content) | set(current_table_content)
        if prior_table_content.get(table) != current_table_content.get(table)
    )

    checks: dict[str, object] = {
        "source_scope": "fixed_synthetic_profile",
        "chronology": "forward",
        "materiality_profile": (
            "same"
            if prior["materiality_profile"] == current["materiality_profile"]
            else "changed"
        ),
        "extraction_profile": (
            "same"
            if prior["extraction_profile_hash"] == current["extraction_profile_hash"]
            else "changed"
        ),
        "geometry_profile": (
            "same"
            if prior["geometry_profile_hash"] == current["geometry_profile_hash"]
            else "changed"
        ),
        "package_metadata": (
            "same"
            if all(
                prior[field] == current[field]
                for field in ("package_identifier", "publication_date", "package_sha256")
            )
            else "changed"
        ),
        "analysis_geometry": (
            "same"
            if prior["analysis_geometry_hash"] == current["analysis_geometry_hash"]
            and prior["analysis_area_m2"] == current["analysis_area_m2"]
            else "changed"
        ),
        "mapunit_geometry": "changed" if mapunit_geometry_changed else "same",
        "changed_mapunit_geometry_ids": changed_mapunit_geometries,
        "attribute_schema": "changed" if schema_changed else "same",
        "changed_attribute_tables": changed_schema_tables,
        "table_content": "changed" if table_content_changed else "same",
        "changed_table_content_ids": changed_table_contents,
        "spatial_diff": "provided" if spatial_diff is not None else "not_provided",
        "derived_state_consistency": "not_evaluated",
        "mapunit_area_drift": "not_evaluated",
    }

    stale_reasons: list[str] = []
    if current["observed_at"] < prior["observed_at"]:
        stale_reasons.append("OBSERVED_AT_REGRESSED")
    if current["publication_date"] < prior["publication_date"]:
        stale_reasons.append("PUBLICATION_DATE_REGRESSED")
    if stale_reasons:
        checks["chronology"] = "regressed"
        return report("STALE_INPUT", stale_reasons)

    if checks["materiality_profile"] == "changed":
        return report("ABSTAIN", ["MATERIALITY_PROFILE_DRIFT"])
    if checks["extraction_profile"] == "changed":
        return report("ABSTAIN", ["EXTRACTION_PROFILE_DRIFT"])
    if checks["geometry_profile"] == "changed":
        return report("ABSTAIN", ["GEOMETRY_PROFILE_DRIFT"])

    if prior["package_sha256"] == current["package_sha256"] and derived_state_changed:
        checks["derived_state_consistency"] = "invalid_same_package_changed_derivation"
        return report(
            "ERROR", ["DERIVED_STATE_CHANGED_WITHOUT_SOURCE_OR_PROFILE_CHANGE"]
        )
    checks["derived_state_consistency"] = "consistent"

    if checks["analysis_geometry"] == "changed":
        reasons: list[str] = []
        if prior["analysis_geometry_hash"] != current["analysis_geometry_hash"]:
            reasons.append("ANALYSIS_GEOMETRY_HASH_DRIFT_REQUIRES_REBASE")
        if prior["analysis_area_m2"] != current["analysis_area_m2"]:
            reasons.append("ANALYSIS_AREA_DRIFT_REQUIRES_REBASE")
        return report("GEOMETRY_DRIFT", reasons)

    analysis_area_m2 = current["analysis_area_m2"]
    profile = current["materiality_profile"]
    assert isinstance(analysis_area_m2, int)
    assert isinstance(profile, dict)
    threshold_ppm = profile["mapunit_area_change_ppm"]
    assert isinstance(threshold_ppm, int)

    l1_delta_m2 = 0
    for mapunit_id in sorted(set(prior_mapunits) | set(current_mapunits)):
        prior_area = prior_mapunits.get(mapunit_id, 0)
        current_area = current_mapunits.get(mapunit_id, 0)
        assert isinstance(prior_area, int) and isinstance(current_area, int)
        l1_delta_m2 += abs(current_area - prior_area)
    aggregate_lower_bound_m2 = l1_delta_m2 // 2

    label_disagreement_area_m2 = 0
    if mapunit_geometry_changed:
        if spatial_diff is None:
            checks["spatial_diff"] = "required_but_missing"
            return report(
                "GEOMETRY_DRIFT", ["MAPUNIT_GEOMETRY_DRIFT_REQUIRES_SPATIAL_DIFF"]
            )

        binding_reasons: list[str] = []
        if spatial_diff["prior_content_hash"] != prior["content_hash"]:
            binding_reasons.append("SPATIAL_DIFF_PRIOR_BINDING_MISMATCH")
        if spatial_diff["current_content_hash"] != current["content_hash"]:
            binding_reasons.append("SPATIAL_DIFF_CURRENT_BINDING_MISMATCH")
        if spatial_diff["prior_geometry_set_hash"] != compute_geometry_set_hash(prior):
            binding_reasons.append("SPATIAL_DIFF_PRIOR_GEOMETRY_BINDING_MISMATCH")
        if spatial_diff["current_geometry_set_hash"] != compute_geometry_set_hash(current):
            binding_reasons.append("SPATIAL_DIFF_CURRENT_GEOMETRY_BINDING_MISMATCH")
        if spatial_diff["geometry_profile_hash"] != prior["geometry_profile_hash"]:
            binding_reasons.append("SPATIAL_DIFF_GEOMETRY_PROFILE_BINDING_MISMATCH")
        if binding_reasons:
            checks["spatial_diff"] = "binding_invalid"
            return report("ERROR", binding_reasons)

        changed_area = spatial_diff["changed_label_area_m2"]
        assert isinstance(changed_area, int)
        if changed_area < aggregate_lower_bound_m2 or changed_area > analysis_area_m2:
            checks["spatial_diff"] = "area_bounds_invalid"
            return report("ERROR", ["SPATIAL_DIFF_AREA_INCONSISTENT"])
        label_disagreement_area_m2 = changed_area
        checks["spatial_diff"] = "bound_and_valid"
        checks["spatial_diff_content_hash"] = spatial_diff["content_hash"]
        checks["spatial_diff_method"] = spatial_diff["method"]
        checks["spatial_diff_crs"] = spatial_diff["crs"]
        checks["spatial_diff_area_unit"] = spatial_diff["area_unit"]
    else:
        if spatial_diff is not None:
            checks["spatial_diff"] = "unexpected_without_geometry_drift"
            return report("ERROR", ["SPATIAL_DIFF_WITHOUT_GEOMETRY_DRIFT"])
        if area_distribution_changed:
            checks["spatial_diff"] = "area_changed_without_geometry_drift"
            return report("ERROR", ["MAPUNIT_AREA_CHANGED_WITHOUT_GEOMETRY_DRIFT"])
        checks["spatial_diff"] = "not_required"

    threshold_crossed = (
        label_disagreement_area_m2 * PPM_DENOMINATOR
        > analysis_area_m2 * threshold_ppm
    )
    if label_disagreement_area_m2 == 0:
        checks["mapunit_area_drift"] = "same"
    elif threshold_crossed:
        checks["mapunit_area_drift"] = "material"
    else:
        checks["mapunit_area_drift"] = "at_or_below_threshold"
    checks["mapunit_label_disagreement_area_m2"] = label_disagreement_area_m2
    checks["aggregate_area_change_lower_bound_m2"] = aggregate_lower_bound_m2
    checks["mapunit_change_ppm_floor"] = (
        label_disagreement_area_m2 * PPM_DENOMINATOR // analysis_area_m2
    )
    checks["mapunit_threshold_ppm"] = threshold_ppm
    checks["materiality_comparison"] = "strictly_greater_than"

    reasons: list[str] = []
    if schema_changed:
        reasons.append("ATTRIBUTE_SCHEMA_DRIFT_REQUIRES_REVIEW")
    if table_content_changed:
        reasons.append("TABLE_CONTENT_DRIFT_REQUIRES_REVIEW")
    if threshold_crossed:
        reasons.append("MAPUNIT_AREA_CHANGE_THRESHOLD_EXCEEDED")
    if reasons:
        return report("PROPOSED_WORK_RECORD", reasons)

    if checks["package_metadata"] == "changed":
        reasons.append("SOURCE_METADATA_DRIFT_BELOW_MATERIALITY")
    if label_disagreement_area_m2 > 0:
        reasons.append("MAPUNIT_AREA_DRIFT_AT_OR_BELOW_THRESHOLD")
    return report("NO_MATERIAL_CHANGE", reasons)


def serialize_report(report: Mapping[str, object]) -> str:
    return json.dumps(report, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def _resolved_output_path(path: Path) -> Path:
    if path.name in {"", ".", ".."}:
        raise OSError("report output filename is invalid")
    candidate = path if path.is_absolute() else Path.cwd() / path
    try:
        resolved_parent = candidate.parent.resolve(strict=True)
        resolved_repo = REPO_ROOT.resolve(strict=True)
    except OSError as error:
        raise OSError("report output parent could not be resolved safely") from error
    if not resolved_parent.is_dir():
        raise OSError("report output parent must be an existing directory")

    resolved_candidate = resolved_parent / candidate.name
    try:
        resolved_candidate.relative_to(resolved_repo)
    except ValueError:
        return resolved_candidate
    raise OSError("report output inside the repository is denied")


def write_report(path: Path, serialized: str) -> None:
    output_path = _resolved_output_path(path)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    for flag_name in ("O_BINARY", "O_CLOEXEC", "O_NOFOLLOW"):
        flags |= getattr(os, flag_name, 0)
    descriptor = os.open(output_path, flags, stat.S_IRUSR | stat.S_IWUSR)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            descriptor = -1
            stream.write((serialized + "\n").encode("utf-8"))
            stream.flush()
            os.fsync(stream.fileno())
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compare two frozen synthetic SSURGO sidecars and emit a review-only drift report."
        )
    )
    parser.add_argument("--prior", required=True, type=Path)
    parser.add_argument("--current", required=True, type=Path)
    parser.add_argument(
        "--spatial-diff",
        type=Path,
        help=(
            "separate fixture-only mapunit-partition disagreement artifact; required "
            "when mapunit geometry fingerprints change"
        ),
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        required=True,
        help="acknowledge that this helper cannot fetch, promote, or publish",
    )
    args = parser.parse_args(argv)

    report = compare_sidecars(args.prior, args.current, args.spatial_diff)
    serialized = serialize_report(report)
    if args.output is None:
        print(serialized)
    else:
        try:
            write_report(args.output, serialized)
        except OSError:
            print("report output could not be created safely", file=sys.stderr)
            return 2

    decision = report.get("decision")
    outcome = decision.get("outcome") if isinstance(decision, dict) else "ERROR"
    return 0 if outcome in SAFE_EXIT_OUTCOMES else 1


if __name__ == "__main__":
    raise SystemExit(main())
