import json,unittest
from pathlib import Path
class T(unittest.TestCase):
  def test_outcomes(self):
    for n in ["answer","abstain","deny","error"]:
      o=json.loads(Path(f"fixtures/ai/focus_mode_response.{n}.valid.json").read_text())
      self.assertIn(o["outcome"],["ANSWER","ABSTAIN","DENY","ERROR"])
