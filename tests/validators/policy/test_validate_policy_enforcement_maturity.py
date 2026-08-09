import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/policy/validate_policy_enforcement_maturity.py"
SPEC = importlib.util.spec_from_file_location("policy_enforcement_maturity", VALIDATOR_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PolicyEnforcementMaturityTests(unittest.TestCase):
    def _case(self, name: str):
        fixtures = json.loads(MODULE.FIXTURES.read_text(encoding="utf-8"))
        return copy.deepcopy(next(case["record"] for case in fixtures["cases"] if case["name"] == name))

    def _rehash(self, record):
        record["spec_hash"] = MODULE.compute_record_spec_hash(record)
        return record

    def test_fixture_replay(self):
        self.assertEqual([], MODULE.replay())

    def test_merge_blocking_cannot_skip_fixture_tested(self):
        record = self._case("runtime_enforced_full_chain")
        record["claimed_stage"] = "MERGE_BLOCKING"
        record["evidence"] = [item for item in record["evidence"] if item["stage"] in {"DESIGNED", "MERGE_BLOCKING"}]
        self.assertEqual("DENY", MODULE.evaluate(self._rehash(record)))

    def test_workflow_evidence_cannot_stand_in_for_required_check(self):
        record = self._case("runtime_enforced_full_chain")
        merge = next(item for item in record["evidence"] if item["stage"] == "MERGE_BLOCKING")
        merge["evidence_kind"] = "FIXTURE_OR_TEST"
        self.assertEqual("DENY", MODULE.evaluate(self._rehash(record)))

    def test_later_stage_evidence_requires_matching_claim(self):
        record = self._case("fixture_tested_chain")
        record["claimed_stage"] = "DESIGNED"
        self.assertEqual("DENY", MODULE.evaluate(self._rehash(record)))

    def test_full_commit_sha_is_required(self):
        record = self._case("designed_only")
        record["observed_commit"] = "6552f43"
        self.assertEqual("ERROR", MODULE.evaluate(self._rehash(record)))

    def test_evidence_references_must_be_canonical(self):
        record = self._case("designed_only")
        record["evidence"][0]["refs"] = list(reversed(record["evidence"][0]["refs"]))
        self.assertEqual("DENY", MODULE.evaluate(self._rehash(record)))

    def test_schema_is_closed(self):
        record = self._case("designed_only")
        record["unexpected"] = True
        self.assertEqual("ERROR", MODULE.evaluate(self._rehash(record)))

    def test_spec_hash_mismatch_is_error(self):
        record = self._case("designed_only")
        record["spec_hash"] = "sha256:" + "0" * 64
        self.assertEqual("ERROR", MODULE.evaluate(record))


if __name__ == "__main__":
    unittest.main()
