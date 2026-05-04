import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_raw(self): d=json.loads(Path('fixtures/domains/hydrology/raw_capture/usgs_water_data.synthetic_streamflow.raw_capture.json').read_text()); self.assertEqual(d['lifecycle_stage'],'RAW')
