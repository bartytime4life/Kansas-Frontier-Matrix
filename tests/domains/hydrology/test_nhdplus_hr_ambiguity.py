from __future__ import annotations

import json
import socket
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest import mock

from tools.validators._common.public_safe_fixture import MAX_FIXTURE_BYTES
from tools.validators.domains.hydrology.validate_nhdplus_waterbody_crosswalk import (
    FIXTURES_ROOT,
    canonical_spec_hash,
    main,
    validate_crosswalk_file,
    validate_document,
)


class NHDPlusWaterbodyCrosswalkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_files = sorted((FIXTURES_ROOT / "valid").glob("*.json"))
        self.invalid_files = sorted((FIXTURES_ROOT / "invalid").glob("*.json"))

    def test_valid_fixtures_pass(self) -> None:
        self.assertGreaterEqual(len(self.valid_files), 2)
        for path in self.valid_files:
            with self.subTest(path=path.name):
                self.assertEqual(validate_crosswalk_file(path), [])

    def test_invalid_fixtures_fail_closed(self) -> None:
        expected_codes = {
            "collapsed_ambiguity.json": {
                "NHDPLUS_WATERBODY_CROSSWALK_AMBIGUITY_COLLAPSED",
                "NHDPLUS_WATERBODY_CROSSWALK_CARDINALITY_MISMATCH",
            },
            "duplicate_pair.json": {
                "NHDPLUS_WATERBODY_CROSSWALK_CARDINALITY_MISMATCH",
                "NHDPLUS_WATERBODY_CROSSWALK_DUPLICATE_PAIR",
            },
            "geometry_equality_claim.json": {
                "NHDPLUS_WATERBODY_CROSSWALK_SCHEMA_INVALID",
            },
            "hash_mismatch.json": {
                "NHDPLUS_WATERBODY_CROSSWALK_HASH_MISMATCH",
            },
            "overlap_exceeds_source_area.json": {
                "NHDPLUS_WATERBODY_CROSSWALK_OVERLAP_AREA_INVALID",
            },
            "wrong_feature_scope.json": {
                "NHDPLUS_WATERBODY_CROSSWALK_SCHEMA_INVALID",
            },
        }
        self.assertEqual({path.name for path in self.invalid_files}, set(expected_codes))
        for path in self.invalid_files:
            with self.subTest(path=path.name):
                codes = {finding.code for finding in validate_crosswalk_file(path)}
                self.assertEqual(codes, expected_codes[path.name])

    def test_many_to_many_fixture_preserves_cardinality_and_abstains(self) -> None:
        payload = json.loads(
            (FIXTURES_ROOT / "valid/many_to_many.json").read_text(encoding="utf-8")
        )
        observed = {
            (
                record["nhdplus_hr_permanent_identifier"],
                record["nhdplus_v2_comid"],
            ): (record["relationship_type"], record["outcome"])
            for record in payload["records"]
        }
        self.assertEqual(
            observed,
            {
                ("synthetic:nhdhr-waterbody:a", 91001): ("complex", "ABSTAIN"),
                ("synthetic:nhdhr-waterbody:a", 91002): ("split", "ABSTAIN"),
                ("synthetic:nhdhr-waterbody:b", 91001): ("merge", "ABSTAIN"),
            },
        )

    def test_hash_and_record_order_are_deterministic(self) -> None:
        payload = json.loads(self.valid_files[0].read_text(encoding="utf-8"))
        self.assertEqual(payload["spec_hash"], canonical_spec_hash(payload))
        reordered = json.loads(
            (FIXTURES_ROOT / "valid/many_to_many.json").read_text(encoding="utf-8")
        )
        reordered["records"] = list(reversed(reordered["records"]))
        reordered["spec_hash"] = canonical_spec_hash(reordered)
        codes = {finding.code for finding in validate_document(reordered)}
        self.assertIn("NHDPLUS_WATERBODY_CROSSWALK_ORDER_INVALID", codes)

    def test_record_limit_is_closed(self) -> None:
        payload = json.loads(
            (FIXTURES_ROOT / "valid/exact.json").read_text(encoding="utf-8")
        )
        payload["records"] = [deepcopy(payload["records"][0]) for _ in range(513)]
        payload["spec_hash"] = canonical_spec_hash(payload)
        codes = {finding.code for finding in validate_document(payload)}
        self.assertIn("NHDPLUS_WATERBODY_CROSSWALK_SCHEMA_INVALID", codes)

    def test_duplicate_json_keys_and_oversize_inputs_fail_before_semantics(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            duplicate = Path(temp_dir) / "duplicate.json"
            duplicate.write_text('{"schema_version":"1.0.0","schema_version":"1.0.0"}', encoding="utf-8")
            self.assertEqual(validate_crosswalk_file(duplicate)[0].code, "FIXTURE_JSON_INVALID")

            oversized = Path(temp_dir) / "oversized.json"
            oversized.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(validate_crosswalk_file(oversized)[0].code, "FIXTURE_TOO_LARGE")

    def test_cli_fixture_suite_and_single_file_polarity(self) -> None:
        self.assertEqual(main(["--fixtures"]), 0)
        self.assertEqual(main([str(FIXTURES_ROOT / "valid/exact.json")]), 0)
        self.assertEqual(main([str(FIXTURES_ROOT / "invalid/hash_mismatch.json")]), 1)
        self.assertEqual(main([]), 2)

    def test_validator_has_no_network_dependency(self) -> None:
        def deny(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access is forbidden")

        with (
            mock.patch.object(socket, "socket", side_effect=deny),
            mock.patch.object(socket, "create_connection", side_effect=deny),
            mock.patch.object(socket, "getaddrinfo", side_effect=deny),
        ):
            for path in self.valid_files + self.invalid_files:
                validate_crosswalk_file(path)


if __name__ == "__main__":
    unittest.main()
