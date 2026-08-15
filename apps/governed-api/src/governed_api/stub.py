import os
from datetime import datetime, timezone

_STUB_SPEC_HASH = "sha256:" + "a" * 64


def make_abstain_envelope(route: str) -> dict:
    issued_at = os.getenv("GOVERNED_API_ISSUED_AT") or datetime.now(timezone.utc).isoformat()
    route_id = route.removeprefix("/")
    return {
        "id": f"stub:{route_id}",
        "spec_hash": _STUB_SPEC_HASH,
        "version": "v1-stub",
        "issued_at": issued_at,
        "outcome": "ABSTAIN",
        "reason_code": "NOT_IMPLEMENTED",
        "evidence_refs": [],
        "policy_state": "baseline",
        "freshness": "current",
        "correction_state": "none",
    }
