import json
import tempfile
import unittest
from pathlib import Path

from tests.subprocess_utils import assert_python_ok, run_python


class SpecHashTests(unittest.TestCase):
    def test_compute_spec_hash_command(self):
        assert_python_ok(self, ["tools/compute_spec_hash.py", "fixtures/release/release_manifest.valid.json"])

    def test_hash_is_order_independent(self):
        a = {"b": 2, "a": 1, "nested": {"z": 9, "y": 8}}
        b = {"nested": {"y": 8, "z": 9}, "a": 1, "b": 2}
        with tempfile.TemporaryDirectory() as td:
            p1 = Path(td) / "a.json"
            p2 = Path(td) / "b.json"
            p1.write_text(json.dumps(a, indent=2))
            p2.write_text(json.dumps(b, indent=2))
            h1 = run_python(["tools/compute_spec_hash.py", str(p1)])
            h2 = run_python(["tools/compute_spec_hash.py", str(p2)])
            self.assertEqual(h1.returncode, 0, msg=h1.stdout + h1.stderr)
            self.assertEqual(h2.returncode, 0, msg=h2.stdout + h2.stderr)
            self.assertEqual(h1.stdout.strip(), h2.stdout.strip())
