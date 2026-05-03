import subprocess,unittest
class T(unittest.TestCase):
  def test(self): self.assertEqual(subprocess.run(["python","tools/check_no_public_internal_paths.py"]).returncode,0)
