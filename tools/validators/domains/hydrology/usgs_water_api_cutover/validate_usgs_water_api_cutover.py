#!/usr/bin/env python3
"""Validate fixture-only USGS Water API cutover assessments."""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
import sys
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[5]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/hydrology/"
    "usgs_water_api_cutover_assessment.schema.json"
)
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100

DENY_REASONS = frozenset(
    {
        "ACTIVE_LEGACY_ENDPOINT_IN_MODERN_ONLY",
        "DUAL_RUN_CONFLICT",
        "LEGACY_ONLY_MODE",
        "SOURCE_DESCRIPTOR_DENIED",
    }
)


class DuplicateKeyError(ValueError):
    """Raised when an object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised for NaN or Infinity tokens."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _load_payload(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
        )
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_UNREADABLE", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(payload: Mapping[str, Any]) -> list[Finding]:
    try:
        errors = list(
            islice(_schema_validator().iter_errors(payload), MAX_SCHEMA_FINDINGS + 1)
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    ordered = sorted(
        errors,
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )[:MAX_SCHEMA_FINDINGS]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in ordered
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def canonical_spec_hash(payload: Mapping[str, Any]) -> str:
    """Return the deterministic hash of a payload excluding its spec_hash."""

    body = {key: value for key, value in payload.items() if key != "spec_hash"}
    encoded = json.dumps(
        body,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def expected_reasons(payload: Mapping[str, Any]) -> list[str]:
    """Derive the exact finite reason set for a valid payload."""

    reasons: set[str] = set()
    descriptor_state = payload["source_descriptor_state"]
    target_mode = payload["target_mode"]
    endpoints = payload["endpoint_profiles"]
    migration = payload["migration"]

    if descriptor_state == "UNRESOLVED":
        reasons.add("SOURCE_DESCRIPTOR_UNRESOLVED")
    elif descriptor_state == "DENIED":
        reasons.add("SOURCE_DESCRIPTOR_DENIED")

    required_roles = set(migration["required_roles"])
    modern_roles = {
        item["role"]
        for item in endpoints
        if item["active"] is True and item["family"] == "modern_waterdata"
    }
    if not required_roles.issubset(modern_roles):
        reasons.add("REQUIRED_ROLE_MISSING")

    active_legacy = [
        item
        for item in endpoints
        if item["active"] is True and item["family"] != "modern_waterdata"
    ]

    if target_mode == "legacy_only":
        reasons.add("LEGACY_ONLY_MODE")
    elif target_mode == "modern_only" and active_legacy:
        reasons.add("ACTIVE_LEGACY_ENDPOINT_IN_MODERN_ONLY")
    elif target_mode == "dual_run":
        if not active_legacy:
            reasons.add("DUAL_RUN_LEGACY_ENDPOINT_MISSING")
        state = migration["dual_run_reconciliation"]
        if state == "MISSING":
            reasons.add("DUAL_RUN_RECONCILIATION_MISSING")
        elif state == "CONFLICTED":
            reasons.add("DUAL_RUN_CONFLICT")

    if migration["rewrite_map_complete"] is not True:
        reasons.add("REWRITE_MAP_INCOMPLETE")
    if int(migration["legacy_dependency_count"]) > 0:
        reasons.add("LEGACY_DEPENDENCIES_REMAIN")
    return sorted(reasons)


def expected_outcome(reasons: Sequence[str]) -> str:
    """Return the finite outcome for a derived reason set."""

    if any(reason in DENY_REASONS for reason in reasons):
        return "DENY"
    if reasons:
        return "HOLD"
    return "CUTOVER_CANDIDATE"


def _semantic_findings(payload: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    endpoints = payload["endpoint_profiles"]
    migration = payload["migration"]
    target_mode = payload["target_mode"]

    endpoint_ids = [item["endpoint_id"] for item in endpoints]
    if endpoint_ids != sorted(endpoint_ids):
        findings.append(
            Finding("ENDPOINT_PROFILES_NOT_CANONICAL", "/endpoint_profiles")
        )
    if len(endpoint_ids) != len(set(endpoint_ids)):
        findings.append(Finding("ENDPOINT_ID_DUPLICATE", "/endpoint_profiles"))

    required_roles = migration["required_roles"]
    if required_roles != sorted(required_roles):
        findings.append(
            Finding("REQUIRED_ROLES_NOT_CANONICAL", "/migration/required_roles")
        )

    modern_roles = sorted(
        {
            item["role"]
            for item in endpoints
            if item["active"] is True and item["family"] == "modern_waterdata"
        }
    )
    if migration["modern_coverage"] != modern_roles:
        findings.append(
            Finding("MODERN_COVERAGE_MISMATCH", "/migration/modern_coverage")
        )

    reconciliation = migration["dual_run_reconciliation"]
    evidence_refs = migration["reconciliation_evidence_refs"]
    if target_mode == "dual_run":
        if reconciliation == "NOT_APPLICABLE":
            findings.append(
                Finding(
                    "DUAL_RUN_RECONCILIATION_STATE_INVALID",
                    "/migration/dual_run_reconciliation",
                )
            )
        if reconciliation == "COMPLETE" and not evidence_refs:
            findings.append(
                Finding(
                    "RECONCILIATION_EVIDENCE_REQUIRED",
                    "/migration/reconciliation_evidence_refs",
                )
            )
        if reconciliation != "COMPLETE" and evidence_refs:
            findings.append(
                Finding(
                    "RECONCILIATION_EVIDENCE_UNEXPECTED",
                    "/migration/reconciliation_evidence_refs",
                )
            )
    elif reconciliation != "NOT_APPLICABLE":
        findings.append(
            Finding(
                "RECONCILIATION_STATE_UNEXPECTED",
                "/migration/dual_run_reconciliation",
            )
        )
    elif evidence_refs:
        findings.append(
            Finding(
                "RECONCILIATION_EVIDENCE_UNEXPECTED",
                "/migration/reconciliation_evidence_refs",
            )
        )

    expected_hash = canonical_spec_hash(payload)
    if payload["spec_hash"] != expected_hash:
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    reasons = expected_reasons(payload)
    decision = payload["decision"]
    if decision["reasons"] != reasons:
        findings.append(Finding("DECISION_REASONS_MISMATCH", "/decision/reasons"))
    if decision["outcome"] != expected_outcome(reasons):
        findings.append(Finding("DECISION_OUTCOME_MISMATCH", "/decision/outcome"))

    return findings


def validate_payload(payload: Mapping[str, Any]) -> ValidationResult:
    """Validate a parsed cutover assessment."""

    findings = _schema_findings(payload)
    if not findings:
        findings.extend(_semantic_findings(payload))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_file(path: Path) -> ValidationResult:
    """Read and validate one bounded JSON document."""

    payload, findings = _load_payload(path)
    if payload is None:
        return ValidationResult(tuple(sorted(findings)))
    return validate_payload(payload)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate a fixture-only USGS Water API cutover assessment."
    )
    parser.add_argument("path", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    result = validate_file(args.path)
    output = {
        "ok": result.ok,
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "scope": "fixture-only-usgs-water-api-cutover",
        "authority": {
            "source_activation": False,
            "lifecycle_write": False,
            "promotion": False,
            "release": False,
            "publication": False,
        },
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
