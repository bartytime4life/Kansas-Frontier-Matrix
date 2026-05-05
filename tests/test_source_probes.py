import subprocess,unittest
class T(unittest.TestCase):
 def test_probe(self): self.assertEqual(subprocess.run(['python','tools/check_source_probes.py']).returncode,0)
