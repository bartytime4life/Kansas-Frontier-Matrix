from __future__ import annotations

import json
import socket
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest import mock

from tools.validators._common.public_safe_fixture import MAX_FIXTURE_BYTES
from tools.validators.validate_huc12_comid_crosswalk_manifest import (
    FIXTURES_ROOT,
    assess_change,
    canonical_spec_hash,
    main,
    validate_document,
    validate_manifest_file,
)


class HUC12COMIDCrosswalkManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_files = sorted((FIXTURES_ROOT / "valid").glob("*.json"))
        self.invalid_files = sorted((FIXTURES_ROOT / "invalid").glob("*.json"))
        self.hold_root = FIXTURES_ROOT / "hold"

    def test_valid_fixtures_pass(self) -> None:
        self.assertEqual(len(self.valid_files), 2)
        for path in self.valid_files:
            with self.subTest(path=path.name):
                self.assertEqual(validate_manifest_file(path), [])

    def test_invalid_fixtures_fail_closed_with_expected_codes(self) -> None:
        expected_codes = {
            "invalid_comid_count.json": {"HUC12_COMID_COUNT_EXCEEDS_ROWS"},
            "invalid_crosswalk_ref_digest_mismatch.json": {
                "HUC12_COMID_CROSSWALK_REF_DIGEST_MISMATCH"
            },
            "invalid_hash_mismatch.json": {"HUC12_COMID_MANIFEST_HASH_MISMATCH"},
            "invalid_huc12.json": {"HUC12_COMID_MANIFEST_SCHEMA_INVALID"},
            "invalid_internal_lifecycle_ref.json": {
                "HUC12_COMID_INTERNAL_LIFECYCLE_REF_DENIED"
            },
            "invalid_placeholder_digest.json": {
                "HUC12_COMID_CROSSWALK_DIGEST_PLACEHOLDER"
            },
            "invalid_time_order.json": {"HUC12_COMID_TIME_ORDER_INVALID"},
        }
        self.assertEqual({path.name for path in self.invalid_files}, set(expected_codes))
        for path in self.invalid_files:
            with self.subTest(path=path.name):
                codes = {finding.code for finding in validate_manifest_file(path)}
                self.assertEqual(codes, expected_codes[path.name])

    def test_spec_hash_and_manifest_identity_are_deterministic(self) -> None:
        payload = json.loads(
            (FIXTURES_ROOT / "valid/valid_initial.json").read_text(encoding="utf-8")
        )
        self.assertEqual(payload["spec_hash"], canonical_spec_hash(payload))
        changed = deepcopy(payload)
        changed["row_count"] += 1
        self.assertNotEqual(payload["spec_hash"], canonical_spec_hash(changed))

        wrong_id = deepcopy(payload)
        wrong_id["manifest_id"] = wrong_id["manifest_id"].replace(
            "2026-04-01", "2026-04-02"
        )
        wrong_id["spec_hash"] = canonical_spec_hash(wrong_id)
        self.assertIn(
            "HUC12_COMID_MANIFEST_ID_MISMATCH",
            {finding.code for finding in validate_document(wrong_id)},
        )

    def test_unchanged_material_inputs_pass_append_only_assessment(self) -> None:
        previous = json.loads(
            (self.hold_root / "previous.json").read_text(encoding="utf-8")
        )
        candidate = json.loads(
            (FIXTURES_ROOT / "valid/valid_continuation_same_inputs.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(assess_change(previous, candidate), ("PASS", []))

    def test_nhd_and_crosswalk_changes_are_review_holds(self) -> None:
        previous = json.loads(
            (self.hold_root / "previous.json").read_text(encoding="utf-8")
        )
        cases = {
            "candidate_nhd_changed.json": "HUC12_COMID_NHD_SNAPSHOT_CHANGED",
            "candidate_crosswalk_changed.json": "HUC12_COMID_CROSSWALK_DIGEST_CHANGED",
        }
        for name, expected_code in cases.items():
            with self.subTest(name=name):
                candidate = json.loads(
                    (self.hold_root / name).read_text(encoding="utf-8")
                )
                status, findings = assess_change(previous, candidate)
                self.assertEqual(status, "HOLD")
                self.assertEqual({finding.code for finding in findings}, {expected_code})

    def test_overlap_and_scope_change_are_denied(self) -> None:
        previous = json.loads(
            (self.hold_root / "previous.json").read_text(encoding="utf-8")
        )
        overlap = json.loads(
            (self.hold_root / "candidate_overlap.json").read_text(encoding="utf-8")
        )
        status, findings = assess_change(previous, overlap)
        self.assertEqual(status, "DENY")
        self.assertIn(
            "HUC12_COMID_TIME_WINDOW_OVERLAP",
            {finding.code for finding in findings},
        )

        other_huc = deepcopy(
            json.loads(
                (FIXTURES_ROOT / "valid/valid_continuation_same_inputs.json").read_text(
                    encoding="utf-8"
                )
            )
        )
        other_huc["huc12"] = "102600150102"
        other_huc["manifest_id"] = other_huc["manifest_id"].replace(
            "102600150101", "102600150102"
        )
        other_huc["spec_hash"] = canonical_spec_hash(other_huc)
        status, findings = assess_change(previous, other_huc)
        self.assertEqual(status, "DENY")
        self.assertIn(
            "HUC12_COMID_CHANGE_SCOPE_MISMATCH",
            {finding.code for finding in findings},
        )

    def test_invalid_candidate_cannot_be_masked_as_hold(self) -> None:
        previous = json.loads(
            (self.hold_root / "previous.json").read_text(encoding="utf-8")
        )
        candidate = json.loads(
            (self.hold_root / "candidate_crosswalk_changed.json").read_text(
                encoding="utf-8"
            )
        )
        candidate["spec_hash"] = "sha256:" + ("9" * 64)
        status, findings = assess_change(previous, candidate)
        self.assertEqual(status, "DENY")
        self.assertIn(
            "HUC12_COMID_MANIFEST_HASH_MISMATCH",
            {finding.code for finding in findings},
        )

    def test_cli_exit_codes_distinguish_pass_hold_deny_and_usage(self) -> None:
        previous = self.hold_root / "previous.json"
        valid = FIXTURES_ROOT / "valid/valid_continuation_same_inputs.json"
        hold = self.hold_root / "candidate_nhd_changed.json"
        invalid = FIXTURES_ROOT / "invalid/invalid_hash_mismatch.json"
        self.assertEqual(main(["--fixtures"]), 0)
        self.assertEqual(main([str(valid)]), 0)
        self.assertEqual(main([str(valid), "--previous", str(previous)]), 0)
        self.assertEqual(main([str(hold), "--previous", str(previous)]), 3)
        self.assertEqual(main([str(invalid), "--previous", str(previous)]), 1)
        self.assertEqual(main([]), 2)

    def test_duplicate_json_keys_and_oversize_inputs_fail_before_semantics(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            duplicate = Path(temp_dir) / "duplicate.json"
            duplicate.write_text(
                '{"schema_version":"a","schema_version":"b"}',
                encoding="utf-8",
            )
            self.assertEqual(
                validate_manifest_file(duplicate)[0].code,
                "FIXTURE_JSON_INVALID",
            )

            oversized = Path(temp_dir) / "oversized.json"
            oversized.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(
                validate_manifest_file(oversized)[0].code,
                "FIXTURE_TOO_LARGE",
            )

    def test_validator_has_no_network_dependency(self) -> None:
        def deny(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access is forbidden")

        with (
            mock.patch.object(socket, "socket", side_effect=deny),
            mock.patch.object(socket, "create_connection", side_effect=deny),
            mock.patch.object(socket, "getaddrinfo", side_effect=deny),
        ):
            for path in self.valid_files + self.invalid_files:
                validate_manifest_file(path)


if __name__ == "__main__":
    unittest.main()
