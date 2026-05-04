import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_work(self): d=json.loads(Path('fixtures/domains/hydrology/work_candidates/usgs_water_data.synthetic_streamflow.work_candidate.json').read_text()); self.assertEqual(d['lifecycle_stage'],'WORK')
