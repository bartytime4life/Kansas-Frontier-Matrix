import hashlib
from .canonical_json import canonical_json

def sign_local(obj_without_signature):
    return "local-stub:" + hashlib.sha256(canonical_json(obj_without_signature).encode()).hexdigest()
