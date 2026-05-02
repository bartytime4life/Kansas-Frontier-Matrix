import json
from pathlib import Path
def test_decision_ceiling_internal_only():
 d=json.loads(Path('tests/fixtures/air_quality/airnow/layer26/expected/preservation_closure_decision_candidate.json').read_text());assert 'INTERNAL_ONLY' in d['outcome_ceiling']
