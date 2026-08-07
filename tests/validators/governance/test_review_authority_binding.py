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
VALIDATOR = REPO_ROOT / "tools/validators/governance/validate_review_authority_binding.py"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/governance/review_authority_binding/cases.json"
SCHEMA = REPO_ROOT / "schemas/contracts/v1/governance/review_authority_binding.schema.json"

spec = importlib.util.spec_from_file_location("review_authority_binding_validator", VALIDATOR)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class ReviewAuthorityBindingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = json.loads(FIXTURES.read_text(encoding="utf-8"))
        base = self.fixture["base_document"]
        self.by_id = {
            case["case_id"]: {
                **case,
                "document": module.materialize_case(base, case),
            }
            for case in self.fixture["cases"]
        }

    def test_schema_is_draft_2020_12_valid(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA.read_text(encoding="utf-8")))

    def test_fixture_suite_has_exact_polarity(self) -> None:
        ok, report = module.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(11, len(report["cases"]))
        self.assertTrue(all(case["ok"] for case in report["cases"]))

    def test_bound_case(self) -> None:
        result = module.validate_document(self.by_id["bound-active-approved"]["document"])
        self.assertEqual(("PASS", "BOUND", ()), (result.status, result.binding_outcome, result.findings))

    def test_hold_cases(self) -> None:
        for case_id in ("hold-provisional", "hold-conditional"):
            result = module.validate_document(self.by_id[case_id]["document"])
            self.assertEqual("PASS", result.status)
            self.assertEqual("HOLD", result.binding_outcome)

    def test_valid_deny_projections(self) -> None:
        for case_id in ("deny-actor-mismatch", "deny-expired", "deny-role-mismatch"):
            result = module.validate_document(self.by_id[case_id]["document"])
            self.assertEqual("PASS", result.status)
            self.assertEqual("DENY", result.binding_outcome)

    def test_identity_tamper_fails_closed(self) -> None:
        result = module.validate_document(self.by_id["invalid-spec-hash"]["document"])
        self.assertEqual("DENY", result.status)
        self.assertIn("BINDING_SPEC_HASH_MISMATCH", {finding.code for finding in result.findings})

    def test_outcome_tamper_fails_closed(self) -> None:
        result = module.validate_document(self.by_id["invalid-outcome-tamper"]["document"])
        codes = {finding.code for finding in result.findings}
        self.assertEqual("DENY", result.status)
        self.assertEqual({"BINDING_ID_MISMATCH", "BINDING_SPEC_HASH_MISMATCH", "OUTCOME_MISMATCH"}, codes)

    def test_self_review_fails_closed(self) -> None:
        result = module.validate_document(self.by_id["invalid-self-review"]["document"])
        self.assertEqual("DENY", result.status)
        self.assertIn("SELF_REVIEW_DENIED", {finding.code for finding in result.findings})

    def test_missing_apply_responsibility_fails_closed(self) -> None:
        result = module.validate_document(self.by_id["invalid-missing-apply-responsibility"]["document"])
        self.assertEqual("DENY", result.status)
        self.assertIn("PREFLIGHT_RESPONSIBILITY_REQUIRED", {finding.code for finding in result.findings})

    def test_symlink_input_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "fixture.json"
            target.write_text(json.dumps(self.by_id["bound-active-approved"]["document"]), encoding="utf-8")
            link = Path(directory) / "link.json"
            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            result = module.validate_file(link)
            self.assertEqual("ERROR", result.status)
            self.assertEqual({"BINDING_JSON_INVALID"}, {finding.code for finding in result.findings})

    def test_cli_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR), "--fixtures"]
        first = subprocess.run(command, check=True, capture_output=True, text=True)
        second = subprocess.run(command, check=True, capture_output=True, text=True)
        self.assertEqual(first.stdout, second.stdout)
        self.assertTrue(json.loads(first.stdout)["ok"])

    def test_validator_has_no_network_or_write_surface(self) -> None:
        source = VALIDATOR.read_text(encoding="utf-8")
        for token in ("import requests", "import urllib", "import socket", "import subprocess", "from subprocess",
                      ".write_text(", ".write_bytes(", "os.remove(", "os.replace(", "open("):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
