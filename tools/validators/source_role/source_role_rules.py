"""Finite source-role anti-collapse and claim-compatibility rules."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from .source_role_core import (
    CASES_PATH,
    BASE_PATH,
    DuplicateKeyError,
    Evaluation,
    Finding,
    NonFiniteNumberError,
    descriptor_validator,
    descriptor_vocabularies,
    expected_request_id,
    load_json,
    report_for,
    request_validator,
    schema_findings,
    sorted_unique_strings,
)

OUTCOME_PRECEDENCE = {"PASS": 0, "ABSTAIN": 1, "RESTRICT": 2, "HOLD": 3, "DENY": 4, "ERROR": 5}
PUBLIC_SAFE_SENSITIVITY = frozenset({"public", "low"})
PUBLIC_DENIED_ROLES = frozenset({"candidate_signal", "fixture_only"})
PRIMARY_CLAIM_ROLES = frozenset({"identity", "legal_status", "observed_event", "observation", "occurrence"})
WEAK_CONFIDENCE = frozenset({"corroborate_before_claim", "context_only", "candidate_only", "fixture_only", "unknown"})
ROLE_RANK_COMPATIBILITY = {
    "authoritative_for_claim": frozenset({"authoritative_for_role", "primary_authority"}),
    "regulatory_context": frozenset({"authoritative_for_role", "regulatory_authority", "contextual"}),
    "legal_context": frozenset({"authoritative_for_role", "legal_authority", "contextual"}),
    "observation": frozenset({"authoritative_for_role", "primary_authority", "corroborating"}),
    "occurrence_evidence": frozenset({"authoritative_for_role", "primary_authority", "corroborating"}),
    "aggregator": frozenset({"aggregator"}),
    "operational_context": frozenset({"authoritative_for_role", "contextual"}),
    "remote_sensing_observation": frozenset({"authoritative_for_role", "primary_authority", "corroborating"}),
    "model_context": frozenset({"derived", "contextual"}),
    "candidate_signal": frozenset({"candidate_only"}),
    "historical_context": frozenset({"primary_authority", "corroborating", "contextual"}),
    "corroborating_context": frozenset({"corroborating", "contextual"}),
    "derived_public_product": frozenset({"derived"}),
    "steward_review_source": frozenset({"steward_authority"}),
    "citation_source": frozenset({"corroborating", "contextual"}),
    "fixture_only": frozenset({"fixture_only"}),
}


def _add(findings: list[Finding], code: str, field: str, outcome: str) -> None:
    findings.append(Finding(code, field, outcome.lower()))


def _outcome(findings: list[Finding]) -> str:
    if not findings:
        return "PASS"
    return max((finding.severity.upper() for finding in findings), key=lambda item: OUTCOME_PRECEDENCE[item])


def evaluate_document(packet: Mapping[str, Any]) -> Evaluation:
    request_errors = schema_findings(request_validator(), packet, "REQUEST_SCHEMA_INVALID", "")
    descriptor = packet.get("descriptor")
    if isinstance(descriptor, dict):
        descriptor_errors = schema_findings(descriptor_validator(), descriptor, "SOURCE_DESCRIPTOR_SCHEMA_INVALID", "/descriptor")
    else:
        descriptor_errors = [Finding("SOURCE_DESCRIPTOR_SCHEMA_INVALID", "/descriptor", "error")]
    schema_errors = request_errors + descriptor_errors
    if schema_errors:
        outcome = "ERROR"
        return Evaluation(outcome, tuple(sorted(set(schema_errors))), report_for(packet, outcome, schema_errors))

    findings: list[Finding] = []
    use = packet["use"]
    assert isinstance(use, dict) and isinstance(descriptor, dict)

    # Canonical arrays are part of deterministic identity and reviewability.
    if not sorted_unique_strings(use.get("requested_claim_roles"), allow_empty=False):
        _add(findings, "CANONICAL_ORDER_REQUIRED", "/use/requested_claim_roles", "ERROR")
    support = use.get("support_refs")
    if isinstance(support, dict):
        for key, value in support.items():
            if not sorted_unique_strings(value):
                _add(findings, "CANONICAL_ORDER_REQUIRED", f"/use/support_refs/{key}", "ERROR")
    role_change = use.get("role_change")
    if isinstance(role_change, dict) and not sorted_unique_strings(role_change.get("lineage_refs")):
        _add(findings, "CANONICAL_ORDER_REQUIRED", "/use/role_change/lineage_refs", "ERROR")

    if use.get("request_id") != expected_request_id(packet):
        _add(findings, "REQUEST_ID_MISMATCH", "/use/request_id", "ERROR")

    if use.get("source_id") != descriptor.get("source_id"):
        _add(findings, "SOURCE_ID_MISMATCH", "/use/source_id", "DENY")
    if use.get("descriptor_version") != descriptor.get("descriptor_version"):
        _add(findings, "DESCRIPTOR_VERSION_MISMATCH", "/use/descriptor_version", "DENY")

    origin = use.get("role_origin")
    if origin == "AI_INFERRED":
        _add(findings, "SOURCE_ROLE_AI_INFERRED_DENIED", "/use/role_origin", "DENY")
    elif origin != "SOURCE_DESCRIPTOR":
        _add(findings, "SOURCE_ROLE_UNSUPPORTED", "/use/role_origin", "DENY")

    vocab = descriptor_vocabularies()
    propagated_role = use.get("propagated_source_role")
    propagated_rank = use.get("propagated_authority_rank")
    requested_roles = use.get("requested_claim_roles", [])
    if propagated_role not in vocab["source_role"]:
        _add(findings, "SOURCE_ROLE_UNSUPPORTED", "/use/propagated_source_role", "DENY")
    if propagated_rank not in vocab["authority_rank"]:
        _add(findings, "AUTHORITY_RANK_UNSUPPORTED", "/use/propagated_authority_rank", "DENY")
    for index, claim_role in enumerate(requested_roles):
        if claim_role not in vocab["claim_role"]:
            _add(findings, "CLAIM_ROLE_UNSUPPORTED", f"/use/requested_claim_roles/{index}", "DENY")

    descriptor_role = descriptor.get("source_role")
    descriptor_rank = descriptor.get("authority_rank")
    changed = propagated_role != descriptor_role or propagated_rank != descriptor_rank
    kind = role_change.get("kind") if isinstance(role_change, dict) else None
    lineage = role_change.get("lineage_refs", []) if isinstance(role_change, dict) else []
    if changed:
        if kind == "NONE" or not lineage:
            _add(findings, "SOURCE_ROLE_COLLAPSE_DENIED", "/use", "DENY")
            if not lineage:
                _add(findings, "ROLE_LINEAGE_MISSING", "/use/role_change/lineage_refs", "DENY")
        else:
            _add(findings, "SOURCE_ROLE_VALIDATOR_HOLD", "/use/role_change", "HOLD")
    elif kind != "NONE":
        _add(findings, "ROLE_CHANGE_WITHOUT_DELTA", "/use/role_change/kind", "ERROR")
    elif lineage:
        _add(findings, "ROLE_LINEAGE_NOT_ALLOWED", "/use/role_change/lineage_refs", "ERROR")

    allowed_ranks = ROLE_RANK_COMPATIBILITY.get(str(descriptor_role), frozenset())
    if descriptor_rank not in allowed_ranks:
        _add(findings, "SOURCE_ROLE_AUTHORITY_MISMATCH", "/descriptor/authority_rank", "DENY")

    admissibility = descriptor.get("admissibility_limits", {})
    allowed_claims = set(admissibility.get("allowed_claim_roles", [])) if isinstance(admissibility, dict) else set()
    prohibited_claims = set(admissibility.get("prohibited_claim_roles", [])) if isinstance(admissibility, dict) else set()
    if any(role not in allowed_claims or role in prohibited_claims for role in requested_roles):
        _add(findings, "CLAIM_ROLE_INCOMPATIBLE", "/use/requested_claim_roles", "DENY")

    authority_claims = use.get("authority_claims", {})
    if isinstance(authority_claims, dict) and any(value is True for value in authority_claims.values()):
        _add(findings, "SOURCE_ROLE_OVERCLAIM", "/use/authority_claims", "DENY")

    rights = descriptor.get("rights", {})
    rights_status = rights.get("rights_status") if isinstance(rights, dict) else None
    exposure = use.get("exposure")
    sensitivity = descriptor.get("sensitivity_default")
    public_release = descriptor.get("public_release", {})
    review_state = descriptor.get("review_state")
    release_state = descriptor.get("release_state")
    confidence = admissibility.get("confidence_posture") if isinstance(admissibility, dict) else None

    if rights_status == "denied":
        _add(findings, "ROLE_POLICY_OR_REVIEW_GAP", "/descriptor/rights/rights_status", "DENY")
    elif rights_status in {"unknown", "noassertion"}:
        if exposure == "PUBLIC":
            _add(findings, "PUBLIC_SURFACE_LEAKAGE_DENIED", "/use/exposure", "DENY")
        else:
            _add(findings, "ROLE_POLICY_OR_REVIEW_GAP", "/descriptor/rights/rights_status", "HOLD")

    if exposure == "PUBLIC":
        if (
            public_release.get("allowed") is not True
            or sensitivity not in PUBLIC_SAFE_SENSITIVITY
            or descriptor_role in PUBLIC_DENIED_ROLES
            or confidence in {"candidate_only", "fixture_only", "unknown"}
        ):
            _add(findings, "PUBLIC_SURFACE_LEAKAGE_DENIED", "/use/exposure", "DENY")
        if review_state not in {"reviewed", "approved"}:
            _add(findings, "ROLE_POLICY_OR_REVIEW_GAP", "/descriptor/review_state", "HOLD")
        if release_state != "released":
            _add(findings, "ROLE_RELEASE_REFERENCE_MISSING", "/descriptor/release_state", "HOLD")
        assert isinstance(support, dict)
        if not support.get("evidence_refs"):
            _add(findings, "ROLE_EVIDENCE_GAP", "/use/support_refs/evidence_refs", "HOLD")
        if not support.get("policy_decision_refs") or not support.get("review_refs"):
            _add(findings, "ROLE_POLICY_OR_REVIEW_GAP", "/use/support_refs", "HOLD")
        if not support.get("release_manifest_refs") or not support.get("correction_refs") or not support.get("rollback_refs"):
            _add(findings, "ROLE_RELEASE_REFERENCE_MISSING", "/use/support_refs", "HOLD")
    elif exposure in {"INTERNAL", "STEWARD"} and (
        rights_status in {"verified_restricted", "permission_required"}
        or sensitivity not in PUBLIC_SAFE_SENSITIVITY
    ):
        _add(findings, "SOURCE_ROLE_VALIDATOR_RESTRICT", "/use/exposure", "RESTRICT")

    if confidence in WEAK_CONFIDENCE and PRIMARY_CLAIM_ROLES.intersection(requested_roles):
        _add(findings, "SOURCE_ROLE_VALIDATOR_ABSTAIN", "/descriptor/admissibility_limits/confidence_posture", "ABSTAIN")

    outcome = _outcome(findings)
    unique = tuple(sorted(set(findings)))
    return Evaluation(outcome, unique, report_for(packet, outcome, unique))


def evaluate_path(path: Path) -> Evaluation:
    try:
        return evaluate_document(load_json(path))
    except (json.JSONDecodeError, DuplicateKeyError, NonFiniteNumberError):
        findings = (Finding("INPUT_JSON_INVALID", "/", "error"),)
    except (OSError, UnicodeError, ValueError, RecursionError):
        findings = (Finding("INPUT_INVALID", "/", "error"),)
    return Evaluation("ERROR", findings, report_for(None, "ERROR", findings))
