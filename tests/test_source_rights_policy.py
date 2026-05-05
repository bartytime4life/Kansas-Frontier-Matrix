import unittest, subprocess
class T(unittest.TestCase):
    def test_rights(self): self.assertEqual(subprocess.run(['python','tools/check_source_rights.py']).returncode,0)
