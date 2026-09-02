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

from tools.validators.evidence import validate_analytic_output_disclosure_assessment as validator

ROOT = Path(__file__).resolve().parents[3]


class AnalyticOutputDisclosureAssessmentTests(unittest.TestCase):
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

    def test_all_analytic_kinds_have_supported_positive_cases(self) -> None:
        manifest = validator.load_fixtures()
        kinds = {
            validator.materialize_case(manifest, case)["output"]["analysis_kind"]
            for case in manifest["cases"]
            if case["expected_outcome"] == "PASS"
        }
        self.assertEqual(set(validator.ROLE_BY_KIND), kinds)
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"PASS", "ABSTAIN", "DENY", "ERROR"}, set(outcomes))
        self.assertGreaterEqual(outcomes["DENY"], 25)

    def test_method_bindings_are_kind_scoped(self) -> None:
        manifest = validator.load_fixtures()
        by_kind = {
            validator.materialize_case(manifest, case)["output"]["analysis_kind"]:
            validator.materialize_case(manifest, case)["method"]
            for case in manifest["cases"]
            if case["expected_outcome"] == "PASS"
        }
        self.assertIsNotNone(by_kind["INDICATOR"]["indicator_definition_ref"])
        for field in (
            "feature_set_manifest_ref",
            "model_card_ref",
            "model_run_receipt_ref",
            "training_lineage_ref",
        ):
            self.assertIsNotNone(by_kind["ML_MODEL"][field])
        self.assertIsNotNone(by_kind["MODEL_INTERPRETATION"]["model_card_ref"])
        self.assertIsNotNone(by_kind["MODEL_INTERPRETATION"]["model_run_receipt_ref"])
        self.assertTrue(
            all(value is None for key, value in by_kind["STATISTIC"].items() if key != "method_ref")
        )

    def test_required_interpretation_limits_are_kind_scoped(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            if case["expected_outcome"] != "PASS":
                continue
            document = validator.materialize_case(manifest, case)
            kind = document["output"]["analysis_kind"]
            limits = set(document["disclosure"]["interpretation_limits"])
            with self.subTest(kind=kind):
                self.assertTrue(validator.required_limits(kind).issubset(limits))

    def test_identity_is_content_addressed_and_replay_stable(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        first = validator.canonical_identity(document)
        second = validator.canonical_identity(json.loads(json.dumps(document)))
        self.assertEqual(first, second)
        changed = json.loads(json.dumps(document))
        changed["output"]["analytic_output_ref"] = "kfm://analytic-output/synthetic-statistic-v2"
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
        sentinel = "do-not-echo-analytic-value"
        document["output"]["analytic_output_ref"] = f"kfm://analytic-output/{sentinel}"
        result = validator.validate_payload(document)
        rendered = validator.serialize(Path("candidate.json"), result)
        self.assertNotIn(sentinel, rendered)
        self.assertNotIn("synthetic-statistic", rendered)

    def test_cli_fixture_replay_and_parser_error_are_deterministic(self) -> None:
        command = [sys.executable, str(Path(validator.__file__)), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn('"cases":40', first.stdout)
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
                (duplicate, "ANALYTIC_JSON_DUPLICATE_KEY"),
                (nonfinite, "ANALYTIC_JSON_NONFINITE_NUMBER"),
                (link, "ANALYTIC_INPUT_SYMLINK_DENIED"),
                (oversized, "ANALYTIC_INPUT_TOO_LARGE"),
            ):
                with self.subTest(path=path.name):
                    value, findings = validator._read(path)
                    self.assertIsNone(value)
                    self.assertEqual(code, findings[0].code)


if __name__ == "__main__":
    unittest.main()
