"""End-to-end proof for the checkout-local, read-only CLI diff route."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "apps" / "cli" / "src"


class DiffCommandTests(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        env = dict(os.environ, PYTHONPATH=str(SOURCE))
        return subprocess.run(
            [sys.executable, "-m", "kfm_cli", *args],
            cwd=ROOT, env=env, capture_output=True, text=True, check=False,
        )

    def test_json_diff_reports_change_and_blocking_exit(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            left, right = Path(folder) / "left.json", Path(folder) / "right.json"
            left.write_text('{"id":"one"}', encoding="utf-8")
            right.write_text('{"id":"two"}', encoding="utf-8")
            result = self.run_cli("diff", "json", "--left", str(left),
                                  "--right", str(right), "--fail-on-change")
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["status"], "changed")
        self.assertEqual(report["summary"]["changed"], ["id"])
        self.assertTrue(report["blocking"])

    def test_release_diff_rejects_untyped_input(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            left, right = Path(folder) / "left.json", Path(folder) / "right.json"
            left.write_text('{"artifacts":[{"artifact_ref":"ref:a"}]}', encoding="utf-8")
            right.write_text('{"object_type":"ReleaseManifest","artifacts":[{"artifact_ref":"ref:a"}]}', encoding="utf-8")
            result = self.run_cli("diff", "release", "--left", str(left),
                                  "--right", str(right))
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(json.loads(result.stdout)["error"]["code"], "LEFT_NOT_RELEASE_MANIFEST")

    def test_help_and_unknown_commands(self) -> None:
        self.assertIn("json", self.run_cli("diff", "--help").stdout)
        self.assertIn("--left", self.run_cli("diff", "json", "--help").stdout)
        unknown = self.run_cli("publish")
        self.assertEqual(unknown.returncode, 2)
        self.assertIn("invalid choice", unknown.stderr)


if __name__ == "__main__":
    unittest.main()
