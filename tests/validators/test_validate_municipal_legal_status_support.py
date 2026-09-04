from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator

REPO_ROOT=Path(__file__).resolve().parents[2]
VALIDATOR_PATH=REPO_ROOT/"tools/validators/validate_municipal_legal_status_support.py"
SCHEMA_PATH=REPO_ROOT/"schemas/contracts/v1/domains/settlements-infrastructure/municipal-legal-status-support.schema.json"
FIXTURE_PROFILE_PATH=REPO_ROOT/"fixtures/contracts/v1/domains/settlements-infrastructure/municipal_legal_status_support/fixture_profile.json"

SPEC=importlib.util.spec_from_file_location("municipal_legal_status_support_validator_under_test",VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE=importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name]=MODULE
SPEC.loader.exec_module(MODULE)

def _profile() -> dict[str,object]:
    return json.loads(FIXTURE_PROFILE_PATH.read_text(encoding="utf-8"))

class MunicipalLegalStatusSupportValidatorTests(unittest.TestCase):
    def test_schema_is_strict_proposed_draft_2020_12(self) -> None:
        schema=json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertEqual(schema["x-kfm"]["status"],"PROPOSED")
        self.assertFalse(schema["additionalProperties"])
        self.assertTrue(schema["properties"]["synthetic"]["const"])
        self.assertEqual(schema["properties"]["subject"]["properties"]["identity_family"]["enum"],["Municipality","CensusPlace"])

    def test_all_finite_outcome_vectors_pass(self) -> None:
        profile=_profile(); cases=profile["valid"]; self.assertEqual(len(cases),7); observed=set()
        for name,case in sorted(cases.items()):
            with self.subTest(name=name):
                candidate=MODULE.materialize_fixture(profile["base"],case["patch"])
                result=MODULE.validate(candidate)
                self.assertTrue(result.ok,result.findings)
                self.assertEqual(result.derived_outcome,case["expected_outcome"])
                self.assertEqual(list(result.derived_reason_codes),case["expected_reasons"])
                observed.add(result.derived_outcome)
        self.assertEqual(observed,{"ANSWER","ABSTAIN","DENY","ERROR"})

    def test_invalid_vectors_match_exact_reviewed_codes(self) -> None:
        profile=_profile(); cases=profile["invalid"]; self.assertEqual(len(cases),5)
        for name,case in sorted(cases.items()):
            with self.subTest(name=name):
                result=MODULE.validate(MODULE.materialize_fixture(profile["base"],case["patch"]))
                actual=sorted({f.code for f in result.findings})
                self.assertFalse(result.ok)
                self.assertEqual(actual,sorted(case["expected_findings"]))

    def test_fixture_cli_replays_exact_profile(self) -> None:
        completed=subprocess.run([sys.executable,str(VALIDATOR_PATH),"--fixtures"],cwd=REPO_ROOT,check=False,capture_output=True,text=True)
        self.assertEqual(completed.returncode,0,completed.stdout+completed.stderr)
        report=json.loads(completed.stdout)
        self.assertTrue(report["ok"]); self.assertEqual(len(report["cases"]),12)
        self.assertTrue(all(row["validation"]=="PASS" for row in report["cases"]))

    def test_argparse_abbreviation_is_fail_closed(self) -> None:
        completed=subprocess.run([sys.executable,str(VALIDATOR_PATH),"--fixt"],cwd=REPO_ROOT,check=False,capture_output=True,text=True)
        self.assertNotEqual(completed.returncode,0)
        self.assertIn("unrecognized arguments",completed.stderr)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/"duplicate.json"; path.write_text('{"id":"a","id":"b"}',encoding="utf-8")
            candidate,findings=MODULE._read(path)
        self.assertIsNone(candidate); self.assertEqual({f.code for f in findings},{"JSON_DUPLICATE_KEY"})

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/"nonfinite.json"; path.write_text('{"value":NaN}',encoding="utf-8")
            candidate,findings=MODULE._read(path)
        self.assertIsNone(candidate); self.assertEqual({f.code for f in findings},{"JSON_NONFINITE_NUMBER"})

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        profile=_profile(); candidate=MODULE.materialize_fixture(profile["base"],{})
        untrusted="UNTRUSTED_VALUE_DO_NOT_ECHO"; candidate["untrusted_negative_canary"]=untrusted; candidate["spec_hash"]=MODULE._canonical_hash(candidate)
        result=MODULE.validate(candidate)
        rendered=json.dumps([{"code":f.code,"field":f.field} for f in result.findings])
        self.assertNotIn(untrusted,rendered); self.assertIn("SCHEMA_INVALID",rendered)

    def test_materialization_and_validation_are_deterministic(self) -> None:
        profile=_profile(); case=profile["valid"]["deny_census_place.json"]
        first=MODULE.materialize_fixture(profile["base"],case["patch"]); second=MODULE.materialize_fixture(profile["base"],case["patch"])
        self.assertEqual(first,second); self.assertEqual(MODULE.validate(first),MODULE.validate(second))

if __name__=="__main__":
    unittest.main()
