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
        self.invalid = FIXTURES_ROOT / "invalid/invalid_schema.json"
        self.mixed = json.loads(self.valid[0].read_text(encoding="utf-8"))

    def test_fixture_polarity_and_declared_outcomes(self) -> None:
        self.assertEqual(len(self.valid), 2)
        for path in self.valid:
            self.assertEqual(validate_manifest_file(path), [])
        self.assertEqual(
            {finding.code for finding in validate_manifest_file(self.invalid)},
            {"PMTILES_DELTA_MANIFEST_SCHEMA_INVALID"},
        )
        decisions = {
            json.loads(path.read_text(encoding="utf-8"))["qc"]["decision"]
            for path in self.valid
        }
        self.assertEqual(decisions, {"PASS", "REVIEW"})

    def test_identity_lineage_and_qc_are_deterministic(self) -> None:
        self.assertEqual(self.mixed["spec_hash"], canonical_spec_hash(self.mixed))
        self.assertEqual((_quadkey(2, 0, 0), _quadkey(2, 0, 1)), ("00", "02"))
        self.assertEqual(
            [tile["change_type"] for tile in self.mixed["tiles"]],
            ["added", "modified", "removed"],
        )
        changed = deepcopy(self.mixed)
        changed["delta_id"] = changed["delta_id"].replace("2026-05-01", "2026-05-02")
        changed["spec_hash"] = canonical_spec_hash(changed)
        self.assertIn(
            "PMTILES_DELTA_ID_MISMATCH",
            {finding.code for finding in validate_document(changed)},
        )

    def test_semantic_guards_fail_closed(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        artifact = deepcopy(self.mixed)
        artifact["base_archive"]["artifact_ref"] = artifact["base_archive"]["artifact_ref"].replace("1" * 64, "f" * 64)
        cases.append(("PMTILES_DELTA_ARTIFACT_REF_DIGEST_MISMATCH", artifact))
        modified = deepcopy(self.mixed)
        modified["tiles"][1]["prior_digest"] = None
        cases.append(("PMTILES_DELTA_MODIFIED_LINEAGE_INVALID", modified))
        internal = deepcopy(self.mixed)
        internal["tiles"][0]["run_receipt_ref"] = internal["tiles"][0]["run_receipt_ref"].replace("kfm://receipt/run/", "kfm://data/work/")
        cases.append(("PMTILES_DELTA_INTERNAL_LIFECYCLE_REF_DENIED", internal))
        qc = deepcopy(self.mixed)
        qc["qc"]["observed"]["average_tile_bytes"] = 1.0
        cases.append(("PMTILES_DELTA_QC_AVERAGE_BYTES_MISMATCH", qc))
        coordinate = deepcopy(self.mixed)
        coordinate["tiles"][0].update({"x": 4, "tile_id": "2/4/0", "quadkey": _quadkey(2, 4, 0)})
        cases.append(("PMTILES_DELTA_TILE_COORDINATE_INVALID", coordinate))
        duplicate = deepcopy(self.mixed)
        duplicate["tiles"][1].update({key: duplicate["tiles"][0][key] for key in ("z", "x", "y", "tile_id", "quadkey")})
        cases.append(("PMTILES_DELTA_TILE_DUPLICATE", duplicate))
        for expected, payload in cases:
            payload["spec_hash"] = canonical_spec_hash(payload)
            self.assertIn(expected, {finding.code for finding in validate_document(payload)})

    def test_cli_parser_and_no_network_polarity(self) -> None:
        self.assertEqual(main(["--fixtures"]), 0)
        self.assertEqual(main([str(self.valid[0])]), 0)
        self.assertEqual(main([str(self.invalid)]), 1)
        self.assertEqual(main([]), 2)
        with tempfile.TemporaryDirectory() as temp_dir:
            duplicate = Path(temp_dir) / "duplicate.json"
            duplicate.write_text('{"schema_version":"a","schema_version":"b"}', encoding="utf-8")
            self.assertEqual(validate_manifest_file(duplicate)[0].code, "FIXTURE_JSON_INVALID")
            oversized = Path(temp_dir) / "oversized.json"
            oversized.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(validate_manifest_file(oversized)[0].code, "FIXTURE_TOO_LARGE")
        def deny(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access is forbidden")
        with (
            mock.patch.object(socket, "socket", side_effect=deny),
            mock.patch.object(socket, "create_connection", side_effect=deny),
            mock.patch.object(socket, "getaddrinfo", side_effect=deny),
        ):
            for path in [*self.valid, self.invalid]:
                validate_manifest_file(path)


if __name__ == "__main__":
    unittest.main()
