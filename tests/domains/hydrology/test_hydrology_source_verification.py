import json,unittest
from pathlib import Path
class T(unittest.TestCase):
  def test_candidates_inactive(self):
    for p in Path('fixtures/source/hydrology').glob('source_descriptor.*.candidate.valid.json'):
      self.assertFalse(json.loads(p.read_text())['public_release_allowed'])
