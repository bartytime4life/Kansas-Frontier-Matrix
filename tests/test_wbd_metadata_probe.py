import subprocess, unittest

class T(unittest.TestCase):
    def test_dry_run_abstain(self):
        p=subprocess.run(["python","tools/probe_wbd_metadata.py","--dry-run"],capture_output=True,text=True)
        self.assertEqual(p.returncode,0)
        self.assertIn("ABSTAIN",p.stdout)
