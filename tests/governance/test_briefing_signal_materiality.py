#!/usr/bin/env python3
"""Deterministic explainable materiality and issue-routing tests."""
from __future__ import annotations

import copy
import io
import json
import socket
import unittest
import urllib.request
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from jsonschema import Draft202012Validator, FormatChecker

from tools.validators.governance.route_briefing_signals import evaluate, main, serialize_report
from tools.validators.governance.validate_briefing_signal import (
    compute_materiality_priority,
    compute_materiality_reason_codes,
    compute_materiality_score,
    compute_routing_disposition,
    validate_file,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/briefing_signal"
VALID_ROOT = FIXTURE_ROOT / "valid"
SEMANTIC_ROOT = FIXTURE_ROOT / "semantic_invalid"
EXAMPLE_ROOT = REPO_ROOT / "examples/briefing_integration"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/briefing_signal.schema.json"
BASE = VALID_ROOT / "valid_1.json"

EXPECTED_ROUTES = {
    "valid_1.json": ("NO_ACTION", ["LOW_PRIORITY_NO_ACTION"]),
    "valid_duplicate_followup.json": ("NO_ACTION", ["DUPLICATE_CLUSTER_NO_ISSUE"]),
    "valid_p0_corrective_override.json": ("OPEN_CORRECTIVE_ISSUE", ["P0_CORRECTIVE_READY"]),
    "valid_p1_source_discovery.json": ("OPEN_SOURCE_DISCOVERY_ISSUE", ["SOURCE_DISCOVERY_READY"]),
    "valid_dependency_hold.json": ("HOLD_FOR_DEPENDENCY", ["DEPENDENCY_BLOCKED"]),
    "valid_reject_unsafe.json": ("REJECT_UNSAFE", ["UNSAFE_FOR_ROUTING"]),
}


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("BriefingSignal materiality routing attempted network access")


class BriefingSignalMaterialityTests(unittest.TestCase):
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

    def _candidate_for_score(self, dimensions: dict[str, int]) -> dict:
        candidate = _load(BASE)
        for key in candidate["materiality"]["dimensions"]:
            candidate["materiality"]["dimensions"][key] = 0
        candidate["materiality"]["dimensions"].update(dimensions)
        candidate["materiality"]["mandatory_override"] = {"applied": False, "reason_code": None}
        return candidate

    def test_threshold_boundaries_are_explicit(self):
        cases = (
            ({"public_safety": 5, "repository_integrity": 5, "recurrence": 5, "reuse_value": 5, "authority_quality": 5}, 55, "P0"),
            ({"public_safety": 5, "repository_integrity": 5, "recurrence": 5, "reuse_value": 5, "authority_quality": 4}, 54, "P1"),
            ({"geospatial_relevance": 5, "recurrence": 5, "reuse_value": 5, "authority_quality": 5}, 35, "P1"),
            ({"geospatial_relevance": 5, "recurrence": 5, "reuse_value": 5, "authority_quality": 4}, 34, "P2"),
            ({"recurrence": 5, "reuse_value": 5}, 20, "P2"),
            ({"recurrence": 5, "reuse_value": 4, "authority_quality": 1}, 19, "P3"),
            ({"authority_quality": 1}, 1, "P3"),
            ({}, 0, "IGNORE"),
        )
        for dimensions, score, priority in cases:
            with self.subTest(score=score, priority=priority):
                candidate = self._candidate_for_score(dimensions)
                self.assertEqual(compute_materiality_score(candidate), score)
                self.assertEqual(compute_materiality_priority(candidate), priority)

    def test_mandatory_override_forces_p0_without_changing_raw_score(self):
        candidate = self._candidate_for_score({"repository_integrity": 1, "rights_sensitivity_risk": 5})
        self.assertLess(compute_materiality_score(candidate), 0)
        candidate["materiality"]["mandatory_override"] = {
            "applied": True,
            "reason_code": "UNEXPECTED_REPOSITORY_MERGE",
        }
        self.assertEqual(compute_materiality_priority(candidate), "P0")
        self.assertIn("UNEXPECTED_REPOSITORY_MERGE", compute_materiality_reason_codes(candidate))

    def test_all_valid_fixtures_recompute_exact_materiality_and_routing(self):
        self.assertEqual({path.name for path in VALID_ROOT.glob("*.json")}, set(EXPECTED_ROUTES))
        for path in sorted(VALID_ROOT.glob("*.json")):
            candidate = _load(path)
            expected_disposition, expected_reasons = EXPECTED_ROUTES[path.name]
            with self.subTest(path=path.name):
                self.assertEqual(candidate["materiality"]["raw_score"], compute_materiality_score(candidate))
                self.assertEqual(candidate["materiality"]["priority"], compute_materiality_priority(candidate))
                self.assertEqual(candidate["materiality"]["reason_codes"], list(compute_materiality_reason_codes(candidate)))
                self.assertEqual(compute_routing_disposition(candidate), (expected_disposition, tuple(expected_reasons)))
                self.assertEqual(candidate["next_action"]["disposition"], expected_disposition)
                self.assertEqual(candidate["routing"]["reason_codes"], expected_reasons)

    def test_examples_update_existing_issue_before_other_routing(self):
        for path in sorted(EXAMPLE_ROOT.glob("*.json")):
            candidate = _load(path)
            with self.subTest(path=path.name):
                self.assertEqual(compute_routing_disposition(candidate), ("UPDATE_EXISTING_ISSUE", ("EXISTING_ISSUE_MATCH",)))
                self.assertEqual(candidate["next_action"]["disposition"], "UPDATE_EXISTING_ISSUE")

    def test_semantic_negative_fixtures_are_schema_valid_and_exact(self):
        schema = _load(SCHEMA_PATH)
        schema_validator = Draft202012Validator(schema, format_checker=FormatChecker())
        candidates = sorted(SEMANTIC_ROOT.glob("*.json"))
        self.assertEqual(len(candidates), 6)
        for path in candidates:
            candidate = _load(path)
            sidecar = path.with_suffix(".expected.txt")
            expected_code, expected_path = sidecar.read_text(encoding="utf-8").strip().split("\t")
            with self.subTest(path=path.name):
                self.assertEqual(list(schema_validator.iter_errors(candidate)), [])
                findings = validate_file(path)
                self.assertEqual(
                    {(finding.code, finding.path) for finding in findings},
                    {(expected_code, expected_path)},
                )

    def test_materiality_routing_report_is_deterministic_order_independent_and_value_free(self):
        paths = list(VALID_ROOT.glob("*.json")) + list(EXAMPLE_ROOT.glob("*.json"))
        first = serialize_report(evaluate(paths))
        second = serialize_report(evaluate(list(reversed(paths))))
        self.assertEqual(first, second)
        report = json.loads(first)
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(len(report["signals"]), 8)
        self.assertFalse(report["authority_created"])
        self.assertFalse(report["repository_mutation_allowed"])
        self.assertNotIn("Synthetic governance event signal", first)
        self.assertNotIn("claim-001", first)

    def test_report_rejects_semantically_invalid_input(self):
        path = SEMANTIC_ROOT / "materiality_score_mismatch.json"
        report = evaluate([path])
        self.assertEqual(report["status"], "FAIL")
        self.assertEqual(report["signals"], [])
        self.assertEqual(report["findings"][0]["code"], "INPUT_MATERIALITY_SCORE_MISMATCH")

    def test_cli_is_deterministic_and_dry_run_only(self):
        paths = [str(path) for path in sorted(VALID_ROOT.glob("*.json"))]
        outputs = []
        for _ in range(2):
            stream = io.StringIO()
            with redirect_stdout(stream):
                code = main(paths)
            self.assertEqual(code, 0)
            outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertIn('"repository_mutation_allowed":false', outputs[0])
        self.assertIn('"authority_created":false', outputs[0])

    def test_no_network_calls_occur(self):
        evaluate(list(VALID_ROOT.glob("*.json")))
        for path in SEMANTIC_ROOT.glob("*.json"):
            validate_file(path)
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
