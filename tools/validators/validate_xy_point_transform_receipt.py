"""Validate fixture-only XY point-transform receipt candidates.

The validator proves closed shape, deterministic identity, explicit source and
CRS bindings, axis-role pairing, declared range and precision reconciliation,
row-count closure, output lineage, and canonical local references. It does not
read a source table, parse a CRS, transform coordinates, resolve evidence,
decide policy or review, promote, release, deploy, publish, or authorize use.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/spatial-foundation/xy_point_transform_receipt.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/spatial-foundation/xy_point_transform_receipt/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {"SOURCE_TABLE_UNRESOLVED", "CRS_UNRESOLVED"}
AXIS_ROLE_PAIRS = {
    ("LONGITUDE", "LATITUDE"),
    ("EASTING", "NORTHING"),
    ("X_COORDINATE", "Y_COORDINATE"),
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (tuple(str(part) for part in error.absolute_path), str(error.validator)),
    )
    return [
        Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path))
        for error in errors[:100]
    ]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _bounds_ordered(bounds: Mapping[str, object]) -> bool:
    return bool(bounds["min_x"] < bounds["max_x"] and bounds["min_y"] < bounds["max_y"])


def _bounds_contained(
    observed: Mapping[str, object], declared: Mapping[str, object]
) -> bool:
    return bool(
        declared["min_x"] <= observed["min_x"] <= observed["max_x"] <= declared["max_x"]
        and declared["min_y"] <= observed["min_y"] <= observed["max_y"] <= declared["max_y"]
    )


def _canonical_refs(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    source = candidate["source_table"]
    crs = candidate["coordinate_reference_system"]
    axes = candidate["axis_mapping"]
    precision = candidate["precision"]
    declared = candidate["declared_valid_bounds"]
    observed = candidate["observed_coordinate_bounds"]
    summary = candidate["validation_summary"]
    output = candidate["output_point_set"]
    assert all(
        isinstance(value, Mapping)
        for value in (source, crs, axes, precision, declared, observed, summary, output)
    )

    if source["resolution"] == "UNRESOLVED":
        findings.add(Finding("SOURCE_TABLE_UNRESOLVED", "/source_table/resolution"))
    if crs["resolution"] == "UNRESOLVED":
        findings.add(Finding("CRS_UNRESOLVED", "/coordinate_reference_system/resolution"))

    x_axis = axes["x"]
    y_axis = axes["y"]
    assert isinstance(x_axis, Mapping) and isinstance(y_axis, Mapping)
    if x_axis["field_name"] == y_axis["field_name"]:
        findings.add(Finding("AXIS_FIELDS_NOT_DISTINCT", "/axis_mapping"))
    role_pair = (x_axis["semantic_role"], y_axis["semantic_role"])
    role_pair_valid = role_pair in AXIS_ROLE_PAIRS
    if not role_pair_valid:
        findings.add(Finding("AXIS_ROLE_PAIR_INVALID", "/axis_mapping"))
    expected_axis_check = "PASS" if role_pair_valid else "FAIL"
    if summary["axis_swap_check"] != expected_axis_check:
        findings.add(Finding("AXIS_SWAP_CHECK_INCONSISTENT", "/validation_summary/axis_swap_check"))

    declared_ordered = _bounds_ordered(declared)
    observed_ordered = _bounds_ordered(observed)
    if not declared_ordered:
        findings.add(Finding("BOUNDS_ORDER_INVALID", "/declared_valid_bounds"))
    if not observed_ordered:
        findings.add(Finding("BOUNDS_ORDER_INVALID", "/observed_coordinate_bounds"))
    if declared_ordered and observed_ordered and not _bounds_contained(observed, declared):
        findings.add(Finding("COORDINATE_RANGE_VIOLATION", "/observed_coordinate_bounds"))

    declared_places = precision["declared_max_decimal_places"]
    if (
        precision["observed_x_decimal_places"] > declared_places
        or precision["observed_y_decimal_places"] > declared_places
    ):
        findings.add(Finding("PRECISION_EXCEEDED", "/precision"))

    if summary["total_rows"] != source["row_count"] or (
        summary["created_points"] + summary["rejected_rows"] != summary["total_rows"]
    ):
        findings.add(Finding("ROW_COUNT_MISMATCH", "/validation_summary"))
    reason_total = sum(
        summary[name]
        for name in (
            "missing_coordinate_rows",
            "out_of_range_rows",
            "non_finite_rows",
            "other_invalid_rows",
        )
    )
    if reason_total != summary["rejected_rows"]:
        findings.add(Finding("REJECTION_COUNT_MISMATCH", "/validation_summary"))
    if output["feature_count"] != summary["created_points"]:
        findings.add(Finding("OUTPUT_COUNT_MISMATCH", "/output_point_set/feature_count"))
    if output["crs_ref"] != crs["crs_ref"] or output["crs_digest"] != crs["crs_digest"]:
        findings.add(Finding("OUTPUT_CRS_MISMATCH", "/output_point_set"))
    if source["artifact_ref"] == output["artifact_ref"]:
        findings.add(Finding("SOURCE_OUTPUT_IDENTITY_COLLISION", "/output_point_set/artifact_ref"))
    if not _canonical_refs(candidate["evidence_refs"]):
        findings.add(Finding("EVIDENCE_REFS_NOT_CANONICAL", "/evidence_refs"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _merge_patch(base: object, patch: object) -> object:
    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, dict) else {}
    for key, value in patch.items():
        if value is None:
            target.pop(key, None)
        else:
            target[key] = _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [
            {
                "name": "fixture_manifest",
                "ok": False,
                "observed": {
                    "outcome": "ERROR",
                    "codes": sorted({item.code for item in load_findings}),
                },
            }
        ]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append(
            {
                "name": entry["name"],
                "ok": observed == expected,
                "expected": expected,
                "observed": observed,
            }
        )
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only XY point-transform receipt candidates."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    if candidate is None:
        result = ValidationResult("ERROR", tuple(sorted(findings)))
    else:
        result = validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
