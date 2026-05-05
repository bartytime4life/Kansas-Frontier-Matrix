import subprocess,unittest
class T(unittest.TestCase):
 def test_terms(self): self.assertEqual(subprocess.run(['python','tools/check_source_terms_reviews.py']).returncode,0)
