"""Build a bounded DecisionEnvelope candidate for Evidence Drawer admission.

This adapter is an anticorruption boundary between the renderer-neutral
MapContextEnvelope and the public-safe EvidenceDrawerPayload. It checks only
explicit, already-declared context and trust fields. It does not resolve
EvidenceRefs, evaluate policy, authenticate callers or reviewers, establish
release state, authorize public use, or publish anything.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
import re
from typing import Final

from .runtime_response import EnvelopeBuildError


MAP_CONTEXT_PROFILE: Final[str] = "kfm.ui.map-context-envelope.v1"
DRAWER_PROFILE: Final[str] = "kfm.explorer.evidence-drawer.public-safe.v1"
ADAPTER_VERSION: Final[str] = "1.0.0"

_OUTCOMES: Final[frozenset[str]] = frozenset(
    {"ANSWER", "ABSTAIN", "DENY", "ERROR"}
)
_CALLER_ROLES: Final[frozenset[str]] = frozenset(
    {"PUBLIC_USER", "AUTHENTICATED_USER", "STEWARD", "REVIEWER", "SYSTEM_TEST"}
)
_PUBLIC_CALLER_ROLES: Final[frozenset[str]] = frozenset(
    {"PUBLIC_USER", "AUTHENTICATED_USER", "STEWARD", "REVIEWER"}
)
_CONTEXT_GOVERNANCE_FIELDS: Final[frozenset[str]] = frozenset(
    {
        "canonical_store_accessed",
        "raw_work_quarantine_accessed",
        "renderer_specific_state_included",
        "evidence_closure_created",
        "policy_authority_created",
        "release_authority_created",
        "public_use_authorized",
        "repository_mutated",
    }
)
_DECISION_ID_RE: Final[re.Pattern[str]] = re.compile(r"^[a-z][a-z0-9_:.-]*$")
_UTC_RE: Final[re.Pattern[str]] = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$"
)
_SAFE_REF_RE: Final[re.Pattern[str]] = re.compile(
    r"^[A-Za-z0-9][A-Za-z0-9._~:/#?=&%+@-]{0,319}$"
)
_DENIED_REF_PREFIXES: Final[tuple[str, ...]] = (
    "raw:",
    "work:",
    "quarantine:",
    "canonical:",
    "internal:",
    "proof:",
    "model:",
    "direct-model:",
)

_REASON_TEXT: Final[dict[str, str]] = {
    "SUPPORTED": "drawer payload admitted",
    "CONTEXT_EXPIRED": "map context expired before admission",
    "CONTEXT_TIME_INCONSISTENT": "map context time is inconsistent",
    "CONTEXT_GOVERNANCE_INVALID": "map context governance boundary is invalid",
    "CALLER_ROLE_DENIED": "caller role is not admitted for this adapter",
    "CALLER_ROLE_INVALID": "caller role is invalid",
    "SELECTION_REQUIRED": "one selected feature is required",
    "SELECTION_AMBIGUOUS": "more than one selected feature is ambiguous",
    "SELECTED_LAYER_UNRESOLVED": "selected layer could not be resolved",
    "SELECTED_LAYER_NOT_PUBLISHED": "selected layer is not declared published",
    "SELECTED_RELEASE_UNBOUND": "selected layer release is not bound to context",
    "SELECTION_EVIDENCE_UNBOUND": "selected evidence is not bound to context",
    "DRAWER_EVIDENCE_OUTSIDE_SELECTION": "drawer evidence is outside the selected feature",
    "DRAWER_TRUST_STATE_MISMATCH": "drawer trust state does not match its outcome",
    "DRAWER_PAYLOAD_INVALID": "drawer payload has an invalid finite outcome surface",
    "MISSING_EVIDENCE": "drawer payload requires abstention",
    "STALE_EVIDENCE": "drawer payload requires abstention",
    "CITATION_UNRESOLVED": "drawer payload requires abstention",
    "RIGHTS_UNRESOLVED": "drawer payload requires abstention",
    "HELD_EVIDENCE": "drawer payload requires abstention",
    "SUPERSEDED_EVIDENCE": "drawer payload requires abstention",
    "WITHDRAWN_EVIDENCE": "drawer payload requires abstention",
    "REVOKED_EVIDENCE": "drawer payload requires abstention",
    "POLICY_DENIED": "drawer payload denied",
    "SENSITIVE_DETAIL_RESTRICTED": "drawer payload denied",
    "UPSTREAM_ERROR": "drawer payload reported an upstream error",
}

_OBLIGATIONS: Final[dict[str, tuple[str, ...]]] = {
    "ANSWER": ("DISPLAY_CITATIONS", "PRESERVE_LIMITATIONS"),
    "ABSTAIN": ("DISPLAY_ABSTENTION",),
    "DENY": ("DISPLAY_SAFE_DENIAL",),
    "ERROR": ("DISPLAY_SAFE_ERROR",),
}


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _array(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        return list(value)
    return []


def _parse_utc(value: object, field: str) -> tuple[str, datetime]:
    if not isinstance(value, str) or _UTC_RE.fullmatch(value) is None:
        raise EnvelopeBuildError("DATETIME_INVALID", field)
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise EnvelopeBuildError("DATETIME_INVALID", field) from exc
    return value, parsed.astimezone(timezone.utc)


def _require_decision_id(value: object) -> str:
    if not isinstance(value, str) or _DECISION_ID_RE.fullmatch(value) is None:
        raise EnvelopeBuildError("DECISION_ID_INVALID", "decision_id")
    return value


def _canonical_refs(value: object) -> list[str] | None:
    items = _array(value)
    if not all(isinstance(item, str) for item in items):
        return None
    refs = [item for item in items if isinstance(item, str)]
    if refs != sorted(set(refs)):
        return None
    if any(
        _SAFE_REF_RE.fullmatch(item) is None
        or item.casefold().startswith(_DENIED_REF_PREFIXES)
        for item in refs
    ):
        return None
    return refs


def _decision(
    *,
    decision_id: str,
    evaluated_at: str,
    outcome: str,
    reason_code: str,
    evidence_refs: Sequence[str] = (),
) -> dict[str, object]:
    if outcome not in _OUTCOMES:
        raise EnvelopeBuildError("OUTCOME_INVALID", "outcome")
    safe_reason = _REASON_TEXT.get(reason_code)
    if safe_reason is None:
        # Never echo an attacker-controlled reason into the envelope.
        outcome = "ERROR"
        reason_code = "DRAWER_PAYLOAD_INVALID"
        safe_reason = _REASON_TEXT[reason_code]
        evidence_refs = ()
    safe_refs = (
        sorted(set(evidence_refs))
        if outcome in {"ANSWER", "ABSTAIN"}
        else []
    )
    return {
        "decision_id": decision_id,
        "id": decision_id,
        "outcome": outcome,
        "decision": outcome,
        "policy_family": "render",
        "reason_code": reason_code,
        "reasons": [safe_reason],
        "obligations": list(_OBLIGATIONS[outcome]),
        "evidence_refs": safe_refs,
        "evaluated_at": evaluated_at,
        "issued_at": evaluated_at,
        "version": ADAPTER_VERSION,
    }


def _trust_matches(
    outcome: str,
    reason_code: str,
    trust: Mapping[str, object],
    refs: Sequence[str],
    citations: Sequence[object],
    history: object,
) -> bool:
    policy = trust.get("policy")
    if outcome == "ANSWER":
        return (
            reason_code == "SUPPORTED"
            and bool(refs)
            and bool(citations)
            and policy == "ALLOW"
            and trust.get("review") == "REVIEWED"
            and trust.get("release") == "RELEASED"
            and trust.get("freshness") == "CURRENT"
            and trust.get("correction") != "SUPERSEDED"
        )
    if outcome == "ABSTAIN":
        return reason_code != "SUPPORTED" and policy == "ABSTAIN"
    if outcome == "DENY":
        return (
            reason_code in {
                "POLICY_DENIED",
                "RIGHTS_UNRESOLVED",
                "SENSITIVE_DETAIL_RESTRICTED",
            }
            and policy == "DENY"
            and not refs
            and not citations
            and not history
        )
    if outcome == "ERROR":
        return (
            reason_code == "UPSTREAM_ERROR"
            and policy == "ERROR"
            and not refs
            and not citations
            and not history
        )
    return False


def build_map_context_evidence_drawer_admission_candidate(
    *,
    decision_id: str,
    evaluated_at: str,
    map_context: Mapping[str, object],
    drawer_payload: Mapping[str, object],
    allow_system_test: bool = False,
) -> dict[str, object]:
    """Build one non-authoritative render-admission DecisionEnvelope candidate.

    Inputs are expected to have passed their authoritative repository validators.
    This helper repeats only the cross-object checks required to keep a selected
    map feature, its released layer, and a public-safe drawer projection aligned.
    """

    checked_id = _require_decision_id(decision_id)
    checked_time, evaluated = _parse_utc(evaluated_at, "evaluated_at")

    if not isinstance(map_context, Mapping):
        raise EnvelopeBuildError("MAP_CONTEXT_NOT_OBJECT", "map_context")
    if not isinstance(drawer_payload, Mapping):
        raise EnvelopeBuildError("DRAWER_PAYLOAD_NOT_OBJECT", "drawer_payload")
    if map_context.get("profile") != MAP_CONTEXT_PROFILE:
        raise EnvelopeBuildError("MAP_CONTEXT_PROFILE_INVALID", "map_context.profile")
    if drawer_payload.get("profile") != DRAWER_PROFILE:
        raise EnvelopeBuildError("DRAWER_PROFILE_INVALID", "drawer_payload.profile")

    _, assembled = _parse_utc(map_context.get("assembled_at"), "map_context.assembled_at")
    _, expires = _parse_utc(map_context.get("expires_at"), "map_context.expires_at")
    if expires <= assembled or evaluated < assembled:
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ERROR",
            reason_code="CONTEXT_TIME_INCONSISTENT",
        )
    if evaluated > expires:
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ABSTAIN",
            reason_code="CONTEXT_EXPIRED",
        )

    governance = _mapping(map_context.get("governance"))
    if set(governance) != _CONTEXT_GOVERNANCE_FIELDS or any(
        governance.get(field) is not False
        for field in _CONTEXT_GOVERNANCE_FIELDS
    ):
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ERROR",
            reason_code="CONTEXT_GOVERNANCE_INVALID",
        )

    caller_role = map_context.get("caller_role")
    if caller_role not in _CALLER_ROLES:
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ERROR",
            reason_code="CALLER_ROLE_INVALID",
        )
    if caller_role == "SYSTEM_TEST" and not allow_system_test:
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="DENY",
            reason_code="CALLER_ROLE_DENIED",
        )
    if caller_role not in _PUBLIC_CALLER_ROLES and caller_role != "SYSTEM_TEST":
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="DENY",
            reason_code="CALLER_ROLE_DENIED",
        )

    selections = _array(map_context.get("selections"))
    if not selections:
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ABSTAIN",
            reason_code="SELECTION_REQUIRED",
        )
    if len(selections) != 1:
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ABSTAIN",
            reason_code="SELECTION_AMBIGUOUS",
        )

    selection = _mapping(selections[0])
    selected_layer_id = selection.get("layer_id")
    selected_refs = _canonical_refs(selection.get("evidence_refs"))
    context_refs = _canonical_refs(map_context.get("evidence_refs"))
    release_refs = _canonical_refs(map_context.get("release_refs"))
    if (
        not isinstance(selected_layer_id, str)
        or selected_refs is None
        or context_refs is None
        or release_refs is None
        or not selected_refs
    ):
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ERROR",
            reason_code="SELECTION_EVIDENCE_UNBOUND",
        )
    if not set(selected_refs).issubset(context_refs):
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ERROR",
            reason_code="SELECTION_EVIDENCE_UNBOUND",
        )

    layers = [
        _mapping(item)
        for item in _array(map_context.get("layers"))
        if isinstance(item, Mapping)
    ]
    matched_layers = [
        layer for layer in layers if layer.get("layer_id") == selected_layer_id
    ]
    if len(matched_layers) != 1:
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ERROR",
            reason_code="SELECTED_LAYER_UNRESOLVED",
        )
    selected_layer = matched_layers[0]
    if selected_layer.get("release_state") != "PUBLISHED":
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ERROR",
            reason_code="SELECTED_LAYER_NOT_PUBLISHED",
        )
    selected_release_ref = selected_layer.get("release_ref")
    if (
        not isinstance(selected_release_ref, str)
        or selected_release_ref not in release_refs
    ):
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ERROR",
            reason_code="SELECTED_RELEASE_UNBOUND",
        )

    outcome = drawer_payload.get("outcome")
    reason_code = drawer_payload.get("reason_code")
    drawer_refs = _canonical_refs(drawer_payload.get("evidence_refs"))
    citations = _array(drawer_payload.get("citations"))
    trust = _mapping(drawer_payload.get("trust_state"))
    history = drawer_payload.get("history")
    if (
        outcome not in _OUTCOMES
        or not isinstance(reason_code, str)
        or reason_code not in _REASON_TEXT
        or drawer_refs is None
    ):
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ERROR",
            reason_code="DRAWER_PAYLOAD_INVALID",
        )

    if not _trust_matches(
        outcome,
        reason_code,
        trust,
        drawer_refs,
        citations,
        history,
    ):
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ERROR",
            reason_code="DRAWER_TRUST_STATE_MISMATCH",
        )

    if outcome in {"ANSWER", "ABSTAIN"} and not set(drawer_refs).issubset(
        selected_refs
    ):
        return _decision(
            decision_id=checked_id,
            evaluated_at=checked_time,
            outcome="ERROR",
            reason_code="DRAWER_EVIDENCE_OUTSIDE_SELECTION",
        )

    return _decision(
        decision_id=checked_id,
        evaluated_at=checked_time,
        outcome=outcome,
        reason_code=reason_code,
        evidence_refs=drawer_refs,
    )


__all__ = [
    "ADAPTER_VERSION",
    "DRAWER_PROFILE",
    "MAP_CONTEXT_PROFILE",
    "build_map_context_evidence_drawer_admission_candidate",
]
