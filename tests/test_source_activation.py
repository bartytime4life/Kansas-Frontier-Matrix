import unittest, subprocess
class T(unittest.TestCase):
    def test_activation(self): self.assertEqual(subprocess.run(['python','tools/check_source_activation.py']).returncode,0)
