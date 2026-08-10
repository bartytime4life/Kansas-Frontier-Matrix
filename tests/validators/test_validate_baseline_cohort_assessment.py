from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.data import validate_baseline_cohort_assessment as validator

ROOT = Path(__file__).resolve().parents[2]


class BaselineCohortAssessmentTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_cases(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(manifest, case))
                findings = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(case["expected_status"], result.status)
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], findings)

    def test_fixture_polarity_and_outcomes_are_non_vacuous(self) -> None:
        manifest = validator.load_fixtures()
        statuses = Counter(case["expected_status"] for case in manifest["cases"])
        outcomes = {case["expected_outcome"] for case in manifest["cases"] if case["expected_outcome"]}
        self.assertEqual({"PASS", "ABSTAIN", "DENY"}, set(statuses))
        self.assertGreaterEqual(statuses["DENY"], 9)
        self.assertEqual({"COMPLETE", "HOLD", "ABSTAIN"}, outcomes)

    def test_identity_is_deterministic(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        self.assertEqual(document["spec_hash"], validator.expected_spec_hash(document))
        self.assertEqual(document["assessment_id"], validator.expected_assessment_id(document["spec_hash"]))

    def test_payload_has_no_observation_values_and_governance_is_inactive(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        serialized = json.dumps(document, sort_keys=True)
        for key in ('"value"', '"mean"', '"median"', '"threshold"'):
            self.assertNotIn(key, serialized)
        self.assertEqual("FIXTURE_ONLY", document["governance"]["execution_mode"])
        self.assertFalse(any(value for key, value in document["governance"].items() if key != "execution_mode"))
        self.assertFalse(document["summary"]["baseline_use_authorized"])
        self.assertFalse(document["summary"]["baseline_publishable"])

    def test_duplicate_keys_fail_closed_without_echo(self) -> None:
        marker = "BASELINE_COHORT_ECHO_SENTINEL"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text('{"object_type":"%s","object_type":"duplicate"}' % marker, encoding="utf-8")
            completed = subprocess.run([sys.executable, str(Path(validator.__file__)), str(path)], cwd=ROOT, capture_output=True, text=True, check=False)
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
            completed = subprocess.run([sys.executable, str(Path(validator.__file__)), str(path)], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertNotEqual(0, completed.returncode)
        self.assertIn("JSON_INPUT_SYMLINK_DENIED", completed.stdout)

    def test_oversized_input_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_bytes(b" " * (validator.MAX_JSON_BYTES + 1))
            completed = subprocess.run([sys.executable, str(Path(validator.__file__)), str(path)], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertNotEqual(0, completed.returncode)
        self.assertIn("JSON_INPUT_TOO_LARGE", completed.stdout)

    def test_fixture_cli(self) -> None:
        completed = subprocess.run([sys.executable, str(Path(validator.__file__)), "--fixtures"], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn('"suite_match":true', completed.stdout)

    def test_validator_has_no_network_or_source_client(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "boto3", "psycopg"):
            self.assertNotIn(token, source)

    def test_source_map_names_full_atlas_triad_and_candidates(self) -> None:
        source_map = (ROOT / "docs/intake/exploratory/baseline-cohort-assessment-source-map.md").read_text(encoding="utf-8")
        for value in ("KFM-TRIAD-036", "KFM-CAND-0106", "KFM-CAND-0107", "KFM-CAND-0108"):
            self.assertIn(value, source_map)


if __name__ == "__main__":
    unittest.main()
