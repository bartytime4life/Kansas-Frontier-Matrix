from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/evidence/validate_as_of_snapshot_disclosure.py"
SPEC = importlib.util.spec_from_file_location("as_of_snapshot_validator", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class AsOfSnapshotDisclosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = (ROOT / "contracts/evidence/as_of_snapshot_disclosure.md").read_bytes()
        cls.schema = VALIDATOR.load_json(ROOT / "schemas/contracts/v1/evidence/as_of_snapshot_disclosure.schema.json")
        cls.manifest = VALIDATOR.load_json(ROOT / "fixtures/contracts/v1/evidence/as_of_snapshot_disclosure/cases.json")

    def case(self, case_id: str):
        case = next(item for item in self.manifest["cases"] if item["case_id"] == case_id)
        return VALIDATOR.validate_candidate(VALIDATOR.materialize_case(self.manifest, case), self.schema, self.contract)

    def test_schema_is_draft_2020_12(self):
        VALIDATOR.Draft202012Validator.check_schema(self.schema)

    def test_exact_fixture_replay(self):
        results = VALIDATOR.validate_fixture_manifest(self.manifest, self.schema, self.contract)
        self.assertEqual(17, len(results))
        self.assertEqual([], [(item["case_id"], item["outcome"], item["expected_outcome"]) for item in results if item["outcome"] != item["expected_outcome"]])

    def test_complete_candidate_passes(self):
        self.assertEqual("PASS", self.case("pass-complete-bitemporal-public-candidate")["outcome"])

    def test_unresolved_source_abstains(self):
        result = self.case("abstain-unresolved-source")
        self.assertEqual("ABSTAIN", result["outcome"])
        self.assertIn("SOURCE_SNAPSHOT_UNRESOLVED", {item["code"] for item in result["findings"]})

    def test_source_after_as_of_denies(self):
        result = self.case("deny-source-after-as-of")
        self.assertEqual("DENY", result["outcome"])
        self.assertIn("SOURCE_SNAPSHOT_AFTER_AS_OF", {item["code"] for item in result["findings"]})

    def test_public_candidate_requires_review_reference(self):
        self.assertIn("PUBLIC_REVIEW_REF_MISSING", {item["code"] for item in self.case("deny-public-review-ref-missing")["findings"]})

    def test_authority_overclaim_is_schema_error(self):
        self.assertEqual("ERROR", self.case("error-authority-overclaim")["outcome"])

    def test_cli_fixture_mode(self):
        self.assertEqual(0, VALIDATOR.main(["--fixtures"]))


if __name__ == "__main__":
    unittest.main()
