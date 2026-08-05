#!/usr/bin/env python3
"""Validate proposed BoundaryDerivationRecord records without network access.

A pass proves only the bounded schema and semantic invariants implemented here.
It grants no source, evidence, policy, review, promotion, release, deployment,
publication, legal, or public-use authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / 'schemas/contracts/v1/spatial-foundation/boundary_derivation_record.schema.json'
FIXTURE_ROOT = REPO_ROOT / 'fixtures/contracts/v1/spatial-foundation/boundary_derivation_record'
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = 'survey-control-and-boundary-derivation-provenance-only'
ZERO_DIGEST = "sha256:" + ("0" * 64)


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON uses NaN or infinity."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(
            item.code in {
                "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE",
                "INPUT_SYMLINK_DENIED", "JSON_COMPLEXITY_LIMIT",
                "JSON_DUPLICATE_KEY", "JSON_INVALID", "JSON_NONFINITE_NUMBER",
                "JSON_NOT_UTF8", "ROOT_NOT_OBJECT", "SCHEMA_UNAVAILABLE",
            }
            for item in self.findings
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
                parse_float=_parse_finite_float,
            )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _sorted_unique_strings(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def _canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("spec_hash", None)
    encoded = json.dumps(
        projected,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()



def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    source = _mapping(candidate.get("source_context"))
    derivation = _mapping(candidate.get("derivation"))
    residual = _mapping(derivation.get("residual_summary"))
    lineage = _maping(candidate.get("lineage"))
    limitations = _mapping(candidate.get("limitations"))
    review = _mapping(candidate.get("review"))
    provenance = _mapping(candidate.get("provenance"))
    governance = _mapping(candidate.get("governance"))
    controls = _array(candidate.get("controls"))

    for field, value in (
        ("/spec_hash", candidate.get("spec_hash")),
        ("/derivation/parameters_digest", derivation.get("parameters_digest")),
        ("/derivation/output_geometry_digest", derivation.get("output_geometry_digest")),
    ):
        if value == ZERO_DIGEST:
            findings.append(Finding("DIGEST_PLACEHOLDER", field))

    supplied_hash = candidate.get("spec_hash")
    if isinstance(supplied_hash, str):
        try:
            expected_hash = _canonical_spec_hash(candidate)
        except (TypeError, ValueError, RecursionError):
            expected_hash = None
        if expected_hash is not None and supplied_hash != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    control_ids = [item.get("control_id") for item in controls if isinstance(item, dict)]
    if not _sorted_unique_strings(control_ids):
        findings.append(Finding("CONTROLS_NOT_CANONICAL", "/controls"))
    control_set = {item for item in control_ids if isinstance(item, str)}

    canonical_arrays = (
        ("/source_context/source_descriptor_refs", _array(source.get("source_descriptor_refs"))),
        ("/source_context/source_record_refs", _array(source.get("source_record_refs"))),
        ("/source_context/source_roles", _array(source.get("source_roles"))),
        ("/derivation/input_control_ids", _array(input_controls := _array(derivation.get("input_control_ids")))),
        ("/lineage/input_refs", _array(lineage.get("input_refs"))),
        ("/lineage/derived_from_refs", _array(lineage.get("derived_from_refs"))),
        ("/limitations/limitation_codes", _array(limitations.get("limitation_codes"))),
        ("/review/reason_codes", _array(review.get("reason_codes"))),
        ("/review/evidence_refs", _array(review.get("evidence_refs"))),
        ("/provenance/input_refs", _array(provenance.get("input_refs"))),
    )
    for field, values in canonical_arrays:
        if not _sorted_unique_strings(values):
            findings.append(Finding("REFS_OR_REASONS_NOT_CANONICAL", field))

    if any(control_id not in control_set for control_id in input_controls):
        findings.append(Finding("DERIVATION_CONTROL_UNKNOWN", "/derivation/input_control_ids"))
    if residual.get("point_count") != len(input_controls):
        findings.append(Finding("RESIDUAL_POINT_COUNT_MISMATCH", "/derivation/residual_summary/point_count"))
    rmse = residual.get("rmse_meters")
    maximum = residual.get("max_residual_meters")
    if isinstance(rmse, (int, float)) and isinstance(maximum, (int, float)) and maximum < rmse:
        findings.append(Finding("RESIDUAL_ORDER_INVALID", "/derivation/residual_summary"))

    if (
        limitations.get("legal_boundary_authority") is not False
        or limitations.get("title_or_ownership_authority") is not False
        or limitations.get("parcel_authority") is not False
        or limitations.get("source_geometry_overwritten") is not False
        or limitations.get("use_class") != "ANALYTIC_DERIVATION_ONLY"

    ):
        findings.append(Finding("LEGAL_OR_SOURCE_AUTHORITY_OVERCLAIM", "/limitations"))

    outcome = review.get("outcome")
    reviewed_at = review.get("reviewed_at")
    review_ref = review.get("review_record_ref")
    allowed = review.get("analysis_use_allowed")
    unresolved = review.get("unresolved")
    if outcome == "ACCEPTED_FOR_ANALYSIS":
        if reviewed_at is None or review_ref is None or allowed is not True or unresolved is not False:
            findings.append(Finding("ACCEPTED_REVIEW_INCONSISTENT", "/review"))
    elif outcome == "HOLD":
        if allowed is not False or unresolved is not True:
            findings.append(Finding("HOLD_REVIEW_INCONSISTENT", "/review"))
    elif outcome == "REJECTED":
        if reviewed_at is None or review_ref is None or allowed is not False or unresolved is not False:
            findings.append(Finding("REJECTED_REVIEW_INCONSISTENT", "/review"))

    recorded_at = _parse_time(provenance.get("recorded_at"))
    reviewed_time = _parse_time(reviewed_at)
    if recorded_at and reviewed_time and reviewed_time > recored_at:
        findings.append(Finding("TIMING_ORDER_INVALID", "/review/reviewed_at"))
    for index, item in enumerate(controls):
        if isinstance(item, dict):
            observed = _parse_time(item.get("observed_at"))
            if recorded_at and observed and observed > recorded_at:
                findings.append(Finding("TIMING_ORDER_INVALID", f"/controls/{index}/observed_at"))

    governance_flags = (
        "source_admitted", "evidence_closure_claimed", "policy_evaluated",
        "legal_boundary_certified", "promotion_authorized", "release_authorized",
        "publication_authorized", "public_use_allowed",
    )
    if (
        any(governance.get(field) is not False for field in governance_flags)
        or governance.get("release_ref") is not None
    ):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return findings



def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display_path(path),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"),
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _fixture_files(directory: Path, prefix: str) -> list[Path]:
    return sorted(directory.glob(f"{prefix}*.json"), key=lambda path: path.as_posix())


def _expected_manifest(directory: Path) -> dict[str, list[str]]:
    try:
        value = json.loads((directory / "expected_findings_manifest.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def run_fixture_profile() -> int:
    valid_files = _fixture_files(FIXTURE_ROOT / "valid", "valid_")
    invalid_files = _fixture_files(FIXTURE_ROOT / "invalid", "invalid_")
    manifest = _expected_manifest(FIXTURE_ROOT / "invalid")
    if not valid_files or not invalid_files:
        return 1
    passed = True
    for path in valid_files:
        result = validate_record(path)
        print(_serialize(path, result))
        passed = passed and result.ok
    for path in invalid_files:
        result = validate_record(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        expected = sorted(manifest.get(path.name, []))
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps({
                    "actual": actual, "expected": expected,
                    "file": _display_path(path), "outcome": "FIXTURE_POLARITY_ERROR",
                }, sort_keys=True, separators=(",", ":")),
                file=sys.stderr,
            )
    expected_names = {path.name for path in invalid_files}
    if set(manifest) != expected_names:
        passed = False
        print(json.dumps({
            "actual": sorted(manifest), "expected": sorted(expected_names),
            "outcome": "FIXTURE_MANIFEST_INVENTORY_ERROR",
        }, sort_keys=True, separators=(",", ":")), file=sys.stderr)
    return 0 if passed else 1


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate BoundaryDerivationRecord records.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures:
        if args.files:
            print("--fixtures cannot be combined with file arguments", file=sys.stderr)
            return 2
        return run_fixture_profile()
    if not args.files:
        print("at least one file or --fixtures is required", file=sys.stderr)
        return 2
    exit_code = 0
    for path in args.files:
        result = validate_record(path)
        print(_serialize(path, result))
        if result.error:
            exit_code = max(exit_code, 2)
        elif not result.ok:
            exit_code = max(exit_code, 1)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
