import subprocess,unittest
class T(unittest.TestCase):
 def test_profile(self): self.assertEqual(subprocess.run(['python','tools/check_hydrology_source_profiles.py']).returncode,0)
