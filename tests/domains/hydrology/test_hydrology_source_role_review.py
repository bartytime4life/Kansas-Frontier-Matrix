import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_not_claim_evidence(self):
        for p in Path('fixtures/domains/hydrology/source_role_review').glob('*.json'):
            d=json.loads(p.read_text()); self.assertIn('cannot satisfy EvidenceRef->EvidenceBundle', d['misuse_examples'])
