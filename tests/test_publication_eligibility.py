import subprocess,unittest
class T(unittest.TestCase):
 def test_pub(self): self.assertEqual(subprocess.run(['python','tools/check_publication_eligibility.py']).returncode,0)
