import unittest, subprocess
class T(unittest.TestCase):
    def test_probe(self): self.assertEqual(subprocess.run(['python','tools/check_source_probe_receipts.py']).returncode,0)
