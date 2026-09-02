"""Pure semantic checks for fixture-only gate override record candidates."""

from __future__ import annotations

import json
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages" / "hashing" / "src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import JsonInputError, compute_spec_hash, load_json_file

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/gate_override_record.schema.json"
MAX_SCHEMA_FINDINGS = 100


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str
    severity: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    override_id: str | None = None
    spec_hash: str | None = None


def pointer(parts: Sequence[object]) -> str:
    escaped = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(escaped) if escaped else "/"


def identity_subject(candidate: Mapping[str, object]) -> dict[str, object]:
    return {
        key: value
        for key, value in candidate.items()
        if key not in {"override_id", "spec_hash", "attestation"}
    }


def attestation_subject(attestation: Mapping[str, object]) -> dict[str, object]:
    return {key: value for key, value in attestation.items() if key != "signature_value"}


def refresh_identity(document: dict[str, object]) -> None:
    digest = compute_spec_hash(identity_subject(document))
    document["spec_hash"] = digest
    document["override_id"] = f"kfm:gate-override:{digest}"
    attestation = document["attestation"]
    assert isinstance(attestation, dict)
    attestation["subject_digest"] = digest
    attestation["signature_value"] = compute_spec_hash(attestation_subject(attestation))


def outcome(findings: set[Finding]) -> str:
    severities = {finding.severity for finding in findings}
    return (
        "ERROR"
        if "ERROR" in severities
        else "DENY"
        if "DENY" in severities
        else "HOLD"
        if "HOLD" in severities
        else "PASS"
    )


def schema_findings(candidate: Mapping[str, object]) -> set[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema, format_checker=FormatChecker()
                ).iter_errors(candidate),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, ValueError, RecursionError):
        return {Finding("OVERRIDE_SCHEMA_UNAVAILABLE", "/", "ERROR")}
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    errors = sorted(
        errors[:MAX_SCHEMA_FINDINGS],
        key=lambda error: (
            pointer(tuple(error.absolute_path)),
            str(error.validator or "schema"),
        ),
    )
    findings = {
        Finding(
            "OVERRIDE_SCHEMA_INVALID",
            pointer(tuple(error.absolute_path)),
            "DENY",
        )
        for error in errors
    }
    if truncated:
        findings.add(Finding("OVERRIDE_SCHEMA_FINDINGS_TRUNCATED", "/", "ERROR"))
    return findings


def _parse_time(value: object) -> datetime:
    if not isinstance(value, str):
        raise ValueError("time is not a string")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        raise ValueError("time is not timezone aware")
    return parsed


def semantic_findings(candidate: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    add = lambda code, path, severity: findings.add(Finding(code, path, severity))

    expected_hash = compute_spec_hash(identity_subject(candidate))
    if candidate["spec_hash"] != expected_hash:
        add("OVERRIDE_SPEC_HASH_MISMATCH", "/spec_hash", "DENY")
    if candidate["override_id"] != f"kfm:gate-override:{expected_hash}":
        add("OVERRIDE_ID_MISMATCH", "/override_id", "DENY")

    actors = candidate["actors"]
    scope = candidate["scope"]
    validity = candidate["validity"]
    remediation = candidate["remediation"]
    attestation = candidate["attestation"]
    assert isinstance(actors, Mapping)
    assert isinstance(scope, Mapping)
    assert isinstance(validity, Mapping)
    assert isinstance(remediation, Mapping)
    assert isinstance(attestation, Mapping)

    for field in ("evidence_refs", "policy_decision_refs", "review_refs"):
        values = candidate[field]
        assert isinstance(values, list)
        if not values:
            add("OVERRIDE_SUPPORT_INCOMPLETE", f"/{field}", "HOLD")
        elif values != sorted(values):
            add("OVERRIDE_REFERENCE_ORDER_INVALID", f"/{field}", "DENY")

    if actors["separation_required"] and actors["requester_ref"] == actors["approver_ref"]:
        add("OVERRIDE_SELF_APPROVAL_DENIED", "/actors/approver_ref", "DENY")

    if attestation["signer_ref"] != actors["approver_ref"]:
        add("OVERRIDE_SIGNER_APPROVER_MISMATCH", "/attestation/signer_ref", "DENY")
    if attestation["subject_digest"] != expected_hash:
        add("OVERRIDE_ATTESTATION_SUBJECT_MISMATCH", "/attestation/subject_digest", "DENY")
    expected_signature = compute_spec_hash(attestation_subject(attestation))
    if attestation["signature_value"] != expected_signature:
        add("OVERRIDE_FIXTURE_SIGNATURE_MISMATCH", "/attestation/signature_value", "DENY")

    for field in ("operations", "paths"):
        values = scope[field]
        assert isinstance(values, list)
        if values != sorted(values):
            add("OVERRIDE_SCOPE_ORDER_INVALID", f"/scope/{field}", "DENY")

    try:
        created = _parse_time(candidate["created_at"])
        valid_from = _parse_time(validity["valid_from"])
        expires_at = _parse_time(validity["expires_at"])
        due_at = _parse_time(remediation["due_at"])
    except (TypeError, ValueError):
        add("OVERRIDE_TIME_PARSE_ERROR", "/", "ERROR")
    else:
        if valid_from < created:
            add("OVERRIDE_VALIDITY_START_INVALID", "/validity/valid_from", "ERROR")
        if expires_at <= valid_from:
            add("OVERRIDE_VALIDITY_INTERVAL_INVALID", "/validity/expires_at", "ERROR")
        if due_at < created:
            add("OVERRIDE_REMEDIATION_DUE_INVALID", "/remediation/due_at", "ERROR")

    return findings


def validate_document(candidate: object) -> ValidationResult:
    if not isinstance(candidate, Mapping):
        finding = Finding("OVERRIDE_ROOT_TYPE", "/", "DENY")
        return ValidationResult("DENY", (finding,))
    findings = schema_findings(candidate)
    if not findings:
        findings = semantic_findings(candidate)
    return ValidationResult(
        outcome(findings),
        tuple(sorted(findings)),
        candidate.get("override_id") if isinstance(candidate.get("override_id"), str) else None,
        candidate.get("spec_hash") if isinstance(candidate.get("spec_hash"), str) else None,
    )
