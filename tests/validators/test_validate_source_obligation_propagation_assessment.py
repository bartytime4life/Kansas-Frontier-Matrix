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

from jsonschema import Draft202012Validator

from tools.validators.source import (
    validate_source_obligation_propagation_assessment as validator,
)

ROOT = Path(__file__).resolve().parents[2]


class SourceObligationPropagationAssessmentTests(unittest.TestCase):
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
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_is_non_vacuous(self) -> None:
        manifest = validator.load_fixtures()
        outcomes = Counter(
            case["expected_outcome"] for case in manifest["cases"]
        )
        self.assertEqual({"PASS", "ABSTAIN", "DENY", "ERROR"}, set(outcomes))
        self.assertGreaterEqual(outcomes["PASS"], 3)
        self.assertGreaterEqual(outcomes["DENY"], 16)

    def test_identity_is_deterministic(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        first = validator.canonical_identity(document)
        second = validator.canonical_identity(
            json.loads(json.dumps(document))
        )
        self.assertEqual(first, second)

    def test_complete_chain_preserves_declared_obligations(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        obligations = document["obligations"]
        required = set(obligations["required_notices"])
        for carrier in document["carrier_chain"]:
            self.assertEqual(
                obligations["attribution_ref"], carrier["attribution_ref"]
            )
            self.assertEqual(obligations["terms_ref"], carrier["terms_ref"])
            self.assertTrue(required.issubset(set(carrier["notices"])))
        self.assertFalse(document["governance"]["export_executed"])
        self.assertFalse(document["governance"]["publication_authorized"])

    def test_governance_non_effects_are_false(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
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

    def test_validator_has_no_network_client_import(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in (
            "requests",
            "urllib.request",
            "httpx",
            "aiohttp",
            "socket.",
        ):
            self.assertNotIn(token, source)

    def test_diagnostics_are_deterministic_and_do_not_echo_values(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        sentinel = "UNTRUSTED-ATTRIBUTION-VALUE-DO-NOT-ECHO"
        document["carrier_chain"][1]["attribution_ref"] = (
            "kfm:attribution:" + sentinel.lower()
        )
        document["result"] = validator.recompute_result(document)
        digest, identifier = validator.canonical_identity(document)
        document["spec_hash"] = digest
        document["assessment_id"] = identifier

        outputs: list[str] = []
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(document), encoding="utf-8")
            for _ in range(2):
                stream = io.StringIO()
                with contextlib.redirect_stdout(stream):
                    code = validator.main([str(path)])
                self.assertEqual(1, code)
                outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertNotIn(sentinel.lower(), outputs[0])
        self.assertIn("ATTRIBUTION_MISSING", outputs[0])

    def test_fixture_cli(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(Path(validator.__file__)),
                "--fixtures",
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn('"suite_match":true', completed.stdout)

    def test_invalid_json_cli_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text("{", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(path)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(2, completed.returncode)
        self.assertIn('"outcome":"ERROR"', completed.stdout)


if __name__ == "__main__":
    unittest.main()
