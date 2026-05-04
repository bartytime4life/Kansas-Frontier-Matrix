import json, unittest
from pathlib import Path

class T(unittest.TestCase):
    def test_drawer_states(self):
        good=json.loads(Path('fixtures/domains/hydrology/evidence_drawer.synthetic.valid.json').read_text())
        bad=json.loads(Path('fixtures/domains/hydrology/evidence_drawer.synthetic.unresolved.json').read_text())
        self.assertEqual(good['ui_trust_state'],'TRUST_READY')
        self.assertEqual(bad['ui_trust_state'],'EVIDENCE_MISSING')
