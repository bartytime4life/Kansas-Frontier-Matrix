from __future__ import annotations

import copy
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
MODULE_PATH = ROOT / "tools/validators/source/validate_map_service_protocol_assessment.py"
SPEC = importlib.util.spec_from_file_location(
    "validate_map_service_protocol_assessment", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class MapServiceProtocolAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = MODULE.load_fixtures()
        cls.cases = {
            case["case_id"]: case for case in cls.manifest["cases"]
        }

    def _candidate(self, case_id: str) -> dict[str, object]:
        return MODULE.materialize_case(self.manifest, self.cases[case_id])

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(
            json.loads(MODULE.SCHEMA.read_text(encoding="utf-8"))
        )

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), len(self.cases))
        self.assertTrue(all(result["ok"] for result in results), results)

    def test_finite_outcomes_are_covered(self) -> None:
        outcomes = {
            MODULE.validate_payload(self._candidate(case_id)).outcome
            for case_id in self.cases
        }
        self.assertEqual(outcomes, {"PASS", "ABSTAIN", "DENY", "ERROR"})

    def test_all_four_protocol_classes_have_a_passing_declaration(self) -> None:
        protocols = {
            self._candidate(case_id)["declaration"]["protocol_class"]
            for case_id in self.cases
            if case_id.startswith("pass_")
        }
        self.assertEqual(protocols, {"PMTILES", "XYZ", "WMTS", "WMS"})

    def test_pmtiles_pass_is_immutable_and_has_no_remote_health_claim(self) -> None:
        candidate = self._candidate("pass_pmtiles_versioned_artifact")
        self.assertTrue(candidate["declaration"]["immutable"])
        self.assertIsNotNone(candidate["declaration"]["artifact_digest"])
        self.assertIsNone(candidate["controls"]["freshness_policy_ref"])
        self.assertIsNone(candidate["controls"]["source_health_ref"])
        self.assertEqual(candidate["controls"]["source_health_state"], "NOT_APPLICABLE")

    def test_remote_passes_remain_context_only_and_health_bound(self) -> None:
        for case_id in (
            "pass_xyz_context_service",
            "pass_wmts_capabilities_service",
            "pass_wms_capabilities_service",
        ):
            with self.subTest(case_id=case_id):
                candidate = self._candidate(case_id)
                self.assertEqual(candidate["declaration"]["source_use_role"], "CONTEXT_ONLY")
                self.assertFalse(candidate["declaration"]["immutable"])
                self.assertIsNone(candidate["declaration"]["artifact_digest"])
                self.assertIsNotNone(candidate["controls"]["freshness_policy_ref"])
                self.assertIsNotNone(candidate["controls"]["source_health_ref"])

    def test_every_materialized_fixture_denies_all_authority(self) -> None:
        for case_id in self.cases:
            with self.subTest(case_id=case_id):
                candidate = self._candidate(case_id)
                self.assertFalse(any(candidate["authority"].values()))
                self.assertFalse(candidate["decision"]["execution_authorized"])

    def test_identity_binds_protocol_semantics(self) -> None:
        candidate = self._candidate("pass_wmts_capabilities_service")
        digest, assessment_id = MODULE.canonical_identity(candidate)
        self.assertEqual(candidate["spec_hash"], digest)
        self.assertEqual(candidate["assessment_id"], assessment_id)
        changed = copy.deepcopy(candidate)
        changed["controls"]["cache_policy"] = "NO_STORE"
        self.assertNotEqual(digest, MODULE.canonical_identity(changed)[0])

    def test_incorrect_declared_decision_fails_closed(self) -> None:
        result = MODULE.validate_payload(
            self._candidate("deny_declared_decision_mismatch")
        )
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            [finding.code for finding in result.findings],
            ["MAP_PROTOCOL_DECISION_MISMATCH"],
        )

    def test_file_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            self.assertEqual(
                [finding.code for finding in MODULE.validate_file(duplicate).findings],
                ["MAP_PROTOCOL_JSON_DUPLICATE_KEY"],
            )
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":Infinity}', encoding="utf-8")
            self.assertEqual(
                [finding.code for finding in MODULE.validate_file(nonfinite).findings],
                ["MAP_PROTOCOL_JSON_NONFINITE_NUMBER"],
            )

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
