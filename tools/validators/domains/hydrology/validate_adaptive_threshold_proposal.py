#!/usr/bin/env python3
"""Validate one deterministic, no-network AdaptiveThresholdProposal packet."""

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
    / "schemas/contracts/v1/domains/hydrology/adaptive_threshold_proposal.schema.json"
)
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "drought-context-threshold-review-only"
RECALIBRATION_METHODS = {
    "RECOMPUTE_SEASONAL_PERCENTILES",
    "REVIEW_ADAPTIVE_THRESHOLD",
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
    projected.pop("proposal_id", None)
    projected.pop("spec_hash", None)
    encoded = json.dumps(
        projected,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def expected_proposal_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return "adaptive-threshold-proposal:" + digest[:24]


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _sorted_unique_strings(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def _parse_datetime(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        expected_hash = canonical_spec_hash(candidate)
        expected_id = expected_proposal_id(candidate)
    except (TypeError, ValueError, RecursionError):
        expected_hash = None
        expected_id = None
    if expected_hash is not None and candidate.get("spec_hash") != expected_hash:
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if expected_id is not None and candidate.get("proposal_id") != expected_id:
        findings.append(Finding("PROPOSAL_ID_MISMATCH", "/proposal_id"))

    detector = _mapping(candidate.get("detector"))
    context = _mapping(candidate.get("drought_context"))
    assessment = _mapping(candidate.get("assessment"))

    if context.get("source_role") != "CLASSIFICATION":
        findings.append(Finding("DROUGHT_SOURCE_ROLE_MISMATCH", "/drought_context/source_role"))
    if context.get("support_type") != "DERIVED_CLASSIFICATION":
        findings.append(Finding("DROUGHT_SUPPORT_TYPE_MISMATCH", "/drought_context/support_type"))

    detector_start = _parse_datetime(detector.get("analysis_start"))
    detector_end = _parse_datetime(detector.get("analysis_end"))
    context_start = _parse_datetime(context.get("valid_start"))
    context_end = _parse_datetime(context.get("valid_end"))
    if detector_start is not None and detector_end is not None and detector_start >= detector_end:
        findings.append(Finding("DETECTOR_WINDOW_INVALID", "/detector"))
    if context_start is not None and context_end is not None and context_start >= context_end:
        findings.append(Finding("DROUGHT_WINDOW_INVALID", "/drought_context"))

    detector_refs = _array(detector.get("evidence_refs"))
    context_refs = _array(context.get("evidence_refs"))
    assessment_refs = _array(assessment.get("evidence_refs"))
    reasons = _array(assessment.get("reason_codes"))
    for field, refs in (
        ("/detector/evidence_refs", detector_refs),
        ("/drought_context/evidence_refs", context_refs),
        ("/assessment/evidence_refs", assessment_refs),
        ("/assessment/reason_codes", reasons),
    ):
        if not _sorted_unique_strings(refs):
            findings.append(
                Finding(
                    "REASON_CODES_NOT_CANONICAL"
                    if field.endswith("reason_codes")
                    else "EVIDENCE_REFS_NOT_CANONICAL",
                    field,
                )
            )
    endpoint_refs = {
        item
        for item in detector_refs + context_refs
        if isinstance(item, str)
    }
    if not endpoint_refs.issubset(
        {item for item in assessment_refs if isinstance(item, str)}
    ):
        findings.append(
            Finding("ASSESSMENT_EVIDENCE_INCOMPLETE", "/assessment/evidence_refs")
        )

    outcome = assessment.get("outcome")
    materiality = assessment.get("materiality")
    method = assessment.get("recommended_method")
    reason_set = {item for item in reasons if isinstance(item, str)}
    baseline_pinned = detector.get("baseline_spec_hash") is not None
    rule_pinned = context.get("materiality_rule_ref") is not None

    if outcome == "KEEP_BASELINE":
        if materiality != "NOT_MATERIAL":
            findings.append(Finding("KEEP_REQUIRES_NOT_MATERIAL", "/assessment/materiality"))
        if method != "NONE":
            findings.append(Finding("KEEP_METHOD_MUST_BE_NONE", "/assessment/recommended_method"))
        if not baseline_pinned:
            findings.append(Finding("KEEP_REQUIRES_BASELINE", "/detector/baseline_spec_hash"))
        if not rule_pinned:
            findings.append(Finding("KEEP_REQUIRES_MATERIALITY_RULE", "/drought_context/materiality_rule_ref"))
        if "DROUGHT_CONTEXT_NOT_MATERIAL" not in reason_set:
            findings.append(Finding("KEEP_REASON_REQUIRED", "/assessment/reason_codes"))
    elif outcome == "REVIEW_RECALIBRATION":
        if materiality != "MATERIAL":
            findings.append(Finding("REVIEW_REQUIRES_MATERIAL", "/assessment/materiality"))
        if method not in RECALIBRATION_METHODS:
            findings.append(Finding("REVIEW_METHOD_INVALID", "/assessment/recommended_method"))
        if not baseline_pinned:
            findings.append(Finding("REVIEW_REQUIRES_BASELINE", "/detector/baseline_spec_hash"))
        if not rule_pinned:
            findings.append(Finding("REVIEW_REQUIRES_MATERIALITY_RULE", "/drought_context/materiality_rule_ref"))
        if "DROUGHT_CONTEXT_MATERIAL" not in reason_set:
            findings.append(Finding("REVIEW_REASON_REQUIRED", "/assessment/reason_codes"))
    elif outcome == "HOLD":
        if materiality != "UNRESOLVED":
            findings.append(Finding("HOLD_MATERIALITY_MUST_BE_UNRESOLVED", "/assessment/materiality"))
        if method != "HOLD":
            findings.append(Finding("HOLD_METHOD_REQUIRED", "/assessment/recommended_method"))
        expected: set[str] = set()
        if not baseline_pinned:
            expected.add("BASELINE_SPEC_UNRESOLVED")
        if not rule_pinned:
            expected.add("MATERIALITY_RULE_UNRESOLVED")
        if baseline_pinned and rule_pinned:
            expected.add("DROUGHT_CONTEXT_UNRESOLVED")
        if not reason_set.intersection(expected):
            findings.append(Finding("HOLD_REASON_MISMATCH", "/assessment/reason_codes"))
    elif outcome == "ERROR":
        if materiality != "UNKNOWN":
            findings.append(Finding("ERROR_MATERIALITY_MUST_BE_UNKNOWN", "/assessment/materiality"))
        if method != "UNKNOWN":
            findings.append(Finding("ERROR_METHOD_MUST_BE_UNKNOWN", "/assessment/recommended_method"))
        if "OPERATIONAL_ERROR" not in reason_set:
            findings.append(Finding("ERROR_REASON_REQUIRED", "/assessment/reason_codes"))

    governance = _mapping(candidate.get("governance"))
    required_true = (
        "classification_not_observation",
        "baseline_not_evidence",
        "watcher_non_publisher",
    )
    required_false = (
        "configuration_mutated",
        "exact_threshold_proposed",
        "network_fetch",
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
                "percentile_computation": False,
                "threshold_computation": False,
                "configuration_mutation": False,
                "event_calling": False,
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
        description="Validate one fixture-first AdaptiveThresholdProposal packet."
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
