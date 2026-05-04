import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_denied(self): d=json.loads(Path('fixtures/domains/hydrology/promotion_dry_runs/hydrology_synthetic_ingest_drill.denied.json').read_text()); self.assertIn(d['finite_result'],['DENY','ABSTAIN'])
