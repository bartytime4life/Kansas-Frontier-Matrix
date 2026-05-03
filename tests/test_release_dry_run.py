import subprocess,unittest
class T(unittest.TestCase):
  def test(self): self.assertEqual(subprocess.run(["python","tools/promotion_dry_run.py"]).returncode,0)
