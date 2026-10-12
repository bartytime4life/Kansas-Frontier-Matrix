from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.evidence import validate_economic_observation as validator

ROOT = Path(__file__).resolve().parents[3]


class EconomicObservationTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(manifest, case))
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_positive_cases_cover_price_suppression_industry_missing_and_correction(self) -> None:
        manifest = validator.load_fixtures()
        passing = [
            validator.materialize_case(manifest, case)
            for case in manifest["cases"]
            if case["expected_outcome"] == "PASS"
        ]
        self.assertTrue({"EMPLOYMENT", "GDP", "AVERAGE_ANNUAL_WAGE"}.issubset(
            {item["measure"]["measure_family"] for item in passing}
        ))
        self.assertEqual(
            {"OBSERVED", "SUPPRESSED", "MISSING"},
            {item["measure"]["result_state"] for item in passing},
        )
        self.assertTrue({"CURRENT_DOLLARS", "CONSTANT_DOLLARS"}.issubset(
            {item["measure"]["price_basis"] for item in passing}
        ))
        self.assertIn(
            "SPECIFIC_INDUSTRY",
            {item["measure"]["industry_scope"] for item in passing},
        )
        self.assertIn(
            "CORRECTED",
            {item["lineage"]["correction_state"] for item in passing},
        )
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"PASS", "DENY"}, set(outcomes))
        self.assertGreaterEqual(outcomes["DENY"], 35)

    def test_suppressed_value_remains_absent_and_method_bound(self) -> None:
        manifest = validator.load_fixtures()
        case = next(case for case in manifest["cases"] if case["case_id"] == "valid-suppressed-gdp")
        document = validator.materialize_case(manifest, case)
        self.assertIsNone(document["measure"]["value"])
        self.assertEqual("SUPPRESSED", document["measure"]["result_state"])
        self.assertEqual("CONFIDENTIALITY", document["suppression"]["reason"])
        self.assertIsNotNone(document["suppression"]["method_ref"])
        self.assertEqual("PASS", validator.validate_payload(document).outcome)

    def test_fixture_has_no_business_person_geometry_or_classification_output(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        keys: set[str] = set()

        def collect(value: object) -> None:
            if isinstance(value, dict):
                keys.update(value)
                for item in value.values():
                    collect(item)
            elif isinstance(value, list):
                for item in value:
                    collect(item)

        collect(document)
        forbidden = {
            "establishment_id",
            "business_name",
            "person_id",
            "address",
            "coordinates",
            "geometry",
            "classification_result",
            "frontier_status",
        }
        self.assertTrue(forbidden.isdisjoint(keys))
        governance = dict(document["governance"])
        self.assertEqual("FIXTURE_ONLY", governance.pop("execution_mode"))
        self.assertTrue(all(value is False for value in governance.values()))

    def test_identity_is_content_addressed_and_replay_stable(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        first = validator.canonical_identity(document)
        second = validator.canonical_identity(json.loads(json.dumps(document)))
        self.assertEqual(first, second)
        changed = json.loads(json.dumps(document))
        changed["measure"]["value"] += 1
        self.assertNotEqual(first, validator.canonical_identity(changed))

    def test_validation_does_not_open_network(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        with mock.patch("socket.socket", side_effect=AssertionError("network denied")):
            result = validator.validate_payload(document)
        self.assertEqual("PASS", result.outcome)
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "socket."):
            self.assertNotIn(token, source)

    def test_serialization_does_not_echo_payload_values(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        sentinel = "do-not-echo-economic-value"
        document["source"]["source_variable_ref"] = (
            "kfm://source-variable/" + sentinel
            + "@sha256:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
        )
        result = validator.validate_payload(document)
        rendered = validator.serialize(Path("candidate.json"), result)
        self.assertNotIn(sentinel, rendered)
        self.assertNotIn("1234", rendered)

    def test_cli_fixture_replay_and_parser_error_are_deterministic(self) -> None:
        command = [sys.executable, str(Path(validator.__file__)), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn('"cases":46', first.stdout)
        self.assertIn('"suite_match":true', first.stdout)

        with tempfile.TemporaryDirectory() as directory:
            invalid = Path(directory) / "invalid.json"
            invalid.write_text("{", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(invalid)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(2, completed.returncode)
        self.assertIn('"outcome":"ERROR"', completed.stdout)

    def test_duplicate_nonfinite_symlink_and_oversize_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":NaN}', encoding="utf-8")
            target = root / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = root / "link.json"
            link.symlink_to(target)
            oversized = root / "oversized.json"
            oversized.write_bytes(b" " * (validator.MAX_BYTES + 1))

            for path, code in (
                (duplicate, "ECONOMIC_JSON_DUPLICATE_KEY"),
                (nonfinite, "ECONOMIC_JSON_NONFINITE_NUMBER"),
                (link, "ECONOMIC_INPUT_SYMLINK_DENIED"),
                (oversized, "ECONOMIC_INPUT_TOO_LARGE"),
            ):
                with self.subTest(path=path.name):
                    value, findings = validator._read(path)
                    self.assertIsNone(value)
                    self.assertEqual(code, findings[0].code)


if __name__ == "__main__":
    unittest.main()
