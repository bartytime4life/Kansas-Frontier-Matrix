import json
from pathlib import Path
def test_non_execution_flags_false():
 d=json.loads(Path('tests/fixtures/air_quality/airnow/layer22/expected/snapshot_preservation_non_execution_attestation.json').read_text());assert d['commands_executed'] is False
