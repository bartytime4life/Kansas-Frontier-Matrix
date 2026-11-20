"""Bounded offline TIGER roads package intake; no geometry decoding or writes.

The supplied byte identity is compared with the committed source reference.
Synthetic packets deliberately do not match provider bytes. Every result stays
on HOLD because domain source admission, rights and sensitivity are unresolved.
"""
from __future__ import annotations

import argparse
import base64
import binascii
from dataclasses import asdict, dataclass, field
import io
import json
from pathlib import Path
import stat
import sys
import zipfile
import zlib

from jsonschema import Draft202012Validator, FormatChecker
from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes, timestamp, utc_time
from connectors.census.src.census import tiger_package as tiger
from tools.local_data.file_io import read_regular

ROOT = Path(__file__).resolve().parents[3]
MANIFEST = "connectors/census/tiger-line-2025-kansas-core.source-reference.json"
SCHEMA = "schemas/contracts/v1/domains/roads-rail-trade/tiger_roads_ingest_candidate.schema.json"
FIXTURE_ROOT = ROOT / "fixtures/domains/roads-rail-trade/tiger_roads_ingest"
MAX_SOURCE = 2 * 1024 * 1024
MAX_PACKET = 3 * 1024 * 1024
MAX_MEMBER = 2 * 1024 * 1024
MAX_EXPANDED = 8 * 1024 * 1024
MAX_MEMBERS = 16
BASE_REASONS = ("SOURCE_ADMISSION_UNVERIFIED", "DOMAIN_DESCRIPTOR_UNRESOLVED",
                "RIGHTS_UNVERIFIED", "SENSITIVITY_NOT_EVALUATED")
LIMITATIONS = ("GEOMETRY_NOT_DECODED", "HEADER_CRS_NOT_TRANSFORM_VERIFIED",
               "COUNTY_SCOPE_FROM_FILE_NAME", "COVERAGE_NOT_ESTABLISHED",
               "NOT_ROAD_ACCESS_OR_ROUTING_AUTHORITY")
AUTHORITIES = ("source_admitted", "review_completed", "evidence_closed", "lifecycle_write",
               "promotion_authorized", "release_authorized", "publication_authorized", "public_use_allowed")


def spec_hash(candidate: dict) -> str:
    return digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "spec_hash"}))


def _identity(candidate: dict) -> str:
    return "tiger-roads-ingest:" + digest_bytes(canonical_bytes({
        "file_name": candidate["file_name"], "artifact": candidate["artifact"]}))


def _zip_preflight(raw: bytes) -> None:
    # Inspect all members, including geometry and optional XML, for CRC/expansion
    # integrity. No member is extracted or interpreted as executable content.
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            infos = archive.infolist()
            if not 1 <= len(infos) <= MAX_MEMBERS:
                raise ValueError("TIGER_ZIP_MEMBER_COUNT")
            seen, total = set(), 0
            for info in infos:
                if (not info.filename or len(info.filename) > 120 or "/" in info.filename
                        or "\\" in info.filename or info.is_dir() or info.filename in seen
                        or stat.S_ISLNK(info.external_attr >> 16) or info.orig_filename != info.filename):
                    raise ValueError("TIGER_ZIP_MEMBER_PATH")
                seen.add(info.filename)
                if info.flag_bits & 1 or info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED):
                    raise ValueError("TIGER_ZIP_COMPRESSION")
                total += info.file_size
                if (info.file_size > MAX_MEMBER or total > MAX_EXPANDED
                        or info.file_size > max(info.compress_size, 1) * tiger.MAX_RATIO):
                    raise ValueError("TIGER_ZIP_EXPANSION_BOUND")
                actual = 0
                with archive.open(info) as stream:
                    while chunk := stream.read(64 * 1024):
                        actual += len(chunk)
                        if actual > info.file_size or actual > MAX_MEMBER:
                            raise ValueError("TIGER_ZIP_EXPANSION_BOUND")
                if actual != info.file_size:
                    raise ValueError("TIGER_ZIP_MEMBER_SIZE")
    except (zipfile.BadZipFile, EOFError, OSError, RuntimeError, NotImplementedError, zlib.error):
        raise ValueError("TIGER_ZIP_INVALID") from None


def validate_candidate(candidate: dict) -> None:
    schema = json.loads((ROOT / SCHEMA).read_text())
    if not Draft202012Validator(schema, format_checker=FormatChecker()).is_valid(candidate):
        raise ValueError("TIGER_CANDIDATE_SCHEMA_INVALID")
    if spec_hash(candidate) != candidate["spec_hash"] or _identity(candidate) != candidate["candidate_id"]:
        raise ValueError("TIGER_CANDIDATE_HASH_INVALID")
    if timestamp(utc_time(candidate["created_at"])) != candidate["created_at"]:
        raise ValueError("TIGER_CAPTURE_TIME_NONCANONICAL")
    reference, artifact, inspection = candidate["reference"], candidate["artifact"], candidate["inspection"]
    manifest_bytes = read_regular(ROOT / MANIFEST, 1024 * 1024)
    entry = tiger.manifest_entry(decode_object(manifest_bytes, limit=1024 * 1024), candidate["file_name"])
    if (reference["sha256"] != digest_bytes(manifest_bytes)
            or reference["expected_sha256"] != "sha256:" + entry["sha256"]
            or reference["expected_byte_length"] != entry["byte_length"]):
        raise ValueError("TIGER_REFERENCE_BINDING_INVALID")
    if utc_time(candidate["created_at"]).year < candidate["vintage"]:
        raise ValueError("TIGER_CAPTURE_BEFORE_VINTAGE")
    matched = (artifact["sha256"] == reference["expected_sha256"]
               and artifact["byte_length"] == reference["expected_byte_length"])
    reasons = list(BASE_REASONS) + ([] if matched else ["REFERENCE_BYTES_NOT_MATCHED"])
    reasons += inspection["reason_codes"]
    blocking = bool(inspection["reason_codes"])
    if (reference["exact_bytes_match"] != matched or candidate["reason_codes"] != reasons
            or inspection["provisional_route"] != ("QUARANTINE_CANDIDATE" if blocking else "RAW_CANDIDATE")
            or inspection["deleted_count"] > inspection["feature_count"]
            or candidate["county_fips"] != candidate["file_name"][8:13]):
        raise ValueError("TIGER_CANDIDATE_INCONSISTENT")


@dataclass(frozen=True)
class IntakeResult:
    candidate: dict = field(repr=False)

    def summary(self) -> dict:
        validate_candidate(self.candidate)
        c = self.candidate
        return {"outcome": "HOLD", "provisional_route": c["inspection"]["provisional_route"],
                "feature_count": c["inspection"]["feature_count"],
                "reference_bytes_match": c["reference"]["exact_bytes_match"],
                "reason_codes": c["reason_codes"], "result_digest": c["spec_hash"],
                **c["authority"]}


def prepare_package(raw: bytes, *, file_name: str, retrieved_at: str) -> IntakeResult:
    """Inspect one bounded, supplied Kansas county ROADS package in memory.

    This small intake profile is not the connector's full-provider size envelope.
    Hash equality is exact-byte reference conformance, never source admission.
    Header/attribute checks do not decode or validate individual road geometry.
    """
    if not isinstance(raw, bytes) or not 0 < len(raw) <= MAX_SOURCE:
        raise ValueError("TIGER_SOURCE_BYTE_BOUND")
    name = tiger.parse_file_name(file_name)
    if name.product != "ROADS" or name.vintage != 2025 or name.scope != "county" or name.scope_code[:2] != "20":
        raise ValueError("TIGER_ROADS_SCOPE")
    manifest_bytes = read_regular(ROOT / MANIFEST, 1024 * 1024)
    entry = tiger.manifest_entry(decode_object(manifest_bytes, limit=1024 * 1024), file_name)
    created_at = timestamp(utc_time(retrieved_at))
    if utc_time(created_at).year < name.vintage:
        raise ValueError("TIGER_CAPTURE_BEFORE_VINTAGE")
    _zip_preflight(raw)
    # Inspect the actual supplied bytes; compare them with the provider reference
    # separately. Never replace or rewrite the committed reference manifest.
    inspection = tiger.inspect_package(raw, file_name=file_name, entry={
        "file_name": file_name, "product": "ROADS", "byte_length": len(raw),
        "sha256": digest_bytes(raw).removeprefix("sha256:")},
        max_bytes=MAX_SOURCE, max_member_bytes=MAX_MEMBER)
    detail = asdict(inspection)
    for key in ("file_name", "product", "vintage", "scope", "package_sha256", "byte_length", "source_role", "admission"):
        detail.pop(key)
    detail["provisional_route"] = detail.pop("route")
    detail["reason_codes"] = list(detail.pop("reasons"))
    # JSON projection avoids tuple/list differences in sealed golden comparisons.
    detail = decode_object(canonical_bytes(detail), limit=MAX_PACKET)
    matched = digest_bytes(raw) == "sha256:" + entry["sha256"] and len(raw) == entry["byte_length"]
    candidate = {
        "object_type": "TigerRoadsIngestCandidate", "schema_version": "1.0.0",
        "created_at": created_at, "file_name": file_name, "vintage": 2025,
        "county_fips": name.scope_code,
        "source_descriptor_ref": "data/registry/roads-rail-trade/sources/census_tiger_roads.yaml",
        "source_role": "REFERENCE_GEOMETRY_CANDIDATE",
        "artifact": {"sha256": digest_bytes(raw), "byte_length": len(raw)},
        "reference": {"path": MANIFEST, "sha256": digest_bytes(manifest_bytes),
                      "expected_sha256": "sha256:" + entry["sha256"],
                      "expected_byte_length": entry["byte_length"], "exact_bytes_match": matched},
        "inspection": detail, "route": "HOLD",
        "reason_codes": list(BASE_REASONS) + ([] if matched else ["REFERENCE_BYTES_NOT_MATCHED"]) + list(inspection.reasons),
        "limitations": list(LIMITATIONS), "authority": {k: False for k in AUTHORITIES},
    }
    candidate["candidate_id"] = _identity(candidate)
    candidate["spec_hash"] = spec_hash(candidate)
    validate_candidate(candidate)
    return IntakeResult(candidate)


def replay_packet(raw: bytes) -> IntakeResult:
    packet = decode_object(raw, limit=MAX_PACKET)
    if (set(packet) != {"fixture_kind", "file_name", "retrieved_at", "package_base64", "package_sha256", "expected"}
            or packet["fixture_kind"] != "SYNTHETIC_TIGER_ROADS"
            or not isinstance(packet["package_base64"], str)):
        raise ValueError("TIGER_PACKET_SHAPE")
    try:
        source = base64.b64decode(packet["package_base64"], validate=True)
    except (binascii.Error, ValueError):
        raise ValueError("TIGER_PACKET_BASE64") from None
    if digest_bytes(source) != packet["package_sha256"]:
        raise ValueError("TIGER_PACKET_HASH")
    result = prepare_package(source, file_name=packet["file_name"], retrieved_at=packet["retrieved_at"])
    if canonical_bytes(result.candidate) != canonical_bytes(packet["expected"]):
        raise ValueError("TIGER_PACKET_GOLDEN_MISMATCH")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", choices=("clean", "duplicate-identity"))
    args = parser.parse_args(argv)
    try:
        result = replay_packet(read_regular(FIXTURE_ROOT / (args.fixture + ".json"), MAX_PACKET))
    except (ValueError, OSError):
        print(canonical_bytes({"outcome": "ERROR", "reason": "TIGER_FIXTURE_REPLAY_FAILED"}).decode(), file=sys.stderr)
        return 1
    print(canonical_bytes(result.summary()).decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
