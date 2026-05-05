import json
from pathlib import Path
req={"receipt_id","source_id","probe_kind","network_mode","url_sha256","response_body_stored","verification_status","validation_result"}
obj=json.loads(Path("fixtures/source/hydrology/source_probe_receipt.wbd.no_network.valid.json").read_text())
missing=sorted(req-set(obj))
if missing:
 print("FAIL",missing); raise SystemExit(1)
print("PASS probe receipt fields present")
p=Path('fixtures/source/hydrology/source_probe_receipt.usgs_waterdata.no_network.valid.json')
o=json.loads(p.read_text())
ok=o.get('verification_status') in {'NEEDS_VERIFICATION','VERIFIED','FAILED','EXPIRED','SUPERSEDED','UNCHECKED'}
print('PASS probe receipt status recorded' if ok else 'FAIL invalid probe status')
raise SystemExit(0 if ok else 1)
