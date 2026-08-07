#!/usr/bin/env python3
"""Validate one deterministic, no-network KGS ProductionMaterialChange packet."""

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

REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/geology/production_material_change.schema.json"
)
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "kgs-production-material-change-only"
CHANGE_FIELDS = {
    "coverage_end": "COVERAGE_END",
    "record_count": "RECORD_COUNT",
    "manifest_digest": "MANIFEST_DIGEST",
    "footprint_digest": "FOOTPRINT_DIGEST",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains NaN or infinity."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    packet_outcome: str | None = None

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def operational_error(self) -> bool:
        return any(
            item.code
            in {
                "FILE_NOT_FOUND",
                "FILE_READ_ERROR",
                "FILE_TOO_LARGE",
                "INPUT_SYMLINK_DENIED",
                "JSON_COMPLEXITY_LIMIT",
                "JSON_DUPLICATE_KEY",
                "JSON_INVALID",
                "JSON_NONFINITE_NUMBER",
                "JSON_NOT_UTF8",
                "ROOT_NOT_OBJECT",
                "SCHEMA_UNAVAILABLE",
            }
            for item in self.findings
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
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
                parse_constant=_reject_nonfinite,
                parse_float=_finite_float,
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
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("assessment_id", None)
    projected.pop("spec_hash", None)
    encoded = json.dumps(
        projected,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def expected_assessment_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return "kgs-production-change:" + digest[:24]


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _sorted_unique_strings(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def _parse_month(value: Any) -> tuple[int, int] | None:
    if not isinstance(value, str) or len(value) != 7 or value[4] != "-":
        return None
    try:
        year = int(value[:4])
        month = int(value[5:])
    except ValueError:
        return None
    if year < 1 or month < 1 or month > 12:
        return None
    return year, month


def _parse_datetime(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None


def _snapshot_findings(name: str, snapshot: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    refs = _array(snapshot.get("evidence_refs"))
    if not _sorted_unique_strings(refs):
        findings.append(Finding("EVIDENCE_REFS_NOT_CANONICAL", f"/{name}/evidence_refs"))
    if snapshot.get("source_role") != "PRODUCTION_RECORDS":
        findings.append(Finding("SOURCE_ROLE_MISMATCH", f"/{name}/source_role"))
    if snapshot.get("support_type") != "OFFICIAL_DERIVED_PRODUCTION_REFERENCE":
        findings.append(Finding("SUPPORT_TYPE_MISMATCH", f"/{name}/support_type"))
    if _parse_month(snapshot.get("coverage_end")) is None:
        findings.append(Finding("COVERAGE_END_INVALID", f"/{name}/coverage_end"))
    if _parse_datetime(snapshot.get("retrieved_at")) is None:
        findings.append(Finding("RETRIEVED_AT_INVALID", f"/{name}/retrieved_at"))
    return findings


def _computed_dimensions(
    prior: Mapping[str, Any], current: Mapping[str, Any]
) -> list[str]:
    return sorted(
        dimension
        for field, dimension in CHANGE_FIELDS.items()
        if prior.get(field) != current.get(field)
    )


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        expected_hash = canonical_spec_hash(candidate)
        expected_id = expected_assessment_id(candidate)
    except (TypeError, ValueError, RecursionError):
        expected_hash = None
        expected_id = None
    if expected_hash is not None and candidate.get("spec_hash") != expected_hash:
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if expected_id is not None and candidate.get("assessment_id") != expected_id:
        findings.append(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))

    current = _mapping(candidate.get("current_snapshot"))
    prior_value = candidate.get("prior_snapshot")
    prior = _mapping(prior_value) if prior_value is not None else None
    findings.extend(_snapshot_findings("current_snapshot", current))
    if prior is not None:
        findings.extend(_snapshot_findings("prior_snapshot", prior))

    assessment = _mapping(candidate.get("assessment"))
    outcome = assessment.get("outcome")
    material_change = assessment.get("material_change")
    dimensions = _array(assessment.get("change_dimensions"))
    reasons = _array(assessment.get("reason_codes"))
    assessment_refs = _array(assessment.get("evidence_refs"))

    if not _sorted_unique_strings(dimensions):
        findings.append(
            Finding("CHANGE_DIMENSIONS_NOT_CANONICAL", "/assessment/change_dimensions")
        )
    if not _sorted_unique_strings(reasons):
        findings.append(Finding("REASON_CODES_NOT_CANONICAL", "/assessment/reason_codes"))
    if not _sorted_unique_strings(assessment_refs):
        findings.append(Finding("EVIDENCE_REFS_NOT_CANONICAL", "/assessment/evidence_refs"))

    snapshot_refs = {
        item
        for snapshot in (prior, current)
        if snapshot is not None
        for item in _array(snapshot.get("evidence_refs"))
        if isinstance(item, str)
    }
    if not snapshot_refs.issubset(
        {item for item in assessment_refs if isinstance(item, str)}
    ):
        findings.append(
            Finding("ASSESSMENT_EVIDENCE_INCOMPLETE", "/assessment/evidence_refs")
        )

    rights_unresolved = current.get("rights_state") != "VERIFIED" or (
        prior is not None and prior.get("rights_state") != "VERIFIED"
    )
    coverage_regression = False
    computed_dimensions: list[str] = []
    if prior is not None:
        computed_dimensions = _computed_dimensions(prior, current)
        prior_month = _parse_month(prior.get("coverage_end"))
        current_month = _parse_month(current.get("coverage_end"))
        coverage_regression = (
            prior_month is not None
            and current_month is not None
            and current_month < prior_month
        )

    reason_set = {item for item in reasons if isinstance(item, str)}
    if outcome == "NO_CHANGE":
        if prior is None:
            findings.append(Finding("NO_CHANGE_WITHOUT_PRIOR", "/assessment/outcome"))
        if rights_unresolved:
            findings.append(Finding("NO_CHANGE_WITH_UNRESOLVED_RIGHTS", "/assessment/outcome"))
        if coverage_regression:
            findings.append(Finding("NO_CHANGE_WITH_COVERAGE_REGRESSION", "/assessment/outcome"))
        if material_change is not False:
            findings.append(Finding("NO_CHANGE_MATERIALITY_INVALID", "/assessment/material_change"))
        if dimensions != []:
            findings.append(Finding("NO_CHANGE_DIMENSIONS_PRESENT", "/assessment/change_dimensions"))
        if computed_dimensions:
            findings.append(Finding("NO_CHANGE_FIELDS_DIFFER", "/assessment/change_dimensions"))
        if "SNAPSHOTS_MATCH" not in reason_set:
            findings.append(Finding("NO_CHANGE_REASON_REQUIRED", "/assessment/reason_codes"))
    elif outcome == "REVIEW":
        if prior is None:
            findings.append(Finding("REVIEW_WITHOUT_PRIOR", "/assessment/outcome"))
        if rights_unresolved:
            findings.append(Finding("REVIEW_WITH_UNRESOLVED_RIGHTS", "/assessment/outcome"))
        if coverage_regression:
            findings.append(Finding("COVERAGE_REGRESSION_REQUIRES_HOLD", "/assessment/outcome"))
        if material_change is not True:
            findings.append(Finding("REVIEW_MATERIALITY_INVALID", "/assessment/material_change"))
        if not computed_dimensions:
            findings.append(Finding("REVIEW_WITHOUT_CHANGE", "/assessment/change_dimensions"))
        if dimensions != computed_dimensions:
            findings.append(Finding("CHANGE_DIMENSIONS_MISMATCH", "/assessment/change_dimensions"))
        if "MATERIAL_CHANGE_DETECTED" not in reason_set:
            findings.append(Finding("REVIEW_REASON_REQUIRED", "/assessment/reason_codes"))
    elif outcome == "HOLD":
        if material_change is not None:
            findings.append(Finding("HOLD_MATERIALITY_MUST_BE_NULL", "/assessment/material_change"))
        if dimensions != []:
            findings.append(Finding("HOLD_DIMENSIONS_MUST_BE_EMPTY", "/assessment/change_dimensions"))
        expected_reasons: set[str] = set()
        if prior is None:
            expected_reasons.add("PRIOR_SNAPSHOT_MISSING")
        if rights_unresolved:
            expected_reasons.add("RIGHTS_STATE_UNRESOLVED")
        if coverage_regression:
            expected_reasons.add("COVERAGE_REGRESSION")
        if not expected_reasons:
            findings.append(Finding("HOLD_WITHOUT_BLOCKER", "/assessment"))
        elif not reason_set.intersection(expected_reasons):
            findings.append(Finding("HOLD_REASON_MISMATCH", "/assessment/reason_codes"))
    elif outcome == "ERROR":
        if material_change is not None:
            findings.append(Finding("ERROR_MATERIALITY_MUST_BE_NULL", "/assessment/material_change"))
        if dimensions != []:
            findings.append(Finding("ERROR_DIMENSIONS_MUST_BE_EMPTY", "/assessment/change_dimensions"))
        if "OPERATIONAL_ERROR" not in reason_set:
            findings.append(Finding("ERROR_REASON_REQUIRED", "/assessment/reason_codes"))

    governance = _mapping(candidate.get("governance"))
    required_true = (
        "source_roles_preserved",
        "production_not_geology",
        "watcher_non_publisher",
    )
    required_false = (
        "network_fetch",
        "raw_rows_compared",
        "policy_evaluated",
        "promotion_authorized",
        "release_authorized",
        "publication_authorized",
    )
    if any(governance.get(name) is not True for name in required_true):
        findings.append(Finding("SOURCE_ROLE_BOUNDARY_VIOLATION", "/governance"))
    if any(governance.get(name) is not False for name in required_false):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(_semantic_findings(candidate))
    packet_outcome = None
    assessment = candidate.get("assessment")
    if isinstance(assessment, dict) and isinstance(assessment.get("outcome"), str):
        packet_outcome = assessment["outcome"]
    return ValidationResult(tuple(sorted(set(findings))), packet_outcome)


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    return validate_payload(candidate)


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    validation_outcome = "PASS" if result.ok else (
        "ERROR" if result.operational_error else "FAIL"
    )
    return json.dumps(
        {
            "file": _display_path(path),
            "findings": [
                {"code": item.code, "field": item.field} for item in result.findings
            ],
            "outcome": validation_outcome,
            "packet_outcome": result.packet_outcome,
            "scope": SCOPE,
            "authority": {
                "network_fetch": False,
                "raw_row_comparison": False,
                "policy_evaluation": False,
                "lifecycle_write": False,
                "promotion": False,
                "release": False,
                "publication": False,
            },
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate one fixture-first KGS ProductionMaterialChange packet."
    )
    parser.add_argument("path", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    result = validate_file(args.path)
    print(_serialize(args.path, result))
    return 0 if result.ok else (2 if result.operational_error else 1)


if __name__ == "__main__":
    sys.exit(main())
