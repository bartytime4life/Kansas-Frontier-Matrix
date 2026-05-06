import hashlib
from pathlib import Path
def sha256_path(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for ch in iter(lambda:f.read(65536),b""): h.update(ch)
    return h.hexdigest()
