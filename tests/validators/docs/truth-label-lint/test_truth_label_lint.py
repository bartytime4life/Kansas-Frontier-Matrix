#!/usr/bin/env python3
"""Focused no-network tests for the opt-in KFM assessment-axis linter."""

from __future__ import annotations

import ast
import importlib.util
import io
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import urllib.request


REPO_ROOT = Path(__file__).resolve().parents[4]
SCRIPT = REPO_ROOT / "tools/validators/docs/truth-label-lint/lint_truth_labels.py"
CASES = Path(__file__).with_name("cases.json")

spec = importlib.util.spec_from_file_location("kfm_truth_label_lint", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError(f"could not load validator module: {SCRIPT}")
linter = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = linter
spec.loader.exec_module(linter)


class TruthLabelLintTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = json.loads(CASES.read_text(encoding="utf-8"))["cases"]

    def test_reviewed_fixture_matrix_has_exact_outcomes_and_codes(self) -> None:
        self.assertGreaterEqual(len(self.cases), 10)
        for case in self.cases:
            with self.subTest(case=case["id"]):
                result = linter.lint_text(case["markdown"], path=case["id"])
                self.assertEqual(case["expected_outcome"], result.outcome)
                expected_codes = set(case.get("expected_codes", []))
                actual_codes = {finding.code for finding in result.findings}
                self.assertTrue(
                    expected_codes.issubset(actual_codes),
                    (expected_codes, actual_codes),
                )

    def test_valid_table_preserves_declared_values_without_interpreting_them(self) -> None:
        result = linter.lint_text(
            "<!-- KFM-ASSESSMENT-AXES: REQUIRED -->\n\n"
            "| Axis | Current result | Notes |\n"
            "|:---|:---:|---:|\n"
            "| Authority / epistemic posture | CUSTOM-BOUNDED | source-scoped |\n"
            "| Capability maturity | EXPERIMENTAL | fixture-only |\n"
        )
        self.assertEqual(linter.PASS, result.outcome)
        self.assertEqual("CUSTOM-BOUNDED", result.authority_posture)
        self.assertEqual("EXPERIMENTAL", result.capability_maturity)
        self.assertEqual((), result.findings)

    def test_require_marker_is_explicit_and_fail_closed(self) -> None:
        result = linter.lint_text(
            "# Assessment\n",
            require_marker=True,
        )
        self.assertEqual(linter.FAIL, result.outcome)
        self.assertEqual([linter.MARKER_MISSING], [item.code for item in result.findings])

    def test_directory_discovery_is_sorted_and_does_not_follow_symlinks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "b.md").write_text("# B\n", encoding="utf-8")
            (root / "a.md").write_text("# A\n", encoding="utf-8")
            nested = root / "nested"
            nested.mkdir()
            (nested / "c.md").write_text("# C\n", encoding="utf-8")
            (root / "ignored.txt").write_text("text", encoding="utf-8")
            symlink = root / "linked.md"
            try:
                symlink.symlink_to(root / "a.md")
            except (OSError, NotImplementedError):
                symlink = None

            paths, errors = linter.discover_markdown([root])
            self.assertEqual((), errors)
            self.assertEqual(
                ["a.md", "b.md", "nested/c.md"],
                [path.relative_to(root).as_posix() for path in paths],
            )
            if symlink is not None:
                _, explicit_errors = linter.discover_markdown([symlink])
                self.assertEqual(linter.ERROR, explicit_errors[0].code)

    def test_malformed_utf8_is_operational_error_not_lint_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.md"
            path.write_bytes(b"\xff")
            result = linter.lint_path(path)
        self.assertEqual(linter.ERROR, result.outcome)
        self.assertEqual(linter.ERROR, result.findings[0].code)

    def test_json_report_is_byte_deterministic(self) -> None:
        results = tuple(
            linter.lint_text(case["markdown"], path=case["id"])
            for case in self.cases
        )
        first = linter._json_report(results, ())
        second = linter._json_report(results, ())
        self.assertEqual(first, second)
        payload = json.loads(first)
        self.assertEqual(linter.FAIL, payload["outcome"])
        self.assertEqual(len(self.cases), payload["summary"]["files"])
        self.assertIn("no truth", payload["authority_boundary"].lower())

    def test_main_uses_finite_exit_codes_and_reports_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "assessment.md"
            path.write_text(self.cases[0]["markdown"], encoding="utf-8")
            stdout = io.StringIO()
            with mock.patch.object(sys, "stdout", stdout):
                code = linter.main([path.as_posix(), "--format", "json"])
        self.assertEqual(0, code)
        payload = json.loads(stdout.getvalue())
        self.assertEqual(linter.PASS, payload["outcome"])
        self.assertEqual(1, payload["summary"]["pass"])

    def test_execution_has_no_network_process_or_model_dependency(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "assessment.md"
            path.write_text(self.cases[0]["markdown"], encoding="utf-8")
            with mock.patch.object(
                socket, "create_connection", side_effect=AssertionError("network denied")
            ), mock.patch.object(
                socket, "getaddrinfo", side_effect=AssertionError("dns denied")
            ), mock.patch.object(
                urllib.request, "urlopen", side_effect=AssertionError("url denied")
            ), mock.patch.object(
                subprocess, "run", side_effect=AssertionError("process denied")
            ):
                result = linter.lint_path(path)
        self.assertEqual(linter.PASS, result.outcome)

        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"), filename=str(SCRIPT))
        imported_roots: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".", 1)[0])
        self.assertTrue(
            imported_roots.isdisjoint(
                {"requests", "httpx", "urllib", "socket", "subprocess", "openai"}
            ),
            imported_roots,
        )


if __name__ == "__main__":
    unittest.main()
