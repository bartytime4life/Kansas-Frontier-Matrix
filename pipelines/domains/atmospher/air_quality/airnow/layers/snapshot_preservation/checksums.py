import hashlib
from pathlib import Path
def sha256_bytes(b): return hashlib.sha256(b).hexdigest()
def sha256_path(p): return sha256_bytes(Path(p).read_bytes())
