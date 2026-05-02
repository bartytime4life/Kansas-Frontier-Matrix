import hashlib
from pathlib import Path

def sha256_path(p):
 h=hashlib.sha256()
 with Path(p).open("rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""):
   h.update(b)
 return h.hexdigest()
