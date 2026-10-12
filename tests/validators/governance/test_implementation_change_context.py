from __future__ import annotations

import copy
import json
import os
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
for path in (REPO_ROOT, HASHING_SRC):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from tools.validators.governance.validate_implementation_change_context import (  # noqa: E402
    CASES,
    GitContextError,
    build_from_git,
    evaluate_document,
    evaluate_path,
    expected_context_id,
    expected_summary,
    load_fixture_cases,
    run_fixture_suite,
    signal_codes,
)


class ImplementationChangeContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(CASES.read_text(encoding="utf-8"))
        cls.cases = {case["name"]: case for case in load_fixture_cases()}

    def document(self, name: str) -> dict[str, object]:
        return copy.deepcopy(self.cases[name]["document"])

    def test_fixture_manifest_has_exact_polarity(self) -> None:
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["cases"], 11)
        self.assertEqual(payload["mismatches"], [])

    def test_ready_context_is_value_minimized_and_non_authoritative(self) -> None:
        document = self.document("ready_attention_bound")
        evaluation = evaluate_document(document)
        self.assertEqual(evaluation.outcome, "READY", evaluation.findings)
        self.assertTrue(document["summary"]["decision_capture_recommended"])
        self.assertFalse(document["content_boundary"]["raw_diff_included"])
        self.assertFalse(document["content_boundary"]["file_content_included"])
        self.assertTrue(document["content_boundary"]["value_minimized"])
        self.assertTrue(all(value is False for value in document["permissions"].values()))

    def test_draft_context_holds(self) -> None:
        evaluation = evaluate_document(self.document("hold_draft"))
        self.assertEqual(evaluation.outcome, "HOLD")
        self.assertEqual([item.code for item in evaluation.findings], ["CONTEXT_DRAFT"])

    def test_recommended_decision_capture_holds_without_reference(self) -> None:
        evaluation = evaluate_document(self.document("hold_missing_decision_ref"))
        self.assertEqual(evaluation.outcome, "HOLD")
        self.assertEqual(
            [item.code for item in evaluation.findings],
            ["IMPLEMENTATION_DECISION_REFERENCE_RECOMMENDED"],
        )

    def test_test_fixture_only_context_can_be_ready_without_decision_record(self) -> None:
        document = self.document("ready_test_fixture_only")
        evaluation = evaluate_document(document)
        self.assertEqual(evaluation.outcome, "READY", evaluation.findings)
        self.assertFalse(document["summary"]["decision_capture_recommended"])
        self.assertEqual(
            document["summary"]["signal_codes"],
            ["CROSS_ROOT", "TEST_OR_FIXTURE_ONLY"],
        )

    def test_sensitive_path_name_is_only_a_mechanical_signal(self) -> None:
        document = self.document("hold_sensitive_path_without_decision_ref")
        self.assertIn("SENSITIVE_PATH_NAME", document["summary"]["signal_codes"])
        self.assertEqual(evaluate_document(document).outcome, "HOLD")

    def test_summary_and_identity_drift_error(self) -> None:
        summary = evaluate_document(self.document("error_summary_drift"))
        identity = evaluate_document(self.document("error_context_id_drift"))
        self.assertEqual(summary.outcome, "ERROR")
        self.assertIn("SUMMARY_MISMATCH", {item.code for item in summary.findings})
        self.assertEqual(identity.outcome, "ERROR")
        self.assertIn("CONTEXT_ID_MISMATCH", {item.code for item in identity.findings})

    def test_raw_diff_field_is_closed_by_schema(self) -> None:
        evaluation = evaluate_document(self.document("error_raw_diff_field"))
        self.assertEqual(evaluation.outcome, "ERROR")
        self.assertEqual({item.code for item in evaluation.findings}, {"SCHEMA_INVALID"})

    def test_binary_metrics_and_rename_shape_error(self) -> None:
        binary = evaluate_document(self.document("error_binary_metrics"))
        rename = evaluate_document(self.document("error_rename_without_previous_path"))
        self.assertIn("BINARY_METRICS_MUST_BE_NULL", {item.code for item in binary.findings})
        self.assertIn("PREVIOUS_PATH_REQUIRED", {item.code for item in rename.findings})

    def test_file_order_is_canonical(self) -> None:
        evaluation = evaluate_document(self.document("error_unsorted_files"))
        self.assertEqual(evaluation.outcome, "ERROR")
        self.assertIn("CANONICAL_FILE_ORDER_REQUIRED", {item.code for item in evaluation.findings})

    def test_unicode_repository_path_is_admitted_when_canonical(self) -> None:
        document = self.document("ready_attention_bound")
        document["files"][1]["path"] = "docs/adr/ADR-0007 — renderer boundary.md"
        document["files"] = sorted(
            document["files"],
            key=lambda item: (item["path"], item["status"], item["previous_path"] or ""),
        )
        document["summary"] = expected_summary(document["files"])
        document["context_id"] = expected_context_id(document)
        self.assertEqual(evaluate_document(document).outcome, "READY")

    def test_identity_excludes_timestamp_status_and_decision_references(self) -> None:
        original = self.document("ready_attention_bound")
        changed = copy.deepcopy(original)
        changed["generated_at"] = "2030-01-01T00:00:00Z"
        changed["status"] = "DRAFT"
        changed["implementation_decision_refs"] = []
        self.assertEqual(expected_context_id(original), expected_context_id(changed))
        self.assertEqual(original["context_id"], expected_context_id(changed))

    def test_signal_derivation_is_deterministic(self) -> None:
        files = self.document("ready_attention_bound")["files"]
        first = signal_codes(files)
        second = signal_codes(copy.deepcopy(files))
        self.assertEqual(first, second)
        self.assertEqual(
            first,
            ["AUTHORITY_SURFACE", "CROSS_ROOT", "LARGE_CHANGE", "WORKFLOW_SURFACE"],
        )

    def test_duplicate_json_keys_fail_as_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"schema_version":"1.0.0","schema_version":"1.0.0"}', encoding="utf-8")
            document, evaluation = evaluate_path(path)
        self.assertIsNone(document)
        self.assertEqual(evaluation.outcome, "ERROR")
        self.assertEqual([item.code for item in evaluation.findings], ["INPUT_JSON_INVALID"])

    def test_fixture_suite_does_not_use_network(self) -> None:
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)

    def _git(self, root: Path, *args: str, env: dict[str, str] | None = None) -> str:
        completed = subprocess.run(
            ["git", "-C", str(root), *args],
            check=True,
            capture_output=True,
            text=True,
            env=env,
        )
        return completed.stdout.strip()

    def _make_git_repository(self, root: Path) -> tuple[str, str]:
        self._git(root, "init", "-q")
        self._git(root, "config", "user.name", "KFM Test")
        self._git(root, "config", "user.email", "kfm-test@example.invalid")
        (root / "contracts/governance").mkdir(parents=True)
        (root / "contracts/governance/example.md").write_text("".join(f"baseline-{index}\n" for index in range(12)), encoding="utf-8")
        self._git(root, "add", ".")
        base_env = {
            **os.environ,
            "GIT_AUTHOR_DATE": "2026-08-06T20:00:00Z",
            "GIT_COMMITTER_DATE": "2026-08-06T20:00:00Z",
        }
        self._git(root, "commit", "-qm", "base", env=base_env)
        base = self._git(root, "rev-parse", "HEAD")

        self._git(root, "mv", "contracts/governance/example.md", "contracts/governance/renamed.md")
        (root / "contracts/governance/renamed.md").write_text(
            "".join(f"baseline-{index}\n" for index in range(12)) + "SECRET_MARKER_THAT_MUST_NOT_APPEAR_IN_CONTEXT\n",
            encoding="utf-8",
        )
        (root / "tests").mkdir()
        (root / "tests/test_example.py").write_text("def test_example():\n    assert True\n", encoding="utf-8")
        (root / "fixtures").mkdir()
        (root / "fixtures/blob.bin").write_bytes(b"\x00\x01\x02")
        self._git(root, "add", ".")
        head_env = {
            **os.environ,
            "GIT_AUTHOR_DATE": "2026-08-06T21:30:00-05:00",
            "GIT_COMMITTER_DATE": "2026-08-06T21:30:00-05:00",
        }
        self._git(root, "commit", "-qm", "head", env=head_env)
        head = self._git(root, "rev-parse", "HEAD")
        return base, head

    def test_git_builder_is_deterministic_and_excludes_diff_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            base, head = self._make_git_repository(root)
            first = build_from_git(
                root,
                repository="example/kfm",
                base_ref=base,
                head_ref=head,
                status="READY_FOR_REVIEW",
                implementation_decision_refs=["kfm:implementation-decision:example:0001"],
            )
            second = build_from_git(
                root,
                repository="example/kfm",
                base_ref=base,
                head_ref=head,
                status="READY_FOR_REVIEW",
                implementation_decision_refs=["kfm:implementation-decision:example:0001"],
            )
        self.assertEqual(first, second)
        self.assertEqual(evaluate_document(first).outcome, "READY")
        rendered = json.dumps(first, sort_keys=True)
        self.assertNotIn("SECRET_MARKER", rendered)
        self.assertNotIn("raw_diff", first)
        self.assertEqual(first["generated_at"], "2026-08-07T02:30:00Z")
        binary = next(item for item in first["files"] if item["path"] == "fixtures/blob.bin")
        self.assertTrue(binary["binary"])
        self.assertIsNone(binary["additions"])
        renamed = next(item for item in first["files"] if item["status"] == "RENAMED")
        self.assertEqual(renamed["previous_path"], "contracts/governance/example.md")

    def test_git_builder_rejects_empty_range(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            base, _head = self._make_git_repository(root)
            with self.assertRaises(GitContextError):
                build_from_git(
                    root,
                    repository="example/kfm",
                    base_ref=base,
                    head_ref=base,
                )

    def test_cli_output_is_deterministic(self) -> None:
        path = CASES
        command = [
            sys.executable,
            str(REPO_ROOT / "tools/validators/governance/validate_implementation_change_context.py"),
            "--cases",
        ]
        environment = dict(os.environ)
        environment["KFM_NO_NETWORK"] = "1"
        first = subprocess.run(command, cwd=REPO_ROOT, env=environment, check=False, capture_output=True, text=True)
        second = subprocess.run(command, cwd=REPO_ROOT, env=environment, check=False, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        payload = json.loads(first.stdout)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(path, CASES)


if __name__ == "__main__":
    unittest.main()
