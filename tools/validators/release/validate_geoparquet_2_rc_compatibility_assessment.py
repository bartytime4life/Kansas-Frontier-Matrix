#!/usr/bin/env python3
"""Validate the inactive GeoParquet 2.0 RC declared compatibility packet."""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/geoparquet_2_rc_compatibility_assessment.schema.json"
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/release/geoparquet_2_rc_compatibility_assessment/cases.json"
PROFILE = "kfm.geoparquet-2-rc-compatibility-assessment.v1"
CANDIDATE_VERSION = "2.0.0-rc.1"
DECLARED_DEFAULT = "1.1.0"
UPSTREAM_COMMIT = "0c7fab74cf1177e2fe61df8eb7fcd1813b73e4aa"
SCOPE = "declared-synthetic-readiness-for-byte-probes"
STATUS_KEYS = {
    "native_geometry_write",
    "native_geometry_read",
    "workflow_round_trip",
    "native_type_inspection",
    "crs_round_trip",
    "row_group_spatial_statistics",
    "row_group_spatial_pruning",
    "legacy_1_1_read",
    "unknown_metadata_preservation",
}
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
        "REQUIRED_ENGINE_MATRIX_INCOMPLETE",
        "GOVERNANCE_BOUNDARY_VIOLATION",
        "SCHEMA_INVALID",
        "DECLARED_OUTCOME_MISMATCH",
    }
)


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


def _engine_reasons(engine_checks: Mapping[str, Any]) -> list[str]:
    reasons: list[str] = []
    if set(engine_checks) != {"GDAL", "DUCKDB", "SEDONA"}:
        return ["REQUIRED_ENGINE_MATRIX_INCOMPLETE"]
    for engine in engine_checks.values():
        if not isinstance(engine, Mapping):
            return ["REQUIRED_ENGINE_MATRIX_INCOMPLETE"]
        if engine.get("pinned") is not True:
            reasons.append("TOOL_VERSION_NOT_PINNED")
        behavior = engine.get("unsupported_assumption_behavior")
        if behavior != "REJECT":
            reasons.append("UNSUPPORTED_ASSUMPTION_NOT_FAIL_CLOSED")
        for key, value in engine.items():
            if key not in STATUS_KEYS:
                continue
            if value == "FAIL":
                reasons.append("BYTE_PROBE_FAILED")
            elif value == "NOT_RUN":
                reasons.append("BYTE_PROBES_PENDING")
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

    reasons.extend(_engine_reasons(candidate["engine_checks"]))
    governance = candidate["governance"]
    if any(value is not False for value in governance.values()):
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


def validate_cases() -> int:
    try:
        value = _load_json(CASES_PATH)
    except (OSError, UnicodeError, json.JSONDecodeError):
        print(json.dumps({"outcome": "ERROR", "reason_codes": ["CASES_UNAVAILABLE"]}, sort_keys=True))
        return 1
    cases = value.get("cases") if isinstance(value, Mapping) else None
    if not isinstance(cases, list) or not cases:
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
        actual = assess(case.get("candidate"))
        expected = case.get("expected")
        comparable = {"outcome": actual.outcome, "reason_codes": list(actual.reason_codes)}
        if comparable != expected:
            failed = True
            print(json.dumps({"case_id": case_id, "actual": comparable, "expected": expected}, sort_keys=True))
        else:
            print(json.dumps({"case_id": case_id, **comparable}, sort_keys=True))
    if failed:
        return 1
    print(f"CONFIRMED: {len(seen)} GeoParquet 2.0 RC assessment cases passed exact polarity.")
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
