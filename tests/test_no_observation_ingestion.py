import subprocess,unittest
class T(unittest.TestCase):
 def test_noing(self): self.assertEqual(subprocess.run(['python','tools/check_no_observation_ingestion.py']).returncode,0)
