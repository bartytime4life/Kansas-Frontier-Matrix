import json
from pathlib import Path
o=json.loads(Path('fixtures/source/hydrology/source_probe_receipt.usgs_waterdata.no_network.valid.json').read_text())
bad=['/items','/iv','/dv','/values','/query']
ok=o['validation_result']=='ABSTAIN' and o['response_body_stored'] is False
print('PASS source probe checks' if ok else 'FAIL source probe checks')
raise SystemExit(0 if ok else 1)
