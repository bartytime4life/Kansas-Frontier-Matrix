from __future__ import annotations

import gzip
import hashlib
import json
import math
import socket
import struct
import subprocess
import sys
import tempfile
import unittest
import urllib.request
from pathlib import Path
from typing import Callable
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_DIR = REPO_ROOT / "tools/validators/pmtiles"
sys.path.insert(0, str(VALIDATOR_DIR))

from validate_attestation_bundle import (
    HOLDS,
    MAX_JSON_BYTES,
    TILE_MANIFEST_CHECK,
    TILE_MANIFEST_FINDING_CODES,
    TILE_MANIFEST_HOLDS,
    TILE_MANIFEST_PARSER_FINDING_CODES,
    TILE_MANIFEST_PROFILE,
    _load_json,
    render_result,
    validate_bundle,
)
from validate_header import HeaderValidationError, inspect_archive
from verify_merkle import MerkleValidationError, inspect_index, merkle_root
from verify_partial_read import (
    HOLDS as PARTIAL_READ_HOLDS,
    PROFILE as PARTIAL_READ_PROFILE,
    render_result as render_partial_read_result,
    verify_partial_read,
)

FIXTURE_ROOT = REPO_ROOT / "fixtures/pmtiles/attestation"
PARTIAL_READ_FIXTURE_ROOT = FIXTURE_ROOT / "partial-read"
SPEC_HASH = "sha256:" + hashlib.sha256(b"kfm-test-build-spec").hexdigest()
OTHER_HASH = "sha256:" + hashlib.sha256(b"different-value").hexdigest()
ROOT_DIRECTORY = b"\x01\x00\x01\x01\x01"

EXPECTED_TILE_MANIFEST_DESCRIPTOR_CODES = {
    "manifest_artifact_name_invalid.json": "TILE_MANIFEST_ARTIFACT_NAME_INVALID",
    "manifest_artifact_name_mismatch.json": "TILE_MANIFEST_ARTIFACT_NAME_MISMATCH",
    "manifest_artifact_ref_control_character.json": "TILE_MANIFEST_ARTIFACT_REF_NOT_DIGEST_BOUND",
    "manifest_artifact_ref_digest_mismatch.json": "TILE_MANIFEST_ARTIFACT_REF_DIGEST_MISMATCH",
    "manifest_artifact_ref_mutable.json": "TILE_MANIFEST_ARTIFACT_REF_NOT_DIGEST_BOUND",
    "manifest_artifact_ref_not_digest_bound.json": "TILE_MANIFEST_ARTIFACT_REF_NOT_DIGEST_BOUND",
    "manifest_bounds_degenerate.json": "TILE_MANIFEST_BOUNDS_ORDER_INVALID",
    "manifest_bounds_header_mismatch.json": "TILE_MANIFEST_BOUNDS_HEADER_MISMATCH",
    "manifest_bounds_mercator_cutoff.json": "TILE_MANIFEST_BOUNDS_ORDER_INVALID",
    "manifest_bounds_order_invalid.json": "TILE_MANIFEST_BOUNDS_ORDER_INVALID",
    "manifest_bounds_value_invalid.json": "TILE_MANIFEST_BOUNDS_INVALID",
    "manifest_byte_size_invalid.json": "TILE_MANIFEST_BYTE_SIZE_INVALID",
    "manifest_byte_size_mismatch.json": "TILE_MANIFEST_BYTE_SIZE_MISMATCH",
    "manifest_complexity_limit.json": "TILE_MANIFEST_COMPLEXITY_LIMIT",
    "manifest_digest_mismatch.json": "TILE_MANIFEST_DIGEST_MISMATCH",
    "manifest_digest_placeholder.json": "TILE_MANIFEST_DIGEST_INVALID",
    "manifest_embedded_payload.json": "TILE_MANIFEST_EMBEDDED_PAYLOAD_DENIED",
    "manifest_generation_tool_missing.json": "TILE_MANIFEST_GENERATION_TOOL_INVALID",
    "manifest_maxzoom_invalid.json": "TILE_MANIFEST_MAXZOOM_INVALID",
    "manifest_media_type_unsupported.json": "TILE_MANIFEST_MEDIA_TYPE_UNSUPPORTED",
    "manifest_minzoom_invalid.json": "TILE_MANIFEST_MINZOOM_INVALID",
    "manifest_pmtiles_profile_invalid.json": "TILE_MANIFEST_PMTILES_PROFILE_INVALID",
    "manifest_profile_invalid.json": "TILE_MANIFEST_PROFILE_INVALID",
    "manifest_source_ref_unversioned.json": "TILE_MANIFEST_SOURCE_REFS_INVALID",
    "manifest_source_ref_control_character.json": "TILE_MANIFEST_SOURCE_REFS_INVALID",
    "manifest_source_refs_missing.json": "TILE_MANIFEST_SOURCE_REFS_INVALID",
    "manifest_spec_hash_invalid.json": "TILE_MANIFEST_SPEC_HASH_INVALID",
    "manifest_spec_hash_mismatch.json": "TILE_MANIFEST_SPEC_HASH_MISMATCH",
    "manifest_tile_format_header_mismatch.json": "TILE_MANIFEST_TILE_FORMAT_MISMATCH",
    "manifest_tile_format_unsupported.json": "TILE_MANIFEST_TILE_FORMAT_UNSUPPORTED",
    "manifest_tiling_scheme_metadata_mismatch.json": "TILE_MANIFEST_TILING_SCHEME_METADATA_MISMATCH",
    "manifest_tiling_scheme_unsupported.json": "TILE_MANIFEST_TILING_SCHEME_UNSUPPORTED",
    "manifest_undeclared_field.json": "TILE_MANIFEST_UNDECLARED_FIELD",
    "manifest_vector_layer_duplicate.json": "TILE_MANIFEST_VECTOR_LAYER_ID_DUPLICATE",
    "manifest_vector_layer_fields_mismatch.json": "TILE_MANIFEST_VECTOR_LAYERS_MISMATCH",
    "manifest_vector_layers_invalid.json": "TILE_MANIFEST_VECTOR_LAYERS_INVALID",
    "manifest_vector_layers_mismatch.json": "TILE_MANIFEST_VECTOR_LAYERS_MISMATCH",
    "manifest_version_unsupported.json": "TILE_MANIFEST_PMTILES_VERSION_UNSUPPORTED",
    "manifest_zoom_header_mismatch.json": "TILE_MANIFEST_ZOOM_HEADER_MISMATCH",
    "manifest_zoom_order_invalid.json": "TILE_MANIFEST_ZOOM_ORDER_INVALID",
}


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
        {
            "name": "synthetic-kfm-fixture",
            "spec_hash": SPEC_HASH,
            "vector_layers": [
                {"id": "synthetic", "fields": {"value": "String"}}
            ],
        },
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
    header[96:102] = bytes((1, internal_compression, 1, 1, 0, 0))
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


def _partial_read_inputs(
    bundle: dict[str, object], mutation: str
) -> dict[str, object]:
    archive = bundle["archive"]
    archive_bytes = bundle["archive_bytes"]
    index = bundle["index"]
    pmsig = bundle["pmsig"]
    assert isinstance(archive, Path)
    assert isinstance(archive_bytes, bytes)
    assert isinstance(index, dict)
    assert isinstance(pmsig, dict)

    directory = archive.parent
    offset = 0
    length = 10
    leaf = 0
    range_bytes = archive_bytes[offset:offset + length]
    leaf_bytes = archive_bytes[:64]

    if mutation == "none":
        pass
    elif mutation == "range_bytes_mismatch":
        range_bytes = bytes((range_bytes[0] ^ 1,)) + range_bytes[1:]
    elif mutation == "leaf_digest_mismatch":
        leaf_bytes = leaf_bytes[:-1] + bytes((leaf_bytes[-1] ^ 1,))
    elif mutation == "range_not_declared":
        offset = 1
        range_bytes = archive_bytes[offset:offset + length]
    elif mutation == "pmsig_root_mismatch":
        pmsig["subject"]["pmidx_merkle_root"] = OTHER_HASH
        _write_json(Path(str(archive) + ".pmsig"), pmsig)
    elif mutation == "cross_chunk_declaration":
        offset = 60
        length = 8
        range_bytes = archive_bytes[offset:offset + length]
        index["ranges"] = [
            {"tile_id": "synthetic", "offset": offset, "length": length, "leaf": leaf}
        ]
        _write_json(Path(str(archive) + ".pmidx"), index)
    else:
        raise AssertionError(f"unknown partial-read mutation: {mutation}")

    range_path = directory / "captured-range.bin"
    leaf_path = directory / "containing-leaf.bin"
    range_path.write_bytes(range_bytes)
    leaf_path.write_bytes(leaf_bytes)
    return {
        "pmidx_path": Path(str(archive) + ".pmidx"),
        "pmsig_path": Path(str(archive) + ".pmsig"),
        "range_path": range_path,
        "leaf_path": leaf_path,
        "archive_size": len(archive_bytes),
        "offset": offset,
        "length": length,
    }


def _build_tile_manifest(bundle: dict[str, object]) -> Path:
    archive = bundle["archive"]
    index = bundle["index"]
    assert isinstance(archive, Path) and isinstance(index, dict)
    archive_digest = index["pmtiles_sha256"]
    assert isinstance(archive_digest, str)
    manifest = {
        "profile": TILE_MANIFEST_PROFILE,
        "artifact_name": archive.name,
        "artifact_ref": (
            "kfm://artifact/pmtiles/synthetic-fixture@" + archive_digest
        ),
        "media_type": "application/vnd.pmtiles",
        "digest": archive_digest,
        "byte_size": archive.stat().st_size,
        "spec_hash": SPEC_HASH,
        "source_manifest_refs": ["kfm://manifest/source/synthetic-fixture@v1"],
        "generation_tool": "kfm-test-builder@1.0.0",
        "pmtiles": {
            "pmtiles_version": "v3",
            "tile_format": "mvt",
            "tiling_scheme": "xyz",
            "minzoom": 0,
            "maxzoom": 0,
            "bounds": [-102.0, 37.0, -94.0, 40.0],
            "vector_layers": [
                {"id": "synthetic", "fields": {"value": "String"}}
            ],
        },
    }
    path = archive.parent / "tile-artifact-manifest.compat.json"
    _write_json(path, manifest)
    bundle["tile_manifest"] = manifest
    return path


def _apply_tile_manifest_mutation(bundle: dict[str, object], mutation: str) -> None:
    archive = bundle["archive"]
    manifest = bundle["tile_manifest"]
    assert isinstance(archive, Path) and isinstance(manifest, dict)
    pmtiles = manifest["pmtiles"]
    assert isinstance(pmtiles, dict)

    if mutation == "manifest_none":
        return
    if mutation == "manifest_profile_invalid":
        manifest["profile"] = "kfm.pmtiles.tile-artifact-manifest.future"
    elif mutation == "manifest_artifact_name_invalid":
        manifest["artifact_name"] = "../tiles.pmtiles"
    elif mutation == "manifest_artifact_name_mismatch":
        manifest["artifact_name"] = "different.pmtiles"
    elif mutation == "manifest_artifact_ref_not_digest_bound":
        manifest["artifact_ref"] = "kfm://artifact/pmtiles/latest"
    elif mutation == "manifest_artifact_ref_control_character":
        manifest["artifact_ref"] = (
            "kfm://artifact/pmtiles/\u202eevil@" + manifest["digest"]
        )
    elif mutation == "manifest_artifact_ref_digest_mismatch":
        manifest["artifact_ref"] = (
            "kfm://artifact/pmtiles/synthetic-fixture@" + OTHER_HASH
        )
    elif mutation == "manifest_media_type_unsupported":
        manifest["media_type"] = "application/octet-stream"
    elif mutation == "manifest_digest_placeholder":
        manifest["digest"] = "sha256:" + ("0" * 64)
    elif mutation == "manifest_digest_mismatch":
        manifest["digest"] = OTHER_HASH
        manifest["artifact_ref"] = (
            "kfm://artifact/pmtiles/synthetic-fixture@" + OTHER_HASH
        )
    elif mutation == "manifest_byte_size_invalid":
        manifest["byte_size"] = 126
    elif mutation == "manifest_byte_size_mismatch":
        manifest["byte_size"] = archive.stat().st_size + 1
    elif mutation == "manifest_spec_hash_mismatch":
        manifest["spec_hash"] = OTHER_HASH
    elif mutation == "manifest_spec_hash_invalid":
        manifest["spec_hash"] = "sha256:" + ("0" * 64)
    elif mutation == "manifest_source_refs_missing":
        manifest["source_manifest_refs"] = []
    elif mutation == "manifest_source_ref_unversioned":
        manifest["source_manifest_refs"] = ["kfm://manifest/source/latest"]
    elif mutation == "manifest_source_ref_control_character":
        manifest["source_manifest_refs"] = [
            "kfm://manifest/source/\u0085evil@v1"
        ]
    elif mutation == "manifest_generation_tool_missing":
        manifest["generation_tool"] = ""
    elif mutation == "manifest_version_unsupported":
        pmtiles["pmtiles_version"] = "v4"
    elif mutation == "manifest_pmtiles_profile_invalid":
        del pmtiles["tiling_scheme"]
    elif mutation == "manifest_tile_format_unsupported":
        pmtiles["tile_format"] = "mlt"
    elif mutation == "manifest_tile_format_header_mismatch":
        payload = bytearray(bundle["archive_bytes"])
        payload[99] = 6
        _rewrite_archive_and_rebind(bundle, bytes(payload))
    elif mutation == "manifest_tiling_scheme_unsupported":
        pmtiles["tiling_scheme"] = "tms"
    elif mutation == "manifest_tiling_scheme_metadata_mismatch":
        metadata = {
            "name": "synthetic-kfm-fixture",
            "scheme": "tms",
            "spec_hash": SPEC_HASH,
            "vector_layers": [
                {"id": "synthetic", "fields": {"value": "String"}}
            ],
        }
        _rewrite_archive_and_rebind(
            bundle,
            _archive_payload(
                metadata_bytes=json.dumps(
                    metadata, separators=(",", ":"), sort_keys=True
                ).encode("utf-8"),
                tile_bytes=b"synthetic-tile-content",
            ),
        )
    elif mutation == "manifest_minzoom_invalid":
        pmtiles["minzoom"] = -1
    elif mutation == "manifest_maxzoom_invalid":
        pmtiles["maxzoom"] = 256
    elif mutation == "manifest_zoom_order_invalid":
        pmtiles["minzoom"], pmtiles["maxzoom"] = 1, 0
    elif mutation == "manifest_zoom_header_mismatch":
        payload = bytearray(bundle["archive_bytes"])
        payload[100], payload[101] = 1, 1
        _rewrite_archive_and_rebind(bundle, bytes(payload))
    elif mutation == "manifest_bounds_value_invalid":
        pmtiles["bounds"][0] = 10**400
    elif mutation == "manifest_bounds_order_invalid":
        pmtiles["bounds"] = [-94.0, 37.0, -102.0, 40.0]
    elif mutation == "manifest_bounds_degenerate":
        pmtiles["bounds"] = [-102.0, 37.0, -102.0, 40.0]
    elif mutation == "manifest_bounds_mercator_cutoff":
        pmtiles["bounds"] = [-102.0, -85.05113, -94.0, 40.0]
    elif mutation == "manifest_bounds_header_mismatch":
        payload = bytearray(bundle["archive_bytes"])
        struct.pack_into("<i", payload, 102, -1_010_000_000)
        _rewrite_archive_and_rebind(bundle, bytes(payload))
    elif mutation == "manifest_vector_layer_duplicate":
        pmtiles["vector_layers"].append(dict(pmtiles["vector_layers"][0]))
    elif mutation == "manifest_vector_layers_mismatch":
        pmtiles["vector_layers"][0]["id"] = "different"
    elif mutation == "manifest_vector_layer_fields_mismatch":
        pmtiles["vector_layers"][0]["fields"]["value"] = "Number"
    elif mutation == "manifest_vector_layers_invalid":
        pmtiles["vector_layers"][0]["fields"] = []
    elif mutation == "manifest_undeclared_field":
        manifest["future_field"] = True
    elif mutation == "manifest_complexity_limit":
        manifest["future_field"] = [0] * 100_001
    elif mutation == "manifest_embedded_payload":
        manifest["payload"] = "synthetic-but-still-denied"
    else:
        raise AssertionError(f"unknown tile-manifest mutation: {mutation}")

    path = archive.parent / "tile-artifact-manifest.compat.json"
    _write_json(path, manifest)


def _rewrite_archive_and_rebind(bundle: dict[str, object], payload: bytes) -> None:
    archive = bundle["archive"]
    index = bundle["index"]
    pmsig = bundle["pmsig"]
    receipt = bundle["receipt"]
    assert isinstance(archive, Path)
    assert isinstance(index, dict) and isinstance(pmsig, dict) and isinstance(receipt, dict)

    archive.write_bytes(payload)
    archive_bytes = archive.read_bytes()
    chunk_bytes = index["merkle"]["chunk_bytes"]
    leaves = [
        "sha256:" + hashlib.sha256(archive_bytes[start:start + chunk_bytes]).hexdigest()
        for start in range(0, len(archive_bytes), chunk_bytes)
    ]
    digest = "sha256:" + hashlib.sha256(archive_bytes).hexdigest()
    index["pmtiles_sha256"] = digest
    index["merkle"]["leaves"] = leaves
    index["merkle"]["root"] = _independent_merkle_root(leaves, index["merkle"]["arity"])
    _write_json(Path(str(archive) + ".pmidx"), index)
    pmsig["subject"]["pmtiles_sha256"] = digest
    pmsig["subject"]["pmidx_merkle_root"] = index["merkle"]["root"]
    _write_json(Path(str(archive) + ".pmsig"), pmsig)
    receipt["subject"][0]["digest"]["sha256"] = digest.removeprefix("sha256:")
    _write_json(Path(str(archive) + ".runreceipt.json"), receipt)
    bundle["archive_bytes"] = archive_bytes
    manifest = bundle.get("tile_manifest")
    if isinstance(manifest, dict):
        manifest["artifact_ref"] = (
            "kfm://artifact/pmtiles/synthetic-fixture@" + digest
        )
        manifest["byte_size"] = archive.stat().st_size
        manifest["digest"] = digest
        _write_json(archive.parent / "tile-artifact-manifest.compat.json", manifest)


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
                if case.get("fixture_profile") == TILE_MANIFEST_PROFILE:
                    manifest_path = _build_tile_manifest(bundle)
                    _apply_tile_manifest_mutation(bundle, case["mutation"])
                    result = validate_bundle(bundle["archive"], manifest_path)
                else:
                    _apply_mutation(bundle, case["mutation"])
                    result = validate_bundle(bundle["archive"])
                self.assertEqual(case["expected"]["status"], result.status)
                self.assertEqual(
                    case["expected"]["issue_codes"],
                    [finding.code for finding in result.findings],
                )

    def test_partial_read_fixture_matrix_is_exact(self) -> None:
        valid = sorted((PARTIAL_READ_FIXTURE_ROOT / "valid").glob("*.json"))
        invalid = sorted((PARTIAL_READ_FIXTURE_ROOT / "invalid").glob("*.json"))
        self.assertEqual(["complete.json"], [path.name for path in valid])
        self.assertEqual(
            {
                "cross_chunk_declaration.json",
                "leaf_digest_mismatch.json",
                "pmsig_root_mismatch.json",
                "range_bytes_mismatch.json",
                "range_not_declared.json",
            },
            {path.name for path in invalid},
        )
        for descriptor in valid + invalid:
            case = json.loads(descriptor.read_text(encoding="utf-8"))
            self.assertEqual(PARTIAL_READ_PROFILE, case["fixture_profile"])
            if descriptor.parent.name == "invalid":
                sidecar = descriptor.with_suffix(".expected_error.txt")
                self.assertTrue(sidecar.is_file(), sidecar)
                self.assertEqual(
                    case["expected"]["issue_codes"][0],
                    sidecar.read_text(encoding="utf-8").strip(),
                )
            with self.subTest(case=case["case_id"]), tempfile.TemporaryDirectory() as raw:
                bundle = _build_bundle(Path(raw))
                inputs = _partial_read_inputs(bundle, case["mutation"])
                result = verify_partial_read(**inputs)
                self.assertEqual(case["expected"]["status"], result.status)
                self.assertEqual(case["expected"]["issue_codes"], list(result.findings))

    def test_partial_read_success_keeps_every_authority_hold(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            inputs = _partial_read_inputs(bundle, "none")
            result = verify_partial_read(**inputs)
            payload = json.loads(render_partial_read_result(result))
        self.assertEqual("STRUCTURAL_HOLD", payload["status"])
        self.assertEqual("NONE", payload["authority"])
        self.assertEqual(list(PARTIAL_READ_HOLDS), payload["holds"])
        self.assertEqual({"offset": 0, "length": 10, "leaf": 0}, payload["verified_range"])
        self.assertIn("RANGE_METADATA_NOT_AUTHENTICATED", payload["holds"])
        self.assertIn("BAO_OUTBOARD_PROOF_UNADOPTED", payload["holds"])

    def test_partial_read_cli_is_explicit_json_and_no_network(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            inputs = _partial_read_inputs(bundle, "none")
            with (
                mock.patch.object(socket.socket, "connect", side_effect=AssertionError),
                mock.patch.object(socket, "create_connection", side_effect=AssertionError),
                mock.patch.object(urllib.request, "urlopen", side_effect=AssertionError),
            ):
                self.assertTrue(verify_partial_read(**inputs).ok)
            completed = subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR_DIR / "verify_partial_read.py"),
                    "--pmidx",
                    str(inputs["pmidx_path"]),
                    "--pmsig",
                    str(inputs["pmsig_path"]),
                    "--range-bytes",
                    str(inputs["range_path"]),
                    "--leaf-bytes",
                    str(inputs["leaf_path"]),
                    "--archive-size",
                    str(inputs["archive_size"]),
                    "--offset",
                    str(inputs["offset"]),
                    "--length",
                    str(inputs["length"]),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
        payload = json.loads(completed.stdout)
        self.assertEqual(PARTIAL_READ_PROFILE, payload["profile"])
        self.assertEqual("STRUCTURAL_HOLD", payload["status"])
        self.assertEqual([], payload["findings"])

    def test_partial_read_denies_symlinks_and_invalid_integer_bounds(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            inputs = _partial_read_inputs(bundle, "none")
            range_path = inputs["range_path"]
            assert isinstance(range_path, Path)
            range_path.unlink()
            range_path.symlink_to(inputs["leaf_path"])
            result = verify_partial_read(**inputs)
            self.assertEqual(("PARTIAL_RANGE_BYTES_SYMLINK_DENIED",), result.findings)

            range_path.unlink()
            inputs = _partial_read_inputs(bundle, "none")
            inputs["archive_size"] = True
            result = verify_partial_read(**inputs)
            self.assertEqual(("PARTIAL_ARCHIVE_SIZE_INVALID",), result.findings)

    def test_tile_manifest_fixture_inventory_and_sidecars_are_exact(self) -> None:
        valid = sorted((FIXTURE_ROOT / "valid").glob("manifest_*.json"))
        invalid = sorted((FIXTURE_ROOT / "invalid").glob("manifest_*.json"))
        sidecars = sorted((FIXTURE_ROOT / "invalid").glob("manifest_*.expected_error.txt"))
        self.assertEqual(["manifest_profile_complete.json"], [path.name for path in valid])
        self.assertEqual(
            set(EXPECTED_TILE_MANIFEST_DESCRIPTOR_CODES),
            {path.name for path in invalid},
        )
        self.assertEqual(
            [path.with_suffix(".expected_error.txt").name for path in invalid],
            [path.name for path in sidecars],
        )
        for path in invalid:
            self.assertEqual(
                EXPECTED_TILE_MANIFEST_DESCRIPTOR_CODES[path.name],
                path.with_suffix(".expected_error.txt")
                .read_text(encoding="utf-8")
                .strip(),
            )
        self.assertEqual(
            TILE_MANIFEST_FINDING_CODES,
            frozenset(EXPECTED_TILE_MANIFEST_DESCRIPTOR_CODES.values())
            | {"TILE_MANIFEST_METADATA_VECTOR_LAYERS_INVALID"},
        )

    def test_tile_manifest_profile_is_opt_in_and_keeps_authority_hold(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            default_payload = json.loads(render_result(validate_bundle(bundle["archive"])))
            manifest_path = _build_tile_manifest(bundle)
            profile_payload = json.loads(
                render_result(validate_bundle(bundle["archive"], manifest_path))
            )
        self.assertNotIn(TILE_MANIFEST_CHECK, default_payload["checks"])
        self.assertNotIn(TILE_MANIFEST_HOLDS[0], default_payload["holds"])
        self.assertIn(TILE_MANIFEST_CHECK, profile_payload["checks"])
        self.assertEqual(list(HOLDS) + list(TILE_MANIFEST_HOLDS), profile_payload["holds"])
        self.assertEqual("NONE", profile_payload["authority"])
        self.assertEqual("STRUCTURAL_PASS", profile_payload["status"])

    def test_tile_manifest_cli_flag_is_explicit_and_offline(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            manifest_path = _build_tile_manifest(bundle)
            completed = subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR_DIR / "validate_attestation_bundle.py"),
                    str(bundle["archive"]),
                    "--tile-manifest",
                    str(manifest_path),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
        payload = json.loads(completed.stdout)
        self.assertEqual("STRUCTURAL_PASS", payload["status"])
        self.assertEqual("NONE", payload["authority"])
        self.assertIn(TILE_MANIFEST_CHECK, payload["checks"])

    def test_tile_manifest_metadata_vector_layers_are_required_for_mvt(self) -> None:
        metadata_cases = (
            {"name": "synthetic-kfm-fixture", "spec_hash": SPEC_HASH},
            {
                "name": "synthetic-kfm-fixture",
                "spec_hash": SPEC_HASH,
                "vector_layers": [{"id": "synthetic"}],
            },
        )
        for metadata in metadata_cases:
            with self.subTest(metadata=metadata), tempfile.TemporaryDirectory() as raw:
                bundle = _build_bundle(Path(raw))
                archive = bundle["archive"]
                _rewrite_archive_and_rebind(
                    bundle,
                    _archive_payload(
                        metadata_bytes=json.dumps(
                            metadata, separators=(",", ":"), sort_keys=True
                        ).encode("utf-8")
                    ),
                )
                manifest_path = _build_tile_manifest(bundle)
                result = validate_bundle(archive, manifest_path)
            self.assertEqual(
                ["TILE_MANIFEST_METADATA_VECTOR_LAYERS_INVALID"],
                [finding.code for finding in result.findings],
            )

    def test_tile_manifest_vector_layer_order_is_not_semantic(self) -> None:
        metadata = {
            "name": "synthetic-kfm-fixture",
            "spec_hash": SPEC_HASH,
            "vector_layers": [
                {"id": "alpha", "fields": {"tiles": "String"}},
                {"id": "beta", "fields": {"b": "Number"}},
            ],
        }
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            archive = bundle["archive"]
            _rewrite_archive_and_rebind(
                bundle,
                _archive_payload(
                    metadata_bytes=json.dumps(
                        metadata, separators=(",", ":"), sort_keys=True
                    ).encode("utf-8")
                ),
            )
            manifest_path = _build_tile_manifest(bundle)
            manifest = bundle["tile_manifest"]
            manifest["pmtiles"]["vector_layers"] = [
                {"id": "beta", "fields": {"b": "Number"}},
                {"id": "alpha", "fields": {"tiles": "String"}},
            ]
            _write_json(manifest_path, manifest)
            result = validate_bundle(archive, manifest_path)
        self.assertTrue(result.ok)

    def test_tile_manifest_bounds_e7_rounding_is_header_exact(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            manifest_path = _build_tile_manifest(bundle)
            manifest = bundle["tile_manifest"]
            manifest["pmtiles"]["bounds"] = [
                -102.00000001,
                37.00000001,
                -94.00000001,
                40.00000001,
            ]
            _write_json(manifest_path, manifest)
            result = validate_bundle(bundle["archive"], manifest_path)
        self.assertTrue(result.ok)

    def test_manifest_parser_reason_code_registry_is_exact(self) -> None:
        observed: set[str] = set()
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)

            missing = root / "missing.json"
            observed.update(f.code for f in _load_json(missing, "TILE_MANIFEST")[1])

            target = root / "target.json"
            target.write_text("{}\n", encoding="utf-8")
            symlink = root / "link.json"
            symlink.symlink_to(target)
            observed.update(f.code for f in _load_json(symlink, "TILE_MANIFEST")[1])

            cases = {
                "duplicate.json": '{"x":1,"x":2}\n',
                "nonfinite.json": '{"x":NaN}\n',
                "invalid.json": '{"x":\n',
                "root.json": '[]\n',
            }
            for name, content in cases.items():
                path = root / name
                path.write_text(content, encoding="utf-8")
                observed.update(f.code for f in _load_json(path, "TILE_MANIFEST")[1])

            oversized = root / "oversized.json"
            oversized.write_bytes(b" " * (MAX_JSON_BYTES + 1))
            observed.update(
                f.code for f in _load_json(oversized, "TILE_MANIFEST")[1]
            )

            unreadable = root / "unreadable.json"
            unreadable.write_text("{}\n", encoding="utf-8")
            with mock.patch.object(Path, "read_text", side_effect=OSError):
                observed.update(
                    f.code for f in _load_json(unreadable, "TILE_MANIFEST")[1]
                )

        self.assertEqual(TILE_MANIFEST_PARSER_FINDING_CODES, frozenset(observed))

    def test_brotli_metadata_is_an_explicit_compatibility_hold(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            bundle = _build_bundle(Path(raw))
            payload = bytearray(bundle["archive_bytes"])
            payload[97] = 3
            _rewrite_archive_and_rebind(bundle, bytes(payload))
            result = validate_bundle(bundle["archive"])
        self.assertEqual(
            ["METADATA_COMPRESSION_UNSUPPORTED"],
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
