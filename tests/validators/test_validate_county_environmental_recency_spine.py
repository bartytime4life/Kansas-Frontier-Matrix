from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.data import validate_county_environmental_recency_spine as validator

ROOT = Path(__file__).resolve().parents[2]


class CountyEnvironmentalRecencySpineTests(unittest.TestCase):
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
        self.assertGreaterEqual(outcomes["DENY"], 9)

    def test_complete_fixture_has_exact_required_lanes(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        self.assertEqual(list(validator.LANES), [item["lane"] for item in document["entries"]])
        self.assertEqual("COMPLETE", document["summary"]["overall_outcome"])
        self.assertTrue(document["summary"]["separate_interpretation_gate_required"])

    def test_reuses_existing_source_health_vocabulary(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        health = schema["$defs"]["entry"]["properties"]["health_outcome"]["enum"]
        self.assertEqual(["HEALTHY", "DEGRADED", "STALE", "UNAVAILABLE", "UNKNOWN"], health)

    def test_governance_non_effects_are_false(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        self.assertEqual("FIXTURE_ONLY", document["governance"]["execution_mode"])
        self.assertFalse(any(value for key, value in document["governance"].items() if key != "execution_mode"))

    def test_duplicate_keys_fail_closed_without_echo(self) -> None:
        marker = "RECENCY_ECHO_SENTINEL"
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

    def test_validator_has_no_network_client(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "socket."):
            self.assertNotIn(token, source)

    def test_source_map_names_both_pass_32_cards(self) -> None:
        source_map = (ROOT / "docs/intake/exploratory/pass-32-county-environmental-recency-source-map.md").read_text(encoding="utf-8")
        self.assertIn("KFM-P32-FEAT-0015", source_map)
        self.assertIn("KFM-P32-IDEA-0001", source_map)


if __name__ == "__main__":
    unittest.main()
