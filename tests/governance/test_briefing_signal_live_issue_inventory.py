#!/usr/bin/env python3
"""Stored GitHubIssueInventoryRead binding tests for BriefingSignal routing."""
from __future__ import annotations

import socket
import unittest
import urllib.request
from pathlib import Path
from unittest.mock import patch

from tools.validators.governance.route_briefing_signals import evaluate
from tools.validators.governance.validate_github_issue_inventory_read import (
    compute_digest,
    compute_receipt_id,
    validate_record,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
RECEIPT = REPO_ROOT / "fixtures/contracts/v1/governance/github_issue_inventory_read/fresh_receipt_1647.json"
EXAMPLES = sorted((REPO_ROOT / "examples/briefing_integration").glob("*.json"))


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("briefing live-read binding attempted network access")


class BriefingSignalLiveIssueInventoryTests(unittest.TestCase):
    def setUp(self):
        self.patchers = [
            patch.object(socket.socket, "connect", side_effect=_unexpected_network),
            patch.object(socket.socket, "connect_ex", side_effect=_unexpected_network),
            patch.object(socket, "create_connection", side_effect=_unexpected_network),
            patch.object(socket, "getaddrinfo", side_effect=_unexpected_network),
            patch.object(urllib.request, "urlopen", side_effect=_unexpected_network),
        ]
        self.mocks = [p.start() for p in self.patchers]
        for p in self.patchers:
            self.addCleanup(p.stop)

    def test_fresh_receipt_identity_is_reproducible(self):
        result = validate_record(RECEIPT, as_of="2026-08-08T02:31:00Z")
        self.assertTrue(result.ok)
        assert result.payload is not None
        self.assertEqual(result.payload["response_digest"], compute_digest(result.payload))
        self.assertEqual(result.payload["receipt_id"], compute_receipt_id(result.payload))
        self.assertFalse(result.payload["repository_mutation_allowed"])
        self.assertFalse(result.payload["authority_created"])

    def test_fresh_live_receipt_binds_existing_issue(self):
        report = evaluate(
            EXAMPLES,
            live_issue_inventory_path=RECEIPT,
            as_of="2026-08-08T02:31:00Z",
        )
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["issue_inventory"]["profile"], "github-live-read-v1")
        for signal in report["signals"]:
            routing = signal["routing"]
            self.assertEqual(routing["disposition"], "UPDATE_EXISTING_ISSUE")
            self.assertEqual(routing["inventory_status"], "BOUND_OPEN_TARGET_LIVE_READ")
            self.assertEqual(routing["target_issue_ids"], [1647])
            self.assertIn("ISSUE_INVENTORY_LIVE_READ_FRESH", routing["reason_codes"])

    def test_stale_receipt_fails_closed_before_routing(self):
        report = evaluate(
            EXAMPLES,
            live_issue_inventory_path=RECEIPT,
            as_of="2026-08-08T02:36:00Z",
        )
        self.assertEqual(report["status"], "FAIL")
        self.assertEqual(report["signals"], [])
        self.assertIn(
            "LIVE_ISSUE_INVENTORY_LIVE_READ_STALE_AT_AS_OF",
            {finding["code"] for finding in report["findings"]},
        )

    def test_as_of_is_required_for_live_receipt(self):
        report = evaluate(EXAMPLES, live_issue_inventory_path=RECEIPT)
        self.assertEqual(report["status"], "FAIL")
        self.assertEqual(report["signals"], [])
        self.assertEqual(report["findings"][0]["code"], "LIVE_ISSUE_INVENTORY_AS_OF_REQUIRED")

    def test_fixture_and_live_inputs_cannot_be_combined(self):
        fixture = REPO_ROOT / "fixtures/contracts/v1/governance/issue_inventory_projection/valid/open-target.json"
        report = evaluate(
            EXAMPLES,
            issue_inventory_path=fixture,
            live_issue_inventory_path=RECEIPT,
            as_of="2026-08-08T02:31:00Z",
        )
        self.assertEqual(report["status"], "FAIL")
        self.assertEqual(report["findings"][0]["code"], "ISSUE_INVENTORY_INPUT_AMBIGUOUS")

    def test_binding_path_never_calls_network(self):
        evaluate(
            EXAMPLES,
            live_issue_inventory_path=RECEIPT,
            as_of="2026-08-08T02:31:00Z",
        )
        for mock in self.mocks:
            mock.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
