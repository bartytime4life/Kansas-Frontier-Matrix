#!/usr/bin/env python3
"""Validate the inactive GeoParquet 2.0 RC exact-toolchain declaration packet."""
from __future__ import annotations

import argparse
import copy
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/geoparquet_2_rc_compatibility_assessment.schema.json"
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/release/geoparquet_2_rc_compatibility_assessment/cases.json"
PROFILE = "kfm.geoparquet-2-rc-compatibility-assessment.v2"
CANDIDATE_VERSION = "2.0.0-rc.1"
DECLARED_DEFAULT = "1.1.0"
UPSTREAM_COMMIT = "0c7fab74cf1177e2fe61df8eb7fcd1813b73e4aa"
SCOPE = "exact-toolchain-declaration-ready-for-byte-probes"
EXPECTED_TOOLCHAINS: Mapping[str, Mapping[str, str]] = {
    "GDAL": {
        "tool_version": "3.13.2",
        "source_ref": "upstream:OSGeo/gdal@b40672525acf3f5c4f29d8541aa7dcff1e18eb92",
    },
    "DUCKDB": {
        "tool_version": "1.5.5",
        "source_ref": "upstream:duckdb/duckdb@d8cdaa33fda8df955cc76ef58a280f68f4cd43fa",
        "extension_version": "spatial@1.5.5",
    },
    "SEDONA_SPARK": {
        "tool_version": "1.9.0",
        "source_ref": "upstream:apache/sedona@34098262086a6137d105cd8d9e0b366e4a8246c0",
        "spark_version": "3.5.9",
        "spark_source_ref": "upstream:apache/spark@7c14a3c28b141cc97a330c4d0f5d2a6da7267f85",
        "java_major": "11",
        "scala_version": "2.12.18",
        "parquet_java_version": "1.13.1",
    },
    "SEDONA_DB": {
        "tool_version": "0.4.0",
        "source_ref": "upstream:apache/sedona:sedonadb-0.4.0-release",
    },
}
EXPECTED_INSPECTOR: Mapping[str, str] = {
    "tool_name": "PYARROW",
    "tool_version": "25.0.0",
    "source_ref": "upstream:apache/arrow@apache-arrow-25.0.0",
}
STATUS_KEYS = frozenset(
    {
        "native_geometry_write",
        "native_geography_write",
        "native_geometry_read",
        "workflow_round_trip",
        "native_type_inspection",
        "logical_type_footer_inspection",
        "crs_round_trip",
        "row_group_spatial_statistics",
        "row_group_statistics_inspection",
        "row_group_spatial_pruning",
        "legacy_1_1_read",
        "unknown_metadata_preservation",
    }
)
ERROR_CODES = frozenset(
    {
        "PROFILE_INVALID",
        "CANDIDATE_VERSION_MISMATCH",
        "RELEASE_CANDIDATE_STATUS_REQUIRED",
        "DECLARED_DEFAULT_CHANGED",
        "UPSTREAM_COMMIT_MISMATCH",
        "NATIVE_LOGICAL_TYPE_REQUIRED",
        "WKB_BYTE_ARRAY_REQUIRED",
        "ROOT_GEOMETRY_REQUIRED",
        "PARQUET_CRS_AUTHORITY_REQUIRED",
        "GEOPARQUET_INLINE_PROJJSON_REQUIRED",
        "GEOPARQUET_CRS_EQUIVALENCE_REQUIRED",
        "PARQUET_NATIVE_SPATIAL_STATISTICS_REQUIRED",
        "GEOPARQUET_1X_COVERING_ASSUMPTION_CONFLICT",
        "LEGACY_1_1_FIXTURES_REQUIRED",
        "REQUIRED_TOOLCHAIN_MATRIX_INCOMPLETE",
        "TOOLCHAIN_VERSION_MISMATCH",
        "TOOLCHAIN_SOURCE_BINDING_MISMATCH",
        "TOOLCHAIN_TRANSITIVE_PIN_MISMATCH",
        "TOOL_ARTIFACT_DIGEST_INVALID",
        "INSPECTOR_PIN_MISMATCH",
        "EVIDENCE_REF_REUSED",
        "GOVERNANCE_BOUNDARY_VIOLATION",
        "SCHEMA_INVALID",
        "DECLARED_OUTCOME_MISMATCH",
    }
)
SHA256_RE = re.compile(r"^sha256:([0-9a-f]{64})$")


@dataclass(frozen=True)
class Assessment:
    outcome: str
    reason_codes: tuple[str, ...]

    def as_dict(self) -> dict[str, object]:
        return {
            "outcome": self.outcome,
            "reason_codes": list(self.reason_codes),
            "scope": SCOPE,
        }


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _schema_validator() -> Draft202012Validator:
    schema = _load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def _schema_valid(candidate: Any) -> bool:
    try:
        return not list(_schema_validator().iter_errors(candidate))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return False


def _digest_valid(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    match = SHA256_RE.fullmatch(value)
    if match is None:
        return False
    digest = match.group(1)
    return digest != "0" * 64 and len(set(digest)) >= 4


def _status_reasons(value: Mapping[str, Any]) -> list[str]:
    reasons: list[str] = []
    for key, status in value.items():
        if key not in STATUS_KEYS:
            continue
        if status == "FAIL":
            reasons.append("BYTE_PROBE_FAILED")
        elif status == "NOT_RUN":
            reasons.append("BYTE_PROBES_PENDING")
    return reasons


def _toolchain_reasons(matrix: Mapping[str, Any], inspector: Mapping[str, Any]) -> list[str]:
    reasons: list[str] = []
    if set(matrix) != set(EXPECTED_TOOLCHAINS):
        return ["REQUIRED_TOOLCHAIN_MATRIX_INCOMPLETE"]

    evidence_refs: list[str] = []
    for lane_name, expected in EXPECTED_TOOLCHAINS.items():
        lane = matrix.get(lane_name)
        if not isinstance(lane, Mapping):
            return ["REQUIRED_TOOLCHAIN_MATRIX_INCOMPLETE"]
        if lane.get("pinned") is not True:
            reasons.append("TOOL_VERSION_NOT_PINNED")
        if lane.get("tool_version") != expected["tool_version"]:
            reasons.append("TOOLCHAIN_VERSION_MISMATCH")
        if lane.get("source_ref") != expected["source_ref"]:
            reasons.append("TOOLCHAIN_SOURCE_BINDING_MISMATCH")
        if not _digest_valid(lane.get("artifact_digest")):
            reasons.append("TOOL_ARTIFACT_DIGEST_INVALID")
        if lane.get("unsupported_assumption_behavior") != "REJECT":
            reasons.append("UNSUPPORTED_ASSUMPTION_NOT_FAIL_CLOSED")
        evidence_ref = lane.get("evidence_ref")
        if isinstance(evidence_ref, str):
            evidence_refs.append(evidence_ref)
        reasons.extend(_status_reasons(lane))

    duckdb = matrix["DUCKDB"]
    if duckdb.get("extension_version") != EXPECTED_TOOLCHAINS["DUCKDB"]["extension_version"]:
        reasons.append("TOOLCHAIN_TRANSITIVE_PIN_MISMATCH")
    if not _digest_valid(duckdb.get("extension_digest")):
        reasons.append("TOOL_ARTIFACT_DIGEST_INVALID")

    sedona_spark = matrix["SEDONA_SPARK"]
    for key in (
        "spark_version",
        "spark_source_ref",
        "java_major",
        "scala_version",
        "parquet_java_version",
    ):
        if sedona_spark.get(key) != EXPECTED_TOOLCHAINS["SEDONA_SPARK"][key]:
            reasons.append("TOOLCHAIN_TRANSITIVE_PIN_MISMATCH")
    if not _digest_valid(sedona_spark.get("spark_distribution_digest")):
        reasons.append("TOOL_ARTIFACT_DIGEST_INVALID")

    if inspector.get("pinned") is not True:
        reasons.append("TOOL_VERSION_NOT_PINNED")
    if any(inspector.get(key) != value for key, value in EXPECTED_INSPECTOR.items()):
        reasons.append("INSPECTOR_PIN_MISMATCH")
    if not _digest_valid(inspector.get("artifact_digest")):
        reasons.append("TOOL_ARTIFACT_DIGEST_INVALID")
    inspector_ref = inspector.get("evidence_ref")
    if isinstance(inspector_ref, str):
        evidence_refs.append(inspector_ref)
    reasons.extend(_status_reasons(inspector))

    if len(evidence_refs) != len(set(evidence_refs)):
        reasons.append("EVIDENCE_REF_REUSED")
    return reasons


def assess(candidate: Any) -> Assessment:
    if not isinstance(candidate, Mapping) or not _schema_valid(candidate):
        return Assessment("ERROR", ("SCHEMA_INVALID",))

    reasons: list[str] = []
    if candidate["profile"] != PROFILE:
        reasons.append("PROFILE_INVALID")
    if candidate["candidate_version"] != CANDIDATE_VERSION:
        reasons.append("CANDIDATE_VERSION_MISMATCH")
    if candidate["release_kind"] != "RELEASE_CANDIDATE":
        reasons.append("RELEASE_CANDIDATE_STATUS_REQUIRED")
    if candidate["declared_default"] != DECLARED_DEFAULT:
        reasons.append("DECLARED_DEFAULT_CHANGED")
    if candidate["upstream_commit"] != UPSTREAM_COMMIT:
        reasons.append("UPSTREAM_COMMIT_MISMATCH")

    fmt = candidate["format_expectations"]
    if fmt["logical_type"] not in {"GEOMETRY", "GEOGRAPHY"}:
        reasons.append("NATIVE_LOGICAL_TYPE_REQUIRED")
    if fmt["physical_type"] != "BYTE_ARRAY" or fmt["encoding"] != "WKB":
        reasons.append("WKB_BYTE_ARRAY_REQUIRED")
    if fmt["root_geometry"] is not True:
        reasons.append("ROOT_GEOMETRY_REQUIRED")
    if fmt["parquet_crs_source_of_truth"] is not True:
        reasons.append("PARQUET_CRS_AUTHORITY_REQUIRED")
    if fmt["geo_metadata_crs_inline_projjson"] is not True:
        reasons.append("GEOPARQUET_INLINE_PROJJSON_REQUIRED")
    if fmt["crs_semantically_equivalent"] is not True:
        reasons.append("GEOPARQUET_CRS_EQUIVALENCE_REQUIRED")
    if fmt["parquet_native_spatial_statistics"] is not True:
        reasons.append("PARQUET_NATIVE_SPATIAL_STATISTICS_REQUIRED")
    if fmt["covering_bbox_column_required"] is not False:
        reasons.append("GEOPARQUET_1X_COVERING_ASSUMPTION_CONFLICT")
    if fmt["legacy_1_1_fixtures_preserved"] is not True:
        reasons.append("LEGACY_1_1_FIXTURES_REQUIRED")

    reasons.extend(_toolchain_reasons(candidate["toolchain_matrix"], candidate["inspector"]))
    if any(value is not False for value in candidate["governance"].values()):
        reasons.append("GOVERNANCE_BOUNDARY_VIOLATION")

    reasons = sorted(set(reasons))
    if any(reason in ERROR_CODES for reason in reasons):
        outcome = "ERROR"
    elif reasons:
        outcome = "HOLD"
    else:
        outcome = "READY"

    if candidate["outcome"] != outcome:
        reasons = sorted(set([*reasons, "DECLARED_OUTCOME_MISMATCH"]))
        outcome = "ERROR"
    return Assessment(outcome, tuple(reasons))


def _deep_update(target: dict[str, Any], overrides: Mapping[str, Any]) -> None:
    for key, value in overrides.items():
        current = target.get(key)
        if isinstance(current, dict) and isinstance(value, Mapping):
            _deep_update(current, value)
        else:
            target[key] = copy.deepcopy(value)


def candidate_from_case(base_candidate: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(dict(base_candidate))
    all_status = case.get("all_probe_status")
    if all_status is not None:
        for lane in candidate.get("toolchain_matrix", {}).values():
            if isinstance(lane, dict):
                for key in list(lane):
                    if key in STATUS_KEYS:
                        lane[key] = all_status
        inspector = candidate.get("inspector")
        if isinstance(inspector, dict):
            for key in list(inspector):
                if key in STATUS_KEYS:
                    inspector[key] = all_status
    overrides = case.get("overrides", {})
    if isinstance(overrides, Mapping):
        _deep_update(candidate, overrides)
    return candidate


def validate_cases() -> int:
    try:
        value = _load_json(CASES_PATH)
    except (OSError, UnicodeError, json.JSONDecodeError):
        print(json.dumps({"outcome": "ERROR", "reason_codes": ["CASES_UNAVAILABLE"]}, sort_keys=True))
        return 1
    base_candidate = value.get("base_candidate") if isinstance(value, Mapping) else None
    cases = value.get("cases") if isinstance(value, Mapping) else None
    if not isinstance(base_candidate, Mapping) or not isinstance(cases, list) or not cases:
        print(json.dumps({"outcome": "ERROR", "reason_codes": ["CASES_INVALID"]}, sort_keys=True))
        return 1
    failed = False
    seen: set[str] = set()
    for case in cases:
        if not isinstance(case, Mapping) or not isinstance(case.get("case_id"), str):
            failed = True
            continue
        case_id = case["case_id"]
        if case_id in seen:
            failed = True
        seen.add(case_id)
        actual = assess(candidate_from_case(base_candidate, case))
        expected = case.get("expected")
        comparable = {"outcome": actual.outcome, "reason_codes": list(actual.reason_codes)}
        if comparable != expected:
            failed = True
            print(json.dumps({"case_id": case_id, "actual": comparable, "expected": expected}, sort_keys=True))
        else:
            print(json.dumps({"case_id": case_id, **comparable}, sort_keys=True))
    if failed:
        return 1
    print(f"CONFIRMED: {len(seen)} GeoParquet 2.0 RC exact-toolchain cases passed exact polarity.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--cases", action="store_true")
    args = parser.parse_args(argv)
    if args.cases:
        if args.files:
            parser.error("--cases cannot be combined with files")
        return validate_cases()
    if not args.files:
        parser.error("provide one or more files or use --cases")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        try:
            candidate = _load_json(path)
            result = assess(candidate)
        except (OSError, UnicodeError, json.JSONDecodeError):
            result = Assessment("ERROR", ("INPUT_UNAVAILABLE",))
        print(json.dumps({"file": path.name, **result.as_dict()}, sort_keys=True))
        failed = failed or result.outcome != "READY"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
