import json
from pathlib import Path
o=json.loads(Path('fixtures/domains/hydrology/source_verification/hydrology_observation_source_profile.usgs_waterdata.valid.json').read_text())
ok=o['source_role']=='OBSERVATION_METADATA_CANDIDATE' and o['metadata_only']
print('PASS hydrology source profiles' if ok else 'FAIL hydrology source profiles')
raise SystemExit(0 if ok else 1)
