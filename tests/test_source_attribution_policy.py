import subprocess,unittest
class T(unittest.TestCase):
 def test_attr(self): self.assertEqual(subprocess.run(['python','tools/check_source_attribution.py']).returncode,0)
