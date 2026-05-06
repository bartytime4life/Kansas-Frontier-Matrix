from .constants import MANIFEST_BOOL_GATES,MANIFEST_FORBIDDEN_KEY_TERMS

def validate_manifest(m):
 e=[]
 for k,v in MANIFEST_BOOL_GATES.items():
  if m.get(k)!=v: e.append(f"MANIFEST_GATE_INVALID:{k}")
 for k in m.keys():
  low=k.lower()
  if any(t in low for t in MANIFEST_FORBIDDEN_KEY_TERMS): e.append(f"MANIFEST_FORBIDDEN_KEY:{k}")
 return e
