import json
from pathlib import Path
bad=[]
for p in Path('fixtures/source/hydrology').glob('source_descriptor.*.candidate.valid.json'):
 o=json.loads(p.read_text())
 if o.get('public_release_allowed') is not False: bad.append(str(p))
r=json.loads(Path('fixtures/source/hydrology/source_rights_decision.wbd.valid.json').read_text())
if r.get('rights_status')=='UNKNOWN' and r.get('publication_eligibility')=='ELIGIBLE_PUBLIC_AFTER_GATES': bad.append('rights decision allows public with unknown rights')
print('PASS source rights fail-closed' if not bad else 'FAIL '+str(bad)); raise SystemExit(0 if not bad else 1)
