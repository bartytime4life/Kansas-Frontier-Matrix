from __future__ import annotations

import json
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.release import validate_signed_rollback_token as validator

ROOT = Path(__file__).resolve().parents[2]


class SignedRollbackTokenTests(unittest.TestCase):
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
        self.assertGreaterEqual(outcomes["DENY"], 10)

    def test_ready_token_binds_prior_release_and_receipt(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        self.assertLess(document["rollback_target"]["alias_revision"], document["current"]["alias_revision"])
        self.assertEqual(document["current"]["alias_revision"] + 1, document["revert_receipt_template"]["next_alias_revision"])
        self.assertEqual(document["rollback_target"]["spec_hash"], document["revert_receipt_template"]["target_spec_hash"])
        self.assertEqual(validator.signing_payload_digest(document), document["signature"]["subject_digest"])

    def test_signing_payload_changes_with_target(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        before = validator.signing_payload_digest(document)
        document["rollback_target"]["spec_hash"] = "sha256:" + "9" * 64
        after = validator.signing_payload_digest(document)
        self.assertNotEqual(before, after)

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
