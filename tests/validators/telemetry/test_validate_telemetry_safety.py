"""The telemetry entry point selects only reviewed, bounded validators."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SOURCE = (
    Path(__file__).resolve().parents[3]
    / "tools/validators/validate_telemetry_safety.py"
)
SPEC = importlib.util.spec_from_file_location("kfm_telemetry_dispatch", SOURCE)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TelemetryDispatchTests(unittest.TestCase):
    def test_fixture_replay_covers_exact_registered_profiles(self) -> None:
        output = io.StringIO()
        with patch.object(MODULE, "_run", return_value="PASS") as run:
            with contextlib.redirect_stdout(output):
                self.assertEqual(MODULE.main(["--fixtures"]), 0)
        self.assertEqual(
            [call.args for call in run.call_args_list],
            [(profile, None) for profile in MODULE.PROFILES],
        )
        report = json.loads(output.getvalue())
        self.assertEqual(report["authority"], "NONE")
        self.assertEqual(report["outcome"], "PASS")

    def test_failed_profile_fails_aggregate_without_candidate_echo(self) -> None:
        output = io.StringIO()
        with patch.object(
            MODULE, "_run",
            side_effect=lambda name, _: "DENY" if name == "trace_receipt_link" else "PASS",
        ):
            with contextlib.redirect_stdout(output):
                self.assertEqual(MODULE.main(["--fixtures"]), 1)
        self.assertEqual(json.loads(output.getvalue())["outcome"], "DENY")

    def test_candidate_requires_known_explicit_profile(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                MODULE.main(["--candidate", "private.json"])
            with self.assertRaises(SystemExit):
                MODULE.main(["--candidate", "private.json", "--profile", "other"])
        output = io.StringIO()
        with patch.object(MODULE, "_run", return_value="DENY") as run:
            with contextlib.redirect_stdout(output):
                self.assertEqual(MODULE.main([
                    "--candidate", "private.json", "--profile", "trace_receipt_link"
                ]), 1)
        run.assert_called_once_with("trace_receipt_link", Path("private.json"))
        self.assertNotIn("private.json", output.getvalue())

    def test_relative_candidate_is_bound_before_validator_changes_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            previous = Path.cwd()
            try:
                os.chdir(directory)
                Path("candidate.json").write_text("{}", encoding="utf-8")
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    code = MODULE.main([
                        "--candidate", "candidate.json",
                        "--profile", "map_build_sustainability",
                    ])
            finally:
                os.chdir(previous)
        # A parsed, schema-invalid candidate is DENY; a wrong-path read is ERROR.
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(output.getvalue())["outcome"], "DENY")
        self.assertNotIn(directory, output.getvalue())

    def test_success_exit_without_verified_fixture_cases_is_error(self) -> None:
        for body in ('', '{"scope":"telemetry.openlineage_run_event_projection","ok":true,"cases":[]}',
                     '{"scope":"telemetry.remote_sensing_lineage_activity","ok":true,"cases":[{"ok":true}]}'):
            with self.subTest(body=body), patch.object(
                MODULE.subprocess, "run",
                return_value=subprocess.CompletedProcess([], 0, body, ""),
            ):
                self.assertEqual(MODULE._run("openlineage_run_event_projection", None), "ERROR")

    def test_legacy_trace_fixture_needs_its_polarity_summary(self) -> None:
        with patch.object(
            MODULE.subprocess, "run",
            return_value=subprocess.CompletedProcess([], 0, '{"scope":"trace-receipt-evidence-linkage-only","outcome":"PASS"}', ""),
        ):
            self.assertEqual(MODULE._run("trace_receipt_link", None), "ERROR")

    def test_candidate_cannot_claim_another_validator_scope(self) -> None:
        with patch.object(
            MODULE.subprocess, "run",
            return_value=subprocess.CompletedProcess([], 0, json.dumps({
                "authority": "NONE", "outcome": "PASS",
                "scope": "telemetry.remote_sensing_lineage_activity",
            }), ""),
        ):
            self.assertEqual(MODULE._run("openlineage_run_event_projection", Path("candidate.json")), "ERROR")


if __name__ == "__main__":
    unittest.main()
