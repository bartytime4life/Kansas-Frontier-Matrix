from __future__ import annotations

import contextlib
import copy
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/release/validate_conditional_write_preflight.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/conditional_write_preflight.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/release/conditional_write_preflight"


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    import sys
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


validator = _load_module("conditional_write_preflight_validator_under_test", VALIDATOR_PATH)
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
SCHEMA_VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


class ConditionalWritePreflightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cases_value = validator.load_json_file(validator.CASES_PATH)
        cls.cases = {case["case_id"]: case for case in cases_value["cases"]}

    def load_json(self, relative: str) -> dict:
        return json.loads((FIXTURE_ROOT / relative).read_text(encoding="utf-8"))

    def test_schema_is_closed_and_fixes_no_effect_claims(self) -> None:
        Draft202012Validator.check_schema(SCHEMA)
        self.assertEqual(SCHEMA["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(SCHEMA["additionalProperties"])
        claims = SCHEMA["$defs"]["claims"]["properties"]
        self.assertFalse(claims["write_request_emitted"]["const"])
        self.assertFalse(claims["write_performed"]["const"])
        self.assertFalse(claims["published"]["const"])
        self.assertFalse(claims["public_use_authorized"]["const"])

    def test_all_cases_build_deterministically_and_match_expected(self) -> None:
        for case_id, case in self.cases.items():
            with self.subTest(case_id=case_id):
                first = validator.build_candidate(case)
                second = validator.build_candidate(case)
                self.assertEqual(first, second)
                result = validator.validate_document(first)
                self.assertEqual(result.outcome, "PASS", result.findings)
                self.assertEqual(
                    {
                        "outcome": first["preflight"]["outcome"],
                        "reason_codes": first["preflight"]["reason_codes"],
                    },
                    case["expected"],
                )

    def test_valid_fixture_replays_exact_create_case(self) -> None:
        expected = validator.build_candidate(self.cases["create_absent_propose_write"])
        fixture = self.load_json("valid/valid_propose_write.json")
        self.assertEqual(fixture, expected)
        self.assertEqual(list(SCHEMA_VALIDATOR.iter_errors(fixture)), [])
        self.assertEqual(validator.validate_document(fixture).outcome, "PASS")

    def test_authority_overreach_is_schema_invalid(self) -> None:
        candidate = self.load_json("invalid/invalid_authority_overreach.json")
        self.assertTrue(list(SCHEMA_VALIDATOR.iter_errors(candidate)))
        result = validator.validate_document(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertTrue(any(finding.code == "SCHEMA_INVALID" for finding in result.findings))

    def test_create_if_absent_models_if_none_match_without_emitting_request(self) -> None:
        candidate = validator.build_candidate(self.cases["create_absent_propose_write"])
        self.assertEqual(candidate["preflight"]["outcome"], "PROPOSE_WRITE")
        self.assertEqual(candidate["preflight"]["request_headers"]["if_none_match"], "*")
        self.assertIsNone(candidate["preflight"]["request_headers"]["if_match"])
        self.assertFalse(candidate["claims"]["write_request_emitted"])
        self.assertFalse(candidate["claims"]["write_performed"])

    def test_replace_if_match_requires_exact_observed_etag(self) -> None:
        matching = validator.build_candidate(self.cases["replace_match_propose_write"])
        conflict = validator.build_candidate(self.cases["replace_etag_mismatch_conflict"])
        self.assertEqual(matching["preflight"]["outcome"], "PROPOSE_WRITE")
        self.assertEqual(conflict["preflight"]["outcome"], "CONFLICT")
        self.assertEqual(conflict["preflight"]["reason_codes"], ["ETAG_MISMATCH"])

    def test_matching_content_digest_is_idempotent_no_action(self) -> None:
        candidate = validator.build_candidate(self.cases["idempotent_content_no_action"])
        self.assertEqual(candidate["preflight"]["outcome"], "NO_ACTION")
        self.assertEqual(candidate["preflight"]["reason_codes"], ["CONTENT_ALREADY_PRESENT"])

    def test_blockers_dominate_a_satisfied_target_condition(self) -> None:
        case = copy.deepcopy(self.cases["create_absent_propose_write"])
        case["upstream"]["policy_outcome"] = "UNKNOWN"
        case["upstream"]["review_state"] = "PENDING"
        case["upstream"]["promotion_state"] = "HELD"
        candidate = validator.build_candidate(case)
        self.assertEqual(candidate["preflight"]["outcome"], "HOLD")
        self.assertEqual(
            candidate["preflight"]["reason_codes"],
            ["POLICY_NOT_ALLOWED", "PROMOTION_NOT_APPROVED", "REVIEW_NOT_APPROVED"],
        )

    def test_release_and_rollback_closure_are_required_for_proposal(self) -> None:
        candidate = validator.build_candidate(self.cases["missing_release_and_rollback_hold"])
        self.assertEqual(candidate["preflight"]["outcome"], "HOLD")
        self.assertEqual(
            candidate["preflight"]["reason_codes"],
            ["RELEASE_MANIFEST_MISSING", "ROLLBACK_TARGET_MISSING"],
        )

    def test_target_state_conflicts_never_fall_back_to_unconditional_write(self) -> None:
        create_conflict = validator.build_candidate(self.cases["create_target_exists_conflict"])
        absent_conflict = validator.build_candidate(self.cases["replace_target_absent_conflict"])
        self.assertEqual(create_conflict["preflight"]["outcome"], "CONFLICT")
        self.assertEqual(absent_conflict["preflight"]["outcome"], "CONFLICT")
        self.assertFalse(create_conflict["claims"]["write_performed"])
        self.assertFalse(absent_conflict["claims"]["write_performed"])

    def test_identity_changes_when_observed_condition_changes(self) -> None:
        original = validator.build_candidate(self.cases["replace_match_propose_write"])
        changed_case = copy.deepcopy(self.cases["replace_match_propose_write"])
        changed_case["target"]["observed_etag"] = "sha256:" + "e" * 64
        changed = validator.build_candidate(changed_case)
        self.assertNotEqual(original["preflight"]["condition_fingerprint"], changed["preflight"]["condition_fingerprint"])
        self.assertNotEqual(original["spec_hash"], changed["spec_hash"])
        self.assertNotEqual(original["intent_id"], changed["intent_id"])

    def test_idempotency_key_does_not_depend_on_observed_state(self) -> None:
        original = validator.build_candidate(self.cases["replace_match_propose_write"])
        changed_case = copy.deepcopy(self.cases["replace_match_propose_write"])
        changed_case["target"]["observed_etag"] = "sha256:" + "e" * 64
        changed = validator.build_candidate(changed_case)
        self.assertEqual(original["request"]["idempotency_key"], changed["request"]["idempotency_key"])

    def test_derived_preflight_mutation_is_denied(self) -> None:
        candidate = self.load_json("valid/valid_propose_write.json")
        candidate["preflight"]["outcome"] = "NO_ACTION"
        result = validator.validate_document(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertTrue(any(f.code == "PREFLIGHT_DERIVATION_MISMATCH" for f in result.findings))

    def test_spec_hash_and_intent_id_mutations_are_denied(self) -> None:
        candidate = self.load_json("valid/valid_propose_write.json")
        candidate["spec_hash"] = "sha256:" + "1" * 64
        candidate["intent_id"] = "kfm:conditional-write-intent:" + "2" * 64
        result = validator.validate_document(candidate)
        codes = {finding.code for finding in result.findings}
        self.assertEqual(result.outcome, "DENY")
        self.assertIn("SPEC_HASH_MISMATCH", codes)
        self.assertIn("INTENT_ID_MISMATCH", codes)

    def test_no_network_or_external_process_surface(self) -> None:
        source = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (
                VALIDATOR_PATH,
                REPO_ROOT / "tools/validators/release/_conditional_write_preflight_model.py",
            )
        )
        denied = (
            "import requests",
            "from requests",
            "import socket",
            "from socket",
            "import urllib",
            "from urllib",
            "import subprocess",
            "from subprocess",
            "requests.put",
            "KFM_PUBLISH_URL",
        )
        for fragment in denied:
            with self.subTest(fragment=fragment):
                self.assertNotIn(fragment, source)

    def test_cli_fixture_suite_and_value_minimized_invalid_json(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exit_code = validator.main(["--fixtures"])
        self.assertEqual(exit_code, 0)
        payload = json.loads(output.getvalue())
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["cases"], 10)

        with tempfile.TemporaryDirectory() as temp_dir:
            canary = "PRIVATE-CANARY"
            bad = Path(temp_dir) / "bad.json"
            bad.write_text('{"value":"' + canary + '",}', encoding="utf-8")
            result = validator.validate_file(bad)
            rendered = json.dumps([{"code": f.code, "path": f.path} for f in result.findings])
            self.assertEqual(result.outcome, "ERROR")
            self.assertNotIn(canary, rendered)


if __name__ == "__main__":
    unittest.main(verbosity=2)
