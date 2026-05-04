import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_no_live_ready(self):
        for p in Path('fixtures/domains/hydrology/connector_readiness').glob('*.json'):
            d=json.loads(p.read_text()); self.assertNotEqual(d['live_fetch_status'],'ready')
