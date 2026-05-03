from pathlib import Path
from .constants import GOV,BAD_KEY,BAD_PATH
def validate_path_safe(p):
 s=str(p); return (not BAD_PATH.search(s)) and (not Path(s).is_absolute())
def validate_manifest(m):
 e=[]
 for k,v in GOV.items():
  if m.get(k)!=v: e.append(f"DENIED_CAPABILITY:{k}")
 for k in m:
  if BAD_KEY.search(k): e.append(f"FORBIDDEN_MANIFEST_KEY:{k}")
 return e
