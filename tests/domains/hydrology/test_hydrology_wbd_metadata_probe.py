import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_wbd_boundary_role(self):
        obj=json.loads(Path("fixtures/source/hydrology/source_descriptor.wbd.candidate.valid.json").read_text())
        self.assertEqual(obj["source_role"],"BOUNDARY_CONTEXT")
        self.assertFalse(obj["public_release_allowed"])
