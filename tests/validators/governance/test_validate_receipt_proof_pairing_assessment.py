from __future__ import annotations
import copy
import unittest
from tools.validators.governance.validate_receipt_proof_pairing_assessment import FIXTURE_PATH, bind_candidate, load_json_object, materialize_fixture_case, validate_candidate, validate_fixture_manifest

class ReceiptProofPairingAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        manifest, findings = load_json_object(FIXTURE_PATH)
        assert manifest is not None, findings
        cls.manifest = manifest
        cls.by_name = {entry["name"]: materialize_fixture_case(manifest, entry) for entry in manifest["cases"]}

    def test_all_fixture_expectations(self):
        results = validate_fixture_manifest()
        self.assertGreaterEqual(len(results), 14)
        self.assertTrue(all(result["ok"] for result in results), results)

    def test_positive_candidate_passes(self):
        self.assertEqual(validate_candidate(self.by_name["valid_pair"]).outcome, "PASS")

    def test_unresolved_reference_abstains(self):
        result = validate_candidate(self.by_name["unresolved_receipt"])
        self.assertEqual(result.outcome, "ABSTAIN")
        self.assertEqual(result.codes, ["REFERENCE_UNRESOLVED"])

    def test_orphans_and_duplicates_deny(self):
        for name in ("orphan_proof", "duplicate_receipt_key", "duplicate_proof_key"):
            with self.subTest(name=name): self.assertEqual(validate_candidate(self.by_name[name]).outcome, "DENY")

    def test_time_and_count_contradictions_deny(self):
        for name in ("proof_precedes_receipt", "pair_count_mismatch"):
            with self.subTest(name=name): self.assertEqual(validate_candidate(self.by_name[name]).outcome, "DENY")

    def test_authority_overclaim_is_schema_error(self):
        self.assertEqual(validate_candidate(self.by_name["authority_overclaim"]).outcome, "ERROR")

    def test_identity_and_hash_are_bound(self):
        for name in ("tampered_profile_hash", "tampered_assessment_id"):
            with self.subTest(name=name): self.assertEqual(validate_candidate(self.by_name[name]).outcome, "DENY")

    def test_rebinding_after_bounded_change_restores_coherence(self):
        candidate = copy.deepcopy(self.by_name["valid_pair"])
        candidate["observed_at"] = "2026-08-11T20:01:00Z"
        candidate = bind_candidate(candidate)
        self.assertEqual(validate_candidate(candidate).outcome, "PASS")

if __name__ == "__main__": unittest.main()
