import json,unittest
from pathlib import Path
class T(unittest.TestCase):
 def test_role(self):
  o=json.loads(Path('fixtures/source/hydrology/source_capability_matrix.usgs_waterdata.valid.json').read_text())
  self.assertEqual(o['source_role'],'OBSERVATION_METADATA_CANDIDATE')
