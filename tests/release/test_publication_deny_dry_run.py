from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

from tools.release.release_dry_run import CASES, build_report


ROOT = Path(__file__).resolve().parents[2]
CLI = ROOT / "tools/release/release_dry_run.py"


class PublicationDenyDryRunTests(unittest.TestCase):
    def test_all_required_negative_paths_are_blocked_exactly(self) -> None:
        report = build_report()
        self.assertEqual(report["dry_run_status"], "PASS")
        self.assertEqual(report["case_count"], 5)
        self.assertEqual(
            [case["case_id"] for case in report["cases"]],
            [case[0] for case in CASES],
        )
        for case in report["cases"]:
            with self.subTest(case=case["case_id"]):
                self.assertEqual(case["publication_outcome"], "DENIED")
                self.assertTrue(case["suite_match"])
                self.assertEqual(
                    case["validation_report"]["readiness"], "BLOCKED"
                )

    def test_report_never_claims_authority_or_assembly(self) -> None:
        report = build_report()
        for field in (
            "authority_created",
            "decision_created",
            "network_used",
            "publication_created",
            "release_candidate_assembled",
        ):
            self.assertIs(report[field], False)
        rendered = json.dumps(report, sort_keys=True)
        for forbidden in ('"APPROVE_READY"', '"PUBLISHED"', '"RELEASED"'):
            self.assertNotIn(forbidden, rendered)

    def test_execution_is_no_network(self) -> None:
        with mock.patch.object(
            socket,
            "socket",
            side_effect=AssertionError("network access is forbidden"),
        ):
            self.assertEqual(build_report()["dry_run_status"], "PASS")

    def test_cli_is_deterministic_and_emits_no_files(self) -> None:
        before = {path.relative_to(ROOT) for path in ROOT.rglob("*") if path.is_file()}
        command = [sys.executable, str(CLI)]
        environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        first = subprocess.run(
            command,
            cwd=ROOT,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
        )
        second = subprocess.run(
            command,
            cwd=ROOT,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
        )
        after = {path.relative_to(ROOT) for path in ROOT.rglob("*") if path.is_file()}
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(json.loads(first.stdout)["dry_run_status"], "PASS")
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
