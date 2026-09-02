#!/usr/bin/env python3
"""Fixture-first KFM geospatial carrier readiness preflight.

The validator inspects declared metadata only. It performs no network access,
no binary parsing, no release mutation, and grants no authority.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/geospatial_carrier_readiness.schema.json"
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/release/geospatial_carrier_readiness/cases.json"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 50
SCOPE = "geospatial-carrier-readiness-metadata-only"
ZERO_SHA256 = "sha256:" + "0" * 64


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True)
class Assessment:
    outcome: str
    reason_codes: tuple[str, ...]
    advisories: tuple[str, ...]

    def as_dict(self) -> dict[str, object]:
        return {
            "outcome": self.outcome,
            "reason_codes": list(self.reason_codes),
            "advisories": list(self.advisories),
            "scope": SCOPE,
        }


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _load_json(path: Path) -> tuple[Any | None, str | None]:
    try:
        if path.is_symlink():
            return None, "INPUT_SYMLINK_DENIED"
        if not path.is_file():
            return None, "FILE_NOT_FOUND"
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, "FILE_TOO_LARGE"
        with path.open("r", encoding="utf-8") as stream:
            return json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_nonfinite,
                parse_float=_finite_float,
            ), None
    except UnicodeDecodeError:
        return None, "JSON_NOT_UTF8"
    except DuplicateKeyError:
        return None, "JSON_DUPLICATE_KEY"
    except NonFiniteNumberError:
        return None, "JSON_NONFINITE_NUMBER"
    except json.JSONDecodeError:
        return None, "JSON_INVALID"
    except OSError:
        return None, "FILE_READ_ERROR"
    except (RecursionError, ValueError):
        return None, "JSON_COMPLEXITY_LIMIT"


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def _schema_errors(candidate: Mapping[str, Any]) -> tuple[str, ...]:
    try:
        errors = list(islice(_schema_validator().iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return ("SCHEMA_UNAVAILABLE",)
    if errors:
        return ("SCHEMA_INVALID",)
    return ()


def _sorted_unique_strings(value: Any) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _power_of_two(value: int) -> bool:
    return value > 0 and value & (value - 1) == 0


def _common(candidate: Mapping[str, Any]) -> tuple[list[str], list[str]]:
    reasons: list[str] = []
    advisories: list[str] = []
    artifact = candidate.get("artifact")
    if isinstance(artifact, Mapping):
        if artifact.get("digest") == ZERO_SHA256:
            reasons.append("ARTIFACT_DIGEST_PLACEHOLDER_DENIED")
        if artifact.get("immutable") is False:
            reasons.append("ARTIFACT_NOT_IMMUTABLE")
    return reasons, advisories


def _cog(candidate: Mapping[str, Any]) -> tuple[list[str], list[str]]:
    reasons, advisories = _common(candidate)
    artifact = candidate["artifact"]
    carrier = candidate["carrier"]
    name = str(artifact["file_name"]).lower()
    if not name.endswith((".tif", ".tiff")):
        reasons.append("COG_EXTENSION_REQUIRED")
    if artifact["media_type"] != "image/tiff":
        reasons.append("COG_MEDIA_TYPE_UNEXPECTED")
    if not carrier["internal_tiling"]:
        reasons.append("COG_INTERNAL_TILING_REQUIRED")
    if not (
        carrier["block_width"] == carrier["block_height"]
        and _power_of_two(carrier["block_width"])
        and 128 <= carrier["block_width"] <= 1024
    ):
        reasons.append("COG_BLOCK_LAYOUT_NONSTANDARD")
    if max(carrier["width"], carrier["height"]) > 512 and carrier["overview_count"] < 1:
        reasons.append("COG_OVERVIEWS_REQUIRED")
    if not carrier["range_read_supported"]:
        reasons.append("COG_RANGE_READ_REQUIRED")
    extensions = carrier["stac_extensions"]
    if not _sorted_unique_strings(extensions):
        reasons.append("NON_CANONICAL_ARRAY")
    elif not {"projection", "raster"}.issubset(set(extensions)):
        reasons.append("COG_STAC_EXTENSIONS_INCOMPLETE")
    return reasons, advisories


def _mvt(candidate: Mapping[str, Any]) -> tuple[list[str], list[str]]:
    reasons, advisories = _common(candidate)
    artifact = candidate["artifact"]
    carrier = candidate["carrier"]
    canonical_arrays = (
        carrier["style_source_layers"],
        carrier["attribute_whitelist"],
        carrier["encoded_attributes"],
        carrier["sensitive_attributes"],
    )
    if not all(_sorted_unique_strings(value) for value in canonical_arrays):
        reasons.append("NON_CANONICAL_ARRAY")
    if not str(carrier["mvt_version"]).startswith("2."):
        reasons.append("MVT_VERSION_UNSUPPORTED")
    if carrier["extent"] != 4096:
        reasons.append("MVT_EXTENT_NONSTANDARD")
    if carrier["tile_scheme"] != "XYZ":
        reasons.append("MVT_XYZ_REQUIRED")
    source_layer = carrier["source_layer"]
    if carrier["manifest_source_layer"] != source_layer or any(
        value != source_layer for value in carrier["style_source_layers"]
    ):
        reasons.append("MVT_SOURCE_LAYER_CONTRACT_MISMATCH")
    if not carrier["stable_feature_ids"]:
        reasons.append("MVT_STABLE_FEATURE_IDS_REQUIRED")
    if not carrier["source_ref_attribute"]:
        reasons.append("MVT_SOURCE_REF_REQUIRED")
    whitelist = set(carrier["attribute_whitelist"])
    encoded = set(carrier["encoded_attributes"])
    if not encoded.issubset(whitelist):
        reasons.append("MVT_ATTRIBUTE_WHITELIST_VIOLATION")
    if carrier["sensitive_attributes"]:
        reasons.append("MVT_SENSITIVE_ATTRIBUTE_EXPOSURE")
    if carrier["max_tile_bytes"] > 65536:
        reasons.append("MVT_TILE_BUDGET_EXCEEDED")
    if carrier["geometry_drop_count"] != 0:
        reasons.append("MVT_GEOMETRY_DROP_DENIED")
    if carrier["area_drift_pct"] > carrier["area_drift_limit_pct"]:
        reasons.append("MVT_AREA_DRIFT_EXCEEDED")
    if carrier["tiler_parameters_hash"] == ZERO_SHA256:
        reasons.append("MVT_TILER_PARAMETERS_PLACEHOLDER_DENIED")
    if carrier["container_kind"] == "PMTILES":
        if artifact["media_type"] != "application/vnd.pmtiles":
            reasons.append("MVT_PMTILES_MEDIA_TYPE_REQUIRED")
        if not str(artifact["file_name"]).lower().endswith(".pmtiles"):
            reasons.append("MVT_PMTILES_EXTENSION_REQUIRED")
        if not carrier["range_read_supported"]:
            reasons.append("MVT_RANGE_READ_REQUIRED")
    else:
        reasons.append("MVT_PUBLIC_CONTAINER_NOT_DEFAULT")
        if artifact["media_type"] not in {
            "application/vnd.mapbox-vector-tile",
            "application/x-protobuf",
        }:
            reasons.append("MVT_MEDIA_TYPE_UNEXPECTED")
    return reasons, advisories


def _geoparquet(candidate: Mapping[str, Any]) -> tuple[list[str], list[str]]:
    reasons, advisories = _common(candidate)
    artifact = candidate["artifact"]
    carrier = candidate["carrier"]
    layout = carrier["layout_profile"]
    if artifact["media_type"] != "application/vnd.apache.parquet":
        reasons.append("GEOPARQUET_MEDIA_TYPE_REQUIRED")
    if not str(artifact["file_name"]).lower().endswith(".parquet"):
        reasons.append("GEOPARQUET_EXTENSION_REQUIRED")
    if carrier["format_version"] != "1.1.0":
        reasons.append("GEOPARQUET_VERSION_NOT_ADOPTED")
    if not carrier["root_geometry_column"]:
        reasons.append("GEOPARQUET_ROOT_GEOMETRY_REQUIRED")
    if carrier["encoding"] != "WKB":
        reasons.append("GEOPARQUET_WKB_REQUIRED")
    if not carrier["explicit_crs"] or carrier["crs_format"] != "PROJJSON":
        reasons.append("GEOPARQUET_EXPLICIT_PROJJSON_CRS_REQUIRED")
    if not _sorted_unique_strings(carrier["geometry_types"]):
        reasons.append("NON_CANONICAL_ARRAY")
    if not carrier["stable_row_grouping"]:
        reasons.append("GEOPARQUET_STABLE_ROW_GROUPING_REQUIRED")
    if not carrier["deterministic_ordering"]:
        reasons.append("GEOPARQUET_DETERMINISTIC_ORDERING_REQUIRED")
    if layout["compression"] != "ZSTD":
        advisories.append("GEOPARQUET_ZSTD_RECOMMENDED")
    if layout["ordering_parameters_digest"] == ZERO_SHA256:
        reasons.append("GEOPARQUET_ORDERING_PARAMETERS_PLACEHOLDER_DENIED")
    if layout["partition_parameters_digest"] == ZERO_SHA256:
        reasons.append("GEOPARQUET_PARTITION_PARAMETERS_PLACEHOLDER_DENIED")
    if layout["writer_parameters_digest"] == ZERO_SHA256:
        reasons.append("GEOPARQUET_WRITER_PARAMETERS_PLACEHOLDER_DENIED")
    if layout["benchmark_digest"] == ZERO_SHA256:
        reasons.append("GEOPARQUET_BENCHMARK_DIGEST_PLACEHOLDER_DENIED")
    if layout["partition_strategy"] == "NONE" and layout["partition_version"] is not None:
        reasons.append("GEOPARQUET_PARTITION_VERSION_UNEXPECTED")
    if layout["partition_strategy"] != "NONE" and layout["partition_version"] is None:
        reasons.append("GEOPARQUET_PARTITION_VERSION_REQUIRED")
    if carrier["null_policy"] != "NULL_ONLY":
        reasons.append("GEOPARQUET_NULL_POLICY_VIOLATION")
    if not carrier["unknown_metadata_preserved"]:
        reasons.append("GEOPARQUET_FORWARD_COMPATIBILITY_REQUIRED")
    if not carrier["numeric_unit_coverage"]:
        reasons.append("GEOPARQUET_NUMERIC_UNIT_COVERAGE_REQUIRED")
    if not carrier["bbox_covering"]:
        advisories.append("GEOPARQUET_BBOX_COVERING_RECOMMENDED")
    return reasons, advisories


ERROR_CODES = frozenset(
    {
        "ARTIFACT_DIGEST_PLACEHOLDER_DENIED",
        "MVT_ATTRIBUTE_WHITELIST_VIOLATION",
        "MVT_SENSITIVE_ATTRIBUTE_EXPOSURE",
        "MVT_GEOMETRY_DROP_DENIED",
        "MVT_AREA_DRIFT_EXCEEDED",
        "MVT_TILER_PARAMETERS_PLACEHOLDER_DENIED",
        "GEOPARQUET_NULL_POLICY_VIOLATION",
        "GEOPARQUET_ORDERING_PARAMETERS_PLACEHOLDER_DENIED",
        "GEOPARQUET_PARTITION_PARAMETERS_PLACEHOLDER_DENIED",
        "GEOPARQUET_WRITER_PARAMETERS_PLACEHOLDER_DENIED",
        "GEOPARQUET_BENCHMARK_DIGEST_PLACEHOLDER_DENIED",
        "NON_CANONICAL_ARRAY",
        "SCHEMA_INVALID",
        "SCHEMA_UNAVAILABLE",
    }
)


def assess(candidate: Any) -> Assessment:
    if not isinstance(candidate, Mapping):
        return Assessment("ERROR", ("ROOT_NOT_OBJECT",), ())
    schema_errors = _schema_errors(candidate)
    if schema_errors:
        return Assessment("ERROR", tuple(sorted(schema_errors)), ())
    kind = candidate["carrier_kind"]
    if kind == "COG":
        reasons, advisories = _cog(candidate)
    elif kind == "MVT":
        reasons, advisories = _mvt(candidate)
    else:
        reasons, advisories = _geoparquet(candidate)
    reasons = sorted(set(reasons))
    advisories = sorted(set(advisories))
    if any(code in ERROR_CODES for code in reasons):
        outcome = "ERROR"
    elif reasons:
        outcome = "HOLD"
    else:
        outcome = "READY"
    return Assessment(outcome, tuple(reasons), tuple(advisories))


def validate_cases() -> int:
    value, error = _load_json(CASES_PATH)
    if error or not isinstance(value, Mapping) or not isinstance(value.get("cases"), list):
        print(json.dumps({"outcome": "ERROR", "reason_codes": [error or "CASES_INVALID"]}, sort_keys=True))
        return 1
    failed = False
    seen: set[str] = set()
    for case in value["cases"]:
        if not isinstance(case, Mapping) or not isinstance(case.get("case_id"), str):
            failed = True
            continue
        case_id = case["case_id"]
        if case_id in seen:
            failed = True
        seen.add(case_id)
        result = assess(case.get("candidate"))
        expected = case.get("expected")
        actual = result.as_dict()
        actual.pop("scope", None)
        if not isinstance(expected, Mapping) or actual != dict(expected):
            failed = True
            print(json.dumps({"case_id": case_id, "outcome": "CASE_MISMATCH", "actual": actual, "expected": expected}, sort_keys=True))
        else:
            print(json.dumps({"case_id": case_id, **actual}, sort_keys=True))
    if failed or not seen:
        return 1
    print(f"CONFIRMED: {len(seen)} geospatial carrier readiness cases passed exact polarity.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate inactive KFM geospatial carrier readiness metadata.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--cases", action="store_true")
    args = parser.parse_args(argv)
    if args.cases:
        if args.files:
            parser.error("--cases cannot be combined with explicit files")
        return validate_cases()
    if not args.files:
        parser.error("provide one or more files or use --cases")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        candidate, error = _load_json(path)
        result = Assessment("ERROR", (error,), ()) if error else assess(candidate)
        print(json.dumps({"file": path.name, **result.as_dict()}, sort_keys=True))
        failed = failed or result.outcome != "READY"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
