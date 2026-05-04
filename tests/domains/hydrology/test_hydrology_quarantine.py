import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_quarantine(self): d=json.loads(Path('fixtures/domains/hydrology/quarantine/usgs_water_data.synthetic_malformed.quarantine_record.json').read_text()); self.assertEqual(d['lifecycle_stage'],'QUARANTINE')
