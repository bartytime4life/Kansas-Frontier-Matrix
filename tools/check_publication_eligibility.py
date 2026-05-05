import json
from pathlib import Path
r=json.loads(Path('fixtures/source/hydrology/source_rights_decision.wbd.valid.json').read_text())
ok=not (r.get('rights_status')=='UNKNOWN' and r.get('publication_eligibility')=='ELIGIBLE_PUBLIC_AFTER_GATES')
print('PASS publication eligibility fail-closed' if ok else 'FAIL publication eligibility')
raise SystemExit(0 if ok else 1)
