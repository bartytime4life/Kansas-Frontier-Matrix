import hashlib
from pathlib import Path

def sha256_path(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()
