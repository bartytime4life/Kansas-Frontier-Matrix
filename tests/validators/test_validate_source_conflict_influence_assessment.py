from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.evidence import validate_source_conflict_influence_assessment as validator

ROOT = Path(__file__).resolve().parents[2]


class SourceConflictInfluenceAssessmentTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_cases(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(manifest, case))
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(case["expected_status"], result.status)
                self.assertEqual(case["expected_relationship"], result.relationship)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_and_relationships_are_non_vacuous(self) -> None:
        manifest = validator.load_fixtures()
        statuses = Counter(case["expected_status"] for case in manifest["cases"])
        relationships = {case["expected_relationship"] for case in manifest["cases"] if case["expected_status"] == "PASS"}
        self.assertEqual({"PASS", "DENY"}, set(statuses))
        self.assertGreaterEqual(statuses["DENY"], 12)
        self.assertEqual({"CONSISTENT", "DIVERGENT", "CONFLICTING", "INSUFFICIENT", "REVOKED_EVIDENCE"}, relationships)

    def test_complete_pair_matrix_is_order_invariant_by_construction(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        source_ids = [item["source_id"] for item in document["sources"]]
        self.assertEqual(sorted(source_ids), source_ids)
        self.assertEqual(validator._expected_pair_ids(source_ids), [item["pair_id"] for item in document["comparisons"]])
        self.assertTrue(document["comparison_profile"]["order_invariant"])

    def test_source_roles_reuse_source_descriptor_vocabulary(self) -> None:
        conflict_schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        descriptor_schema = json.loads((ROOT / "schemas/contracts/v1/source/source_descriptor.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(descriptor_schema["$defs"]["source_role"]["enum"], conflict_schema["$defs"]["source_role"]["enum"])

    def test_governance_non_effects_are_false(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        self.assertFalse(document["summary"]["claim_resolution_allowed"])
        self.assertTrue(document["summary"]["separate_policy_gate_required"])
        self.assertEqual("FIXTURE_ONLY", document["governance"]["execution_mode"])
        self.assertFalse(any(value for key, value in document["governance"].items() if key != "execution_mode"))

    def test_duplicate_keys_fail_closed_without_echo(self) -> None:
        marker = "SOURCE_CONFLICT_ECHO_SENTINEL"
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
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn('"suite_match":true', completed.stdout)

    def test_validator_has_no_network_or_source_client(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "boto3", "psycopg"):
            self.assertNotIn(token, source)

    def test_source_map_names_full_atlas_triad_and_candidates(self) -> None:
        source_map = (ROOT / "docs/intake/exploratory/source-conflict-influence-assessment-source-map.md").read_text(encoding="utf-8")
        for value in ("KFM-TRIAD-065", "KFM-CAND-0193", "KFM-CAND-0194", "KFM-CAND-0195"):
            self.assertIn(value, source_map)


if __name__ == "__main__":
    unittest.main()
