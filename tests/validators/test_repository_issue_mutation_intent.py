from __future__ import annotations

import contextlib
import copy
import io
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.validators._common.jsonschema_runner import load_validator
from tools.validators.repository_control import validate_issue_mutation_intent as validator
from tools.validators.validate_all import load_registry, select_validators


class RepositoryIssueMutationIntentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = {
            case["case_id"]: case for case in validator._cases()
        }

    def load_json(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_schema_is_closed_single_action_and_no_authority(self) -> None:
        schema = self.load_json(validator.SCHEMA_PATH)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["$defs"]["intent"]["additionalProperties"])
        action = schema["$defs"]["action"]
        self.assertFalse(action["additionalProperties"])
        self.assertEqual(action["properties"]["type"]["const"], "ADD_LABEL")
        self.assertEqual(action["properties"]["label"]["const"], "needs-review")
        self.assertEqual(
            schema["properties"]["execution_mode"]["const"],
            "FIXTURE_ONLY_DECLARATION",
        )
        claims = schema["$defs"]["claims"]["properties"]
        self.assertTrue(claims["deterministic_evaluation"]["const"])
        for field in (
            "validator_network_accessed",
            "validator_external_mutation_performed",
            "external_state_authenticated",
            "authority_authenticated",
            "subject_execution_authenticated",
            "live_mutation_adapter_present",
            "mutation_verified",
            "pull_request_lifecycle_changed",
            "repository_settings_changed",
            "release_deployment_promotion_or_publication_changed",
        ):
            self.assertFalse(claims[field]["const"], field)

    def test_all_cases_build_deterministically_and_match_expected(self) -> None:
        for case_id, case in self.cases.items():
            with self.subTest(case_id=case_id):
                first = validator.build_candidate(case)
                second = validator.build_candidate(case)
                self.assertEqual(first, second)
                self.assertEqual(validator.validate_document(first).outcome, "PASS")
                self.assertEqual(
                    {
                        "outcome": first["receipt"]["outcome"],
                        "reason_codes": first["receipt"]["reason_codes"],
                    },
                    case["expected"],
                )

    def test_rendered_no_op_fixture_matches_builder(self) -> None:
        expected = validator.build_candidate(self.cases["already_satisfied_no_op"])
        fixture = self.load_json(validator.VALID_PATH)
        self.assertEqual(fixture, expected)
        self.assertEqual(list(load_validator(validator.SCHEMA_PATH).iter_errors(fixture)), [])
        self.assertEqual(validator.validate_document(fixture).outcome, "PASS")

    def test_action_chaining_ambiguous_target_and_unsupported_action_are_denied(self) -> None:
        for path in validator.INVALID_PATHS:
            with self.subTest(path=path.name):
                candidate, expected = validator._invalid_candidate(path)
                result = validator.validate_document(candidate)
                self.assertEqual(result.outcome, expected["outcome"])
                self.assertIn(
                    (expected["finding_code"], expected["path"]),
                    {(finding.code, finding.path) for finding in result.findings},
                )

    def test_target_state_authority_and_replay_fail_closed(self) -> None:
        expectations = {
            "stale_state_denied": "STALE_TARGET_STATE",
            "stale_revision_denied": "STALE_TARGET_REVISION",
            "wrong_repository_denied": "WRONG_REPOSITORY",
            "target_substitution_denied": "TARGET_SUBSTITUTION",
            "missing_authority_denied": "MISSING_AUTHORITY",
            "authority_denied": "AUTHORITY_NOT_ALLOWED",
            "unauthorized_actor_class_denied": "AUTHORITY_MISMATCH",
            "expired_intent_denied": "EXPIRED_INTENT",
            "reused_key_different_parameters_denied": "IDEMPOTENCY_KEY_REUSED",
        }
        for case_id, reason in expectations.items():
            with self.subTest(case_id=case_id):
                candidate = validator.build_candidate(self.cases[case_id])
                self.assertEqual(candidate["receipt"]["outcome"], "DENIED")
                self.assertEqual(candidate["receipt"]["reason_codes"], [reason])
                self.assertFalse(candidate["receipt"]["attempted"])
                self.assertFalse(candidate["receipt"]["applied"])
                self.assertEqual(candidate["receipt"]["readback_status"], "NOT_AVAILABLE")

    def test_retry_converges_to_exact_no_op(self) -> None:
        candidate = validator.build_candidate(self.cases["replay_converged_no_op"])
        self.assertEqual(candidate["receipt"]["outcome"], "NO_OP")
        self.assertEqual(candidate["receipt"]["reason_codes"], ["REPLAY_CONVERGED"])
        self.assertFalse(candidate["attempt"]["request_emitted"])
        self.assertFalse(candidate["receipt"]["attempted"])
        self.assertEqual(candidate["receipt"]["readback_status"], "EXACT")

    def test_applied_requires_exact_readback_but_never_claims_live_proof(self) -> None:
        candidate = validator.build_candidate(self.cases["applied_exact_readback"])
        self.assertEqual(candidate["receipt"]["outcome"], "APPLIED")
        self.assertTrue(candidate["receipt"]["attempted"])
        self.assertTrue(candidate["receipt"]["applied"])
        self.assertEqual(candidate["receipt"]["readback_status"], "EXACT")
        self.assertFalse(candidate["claims"]["subject_execution_authenticated"])
        self.assertFalse(candidate["claims"]["mutation_verified"])
        self.assertFalse(candidate["claims"]["validator_external_mutation_performed"])

        mismatch = validator.build_candidate(self.cases["readback_mismatch_error"])
        self.assertEqual(mismatch["receipt"]["outcome"], "ERROR")
        self.assertEqual(mismatch["receipt"]["reason_codes"], ["READBACK_MISMATCH"])
        self.assertFalse(mismatch["receipt"]["applied"])

    def test_transport_failure_and_replay_divergence_are_explicit_errors(self) -> None:
        expectations = {
            "attempt_after_denial_error": "ATTEMPT_AFTER_DENIAL",
            "transport_failure_error": "TRANSPORT_FAILURE",
            "replay_state_divergence_error": "REPLAY_STATE_DIVERGENCE",
        }
        for case_id, reason in expectations.items():
            with self.subTest(case_id=case_id):
                candidate = validator.build_candidate(self.cases[case_id])
                self.assertEqual(candidate["receipt"]["outcome"], "ERROR")
                self.assertEqual(candidate["receipt"]["reason_codes"], [reason])
                self.assertFalse(candidate["receipt"]["applied"])

    def test_intent_receipt_and_spec_identity_mutations_are_denied(self) -> None:
        candidate = validator.build_candidate(self.cases["already_satisfied_no_op"])
        candidate["intent"]["intent_id"] = (
            "kfm:repository-issue-mutation-intent:" + "0" * 64
        )
        candidate["receipt"]["outcome"] = "ATTEMPTED"
        candidate["receipt"]["receipt_id"] = (
            "kfm:repository-issue-mutation-receipt:" + "1" * 64
        )
        candidate["spec_hash"] = "sha256:" + "2" * 64
        codes = {finding.code for finding in validator.validate_document(candidate).findings}
        self.assertIn("INTENT_ID_MISMATCH", codes)
        self.assertIn("RECEIPT_DERIVATION_MISMATCH", codes)
        self.assertIn("RECEIPT_ID_MISMATCH", codes)
        self.assertIn("SPEC_HASH_MISMATCH", codes)

    def test_validator_executes_with_network_socket_blocked(self) -> None:
        with mock.patch.object(
            socket,
            "socket",
            side_effect=AssertionError("network access is forbidden"),
        ):
            for case in self.cases.values():
                candidate = validator.build_candidate(case)
                self.assertEqual(validator.validate_document(candidate).outcome, "PASS")

    def test_static_surface_has_no_network_writer_or_credentials(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8").lower()
        denied = (
            "import requests",
            "from requests",
            "import socket",
            "from socket",
            "import urllib",
            "from urllib",
            "import subprocess",
            "from subprocess",
            "import httpx",
            "from httpx",
            "pygithub",
            "github_token",
            "gh_token",
            "os.environ",
            "urlopen(",
        )
        for fragment in denied:
            with self.subTest(fragment=fragment):
                self.assertNotIn(fragment, source)

    def test_invalid_json_cli_does_not_echo_canary(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "bad.json"
            canary = "PRIVATE-CANARY-MUTATION-TOKEN"
            path.write_text('{"value":"' + canary + '",}', encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = validator.main([str(path)])
            self.assertEqual(code, 2)
            self.assertNotIn(canary, output.getvalue())

    def test_fixture_suite_cli(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = validator.main(["--fixtures"])
        self.assertEqual(code, 0)
        payload = json.loads(output.getvalue())
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["cases"], 17)
        self.assertEqual(payload["authority"], "NONE")

    def test_validator_registry_selects_every_changed_path(self) -> None:
        registry = load_registry(
            validator.REPO_ROOT / "tools/validators/validator_registry.json",
            validator.REPO_ROOT,
        )
        paths = (
            "contracts/governance/repository_issue_mutation_intent.md",
            "schemas/contracts/v1/governance/repository_issue_mutation_intent.schema.json",
            "fixtures/contracts/v1/governance/repository_issue_mutation_intent/cases.json",
            "tests/validators/test_repository_issue_mutation_intent.py",
            "tools/validators/repository_control/validate_issue_mutation_intent.py",
        )
        for path in paths:
            with self.subTest(path=path):
                selected, mode = select_validators(
                    registry, profile="changed-area", changed_paths=(path,)
                )
                self.assertEqual(mode, "changed-area")
                self.assertIn(
                    "repository-issue-mutation-intent",
                    {item.validator_id for item in selected},
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
