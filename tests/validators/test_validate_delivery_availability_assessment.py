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

from tools.validators.source import validate_delivery_availability_assessment as validator

ROOT = Path(__file__).resolve().parents[2]


class DeliveryAvailabilityAssessmentTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(
                    validator.materialize_case(manifest, case)
                )
                actual = [
                    {"code": finding.code, "path": finding.path}
                    for finding in result.findings
                ]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_and_delivery_states_are_non_vacuous(self) -> None:
        manifest = validator.load_fixtures()
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"PASS", "ABSTAIN", "DENY", "ERROR"}, set(outcomes))
        self.assertGreaterEqual(outcomes["DENY"], 10)
        valid_states = {
            validator.materialize_case(manifest, case)["decision"]["state"]
            for case in manifest["cases"][:8]
        }
        self.assertEqual(
            {
                "ON_TIME",
                "EXPECTED_LAG",
                "LATE",
                "STALE",
                "MISSING",
                "SOURCE_OUTAGE",
                "SUPERSEDED",
                "ERROR",
            },
            valid_states,
        )

    def test_expected_lag_is_not_lateness_or_staleness(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][1])
        self.assertEqual("EXPECTED_LAG", document["decision"]["state"])
        self.assertEqual("UNAVAILABLE", document["decision"]["freshness_state"])
        self.assertEqual(10800, document["expectation"]["observation_cadence_seconds"])
        self.assertEqual(10800, document["expectation"]["product_cadence_seconds"])
        self.assertEqual(
            {"minimum_seconds": 3600, "maximum_seconds": 7200},
            document["expectation"]["delivery_window_seconds"],
        )

    def test_identity_is_content_addressed_and_replay_stable(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        first = validator.canonical_identity(document)
        second = validator.canonical_identity(json.loads(json.dumps(document)))
        self.assertEqual(first, second)
        changed = json.loads(json.dumps(document))
        changed["source_descriptor_version"] = "v4"
        self.assertNotEqual(first, validator.canonical_identity(changed))

    def test_learned_latency_cannot_mutate_expectation_or_authority(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][2])
        self.assertEqual(10800, document["learned_observation"]["observed_delivery_latency_seconds"])
        self.assertEqual(
            "REVIEW_REQUIRED",
            document["learned_observation"]["use_for_expectation_update"],
        )
        self.assertFalse(document["learned_observation"]["expectation_mutated"])
        self.assertEqual("FIXTURE_ONLY", document["governance"]["execution_mode"])
        self.assertFalse(
            any(
                value
                for key, value in document["governance"].items()
                if key != "execution_mode"
            )
        )

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
        sentinel = "do-not-echo-source-value"
        document["source_id"] = sentinel
        result = validator.validate_payload(document)
        rendered = validator.serialize(Path("candidate.json"), result)
        self.assertNotIn(sentinel, rendered)
        self.assertNotIn("synthetic.atmos.product", rendered)

    def test_cli_fixture_replay_and_parser_errors_are_deterministic(self) -> None:
        command = [sys.executable, str(Path(validator.__file__)), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn('"cases":20', first.stdout)
        self.assertIn('"suite_match":true', first.stdout)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            invalid = root / "invalid.json"
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
                (duplicate, "DELIVERY_JSON_DUPLICATE_KEY"),
                (nonfinite, "DELIVERY_JSON_NONFINITE_NUMBER"),
                (link, "DELIVERY_INPUT_SYMLINK_DENIED"),
                (oversized, "DELIVERY_INPUT_TOO_LARGE"),
            ):
                with self.subTest(path=path.name):
                    value, findings = validator._read(path)
                    self.assertIsNone(value)
                    self.assertEqual(code, findings[0].code)


if __name__ == "__main__":
    unittest.main()
