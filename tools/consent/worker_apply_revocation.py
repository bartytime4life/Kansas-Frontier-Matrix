from datetime import datetime, timezone


def apply_revocation(run_receipt: dict, revoke_delta: dict) -> dict:
    return {
        "object_type": "run_receipt",
        "schema_version": "v1",
        "run_id": run_receipt["run_id"] + ".revoked",
        "spec_hash": run_receipt["spec_hash"],
        "artifact_spec_hash": run_receipt["artifact_spec_hash"],
        "consent_vc_id": revoke_delta["consent_vc_id"],
        "revoke_delta_id": revoke_delta["revoke_delta_id"],
        "obligations_snapshot": run_receipt.get("obligations_snapshot", {}),
        "action": "suppress_or_recompute",
        "status": "SUPPRESSED",
        "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    }
