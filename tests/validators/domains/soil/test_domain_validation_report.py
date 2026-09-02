from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
VALIDATOR = ROOT / "tools/validators/domains/soil/validate_domain_validation_report.py"
CASES = ROOT / "fixtures/domains/soil/domain_validation_report/cases.json"
SCHEMA = ROOT / "schemas/contracts/v1/domains/soil/domain_validation_report.schema.json"

SPEC = importlib.util.spec_from_file_location("soil_domain_validation_report_validator", VALIDATOR)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SoilDomainValidationReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = json.loads(CASES.read_text(encoding="utf-8"))["cases"]
        cls.schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    def test_schema_is_closed_and_non_authoritative(self) -> None:
        self.assertFalse(self.schema["additionalProperties"])
        self.assertEqual(
            self.schema["properties"]["profile"]["const"],
            "kfm.domains.soil.domain-validation-report.v1",
        )
        self.assertFalse(self.schema["properties"]["public_use_allowed"]["const"])
        self.assertFalse(self.schema["x-kfm"]["public_release_authority"])

    def test_fixture_matrix_matches_exact_outcomes(self) -> None:
        for case in self.cases:
            with self.subTest(case=case["name"]):
                outcome, findings = MODULE.evaluate(case["candidate"])
                self.assertEqual(outcome, case["expected_outcome"])
                self.assertEqual(findings, case["expected_findings"])

    def test_pass_and_fail_are_both_valid_report_states(self) -> None:
        by_name = {case["name"]: case for case in self.cases}
        self.assertEqual(MODULE.evaluate(by_name["pass"]["candidate"]), ("PASS", []))
        self.assertEqual(MODULE.evaluate(by_name["fail"]["candidate"]), ("PASS", []))

    def test_result_polarity_is_enforced(self) -> None:
        by_name = {case["name"]: case for case in self.cases}
        self.assertEqual(
            MODULE.evaluate(by_name["pass_with_findings"]["candidate"])[1],
            ["PASS_HAS_FINDINGS"],
        )
        self.assertEqual(
            MODULE.evaluate(by_name["fail_without_findings"]["candidate"])[1],
            ["NONPASS_MISSING_FINDINGS"],
        )

    def test_valid_report_has_deterministic_identity(self) -> None:
        candidate = self.cases[0]["candidate"]
        digest = MODULE.canonical_hash(candidate)
        self.assertEqual(candidate["spec_hash"], f"sha256:{digest}")
        self.assertEqual(candidate["id"], f"soil-validation:{digest[:24]}")


if __name__ == "__main__":
    unittest.main()
