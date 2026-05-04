import json, unittest
from pathlib import Path

class T(unittest.TestCase):
    def test_correction_and_rollback_linked(self):
        c=json.loads(Path('fixtures/domains/hydrology/correction_notice.synthetic.json').read_text())
        r=json.loads(Path('fixtures/domains/hydrology/rollback_card.synthetic.json').read_text())
        self.assertEqual(c['affected_release_candidate_id'], r['release_candidate_id'])
        self.assertEqual(c['finite_state'], 'CORRECTION_PENDING')
        self.assertEqual(r['finite_state'], 'READY')
