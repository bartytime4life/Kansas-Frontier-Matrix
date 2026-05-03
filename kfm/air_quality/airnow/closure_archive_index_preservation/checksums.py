import hashlib
def sha256_bytes(b): return hashlib.sha256(b).hexdigest()
