import os
from datetime import datetime, timezone


def make_abstain_envelope(route: str) -> dict:
    issued_at = os.getenv("GOVERNED_API_ISSUED_AT") or datetime.now(timezone.utc).isoformat()
    route_id = route.removeprefix("/")
    return {
        "id": f"stub:{route_id}",
        "decision_id": f"stub:{route_id}",
        "spec_hash": "sha256:" + "0" * 64,
        "version": "v1-stub",
        "issued_at": issued_at,
        "evaluated_at": issued_at,
        "decision": "ABSTAIN",
        "outcome": "ABSTAIN",
        "policy_family": "capability",
        "reason_code": "NOT_IMPLEMENTED",
        "reasons": ["Route is scaffolded but not implemented"],
        "obligations": [],
        "evidence_refs": [],
    }
