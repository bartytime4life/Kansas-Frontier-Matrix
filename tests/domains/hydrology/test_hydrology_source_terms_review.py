import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_terms_blocked(self):
        for p in Path('fixtures/domains/hydrology/source_terms_review').glob('*.json'):
            d=json.loads(p.read_text()); self.assertFalse(d['public_release_allowed']); self.assertFalse(d['data_fetch_allowed'])
