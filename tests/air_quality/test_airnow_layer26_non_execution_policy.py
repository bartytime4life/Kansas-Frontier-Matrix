import json
from pathlib import Path
def test_non_execution_flags_false():
 d=json.loads(Path('tests/fixtures/air_quality/airnow/layer26/expected/preservation_closure_non_execution_attestation.json').read_text());assert d['commands_executed'] is False
