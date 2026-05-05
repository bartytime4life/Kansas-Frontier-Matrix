import unittest, subprocess
class T(unittest.TestCase):
    def test_semantics(self): self.assertEqual(subprocess.run(['python','tools/check_source_semantics.py']).returncode,0)
