from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/data/validate_public_map_misuse_review.py"
SPEC = importlib.util.spec_from_file_location("public_map_misuse_validator", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class PublicMapMisuseReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = (ROOT / "contracts/data/public_map_misuse_review.md").read_bytes()
        cls.schema = VALIDATOR.load_json(ROOT / "schemas/contracts/v1/data/public_map_misuse_review.schema.json")
        cls.manifest = VALIDATOR.load_json(ROOT / "fixtures/contracts/v1/data/public_map_misuse_review/cases.json")

    def case(self, case_id: str):
        case = next(item for item in self.manifest["cases"] if item["case_id"] == case_id)
        return VALIDATOR.validate_candidate(VALIDATOR.materialize_case(self.manifest, case), self.schema, self.contract)

    def test_schema_is_draft_2020_12(self):
        VALIDATOR.Draft202012Validator.check_schema(self.schema)

    def test_exact_fixture_replay(self):
        results = VALIDATOR.validate_fixture_manifest(self.manifest, self.schema, self.contract)
        self.assertEqual(14, len(results))
        self.assertEqual([], [(item["case_id"], item["outcome"], item["expected_outcome"]) for item in results if item["outcome"] != item["expected_outcome"]])

    def test_complete_candidate_passes(self):
        self.assertEqual("PASS", self.case("pass-complete-high-consequence-review")["outcome"])

    def test_unresolved_prerequisite_abstains(self):
        result = self.case("abstain-unresolved-omission-disclosure")
        self.assertEqual("ABSTAIN", result["outcome"])
        self.assertIn("PREREQUISITE_UNRESOLVED", {item["code"] for item in result["findings"]})

    def test_material_concern_denies(self):
        result = self.case("deny-material-concern-undisclosed")
        self.assertEqual("DENY", result["outcome"])
        self.assertIn("MATERIAL_CONCERN_UNDISCLOSED", {item["code"] for item in result["findings"]})

    def test_high_consequence_requires_review_ref(self):
        result = self.case("deny-high-consequence-review-missing")
        self.assertIn("HIGH_CONSEQUENCE_REVIEW_REF_MISSING", {item["code"] for item in result["findings"]})

    def test_authority_overclaim_is_schema_error(self):
        self.assertEqual("ERROR", self.case("error-authority-overclaim")["outcome"])

    def test_cli_fixture_mode(self):
        self.assertEqual(0, VALIDATOR.main(["--fixtures"]))


if __name__ == "__main__":
    unittest.main()
