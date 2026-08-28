from __future__ import annotations

import copy
import importlib.util
import json
import socket
import sys
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/validators/evidence/validate_clustering_output_role_assessment.py"
SPEC = importlib.util.spec_from_file_location("clustering_output_role_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class ClusteringOutputRoleAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 12)

    def test_positive_profiles_remain_exploratory(self) -> None:
        for name in ("pass_reviewed_exploratory", "pass_public_candidate_with_caveat"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertEqual(candidate["labeling"]["output_role"], "EXPLORATORY_GROUPING")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_incomplete_evidence_abstains(self) -> None:
        self.assertEqual(MODULE.validate_candidate(self._candidate("abstain_evaluation_partial")).outcome, "ABSTAIN")
        self.assertEqual(MODULE.validate_candidate(self._candidate("abstain_validation_pending")).outcome, "ABSTAIN")

    def test_authority_and_public_caveat_overclaims_fail_closed(self) -> None:
        expected = {
            "deny_authoritative_role": ["AUTHORITATIVE_CLUSTER_ROLE_DENIED"],
            "deny_domain_category_claim": ["DOMAIN_CATEGORY_CLAIM_DENIED"],
            "deny_public_no_caveat": ["PUBLIC_CAVEAT_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_method_and_label_review_invariants_fail_closed(self) -> None:
        self.assertEqual(MODULE.validate_candidate(self._candidate("deny_cluster_count_mismatch")).codes, ["CLUSTER_COUNT_MISMATCH"])
        self.assertEqual(MODULE.validate_candidate(self._candidate("deny_random_without_seed")).codes, ["INITIALIZATION_SEED_REQUIRED"])
        self.assertEqual(MODULE.validate_candidate(self._candidate("deny_analyst_label_without_review")).codes, ["ANALYST_LABEL_REVIEW_REQUIRED", "REVIEW_PENDING"])

    def test_profile_hash_binds_semantics(self) -> None:
        candidate = self._candidate("pass_reviewed_exploratory")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["method"]["declared_cluster_count"] = 6
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
