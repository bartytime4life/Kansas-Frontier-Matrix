from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from _support import FIXTURE_ROOT, VALIDATOR_PATH, copy_fixture


class StaleScanCliTests(unittest.TestCase):
    def _run(self, *args: str, root: Path = FIXTURE_ROOT):
        return subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--repo-root", str(root), *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            check=False,
        )

    def test_cli_requires_explicit_as_of_date(self) -> None:
        completed = self._run("--format", "json", "README.md", "docs")

        self.assertEqual(completed.returncode, 2)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "ERROR")
        self.assertIn("required", payload["findings"][0]["message"])

    def test_cli_json_warn_exit_is_zero(self) -> None:
        completed = self._run(
            "--as-of",
            "2026-08-07",
            "--format",
            "json",
            "README.md",
            "docs",
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "DOC_STALE_SCAN_WARN")

    def test_cli_warnings_as_errors_exit_is_one(self) -> None:
        completed = self._run(
            "--as-of",
            "2026-08-07",
            "--warnings-as-errors",
            "--format",
            "json",
            "README.md",
            "docs",
        )

        self.assertEqual(completed.returncode, 1)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "DOC_STALE_SCAN_FAIL")

    def test_cli_type_window_validation_errors_safely(self) -> None:
        completed = self._run(
            "--as-of",
            "2026-08-07",
            "--type-window",
            "invalid",
            "--format",
            "json",
            "README.md",
        )

        self.assertEqual(completed.returncode, 2)
        self.assertEqual(json.loads(completed.stdout)["outcome"], "ERROR")

    def test_cli_writes_explicit_output_without_mutating_inputs(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        before = {
            path.relative_to(root).as_posix(): path.read_bytes()
            for path in root.rglob("*")
            if path.is_file()
        }
        output = root / "report" / "stale.md"

        completed = self._run(
            "--as-of",
            "2026-08-07",
            "--format",
            "markdown",
            "--output",
            str(output),
            "README.md",
            "docs",
            root=root,
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("Freshness Workbench", output.read_text(encoding="utf-8"))
        after = {
            path.relative_to(root).as_posix(): path.read_bytes()
            for path in root.rglob("*")
            if path.is_file() and path != output
        }
        self.assertEqual(before, after)

    @unittest.skipIf(os.name == "nt", "symbolic-link behavior varies on Windows")
    def test_cli_denies_symbolic_link_output(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        base = Path(temporary.name)
        target = base / "target.txt"
        target.write_text("preserve", encoding="utf-8")
        link = base / "output.txt"
        link.symlink_to(target)

        completed = self._run(
            "--as-of",
            "2026-08-07",
            "--output",
            str(link),
            "README.md",
            "docs",
        )

        self.assertEqual(completed.returncode, 2)
        self.assertEqual(target.read_text(encoding="utf-8"), "preserve")


if __name__ == "__main__":
    unittest.main()
