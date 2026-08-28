"""Semantic review rules and finite outcome classification."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

from .model import (
    ERROR_CODES,
    FALSE_EFFECTS,
    Finding,
    ValidationResult,
    canonical_spec_hash,
    expected_review_id,
    read_object,
    schema_findings,
)


def _canonical(values: Any) -> bool:
    return (
        isinstance(values, list)
        and bool(values)
        and all(isinstance(value, str) for value in values)
        and values == sorted(set(values))
    )


def _datetime(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(
            value[:-1] + "+00:00" if value.endswith("Z") else value
        )
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    arrays = (
        "related_contexts",
        "object_family_refs",
        "public_api_resource_refs",
        "internal_aliases",
        "evidence_refs",
        "source_refs",
        "limitations",
    )
    for key in arrays:
        if not _canonical(candidate.get(key)):
            findings.append(Finding("NONCANONICAL_REFERENCE_ARRAY", f"/{key}"))

    related = candidate.get("related_contexts")
    if isinstance(related, list) and candidate.get("owning_context") in related:
        findings.append(Finding("OWNING_CONTEXT_SELF_REFERENCE", "/related_contexts"))

    term = candidate.get("public_term")
    aliases = candidate.get("internal_aliases")
    if isinstance(term, str) and isinstance(aliases, list) and any(
        isinstance(alias, str) and alias.casefold() == term.casefold()
        for alias in aliases
    ):
        findings.append(Finding("PUBLIC_TERM_ALIAS_COLLISION", "/internal_aliases"))

    stability = candidate.get("stability")
    kind = candidate.get("change_kind")
    migration = candidate.get("migration_ref")
    window = candidate.get("compatibility_window")
    if kind in {"BREAKING", "DEPRECATION"}:
        if migration is None:
            findings.append(Finding("MIGRATION_REQUIRED", "/migration_ref"))
        if window is None:
            findings.append(
                Finding("COMPATIBILITY_WINDOW_REQUIRED", "/compatibility_window")
            )
    else:
        if migration is not None:
            findings.append(Finding("MIGRATION_NOT_ALLOWED", "/migration_ref"))
        if window is not None:
            findings.append(
                Finding("COMPATIBILITY_WINDOW_NOT_ALLOWED", "/compatibility_window")
            )

    if isinstance(window, Mapping):
        start = _datetime(window.get("starts_at"))
        end = _datetime(window.get("ends_at"))
        if start is None or end is None or start >= end:
            findings.append(
                Finding("COMPATIBILITY_WINDOW_INVALID", "/compatibility_window")
            )

    if (stability == "DEPRECATED") != (kind == "DEPRECATION"):
        findings.append(Finding("DEPRECATION_STATE_MISMATCH", "/stability"))
    if candidate.get("decision") != "HOLD":
        findings.append(Finding("DECISION_OVERCLAIM", "/decision"))
    if candidate.get("adoption_ref") is not None:
        findings.append(Finding("ADOPTION_OVERCLAIM", "/adoption_ref"))
    if candidate.get("public_use_allowed") is not False:
        findings.append(Finding("PUBLIC_USE_OVERCLAIM", "/public_use_allowed"))
    if candidate.get("effects") != FALSE_EFFECTS:
        findings.append(Finding("EFFECT_OVERCLAIM", "/effects"))

    try:
        expected_hash = canonical_spec_hash(candidate)
        expected_id = expected_review_id(candidate)
    except RuntimeError:
        findings.append(Finding("HASHING_UNAVAILABLE", "/spec_hash"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("review_id") != expected_id:
            findings.append(
                Finding("PUBLISHED_LANGUAGE_REVIEW_ID_MISMATCH", "/review_id")
            )
    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = schema_findings(candidate)
    if not findings:
        findings.extend(semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    if not ordered:
        return ValidationResult("PASS", ordered)
    outcome = "ERROR" if any(item.code in ERROR_CODES for item in ordered) else "DENY"
    return ValidationResult(outcome, ordered)


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = read_object(path)
    if candidate is None:
        return ValidationResult("ERROR", tuple(sorted(set(findings))))
    return validate_payload(candidate)
