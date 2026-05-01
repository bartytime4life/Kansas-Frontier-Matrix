import hmac
import hashlib
from .canonical_json import canonical_json_bytes

STUB_KEY = b"kfm-local-signing-stub-v1"


def sign_payload(payload: dict) -> str:
    return "stubsig_" + hmac.new(STUB_KEY, canonical_json_bytes(payload), hashlib.sha256).hexdigest()
