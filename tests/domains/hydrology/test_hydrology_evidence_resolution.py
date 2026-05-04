import json, unittest
from pathlib import Path

class T(unittest.TestCase):
    def test_valid_and_invalid_claim_resolution(self):
        claim = json.loads(Path('fixtures/domains/hydrology/claim.synthetic.valid.json').read_text())
        bad = json.loads(Path('fixtures/domains/hydrology/claim.synthetic.invalid_missing_evidence.json').read_text())
        ref = json.loads(Path('fixtures/evidence/evidence_ref.valid.json').read_text())
        bundle = json.loads(Path('fixtures/evidence/evidence_bundle.valid.json').read_text())
        self.assertEqual(claim['evidence_ref'], ref['id'])
        self.assertIn(ref['id'], bundle['evidence_refs'])
        self.assertNotEqual(bad['evidence_ref'], ref['id'])
