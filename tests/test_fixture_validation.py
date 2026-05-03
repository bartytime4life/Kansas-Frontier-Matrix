import subprocess,unittest
class T(unittest.TestCase):
  def test(self): self.assertEqual(subprocess.run(["python","tools/validate_fixtures.py"]).returncode,0)
