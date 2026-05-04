import json
import subprocess
import tempfile
import unittest
from pathlib import Path


class SpecHashTests(unittest.TestCase):
    def test_compute_spec_hash_command(self):
        self.assertEqual(subprocess.run(["python", "tools/compute_spec_hash.py", "fixtures/release/release_manifest.valid.json"]).returncode, 0)

    def test_hash_is_order_independent(self):
        a = {"b": 2, "a": 1, "nested": {"z": 9, "y": 8}}
        b = {"nested": {"y": 8, "z": 9}, "a": 1, "b": 2}
        with tempfile.TemporaryDirectory() as td:
            p1 = Path(td) / "a.json"
            p2 = Path(td) / "b.json"
            p1.write_text(json.dumps(a, indent=2))
            p2.write_text(json.dumps(b, indent=2))
            h1 = subprocess.check_output(["python", "tools/compute_spec_hash.py", str(p1)], text=True).strip()
            h2 = subprocess.check_output(["python", "tools/compute_spec_hash.py", str(p2)], text=True).strip()
            self.assertEqual(h1, h2)
