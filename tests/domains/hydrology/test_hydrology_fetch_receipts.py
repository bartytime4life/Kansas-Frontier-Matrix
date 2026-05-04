import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_not_evidence(self):
        d=json.loads(Path('fixtures/domains/hydrology/fetch_receipts/usgs_water_data.mock_simulated.fetch_receipt.json').read_text())
        self.assertIn('not EvidenceBundle', d['evidence_boundary'])
