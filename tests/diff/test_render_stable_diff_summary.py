from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.ci.render_stable_diff_summary import (
    SummaryRenderError,
    main,
    render_stable_diff_summary,
)


class StableDiffSummaryTests(unittest.TestCase):
    def _write_report(self, directory: str, report: dict[str, object]) -> Path:
        path = Path(directory) / "report.json"
        path.write_text(json.dumps(report, sort_keys=True), encoding="utf-8")
        return path

    @staticmethod
    def _same_report() -> dict[str, object]:
        return {
            "tool": "stable-diff",
            "status": "same",
            "blocking": False,
            "left": "fixtures/same/left.json",
            "right": "fixtures/same/right.json",
            "summary": {"added": [], "removed": [], "changed": []},
        }

    @staticmethod
    def _changed_report(*, blocking: bool = False) -> dict[str, object]:
        return {
            "tool": "stable-diff",
            "status": "changed",
            "blocking": blocking,
            "left": "/tmp/work/left.json",
            "right": "/tmp/work/right.json",
            "summary": {
                "added": ["new_key"],
                "removed": ["old_key"],
                "changed": ["shared_key"],
            },
        }

    @staticmethod
    def _error_report() -> dict[str, object]:
        return {
            "tool": "stable-diff",
            "status": "error",
            "blocking": True,
            "left": "left.json",
            "right": "right.json",
            "summary": {"added": [], "removed": [], "changed": []},
            "error": {
                "code": "RIGHT_JSON_INVALID",
                "message": "right input is malformed JSON at line 1, column 2.",
            },
        }

    def test_same_report_renders_deterministically(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_report(directory, self._same_report())
            first = render_stable_diff_summary(path)
            second = render_stable_diff_summary(path)
        self.assertEqual(first.markdown, second.markdown)
        self.assertEqual(first.status, "same")
        self.assertEqual(first.exit_code, 0)
        self.assertIn("- **Changed top-level keys:** `0`", first.markdown)

    def test_changed_report_is_bounded_and_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_report(directory, self._changed_report())
            first = render_stable_diff_summary(path)
            second = render_stable_diff_summary(path)
        self.assertEqual(first.markdown, second.markdown)
        self.assertEqual(first.exit_code, 0)
        self.assertIn('`"new_key"`', first.markdown)
        self.assertIn('`"old_key"`', first.markdown)
        self.assertIn('`"shared_key"`', first.markdown)
        self.assertNotIn("/tmp/work/", first.markdown)
        self.assertIn("does not compare source bytes", first.markdown)

    def test_blocking_changed_report_returns_one(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_report(directory, self._changed_report(blocking=True))
            output = Path(directory) / "summary.md"
            self.assertEqual(main(["--report", str(path), "--output", str(output)]), 1)
            self.assertTrue(output.is_file())

    def test_error_report_surfaces_code_not_message(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_report(directory, self._error_report())
            result = render_stable_diff_summary(path)
        self.assertEqual(result.exit_code, 2)
        self.assertIn("RIGHT_JSON_INVALID", result.markdown)
        self.assertNotIn("malformed JSON", result.markdown)

    def test_contradictory_status_fails_closed(self) -> None:
        report = self._same_report()
        report["summary"] = {"added": [], "removed": [], "changed": ["unexpected"]}
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_report(directory, report)
            with self.assertRaisesRegex(SummaryRenderError, "STATUS_CONTRADICTION"):
                render_stable_diff_summary(path)

    def test_noncanonical_arrays_fail_closed(self) -> None:
        report = self._changed_report()
        report["summary"] = {"added": ["z", "a"], "removed": [], "changed": []}
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_report(directory, report)
            with self.assertRaisesRegex(SummaryRenderError, "SUMMARY_ARRAY_NOT_CANONICAL"):
                render_stable_diff_summary(path)

    def test_markdown_metacharacters_are_escaped(self) -> None:
        report = self._changed_report()
        report["summary"] = {"added": ["a|b`c"], "removed": [], "changed": []}
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_report(directory, report)
            result = render_stable_diff_summary(path)
        self.assertIn("\\|", result.markdown)
        self.assertIn("\\`", result.markdown)

    def test_extra_fields_fail_closed(self) -> None:
        report = self._same_report()
        report["authority"] = "invented"
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_report(directory, report)
            with self.assertRaisesRegex(SummaryRenderError, "REPORT_SHAPE_INVALID"):
                render_stable_diff_summary(path)


if __name__ == "__main__":
    unittest.main()
