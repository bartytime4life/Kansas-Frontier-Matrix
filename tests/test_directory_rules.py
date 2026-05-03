import subprocess,unittest
class T(unittest.TestCase):
  def test(self): self.assertEqual(subprocess.run(["python","tools/check_directory_rules.py"]).returncode,0)
