import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_links(self): c=json.loads(Path('fixtures/domains/hydrology/correction_notice.pr006_synthetic_ingest.json').read_text()); r=json.loads(Path('fixtures/domains/hydrology/rollback_card.pr006_synthetic_ingest_drill.json').read_text()); self.assertEqual(r['finite_state'],'ROLLBACK_READY'); self.assertEqual(c['affected_work_candidate_id'],'work-1')
