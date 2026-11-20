"""Offline tests for the marker-gated pin extractor used by the CI lock audit."""
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools/ci"))

import marker_gated_pins as module  # noqa: E402

A = "a" * 64
B = "b" * 64
C = "c" * 64
CURRENT = f"{sys.version_info.major}.{sys.version_info.minor}"


class MarkerGatedPinsTests(unittest.TestCase):
    def test_only_pins_excluded_here_are_returned_without_markers(self) -> None:
        text = (
            "# comment\n"
            f"certifi==1 \\\n    --hash=sha256:{A}\n"
            f'pkg==1.0; python_version == "{CURRENT}" \\\n    --hash=sha256:{B}\n'
            f'pkg==2.0; python_version != "{CURRENT}" \\\n'
            f"    --hash=sha256:{B} \\\n    --hash=sha256:{C}\n"
        )
        self.assertEqual(
            module.excluded_requirements(text),
            [f"pkg==2.0 --hash=sha256:{B} --hash=sha256:{C}"],
        )

    def test_unhashed_or_truncated_requirements_fail_closed(self) -> None:
        with self.assertRaises(module.LockFormatError):
            module.excluded_requirements("pkg==1.0\n")
        with self.assertRaises(module.LockFormatError):
            module.excluded_requirements(f"pkg==1.0 \\\n    --hash=sha256:{A} \\\n")

    def test_cli_writes_one_file_per_lock_with_excluded_pins(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            gated = root / "gated.lock"
            gated.write_text(
                f'pkg==2.0; python_version != "{CURRENT}" \\\n    --hash=sha256:{A}\n',
                encoding="utf-8",
            )
            plain = root / "plain.lock"
            plain.write_text(f"pkg==1.0 \\\n    --hash=sha256:{A}\n", encoding="utf-8")
            out = root / "out"
            written = module.write_excluded([gated, plain], out)
            self.assertEqual(written, [out / "gated.lock"])
            self.assertEqual(
                (out / "gated.lock").read_text(encoding="utf-8"),
                f"pkg==2.0 --hash=sha256:{A}\n",
            )
            self.assertEqual(module.main(["--output-dir", str(root / "x"), str(root / "missing.lock")]), 2)

    def test_every_ci_lock_parses(self) -> None:
        for lock in sorted((ROOT / "tools/ci").glob("*.lock")):
            with self.subTest(lock=lock.name):
                module.excluded_requirements(lock.read_text(encoding="utf-8"))

    def test_audit_job_scans_the_gated_pins(self) -> None:
        workflow = yaml.safe_load((ROOT / ".github/workflows/dependency-scan.yml").read_text())
        runs = [step.get("run", "") for step in workflow["jobs"]["pip-audit"]["steps"]]
        gated = [run for run in runs if "marker_gated_pins.py" in run]
        self.assertEqual(len(gated), 1)
        self.assertIn("tools/ci/*.lock", gated[0])
        self.assertIn("python -m pip_audit", gated[0])
        for flag in ("--require-hashes", "--disable-pip", "--strict"):
            self.assertIn(flag, gated[0])
        self.assertLess(runs.index(next(r for r in runs if "--requirement tools/ci/" in r)),
                        runs.index(gated[0]))


if __name__ == "__main__":
    unittest.main()
