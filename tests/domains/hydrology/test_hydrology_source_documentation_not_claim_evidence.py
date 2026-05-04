import json, unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_docs_not_evidence(self):
        doc=json.loads(Path('fixtures/domains/hydrology/source_documentation_checks/usgs_water_data.documentation_check.json').read_text())
        self.assertNotIn('evidence_ref', doc)
