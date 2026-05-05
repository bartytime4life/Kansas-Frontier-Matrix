import json
from pathlib import Path
p=Path('fixtures/source/hydrology/source_probe_receipt.valid.json')
o=json.loads(p.read_text())
ok=o.get('verification_status') in {'NEEDS_VERIFICATION','VERIFIED','FAILED','EXPIRED','SUPERSEDED','UNCHECKED'}
print('PASS probe receipt status recorded' if ok else 'FAIL invalid probe status')
raise SystemExit(0 if ok else 1)
