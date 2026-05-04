import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_not_evidence(self): d=json.loads(Path('fixtures/domains/hydrology/raw_capture_receipts/usgs_water_data.synthetic_streamflow.raw_capture_receipt.json').read_text()); self.assertIn('not EvidenceBundle',d['evidence_boundary'])
