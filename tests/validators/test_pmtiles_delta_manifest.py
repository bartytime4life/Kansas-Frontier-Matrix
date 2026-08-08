from __future__ import annotations

import json
import socket
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest import mock

from tools.validators._common.public_safe_fixture import MAX_FIXTURE_BYTES
from tools.validators.validate_pmtiles_delta_manifest import (
    FIXTURES_ROOT,
    _quadkey,
    canonical_spec_hash,
    main,
    validate_document,
    validate_manifest_file,
)


class PMTilesDeltaManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid = sorted((FIXTURES_ROOT / "valid").glob("*.json"))
        self.invalid_schema = FIXTURES_ROOT / "invalid/invalid_schema.json"
        self.expected_manifest_path = (
            FIXTURES_ROOT / "expected_findings_manifest.json"
        )
        self.expected_manifest = json.loads(
            self.expected_manifest_path.read_text(encoding="utf-8")
        )
        self.mixed = json.loads(self.valid[0].read_text(encoding="utf-8"))

    @staticmethod
    def _finding_records(path: Path) -> list[dict[str, str]]:
        return [
            {"code": finding.code, "path": finding.path}
            for finding in validate_manifest_file(path)
        ]

    def test_fixture_polarity_and_declared_outcomes(self) -> None:
        self.assertEqual(len(self.valid), 2)
        for path in self.valid:
            self.assertEqual(validate_manifest_file(path), [])
        self.assertEqual(
            {
                finding.code
                for finding in validate_manifest_file(self.invalid_schema)
            },
            {"PMTILES_DELTA_MANIFEST_SCHEMA_INVALID"},
        )
        decisions = {
            json.loads(path.read_text(encoding="utf-8"))["qc"]["decision"]
            for path in self.valid
        }
        self.assertEqual(decisions, {"PASS", "REVIEW"})

    def test_persisted_semantic_invalid_findings_are_exact(self) -> None:
        self.assertEqual(
            self.expected_manifest["schema_version"],
            "kfm.fixture-findings-manifest.v1",
        )
        self.assertEqual(
            self.expected_manifest["scope"],
            "map.pmtiles_delta_manifest",
        )
        cases = self.expected_manifest["cases"]
        actual_names = {
            path.name
            for path in (FIXTURES_ROOT / "invalid").glob("invalid_*.json")
            if path.name != self.invalid_schema.name
        }
        self.assertEqual(set(cases), actual_names)
        for filename, expected in sorted(cases.items()):
            path = FIXTURES_ROOT / "invalid" / filename
            self.assertEqual(self._finding_records(path), expected, filename)

    def test_identity_lineage_and_qc_are_deterministic(self) -> None:
        self.assertEqual(
            self.mixed["spec_hash"],
            canonical_spec_hash(self.mixed),
        )
        self.assertEqual(
            (_quadkey(2, 0, 0), _quadkey(2, 0, 1)),
            ("00", "02"),
        )
        self.assertEqual(
            [tile["change_type"] for tile in self.mixed["tiles"]],
            ["added", "modified", "removed"],
        )
        changed = deepcopy(self.mixed)
        changed["delta_id"] = changed["delta_id"].replace(
            "2026-05-01",
            "2026-05-02",
        )
        changed["spec_hash"] = canonical_spec_hash(changed)
        self.assertIn(
            "PMTILES_DELTA_ID_MISMATCH",
            {finding.code for finding in validate_document(changed)},
        )

    def test_semantic_guards_fail_closed(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []

        threshold_order = deepcopy(self.mixed)
        threshold_order["qc"]["thresholds"]["review_masked_pct"] = 20.0
        cases.append(
            ("PMTILES_DELTA_QC_THRESHOLD_ORDER_INVALID", threshold_order)
        )

        quadkey = deepcopy(self.mixed)
        quadkey["tiles"][0]["quadkey"] = "03"
        cases.append(("PMTILES_DELTA_QUADKEY_MISMATCH", quadkey))

        expected_count = deepcopy(self.mixed)
        expected_count["expected_tile_count"] = 4
        expected_count["qc"]["observed"]["tile_count_deviation_pct"] = 25.0
        expected_count["qc"]["decision"] = "REJECT"
        cases.append(
            ("PMTILES_DELTA_EXPECTED_TILE_COUNT_MISMATCH", expected_count)
        )

        for expected, payload in cases:
            payload["spec_hash"] = canonical_spec_hash(payload)
            self.assertIn(
                expected,
                {finding.code for finding in validate_document(payload)},
            )

    def test_cli_parser_and_no_network_polarity(self) -> None:
        semantic_invalid = [
            FIXTURES_ROOT / "invalid" / filename
            for filename in sorted(self.expected_manifest["cases"])
        ]

        self.assertEqual(main(["--fixtures"]), 0)
        self.assertEqual(main([str(self.valid[0])]), 0)
        self.assertEqual(main([str(self.invalid_schema)]), 1)
        for path in semantic_invalid:
            self.assertEqual(main([str(path)]), 1, path.name)
        self.assertEqual(main([]), 2)

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

        def deny(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access is forbidden")

        with (
            mock.patch.object(socket, "socket", side_effect=deny),
            mock.patch.object(socket, "create_connection", side_effect=deny),
            mock.patch.object(socket, "getaddrinfo", side_effect=deny),
        ):
            for path in [*self.valid, self.invalid_schema, *semantic_invalid]:
                validate_manifest_file(path)


if __name__ == "__main__":
    unittest.main()
