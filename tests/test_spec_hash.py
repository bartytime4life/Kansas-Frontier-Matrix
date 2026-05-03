import subprocess,unittest
class T(unittest.TestCase):
  def test(self): self.assertEqual(subprocess.run(["python","tools/compute_spec_hash.py","fixtures/release/release_manifest.valid.json"]).returncode,0)
