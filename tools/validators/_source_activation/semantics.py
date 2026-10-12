"""Cross-field semantics for the proposed SourceActivationDecision profile."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime

from .io import Finding, mapping, strings

_BLOCKED_RIGHTS = {"unknown", "noassertion", "denied"}
_REVIEWED_DESCRIPTOR = {"reviewed", "approved"}
_RESTRICTED_SENSITIVITY = {
    "restricted", "sensitive_location", "living_person", "dna_genomic",
    "cultural_sensitive", "infrastructure_sensitive", "steward_controlled",
    "controlled", "unknown_review_required",
}


def _aware(value: object) -> tuple[datetime | None, bool]:
    if not isinstance(value, str):
        return None, False
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None, False
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None, True
    return parsed, False


def _add(findings: list[Finding], code: str, field: str, detail: str) -> None:
    findings.append(Finding(code, field, detail))


def semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    context = mapping(candidate.get("context"))
    decision = mapping(candidate.get("decision"))
    timing = mapping(candidate.get("timing"))
    lineage = mapping(candidate.get("lineage"))

    source_id = candidate.get("source_id")
    version = candidate.get("descriptor_version")
    descriptor_ref = candidate.get("source_descriptor_ref")
    role_ref = candidate.get("source_role_ref")
    if isinstance(source_id, str) and isinstance(version, str):
        expected = f"source-descriptor:{source_id}:{version}"
        if descriptor_ref != expected:
            _add(findings, "SOURCE_DESCRIPTOR_REF_UNBOUND", "/source_descriptor_ref", "descriptor reference is not bound to source and version")
        if isinstance(descriptor_ref, str) and role_ref != f"{descriptor_ref}#/source_role":
            _add(findings, "SOURCE_ROLE_REF_UNBOUND", "/source_role_ref", "role reference is not bound to the descriptor")

    for field, value in (
        ("/source_descriptor_digest", candidate.get("source_descriptor_digest")),
        ("/governance/spec_hash", mapping(candidate.get("governance")).get("spec_hash")),
    ):
        if value == "sha256:" + ("0" * 64):
            _add(findings, "PLACEHOLDER_DIGEST", field, "all-zero digest placeholders are denied")

    parsed: dict[str, datetime] = {}
    for field in ("created_at", "effective_at", "expires_at", "hold_expires_at"):
        timestamp, missing_zone = _aware(timing.get(field))
        if missing_zone:
            _add(findings, "TEMPORAL_TIMEZONE_REQUIRED", f"/timing/{field}", "date-time must include an offset")
        elif timestamp is not None:
            parsed[field] = timestamp
    created = parsed.get("created_at")
    effective = parsed.get("effective_at")
    expires = parsed.get("expires_at")
    hold_expires = parsed.get("hold_expires_at")
    if created and effective and effective < created:
        _add(findings, "EFFECTIVE_TIME_INVALID", "/timing/effective_at", "effective time must not precede creation")
    if effective and expires and expires <= effective:
        _add(findings, "EXPIRY_TIME_INVALID", "/timing/expires_at", "expiry must follow effective time")
    if created and hold_expires and hold_expires <= created:
        _add(findings, "HOLD_EXPIRY_INVALID", "/timing/hold_expires_at", "hold expiry must follow creation")

    decision_id = candidate.get("activation_decision_id")
    supersedes = lineage.get("supersedes")
    superseded_by = lineage.get("superseded_by")
    if isinstance(decision_id, str) and decision_id in {supersedes, superseded_by}:
        _add(findings, "SELF_LINEAGE_REFERENCE", "/lineage", "decision cannot reference itself")
    if isinstance(supersedes, str) and supersedes == superseded_by:
        _add(findings, "LINEAGE_DIRECTION_CONFLICT", "/lineage", "one decision cannot be predecessor and successor")

    route = decision.get("route")
    state = decision.get("activation_state")
    scope = decision.get("activation_scope")
    obligations = strings(decision.get("obligations"))
    policy_refs = strings(decision.get("policy_decision_refs"))
    review_state = decision.get("review_state")
    review_refs = strings(decision.get("review_refs"))
    rights = context.get("rights_status")
    sensitivity = context.get("sensitivity_class")
    access = context.get("access_posture")
    descriptor_review = context.get("descriptor_review_state")
    registry = context.get("registry_state")

    if route == "ADMIT_TO_RAW":
        if rights in _BLOCKED_RIGHTS:
            _add(findings, "ADMIT_RIGHTS_BLOCKED", "/context/rights_status", "admit route requires permitted rights")
        if access in {"closed", "unknown"}:
            _add(findings, "ADMIT_ACCESS_BLOCKED", "/context/access_posture", "admit route requires resolved access")
        if descriptor_review not in _REVIEWED_DESCRIPTOR:
            _add(findings, "ADMIT_DESCRIPTOR_REVIEW_REQUIRED", "/context/descriptor_review_state", "admit route requires reviewed descriptor posture")
        if not policy_refs:
            _add(findings, "ADMIT_POLICY_REFERENCE_REQUIRED", "/decision/policy_decision_refs", "admit route requires policy references")
        if scope == "fixture_only" and state != "fixture_only":
            _add(findings, "FIXTURE_SCOPE_STATE_INVALID", "/decision/activation_state", "fixture-only scope requires fixture-only state")
        if scope == "metadata_only" and state not in {"live_candidate", "live_active"}:
            _add(findings, "METADATA_SCOPE_STATE_INVALID", "/decision/activation_state", "metadata scope requires candidate or active state")
        if scope == "raw_capture":
            if state != "live_active":
                _add(findings, "RAW_CAPTURE_REQUIRES_LIVE_ACTIVE", "/decision/activation_state", "raw capture requires live-active state")
            if review_state != "approved" or not review_refs:
                _add(findings, "RAW_CAPTURE_REQUIRES_APPROVED_REVIEW", "/decision/review_state", "raw capture requires approved review")
            if registry != "active":
                _add(findings, "RAW_CAPTURE_REQUIRES_ACTIVE_REGISTRY", "/context/registry_state", "raw capture requires active registry posture")
            if "require_ingest_receipt" not in obligations:
                _add(findings, "RAW_CAPTURE_RECEIPT_OBLIGATION_MISSING", "/decision/obligations", "raw capture requires an ingest-receipt obligation")
            if sensitivity in _RESTRICTED_SENSITIVITY and review_state != "approved":
                _add(findings, "RAW_CAPTURE_SENSITIVITY_REVIEW_REQUIRED", "/context/sensitivity_class", "restricted sensitivity requires approved review")

    elif route == "QUARANTINE":
        if state != "quarantined":
            _add(findings, "QUARANTINE_STATE_INVALID", "/decision/activation_state", "quarantine route requires quarantined state")
        if scope != "quarantine_only":
            _add(findings, "QUARANTINE_SCOPE_INVALID", "/decision/activation_scope", "quarantine route requires quarantine-only scope")
        if not {"route_to_quarantine", "open_quarantine_case"} <= obligations:
            _add(findings, "QUARANTINE_OBLIGATION_MISSING", "/decision/obligations", "quarantine route requires routing and case obligations")

    elif route == "HOLD":
        if state not in {"disabled", "live_candidate"}:
            _add(findings, "HOLD_STATE_INVALID", "/decision/activation_state", "hold route requires disabled or candidate state")
        if scope != "none":
            _add(findings, "HOLD_SCOPE_INVALID", "/decision/activation_scope", "hold route cannot grant scope")
        if review_state != "pending" or not review_refs:
            _add(findings, "HOLD_REVIEW_REQUIRED", "/decision/review_state", "hold route requires pending reviewer routing")
        if timing.get("hold_expires_at") is None:
            _add(findings, "HOLD_EXPIRY_REQUIRED", "/timing/hold_expires_at", "hold route requires expiry")
        if "set_hold_expiry" not in obligations:
            _add(findings, "HOLD_EXPIRY_OBLIGATION_MISSING", "/decision/obligations", "hold route requires expiry obligation")

    elif route == "DENY_INTAKE":
        if state not in {"disabled", "retired"}:
            _add(findings, "DENY_STATE_INVALID", "/decision/activation_state", "denied intake requires disabled or retired state")
        if scope != "none":
            _add(findings, "DENY_SCOPE_INVALID", "/decision/activation_scope", "denied intake cannot grant scope")

    elif route == "ERROR":
        if state != "disabled":
            _add(findings, "ERROR_STATE_INVALID", "/decision/activation_state", "error route requires disabled state")
        if scope != "none":
            _add(findings, "ERROR_SCOPE_INVALID", "/decision/activation_scope", "error route cannot grant scope")

    if route != "HOLD" and timing.get("hold_expires_at") is not None:
        _add(findings, "UNEXPECTED_HOLD_EXPIRY", "/timing/hold_expires_at", "hold expiry is only valid for HOLD")
    operation = candidate.get("operation")
    if operation == "retirement" and (route != "DENY_INTAKE" or state != "retired"):
        _add(findings, "RETIREMENT_ROUTE_INVALID", "/operation", "retirement requires denied intake and retired state")
    if operation == "deactivation" and route not in {"DENY_INTAKE", "HOLD", "ERROR"}:
        _add(findings, "DEACTIVATION_ROUTE_INVALID", "/operation", "deactivation cannot admit to RAW")
    return findings
