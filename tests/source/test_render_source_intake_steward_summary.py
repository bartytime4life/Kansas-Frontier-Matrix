from __future__ import annotations

import copy
import hashlib
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.ci.render_source_intake_steward_summary import (
    SummaryRenderError,
    main,
    render_source_intake_steward_summary,
)

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "fixtures/contracts/v1/source/source_intake_record"
PROPOSED = FIXTURES / "valid/valid_proposed_work_record.json"
NO_CHANGE = FIXTURES / "valid/valid_no_material_change.json"
QUARANTINE = FIXTURES / "valid/valid_quarantine_blocking.json"


class SourceIntakeStewardSummaryTests(unittest.TestCase):
    @staticmethod
    def _load(path: Path) -> dict[str, object]:
        return json.loads(path.read_text(encoding="utf-8"))

    @staticmethod
    def _write(directory: str, value: dict[str, object]) -> Path:
        path = Path(directory) / "record.json"
        path.write_text(json.dumps(value, sort_keys=True), encoding="utf-8")
        return path

    def test_proposed_work_record_is_deterministic_and_review_ready(self) -> None:
        first = render_source_intake_steward_summary(PROPOSED)
        second = render_source_intake_steward_summary(PROPOSED)
        self.assertEqual(first, second)
        self.assertEqual(first.status, "READY_FOR_REVIEW")
        self.assertFalse(first.blocking)
        self.assertIn("Synthetic county fixture crossed", first.markdown)
        self.assertIn("`REVIEW_FOR_PROCESSED`", first.markdown)
        expected = "sha256:" + hashlib.sha256(PROPOSED.read_bytes()).hexdigest()
        self.assertEqual(first.source_record_sha256, expected)
        self.assertIn(expected, first.markdown)

    def test_no_change_is_no_action(self) -> None:
        result = render_source_intake_steward_summary(NO_CHANGE)
        self.assertEqual(result.status, "NO_ACTION")
        self.assertFalse(result.blocking)
        self.assertIn("`NO_ACTION`", result.markdown)
        self.assertNotIn("`REVIEW_FOR_PROCESSED`", result.markdown)

    def test_sensitive_quarantine_redacts_detail(self) -> None:
        result = render_source_intake_steward_summary(QUARANTINE)
        self.assertEqual(result.status, "HOLD")
        self.assertTrue(result.blocking)
        self.assertIn("Sensitive or non-public drift detail is redacted", result.markdown)
        self.assertIn("**Changed fields:** `REDACTED`", result.markdown)
        self.assertNotIn("fixture-sensitive", result.markdown)
        self.assertNotIn("Synthetic taxonomy drift", result.markdown)

    def test_missing_rollback_target_holds_work_proposal(self) -> None:
        value = copy.deepcopy(self._load(PROPOSED))
        del value["drift_summary"]["prior_identity_ref"]  # type: ignore[index]
        with tempfile.TemporaryDirectory() as directory:
            path = self._write(directory, value)
            result = render_source_intake_steward_summary(path)
        self.assertEqual(result.status, "HOLD")
        self.assertIn("`ROLLBACK_TARGET_NOT_DECLARED`", result.markdown)
        self.assertNotIn("`REVIEW_FOR_PROCESSED`", result.markdown)

    def test_markdown_metacharacters_are_escaped(self) -> None:
        value = copy.deepcopy(self._load(PROPOSED))
        value["drift_summary"]["summary"] = "[fixture](https://invalid.example) | *changed*"  # type: ignore[index]
        with tempfile.TemporaryDirectory() as directory:
            path = self._write(directory, value)
            result = render_source_intake_steward_summary(path)
        self.assertIn(r"\[fixture\]\(https://invalid\.example\)", result.markdown)
        self.assertIn(r"\| \*changed\*", result.markdown)
        self.assertNotIn("[fixture](https://invalid.example)", result.markdown)

    def test_invalid_record_returns_value_free_error(self) -> None:
        invalid = FIXTURES / "invalid/invalid_direct_publish.json"
        with self.assertRaises(SummaryRenderError) as raised:
            render_source_intake_steward_summary(invalid)
        self.assertEqual(raised.exception.code, "SCHEMA_INVALID")
        self.assertNotIn("PUBLISHED", str(raised.exception))

    def test_duplicate_key_input_fails_without_echo(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"object_type":"secret-value","object_type":"duplicate"}', encoding="utf-8")
            with self.assertRaises(SummaryRenderError) as raised:
                render_source_intake_steward_summary(path)
        self.assertEqual(raised.exception.code, "JSON_DUPLICATE_KEY")
        self.assertNotIn("secret-value", str(raised.exception))

    def test_no_network_is_required(self) -> None:
        def deny(*_args: object, **_kwargs: object) -> object:
            raise AssertionError("network access attempted")
        with (
            mock.patch.object(socket, "socket", side_effect=deny),
            mock.patch.object(socket, "create_connection", side_effect=deny),
            mock.patch.object(socket, "getaddrinfo", side_effect=deny),
        ):
            self.assertEqual(render_source_intake_steward_summary(PROPOSED).status, "READY_FOR_REVIEW")

    def test_cli_writes_summary_and_preserves_blocking_exit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "summary.md"
            self.assertEqual(main(["--record", str(QUARANTINE), "--output", str(output)]), 1)
            self.assertIn("# Source Intake Steward Summary", output.read_text(encoding="utf-8"))

    def test_output_symlink_is_denied(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target.md"
            target.write_text("do not overwrite", encoding="utf-8")
            link = root / "summary.md"
            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("symlink unavailable")
            with self.assertRaises(SummaryRenderError) as raised:
                render_source_intake_steward_summary(PROPOSED, link)
            self.assertEqual(raised.exception.code, "OUTPUT_SYMLINK_DENIED")
            self.assertEqual(target.read_text(encoding="utf-8"), "do not overwrite")


if __name__ == "__main__":
    unittest.main()
