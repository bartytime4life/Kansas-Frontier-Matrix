#!/usr/bin/env python3
"""Fixture-backed BriefingSignal issue-inventory projection tests."""
from __future__ import annotations

import io
import json
import socket
import unittest
import urllib.request
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from tools.validators.governance.route_briefing_signals import (
    evaluate,
    main as route_main,
    serialize_report,
)
from tools.validators.governance.validate_issue_inventory_projection import (
    bind_issue_inventory,
    compute_projection_digest,
    compute_projection_id,
    main as projection_main,
    validate_projection,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
PROJECTION_ROOT = (
    REPO_ROOT
    / "fixtures/contracts/v1/governance/issue_inventory_projection"
)
VALID_ROOT = PROJECTION_ROOT / "valid"
INVALID_ROOT = PROJECTION_ROOT / "invalid"
EXAMPLE_ROOT = REPO_ROOT / "examples/briefing_integration"
SIGNAL_VALID_ROOT = (
    REPO_ROOT / "fixtures/contracts/v1/governance/briefing_signal/valid"
)
OPEN = VALID_ROOT / "open-target.json"
CLOSED = VALID_ROOT / "closed-target.json"
MISSING = VALID_ROOT / "missing-target.json"

EXPECTED_INVALID_CODES = {
    "digest-mismatch.json": {"PROJECTION_DIGEST_MISMATCH"},
    "duplicate-issue-number.json": {"ISSUE_NUMBER_DUPLICATE"},
    "unsorted-issues.json": {"ISSUES_NOT_SORTED"},
    "mutation-allowed.json": {"SCHEMA_INVALID"},
    "issue-updated-after-projection.json": {
        "ISSUE_UPDATED_AFTER_PROJECTION"
    },
}


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError(
        "IssueInventoryProjection attempted network access"
    )


class BriefingSignalIssueInventoryTests(unittest.TestCase):
    def setUp(self):
        self.network_mocks = []
        for patcher in (
            patch.object(
                socket.socket,
                "connect",
                side_effect=_unexpected_network,
            ),
            patch.object(
                socket.socket,
                "connect_ex",
                side_effect=_unexpected_network,
            ),
            patch.object(
                socket,
                "create_connection",
                side_effect=_unexpected_network,
            ),
            patch.object(
                socket,
                "getaddrinfo",
                side_effect=_unexpected_network,
            ),
            patch.object(
                urllib.request,
                "urlopen",
                side_effect=_unexpected_network,
            ),
        ):
            self.network_mocks.append(patcher.start())
            self.addCleanup(patcher.stop)

    def test_valid_projection_fixtures_are_closed_and_reproducible(self):
        paths = sorted(VALID_ROOT.glob("*.json"))
        self.assertEqual(
            {path.name for path in paths},
            {
                "open-target.json",
                "closed-target.json",
                "missing-target.json",
            },
        )
        for path in paths:
            with self.subTest(path=path.name):
                result = validate_projection(path)
                self.assertTrue(result.ok)
                self.assertEqual(result.findings, ())
                self.assertIsNotNone(result.payload)
                assert result.payload is not None
                self.assertEqual(
                    result.payload["projection_digest"],
                    compute_projection_digest(result.payload),
                )
                self.assertEqual(
                    result.payload["projection_id"],
                    compute_projection_id(result.payload),
                )
                self.assertFalse(
                    result.payload["live_state_verified"]
                )
                self.assertFalse(
                    result.payload["authority_created"]
                )
                self.assertFalse(
                    result.payload["repository_mutation_allowed"]
                )

    def test_invalid_projection_fixtures_fail_closed(self):
        paths = sorted(INVALID_ROOT.glob("*.json"))
        self.assertEqual(
            {path.name for path in paths},
            set(EXPECTED_INVALID_CODES),
        )
        for path in paths:
            with self.subTest(path=path.name):
                result = validate_projection(path)
                self.assertFalse(result.ok)
                self.assertIsNone(result.payload)
                codes = {finding.code for finding in result.findings}
                self.assertTrue(
                    EXPECTED_INVALID_CODES[path.name].issubset(codes)
                )

    def test_open_fixture_binds_existing_issue_examples(self):
        report = evaluate(
            sorted(EXAMPLE_ROOT.glob("*.json")),
            OPEN,
        )
        self.assertEqual(report["status"], "PASS")
        self.assertIsNotNone(report["issue_inventory"])
        for signal in report["signals"]:
            routing = signal["routing"]
            self.assertEqual(
                routing["declared_disposition"],
                "UPDATE_EXISTING_ISSUE",
            )
            self.assertEqual(
                routing["disposition"],
                "UPDATE_EXISTING_ISSUE",
            )
            self.assertEqual(
                routing["inventory_status"],
                "BOUND_OPEN_TARGET",
            )
            self.assertEqual(
                routing["target_issue_ids"],
                [1647],
            )
            self.assertIn(
                "ISSUE_INVENTORY_OPEN_TARGET",
                routing["reason_codes"],
            )

    def test_missing_inventory_holds_declared_issue_updates(self):
        report = evaluate(
            sorted(EXAMPLE_ROOT.glob("*.json")),
        )
        self.assertEqual(report["status"], "PASS")
        self.assertIsNone(report["issue_inventory"])
        for signal in report["signals"]:
            routing = signal["routing"]
            self.assertEqual(
                routing["disposition"],
                "HOLD_FOR_DEPENDENCY",
            )
            self.assertEqual(
                routing["inventory_status"],
                "REQUIRED",
            )
            self.assertEqual(
                routing["target_issue_ids"],
                [],
            )
            self.assertIn(
                "ISSUE_INVENTORY_REQUIRED",
                routing["reason_codes"],
            )

    def test_closed_and_missing_targets_hold(self):
        cases = (
            (
                CLOSED,
                "TARGET_CLOSED",
                "ISSUE_INVENTORY_TARGET_CLOSED",
            ),
            (
                MISSING,
                "TARGET_MISSING",
                "ISSUE_INVENTORY_TARGET_MISSING",
            ),
        )
        examples = sorted(EXAMPLE_ROOT.glob("*.json"))
        for path, status, reason in cases:
            with self.subTest(path=path.name):
                report = evaluate(examples, path)
                self.assertEqual(report["status"], "PASS")
                for signal in report["signals"]:
                    routing = signal["routing"]
                    self.assertEqual(
                        routing["disposition"],
                        "HOLD_FOR_DEPENDENCY",
                    )
                    self.assertEqual(
                        routing["inventory_status"],
                        status,
                    )
                    self.assertIn(
                        reason,
                        routing["reason_codes"],
                    )

    def test_multiple_open_targets_are_ambiguous(self):
        result = validate_projection(OPEN)
        self.assertTrue(result.ok)
        assert result.payload is not None
        binding = bind_issue_inventory(
            declared_disposition="UPDATE_EXISTING_ISSUE",
            declared_reason_codes=["EXISTING_ISSUE_MATCH"],
            matched_issue_ids=[1647, 1675],
            projection=result.payload,
        )
        self.assertEqual(
            binding["disposition"],
            "HOLD_FOR_DEPENDENCY",
        )
        self.assertEqual(
            binding["inventory_status"],
            "AMBIGUOUS_OPEN_TARGETS",
        )
        self.assertEqual(binding["target_issue_ids"], [])
        self.assertIn(
            "ISSUE_INVENTORY_AMBIGUOUS_OPEN_TARGETS",
            binding["reason_codes"],
        )

    def test_non_update_routes_do_not_require_inventory(self):
        path = SIGNAL_VALID_ROOT / "valid_1.json"
        report = evaluate([path])
        self.assertEqual(report["status"], "PASS")
        routing = report["signals"][0]["routing"]
        self.assertEqual(
            routing["disposition"],
            routing["declared_disposition"],
        )
        self.assertEqual(
            routing["inventory_status"],
            "NOT_REQUIRED",
        )

    def test_invalid_inventory_fails_before_signal_projection(self):
        report = evaluate(
            sorted(EXAMPLE_ROOT.glob("*.json")),
            INVALID_ROOT / "digest-mismatch.json",
        )
        self.assertEqual(report["status"], "FAIL")
        self.assertEqual(report["signals"], [])
        self.assertIsNone(report["issue_inventory"])
        self.assertIn(
            "ISSUE_INVENTORY_PROJECTION_DIGEST_MISMATCH",
            {finding["code"] for finding in report["findings"]},
        )

    def test_reports_are_deterministic_and_value_minimized(self):
        paths = sorted(EXAMPLE_ROOT.glob("*.json"))
        first = serialize_report(evaluate(paths, OPEN))
        second = serialize_report(
            evaluate(list(reversed(paths)), OPEN)
        )
        self.assertEqual(first, second)
        self.assertNotIn('"headline"', first)
        self.assertNotIn('"claims"', first)
        self.assertNotIn('"source_ref"', first)
        self.assertIn('"live_state_verified":false', first)
        self.assertIn('"repository_mutation_allowed":false', first)

    def test_validator_and_router_cli_are_deterministic(self):
        projection_outputs = []
        route_outputs = []
        examples = [
            str(path)
            for path in sorted(EXAMPLE_ROOT.glob("*.json"))
        ]
        for _ in range(2):
            projection_stream = io.StringIO()
            with redirect_stdout(projection_stream):
                projection_code = projection_main([str(OPEN)])
            self.assertEqual(projection_code, 0)
            projection_outputs.append(
                projection_stream.getvalue()
            )

            route_stream = io.StringIO()
            with redirect_stdout(route_stream):
                route_code = route_main(
                    [
                        "--issue-inventory",
                        str(OPEN),
                        *examples,
                    ]
                )
            self.assertEqual(route_code, 0)
            route_outputs.append(route_stream.getvalue())

        self.assertEqual(
            projection_outputs[0],
            projection_outputs[1],
        )
        self.assertEqual(route_outputs[0], route_outputs[1])

    def test_no_network_calls_or_mutation_clients_exist(self):
        evaluate(
            sorted(EXAMPLE_ROOT.glob("*.json")),
            OPEN,
        )
        validate_projection(OPEN)
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()

        source_paths = (
            REPO_ROOT
            / "tools/validators/governance/"
            "validate_issue_inventory_projection.py",
            REPO_ROOT
            / "tools/validators/governance/"
            "route_briefing_signals.py",
        )
        for path in source_paths:
            source = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertNotIn("requests.", source)
                self.assertNotIn("httpx.", source)
                self.assertNotIn("urllib.request", source)
                self.assertNotIn("subprocess.", source)
                self.assertNotIn("PyGithub", source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
