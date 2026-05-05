import hashlib
from .canonical_json import canonical_json

def sha(obj):
    return hashlib.sha256(canonical_json(obj).encode()).hexdigest()
