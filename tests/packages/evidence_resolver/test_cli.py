from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR = REPO_ROOT / "tools/validators/evidence_resolver/validate_candidate.py"
FIXTURES = REPO_ROOT / "fixtures/packages/evidence_resolver/v1alpha1"


class EvidenceResolutionCandidateCLITests(unittest.TestCase):
    def _run(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), *args],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
            env={
                "PATH": "",
                "PYTHONHASHSEED": "0",
                "PYTHONDONTWRITEBYTECODE": "1",
                "PYTHONUNBUFFERED": "1",
                "TZ": "UTC",
                "KFM_NO_NETWORK": "1",
            },
        )

    def test_fixture_suite_passes(self) -> None:
        completed = self._run("--fixtures", str(FIXTURES))
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("RESOLVED=2", completed.stdout)
        self.assertIn("UNRESOLVED=13", completed.stdout)
        self.assertIn("DENIED=1", completed.stdout)
        self.assertIn("ERROR=5", completed.stdout)

    def test_negative_only_suite_excludes_resolved_case(self) -> None:
        completed = self._run(
            "--fixtures", str(FIXTURES), "--negative-only"
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("RESOLVED=0", completed.stdout)

    def test_unreadable_input_fails_closed_without_echo(self) -> None:
        sentinel = "raw-sensitive-sentinel"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text("{" + sentinel, encoding="utf-8")
            completed = self._run("--input", str(path))
        self.assertEqual(4, completed.returncode)
        payload = json.loads(completed.stdout)
        self.assertEqual("ERROR", payload["status"])
        self.assertFalse(payload["authoritative"])
        self.assertNotIn(sentinel, completed.stdout + completed.stderr)

    def test_huge_integer_fails_closed_without_traceback(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "huge.json"
            path.write_text('{"number":' + "9" * 129 + "}", encoding="utf-8")
            completed = self._run("--input", str(path))
        self.assertEqual(4, completed.returncode)
        self.assertEqual("", completed.stderr)
        self.assertNotIn("Traceback", completed.stdout)
        self.assertEqual("ERROR", json.loads(completed.stdout)["status"])

    def test_oversized_file_is_read_with_a_hard_limit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "oversized.json"
            path.write_bytes(b"x" * 131_073)
            completed = self._run("--input", str(path))
        self.assertEqual(4, completed.returncode)
        payload = json.loads(completed.stdout)
        self.assertEqual("input/too-large", payload["issues"][0]["code"])
        self.assertEqual("", completed.stderr)

    def test_negative_mode_cannot_skip_a_relabeled_negative(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            copied = Path(directory) / "v1alpha1"
            shutil.copytree(FIXTURES, copied)
            path = copied / "invalid/policy_denied.json"
            payload = json.loads(path.read_text(encoding="utf-8"))
            payload["expected"]["status"] = "RESOLVED"
            path.write_text(json.dumps(payload), encoding="utf-8")
            completed = self._run(
                "--fixtures", str(copied), "--negative-only"
            )
        self.assertEqual(1, completed.returncode)
        self.assertIn("fixture/evaluation-error", completed.stderr)

    def test_fixture_inventory_is_ratcheted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            copied = Path(directory) / "v1alpha1"
            shutil.copytree(FIXTURES, copied)
            (copied / "invalid/policy_denied.json").unlink()
            completed = self._run("--fixtures", str(copied))
        self.assertEqual(1, completed.returncode)
        self.assertIn("fixture/inventory-mismatch", completed.stderr)


if __name__ == "__main__":
    unittest.main()
