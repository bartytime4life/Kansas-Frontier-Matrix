from __future__ import annotations

import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.citation import validate_citation_validation_report as validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    ROOT
    / "schemas/contracts/v1/evidence/citation_validation_report.schema.json"
)
VALIDATOR_PATH = (
    ROOT
    / "tools/validators/citation/validate_citation_validation_report.py"
)
WRAPPER_PATH = ROOT / "tools/validators/validate_citation_validation.py"
SOURCE_MAP_PATH = (
    ROOT
    / "docs/intake/exploratory/citation-validation-report-closure-source-map.md"
)


class CitationValidationReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = validator.load_fixtures()
        cls.cases = {
            case["case_id"]: case for case in cls.manifest["cases"]
        }

    def materialize(self, case_id: str) -> dict[str, object]:
        return validator.materialize_case(
            self.manifest,
            self.cases[case_id],
        )

    def test_schema_is_valid_draft_2020_12_and_closed(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        for name in ("subject", "locator", "citation", "summary"):
            with self.subTest(definition=name):
                self.assertFalse(schema["$defs"][name]["additionalProperties"])

    def test_exact_fixture_suite(self) -> None:
        self.assertEqual(0, validator.run_fixtures())

    def test_fixture_outcomes_cover_all_finite_states(self) -> None:
        statuses: set[str] = set()
        report_outcomes: set[str] = set()
        for case in self.manifest["cases"]:
            result = validator.validate_payload(
                validator.materialize_case(self.manifest, case)
            )
            statuses.add(result.outcome)
            if result.report_outcome is not None:
                report_outcomes.add(result.report_outcome)
        self.assertEqual({"PASS", "ABSTAIN", "DENY", "ERROR"}, statuses)
        self.assertEqual(
            {"PASS", "ABSTAIN", "DENY", "ERROR"},
            report_outcomes,
        )

    def test_identity_is_deterministic_and_sensitive(self) -> None:
        first = self.materialize("valid-internal-review-pass")
        second = self.materialize("valid-internal-review-pass")
        self.assertEqual(first["report_id"], second["report_id"])
        self.assertEqual(first["spec_hash"], second["spec_hash"])
        changed = copy.deepcopy(first)
        changed["checked_at"] = "2026-08-10T18:31:00Z"
        digest, identifier = validator.canonical_identity(changed)
        self.assertNotEqual(first["spec_hash"], digest)
        self.assertNotEqual(first["report_id"], identifier)

    def test_missing_evidence_abstains_without_becoming_false(self) -> None:
        payload = self.materialize("valid-missing-evidence-abstains")
        result = validator.validate_payload(payload)
        self.assertEqual("ABSTAIN", result.outcome)
        self.assertTrue(payload["summary"]["blocking"])
        self.assertIn(
            "CITATION_MISSING",
            payload["citations"][0]["reason_codes"],
        )
        self.assertNotEqual("PASS", payload["citations"][0]["declared_outcome"])

    def test_public_candidate_requires_policy_review_and_release(self) -> None:
        held = self.materialize("valid-public-unreleased-citation-abstains")
        passed = self.materialize("valid-public-candidate-pass")
        self.assertEqual(
            "ABSTAIN",
            validator.validate_payload(held).outcome,
        )
        self.assertEqual("PASS", validator.validate_payload(passed).outcome)
        self.assertIn(
            "CITATION_RELEASE_NOT_READY",
            held["summary"]["reason_codes"],
        )

    def test_rights_and_withdrawal_denials_are_preserved(self) -> None:
        rights = self.materialize("valid-rights-denial-preserved")
        withdrawn = self.materialize(
            "valid-withdrawn-public-citation-denied"
        )
        self.assertEqual("DENY", validator.validate_payload(rights).outcome)
        self.assertEqual(
            "DENY",
            validator.validate_payload(withdrawn).outcome,
        )
        self.assertIn(
            "CITATION_RIGHTS_DENIED",
            rights["summary"]["reason_codes"],
        )
        self.assertIn(
            "CITATION_RELEASE_WITHDRAWN",
            withdrawn["summary"]["reason_codes"],
        )

    def test_parser_rejects_duplicate_keys_and_nonfinite_numbers(self) -> None:
        samples = [
            (
                '{"a":1,"a":2}',
                "CITATION_REPORT_JSON_DUPLICATE_KEY",
            ),
            (
                '{"a":NaN}',
                "CITATION_REPORT_JSON_NONFINITE_NUMBER",
            ),
        ]
        with tempfile.TemporaryDirectory() as directory:
            for index, (content, expected_code) in enumerate(samples):
                with self.subTest(expected_code=expected_code):
                    path = Path(directory) / f"sample-{index}.json"
                    path.write_text(content, encoding="utf-8")
                    value, findings = validator._read(path)
                    self.assertIsNone(value)
                    self.assertEqual(expected_code, findings[0].code)

    def test_parser_rejects_symlink_input(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = Path(directory) / "link.json"
            link.symlink_to(target)
            value, findings = validator._read(link)
            self.assertIsNone(value)
            self.assertEqual(
                "CITATION_REPORT_INPUT_SYMLINK_DENIED",
                findings[0].code,
            )

    def test_fixtures_are_synthetic_and_network_free(self) -> None:
        fixture_text = json.dumps(self.manifest, sort_keys=True).lower()
        for forbidden in (
            "http://",
            "https://",
            "gdrive://",
            "drive.google",
            "token=",
            "password",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, fixture_text)
        self.assertIn("kfm:fixture:", fixture_text)
        with mock.patch(
            "socket.socket",
            side_effect=AssertionError("validator network access denied"),
        ):
            self.assertEqual(0, validator.run_fixtures())

    def test_every_authority_effect_is_false(self) -> None:
        for case_id in (
            "valid-internal-review-pass",
            "valid-public-candidate-pass",
            "valid-missing-evidence-abstains",
            "valid-rights-denial-preserved",
        ):
            with self.subTest(case_id=case_id):
                payload = self.materialize(case_id)
                self.assertTrue(
                    all(value is False for value in payload["permissions"].values())
                )
                self.assertEqual(
                    [
                        "declared_states_not_authenticated",
                        "no_evidence_resolution",
                        "no_policy_evaluation",
                        "no_review_authentication",
                        "no_release_verification",
                        "no_publication_authority",
                    ],
                    payload["limitations"],
                )

    def test_compatibility_entrypoint_runs_the_same_fixture_suite(self) -> None:
        environment = os.environ.copy()
        environment.update(
            {
                "KFM_NO_NETWORK": "1",
                "PYTHONHASHSEED": "0",
                "PYTHONDONTWRITEBYTECODE": "1",
                "TZ": "UTC",
            }
        )
        completed = subprocess.run(
            [sys.executable, str(WRAPPER_PATH), "--fixtures"],
            cwd=ROOT,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        report = json.loads(completed.stdout)
        self.assertTrue(report["suite_match"])
        self.assertEqual(len(self.manifest["cases"]), report["cases"])

    def test_source_map_is_repository_only_and_paths_exist(self) -> None:
        self.assertTrue(VALIDATOR_PATH.is_file())
        self.assertTrue(SOURCE_MAP_PATH.is_file())
        text = SOURCE_MAP_PATH.read_text(encoding="utf-8").lower()
        for forbidden in (
            "gdrive://",
            "drive.google",
            "connected private",
            "private document",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, text)
        self.assertIn("public repository files only", text)


if __name__ == "__main__":
    unittest.main()
