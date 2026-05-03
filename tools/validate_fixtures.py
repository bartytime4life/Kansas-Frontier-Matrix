import json
from pathlib import Path
errs=[]
for p in Path("fixtures").rglob("*.valid.json"):
 o=json.loads(p.read_text())
 if o.get("knowledge_character")!="SYNTHETIC_TEST": errs.append(f"{p}: knowledge_character")
 if "focus_mode_response.answer" in p.name and not o.get("citations"): errs.append(f"{p}: missing citations")
rm=json.loads(Path("fixtures/release/release_manifest.valid.json").read_text())
if not rm.get("rollback_target") or not rm.get("correction_route"): errs.append("release manifest continuity")
print("FAIL" if errs else "PASS", errs)
raise SystemExit(1 if errs else 0)
