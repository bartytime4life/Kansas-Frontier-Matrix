import json
from pathlib import Path
BAD=["data/raw","data/work","data/quarantine","steward-only","model-runtime"]
viol=[]
for p in Path("fixtures").rglob("*.json"):
 t=p.read_text()
 if any(b in t for b in BAD) and "invalid" not in p.parts: viol.append(str(p))
print("FAIL" if viol else "PASS", viol)
raise SystemExit(1 if viol else 0)
