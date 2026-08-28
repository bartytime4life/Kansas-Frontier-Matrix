#!/usr/bin/env python3
"""Reconcile the existing KFM PMTiles compatibility attestation bundle.

This offline validator binds one archive to its PMIDX, PMSIG, and RunReceipt
companions.  Success is structural only.  Signature verification, policy
evaluation, and release authorization are deliberately reported as holds.  An
opt-in, non-canonical TileArtifactManifest compatibility descriptor can also be
checked against the already-inspected archive and bundle.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

from validate_header import HeaderValidationError, inspect_archive
from verify_merkle import MerkleValidationError, inspect_index

MAX_JSON_BYTES = 1024 * 1024
MAX_MANIFEST_NODES = 100_000
SHA256_RE = re.compile(r"^sha256:[a-f0-9]{64}$")
GENERATION_TOOL_RE = re.compile(
    r"^[A-Za-z0-9][A-Za-z0-9._/-]*@[A-Za-z0-9][A-Za-z0-9._+-]*$"
)
DECLARED_SOURCE_REF_RE = re.compile(
    r"^(?:kfm://|urn:)[^\x00-\x20\x7f@]+@(?:v[0-9][A-Za-z0-9._+-]*|sha256:[a-f0-9]{64})$"
)
DIGEST_BOUND_ARTIFACT_REF_RE = re.compile(
    r"^(?:kfm://|urn:)[^\x00-\x20\x7f@]+@sha256:[a-f0-9]{64}$"
)
PROFILE = "kfm.pmtiles.attestation.compat.v1"
TILE_MANIFEST_PROFILE = "kfm.pmtiles.tile-artifact-manifest.compat.v1"
HOLDS = (
    "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
    "POLICY_EVALUATION_NOT_RUN",
    "RANGE_METADATA_NOT_AUTHENTICATED",
    "RELEASE_AUTHORIZATION_NOT_EVALUATED",
)
TILE_MANIFEST_HOLDS = (
    "TILE_ARTIFACT_MANIFEST_SCHEMA_AUTHORITY_UNRESOLVED",
    "TILE_MANIFEST_DECLARED_PROVENANCE_UNATTESTED",
    "TILE_MANIFEST_ARTIFACT_REF_REGISTRY_UNRESOLVED",
)
CHECKS = (
    "PMTILES_V3_HEADER_METADATA",
    "PMIDX_ARCHIVE_CHUNKS_MERKLE_RANGES",
    "PMSIG_SUBJECT_SHAPE",
    "RUNRECEIPT_SUBJECT_SHAPE",
    "CROSS_ARTIFACT_DIGEST_SPEC_HASH_ROOT",
)
TILE_MANIFEST_CHECK = "DECLARED_TILE_ARTIFACT_MANIFEST_PMTILES_MVT_PROFILE"
TILE_MANIFEST_FINDING_CODES = frozenset(
    {
        "TILE_MANIFEST_ARTIFACT_NAME_INVALID",
        "TILE_MANIFEST_ARTIFACT_NAME_MISMATCH",
        "TILE_MANIFEST_ARTIFACT_REF_DIGEST_MISMATCH",
        "TILE_MANIFEST_ARTIFACT_REF_NOT_DIGEST_BOUND",
        "TILE_MANIFEST_BOUNDS_HEADER_MISMATCH",
        "TILE_MANIFEST_BOUNDS_INVALID",
        "TILE_MANIFEST_BOUNDS_ORDER_INVALID",
        "TILE_MANIFEST_BYTE_SIZE_INVALID",
        "TILE_MANIFEST_BYTE_SIZE_MISMATCH",
        "TILE_MANIFEST_COMPLEXITY_LIMIT",
        "TILE_MANIFEST_DIGEST_INVALID",
        "TILE_MANIFEST_DIGEST_MISMATCH",
        "TILE_MANIFEST_EMBEDDED_PAYLOAD_DENIED",
        "TILE_MANIFEST_GENERATION_TOOL_INVALID",
        "TILE_MANIFEST_MAXZOOM_INVALID",
        "TILE_MANIFEST_MEDIA_TYPE_UNSUPPORTED",
        "TILE_MANIFEST_METADATA_VECTOR_LAYERS_INVALID",
        "TILE_MANIFEST_MINZOOM_INVALID",
        "TILE_MANIFEST_PMTILES_PROFILE_INVALID",
        "TILE_MANIFEST_PMTILES_VERSION_UNSUPPORTED",
        "TILE_MANIFEST_PROFILE_INVALID",
        "TILE_MANIFEST_SOURCE_REFS_INVALID",
        "TILE_MANIFEST_SPEC_HASH_INVALID",
        "TILE_MANIFEST_SPEC_HASH_MISMATCH",
        "TILE_MANIFEST_TILE_FORMAT_MISMATCH",
        "TILE_MANIFEST_TILE_FORMAT_UNSUPPORTED",
        "TILE_MANIFEST_TILING_SCHEME_METADATA_MISMATCH",
        "TILE_MANIFEST_TILING_SCHEME_UNSUPPORTED",
        "TILE_MANIFEST_UNDECLARED_FIELD",
        "TILE_MANIFEST_VECTOR_LAYERS_INVALID",
        "TILE_MANIFEST_VECTOR_LAYERS_MISMATCH",
        "TILE_MANIFEST_VECTOR_LAYER_ID_DUPLICATE",
        "TILE_MANIFEST_ZOOM_HEADER_MISMATCH",
        "TILE_MANIFEST_ZOOM_ORDER_INVALID",
    }
)
TILE_MANIFEST_PARSER_FINDING_CODES = frozenset(
    {
        "TILE_MANIFEST_JSON_DUPLICATE_KEY",
        "TILE_MANIFEST_JSON_INVALID",
        "TILE_MANIFEST_JSON_NONFINITE_NUMBER",
        "TILE_MANIFEST_JSON_TOO_LARGE",
        "TILE_MANIFEST_JSON_UNREADABLE",
        "TILE_MANIFEST_NOT_FILE",
        "TILE_MANIFEST_ROOT_INVALID",
        "TILE_MANIFEST_SYMLINK_DENIED",
    }
)
FORBIDDEN_MANIFEST_PAYLOAD_KEYS = frozenset(
    {"archive_bytes", "content_base64", "payload", "tile_data", "tiles"}
)


class _DuplicateKeyError(ValueError):
    pass


class _NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True)
class Finding:
    code: str


@dataclass(frozen=True)
class SignatureSubject:
    pmtiles_sha256: str
    pmidx_merkle_root: str
    spec_hash: str


@dataclass(frozen=True)
class ReceiptSubject:
    name: str
    pmtiles_sha256: str
    spec_hash: str


@dataclass(frozen=True)
class BundleResult:
    findings: tuple[Finding, ...]
    tile_manifest_checked: bool = False

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def status(self) -> str:
        return "STRUCTURAL_PASS" if self.ok else "DENY"


def companion_paths(archive: Path) -> tuple[Path, Path, Path]:
    """Return the compatibility names already used by the repository workflow."""

    raw = str(archive)
    return (
        Path(raw + ".pmidx"),
        Path(raw + ".pmsig"),
        Path(raw + ".runreceipt.json"),
    )


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise _DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise _NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise _NonFiniteNumberError
    return parsed


def _load_json(path: Path, prefix: str) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding(f"{prefix}_SYMLINK_DENIED")]
        if not path.is_file():
            return None, [Finding(f"{prefix}_NOT_FILE")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding(f"{prefix}_JSON_TOO_LARGE")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except _DuplicateKeyError:
        return None, [Finding(f"{prefix}_JSON_DUPLICATE_KEY")]
    except _NonFiniteNumberError:
        return None, [Finding(f"{prefix}_JSON_NONFINITE_NUMBER")]
    except (UnicodeError, json.JSONDecodeError):
        return None, [Finding(f"{prefix}_JSON_INVALID")]
    except (OSError, RecursionError, ValueError):
        return None, [Finding(f"{prefix}_JSON_UNREADABLE")]
    if not isinstance(value, dict):
        return None, [Finding(f"{prefix}_ROOT_INVALID")]
    return value, []


def _hash(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    normalized = value.lower()
    return normalized if SHA256_RE.fullmatch(normalized) else None


def _non_placeholder_hash(value: object) -> str | None:
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        return None
    if value == "sha256:" + ("0" * 64):
        return None
    return value


def _is_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _payload_scan_finding(value: object) -> Finding | None:
    stack: list[tuple[object, bool]] = [(value, False)]
    visited = 0
    while stack:
        current, is_vector_field_map = stack.pop()
        visited += 1
        if visited > MAX_MANIFEST_NODES:
            return Finding("TILE_MANIFEST_COMPLEXITY_LIMIT")
        if isinstance(current, dict):
            if not is_vector_field_map and any(
                key in FORBIDDEN_MANIFEST_PAYLOAD_KEYS for key in current
            ):
                return Finding("TILE_MANIFEST_EMBEDDED_PAYLOAD_DENIED")
            stack.extend(
                (item, key == "fields") for key, item in current.items()
            )
        elif isinstance(current, list):
            stack.extend((item, False) for item in current)
    return None


def _declared_source_refs(value: object) -> bool:
    return (
        isinstance(value, list)
        and 1 <= len(value) <= 100
        and all(
            isinstance(item, str)
            and item.isascii()
            and DECLARED_SOURCE_REF_RE.fullmatch(item)
            for item in value
        )
        and len(set(value)) == len(value)
    )


def _vector_layers(
    value: object,
) -> tuple[dict[str, dict[str, str]] | None, list[Finding]]:
    if not isinstance(value, list) or not value or len(value) > 1_000:
        return None, [Finding("TILE_MANIFEST_VECTOR_LAYERS_INVALID")]
    layers: dict[str, dict[str, str]] = {}
    for layer in value:
        if not isinstance(layer, dict) or set(layer) != {"id", "fields"}:
            return None, [Finding("TILE_MANIFEST_VECTOR_LAYERS_INVALID")]
        layer_id = layer.get("id")
        fields = layer.get("fields")
        if (
            not isinstance(layer_id, str)
            or not layer_id
            or len(layer_id) > 255
            or not isinstance(fields, dict)
            or len(fields) > 10_000
            or not all(
                isinstance(key, str)
                and key
                and len(key) <= 255
                and isinstance(item, str)
                and item
                and len(item) <= 255
                for key, item in fields.items()
            )
        ):
            return None, [Finding("TILE_MANIFEST_VECTOR_LAYERS_INVALID")]
        if layer_id in layers:
            return None, [Finding("TILE_MANIFEST_VECTOR_LAYER_ID_DUPLICATE")]
        layers[layer_id] = fields
    return layers, []


def _metadata_vector_layers(value: object) -> dict[str, dict[str, str]] | None:
    if not isinstance(value, list) or not value:
        return None
    layers: dict[str, dict[str, str]] = {}
    for layer in value:
        if not isinstance(layer, dict):
            return None
        layer_id = layer.get("id")
        fields = layer.get("fields")
        if (
            not isinstance(layer_id, str)
            or not layer_id
            or not isinstance(fields, dict)
            or len(fields) > 10_000
            or not all(
                isinstance(key, str)
                and key
                and len(key) <= 255
                and isinstance(item, str)
                and item
                and len(item) <= 255
                for key, item in fields.items()
            )
            or layer_id in layers
        ):
            return None
        layers[layer_id] = fields
    return layers


def _finite_number(value: object) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    try:
        normalized = float(value)
    except (OverflowError, ValueError):
        return None
    return normalized if math.isfinite(normalized) else None


def _validate_tile_manifest(
    value: dict[str, object], archive: Path, archive_info: object, index_info: object
) -> list[Finding]:
    """Validate a declared PMTiles/MVT profile without defining schema authority."""

    findings: list[Finding] = []
    allowed = {
        "profile",
        "artifact_name",
        "artifact_ref",
        "media_type",
        "digest",
        "byte_size",
        "spec_hash",
        "source_manifest_refs",
        "generation_tool",
        "pmtiles",
    }
    payload_scan_finding = _payload_scan_finding(value)
    if payload_scan_finding is not None:
        findings.append(payload_scan_finding)
    elif set(value) - allowed:
        findings.append(Finding("TILE_MANIFEST_UNDECLARED_FIELD"))

    if value.get("profile") != TILE_MANIFEST_PROFILE:
        findings.append(Finding("TILE_MANIFEST_PROFILE_INVALID"))

    artifact_name = value.get("artifact_name")
    if (
        not isinstance(artifact_name, str)
        or not artifact_name
        or "\\" in artifact_name
        or PurePosixPath(artifact_name).name != artifact_name
        or not artifact_name.endswith(".pmtiles")
    ):
        findings.append(Finding("TILE_MANIFEST_ARTIFACT_NAME_INVALID"))
    elif artifact_name != archive.name:
        findings.append(Finding("TILE_MANIFEST_ARTIFACT_NAME_MISMATCH"))

    artifact_ref = value.get("artifact_ref")
    if (
        not isinstance(artifact_ref, str)
        or not artifact_ref.isascii()
        or not DIGEST_BOUND_ARTIFACT_REF_RE.fullmatch(artifact_ref)
    ):
        findings.append(Finding("TILE_MANIFEST_ARTIFACT_REF_NOT_DIGEST_BOUND"))

    if value.get("media_type") != "application/vnd.pmtiles":
        findings.append(Finding("TILE_MANIFEST_MEDIA_TYPE_UNSUPPORTED"))

    digest = _non_placeholder_hash(value.get("digest"))
    if digest is None:
        findings.append(Finding("TILE_MANIFEST_DIGEST_INVALID"))
    else:
        if index_info is not None and digest != index_info.pmtiles_sha256:
            findings.append(Finding("TILE_MANIFEST_DIGEST_MISMATCH"))
        if (
            isinstance(artifact_ref, str)
            and artifact_ref.isascii()
            and DIGEST_BOUND_ARTIFACT_REF_RE.fullmatch(artifact_ref)
            and not artifact_ref.endswith("@" + digest)
        ):
            findings.append(Finding("TILE_MANIFEST_ARTIFACT_REF_DIGEST_MISMATCH"))

    byte_size = value.get("byte_size")
    if not _is_integer(byte_size) or byte_size < 127:
        findings.append(Finding("TILE_MANIFEST_BYTE_SIZE_INVALID"))
    elif archive_info is not None and byte_size != archive_info.archive_bytes:
        findings.append(Finding("TILE_MANIFEST_BYTE_SIZE_MISMATCH"))

    spec_hash = _non_placeholder_hash(value.get("spec_hash"))
    if spec_hash is None:
        findings.append(Finding("TILE_MANIFEST_SPEC_HASH_INVALID"))
    elif archive_info is not None and spec_hash != archive_info.spec_hash:
        findings.append(Finding("TILE_MANIFEST_SPEC_HASH_MISMATCH"))

    if not _declared_source_refs(value.get("source_manifest_refs")):
        findings.append(Finding("TILE_MANIFEST_SOURCE_REFS_INVALID"))
    generation_tool = value.get("generation_tool")
    if not isinstance(generation_tool, str) or not GENERATION_TOOL_RE.fullmatch(
        generation_tool
    ):
        findings.append(Finding("TILE_MANIFEST_GENERATION_TOOL_INVALID"))

    pmtiles = value.get("pmtiles")
    if not isinstance(pmtiles, dict):
        return findings + [Finding("TILE_MANIFEST_PMTILES_PROFILE_INVALID")]
    expected_pmtiles_fields = {
        "pmtiles_version",
        "tile_format",
        "tiling_scheme",
        "minzoom",
        "maxzoom",
        "bounds",
        "vector_layers",
    }
    if set(pmtiles) != expected_pmtiles_fields:
        return findings + [Finding("TILE_MANIFEST_PMTILES_PROFILE_INVALID")]

    version = pmtiles.get("pmtiles_version")
    if version != "v3":
        findings.append(Finding("TILE_MANIFEST_PMTILES_VERSION_UNSUPPORTED"))

    tile_format = pmtiles.get("tile_format")
    if tile_format != "mvt":
        findings.append(Finding("TILE_MANIFEST_TILE_FORMAT_UNSUPPORTED"))
    elif archive_info is not None and archive_info.header.tile_type != 1:
        findings.append(Finding("TILE_MANIFEST_TILE_FORMAT_MISMATCH"))

    tiling_scheme = pmtiles.get("tiling_scheme")
    if tiling_scheme != "xyz":
        findings.append(Finding("TILE_MANIFEST_TILING_SCHEME_UNSUPPORTED"))
    elif archive_info is not None:
        metadata_scheme = archive_info.metadata.get("scheme", "xyz")
        if metadata_scheme != tiling_scheme:
            findings.append(
                Finding("TILE_MANIFEST_TILING_SCHEME_METADATA_MISMATCH")
            )

    minzoom = pmtiles.get("minzoom")
    maxzoom = pmtiles.get("maxzoom")
    zoom_valid = True
    if not _is_integer(minzoom) or not 0 <= minzoom <= 255:
        findings.append(Finding("TILE_MANIFEST_MINZOOM_INVALID"))
        zoom_valid = False
    if not _is_integer(maxzoom) or not 0 <= maxzoom <= 255:
        findings.append(Finding("TILE_MANIFEST_MAXZOOM_INVALID"))
        zoom_valid = False
    if zoom_valid and minzoom > maxzoom:
        findings.append(Finding("TILE_MANIFEST_ZOOM_ORDER_INVALID"))
        zoom_valid = False
    if zoom_valid and archive_info is not None and (
        minzoom != archive_info.header.min_zoom
        or maxzoom != archive_info.header.max_zoom
    ):
        findings.append(Finding("TILE_MANIFEST_ZOOM_HEADER_MISMATCH"))

    bounds = pmtiles.get("bounds")
    bounds_e7: list[int] | None = None
    if (
        not isinstance(bounds, list)
        or len(bounds) != 4
        or any(_finite_number(item) is None for item in bounds)
    ):
        findings.append(Finding("TILE_MANIFEST_BOUNDS_INVALID"))
    else:
        normalized_bounds = [_finite_number(item) for item in bounds]
        assert all(item is not None for item in normalized_bounds)
        west, south, east, north = (float(item) for item in normalized_bounds)
        if not (
            -180 <= west < east <= 180
            and -85.051129 <= south < north <= 85.051129
        ):
            findings.append(Finding("TILE_MANIFEST_BOUNDS_ORDER_INVALID"))
        else:
            bounds_e7 = [
                round(item * 10_000_000) for item in (west, south, east, north)
            ]
    if bounds_e7 is not None and archive_info is not None and bounds_e7 != [
        archive_info.header.min_lon_e7,
        archive_info.header.min_lat_e7,
        archive_info.header.max_lon_e7,
        archive_info.header.max_lat_e7,
    ]:
        findings.append(Finding("TILE_MANIFEST_BOUNDS_HEADER_MISMATCH"))

    vector_layers, vector_findings = _vector_layers(pmtiles.get("vector_layers"))
    findings.extend(vector_findings)
    if vector_layers is not None and archive_info is not None:
        metadata_layers = _metadata_vector_layers(
            archive_info.metadata.get("vector_layers")
        )
        if metadata_layers is None:
            findings.append(Finding("TILE_MANIFEST_METADATA_VECTOR_LAYERS_INVALID"))
        elif vector_layers != metadata_layers:
            findings.append(Finding("TILE_MANIFEST_VECTOR_LAYERS_MISMATCH"))
    return findings


def _signature_subject(
    value: dict[str, object],
) -> tuple[SignatureSubject | None, list[Finding]]:
    findings: list[Finding] = []
    if value.get("schema_version") != "kfm.pmsig.v1":
        findings.append(Finding("PMSIG_SCHEMA_VERSION_INVALID"))
    subject = value.get("subject")
    if not isinstance(subject, dict):
        return None, findings + [Finding("PMSIG_SUBJECT_INVALID")]
    archive_digest = _hash(subject.get("pmtiles_sha256"))
    root = _hash(subject.get("pmidx_merkle_root"))
    spec_hash = _hash(subject.get("spec_hash"))
    if archive_digest is None:
        findings.append(Finding("PMSIG_ARCHIVE_DIGEST_INVALID"))
    if root is None:
        findings.append(Finding("PMSIG_MERKLE_ROOT_INVALID"))
    if spec_hash is None:
        findings.append(Finding("PMSIG_SPEC_HASH_INVALID"))
    if not isinstance(value.get("key_id"), str) or not value.get("key_id"):
        findings.append(Finding("PMSIG_KEY_ID_INVALID"))
    if not isinstance(value.get("signature"), str) or not value.get("signature"):
        findings.append(Finding("PMSIG_SIGNATURE_SHAPE_INVALID"))
    if archive_digest is None or root is None or spec_hash is None:
        return None, findings
    return SignatureSubject(archive_digest, root, spec_hash), findings


def _receipt_subject(
    value: dict[str, object],
) -> tuple[ReceiptSubject | None, list[Finding]]:
    findings: list[Finding] = []
    if value.get("schema_version") != "kfm.runreceipt.pmtiles.v1":
        findings.append(Finding("RUNRECEIPT_SCHEMA_VERSION_INVALID"))
    if value.get("type") != "https://slsa.dev/provenance/v1":
        findings.append(Finding("RUNRECEIPT_TYPE_INVALID"))
    subjects = value.get("subject")
    if not isinstance(subjects, list) or len(subjects) != 1:
        return None, findings + [Finding("RUNRECEIPT_SUBJECT_INVALID")]
    subject = subjects[0]
    if not isinstance(subject, dict):
        return None, findings + [Finding("RUNRECEIPT_SUBJECT_INVALID")]
    name = subject.get("name")
    digest = subject.get("digest")
    raw_digest = digest.get("sha256") if isinstance(digest, dict) else None
    if isinstance(raw_digest, str) and not raw_digest.startswith("sha256:"):
        raw_digest = "sha256:" + raw_digest
    archive_digest = _hash(raw_digest)

    predicate = value.get("predicate")
    definition = predicate.get("buildDefinition") if isinstance(predicate, dict) else None
    build_type = definition.get("buildType") if isinstance(definition, dict) else None
    parameters = (
        definition.get("externalParameters") if isinstance(definition, dict) else None
    )
    spec_hash = _hash(
        parameters.get("spec_hash") if isinstance(parameters, dict) else None
    )
    run_details = predicate.get("runDetails") if isinstance(predicate, dict) else None
    builder = run_details.get("builder") if isinstance(run_details, dict) else None

    if not isinstance(name, str) or not name or "\\" in name:
        findings.append(Finding("RUNRECEIPT_SUBJECT_NAME_INVALID"))
    if archive_digest is None:
        findings.append(Finding("RUNRECEIPT_ARCHIVE_DIGEST_INVALID"))
    if build_type != "kfm/pmtiles/build@v1":
        findings.append(Finding("RUNRECEIPT_BUILD_TYPE_INVALID"))
    if spec_hash is None:
        findings.append(Finding("RUNRECEIPT_SPEC_HASH_INVALID"))
    if (
        not isinstance(builder, dict)
        or not isinstance(builder.get("id"), str)
        or not builder.get("id")
    ):
        findings.append(Finding("RUNRECEIPT_BUILDER_INVALID"))
    if not isinstance(name, str) or archive_digest is None or spec_hash is None:
        return None, findings
    return ReceiptSubject(name, archive_digest, spec_hash), findings


def _name_matches_archive(name: str, archive: Path) -> bool:
    path = PurePosixPath(name)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        return False
    return path.name == archive.name


def validate_bundle(archive: Path, tile_manifest: Path | None = None) -> BundleResult:
    """Reconcile one split bundle without granting cryptographic or release trust."""

    findings: list[Finding] = []
    archive_info = None
    index_info = None
    try:
        archive_info = inspect_archive(archive)
    except HeaderValidationError as exc:
        findings.append(Finding(exc.code))

    pmidx_path, pmsig_path, receipt_path = companion_paths(archive)
    try:
        index_info = inspect_index(pmidx_path, archive)
    except MerkleValidationError as exc:
        findings.append(Finding(exc.code))

    pmsig, pmsig_load_findings = _load_json(pmsig_path, "PMSIG")
    findings.extend(pmsig_load_findings)
    signature = None
    if pmsig is not None:
        signature, signature_findings = _signature_subject(pmsig)
        findings.extend(signature_findings)

    receipt, receipt_load_findings = _load_json(receipt_path, "RUNRECEIPT")
    findings.extend(receipt_load_findings)
    receipt_subject = None
    if receipt is not None:
        receipt_subject, receipt_findings = _receipt_subject(receipt)
        findings.extend(receipt_findings)

    if archive_info is not None and index_info is not None:
        if archive_info.spec_hash != index_info.spec_hash:
            findings.append(Finding("PMTILES_PMIDX_SPEC_HASH_MISMATCH"))
    if signature is not None and index_info is not None:
        if signature.pmtiles_sha256 != index_info.pmtiles_sha256:
            findings.append(Finding("PMSIG_ARCHIVE_DIGEST_MISMATCH"))
        if signature.pmidx_merkle_root != index_info.merkle_root:
            findings.append(Finding("PMSIG_MERKLE_ROOT_MISMATCH"))
        if signature.spec_hash != index_info.spec_hash:
            findings.append(Finding("PMSIG_SPEC_HASH_MISMATCH"))
    if receipt_subject is not None and index_info is not None:
        if receipt_subject.pmtiles_sha256 != index_info.pmtiles_sha256:
            findings.append(Finding("RUNRECEIPT_ARCHIVE_DIGEST_MISMATCH"))
        if receipt_subject.spec_hash != index_info.spec_hash:
            findings.append(Finding("RUNRECEIPT_SPEC_HASH_MISMATCH"))
        if not _name_matches_archive(receipt_subject.name, archive):
            findings.append(Finding("RUNRECEIPT_SUBJECT_NAME_MISMATCH"))

    if tile_manifest is not None:
        manifest, manifest_load_findings = _load_json(tile_manifest, "TILE_MANIFEST")
        findings.extend(manifest_load_findings)
        if manifest is not None:
            findings.extend(
                _validate_tile_manifest(manifest, archive, archive_info, index_info)
            )

    return BundleResult(
        tuple(sorted(set(findings), key=lambda item: item.code)),
        tile_manifest_checked=tile_manifest is not None,
    )


def render_result(result: BundleResult) -> str:
    """Render bounded machine output containing codes, never candidate values."""

    return json.dumps(
        {
            "authority": "NONE",
            "checks": list(CHECKS)
            + ([TILE_MANIFEST_CHECK] if result.tile_manifest_checked else []),
            "holds": list(HOLDS)
            + (list(TILE_MANIFEST_HOLDS) if result.tile_manifest_checked else []),
            "issues": [{"code": finding.code} for finding in result.findings],
            "profile": PROFILE,
            "status": result.status,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pmtiles", type=Path)
    parser.add_argument(
        "--tile-manifest",
        type=Path,
        help="opt-in non-canonical PMTiles/MVT TileArtifactManifest descriptor",
    )
    args = parser.parse_args()
    try:
        result = validate_bundle(args.pmtiles, args.tile_manifest)
    except Exception:  # fail closed without echoing attacker-controlled values
        print(
            json.dumps(
                {
                    "authority": "NONE",
                    "holds": list(HOLDS)
                    + (list(TILE_MANIFEST_HOLDS) if args.tile_manifest else []),
                    "issues": [{"code": "INTERNAL_VALIDATOR_ERROR"}],
                    "profile": PROFILE,
                    "status": "ERROR",
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 2
    print(render_result(result))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
