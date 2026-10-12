#!/usr/bin/env python3
"""Validate the bounded synthetic PMTiles delta-manifest profile."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from datetime import datetime
from pathlib import Path
from typing import Sequence

from jsonschema import Draft202012Validator

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.validators._common.public_safe_fixture import (
    Finding,
    add_finding,
    validate_fixture_file,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/map/pmtiles_delta_manifest.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/pmtiles/delta_manifest"
SCOPE = "map.pmtiles_delta_manifest"
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
SCHEMA_VALIDATOR = Draft202012Validator(SCHEMA)
ZERO_HASH = "sha256:" + ("0" * 64)
FORBIDDEN_LIFECYCLE_FRAGMENTS = (
    "/raw/",
    "/work/",
    "/quarantine/",
    "data/raw/",
    "data/work/",
    "data/quarantine/",
)


def serialize_outcome(path: Path, findings: list[Finding]) -> str:
    payload = {
        "file": str(path),
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in sorted(findings)
        ],
        "scope": SCOPE,
        "status": "DENY" if findings else "PASS",
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def canonical_spec_hash(document: dict[str, object]) -> str:
    """Hash every declared field except spec_hash using canonical JSON."""

    identity_document = {key: value for key, value in document.items() if key != "spec_hash"}
    canonical = json.dumps(
        identity_document,
        ensure_ascii=True,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def _json_path(error_path: Sequence[object]) -> str:
    result = "$"
    for part in error_path:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.removesuffix("Z") + "+00:00")


def _quadkey(z: int, x: int, y: int) -> str:
    digits: list[str] = []
    for level in range(z, 0, -1):
        bit = 1 << (level - 1)
        digit = 0
        if x & bit:
            digit += 1
        if y & bit:
            digit += 2
        digits.append(str(digit))
    return "".join(digits)


def _close_enough(left: float, right: float) -> bool:
    return math.isclose(left, right, rel_tol=0.0, abs_tol=1e-9)


def validate_document(candidate: object) -> list[Finding]:
    """Validate shape, lineage, tile identity, counts, and declared QC."""

    findings: set[Finding] = set()
    schema_errors = sorted(
        SCHEMA_VALIDATOR.iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        add_finding(
            findings,
            "PMTILES_DELTA_MANIFEST_SCHEMA_INVALID",
            _json_path(tuple(error.absolute_path)),
        )
    if schema_errors or not isinstance(candidate, dict):
        return sorted(findings)

    if candidate["spec_hash"] == ZERO_HASH or candidate["spec_hash"] != canonical_spec_hash(candidate):
        add_finding(findings, "PMTILES_DELTA_MANIFEST_HASH_MISMATCH", "$.spec_hash")

    expected_delta_id = (
        "kfm://manifest/map/pmtiles-delta/"
        f"{candidate['layer_id'].removeprefix('kfm:')}/{candidate['valid_from'][:10]}"
    )
    if candidate["delta_id"] != expected_delta_id:
        add_finding(findings, "PMTILES_DELTA_ID_MISMATCH", "$.delta_id")

    try:
        valid_from = _parse_utc(candidate["valid_from"])
        valid_to = _parse_utc(candidate["valid_to"])
    except ValueError:
        add_finding(findings, "PMTILES_DELTA_TIME_INVALID", "$.valid_from")
    else:
        if valid_from >= valid_to:
            add_finding(findings, "PMTILES_DELTA_TIME_ORDER_INVALID", "$.valid_to")

    for archive_name in ("base_archive", "delta_archive"):
        archive = candidate[archive_name]
        digest = archive["archive_digest"]
        if digest == ZERO_HASH:
            add_finding(findings, "PMTILES_DELTA_ARCHIVE_DIGEST_PLACEHOLDER", f"$.{archive_name}.archive_digest")
        if not archive["artifact_ref"].endswith("@" + digest):
            add_finding(findings, "PMTILES_DELTA_ARTIFACT_REF_DIGEST_MISMATCH", f"$.{archive_name}.artifact_ref")
        if archive["index_digest"] == ZERO_HASH:
            add_finding(findings, "PMTILES_DELTA_INDEX_DIGEST_PLACEHOLDER", f"$.{archive_name}.index_digest")

    refs: list[tuple[str, str]] = [
        ("$.base_archive.artifact_ref", candidate["base_archive"]["artifact_ref"]),
        ("$.delta_archive.artifact_ref", candidate["delta_archive"]["artifact_ref"]),
        ("$.attestation_ref", candidate["attestation_ref"]),
    ]
    refs.extend(
        (f"$.source_manifest_refs[{index}]", value)
        for index, value in enumerate(candidate["source_manifest_refs"])
    )

    tiles = candidate["tiles"]
    ordered_keys = [(tile["z"], tile["x"], tile["y"]) for tile in tiles]
    if ordered_keys != sorted(ordered_keys):
        add_finding(findings, "PMTILES_DELTA_TILE_ORDER_INVALID", "$.tiles")
    if len(set(ordered_keys)) != len(ordered_keys):
        add_finding(findings, "PMTILES_DELTA_TILE_DUPLICATE", "$.tiles")

    additions = 0
    removals = 0
    emitted_bytes: list[int] = []
    masked_values: list[float] = []
    for index, tile in enumerate(tiles):
        path = f"$.tiles[{index}]"
        refs.append((f"{path}.run_receipt_ref", tile["run_receipt_ref"]))
        z = tile["z"]
        x = tile["x"]
        y = tile["y"]
        limit = 1 << z
        if x >= limit or y >= limit:
            add_finding(findings, "PMTILES_DELTA_TILE_COORDINATE_INVALID", path)
        if tile["tile_id"] != f"{z}/{x}/{y}":
            add_finding(findings, "PMTILES_DELTA_TILE_ID_MISMATCH", f"{path}.tile_id")
        if tile["quadkey"] != _quadkey(z, x, y):
            add_finding(findings, "PMTILES_DELTA_QUADKEY_MISMATCH", f"{path}.quadkey")

        change_type = tile["change_type"]
        digest = tile["digest"]
        prior_digest = tile["prior_digest"]
        byte_size = tile["bytes"]
        if change_type == "added":
            additions += 1
            if digest is None or prior_digest is not None or byte_size <= 0:
                add_finding(findings, "PMTILES_DELTA_ADDED_LINEAGE_INVALID", path)
        elif change_type == "modified":
            if (
                digest is None
                or prior_digest is None
                or digest == prior_digest
                or byte_size <= 0
            ):
                add_finding(findings, "PMTILES_DELTA_MODIFIED_LINEAGE_INVALID", path)
        else:
            removals += 1
            if digest is not None or prior_digest is None or byte_size != 0:
                add_finding(findings, "PMTILES_DELTA_REMOVED_LINEAGE_INVALID", path)

        for digest_name in ("digest", "prior_digest"):
            value = tile[digest_name]
            if value == ZERO_HASH:
                add_finding(findings, "PMTILES_DELTA_TILE_DIGEST_PLACEHOLDER", f"{path}.{digest_name}")

        if change_type != "removed":
            emitted_bytes.append(byte_size)
            if not _close_enough(tile["masked_pct"] + tile["coverage_pct"], 100.0):
                add_finding(findings, "PMTILES_DELTA_COVERAGE_BALANCE_INVALID", path)
        masked_values.append(float(tile["masked_pct"]))

    for path, value in refs:
        lowered = value.lower()
        if any(fragment in lowered for fragment in FORBIDDEN_LIFECYCLE_FRAGMENTS):
            add_finding(findings, "PMTILES_DELTA_INTERNAL_LIFECYCLE_REF_DENIED", path)

    expected_count = candidate["base_archive"]["tile_count"] + additions - removals
    if candidate["expected_tile_count"] != expected_count:
        add_finding(findings, "PMTILES_DELTA_EXPECTED_TILE_COUNT_MISMATCH", "$.expected_tile_count")
    if candidate["produced_tile_count"] < 0:
        add_finding(findings, "PMTILES_DELTA_PRODUCED_TILE_COUNT_INVALID", "$.produced_tile_count")

    observed_max_masked = max(masked_values, default=0.0)
    observed_average_bytes = (
        sum(emitted_bytes) / len(emitted_bytes) if emitted_bytes else 0.0
    )
    denominator = max(candidate["expected_tile_count"], 1)
    observed_deviation = (
        abs(candidate["produced_tile_count"] - candidate["expected_tile_count"])
        / denominator
        * 100.0
    )

    qc = candidate["qc"]
    thresholds = qc["thresholds"]
    observed = qc["observed"]
    if thresholds["review_masked_pct"] > thresholds["reject_masked_pct"]:
        add_finding(findings, "PMTILES_DELTA_QC_THRESHOLD_ORDER_INVALID", "$.qc.thresholds")
    if not _close_enough(float(observed["max_masked_pct"]), observed_max_masked):
        add_finding(findings, "PMTILES_DELTA_QC_MAX_MASKED_MISMATCH", "$.qc.observed.max_masked_pct")
    if not _close_enough(float(observed["average_tile_bytes"]), observed_average_bytes):
        add_finding(findings, "PMTILES_DELTA_QC_AVERAGE_BYTES_MISMATCH", "$.qc.observed.average_tile_bytes")
    if not _close_enough(float(observed["tile_count_deviation_pct"]), observed_deviation):
        add_finding(findings, "PMTILES_DELTA_QC_TILE_COUNT_DEVIATION_MISMATCH", "$.qc.observed.tile_count_deviation_pct")

    if (
        observed_max_masked > thresholds["reject_masked_pct"]
        or observed_average_bytes > thresholds["max_average_tile_bytes"]
        or observed_deviation > thresholds["max_tile_count_deviation_pct"]
    ):
        expected_decision = "REJECT"
    elif observed_max_masked > thresholds["review_masked_pct"]:
        expected_decision = "REVIEW"
    else:
        expected_decision = "PASS"
    if qc["decision"] != expected_decision:
        add_finding(findings, "PMTILES_DELTA_QC_DECISION_MISMATCH", "$.qc.decision")

    return sorted(findings)


def validate_manifest_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_document)


def _fixture_suite() -> int:
    ok = True
    for expected_valid, directory in (
        (True, FIXTURES_ROOT / "valid"),
        (False, FIXTURES_ROOT / "invalid"),
    ):
        files = sorted(directory.glob("*.json"))
        if not files:
            print(f"FAIL {directory}: no JSON fixtures found")
            ok = False
            continue
        for path in files:
            findings = validate_manifest_file(path)
            accepted = not findings
            if accepted == expected_valid:
                print(f"{'OK' if expected_valid else 'EXPECTED_FAIL'} {path}")
            else:
                print(serialize_outcome(path, findings))
                ok = False
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate synthetic PMTiles delta manifests."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(list(sys.argv[1:] if argv is None else argv))
    if args.fixtures:
        if args.files:
            print("--fixtures cannot be combined with file arguments", file=sys.stderr)
            return 2
        return _fixture_suite()
    if not args.files:
        print("at least one manifest file is required", file=sys.stderr)
        return 2

    any_findings = False
    for path in sorted(args.files, key=lambda value: str(value)):
        findings = validate_manifest_file(path)
        any_findings = any_findings or bool(findings)
        print(serialize_outcome(path, findings))
    return 1 if any_findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
