import hashlib
from datetime import datetime, timezone
from .canonical_json import sha256_hex
from .signing_stub import sign_payload


def issue_consent(request: dict) -> dict:
    issued_at = request.get("issued_at") or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    obligations_snapshot_hash = sha256_hex(request["obligations"])
    consent_vc_id = "consent_vc_" + hashlib.sha256(f"{request['subject_id']}|{obligations_snapshot_hash}|{issued_at}".encode()).hexdigest()[:24]
    unsigned = {
        "consent_vc_id": consent_vc_id,
        "obligations_snapshot_hash": obligations_snapshot_hash,
        "issued_at": issued_at,
        "obligations_url": request.get("obligations_url", "policy/consent/ecology.v1.md")
    }
    out = dict(unsigned)
    out["signature"] = sign_payload(unsigned)
    return out
