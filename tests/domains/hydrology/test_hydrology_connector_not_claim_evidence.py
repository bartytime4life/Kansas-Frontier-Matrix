import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_receipt_not_claim_evidence(self):
        r=json.loads(Path('fixtures/domains/hydrology/fetch_receipts/usgs_water_data.mock_simulated.fetch_receipt.json').read_text())
        self.assertNotIn('evidence_ref', r)
