import os
from datetime import datetime, timezone

_STUB_SPEC_HASH = "sha256:" + "a" * 64


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
