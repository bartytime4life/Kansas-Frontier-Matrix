import json
import unittest
from pathlib import Path

from tests.subprocess_utils import assert_python_ok


class ValidatorScriptTests(unittest.TestCase):
    def test_validator_scripts(self):
        for script in [
            "tools/validators/validate_source_terms.py",
            "tools/validators/validate_activation_decisions.py",
            "tools/validators/validate_evidence_closure.py",
            "tools/validators/validate_public_path_guards.py",
            "tools/validators/validate_fixture_validation.py",
        ]:
            with self.subTest(script=script):
                assert_python_ok(self, [script])


class HashingTests(unittest.TestCase):
    def test_compute_spec_hash_shared_schema(self):
        assert_python_ok(self, ["tools/compute_spec_hash.py", "schemas/contracts/v1/shared/policy_decision.schema.json"])


class EvidenceClosureFixtureTests(unittest.TestCase):
    def test_evidence_ref_closes_to_bundle(self):
        evidence_ref = json.loads(Path("fixtures/evidence/evidence_ref.valid.json").read_text())
        bundle = json.loads(Path("fixtures/evidence/evidence_bundle.valid.json").read_text())
        self.assertEqual(evidence_ref.get("bundle_id"), bundle.get("id"))
        self.assertIn(evidence_ref.get("id"), bundle.get("evidence_refs", []))


class InvalidFixtureSemanticsTests(unittest.TestCase):
    def test_intentional_invalid_no_network_fixtures(self):
        base = Path("fixtures/domains/hydrology/no_network")

        unresolved = json.loads((base / "hydrology_no_network.invalid_unresolved_evidence.json").read_text())
        self.assertEqual(unresolved["focus_outcome"], "ANSWER")
        self.assertFalse(unresolved["evidence_resolved"])

        bad_enum = json.loads((base / "hydrology_no_network.invalid_bad_activation_enum.json").read_text())
        self.assertNotIn(bad_enum["source_activation_decision"], {"ALLOW", "ABSTAIN", "DENY", "ERROR"})

        missing_citations = json.loads((base / "hydrology_no_network.invalid_missing_citations.json").read_text())
        self.assertEqual(missing_citations.get("citations"), [])

        invented_http = json.loads((base / "hydrology_no_network.invalid_invented_http_facts.json").read_text())
        self.assertEqual(invented_http["network_mode"], "DISABLED")
        self.assertEqual(invented_http["http_facts"][0]["kind"], "LIVE_HTTP_RESPONSE")


class NoNetworkBehaviorTests(unittest.TestCase):
    def test_valid_no_network_fixture(self):
        valid = json.loads(Path("fixtures/domains/hydrology/no_network/hydrology_no_network.valid.json").read_text())
        self.assertEqual(valid["network_mode"], "DISABLED")
        self.assertEqual(valid["source_activation_decision"], "ABSTAIN")
        self.assertEqual(valid["focus_outcome"], "ABSTAIN")
        self.assertGreater(len(valid.get("citations", [])), 0)


class HydrologySyntheticProofTests(unittest.TestCase):
    def test_hydrology_proof_validator(self):
        assert_python_ok(self, ["tools/validators/validate_hydrology_proof_slice.py"])


if __name__ == "__main__":
    unittest.main()
