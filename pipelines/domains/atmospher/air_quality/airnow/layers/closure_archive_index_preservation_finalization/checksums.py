from hashlib import sha256
from pathlib import Path
def sha256_path(p):
 h=sha256()
 with Path(p).open("rb") as f:
  for c in iter(lambda:f.read(65536),b""): h.update(c)
 return h.hexdigest()
