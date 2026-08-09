from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[2]
MODULE_PATH=ROOT/'tools/validators/release/validate_operational_trust_rollup.py'
SPEC=importlib.util.spec_from_file_location('operational_trust_rollup_validator',MODULE_PATH)
assert SPEC and SPEC.loader
MODULE=importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name]=MODULE
SPEC.loader.exec_module(MODULE)


class OperationalTrustRollupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls)->None:
        cls.manifest=json.loads(MODULE.FIXTURE_PATH.read_text(encoding='utf-8'))

    def test_schema_is_valid_draft_2020_12(self)->None:
        Draft202012Validator.check_schema(MODULE._schema())

    def test_fixture_manifest_matches_exact_outcomes(self)->None:
        results=MODULE.validate_fixture_manifest()
        self.assertEqual(len(results),15)
        self.assertTrue(all(item['ok'] for item in results),results)

    def test_ready_summary_is_complete(self)->None:
        result=MODULE.validate_candidate(MODULE.materialize_fixture_case(self.manifest,self.manifest['cases'][0]))
        self.assertEqual(result.outcome,'READY')
        self.assertEqual(result.summary['component_count'],8)

    def test_pending_review_holds(self)->None:
        entry=next(case for case in self.manifest['cases'] if case['name']=='hold_review_pending')
        candidate=MODULE.materialize_fixture_case(self.manifest,entry)
        result=MODULE.validate_candidate(candidate)
        self.assertEqual(result.outcome,'HOLD')
        self.assertEqual(result.codes,['REVIEW_PENDING'])

    def test_missing_rollback_denies(self)->None:
        entry=next(case for case in self.manifest['cases'] if case['name']=='deny_rollback_missing')
        candidate=MODULE.materialize_fixture_case(self.manifest,entry)
        self.assertEqual(MODULE.validate_candidate(candidate).outcome,'DENY')

    def test_error_component_errors(self)->None:
        entry=next(case for case in self.manifest['cases'] if case['name']=='error_evidence_component')
        candidate=MODULE.materialize_fixture_case(self.manifest,entry)
        self.assertEqual(MODULE.validate_candidate(candidate).outcome,'ERROR')

    def test_spec_hash_replays(self)->None:
        candidate=MODULE.materialize_fixture_case(self.manifest,self.manifest['cases'][0])
        self.assertEqual(candidate['rollup_spec_hash'],MODULE.compute_rollup_hash(candidate))


if __name__=='__main__':
    unittest.main()
