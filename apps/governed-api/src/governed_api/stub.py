from datetime import datetime, timezone


def make_abstain_envelope(route: str) -> dict:
    issued_at = datetime.now(timezone.utc).isoformat()
    return {
        "id": f"stub:{route}",
        "spec_hash": "stub:abstain",
        "version": "v1-stub",
        "issued_at": issued_at,
        "decision": "ABSTAIN",
        "reason_code": "NOT_IMPLEMENTED",
        "evidence_refs": [],
    }
