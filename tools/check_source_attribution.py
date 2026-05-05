import json
from pathlib import Path
obj=json.loads(Path('fixtures/source/hydrology/source_attribution_requirement.wbd.valid.json').read_text())
ok=obj.get('attribution_status') in {'NEEDS_VERIFICATION','REQUIRED','NOT_REQUIRED'}
print('PASS source attribution checks' if ok else 'FAIL source attribution checks')
raise SystemExit(0 if ok else 1)
