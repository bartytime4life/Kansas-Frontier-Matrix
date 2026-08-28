#!/usr/bin/env python3
"""Validate one deterministic, no-network PrescribedBurnQualityFlag packet."""

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
    / "schemas/contracts/v1/domains/atmosphere/prescribed_burn_quality_flag.schema.json"
)
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "prescribed-burn-air-quality-context-only"
EXPECTED_USE = {
    "SUPPORTED_CONTEXT": ("SUPPRESS_EVENT_CALLING", "EXCLUDE"),
    "POSSIBLE_CONTEXT": ("ALLOW_WITH_FLAG", "INCLUDE_WITH_FLAG"),
    "NOT_SUPPORTED": ("ALLOW_UNFLAGGED", "INCLUDE_UNFLAGGED"),
    "UNRESOLVED": ("HOLD", "HOLD"),
    "UNKNOWN": ("UNKNOWN", "UNKNOWN"),
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
    projected.pop("flag_id", None)
    projected.pop("spec_hash", None)
    encoded = json.dumps(
        projected,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def expected_flag_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return "air-quality-smoke-flag:" + digest[:24]


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
        expected_id = expected_flag_id(candidate)
    except (TypeError, ValueError, RecursionError):
        expected_hash = None
        expected_id = None
    if expected_hash is not None and candidate.get("spec_hash") != expected_hash:
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if expected_id is not None and candidate.get("flag_id") != expected_id:
        findings.append(Finding("FLAG_ID_MISMATCH", "/flag_id"))

    observation = _mapping(candidate.get("observation"))
    context = _mapping(candidate.get("smoke_context"))
    assessment = _mapping(candidate.get("assessment"))

    if observation.get("source_role") != "OBSERVATION":
        findings.append(Finding("OBSERVATION_SOURCE_ROLE_MISMATCH", "/observation/source_role"))
    if observation.get("support_type") != "DIRECT_MEASUREMENT":
        findings.append(Finding("OBSERVATION_SUPPORT_TYPE_MISMATCH", "/observation/support_type"))
    if context.get("source_role") != "CONTEXT":
        findings.append(Finding("CONTEXT_SOURCE_ROLE_MISMATCH", "/smoke_context/source_role"))
    if context.get("support_type") != "CONTEXT_ONLY":
        findings.append(Finding("CONTEXT_SUPPORT_TYPE_MISMATCH", "/smoke_context/support_type"))

    observation_refs = _array(observation.get("evidence_refs"))
    context_refs = _array(context.get("evidence_refs"))
    assessment_refs = _array(assessment.get("evidence_refs"))
    reasons = _array(assessment.get("reason_codes"))
    for field, refs in (
        ("/observation/evidence_refs", observation_refs),
        ("/smoke_context/evidence_refs", context_refs),
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
        for item in observation_refs + context_refs
        if isinstance(item, str)
    }
    if not endpoint_refs.issubset(
        {item for item in assessment_refs if isinstance(item, str)}
    ):
        findings.append(
            Finding("ASSESSMENT_EVIDENCE_INCOMPLETE", "/assessment/evidence_refs")
        )

    observed_at = _parse_datetime(observation.get("observed_at"))
    valid_start = _parse_datetime(context.get("valid_start"))
    valid_end = _parse_datetime(context.get("valid_end"))
    if valid_start is not None and valid_end is not None and valid_start >= valid_end:
        findings.append(Finding("CONTEXT_TEMPORAL_WINDOW_INVALID", "/smoke_context"))
    declared_temporal = assessment.get("temporal_relation")
    if observed_at is not None and valid_start is not None and valid_end is not None:
        computed_temporal = (
            "OVERLAP" if valid_start <= observed_at < valid_end else "DISJOINT"
        )
        if declared_temporal != "UNKNOWN" and declared_temporal != computed_temporal:
            findings.append(
                Finding("TEMPORAL_RELATION_MISMATCH", "/assessment/temporal_relation")
            )

    outcome = assessment.get("outcome")
    influence = assessment.get("influence_status")
    detector = assessment.get("detector_disposition")
    training = assessment.get("model_training_disposition")
    spatial = assessment.get("spatial_relation")
    temporal = assessment.get("temporal_relation")
    reason_set = {item for item in reasons if isinstance(item, str)}
    requested = candidate.get("requested_claim_type")

    expected_use = EXPECTED_USE.get(influence)
    if expected_use is not None and (detector, training) != expected_use:
        findings.append(Finding("DOWNSTREAM_DISPOSITION_MISMATCH", "/assessment"))

    if requested == "CAUSAL":
        if outcome != "DENY":
            findings.append(Finding("CAUSAL_REQUEST_NOT_DENIED", "/assessment/outcome"))
        if "CAUSALITY_ASSERTION_DENIED" not in reason_set:
            findings.append(Finding("CAUSAL_DENY_REASON_REQUIRED", "/assessment/reason_codes"))
        if influence != "UNKNOWN":
            findings.append(Finding("CAUSAL_DENY_INFLUENCE_MUST_BE_UNKNOWN", "/assessment/influence_status"))
    elif outcome == "ANSWER":
        if spatial == "UNKNOWN":
            findings.append(Finding("ANSWER_SPATIAL_UNRESOLVED", "/assessment/spatial_relation"))
        if temporal == "UNKNOWN":
            findings.append(Finding("ANSWER_TEMPORAL_UNRESOLVED", "/assessment/temporal_relation"))
        if influence in {"UNRESOLVED", "UNKNOWN"}:
            findings.append(Finding("ANSWER_INFLUENCE_UNRESOLVED", "/assessment/influence_status"))
        if influence in {"SUPPORTED_CONTEXT", "POSSIBLE_CONTEXT"}:
            if spatial != "OVERLAP" or temporal != "OVERLAP":
                findings.append(Finding("SMOKE_CONTEXT_REQUIRES_OVERLAP", "/assessment"))
            if "SMOKE_CONTEXT_FLAGGED" not in reason_set:
                findings.append(Finding("SMOKE_FLAG_REASON_REQUIRED", "/assessment/reason_codes"))
        if influence == "NOT_SUPPORTED":
            if spatial != "DISJOINT" and temporal != "DISJOINT":
                findings.append(Finding("NOT_SUPPORTED_REQUIRES_DISJOINT_RELATION", "/assessment"))
            if "SMOKE_CONTEXT_NOT_SUPPORTED" not in reason_set:
                findings.append(Finding("NOT_SUPPORTED_REASON_REQUIRED", "/assessment/reason_codes"))
    elif outcome == "ABSTAIN":
        if influence != "UNRESOLVED":
            findings.append(Finding("ABSTAIN_INFLUENCE_MUST_BE_UNRESOLVED", "/assessment/influence_status"))
        if spatial != "UNKNOWN" and temporal != "UNKNOWN":
            findings.append(Finding("ABSTAIN_WITHOUT_UNRESOLVED_RELATION", "/assessment"))
        if "SMOKE_CONTEXT_UNRESOLVED" not in reason_set:
            findings.append(Finding("ABSTAIN_REASON_REQUIRED", "/assessment/reason_codes"))
    elif outcome == "DENY":
        allowed = {"CAUSALITY_ASSERTION_DENIED", "SENSITIVE_SCOPE_BLOCKED"}
        if not reason_set.intersection(allowed):
            findings.append(Finding("DENY_REASON_REQUIRED", "/assessment/reason_codes"))
    elif outcome == "ERROR":
        if "OPERATIONAL_ERROR" not in reason_set:
            findings.append(Finding("ERROR_REASON_REQUIRED", "/assessment/reason_codes"))
        if any(
            value != "UNKNOWN"
            for value in (spatial, temporal, influence, detector, training)
        ):
            findings.append(Finding("ERROR_STATE_NOT_UNKNOWN", "/assessment"))

    if assessment.get("causal_claim") is not False:
        findings.append(Finding("CAUSAL_CLAIM_DENIED", "/assessment/causal_claim"))

    governance = _mapping(candidate.get("governance"))
    required_true = (
        "source_roles_preserved",
        "observation_not_context",
        "context_not_observation",
        "causality_not_inferred",
    )
    required_false = (
        "configuration_mutated",
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
                "dispersion_model": False,
                "spatial_computation": False,
                "causal_inference": False,
                "configuration_mutation": False,
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
        description="Validate one fixture-first PrescribedBurnQualityFlag packet."
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
