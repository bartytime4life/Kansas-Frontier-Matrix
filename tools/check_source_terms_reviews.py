import json
from pathlib import Path
obj=json.loads(Path('fixtures/source/hydrology/source_terms_check_receipt.wbd.no_network.valid.json').read_text())
assert obj['validation_result'] in {'ABSTAIN','DENY','PASS','WARN','FAIL','ERROR'}
print('PASS source terms review fixtures valid')
