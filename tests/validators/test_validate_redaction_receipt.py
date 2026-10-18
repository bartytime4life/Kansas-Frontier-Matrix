from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.receipts import validate_redaction_receipt as validator

ROOT = Path(__file__).resolve().parents[2]


class RedactionReceiptTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual("contracts/shared/redaction_receipt.md", schema["x-kfm"]["contract_doc"])

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

    def test_public_fixture_contains_no_protected_or_reversal_material(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        self.assertFalse(document["exposure"]["protected_value_present"])
        self.assertFalse(document["exposure"]["reversal_material_present"])
        self.assertTrue(document["transform"]["hidden_parameters_withheld"])

    def test_governance_non_effects_are_false(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        self.assertEqual("FIXTURE_ONLY", document["governance"]["execution_mode"])
        self.assertFalse(any(value for key, value in document["governance"].items() if key != "execution_mode"))

    def test_validator_has_no_network_or_geometry_runtime_import(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "shapely", "geopandas"):
            self.assertNotIn(token, source)

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

    def _case(self, case_id: str, *mutations: dict) -> dict:
        manifest = validator.load_fixtures()
        case = dict(next(item for item in manifest["cases"] if item["case_id"] == case_id))
        case["mutations"] = [*case.get("mutations", []), *mutations]
        return validator.materialize_case(manifest, case)

    def _codes(self, document: dict) -> tuple[str, list[str]]:
        result = validator.validate_payload(document)
        return result.outcome, [item.code for item in result.findings]

    def test_public_candidate_requires_full_release_basis(self) -> None:
        for path, value, code in (
            ("/basis/evidence_refs", [], "REDACTION_EVIDENCE_REQUIRED"),
            ("/release_context/release_candidate_ref", None, "REDACTION_RELEASE_CANDIDATE_REQUIRED"),
            ("/release_context/rollback_ref", None, "REDACTION_ROLLBACK_REQUIRED"),
        ):
            with self.subTest(path=path):
                self.assertEqual(("DENY", [code]), self._codes(self._case("generalized-public", {"path": path, "value": value})))

    def test_withheld_content_cannot_be_public_or_tiered(self) -> None:
        outcome, codes = self._codes(self._case("withheld", {"path": "/exposure/output_public_candidate", "value": True}))
        self.assertEqual("DENY", outcome)
        self.assertIn("REDACTION_WITHHOLD_PUBLIC_FORBIDDEN", codes)
        self.assertEqual(
            ("DENY", ["REDACTION_WITHHOLD_TIER_FORBIDDEN"]),
            self._codes(self._case("withheld", {"path": "/exposure/output_sensitivity", "value": "T1"})),
        )

    def _cli(self, path: Path) -> tuple[int, dict]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = validator.main([str(path)])
        return code, json.loads(out.getvalue())

    def test_cli_exit_codes_follow_outcome(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            for case_id, outcome, exit_code in (
                ("generalized-public", "PASS", 0),
                ("public-missing-policy", "DENY", 1),
                ("processing-error", "ERROR", 2),
                ("review-hold", "ABSTAIN", 3),
            ):
                with self.subTest(case=case_id):
                    path = Path(directory) / f"{case_id}.json"
                    path.write_text(json.dumps(self._case(case_id)), encoding="utf-8")
                    code, report = self._cli(path)
                    self.assertEqual((exit_code, outcome), (code, report["outcome"]))
                    self.assertEqual("NONE", report["authority"])
                    self.assertIn("no_publication", report["non_effects"])

    def test_unreadable_inputs_are_errors_not_denials(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inputs = {
                "duplicate.json": ('{"a": 1, "a": 2}', "REDACTION_JSON_DUPLICATE_KEY"),
                "nan.json": ('{"a": NaN}', "REDACTION_JSON_NONFINITE_NUMBER"),
                "overflow.json": ('{"a": 1e400}', "REDACTION_JSON_NONFINITE_NUMBER"),
                "broken.json": ('{"a": ', "REDACTION_JSON_INVALID"),
                "huge-int.json": ('{"a": ' + "9" * 5000 + "}", "REDACTION_JSON_INVALID"),
                "latin1.json": (b'{"a": "\xff"}', "REDACTION_JSON_INVALID"),
                "array.json": ("[]", "REDACTION_ROOT_NOT_OBJECT"),
            }
            for name, (content, code) in inputs.items():
                path = root / name
                if isinstance(content, bytes):
                    path.write_bytes(content)
                else:
                    path.write_text(content, encoding="utf-8")
                with self.subTest(input=name):
                    exit_code, report = self._cli(path)
                    self.assertEqual(2, exit_code)
                    self.assertEqual("ERROR", report["outcome"])
                    self.assertEqual([{"code": code, "path": "/"}], report["findings"])
            (root / "link.json").symlink_to(root / "array.json")
            self.assertEqual("REDACTION_INPUT_SYMLINK_DENIED", self._cli(root / "link.json")[1]["findings"][0]["code"])
            self.assertEqual("REDACTION_INPUT_NOT_FILE", self._cli(root)[1]["findings"][0]["code"])
            with mock.patch.object(validator, "MAX_BYTES", 1):
                self.assertEqual("REDACTION_INPUT_TOO_LARGE", self._cli(root / "array.json")[1]["findings"][0]["code"])

    def test_cli_argument_conflicts_are_refused(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()):
            for argv in ([], ["--fixtures", "receipt.json"]):
                with self.subTest(argv=argv), self.assertRaises(SystemExit) as raised:
                    validator.main(argv)
                self.assertEqual(2, raised.exception.code)

    def test_schema_finding_flood_is_truncated(self) -> None:
        # A wrong type on every field yields one schema error per field.
        document = {key: 0 for key in self._case("generalized-public")}
        self.assertGreater(len(document), 4)
        with mock.patch.object(validator, "MAX_FINDINGS", 3):
            result = validator.validate_payload(document)
        self.assertEqual("DENY", result.outcome)
        self.assertIn("REDACTION_SCHEMA_FINDINGS_TRUNCATED", [item.code for item in result.findings])
        self.assertLessEqual(len(result.findings), 4)


if __name__ == "__main__":
    unittest.main()
