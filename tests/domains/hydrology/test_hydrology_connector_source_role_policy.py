import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_misuse(self):
        wbd=json.loads(Path('fixtures/domains/hydrology/source_role_review/usgs_wbd.source_role_review_note.json').read_text())
        self.assertIn('streamflow_observation', wbd['disallowed_claim_types'])
