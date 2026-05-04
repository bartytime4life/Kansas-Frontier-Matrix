import unittest
from pathlib import Path
class T(unittest.TestCase):
    def test_no_connector_internal(self):
        t=Path('fixtures/ui/evidence_drawer_payload.valid.json').read_text().lower()
        self.assertNotIn('connector-',t)
