import subprocess,unittest
class T(unittest.TestCase):
 def test_dryrun(self):
  p=subprocess.run(['python','tools/review_wbd_terms_rights.py','--dry-run'],capture_output=True,text=True)
  self.assertEqual(p.returncode,0); self.assertIn('ABSTAIN',p.stdout)
