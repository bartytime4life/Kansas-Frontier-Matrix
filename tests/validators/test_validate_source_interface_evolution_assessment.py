from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.source import (
    validate_source_interface_evolution_assessment as validator,
)

ROOT = Path(__file__).resolve().parents[2]


class SourceInterfaceEvolutionAssessmentTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_cases(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(
                    validator.materialize_case(manifest, case)
                )
                actual = [
                    {"code": item.code, "path": item.path}
                    for item in result.findings
                ]
                self.assertEqual(case["expected_status"], result.status)
                self.assertEqual(
                    case["expected_assessment_state"],
                    result.assessment_state,
                )
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_and_states_are_non_vacuous(self) -> None:
        manifest = validator.load_fixtures()
        statuses = Counter(
            case["expected_status"] for case in manifest["cases"]
        )
        states = {
            case["expected_assessment_state"]
            for case in manifest["cases"]
            if case["expected_assessment_state"] is not None
        }
        self.assertEqual({"PASS", "DENY"}, set(statuses))
        self.assertGreaterEqual(statuses["PASS"], 10)
        self.assertGreaterEqual(statuses["DENY"], 10)
        self.assertEqual(
            {
                "UNCHANGED",
                "MIGRATION_HELD",
                "DUAL_READ_CANDIDATE",
                "MIGRATION_CANDIDATE",
                "ROLLBACK_CANDIDATE",
                "RETIREMENT_REVIEW_CANDIDATE",
            },
            states,
        )

    def test_finite_compatibility_grammar_is_exercised(self) -> None:
        manifest = validator.load_fixtures()
        classifications = {
            validator.expected_compatibility(
                validator.materialize_case(manifest, case)
            )["classification"]
            for case in manifest["cases"]
            if case["case_id"]
            in {
                "unchanged-interface",
                "additive-interface-migration-candidate",
                "breaking-interface-dual-read-candidate",
                "redirect-observation-held",
                "partial-observation-held",
                "undocumented-drift-held",
                "canonical-identity-change-denied",
            }
        }
        self.assertEqual(
            {
                "UNCHANGED",
                "ADDITIVE",
                "BREAKING",
                "REDIRECTED",
                "PARTIAL_SAMPLE",
                "UNDOCUMENTED",
                "INCOMPARABLE",
            },
            classifications,
        )

    def test_breaking_change_requires_bound_dual_read(self) -> None:
        manifest = validator.load_fixtures()
        cases = {case["case_id"]: case for case in manifest["cases"]}
        denied = validator.validate_payload(
            validator.materialize_case(
                manifest, cases["breaking-change-without-dual-read"]
            )
        )
        proposed = validator.validate_payload(
            validator.materialize_case(
                manifest,
                cases["breaking-interface-dual-read-candidate"],
            )
        )
        self.assertEqual("DENY", denied.status)
        self.assertEqual("PASS", proposed.status)
        self.assertEqual("DUAL_READ_CANDIDATE", proposed.assessment_state)

    def test_summary_is_reproduced_and_never_authorizes_trust(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            if case["expected_status"] != "PASS":
                continue
            with self.subTest(case=case["case_id"]):
                document = validator.materialize_case(manifest, case)
                self.assertEqual(
                    validator.expected_summary(document), document["summary"]
                )
                self.assertFalse(document["summary"]["trusted_surface_allowed"])
                self.assertTrue(
                    document["migration"]["separate_decision_required"]
                )
                self.assertFalse(document["migration"]["decision_has_effect"])

    def test_governance_non_effects_are_false(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        governance = document["governance"]
        self.assertEqual("FIXTURE_ONLY", governance["execution_mode"])
        self.assertFalse(
            any(
                value
                for key, value in governance.items()
                if key != "execution_mode"
            )
        )

    def test_duplicate_keys_fail_closed_without_echo(self) -> None:
        marker = "INTERFACE_EVOLUTION_ECHO_SENTINEL"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(
                '{"object_type":"%s","object_type":"duplicate"}' % marker,
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(path)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertNotEqual(0, completed.returncode)
        self.assertIn("JSON_DUPLICATE_KEY", completed.stdout)
        self.assertNotIn(marker, completed.stdout)
        self.assertNotIn(marker, completed.stderr)

    def test_symlink_input_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            target.write_text("{}", encoding="utf-8")
            path = Path(directory) / "candidate.json"
            path.symlink_to(target)
            completed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(path)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertNotEqual(0, completed.returncode)
        self.assertIn("JSON_INPUT_SYMLINK_DENIED", completed.stdout)

    def test_oversized_input_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_bytes(b" " * (validator.MAX_JSON_BYTES + 1))
            completed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(path)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertNotEqual(0, completed.returncode)
        self.assertIn("JSON_INPUT_TOO_LARGE", completed.stdout)

    def test_fixture_cli(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(Path(validator.__file__)), "--fixtures"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn('"suite_match":true', completed.stdout)

    def test_validator_has_no_network_or_connector_client(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in (
            "requests",
            "urllib.request",
            "httpx",
            "aiohttp",
            "boto3",
            "psycopg",
        ):
            self.assertNotIn(token, source)

    def test_source_map_names_full_atlas_triad_and_candidates(self) -> None:
        source_map = (
            ROOT
            / "docs/intake/exploratory/source-interface-evolution-source-map.md"
        ).read_text(encoding="utf-8")
        for value in (
            "KFM-TRIAD-070",
            "KFM-CAND-0208",
            "KFM-CAND-0209",
            "KFM-CAND-0210",
            "New Ideas 4-14-26",
        ):
            self.assertIn(value, source_map)


if __name__ == "__main__":
    unittest.main()
