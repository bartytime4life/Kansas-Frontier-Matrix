from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators import validate_pipeline_replay_assessment as validator

ROOT = Path(__file__).resolve().parents[2]


class PipelineReplayAssessmentTests(unittest.TestCase):
    def test_schema_is_valid_and_closed(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual("PROPOSED", schema["x-kfm"]["status"])

    def test_exact_fixture_cases(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(manifest, case))
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(case["expected_status"], result.status)
                self.assertEqual(case["expected_replay_outcome"], result.replay_outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_and_report_outcomes_are_non_vacuous(self) -> None:
        cases = validator.load_fixtures()["cases"]
        statuses = Counter(case["expected_status"] for case in cases)
        outcomes = {case["expected_replay_outcome"] for case in cases if case["expected_status"] == "PASS"}
        self.assertGreaterEqual(statuses["PASS"], 7)
        self.assertGreaterEqual(statuses["DENY"], 6)
        self.assertEqual({"PASS", "FAIL"}, outcomes)

    def test_every_drift_dimension_is_covered(self) -> None:
        manifest = validator.load_fixtures()
        codes: set[str] = set()
        for case in manifest["cases"]:
            if case["expected_status"] == "PASS":
                document = validator.materialize_case(manifest, case)
                codes.update(document["report"]["drift_codes"])
        self.assertEqual({"SOURCE_SNAPSHOT_DRIFT", "TRANSFORM_PARAMETERS_DRIFT", "MODEL_IDENTITY_DRIFT", "VALIDATOR_SET_DRIFT", "OUTPUT_DRIFT"}, codes)

    def test_report_never_claims_execution_or_authoritative_equivalence(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            if case["expected_status"] != "PASS":
                continue
            document = validator.materialize_case(manifest, case)
            self.assertEqual(validator.expected_report(document), document["report"])
            self.assertFalse(document["report"]["replay_execution_claimed"])
            self.assertFalse(document["report"]["replay_equivalence_authoritative"])
            self.assertFalse(document["governance"]["pipeline_executed"])

    def test_identity_tamper_is_denied(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        document["pipeline_ref"] = "kfm:pipeline:tampered"
        result = validator.validate_payload(document)
        self.assertEqual("DENY", result.status)
        self.assertEqual("PIPELINE_REPLAY_SPEC_HASH_MISMATCH", result.findings[0].code)

    def test_duplicate_keys_fail_closed_without_echo(self) -> None:
        marker = "PIPELINE_REPLAY_ECHO_SENTINEL"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text('{"object_type":"%s","object_type":"duplicate"}' % marker, encoding="utf-8")
            completed = subprocess.run([sys.executable, str(Path(validator.__file__)), str(path)], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertNotEqual(0, completed.returncode)
        self.assertIn("JSON_DUPLICATE_KEY", completed.stdout)
        self.assertNotIn(marker, completed.stdout + completed.stderr)

    def test_symlink_and_oversized_input_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = Path(directory) / "link.json"
            link.symlink_to(target)
            linked = subprocess.run([sys.executable, str(Path(validator.__file__)), str(link)], cwd=ROOT, capture_output=True, text=True, check=False)
            large = Path(directory) / "large.json"
            large.write_bytes(b" " * (validator.MAX_JSON_BYTES + 1))
            oversized = subprocess.run([sys.executable, str(Path(validator.__file__)), str(large)], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertIn("JSON_INPUT_SYMLINK_DENIED", linked.stdout)
        self.assertIn("JSON_INPUT_TOO_LARGE", oversized.stdout)

    def test_fixture_cli(self) -> None:
        completed = subprocess.run([sys.executable, str(Path(validator.__file__)), "--fixtures"], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn('"suite_match":true', completed.stdout)

    def test_validator_has_no_network_pipeline_model_or_runtime_client(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "boto3", "subprocess", "openai", "dagster"):
            self.assertNotIn(token, source)

    def test_source_map_names_drive_card_and_adjacent_boundaries(self) -> None:
        source = (ROOT / "docs/intake/exploratory/pipeline-replay-assessment-source-map.md").read_text(encoding="utf-8")
        for value in ("Replay Verification of Pipelines and Receipts Implementation Surface", "SRC-DOCTRINE", "SRC-AIBOC", "RecompileManifest", "ReplaySafeEffectLedger"):
            self.assertIn(value, source)


if __name__ == "__main__":
    unittest.main()
