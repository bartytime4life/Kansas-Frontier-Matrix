import subprocess,unittest
class T(unittest.TestCase):
 def test_sem(self): self.assertEqual(subprocess.run(['python','tools/check_hydrology_observation_semantics.py']).returncode,0)
