from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators import validate_outcome_projection_parity as validator

ROOT = Path(__file__).resolve().parents[2]


class OutcomeProjectionParityTests(unittest.TestCase):
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
                    case["expected_parity_status"], result.parity_status
                )
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_and_statuses_are_non_vacuous(self) -> None:
        manifest = validator.load_fixtures()
        statuses = Counter(
            case["expected_status"] for case in manifest["cases"]
        )
        parity_statuses = {
            case["expected_parity_status"]
            for case in manifest["cases"]
            if case["expected_parity_status"] is not None
        }
        self.assertEqual({"PASS", "DENY"}, set(statuses))
        self.assertGreaterEqual(statuses["PASS"], 7)
        self.assertGreaterEqual(statuses["DENY"], 10)
        self.assertEqual(
            {
                "PARITY_CONFIRMED",
                "AUTHORIZED_DEGRADATION",
                "PARITY_FAILURE",
            },
            parity_statuses,
        )

    def test_all_four_finite_outcomes_are_preserved(self) -> None:
        manifest = validator.load_fixtures()
        cases = {
            case["case_id"]: case
            for case in manifest["cases"]
            if case["case_id"].endswith("parity-preserved")
        }
        outcomes = {
            validator.materialize_case(manifest, case)["report"][
                "terminal_outcome"
            ]
            for case in cases.values()
        }
        self.assertEqual({"ANSWER", "ABSTAIN", "DENY", "ERROR"}, outcomes)

    def test_profile_matrix_has_no_upgrade_to_answer(self) -> None:
        profile = validator.load_fixtures()["base"]["projection_profile"]
        self.assertEqual(
            list(validator.SAFE_OUTCOME_PAIRS),
            profile["allowed_outcome_pairs"],
        )
        for source in ("ABSTAIN", "DENY", "ERROR"):
            self.assertNotIn(
                f"{source}->ANSWER", profile["allowed_outcome_pairs"]
            )

    def test_report_is_reproduced_and_never_authorizes_trust(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            if case["expected_parity_status"] is None:
                continue
            with self.subTest(case=case["case_id"]):
                document = validator.materialize_case(manifest, case)
                self.assertEqual(
                    validator.expected_report(document), document["report"]
                )
                self.assertFalse(document["report"]["trusted_surface_allowed"])
                self.assertTrue(
                    document["report"]["separate_policy_review_required"]
                )

    def test_governance_non_effects_are_false(self) -> None:
        document = validator.materialize_case(
            validator.load_fixtures(),
            validator.load_fixtures()["cases"][0],
        )
        self.assertEqual(
            "FIXTURE_ONLY", document["governance"]["execution_mode"]
        )
        self.assertFalse(
            any(
                value
                for key, value in document["governance"].items()
                if key != "execution_mode"
            )
        )

    def test_runtime_envelope_names_the_same_finite_outcomes(self) -> None:
        source = (
            ROOT
            / "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json"
        ).read_text(encoding="utf-8")
        for outcome in ("ANSWER", "ABSTAIN", "DENY", "ERROR"):
            self.assertIn(f'"{outcome}"', source)

    def test_duplicate_keys_fail_closed_without_echo(self) -> None:
        marker = "OUTCOME_PARITY_ECHO_SENTINEL"
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
            [
                sys.executable,
                str(Path(validator.__file__)),
                "--fixtures",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn('"suite_match":true', completed.stdout)

    def test_validator_has_no_network_or_runtime_client(self) -> None:
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
            / "docs/intake/exploratory/outcome-projection-parity-source-map.md"
        ).read_text(encoding="utf-8")
        for value in (
            "KFM-TRIAD-066",
            "KFM-CAND-0196",
            "KFM-CAND-0197",
            "KFM-CAND-0198",
            "New Ideas 4-14-26",
            "New Ideas 4-15-26",
        ):
            self.assertIn(value, source_map)


if __name__ == "__main__":
    unittest.main()
