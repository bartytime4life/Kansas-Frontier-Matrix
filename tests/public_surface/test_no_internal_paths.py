import unittest
from pathlib import Path

class T(unittest.TestCase):
    def test_no_internal(self):
        forbidden=['data/raw/','data/work/','data/quarantine/','canonical','proof-pack','review-only','steward-only','direct_model']
        for rel in ['fixtures/ui/evidence_drawer_payload.valid.json','fixtures/ai/focus_mode_response.answer.valid.json']:
            text=Path(rel).read_text().lower()
            for bad in forbidden:
                self.assertNotIn(bad,text)
