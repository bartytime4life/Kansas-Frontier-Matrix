import json,unittest
from pathlib import Path
class T(unittest.TestCase):
 def test_no_public(self):
  r=json.loads(Path('fixtures/source/hydrology/source_rights_decision.wbd.valid.json').read_text())
  self.assertNotEqual(r['publication_eligibility'],'ELIGIBLE_PUBLIC_AFTER_GATES')
