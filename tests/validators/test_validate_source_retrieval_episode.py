from __future__ import annotations

import copy
import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONNECTORS_SRC = ROOT / "packages/connectors-core/src"
if str(CONNECTORS_SRC) not in sys.path:
    sys.path.insert(0, str(CONNECTORS_SRC))

from jsonschema import Draft202012Validator

from connectors_core import core as connector_core
from tools.validators.source import validate_source_retrieval_episode as validator


class SourceRetrievalEpisodeTests(unittest.TestCase):
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

    def test_transport_categories_match_connector_model_and_fixtures(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        schema_categories = set(
            schema["$defs"]["transport"]["properties"]["category"]["enum"]
        )
        connector_categories = {
            category.value for category in connector_core.TransportCategory
        }
        manifest = validator.load_fixtures()
        fixture_categories = {
            base["transport"]["category"]
            for base in manifest["bases"].values()
        }
        fixture_categories.update(
            mutation["value"]
            for case in manifest["cases"]
            for mutation in case.get("mutations", [])
            if mutation["path"] == "/transport/category"
        )
        self.assertEqual(connector_categories, schema_categories)
        self.assertEqual(connector_categories, fixture_categories)

    def test_etag_matches_connector_syntax_and_length_bound(self) -> None:
        manifest = validator.load_fixtures()

        def validate_etag(value: str) -> validator.Result:
            document = copy.deepcopy(manifest["bases"]["get_success"])
            document["transport"]["etag"] = value
            document["result"] = validator.recompute_result(document)
            document["spec_hash"], document["episode_id"] = (
                validator.canonical_identity(document)
            )
            return validator.validate_payload(document)

        longest = 'W/"' + ("a" * 512) + '"'
        self.assertEqual(longest, connector_core.ETag.parse(longest).render())
        self.assertEqual("PASS", validate_etag(longest).outcome)

        too_long = '"' + ("a" * 513) + '"'
        with self.assertRaises(connector_core.ConnectorPrimitiveError):
            connector_core.ETag.parse(too_long)
        result = validate_etag(too_long)
        self.assertEqual("DENY", result.outcome)
        self.assertEqual(
            (
                validator.Finding(
                    "RETRIEVAL_SCHEMA_INVALID", "/transport/etag"
                ),
            ),
            result.findings,
        )

    def test_fixture_polarity_is_non_vacuous(self) -> None:
        manifest = validator.load_fixtures()
        outcomes = Counter(
            case["expected_outcome"] for case in manifest["cases"]
        )
        self.assertEqual({"PASS", "ABSTAIN", "DENY", "ERROR"}, set(outcomes))
        self.assertGreaterEqual(outcomes["DENY"], 12)
        self.assertGreaterEqual(outcomes["ABSTAIN"], 4)

    def test_identity_is_deterministic(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        first = validator.canonical_identity(document)
        second = validator.canonical_identity(
            json.loads(json.dumps(document))
        )
        self.assertEqual(first, second)

    def test_failure_episode_never_claims_false_clear(self) -> None:
        manifest = validator.load_fixtures()
        timeout_case = next(
            case for case in manifest["cases"]
            if case["case_id"] == "timeout"
        )
        document = validator.materialize_case(manifest, timeout_case)
        self.assertFalse(document["governance"]["current_data_claimed"])
        self.assertFalse(document["governance"]["no_current_data_claimed"])
        self.assertFalse(document["governance"]["source_artifact_created"])
        self.assertIsNone(document["transport"]["body_digest"])

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
        sentinel = "UNTRUSTED-LOCATOR-VALUE-DO-NOT-ECHO"
        document["redacted_locator"] = (
            "https://official.example.invalid/source?" + sentinel
        )
        digest, identifier = validator.canonical_identity(document)
        document["spec_hash"] = digest
        document["episode_id"] = identifier

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
        self.assertNotIn(sentinel, outputs[0])
        self.assertIn("RETRIEVAL_LOCATOR_UNSAFE", outputs[0])

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
