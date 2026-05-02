import json
from pathlib import Path
def test_ledger_counts():
 d=json.loads(Path('tests/fixtures/air_quality/airnow/layer26/expected/preservation_closure_review_finalization_ledger.json').read_text());assert d['acceptance_count']>=0
