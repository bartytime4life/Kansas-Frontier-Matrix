import subprocess,unittest
class T(unittest.TestCase):
 def test_dryrun(self):
  p=subprocess.run(['python','tools/probe_usgs_water_data_metadata.py','--dry-run'],capture_output=True,text=True)
  self.assertEqual(p.returncode,0); self.assertIn('ABSTAIN',p.stdout)
