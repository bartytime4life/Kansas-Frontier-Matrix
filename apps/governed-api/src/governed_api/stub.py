import os
from datetime import datetime, timezone
import re

_STUB_SPEC_HASH = "sha256:" + "a" * 64
_SAFE_CORRELATION_ID = re.compile(r"^[A-Za-z0-9_-]{1,64}$")

# Fixture-only translation profile. These names are local to this proof slice;
# they are not a public registry or a new envelope shape.
_FAILURE_PROFILE = {
    "malformed_input": ("ERROR", "INVALID_REQUEST"),
    "unsupported_scope": ("ABSTAIN", "UNSUPPORTED_SCOPE"),
    "missing_evidence": ("ABSTAIN", "MISSING_EVIDENCE"),
    "policy_denial": ("DENY", "POLICY_DENIED"),
    "stale_dependency": ("ABSTAIN", "SOURCE_STALE"),
    "dependency_unavailable": ("ERROR", "DEPENDENCY_UNAVAILABLE"),
    "timeout": ("ERROR", "REQUEST_TIMEOUT"),
    "cancellation": ("ABSTAIN", "REQUEST_CANCELLED"),
    "internal_defect": ("ERROR", "SAFE_RUNTIME_ERROR"),
}


def _issued_at() -> str:
    return os.getenv("GOVERNED_API_ISSUED_AT") or datetime.now(timezone.utc).isoformat()


def make_abstain_envelope(route: str) -> dict:
    route_id = route.removeprefix("/")
    return {
        "id": f"stub:{route_id}",
        "spec_hash": _STUB_SPEC_HASH,
        "version": "v1-stub",
        "issued_at": _issued_at(),
        "outcome": "ABSTAIN",
        "reason_code": "NOT_IMPLEMENTED",
        "evidence_refs": [],
        "policy_state": "baseline",
        "freshness": "current",
        "correction_state": "none",
    }


def make_error_envelope(error_id: str) -> dict:
    """Return the schema-backed fail-closed ERROR shape used by the scaffold."""

    return {
        "id": f"stub:error:{error_id}",
        "spec_hash": _STUB_SPEC_HASH,
        "version": "v1-stub",
        "issued_at": _issued_at(),
        "outcome": "ERROR",
        "reason_code": "SAFE_RUNTIME_ERROR",
        "evidence_refs": [],
        "policy_state": "unknown_fail_closed",
        "freshness": "unknown_fail_closed",
        "correction_state": "none",
    }


def make_fixture_failure_envelope(kind: str, correlation_id: str) -> dict:
    """Translate one deterministic negative fixture without adding a route.

    The existing RuntimeResponseEnvelope schema has no correlation field.
    The safe fixture identifier is therefore bound to its existing id field,
    and untrusted correlation input is replaced with unavailable.
    """

    try:
        outcome, reason_code = _FAILURE_PROFILE[kind]
    except KeyError as exc:
        raise ValueError(f"unknown fixture failure kind: {kind}") from exc

    candidate = correlation_id.strip() if isinstance(correlation_id, str) else ""
    safe_correlation = candidate if _SAFE_CORRELATION_ID.fullmatch(candidate) else "unavailable"
    policy_state = "denied" if outcome == "DENY" else "unknown_fail_closed"
    freshness = "stale" if kind == "stale_dependency" else "unknown_fail_closed"
    return {
        "id": f"fixture:failure:{kind}:{safe_correlation}",
        "spec_hash": _STUB_SPEC_HASH,
        "version": "v1-stub-fixture",
        "issued_at": _issued_at(),
        "outcome": outcome,
        "reason_code": reason_code,
        "evidence_refs": [],
        "policy_state": policy_state,
        "freshness": freshness,
        "correction_state": "none",
    }
