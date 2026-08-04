#!/usr/bin/env python3
"""Deterministic event-cluster and issue-routing dry-run tests."""
from __future__ import annotations

import copy
import io
import json
import socket
import tempfile
import unittest
import urllib.request
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from tools.validators.governance.deduplicate_briefing_signals import (
    evaluate,
    main,
    serialize_report,
)
from tools.validators.governance.validate_briefing_signal import (
    compute_issue_idempotency_key,
    compute_signal_digest,
    compute_signal_id,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
VALID_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/briefing_signal/valid"
PRIMARY = VALID_ROOT / "valid_1.json"
FOLLOWUP = VALID_ROOT / "valid_duplicate_followup.json"
INVALID_DUPLICATE = (
    REPO_ROOT
    / "fixtures/contracts/v1/governance/briefing_signal/invalid/invalid_duplicate_issue_create.json"
)


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _write(path: Path, candidate: dict) -> None:
    path.write_text(json.dumps(candidate, indent=2) + "\n", encoding="utf-8")


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("BriefingSignal dedup dry-run attempted network access")


class BriefingSignalDedupTests(unittest.TestCase):
    def setUp(self):
        self.network_mocks = []
        for patcher in (
            patch.object(socket.socket, "connect", side_effect=_unexpected_network),
            patch.object(socket.socket, "connect_ex", side_effect=_unexpected_network),
            patch.object(socket, "create_connection", side_effect=_unexpected_network),
            patch.object(socket, "getaddrinfo", side_effect=_unexpected_network),
            patch.object(urllib.request, "urlopen", side_effect=_unexpected_network),
        ):
            self.network_mocks.append(patcher.start())
            self.addCleanup(patcher.stop)

    def test_same_story_revised_headline_forms_one_cluster(self):
        report = evaluate([PRIMARY, FOLLOWUP])
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(len(report["clusters"]), 1)
        cluster = report["clusters"][0]
        self.assertEqual(cluster["distinct_signal_count"], 2)
        self.assertEqual(cluster["primary_signal_id"], _load(PRIMARY)["signal_id"])

    def test_input_order_does_not_change_report(self):
        first = serialize_report(evaluate([PRIMARY, FOLLOWUP]))
        second = serialize_report(evaluate([FOLLOWUP, PRIMARY]))
        self.assertEqual(first, second)

    def test_replayed_input_is_idempotently_counted_not_recreated(self):
        report = evaluate([PRIMARY, PRIMARY, FOLLOWUP])
        self.assertEqual(report["status"], "PASS")
        cluster = report["clusters"][0]
        self.assertEqual(cluster["distinct_signal_count"], 2)
        self.assertEqual(cluster["replay_count"], 3)
        self.assertEqual(len(report["operations"]), 2)

    def test_duplicate_issue_create_is_rejected_before_projection(self):
        report = evaluate([PRIMARY, INVALID_DUPLICATE])
        codes = {item["code"] for item in report["findings"]}
        self.assertEqual(report["status"], "FAIL")
        self.assertIn("INPUT_DUPLICATE_CANNOT_OPEN_ISSUE", codes)
        self.assertFalse(report["repository_mutation_allowed"])
        self.assertFalse(report["authority_created"])

    def test_unclassified_same_cluster_is_rejected(self):
        primary = _load(PRIMARY)
        followup = _load(FOLLOWUP)
        followup["status"] = "NEEDS_VERIFICATION"
        followup["deduplication"] = {
            "status": "UNRESOLVED",
            "matched_signal_ids": [],
            "matched_issue_ids": [],
            "reason_codes": ["NO_MATCH_EVIDENCE"],
        }
        followup["next_action"]["idempotency_key"] = compute_issue_idempotency_key(followup)
        with tempfile.TemporaryDirectory() as directory:
            p1 = Path(directory) / "primary.json"
            p2 = Path(directory) / "followup.json"
            _write(p1, primary)
            _write(p2, followup)
            report = evaluate([p1, p2])
        codes = {item["code"] for item in report["findings"]}
        self.assertIn("DUPLICATE_CLASSIFICATION_REQUIRED", codes)
        self.assertIn("PRIMARY_SIGNAL_REFERENCE_REQUIRED", codes)

    def test_signal_id_collision_is_detected(self):
        primary = _load(PRIMARY)
        collision = copy.deepcopy(primary)
        collision["headline"] = "Different content forced under the same declared signal ID"
        collision["identity"]["signal_digest"] = compute_signal_digest(collision)
        collision["next_action"]["idempotency_key"] = compute_issue_idempotency_key(collision)
        self.assertNotEqual(compute_signal_id(collision), primary["signal_id"])
        collision["signal_id"] = primary["signal_id"]
        with tempfile.TemporaryDirectory() as directory:
            p1 = Path(directory) / "primary.json"
            p2 = Path(directory) / "collision.json"
            _write(p1, primary)
            _write(p2, collision)
            report = evaluate([p1, p2])
        codes = {item["code"] for item in report["findings"]}
        self.assertIn("INPUT_SIGNAL_ID_MISMATCH", codes)

    def test_cli_is_deterministic_and_dry_run_only(self):
        outputs = []
        for _ in range(2):
            stream = io.StringIO()
            with redirect_stdout(stream):
                code = main([str(PRIMARY), str(FOLLOWUP)])
            self.assertEqual(code, 0)
            outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertIn('"repository_mutation_allowed":false', outputs[0])
        self.assertIn('"authority_created":false', outputs[0])

    def test_no_network_calls_occur(self):
        evaluate([PRIMARY, FOLLOWUP])
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
