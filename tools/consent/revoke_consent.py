import hmac
import hashlib
from .signing_stub import sign_payload


def _derive_key(token: str) -> bytes:
    prk = hmac.new(b"kfm:revoke:v1", token.encode("utf-8"), hashlib.sha256).digest()
    return hmac.new(prk, b"kfm:revoke:v1:id", hashlib.sha256).digest()


def revoke_consent(request: dict) -> dict:
    token = request.get("revocation_token")
    if not token and not request.get("revoke_vc_jwt"):
        raise ValueError("revocation_token or revoke_vc_jwt is required")
    key = _derive_key(token if token else request["revoke_vc_jwt"])
    message = f"{request['prior_spec_hash']}|{request['delta_timestamp']}".encode("utf-8")
    revoke_delta_id = "rvk_" + hmac.new(key, message, hashlib.sha256).hexdigest()
    unsigned = {
        "object_type": "RevokeDelta",
        "schema_version": "v1",
        "revoke_delta_id": revoke_delta_id,
        "consent_vc_id": request["consent_vc_id"],
        "prior_spec_hash": request["prior_spec_hash"],
        "delta_timestamp": request["delta_timestamp"],
        "obligations_action": "suppress_or_recompute"
    }
    out = dict(unsigned)
    out["signature"] = sign_payload(unsigned)
    return out
