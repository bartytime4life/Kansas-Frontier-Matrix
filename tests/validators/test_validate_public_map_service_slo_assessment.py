from __future__ import annotations

import importlib.util
import json
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/validate_public_map_service_slo_assessment.py"
SPEC = importlib.util.spec_from_file_location(
    "public_map_service_slo_assessment_validator", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class PublicMapServiceSLOAssessmentTests(unittest.TestCase):
    """Prove exact SLO arithmetic and the no-effect validation boundary."""

    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 34)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_complete_service_kinds_pass_without_authority(self) -> None:
        for name in (
            "pass_server_mediated_layer",
            "pass_static_pmtiles",
            "pass_static_cog",
            "pass_governed_map_api",
            "pass_composite_map_surface",
            "pass_exact_objective_boundary",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertIsNone(candidate["support"]["release_manifest_ref"])

    def test_unresolved_support_abstains(self) -> None:
        for name in (
            "abstain_assessment_incomplete",
            "abstain_window_incomplete",
            "abstain_policy_unresolved",
            "abstain_telemetry_missing",
            "abstain_review_missing",
            "abstain_rollback_missing",
            "abstain_latency_observation_missing",
            "abstain_latency_sample_missing",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).outcome,
                "ABSTAIN",
            )

    def test_budget_and_latency_breaches_deny(self) -> None:
        expected = {
            "deny_budget_exhausted": ["BUDGET_EXHAUSTED"],
            "deny_latency_breach": ["LATENCY_BREACH"],
            "deny_budget_and_latency": ["BUDGET_EXHAUSTED", "LATENCY_BREACH"],
        }
        for name, codes in expected.items():
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual(result.outcome, "DENY")
            self.assertEqual(result.codes, codes)

    def test_integer_budget_arithmetic_fails_closed(self) -> None:
        expected = {
            "deny_good_events_exceed_eligible": "GOOD_EVENTS_EXCEED_ELIGIBLE",
            "deny_allowed_bad_events_mismatch": "ALLOWED_BAD_EVENTS_MISMATCH",
            "deny_observed_bad_events_mismatch": "OBSERVED_BAD_EVENTS_MISMATCH",
            "deny_remaining_bad_events_mismatch": "REMAINING_BAD_EVENTS_MISMATCH",
            "deny_budget_state_mismatch": "BUDGET_STATE_MISMATCH",
        }
        for name, code in expected.items():
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).codes,
                [code],
            )

    def test_window_latency_report_and_canonicality_fail_closed(self) -> None:
        for name in (
            "deny_window_order",
            "deny_latency_state_mismatch",
            "deny_report_outcome_mismatch",
            "deny_report_findings_mismatch",
            "deny_support_refs_not_canonical",
            "deny_limitation_set_mismatch",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).outcome,
                "DENY",
            )

    def test_hash_and_identity_bind_service_semantics(self) -> None:
        candidate = self._candidate("pass_server_mediated_layer")
        spec_hash = MODULE.compute_spec_hash(candidate)
        self.assertEqual(candidate["spec_hash"], spec_hash)
        self.assertEqual(
            candidate["assessment_id"], MODULE.expected_assessment_id(spec_hash)
        )
        changed = json.loads(json.dumps(candidate))
        changed["availability"]["good_events"] = 994
        self.assertNotEqual(spec_hash, MODULE.compute_spec_hash(changed))

    def test_profile_contains_no_live_monitor_or_automatic_effect(self) -> None:
        candidate = self._candidate("pass_server_mediated_layer")
        self.assertEqual(candidate["execution"]["mode"], "FIXTURE_ONLY")
        self.assertFalse(candidate["execution"]["network_attempted"])
        self.assertFalse(candidate["execution"]["live_service_queried"])
        self.assertEqual(candidate["report"]["promotion_effect"], "NO_AUTOMATIC_EFFECT")
        self.assertEqual(candidate["report"]["rollback_effect"], "REVIEW_ONLY")
        self.assertNotIn("endpoint", candidate)
        self.assertNotIn("credentials", candidate)

    def test_error_and_schema_paths_are_finite(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("error_assessment")).outcome,
            "ERROR",
        )
        for name in (
            "error_schema_unknown_field",
            "error_schema_source_card",
            "error_schema_authority_overclaim",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).codes,
                ["SCHEMA_INVALID"],
            )

    def test_duplicate_json_is_rejected_without_echo(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"service_ref":"a","service_ref":"b"}', encoding="utf-8")
            candidate, findings = MODULE.load_json_object(path)
        self.assertIsNone(candidate)
        self.assertEqual([finding.code for finding in findings], ["JSON_DUPLICATE_KEY"])
        self.assertNotIn("a", repr(findings))
        self.assertNotIn("b", repr(findings))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket,
            "create_connection",
            side_effect=AssertionError("network denied"),
        ), mock.patch.object(
            socket,
            "socket",
            side_effect=AssertionError("network denied"),
        ):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
