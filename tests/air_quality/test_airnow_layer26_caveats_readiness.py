import json
from pathlib import Path
def test_required_caveats_and_readiness_flags():
 cav=json.loads(Path('tests/fixtures/air_quality/airnow/layer26/expected/preservation_closure_caveat_continuity_register.json').read_text());assert 'AIRNOW_PRELIMINARY_DATA' in cav['caveats']
