import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_role_limits(self):
        fema=json.loads(Path('data/registry/sources/hydrology/fema-nfhl.source_descriptor.json').read_text())
        wbd=json.loads(Path('data/registry/sources/hydrology/usgs-wbd.source_descriptor.json').read_text())
        dep=json.loads(Path('data/registry/sources/hydrology/usgs-3dep.source_descriptor.json').read_text())
        self.assertEqual(fema['knowledge_character'],'regulatory_flood_hazard_context')
        self.assertEqual(wbd['knowledge_character'],'hydrologic_unit_boundary')
        self.assertEqual(dep['knowledge_character'],'elevation_terrain_context')
