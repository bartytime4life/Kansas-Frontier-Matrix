from pathlib import Path
from .constants import *

def _walk(o):
    if isinstance(o, dict):
        for k,v in o.items():
            yield k,v
            yield from _walk(v)
    elif isinstance(o, list):
        for x in o: yield from _walk(x)

def validate_manifest(m):
    errs=[]
    for k,v in GOVERNANCE_EXPECTED.items():
        if m.get(k)!=v: errs.append(f"MANIFEST_FIELD_INVALID:{k}")
    for k,_ in _walk(m):
        lk=str(k).lower()
        if any(t in lk for t in FORBIDDEN_MANIFEST_KEY_TOKENS): errs.append(f"FORBIDDEN_MANIFEST_KEY:{k}")
    return sorted(set(errs))

def validate_path_safe(path):
    s=str(path).lower()
    if any(x in s for x in DENIED_SCHEMES): return False
    if '..' in Path(path).parts: return False
    if any(t in s for t in FORBIDDEN_PATH_TOKENS): return False
    return True
