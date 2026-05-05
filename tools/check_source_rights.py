import json
from pathlib import Path
BAD=[]
for p in Path('fixtures/source/hydrology').glob('source_descriptor.*.candidate.valid.json'):
 o=json.loads(p.read_text())
 if o.get('public_release_allowed') is not False: BAD.append(f'{p}: public_release_allowed must be false')
 if o.get('rights_status') in {'UNKNOWN','NOASSERTION'} and o.get('public_release_allowed') is True: BAD.append(f'{p}: unknown rights cannot be public')
r=json.loads(Path('fixtures/source/hydrology/source_rights_decision.wbd.valid.json').read_text())
if r.get('rights_status')=='UNKNOWN' and r.get('publication_eligibility')=='ELIGIBLE_PUBLIC_AFTER_GATES': BAD.append('rights decision allows public with unknown rights')
print('PASS source rights fail-closed' if not BAD else 'FAIL '+str(BAD)); raise SystemExit(0 if not BAD else 1)
