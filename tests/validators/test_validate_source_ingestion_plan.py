from __future__ import annotations

import json
import socket
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.validate_source_ingestion_plan import (
    FIXTURE_ROOT,
    MAX_FILE_BYTES,
    SCHEMA_PATH,
    _canonical_hash,
    main as validate_main,
    validate_document,
    validate_file,
)


class SourceIngestionPlanTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        self.invalid = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_valid_fixtures_cover_all_modes_and_have_canonical_identity(self) -> None:
        self.assertEqual(len(self.valid), 3)
        modes = set()
        for path in self.valid:
            with self.subTest(path=path.name):
                self.assertEqual(validate_file(path).findings, ())
                payload = json.loads(path.read_text(encoding="utf-8"))
                modes.add(payload["selection"]["mode"])
                self.assertEqual(payload["determinism"]["spec_hash"], _canonical_hash(payload))
                self.assertTrue(payload["plan_id"].endswith(_canonical_hash(payload).split(":", 1)[1]))
        self.assertEqual(modes, {"HTTP_CONDITIONAL", "EVENT_CDC", "SCHEDULED_ETL"})

    def test_invalid_fixtures_match_exact_manifest(self) -> None:
        expected = json.loads((FIXTURE_ROOT / "invalid/expected_findings_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(set(expected), {path.name for path in self.invalid})
        for path in self.invalid:
            with self.subTest(path=path.name):
                actual = sorted({item.code for item in validate_file(path).findings})
                self.assertEqual(actual, sorted(expected[path.name]))

    def test_not_modified_is_no_new_artifact(self) -> None:
        payload = json.loads((FIXTURE_ROOT / "valid/valid_http_conditional.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["lane"]["not_modified_outcome"], "NOT_MODIFIED")
        self.assertFalse(payload["lane"]["not_modified_writes_new_artifact"])

    def test_governance_never_creates_source_or_release_authority(self) -> None:
        for path in self.valid:
            payload = json.loads(path.read_text(encoding="utf-8"))
            governance = payload["governance"]
            self.assertEqual(governance["release_state"], "HOLD")
            for field in ("authority_created", "source_activation_allowed", "network_execution_authorized", "promotion_authorized", "public_use_allowed"):
                self.assertFalse(governance[field])

    def test_mutated_plan_recomputes_identity(self) -> None:
        payload = json.loads((FIXTURE_ROOT / "valid/valid_scheduled_etl.json").read_text(encoding="utf-8"))
        original = payload["determinism"]["spec_hash"]
        payload["lane"]["cost_guardrail"]["max_units"] += 1
        self.assertNotEqual(original, _canonical_hash(payload))

    def test_duplicate_keys_nonfinite_and_oversize_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            duplicate = Path(temp) / "duplicate.json"
            duplicate.write_text('{"schema_version":"x","schema_version":"x"}', encoding="utf-8")
            self.assertEqual(validate_file(duplicate).findings[0].code, "JSON_DUPLICATE_KEY")
            nonfinite = Path(temp) / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            self.assertEqual(validate_file(nonfinite).findings[0].code, "JSON_NONFINITE_NUMBER")
            large = Path(temp) / "large.json"
            large.write_bytes(b" " * (MAX_FILE_BYTES + 1))
            self.assertEqual(validate_file(large).findings[0].code, "FILE_TOO_LARGE")

    def test_cli_fixture_and_single_file_polarity(self) -> None:
        self.assertEqual(validate_main(["--fixtures"]), 0)
        self.assertEqual(validate_main([str(self.valid[0])]), 0)
        self.assertEqual(validate_main([str(self.invalid[0])]), 1)

    def test_validator_has_no_network_dependency(self) -> None:
        def deny(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access is forbidden")
        with (
            mock.patch.object(socket, "socket", side_effect=deny),
            mock.patch.object(socket, "create_connection", side_effect=deny),
            mock.patch.object(socket, "getaddrinfo", side_effect=deny),
        ):
            for path in [*self.valid, *self.invalid]:
                validate_file(path)


if __name__ == "__main__":
    unittest.main()
