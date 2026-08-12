from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = (
    REPO_ROOT
    / "tools/validators/directory_governance/validate_repository_topology.py"
)
SPEC = importlib.util.spec_from_file_location(
    "kfm_validate_repository_topology_output_security", MODULE_PATH
)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class RepositoryTopologyOutputSecurityTests(unittest.TestCase):
    def test_trusted_baseline_enforcement_returns_no_caller_data(self) -> None:
        candidate_ref = "refs/heads/internal-baseline"
        resolved_sha = "a" * 40
        with (
            mock.patch.object(
                module,
                "_git",
                side_effect=[
                    (resolved_sha + "\n").encode("ascii"),
                    b"{}",
                ],
            ),
            mock.patch.object(module, "_load_baseline_bytes", return_value=({}, {})),
            mock.patch.object(module, "validate_baseline_transition") as transition,
        ):
            result = module.enforce_trusted_baseline(
                Path("."),
                {"generated_from_ref": "main@not-bootstrap"},
                {},
                candidate_ref,
            )

        self.assertIsNone(result)
        transition.assert_called_once()

    def test_cli_redacts_trusted_transition_without_echo(self) -> None:
        candidate_ref = "refs/heads/internal-baseline"
        resolved_sha = "b" * 40
        current_data = {
            "expires_on": "2026-11-10",
            "generated_from_ref": "main@not-bootstrap",
        }
        output = io.StringIO()

        with tempfile.TemporaryDirectory() as directory:
            baseline_path = Path(directory) / "baseline.json"
            baseline_path.write_text("{}\n", encoding="utf-8")
            with (
                mock.patch.object(module, "scan", return_value=((), 0)),
                mock.patch.object(
                    module,
                    "_load_baseline_bytes",
                    side_effect=[(current_data, {}), ({}, {})],
                ),
                mock.patch.object(
                    module,
                    "_git",
                    side_effect=[
                        (resolved_sha + "\n").encode("ascii"),
                        b"{}",
                    ],
                ),
                mock.patch.object(module, "validate_baseline_transition"),
                redirect_stdout(output),
            ):
                code = module.main(
                    [
                        "--repo-root",
                        str(REPO_ROOT),
                        "--baseline",
                        str(baseline_path),
                        "--trusted-baseline-ref",
                        candidate_ref,
                    ]
                )

        rendered = output.getvalue()
        report = json.loads(rendered)
        self.assertEqual(0, code, rendered)
        self.assertEqual("PASS", report["outcome"])
        self.assertEqual("[REDACTED]", report["baseline"]["trusted_transition"])
        self.assertNotIn(candidate_ref, rendered)
        self.assertNotIn(resolved_sha, rendered)

    def test_text_summary_never_receives_trusted_ref_data(self) -> None:
        candidate_ref = "refs/heads/internal-baseline"
        resolved_sha = "c" * 40
        current_data = {
            "expires_on": "2026-11-10",
            "generated_from_ref": "main@not-bootstrap",
        }
        output = io.StringIO()

        with tempfile.TemporaryDirectory() as directory:
            baseline_path = Path(directory) / "baseline.json"
            baseline_path.write_text("{}\n", encoding="utf-8")
            with (
                mock.patch.object(module, "scan", return_value=((), 0)),
                mock.patch.object(
                    module,
                    "_load_baseline_bytes",
                    side_effect=[(current_data, {}), ({}, {})],
                ),
                mock.patch.object(
                    module,
                    "_git",
                    side_effect=[
                        (resolved_sha + "\n").encode("ascii"),
                        b"{}",
                    ],
                ),
                mock.patch.object(module, "validate_baseline_transition"),
                redirect_stdout(output),
            ):
                code = module.main(
                    [
                        "--repo-root",
                        str(REPO_ROOT),
                        "--baseline",
                        str(baseline_path),
                        "--trusted-baseline-ref",
                        candidate_ref,
                        "--format",
                        "text",
                    ]
                )

        rendered = output.getvalue()
        self.assertEqual(0, code, rendered)
        self.assertTrue(rendered.startswith("PASS:"), rendered)
        self.assertNotIn(candidate_ref, rendered)
        self.assertNotIn(resolved_sha, rendered)

    def test_text_error_reports_only_exception_type(self) -> None:
        candidate_ref = "refs/heads/internal-baseline"
        resolved_sha = "d" * 40
        current_data = {
            "expires_on": "2026-11-10",
            "generated_from_ref": "main@not-bootstrap",
        }
        output = io.StringIO()

        with tempfile.TemporaryDirectory() as directory:
            baseline_path = Path(directory) / "baseline.json"
            baseline_path.write_text("{}\n", encoding="utf-8")
            with (
                mock.patch.object(module, "scan", return_value=((), 0)),
                mock.patch.object(
                    module,
                    "_load_baseline_bytes",
                    return_value=(current_data, {}),
                ),
                mock.patch.object(
                    module,
                    "enforce_trusted_baseline",
                    side_effect=module.TopologyError(
                        f"rejected {candidate_ref} at {resolved_sha}"
                    ),
                ),
                redirect_stdout(output),
            ):
                code = module.main(
                    [
                        "--repo-root",
                        str(REPO_ROOT),
                        "--baseline",
                        str(baseline_path),
                        "--trusted-baseline-ref",
                        candidate_ref,
                        "--format",
                        "text",
                    ]
                )

        rendered = output.getvalue()
        self.assertEqual(2, code, rendered)
        self.assertEqual("ERROR_VALIDATOR: TopologyError\n", rendered)
        self.assertNotIn(candidate_ref, rendered)
        self.assertNotIn(resolved_sha, rendered)


if __name__ == "__main__":
    unittest.main()
