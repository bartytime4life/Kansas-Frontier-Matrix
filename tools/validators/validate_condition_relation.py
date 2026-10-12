#!/usr/bin/env python3
"""Validate one deterministic, no-network ConditionRelation packet."""

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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/condition_relation.schema.json"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "condition-relation-only"

ROLE_SUPPORT = {
    "OBSERVATION": "DIRECT_MEASUREMENT",
    "CLASSIFICATION": "DERIVED_CLASSIFICATION",
    "FORECAST": "PREDICTION",
    "ADVISORY": "REGULATORY_STATUS",
    "MODEL": "MODELED_ESTIMATE",
    "CONTEXT": "CONTEXT_ONLY",
}
WEIGHTING_METHODS = {"AREA_WEIGHTED", "DISTANCE_WEIGHTED", "STATION_ASSIGNMENT"}


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
    projected.pop("relation_id", None)
    projected.pop("spec_hash", None)
    encoded = json.dumps(
        projected,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def expected_relation_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return "condition-relation:" + digest[:24]


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


def _endpoint_findings(name: str, endpoint: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    role = endpoint.get("source_role")
    support = endpoint.get("support_type")
    if ROLE_SUPPORT.get(role) != support:
        findings.append(Finding("SOURCE_ROLE_SUPPORT_TYPE_MISMATCH", f"/{name}/support_type"))
    refs = _array(endpoint.get("evidence_refs"))
    if not _sorted_unique_strings(refs):
        findings.append(Finding("EVIDENCE_REFS_NOT_CANONICAL", f"/{name}/evidence_refs"))
    temporal = _mapping(endpoint.get("temporal_scope"))
    start = _parse_datetime(temporal.get("start"))
    end = _parse_datetime(temporal.get("end"))
    if start is not None and end is not None and start >= end:
        findings.append(Finding("TEMPORAL_WINDOW_INVALID", f"/{name}/temporal_scope"))
    return findings


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        expected_hash = canonical_spec_hash(candidate)
        expected_id = expected_relation_id(candidate)
    except (TypeError, ValueError, RecursionError):
        expected_hash = None
        expected_id = None
    if expected_hash is not None and candidate.get("spec_hash") != expected_hash:
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if expected_id is not None and candidate.get("relation_id") != expected_id:
        findings.append(Finding("RELATION_ID_MISMATCH", "/relation_id"))

    left = _mapping(candidate.get("left"))
    right = _mapping(candidate.get("right"))
    findings.extend(_endpoint_findings("left", left))
    findings.extend(_endpoint_findings("right", right))
    if left.get("subject_ref") == right.get("subject_ref"):
        findings.append(Finding("SELF_RELATION_DENIED", "/right/subject_ref"))

    assessment = _mapping(candidate.get("assessment"))
    reason_codes = _array(assessment.get("reason_codes"))
    assessment_refs = _array(assessment.get("evidence_refs"))
    if not _sorted_unique_strings(reason_codes):
        findings.append(Finding("REASON_CODES_NOT_CANONICAL", "/assessment/reason_codes"))
    if not _sorted_unique_strings(assessment_refs):
        findings.append(Finding("EVIDENCE_REFS_NOT_CANONICAL", "/assessment/evidence_refs"))

    endpoint_refs = {
        item
        for endpoint in (left, right)
        for item in _array(endpoint.get("evidence_refs"))
        if isinstance(item, str)
    }
    if not endpoint_refs.issubset({item for item in assessment_refs if isinstance(item, str)}):
        findings.append(Finding("ASSESSMENT_EVIDENCE_INCOMPLETE", "/assessment/evidence_refs"))

    left_scale = _mapping(left.get("spatial_scope")).get("scale")
    right_scale = _mapping(right.get("spatial_scope")).get("scale")
    scale = assessment.get("scale_compatibility")
    weighting = assessment.get("weighting_method")
    if left_scale != right_scale and scale == "COMPATIBLE":
        findings.append(Finding("CROSS_SCALE_RELATION_REQUIRES_WEIGHTING", "/assessment/scale_compatibility"))
    if scale == "REQUIRES_WEIGHTING" and weighting not in WEIGHTING_METHODS:
        findings.append(Finding("WEIGHTING_REQUIRED", "/assessment/weighting_method"))
    if scale in {"INCOMPATIBLE", "UNKNOWN"} and weighting in WEIGHTING_METHODS:
        findings.append(Finding("WEIGHTING_FOR_UNRESOLVED_SCALE_DENIED", "/assessment/weighting_method"))

    relation_kind = candidate.get("relation_kind")
    roles = {left.get("source_role"), right.get("source_role")}
    if relation_kind == "OUTLOOK_ALIGNMENT" and "FORECAST" not in roles:
        findings.append(Finding("OUTLOOK_FORECAST_ROLE_REQUIRED", "/relation_kind"))

    requested_claim = candidate.get("requested_claim_type")
    outcome = assessment.get("outcome")
    reason_set = {item for item in reason_codes if isinstance(item, str)}
    spatial = assessment.get("spatial_relation")
    temporal = assessment.get("temporal_relation")

    if requested_claim == "CAUSAL":
        if outcome != "DENY":
            findings.append(Finding("CAUSAL_REQUEST_NOT_DENIED", "/assessment/outcome"))
        if "CAUSALITY_ASSERTION_DENIED" not in reason_set:
            findings.append(Finding("CAUSAL_DENY_REASON_REQUIRED", "/assessment/reason_codes"))
    elif outcome == "ANSWER":
        if "CONTEXTUAL_RELATION_SUPPORTED" not in reason_set:
            findings.append(Finding("ANSWER_REASON_REQUIRED", "/assessment/reason_codes"))
        if spatial == "UNKNOWN":
            findings.append(Finding("ANSWER_SPATIAL_UNRESOLVED", "/assessment/spatial_relation"))
        if temporal == "UNKNOWN":
            findings.append(Finding("ANSWER_TEMPORAL_UNRESOLVED", "/assessment/temporal_relation"))
        if scale in {"UNKNOWN", "INCOMPATIBLE"}:
            findings.append(Finding("ANSWER_SCALE_UNRESOLVED", "/assessment/scale_compatibility"))
    elif outcome == "ABSTAIN":
        expected_reasons: set[str] = set()
        if spatial == "UNKNOWN":
            expected_reasons.add("SPATIAL_RELATION_UNRESOLVED")
        if temporal == "UNKNOWN":
            expected_reasons.add("TEMPORAL_RELATION_UNRESOLVED")
        if scale == "UNKNOWN":
            expected_reasons.add("SCALE_COMPATIBILITY_UNRESOLVED")
        if scale == "INCOMPATIBLE":
            expected_reasons.add("SCALE_INCOMPATIBLE")
        if not expected_reasons:
            findings.append(Finding("ABSTAIN_WITHOUT_UNRESOLVED_DIMENSION", "/assessment"))
        elif not reason_set.intersection(expected_reasons):
            findings.append(Finding("ABSTAIN_REASON_MISMATCH", "/assessment/reason_codes"))
    elif outcome == "DENY":
        allowed = {"CAUSALITY_ASSERTION_DENIED", "SOURCE_ROLE_COLLAPSE_DENIED", "SENSITIVE_SCOPE_BLOCKED"}
        if not reason_set.intersection(allowed):
            findings.append(Finding("DENY_REASON_REQUIRED", "/assessment/reason_codes"))
    elif outcome == "ERROR":
        if "OPERATIONAL_ERROR" not in reason_set:
            findings.append(Finding("ERROR_REASON_REQUIRED", "/assessment/reason_codes"))
        if any(value != "UNKNOWN" for value in (spatial, temporal, scale, weighting)):
            findings.append(Finding("ERROR_STATE_NOT_UNKNOWN", "/assessment"))

    governance = _mapping(candidate.get("governance"))
    required_true = (
        "source_roles_preserved",
        "support_types_preserved",
        "causality_not_inferred",
        "observation_not_forecast",
        "classification_not_observation",
    )
    required_false = (
        "authority_created",
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
    validation_outcome = "PASS" if result.ok else ("ERROR" if result.operational_error else "FAIL")
    return json.dumps(
        {
            "file": _display_path(path),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": validation_outcome,
            "packet_outcome": result.packet_outcome,
            "scope": SCOPE,
            "authority": {
                "network_fetch": False,
                "spatial_computation": False,
                "causal_inference": False,
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
    parser = argparse.ArgumentParser(description="Validate one fixture-first ConditionRelation packet.")
    parser.add_argument("path", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    result = validate_file(args.path)
    print(_serialize(args.path, result))
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
