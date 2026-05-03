import json,unittest
from pathlib import Path
class T(unittest.TestCase):
  def test_lane(self):
    f=json.loads(Path("fixtures/domains/hydrology/hydrology_feature.valid.json").read_text())
    self.assertEqual(f["knowledge_character"],"SYNTHETIC_TEST")
