from __future__ import annotations

import gzip
import hashlib
import json
import math
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Callable

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_DIR = REPO_ROOT / "tools/validators/pmtiles"
sys.path.insert(0, str(VALIDATOR_DIR))

from validate_attestation_bundle import HOLDS, render_result, validate_bundle
from validate_header import HeaderValidationError, inspect_archive
from verify_merkle import MerkleValidationError, inspect_index, merkle_root

FIXTURE_ROOT = REPO_ROOT / "fixtures/pmtiles/attestation"
SPEC_HASH = "sha256:" + hashlib.sha256(b"kfm-test-build-spec").hexdigest()
OTHER_HASH = "sha256:" + hashlib.sha256(b"different-value").hexdigest()
ROOT_DIRECTORY = b"\x01\x00\x01\x01\x01"


def _write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _independent_merkle_root(leaves: list[str], arity: int) -> str:
    if not leaves:
        return "sha256:" + hashlib.sha256(b"").hexdigest()
    level = [bytes.fromhex(value.split(":", 1)[1]) for value in leaves]
    while len(level) > 1:
        next_level: list[bytes] = []
        for start in range(0, len(level), arity):
            next_level.append(
                hashlib.sha256(b"".join(level[start:start + arity])).digest()
            )
        level = next_level
    return "sha256:" + level[0].hex()


def _archive_payload(
    *,
    metadata_bytes: bytes | None = None,
    internal_compression: int = 1,
    tile_bytes: bytes = b"\x01",
) -> bytes:
    metadata_bytes = metadata_bytes or json.dumps(
        {"name": "synthetic-kfm-fixture", "spec_hash": SPEC_HASH},
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    root_offset = 127
    metadata_offset = root_offset + len(ROOT_DIRECTORY)
    tile_offset = metadata_offset + len(metadata_bytes)
    header = bytearray(127)
    header[:7] = b"PMTiles"
    header[7] = 3
    # Independent fixture layout: eleven uint64 values followed by the byte and
    # signed-coordinate fields defined by PMTiles v3.
    struct.pack_into(
        "<11Q",
        header,
        8,
        root_offset,
        len(ROOT_DIRECTORY),
        metadata_offset,
        len(metadata_bytes),
        0,
        0,
        tile_offset,
        len(tile_bytes),
        1,
        1,
        1,
    )
    header[96:102] = bytes((1, internal_compression, 1, 0, 0, 0))
    struct.pack_into("<i", header, 102, -1_020_000_000)
    struct.pack_into("<i", header, 106, 370_000_000)
    struct.pack_into("<i", header, 110, -940_000_000)
    struct.pack_into("<i", header, 114, 400_000_000)
    header[118] = 0
    struct.pack_into("<i", header, 119, -980_000_000)
    struct.pack_into("<i", header, 123, 385_000_000)
    return bytes(header) + ROOT_DIRECTORY + metadata_bytes + tile_bytes


def _build_bundle(directory: Path, *, chunk_bytes: int = 64) -> dict[str, object]:
    archive = directory / "tiles.pmtiles"
    archive.write_bytes(_archive_payload(tile_bytes=b"synthetic-tile-content"))
    archive_bytes = archive.read_bytes()
    leaves = [
        "sha256:" + hashlib.sha256(archive_bytes[start:start + chunk_bytes]).hexdigest()
        for start in range(0, len(archive_bytes), chunk_bytes)
    ]
    archive_digest = "sha256:" + hashlib.sha256(archive_bytes).hexdigest()
    index = {
        "schema_version": "kfm.pmidx.v1",
        "spec_hash": SPEC_HASH,
        "pmtiles_sha256": archive_digest,
        "merkle": {
            "arity": 2,
            "chunk_bytes": chunk_bytes,
            "root": _independent_merkle_root(leaves, 2),
            "leaves": leaves,
        },
        "ranges": [{"tile_id": "synthetic", "offset": 0, "length": 10, "leaf": 0}],
    }
    pmsig = {
        "schema_version": "kfm.pmsig.v1",
        "subject": {
            "pmtiles_sha256": archive_digest,
            "pmidx_merkle_root": index["merkle"]["root"],
            "spec_hash": SPEC_HASH,
        },
        "key_id": "TEST_ONLY_UNAPPROVED_KEY",
        "signature": "DEVELOPMENT_PLACEHOLDER_NOT_A_VALID_COSE_SIGNATURE",
    }
    receipt = {
        "schema_version": "kfm.runreceipt.pmtiles.v1",
        "type": "https://slsa.dev/provenance/v1",
        "subject": [
            {
                "name": archive.name,
                "digest": {"sha256": archive_digest.removeprefix("sha256:")},
            }
        ],
        "predicate": {
            "buildDefinition": {
                "buildType": "kfm/pmtiles/build@v1",
                "externalParameters": {"spec_hash": SPEC_HASH},
            },
            "runDetails": {"builder": {"id": "kfm-test-builder"}},
        },
    }
    _write_json(Path(str(archive) + ".pmidx"), index)
    _write_json(Path(str(archive) + ".pmsig"), pmsig)
    _write_json(Path(str(archive) + ".runreceipt.json"), receipt)
    return {
        "archive": archive,
        "archive_bytes": archive_bytes,
        "index": index,
        "pmsig": pmsig,
        "receipt": receipt,
    }


def _apply_mutation(bundle: dict[str, object], mutation: str) -> None:
    archive = bundle["archive"]
    assert isinstance(archive, Path)
    index = bundle["index"]
    pmsig = bundle["pmsig"]
    receipt = bundle["receipt"]
    assert isinstance(index, dict) and isinstance(pmsig, dict) and isinstance(receipt, dict)

    if mutation == "none":
        return
    if mutation == "pmidx_spec_hash_mismatch":
        index["spec_hash"] = OTHER_HASH
        _write_json(Path(str(archive) + ".pmidx"), index)
    elif mutation == "pmidx_leaf_digest_mismatch":
        index["merkle"]["leaves"][1] = OTHER_HASH
        _write_json(Path(str(archive) + ".pmidx"), index)
    elif mutation == "pmidx_leaf_count_mismatch":
        index["merkle"]["leaves"].pop()
        _write_json(Path(str(archive) + ".pmidx"), index)
    elif mutation == "pmidx_merkle_root_mismatch":
        index["merkle"]["root"] = OTHER_HASH
        _write_json(Path(str(archive) + ".pmidx"), index)
    elif mutation == "pmidx_range_out_of_bounds":
        index["ranges"][0].update(
            {"offset": len(bundle["archive_bytes"]) - 1, "length": 2}
        )
        _write_json(Path(str(archive) + ".pmidx"), index)
    elif mutation == "pmsig_spec_hash_mismatch":
        pmsig["subject"]["spec_hash"] = OTHER_HASH
        _write_json(Path(str(archive) + ".pmsig"), pmsig)
    elif mutation == "pmsig_archive_digest_mismatch":
        pmsig["subject"]["pmtiles_sha256"] = OTHER_HASH
        _write_json(Path(str(archive) + ".pmsig"), pmsig)
    elif mutation == "pmsig_merkle_root_mismatch":
        pmsig["subject"]["pmidx_merkle_root"] = OTHER_HASH
        _write_json(Path(str(archive) + ".pmsig"), pmsig)
    elif mutation == "pmsig_schema_version_invalid":
        pmsig["schema_version"] = "kfm.pmsig.future"
        _write_json(Path(str(archive) + ".pmsig"), pmsig)
    elif mutation == "runreceipt_spec_hash_mismatch":
        receipt["predicate"]["buildDefinition"]["externalParameters"][
            "spec_hash"
        ] = OTHER_HASH
        _write_json(Path(str(archive) + ".runreceipt.json"), receipt)
    elif mutation == "runreceipt_archive_digest_mismatch":
        receipt["subject"][0]["digest"]["sha256"] = OTHER_HASH.removeprefix(
            "sha256:"
        )
        _write_json(Path(str(archive) + ".runreceipt.json"), receipt)
    elif mutation == "runreceipt_subject_name_mismatch":
        receipt["subject"][0]["name"] = "different.pmtiles"
        _write_json(Path(str(archive) + ".runreceipt.json"), receipt)
    elif mutation == "runreceipt_subject_count_invalid":
        receipt["subject"].append(dict(receipt["subject"][0]))
        _write_json(Path(str(archive) + ".runreceipt.json"), receipt)
    elif mutation == "pmsig_duplicate_key":
        Path(str(archive) + ".pmsig").write_text(
            '{"schema_version":"kfm.pmsig.v1",'
            '"schema_version":"kfm.pmsig.v1"}\n',
            encoding="utf-8",
        )
    elif mutation == "missing_runreceipt":
        Path(str(archive) + ".runreceipt.json").unlink()
    else:
        raise AssertionError(f"unknown fixture mutation: {mutation}")


class PMTilesAttestationBundleTests(unittest.TestCase):
    def test_repository_owned_fixture_matrix(self) -> None:
        descriptors = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
        descriptors += sorted((FIXTURE_ROOT / "invalid").glob("*.json"))
        self.assertGreaterEqual(len(descriptors), 10)
        for descriptor in descriptors:
            case = json.loads(descriptor.read_text(encoding="utf-8"))
            if descriptor.parent.name == "invalid":
                expected_sidecar = descriptor.with_suffix(".expected_error.txt")
                self.assertTrue(expected_sidecar.is_file(), expected_sidecar)
                primary_code = expected_sidecar.read_text(encoding="utf-8").strip()
                self.assertTrue(primary_code)
                self.assertNotIn("\n", primary_code)
                self.assertIn(primary_code, case["expected"]["issue_codes"])
            with self.subTest(case=case["case_id"]), tempfile.TemporaryDirectory() as raw:
                bundle = _build_bundle(Path(raw))
                _apply_mutation(bundle, case["mutation"])
                result = validate_bundle(bundle["archive"])
                self.assertEqual(case["expected"]["status"], result.status)
                self.assertEqual(
                    case["expected"]["issue_codes"],
                    [finding.code for finding in result.findings],
                )

    def test_success_is_structural_and_keeps_all_holds(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            result = validate_bundle(_build_bundle(Path(raw))["archive"])
        rendered = json.loads(render_result(result))
        self.assertEqual("STRUCTURAL_PASS", rendered["status"])
        self.assertEqual("NONE", rendered["authority"])
        self.assertEqual(list(HOLDS), rendered["holds"])

    def test_header_decodes_all_distinct_field_classes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            archive = Path(raw) / "tiles.pmtiles"
            archive.write_bytes(_archive_payload())
            inspection = inspect_archive(archive)
        self.assertEqual(127, inspection.header.root_offset)
        self.assertEqual(5, inspection.header.root_length)
        self.assertEqual(1, inspection.header.addressed_tiles_count)
        self.assertEqual(1, inspection.header.clustered)
        self.assertEqual(1, inspection.header.internal_compression)
        self.assertEqual(-1_020_000_000, inspection.header.min_lon_e7)
        self.assertEqual(385_000_000, inspection.header.center_lat_e7)

    def test_header_accepts_spec_defined_unknown_counts_and_current_enums(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            archive = Path(raw) / "tiles.pmtiles"
            payload = bytearray(_archive_payload())
            for offset in (72, 80, 88):
                struct.pack_into("<Q", payload, offset, 0)
            payload[98] = 0  # unknown tile compression is a defined enum value
            payload[99] = 6  # MapLibre Vector Tile
            payload[100], payload[101], payload[118] = 5, 8, 0
            archive.write_bytes(payload)
            inspection = inspect_archive(archive)
        self.assertEqual(0, inspection.header.addressed_tiles_count)
        self.assertEqual(6, inspection.header.tile_type)
        self.assertEqual(0, inspection.header.center_zoom)

    def test_header_rejects_truncation_root_limit_overlap_zoom_and_bounds(self) -> None:
        cases: list[tuple[str, Callable[[bytearray], bytes]]] = []

        def truncated(value: bytearray) -> bytes:
            return bytes(value[:126])

        def root_limit(value: bytearray) -> bytes:
            struct.pack_into("<Q", value, 8, 16_383)
            struct.pack_into("<Q", value, 16, 2)
            return bytes(value)

        def overlap(value: bytearray) -> bytes:
            root_offset = struct.unpack_from("<Q", value, 8)[0]
            struct.pack_into("<Q", value, 24, root_offset + 1)
            return bytes(value)

        def zoom(value: bytearray) -> bytes:
            value[100], value[101] = 4, 3
            return bytes(value)

        def bounds(value: bytearray) -> bytes:
            struct.pack_into("<i", value, 102, 100)
            struct.pack_into("<i", value, 110, -100)
            return bytes(value)

        cases.extend(
            [
                ("HEADER_TRUNCATED", truncated),
                ("HEADER_ROOT_DIRECTORY_TOO_LARGE", root_limit),
                ("HEADER_REGION_OVERLAP", overlap),
                ("HEADER_ZOOM_INVALID", zoom),
                ("HEADER_BOUNDS_INVALID", bounds),
            ]
        )
        for expected, mutate in cases:
            with self.subTest(expected=expected), tempfile.TemporaryDirectory() as raw:
                archive = Path(raw) / "tiles.pmtiles"
                archive.write_bytes(mutate(bytearray(_archive_payload())))
                with self.assertRaises(HeaderValidationError) as caught:
                    inspect_archive(archive)
                self.assertEqual(expected, caught.exception.code)

    def test_metadata_gzip_success_and_unsupported_compression(self) -> None:
        raw_metadata = json.dumps({"spec_hash": SPEC_HASH}).encode("utf-8")
        with tempfile.TemporaryDirectory() as raw:
            archive = Path(raw) / "gzip.pmtiles"
            archive.write_bytes(
                _archive_payload(
                    metadata_bytes=gzip.compress(raw_metadata), internal_compression=2
                )
            )
            self.assertEqual(SPEC_HASH, inspect_archive(archive).spec_hash)
            archive.write_bytes(
                _archive_payload(metadata_bytes=raw_metadata, internal_compression=3)
            )
            with self.assertRaises(HeaderValidationError) as caught:
                inspect_archive(archive)
            self.assertEqual("METADATA_COMPRESSION_UNSUPPORTED", caught.exception.code)

            archive.write_bytes(
                _archive_payload(
                    metadata_bytes=gzip.compress(b"x" * (1024 * 1024 + 1)),
                    internal_compression=2,
                )
            )
            with self.assertRaises(HeaderValidationError) as caught:
                inspect_archive(archive)
            self.assertEqual("METADATA_TOO_LARGE", caught.exception.code)

    def test_metadata_rejects_conflicting_or_malformed_spec_hash_aliases(self) -> None:
        metadata_cases = (
            (
                {"spec_hash": SPEC_HASH, "kfm": {"spec_hash": OTHER_HASH}},
                "SPEC_HASH_MISMATCH",
            ),
            (
                {"spec_hash": SPEC_HASH, "kfm": {"spec_hash": "attacker-value"}},
                "SPEC_HASH_INVALID",
            ),
        )
        for metadata, expected in metadata_cases:
            with self.subTest(expected=expected), tempfile.TemporaryDirectory() as raw:
                archive = Path(raw) / "tiles.pmtiles"
                archive.write_bytes(
                    _archive_payload(
                        metadata_bytes=json.dumps(metadata).encode("utf-8")
                    )
                )
                with self.assertRaises(HeaderValidationError) as caught:
                    inspect_archive(archive)
                self.assertEqual(expected, caught.exception.code)

    def test_each_json_parser_rejects_nonfinite_numbers(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            archive = bundle["archive"]

            metadata = ('{"spec_hash":"' + SPEC_HASH + '","unsafe":NaN}').encode()
            archive.write_bytes(_archive_payload(metadata_bytes=metadata))
            with self.assertRaises(HeaderValidationError) as caught:
                inspect_archive(archive)
            self.assertEqual("METADATA_JSON_NONFINITE_NUMBER", caught.exception.code)

            bundle = _build_bundle(Path(raw))
            archive = bundle["archive"]
            index_path = Path(str(archive) + ".pmidx")
            index_text = index_path.read_text(encoding="utf-8").rstrip()[:-1]
            index_path.write_text(index_text + ',"unsafe":NaN}\n', encoding="utf-8")
            with self.assertRaises(MerkleValidationError) as caught:
                inspect_index(index_path, archive)
            self.assertEqual("PMIDX_JSON_NONFINITE_NUMBER", caught.exception.code)

            bundle = _build_bundle(Path(raw))
            archive = bundle["archive"]
            Path(str(archive) + ".pmsig").write_text(
                '{"schema_version":"kfm.pmsig.v1","unsafe":Infinity}\n',
                encoding="utf-8",
            )
            result = validate_bundle(archive)
            self.assertEqual(
                ["PMSIG_JSON_NONFINITE_NUMBER"],
                [finding.code for finding in result.findings],
            )

    def test_merkle_golden_vector_uses_odd_final_group(self) -> None:
        leaves = [
            "sha256:ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb",
            "sha256:3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d",
            "sha256:2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6",
        ]
        self.assertEqual(
            "sha256:e76328b6ca10676c686a0d534e8222ad8da04fdfe14c6f6ff67d08cbbd24c605",
            merkle_root(leaves, 2),
        )

    def test_pmidx_bool_chunk_size_and_cross_chunk_range_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            archive = bundle["archive"]
            index = bundle["index"]
            index["merkle"]["chunk_bytes"] = True
            _write_json(Path(str(archive) + ".pmidx"), index)
            with self.assertRaises(MerkleValidationError) as caught:
                inspect_index(Path(str(archive) + ".pmidx"), archive)
            self.assertEqual("PMIDX_CHUNK_BYTES_INVALID", caught.exception.code)

            bundle = _build_bundle(Path(raw), chunk_bytes=64)
            archive = bundle["archive"]
            index = bundle["index"]
            index["ranges"] = [{"offset": 60, "length": 8, "leaf": 0}]
            _write_json(Path(str(archive) + ".pmidx"), index)
            with self.assertRaises(MerkleValidationError) as caught:
                inspect_index(Path(str(archive) + ".pmidx"), archive)
            self.assertEqual("PMIDX_RANGE_LEAF_BINDING_INVALID", caught.exception.code)

    def test_current_attestation_producers_remain_compatible(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            archive = bundle["archive"]
            pmidx = Path(str(archive) + ".pmidx")
            subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "tools/attest/sign_pmtiles.py"),
                    "--pmtiles",
                    archive.name,
                    "--pmidx",
                    pmidx.name,
                    "--spec-hash",
                    SPEC_HASH,
                    "--key-id",
                    "TEST_ONLY_UNAPPROVED_KEY",
                    "--out",
                    archive.name + ".pmsig",
                ],
                check=True,
                capture_output=True,
                text=True,
                cwd=raw,
            )
            subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "tools/attest/build_runreceipt.py"),
                    "--pmtiles",
                    archive.name,
                    "--spec-hash",
                    SPEC_HASH,
                    "--builder-id",
                    "kfm-test-builder",
                    "--out",
                    archive.name + ".runreceipt.json",
                ],
                check=True,
                capture_output=True,
                text=True,
                cwd=raw,
            )
            result = validate_bundle(archive)
        self.assertTrue(result.ok)

    def test_output_is_sorted_deduplicated_and_never_echoes_values(self) -> None:
        sentinel = "DO_NOT_ECHO\n::error::attacker-value"
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            archive = bundle["archive"]
            pmsig = bundle["pmsig"]
            receipt = bundle["receipt"]
            pmsig["key_id"] = sentinel
            pmsig["subject"]["spec_hash"] = sentinel
            receipt["subject"][0]["name"] = sentinel
            receipt["predicate"]["buildDefinition"]["externalParameters"][
                "spec_hash"
            ] = sentinel
            _write_json(Path(str(archive) + ".pmsig"), pmsig)
            _write_json(Path(str(archive) + ".runreceipt.json"), receipt)
            rendered = render_result(validate_bundle(archive))
        self.assertNotIn(sentinel, rendered)
        payload = json.loads(rendered)
        codes = [item["code"] for item in payload["issues"]]
        self.assertEqual(sorted(set(codes)), codes)

    def test_oversized_companion_has_one_finite_code(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            archive = bundle["archive"]
            Path(str(archive) + ".pmsig").write_text(
                '{"padding":"' + ("x" * (1024 * 1024)) + '"}', encoding="utf-8"
            )
            result = validate_bundle(archive)
        self.assertEqual(["PMSIG_JSON_TOO_LARGE"], [item.code for item in result.findings])

    def test_symlink_companion_is_denied_without_following_it(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            archive = bundle["archive"]
            pmsig = Path(str(archive) + ".pmsig")
            target = Path(raw) / "target.json"
            pmsig.replace(target)
            pmsig.symlink_to(target)
            result = validate_bundle(archive)
        self.assertEqual(["PMSIG_SYMLINK_DENIED"], [item.code for item in result.findings])


if __name__ == "__main__":
    unittest.main()
