import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/governance/validate_negative_state_audit.py"
SPEC = importlib.util.spec_from_file_location("negative_state_audit", VALIDATOR_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class NegativeStateAuditTests(unittest.TestCase):
    def _case(self, name: str = "valid_three_way_matrix"):
        fixtures = json.loads(MODULE.FIXTURES.read_text(encoding="utf-8"))
        return copy.deepcopy(next(case["record"] for case in fixtures["cases"] if case["name"] == name))

    def _rehash(self, record):
        record["spec_hash"] = MODULE.compute_record_spec_hash(record)
        return record

    def test_fixture_replay(self):
        self.assertEqual([], MODULE.replay())

    def test_approved_case_requires_evidence_and_release(self):
        record = self._case()
        approved = next(case for case in record["cases"] if case["case_kind"] == "APPROVED_ARTIFACT")
        approved.pop("evidence_bundle_refs")
        self.assertEqual("DENY", MODULE.evaluate(self._rehash(record)))

    def test_denied_case_cannot_expose_release_manifest(self):
        record = self._case()
        denied = next(case for case in record["cases"] if case["case_kind"] == "POLICY_DENIAL")
        denied["release_manifest_ref"] = "release://manifest/unsafe"
        self.assertEqual("DENY", MODULE.evaluate(self._rehash(record)))

    def test_exact_three_case_matrix_is_required(self):
        record = self._case()
        record["cases"].pop()
        self.assertEqual("ERROR", MODULE.evaluate(self._rehash(record)))

    def test_failure_case_must_represent_a_real_failure(self):
        record = self._case()
        failure = next(case for case in record["cases"] if case["case_kind"] == "CITATION_OR_VALIDATION_FAILURE")
        failure["citation_outcome"] = "PASS"
        failure.pop("failure_report_ref")
        self.assertEqual("DENY", MODULE.evaluate(self._rehash(record)))

    def test_schema_is_closed(self):
        record = self._case()
        record["unexpected"] = True
        self.assertEqual("ERROR", MODULE.evaluate(self._rehash(record)))

    def test_spec_hash_mismatch_is_error(self):
        record = self._case()
        record["spec_hash"] = "sha256:" + "0" * 64
        self.assertEqual("ERROR", MODULE.evaluate(record))


if __name__ == "__main__":
    unittest.main()
