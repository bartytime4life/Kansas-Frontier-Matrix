import json
from pathlib import Path
def test_candidate_only_and_residual_only():
 a=json.loads(Path('tests/fixtures/air_quality/airnow/layer22/expected/snapshot_preservation_acceptance_consolidation.json').read_text());b=json.loads(Path('tests/fixtures/air_quality/airnow/layer22/expected/snapshot_preservation_blocker_consolidation.json').read_text());assert a['candidate_only'] is True and b['residual_only'] is True
