import json
from pathlib import Path
errs=[]
for p in Path('fixtures/source/hydrology').glob('source_activation_decision*.valid.json'):
 o=json.loads(p.read_text())
 if o['decision']=='ALLOW' and o.get('source_id','').startswith('SRC-HYD-') and 'SYNTHETIC' not in o.get('source_id','') and not o.get('synthetic_test'): errs.append(f'{p}: real source cannot be ALLOW')
print('PASS source activation gates fail closed' if not errs else 'FAIL '+str(errs))
raise SystemExit(0 if not errs else 1)
