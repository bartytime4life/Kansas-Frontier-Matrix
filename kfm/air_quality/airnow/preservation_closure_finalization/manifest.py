import re
from pathlib import Path
from .constants import MANIFEST_BOOL_GATES,MANIFEST_FORBIDDEN_KEY_TERMS,DENY_SCHEMES,FORBIDDEN_PATH_TERMS
def validate_path_safe(v):
 vv=v.lower(); return not((".." in Path(v).parts) or any(vv.startswith(s) for s in DENY_SCHEMES) or ("://" in vv) or any(t in vv for t in FORBIDDEN_PATH_TERMS))
def validate_manifest(m):
 e=[]
 for k,v in MANIFEST_BOOL_GATES.items():
  if m.get(k)!=v: e.append(f"MANIFEST_GATE_INVALID:{k}")
 for k in m.keys():
  if any(t in k.lower() for t in MANIFEST_FORBIDDEN_KEY_TERMS): e.append(f"MANIFEST_FORBIDDEN_KEY:{k}")
 return e
