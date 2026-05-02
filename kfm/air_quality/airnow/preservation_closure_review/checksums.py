import hashlib
from pathlib import Path

def sha256_path(p):
 return hashlib.sha256(Path(p).read_bytes()).hexdigest()
