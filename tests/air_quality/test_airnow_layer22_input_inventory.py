import json
from pathlib import Path
def test_input_inventory_expected_fixture_exists():
 d=json.loads(Path('tests/fixtures/air_quality/airnow/layer22/expected/snapshot_preservation_finalization_input_inventory.json').read_text());assert d['object_type'].endswith('InputInventory')
