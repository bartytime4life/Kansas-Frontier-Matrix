import unittest
from tools.connectors.offline_mock_transport import execute
class T(unittest.TestCase):
    def test_sim_and_block(self):
        self.assertEqual(execute('fixtures/domains/hydrology/fetch_plans/usgs_water_data.mock_allowed.json')['finite_state'],'SIMULATED')
        self.assertEqual(execute('fixtures/domains/hydrology/fetch_plans/usgs_water_data.real_blocked.json')['finite_state'],'BLOCKED')
