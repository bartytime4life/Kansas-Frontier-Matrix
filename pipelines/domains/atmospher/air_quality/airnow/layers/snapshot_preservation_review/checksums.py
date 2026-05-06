import hashlib
from pathlib import Path

def sha256_path(p):
 h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
