import json
from pathlib import Path
p=Path('fixtures/domains/hydrology/source_verification/hydrology_source_profile.valid.json')
o=json.loads(p.read_text())
bad=[]
if o.get('source_role')=='BOUNDARY_CONTEXT' and any('observed' in c for c in o.get('claims',[])): bad.append('WBD boundary cannot claim observed flow')
print('PASS source semantics checks' if not bad else 'FAIL '+str(bad))
raise SystemExit(0 if not bad else 1)
