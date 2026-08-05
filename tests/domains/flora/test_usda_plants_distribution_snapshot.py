from __future__ import annotations

import json
import socket
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest import mock

from tools.ingest.usda_plants.normalize_distribution_snapshot import (
    NormalizationError,
    build_snapshot,
    main as normalize_main,
    write_snapshot,
)
from tools.validators._common.public_safe_fixture import MAX_FIXTURE_BYTES
from tools.validators.domains.flora.validate_usda_plants_distribution_snapshot import (
    FIXTURES_ROOT,
    canonical_spec_hash,
    main as validate_main,
    validate_document,
    validate_snapshot_file,
)


EVIDENCE_REF = (
    "kfm://evidence/flora/usda-plants/synthetic-2026-04-30@sha256:"
    + ("e" * 64)
)


class USDAPlantsDistributionSnapshotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.input_root = FIXTURES_ROOT / "input"
        self.valid_path = FIXTURES_ROOT / "valid/valid_snapshot.json"
        self.invalid_files = sorted((FIXTURES_ROOT / "invalid").glob("*.json"))

    def test_valid_fixture_passes_and_hash_is_canonical(self) -> None:
        self.assertEqual(validate_snapshot_file(self.valid_path), [])
        payload = json.loads(self.valid_path.read_text(encoding="utf-8"))
        self.assertEqual(payload["spec_hash"], canonical_spec_hash(payload))

    def test_invalid_fixtures_fail_with_stable_reason_codes(self) -> None:
        expected = {
            "coverage_incomplete.json": {
                "USDA_PLANTS_DISTRIBUTION_COVERAGE_INCOMPLETE"
            },
            "distribution_order_invalid.json": {
                "USDA_PLANTS_DISTRIBUTION_ORDER_INVALID"
            },
            "duplicate_source_row.json": {
                "USDA_PLANTS_SOURCE_ROW_DUPLICATE"
            },
            "exact_geometry_field.json": {
                "USDA_PLANTS_DISTRIBUTION_SCHEMA_INVALID",
                "USDA_PLANTS_EXACT_GEOMETRY_FIELD_DENIED",
            },
            "hash_mismatch.json": {"USDA_PLANTS_SPEC_HASH_MISMATCH"},
            "internal_lifecycle_ref.json": {
                "USDA_PLANTS_INTERNAL_LIFECYCLE_REF_DENIED"
            },
            "missing_row_as_absence.json": {
                "USDA_PLANTS_DISTRIBUTION_INTERPRETATION_MISMATCH",
                "USDA_PLANTS_DISTRIBUTION_STATE_SOURCE_MISMATCH",
                "USDA_PLANTS_EXPLICIT_ABSENCE_ROW_REQUIRED",
                "USDA_PLANTS_SOURCE_ROW_PRESENCE_MISMATCH",
            },
            "release_hold_removed.json": {
                "USDA_PLANTS_DISTRIBUTION_SCHEMA_INVALID"
            },
            "scientific_author_missing.json": {
                "USDA_PLANTS_SCIENTIFIC_AUTHORSHIP_MISSING"
            },
        }
        self.assertEqual({path.name for path in self.invalid_files}, set(expected))
        for path in self.invalid_files:
            with self.subTest(path=path.name):
                codes = {
                    finding.code for finding in validate_snapshot_file(path)
                }
                self.assertEqual(codes, expected[path.name])

    def test_normalizer_rebuilds_fixture_and_preserves_no_row_as_no_claim(self) -> None:
        candidate = build_snapshot(
            taxa_path=self.input_root / "taxa.csv",
            counties_path=self.input_root / "counties.csv",
            distribution_path=self.input_root / "distribution.csv",
            snapshot_date="2026-04-30",
            evidence_ref=EVIDENCE_REF,
        )
        expected = json.loads(self.valid_path.read_text(encoding="utf-8"))
        self.assertEqual(candidate, expected)

        missing_pair = next(
            state
            for state in candidate["distribution_states"]
            if state["plants_symbol"] == "ASCA11"
            and state["county_fips"] == "20053"
        )
        self.assertEqual(missing_pair["state"], "not_reported")
        self.assertEqual(missing_pair["interpretation"], "no_claim")
        self.assertFalse(missing_pair["source_row_present"])
        self.assertEqual(candidate["summary"]["not_reported"], 1)

        with tempfile.TemporaryDirectory() as temp_dir:
            first = Path(temp_dir) / "first.json"
            second = Path(temp_dir) / "second.json"
            write_snapshot(candidate, first)
            write_snapshot(candidate, second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(first.read_bytes(), self.valid_path.read_bytes())

    def test_normalizer_rejects_duplicate_and_unknown_source_rows(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            taxa = root / "taxa.csv"
            counties = root / "counties.csv"
            distribution = root / "distribution.csv"
            taxa.write_text(
                (self.input_root / "taxa.csv").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            counties.write_text(
                (self.input_root / "counties.csv").read_text(encoding="utf-8"),
                encoding="utf-8",
            )

            distribution.write_text(
                "plants_symbol,county_fips,presence\n"
                "ACMI2,20041,present\n"
                "ACMI2,20041,present\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                NormalizationError, "DISTRIBUTION_PAIR_DUPLICATE"
            ):
                build_snapshot(
                    taxa_path=taxa,
                    counties_path=counties,
                    distribution_path=distribution,
                    snapshot_date="2026-04-30",
                    evidence_ref=EVIDENCE_REF,
                )

            distribution.write_text(
                "plants_symbol,county_fips,presence\n"
                "UNKNOWN,20041,present\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                NormalizationError, "DISTRIBUTION_TAXON_UNKNOWN"
            ):
                build_snapshot(
                    taxa_path=taxa,
                    counties_path=counties,
                    distribution_path=distribution,
                    snapshot_date="2026-04-30",
                    evidence_ref=EVIDENCE_REF,
                )

    def test_cross_product_and_summary_recompute_fail_closed(self) -> None:
        payload = json.loads(self.valid_path.read_text(encoding="utf-8"))
        payload["distribution_states"] = payload["distribution_states"][:-1]
        payload["summary"]["cell_count"] = 3
        payload["summary"]["not_reported"] = 0
        payload["spec_hash"] = canonical_spec_hash(payload)
        codes = {finding.code for finding in validate_document(payload)}
        self.assertEqual(
            codes, {"USDA_PLANTS_DISTRIBUTION_COVERAGE_INCOMPLETE"}
        )

        payload = json.loads(self.valid_path.read_text(encoding="utf-8"))
        payload["summary"]["reported_present"] = 999
        payload["spec_hash"] = canonical_spec_hash(payload)
        codes = {finding.code for finding in validate_document(payload)}
        self.assertEqual(codes, {"USDA_PLANTS_SUMMARY_MISMATCH"})

    def test_duplicate_keys_and_oversize_inputs_fail_before_semantics(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            duplicate = Path(temp_dir) / "duplicate.json"
            duplicate.write_text(
                '{"schema_version":"x","schema_version":"x"}',
                encoding="utf-8",
            )
            self.assertEqual(
                validate_snapshot_file(duplicate)[0].code,
                "FIXTURE_JSON_INVALID",
            )

            oversized = Path(temp_dir) / "oversized.json"
            oversized.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(
                validate_snapshot_file(oversized)[0].code,
                "FIXTURE_TOO_LARGE",
            )

    def test_cli_fixture_and_single_file_polarity(self) -> None:
        self.assertEqual(validate_main(["--fixtures"]), 0)
        self.assertEqual(validate_main([str(self.valid_path)]), 0)
        self.assertEqual(
            validate_main(
                [str(FIXTURES_ROOT / "invalid/hash_mismatch.json")]
            ),
            1,
        )
        self.assertEqual(validate_main([]), 2)

        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "snapshot.json"
            self.assertEqual(
                normalize_main(
                    [
                        "--taxa",
                        str(self.input_root / "taxa.csv"),
                        "--counties",
                        str(self.input_root / "counties.csv"),
                        "--distribution",
                        str(self.input_root / "distribution.csv"),
                        "--snapshot-date",
                        "2026-04-30",
                        "--evidence-ref",
                        EVIDENCE_REF,
                        "--out",
                        str(output),
                    ]
                ),
                0,
            )
            self.assertEqual(output.read_bytes(), self.valid_path.read_bytes())

    def test_normalizer_and_validator_have_no_network_dependency(self) -> None:
        def deny(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access is forbidden")

        with (
            mock.patch.object(socket, "socket", side_effect=deny),
            mock.patch.object(socket, "create_connection", side_effect=deny),
            mock.patch.object(socket, "getaddrinfo", side_effect=deny),
        ):
            candidate = build_snapshot(
                taxa_path=self.input_root / "taxa.csv",
                counties_path=self.input_root / "counties.csv",
                distribution_path=self.input_root / "distribution.csv",
                snapshot_date="2026-04-30",
                evidence_ref=EVIDENCE_REF,
            )
            self.assertEqual(validate_document(candidate), [])
            for path in [self.valid_path, *self.invalid_files]:
                validate_snapshot_file(path)


if __name__ == "__main__":
    unittest.main()
