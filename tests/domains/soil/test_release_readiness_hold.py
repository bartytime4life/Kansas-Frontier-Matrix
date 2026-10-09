#!/usr/bin/env python3
"""Exercise the Soil readiness hold in an isolated, synthetic repository.

This tests CI guards only; it cannot accept proof, admit a source, or release data.
"""

from __future__ import annotations

import os
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
WORKFLOW = REPO_ROOT / ".github/workflows/domain-soil.yml"
RELEASE_INDEX = Path("docs/domains/soil/RELEASE_INDEX.md")
# Original bytes at ebcc4988, deliberately restored by merged PR #4941.
PROTECTED_MARKER = "# soil — RELEASE_INDEX.md\n\nGreenfield placeholder.\n".encode("utf-8")
REQUIRED_PATHS = (
    Path("release/candidates/soil/README.md"),
    RELEASE_INDEX,
    Path("docs/runbooks/soil/PROMOTION_RUNBOOK.md"),
    Path("docs/runbooks/soil/ROLLBACK_RUNBOOK.md"),
    Path("data/published/layers/soil/README.md"),
    Path(".github/workflows/release-dry-run.yml"),
)
HOLD = (
    "WORKFLOW_HOLD: no accepted Soil release dry-run command "
    "or candidate manifest contract"
)


def readiness_script() -> str:
    """Read the actual literal bash step; fail if its layout becomes ambiguous."""
    prefix = (
        "      - name: Evaluate Soil release dry-run readiness\n"
        "        shell: bash\n"
        "        run: |\n"
    )
    workflow = WORKFLOW.read_text(encoding="utf-8")
    if workflow.count(prefix) != 1:
        raise AssertionError("Expected one literal Soil release-readiness bash step")
    lines: list[str] = []
    for line in workflow.split(prefix, 1)[1].splitlines():
        if line and not line.startswith("          "):
            break
        lines.append(line)
    if not lines:
        raise AssertionError("Soil release-readiness bash step is empty")
    return textwrap.dedent("\n".join(lines))


class SoilReleaseReadinessHoldTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="kfm-soil-readiness-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for path in (*REQUIRED_PATHS, Path("Makefile")):
            destination = self.root / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes((REPO_ROOT / path).read_bytes())
        (self.root / RELEASE_INDEX).write_bytes(PROTECTED_MARKER)

    def evaluate(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["bash", "--noprofile", "--norc", "-c", readiness_script()],
            cwd=self.root,
            env={**os.environ, "KFM_NO_NETWORK": "1", "PYTHONDONTWRITEBYTECODE": "1"},
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )

    def assert_rejected(self, message: str) -> None:
        result = self.evaluate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(message, result.stdout)
        self.assertNotIn(HOLD, result.stdout)
        self.assertNotIn("WORKFLOW_SKIPPED_EXPLICIT", result.stdout)

    def test_repository_preserves_original_marker_bytes(self) -> None:
        self.assertEqual((REPO_ROOT / RELEASE_INDEX).read_bytes(), PROTECTED_MARKER)

    def test_original_marker_passes_only_with_explicit_release_hold(self) -> None:
        for lane in ("release/candidates/soil", "data/published/layers/soil"):
            (self.root / lane / ".gitkeep").touch()
        result = self.evaluate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(
            result.stdout.splitlines(),
            ["WORKFLOW_SKIPPED_EXPLICIT: publish-dry-run-soil", HOLD],
        )

    def test_any_marker_edit_or_release_row_is_rejected(self) -> None:
        mutations = (
            b"",
            PROTECTED_MARKER + b"\n",
            PROTECTED_MARKER.replace(b"placeholder.", b"placeholder. "),
            PROTECTED_MARKER.replace(b"Greenfield", b"Updated"),
            PROTECTED_MARKER + b"\n| synthetic-release | released |\n",
        )
        for marker in mutations:
            with self.subTest(marker=marker):
                (self.root / RELEASE_INDEX).write_bytes(marker)
                self.assert_rejected("The Soil release index changed.")

    def test_missing_required_boundary_is_rejected(self) -> None:
        for path in REQUIRED_PATHS:
            with self.subTest(path=str(path)):
                target = self.root / path
                original = target.read_bytes()
                target.unlink()
                try:
                    self.assert_rejected(f"Required Soil release boundary is missing: {path}")
                finally:
                    target.write_bytes(original)

    def test_changed_candidate_posture_is_rejected(self) -> None:
        (self.root / REQUIRED_PATHS[0]).write_text("Synthetic changed posture.\n")
        self.assert_rejected("The documented Soil candidate posture changed.")

    def test_new_candidate_record_is_rejected(self) -> None:
        (self.root / "release/candidates/soil/synthetic.json").write_text("{}\n")
        self.assert_rejected("A Soil candidate record surfaced")

    def test_new_release_dry_run_target_is_rejected(self) -> None:
        makefile = self.root / "Makefile"
        original = makefile.read_bytes()
        for target in ("soil-release-dry-run", "release-dry-run-soil"):
            with self.subTest(target=target):
                makefile.write_bytes(original + f"\n{target}:\n".encode("utf-8"))
                self.assert_rejected("A Soil release dry-run target now exists.")


if __name__ == "__main__":
    unittest.main()
