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

from tools.validators.governance.validate_verification_backlog_item import (  # noqa: E402
    FIXTURE_CASE_FILES,
    evaluate_document,
    evaluate_path,
    expected_item_id,
    expected_spec_hash,
    load_fixture_cases,
    run_fixture_suite,
)


class VerificationBacklogItemTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = {case["name"]: case for case in load_fixture_cases()}

    def document(self, name: str) -> dict[str, object]:
        return copy.deepcopy(self.cases[name]["document"])

    def test_fixture_manifest_has_exact_polarity(self) -> None:
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["cases"], 11)
        self.assertEqual(payload["mismatches"], [])

    def test_resolved_item_is_ready(self) -> None:
        document = self.document("ready_resolved")
        evaluation = evaluate_document(document)
        self.assertEqual(evaluation.outcome, "READY", evaluation.findings)
        self.assertEqual(document["resolution"]["status"], "CONFIRMED")
        self.assertTrue(document["acceptance"]["evidence_refs"])
        self.assertTrue(document["acceptance"]["validation_tests"])
        self.assertTrue(all(value is False for value in document["permissions"].values()))

    def test_superseded_item_is_ready(self) -> None:
        document = self.document("ready_superseded")
        evaluation = evaluate_document(document)
        self.assertEqual(evaluation.outcome, "READY", evaluation.findings)
        self.assertIsNotNone(document["lineage"]["superseded_by_item_id"])

    def test_open_item_holds_with_explicit_residue(self) -> None:
        evaluation = evaluate_document(self.document("hold_open_unknown"))
        self.assertEqual(evaluation.outcome, "HOLD")
        self.assertIn("ITEM_UNRESOLVED", {item.code for item in evaluation.findings})
        self.assertIn("RESIDUAL_UNKNOWNS_REMAIN", {item.code for item in evaluation.findings})
        self.assertIn("CONSTRAINT_REVIEW_REQUIRED", {item.code for item in evaluation.findings})

    def test_blocked_sensitive_item_holds(self) -> None:
        evaluation = evaluate_document(self.document("hold_blocked_sensitive_review"))
        self.assertEqual(evaluation.outcome, "HOLD")
        self.assertEqual(
            {item.code for item in evaluation.findings},
            {
                "CONSTRAINT_REVIEW_REQUIRED",
                "ITEM_UNRESOLVED",
                "RESIDUAL_UNKNOWNS_REMAIN",
                "RESOLUTION_NOT_CONFIRMED",
            },
        )

    def test_resolved_claim_without_closure_is_error(self) -> None:
        evaluation = evaluate_document(self.document("error_resolved_without_closure"))
        self.assertEqual(evaluation.outcome, "ERROR")
        self.assertIn("RESOLVED_PRIMARY_EVIDENCE_REQUIRED", {item.code for item in evaluation.findings})
        self.assertIn("RESOLVED_WITH_UNCLEARED_CONSTRAINT", {item.code for item in evaluation.findings})

    def test_identity_and_spec_hash_drift_error(self) -> None:
        identity = evaluate_document(self.document("error_item_id_drift"))
        state = evaluate_document(self.document("error_spec_hash_drift"))
        self.assertEqual(identity.outcome, "ERROR")
        self.assertEqual({item.code for item in identity.findings}, {"ITEM_ID_MISMATCH"})
        self.assertEqual(state.outcome, "ERROR")
        self.assertEqual({item.code for item in state.findings}, {"SPEC_HASH_MISMATCH"})

    def test_identity_excludes_resolution_progress(self) -> None:
        original = self.document("ready_resolved")
        changed = copy.deepcopy(original)
        changed["work_state"] = "IN_PROGRESS"
        changed["resolution"]["status"] = "NEEDS_VERIFICATION"
        changed["resolution"]["answer_summary"] = "Reopened for a newer evidence snapshot."
        changed["updated_at"] = "2030-01-01T00:00:00Z"
        self.assertEqual(expected_item_id(original), expected_item_id(changed))
        self.assertEqual(original["item_id"], expected_item_id(changed))
        self.assertNotEqual(expected_spec_hash(original), expected_spec_hash(changed))

    def test_canonical_order_is_required(self) -> None:
        evaluation = evaluate_document(self.document("error_unsorted_arrays"))
        self.assertEqual(evaluation.outcome, "ERROR")
        self.assertEqual({item.code for item in evaluation.findings}, {"CANONICAL_ORDER_REQUIRED"})

    def test_evidence_mode_must_be_declared(self) -> None:
        evaluation = evaluate_document(self.document("error_evidence_mode_mismatch"))
        self.assertEqual(evaluation.outcome, "ERROR")
        self.assertEqual({item.code for item in evaluation.findings}, {"EVIDENCE_MODE_NOT_DECLARED"})

    def test_supersession_and_blocked_state_must_be_coherent(self) -> None:
        superseded = evaluate_document(self.document("error_superseded_without_target"))
        blocked = evaluate_document(self.document("error_blocked_without_blocker"))
        self.assertEqual({item.code for item in superseded.findings}, {"SUPERSESSION_TARGET_REQUIRED"})
        self.assertEqual({item.code for item in blocked.findings}, {"BLOCKED_WITHOUT_BLOCKER"})

    def test_duplicate_json_keys_fail_as_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"schema_version":"1.0.0","schema_version":"1.0.0"}', encoding="utf-8")
            document, evaluation = evaluate_path(path)
        self.assertIsNone(document)
        self.assertEqual(evaluation.outcome, "ERROR")
        self.assertEqual([item.code for item in evaluation.findings], ["INPUT_JSON_INVALID"])

    def test_schema_closes_authority_overreach(self) -> None:
        document = self.document("ready_resolved")
        document["permissions"]["may_make_governance_decision"] = True
        evaluation = evaluate_document(document)
        self.assertEqual(evaluation.outcome, "ERROR")
        self.assertEqual({item.code for item in evaluation.findings}, {"SCHEMA_INVALID"})

    def test_fixture_suite_is_no_network(self) -> None:
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)

    def test_cli_output_is_deterministic(self) -> None:
        command = [
            sys.executable,
            str(REPO_ROOT / "tools/validators/governance/validate_verification_backlog_item.py"),
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
        self.assertEqual([path.name for path in FIXTURE_CASE_FILES], ["cases_ready_hold.json", "cases_error.json"])


if __name__ == "__main__":
    unittest.main()
