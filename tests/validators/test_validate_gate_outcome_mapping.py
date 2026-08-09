from __future__ import annotations

import json
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.governance import validate_gate_outcome_mapping as validator

ROOT = Path(__file__).resolve().parents[2]


class GateOutcomeMappingTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_cases(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(manifest, case))
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_is_non_vacuous(self) -> None:
        manifest = validator.load_fixtures()
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"PASS", "ABSTAIN", "DENY", "ERROR"}, set(outcomes))
        self.assertGreaterEqual(outcomes["DENY"], 6)

    def test_both_pass_surfaces_are_covered(self) -> None:
        manifest = validator.load_fixtures()
        pass_documents = [
            validator.materialize_case(manifest, case)
            for case in manifest["cases"]
            if case["expected_outcome"] == "PASS"
        ]
        self.assertEqual({"PROMOTION", "ANSWER"}, {item["target_surface"] for item in pass_documents})

    def test_source_promote_term_adapts_to_existing_approve_vocabulary(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        self.assertEqual("PromotionDecision", document["mapped"]["destination_contract"])
        self.assertEqual("APPROVE", document["mapped"]["outcome"])
        self.assertNotEqual("PROMOTE", document["mapped"]["outcome"])

    def test_error_uses_decision_envelope_for_both_surfaces(self) -> None:
        manifest = validator.load_fixtures()
        error_cases = [case for case in manifest["cases"] if case["expected_outcome"] == "ERROR"]
        self.assertEqual(2, len(error_cases))
        for case in error_cases:
            document = validator.materialize_case(manifest, case)
            self.assertEqual("DecisionEnvelope", document["mapped"]["destination_contract"])
            self.assertEqual("ERROR", document["mapped"]["outcome"])

    def test_governance_non_effects_are_false(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        self.assertEqual("FIXTURE_ONLY", document["governance"]["execution_mode"])
        self.assertFalse(any(value for key, value in document["governance"].items() if key != "execution_mode"))

    def test_fixture_cli(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(Path(validator.__file__)), "--fixtures"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn('"suite_match":true', completed.stdout)

    def test_validator_has_no_host_or_network_client(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "PyGithub", "github.Github"):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
