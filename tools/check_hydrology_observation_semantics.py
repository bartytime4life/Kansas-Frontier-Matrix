import json
from pathlib import Path
o=json.loads(Path('fixtures/domains/hydrology/source_verification/hydrology_parameter_semantics.usgs_waterdata.valid.json').read_text())
ok=o.get('not_current_claim_evidence') is True
print('PASS hydrology observation semantics' if ok else 'FAIL hydrology observation semantics')
raise SystemExit(0 if ok else 1)
