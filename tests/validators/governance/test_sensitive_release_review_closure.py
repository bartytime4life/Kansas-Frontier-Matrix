from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR = REPO_ROOT / "tools/validators/governance/validate_sensitive_release_review_closure.py"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/governance/sensitive_release_review_closure/cases.json"
SCHEMA = REPO_ROOT / "schemas/contracts/v1/governance/sensitive_release_review_closure.schema.json"

spec = importlib.util.spec_from_file_location("sensitive_release_review_validator", VALIDATOR)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class SensitiveReleaseReviewClosureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = json.loads(FIXTURES.read_text(encoding="utf-8"))
        base = self.fixture["base_document"]
        self.by_id = {
            case["case_id"]: {**case, "document": module.materialize_case(base, case)}
            for case in self.fixture["cases"]
        }

    def test_schema_is_draft_2020_12_valid(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA.read_text(encoding="utf-8")))

    def test_fixture_suite_has_exact_polarity(self) -> None:
        ok, report = module.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(12, len(report["cases"]))
        self.assertTrue(all(case["ok"] for case in report["cases"]))

    def test_t3_and_t4_close_only_for_separate_gate(self) -> None:
        for case_id in ("closed-t3", "closed-t4"):
            result = module.validate_document(self.by_id[case_id]["document"])
            self.assertEqual(("PASS", "CLOSED_FOR_SEPARATE_RELEASE_GATE", ()), (result.status, result.closure_outcome, result.findings))

    def test_hold_and_policy_deny_are_coherent_finite_results(self) -> None:
        expected = {
            "hold-conditional-review": "HOLD",
            "hold-policy": "HOLD",
            "hold-policy-abstain": "HOLD",
            "deny-policy": "DENY",
        }
        for case_id, outcome in expected.items():
            result = module.validate_document(self.by_id[case_id]["document"])
            self.assertEqual("PASS", result.status)
            self.assertEqual(outcome, result.closure_outcome)

    def test_embedded_review_binding_is_reused_and_validated(self) -> None:
        document = self.by_id["closed-t3"]["document"]
        result = module._REVIEW.validate_document(document["review_binding"])
        self.assertEqual(("PASS", "BOUND", ()), (result.status, result.binding_outcome, result.findings))

    def test_independence_and_binding_fail_closed(self) -> None:
        expected = {
            "invalid-reviewer-in-author-role-chain": "REVIEWER_IN_AUTHOR_ROLE_CHAIN",
            "invalid-missing-release-review-responsibility": "RELEASE_REVIEW_RESPONSIBILITY_MISSING",
            "invalid-subject-mismatch": "SUBJECT_MISMATCH",
            "invalid-self-review": "SELF_REVIEW_DENIED",
        }
        for case_id, code in expected.items():
            result = module.validate_document(self.by_id[case_id]["document"])
            self.assertEqual("DENY", result.status)
            self.assertIn(code, {finding.code for finding in result.findings})

    def test_authority_and_identity_tamper_fail_closed(self) -> None:
        authority = module.validate_document(self.by_id["invalid-authority-overclaim"]["document"])
        identity = module.validate_document(self.by_id["invalid-spec-hash"]["document"])
        self.assertEqual({"SCHEMA_INVALID"}, {finding.code for finding in authority.findings})
        self.assertEqual({"CLOSURE_SPEC_HASH_MISMATCH"}, {finding.code for finding in identity.findings})

    def test_symlink_input_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "fixture.json"
            target.write_text(json.dumps(self.by_id["closed-t3"]["document"]), encoding="utf-8")
            link = Path(directory) / "link.json"
            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            result = module.validate_file(link)
            self.assertEqual("ERROR", result.status)
            self.assertEqual({"CLOSURE_JSON_INVALID"}, {finding.code for finding in result.findings})

    def test_cli_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR), "--fixtures"]
        first = subprocess.run(command, check=True, capture_output=True, text=True)
        second = subprocess.run(command, check=True, capture_output=True, text=True)
        self.assertEqual(first.stdout, second.stdout)
        self.assertTrue(json.loads(first.stdout)["ok"])

    def test_validator_has_no_network_or_write_surface(self) -> None:
        source = VALIDATOR.read_text(encoding="utf-8")
        for token in (
            "import requests",
            "import urllib",
            "import socket",
            "import subprocess",
            "from subprocess",
            ".write_text(",
            ".write_bytes(",
            "os.remove(",
            "os.replace(",
            "open(",
        ):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
