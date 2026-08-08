#!/usr/bin/env python3
"""Validate the synthetic mobile PMTiles verify/decode/render fixture packet.

The validator reuses the repository's bounded PMTiles v3 header and PMIDX
integrity inspectors, then checks the fixture-only signature subject,
RunReceipt subject, tile range/digest, device envelope, budgets, explicit
holds, and all-false authority posture.

Success proves only deterministic synthetic fixture integrity. It does not
perform cryptographic signature verification, load MapLibre, admit a source,
resolve evidence or policy, authorize release, or publish.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import copy
import hashlib
import json
import math
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

VALIDATOR_DIR = Path(__file__).resolve().parent
REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VALIDATOR_DIR))

from validate_header import HeaderValidationError, inspect_archive
from verify_merkle import MerkleValidationError, inspect_index

FIXTURE_PATH = REPO_ROOT / "fixtures/pmtiles/mobile_verification/cases.json"
PROFILE = "kfm.pmtiles.mobile-verification-fixtures.v1"
BUNDLE_PROFILE = "kfm.pmtiles.mobile-verification-fixture.v1"
MAX_FIXTURE_BYTES = 1024 * 1024
MAX_ARCHIVE_BYTES = 1024 * 1024
SHA256_PREFIX = "sha256:"
ZERO_HASH = SHA256_PREFIX + ("0" * 64)
EXPECTED_HOLDS = frozenset(
    {
        "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
        "MAPLIBRE_RUNTIME_UNADMITTED",
        "RELEASE_AUTHORIZATION_NOT_EVALUATED",
    }
)
AUTHORITY_FIELDS = frozenset(
    {
        "source_admission",
        "evidence",
        "policy",
        "promotion",
        "release",
        "deployment",
        "publication",
        "public_use",
    }
)


class _DuplicateKeyError(ValueError):
    pass


class _NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise _DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise _NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise _NonFiniteNumberError
    return parsed


def _load_json(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("MOBILE_PMTILES_FIXTURE_SYMLINK_DENIED")]
        if not path.is_file():
            return None, [Finding("MOBILE_PMTILES_FIXTURE_NOT_FILE")]
        if path.stat().st_size > MAX_FIXTURE_BYTES:
            return None, [Finding("MOBILE_PMTILES_FIXTURE_TOO_LARGE")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except _DuplicateKeyError:
        return None, [Finding("MOBILE_PMTILES_FIXTURE_DUPLICATE_KEY")]
    except _NonFiniteNumberError:
        return None, [Finding("MOBILE_PMTILES_FIXTURE_NONFINITE_NUMBER")]
    except (UnicodeError, json.JSONDecodeError):
        return None, [Finding("MOBILE_PMTILES_FIXTURE_JSON_INVALID")]
    except (OSError, RecursionError, ValueError):
        return None, [Finding("MOBILE_PMTILES_FIXTURE_UNREADABLE")]
    if not isinstance(value, dict):
        return None, [Finding("MOBILE_PMTILES_FIXTURE_ROOT_INVALID")]
    return value, []


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")


def _sha256(value: bytes) -> str:
    return SHA256_PREFIX + hashlib.sha256(value).hexdigest()


def _valid_hash(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == len(SHA256_PREFIX) + 64
        and value.startswith(SHA256_PREFIX)
        and all(character in "0123456789abcdef" for character in value[7:])
        and value != ZERO_HASH
    )


def _decode_archive(value: object) -> tuple[bytes | None, list[Finding]]:
    if not isinstance(value, str):
        return None, [Finding("MOBILE_PMTILES_ARCHIVE_BASE64_INVALID")]
    try:
        decoded = base64.b64decode(value, validate=True)
    except (binascii.Error, ValueError):
        return None, [Finding("MOBILE_PMTILES_ARCHIVE_BASE64_INVALID")]
    if not 127 <= len(decoded) <= MAX_ARCHIVE_BYTES:
        return None, [Finding("MOBILE_PMTILES_ARCHIVE_SIZE_INVALID")]
    return decoded, []


def _single_subject_digest(
    receipt: object, archive_name: str
) -> tuple[str | None, str | None]:
    if not isinstance(receipt, dict):
        return None, None
    if receipt.get("schema_version") != "kfm.runreceipt.pmtiles.v1":
        return None, None
    subject = receipt.get("subject")
    predicate = receipt.get("predicate")
    if not isinstance(subject, list) or len(subject) != 1:
        return None, None
    item = subject[0]
    if not isinstance(item, dict) or item.get("name") != archive_name:
        return None, None
    digest = item.get("digest")
    if not isinstance(digest, dict) or set(digest) != {"sha256"}:
        return None, None
    raw_digest = digest.get("sha256")
    if not isinstance(raw_digest, str) or len(raw_digest) != 64:
        return None, None
    if not isinstance(predicate, dict):
        return None, None
    build_definition = predicate.get("buildDefinition")
    if not isinstance(build_definition, dict):
        return None, None
    external_parameters = build_definition.get("externalParameters")
    if not isinstance(external_parameters, dict):
        return None, None
    spec_hash = external_parameters.get("spec_hash")
    return SHA256_PREFIX + raw_digest, spec_hash if isinstance(spec_hash, str) else None


def _validate_common_shape(bundle: dict[str, object]) -> list[Finding]:
    findings: set[Finding] = set()

    if bundle.get("profile") != BUNDLE_PROFILE:
        findings.add(Finding("MOBILE_PMTILES_PROFILE_INVALID"))
    archive_name = bundle.get("archive_name")
    if archive_name != "mobile-base.pmtiles":
        findings.add(Finding("MOBILE_PMTILES_ARCHIVE_NAME_INVALID"))

    mobile = bundle.get("mobile_profile")
    if not isinstance(mobile, dict) or set(mobile) != {
        "viewport_width",
        "viewport_height",
        "device_scale_factor",
        "has_touch",
        "is_mobile",
    }:
        findings.add(Finding("MOBILE_PMTILES_DEVICE_PROFILE_INVALID"))
    else:
        integer_fields = ("viewport_width", "viewport_height", "device_scale_factor")
        if any(
            isinstance(mobile.get(field), bool)
            or not isinstance(mobile.get(field), int)
            or int(mobile[field]) <= 0
            for field in integer_fields
        ):
            findings.add(Finding("MOBILE_PMTILES_DEVICE_PROFILE_INVALID"))
        if mobile.get("has_touch") is not True or mobile.get("is_mobile") is not True:
            findings.add(Finding("MOBILE_PMTILES_DEVICE_PROFILE_INVALID"))

    budgets = bundle.get("budgets")
    if not isinstance(budgets, dict) or set(budgets) != {
        "max_archive_bytes",
        "max_tile_bytes",
        "max_verify_ms",
        "max_decode_render_ms",
    }:
        findings.add(Finding("MOBILE_PMTILES_BUDGET_INVALID"))
    elif any(
        isinstance(value, bool)
        or not isinstance(value, int)
        or value <= 0
        for value in budgets.values()
    ):
        findings.add(Finding("MOBILE_PMTILES_BUDGET_INVALID"))

    holds = bundle.get("holds")
    if (
        not isinstance(holds, list)
        or len(holds) != len(set(holds))
        or frozenset(holds) != EXPECTED_HOLDS
    ):
        findings.add(Finding("MOBILE_PMTILES_HOLDS_INVALID"))

    if (
        bundle.get("maplibre_boot_state") != "HOLD"
        or bundle.get("maplibre_boot_reason") != "MAPLIBRE_RUNTIME_UNADMITTED"
    ):
        findings.add(Finding("MOBILE_PMTILES_MAPLIBRE_AUTHORITY_OVERCLAIM"))

    authority = bundle.get("authority")
    if not isinstance(authority, dict) or set(authority) != AUTHORITY_FIELDS:
        findings.add(Finding("MOBILE_PMTILES_AUTHORITY_INVALID"))
    elif any(value is not False for value in authority.values()):
        findings.add(Finding("MOBILE_PMTILES_AUTHORITY_OVERCLAIM"))

    pixel = bundle.get("expected_pixel_rgba")
    if (
        not isinstance(pixel, list)
        or len(pixel) != 4
        or any(
            isinstance(value, bool)
            or not isinstance(value, int)
            or not 0 <= value <= 255
            for value in pixel
        )
    ):
        findings.add(Finding("MOBILE_PMTILES_PIXEL_EXPECTATION_INVALID"))

    return sorted(findings)


def validate_bundle(bundle: object) -> list[Finding]:
    if not isinstance(bundle, dict):
        return [Finding("MOBILE_PMTILES_BUNDLE_INVALID")]

    findings: set[Finding] = set(_validate_common_shape(bundle))
    archive, archive_findings = _decode_archive(bundle.get("archive_base64"))
    findings.update(archive_findings)
    if archive is None:
        return sorted(findings)

    archive_name = bundle.get("archive_name")
    if not isinstance(archive_name, str):
        return sorted(findings | {Finding("MOBILE_PMTILES_ARCHIVE_NAME_INVALID")})

    pmidx = bundle.get("pmidx")
    pmsig = bundle.get("pmsig")
    runreceipt = bundle.get("runreceipt")
    sidecar_digests = bundle.get("sidecar_digests")
    if not isinstance(pmidx, dict):
        findings.add(Finding("MOBILE_PMTILES_PMIDX_INVALID"))
    if not isinstance(pmsig, dict):
        findings.add(Finding("MOBILE_PMTILES_PMSIG_INVALID"))
    if not isinstance(runreceipt, dict):
        findings.add(Finding("MOBILE_PMTILES_RUNRECEIPT_INVALID"))
    if (
        not isinstance(sidecar_digests, dict)
        or set(sidecar_digests)
        != {"pmidx_sha256", "pmsig_sha256", "runreceipt_sha256"}
        or not all(_valid_hash(value) for value in sidecar_digests.values())
    ):
        findings.add(Finding("MOBILE_PMTILES_SIDECAR_DIGESTS_INVALID"))

    if not isinstance(pmidx, dict) or not isinstance(pmsig, dict) or not isinstance(
        runreceipt, dict
    ):
        return sorted(findings)

    if isinstance(sidecar_digests, dict):
        for name, value in (
            ("pmidx_sha256", pmidx),
            ("pmsig_sha256", pmsig),
            ("runreceipt_sha256", runreceipt),
        ):
            if sidecar_digests.get(name) != _sha256(_canonical_bytes(value)):
                findings.add(Finding("MOBILE_PMTILES_SIDECAR_DIGEST_MISMATCH"))

    with tempfile.TemporaryDirectory() as temp_dir:
        directory = Path(temp_dir)
        archive_path = directory / archive_name
        pmidx_path = Path(str(archive_path) + ".pmidx")
        archive_path.write_bytes(archive)
        pmidx_path.write_bytes(_canonical_bytes(pmidx))

        try:
            archive_info = inspect_archive(archive_path)
        except HeaderValidationError:
            findings.add(Finding("MOBILE_PMTILES_HEADER_INVALID"))
            return sorted(findings)

        try:
            index_info = inspect_index(pmidx_path, archive_path)
        except MerkleValidationError as exc:
            mapping = {
                "PMIDX_ARCHIVE_DIGEST_MISMATCH":
                    "MOBILE_PMTILES_ARCHIVE_DIGEST_MISMATCH",
                "PMIDX_MERKLE_ROOT_MISMATCH":
                    "MOBILE_PMTILES_MERKLE_ROOT_MISMATCH",
                "PMIDX_RANGE_OUT_OF_BOUNDS":
                    "MOBILE_PMTILES_RANGE_OUT_OF_BOUNDS",
                "PMIDX_RANGE_LEAF_BINDING_INVALID":
                    "MOBILE_PMTILES_RANGE_LEAF_BINDING_INVALID",
            }
            findings.add(Finding(mapping.get(exc.code, "MOBILE_PMTILES_PMIDX_INVALID")))
            return sorted(findings)

    if archive_info.spec_hash != index_info.spec_hash:
        findings.add(Finding("MOBILE_PMTILES_SPEC_HASH_MISMATCH"))

    ranges = pmidx.get("ranges")
    if not isinstance(ranges, list) or len(ranges) != 1:
        findings.add(Finding("MOBILE_PMTILES_TILE_RANGE_INVALID"))
    else:
        tile = ranges[0]
        if not isinstance(tile, dict):
            findings.add(Finding("MOBILE_PMTILES_TILE_RANGE_INVALID"))
        else:
            required = {
                "tile_id",
                "offset",
                "length",
                "leaf",
                "sha256",
                "media_type",
            }
            if not required.issubset(tile):
                findings.add(Finding("MOBILE_PMTILES_TILE_RANGE_INVALID"))
            else:
                offset = tile.get("offset")
                length = tile.get("length")
                if (
                    isinstance(offset, bool)
                    or not isinstance(offset, int)
                    or isinstance(length, bool)
                    or not isinstance(length, int)
                    or offset < 0
                    or length <= 0
                    or offset + length > len(archive)
                ):
                    findings.add(Finding("MOBILE_PMTILES_RANGE_OUT_OF_BOUNDS"))
                else:
                    tile_bytes = archive[offset:offset + length]
                    if tile.get("sha256") != _sha256(tile_bytes):
                        findings.add(Finding("MOBILE_PMTILES_TILE_DIGEST_MISMATCH"))
                    if tile.get("tile_id") != "0/0/0":
                        findings.add(Finding("MOBILE_PMTILES_TILE_ID_INVALID"))
                    if tile.get("media_type") != "image/png":
                        findings.add(Finding("MOBILE_PMTILES_TILE_MEDIA_TYPE_INVALID"))
                    if not tile_bytes.startswith(b"\x89PNG\r\n\x1a\n"):
                        findings.add(Finding("MOBILE_PMTILES_TILE_PAYLOAD_INVALID"))

                    budgets = bundle.get("budgets")
                    if isinstance(budgets, dict):
                        if len(archive) > budgets.get("max_archive_bytes", 0):
                            findings.add(Finding("MOBILE_PMTILES_ARCHIVE_BUDGET_EXCEEDED"))
                        if length > budgets.get("max_tile_bytes", 0):
                            findings.add(Finding("MOBILE_PMTILES_TILE_BUDGET_EXCEEDED"))

    subject = pmsig.get("subject")
    if (
        pmsig.get("schema_version") != "kfm.pmsig.v1"
        or not isinstance(subject, dict)
        or subject.get("pmtiles_sha256") != index_info.pmtiles_sha256
        or subject.get("pmidx_merkle_root") != index_info.merkle_root
        or subject.get("spec_hash") != index_info.spec_hash
    ):
        findings.add(Finding("MOBILE_PMTILES_SIGNATURE_SUBJECT_MISMATCH"))
    if (
        pmsig.get("key_id") != "TEST_ONLY_UNAPPROVED_KEY"
        or pmsig.get("signature")
        != "DEVELOPMENT_PLACEHOLDER_NOT_A_VALID_COSE_SIGNATURE"
    ):
        findings.add(Finding("MOBILE_PMTILES_SIGNATURE_HOLD_INVALID"))

    receipt_digest, receipt_spec_hash = _single_subject_digest(
        runreceipt, archive_name
    )
    if (
        receipt_digest != index_info.pmtiles_sha256
        or receipt_spec_hash != index_info.spec_hash
    ):
        findings.add(Finding("MOBILE_PMTILES_RUNRECEIPT_SUBJECT_MISMATCH"))

    return sorted(findings)


def _rebind_sidecar_digest(bundle: dict[str, object], name: str) -> None:
    sidecar_digests = bundle["sidecar_digests"]
    assert isinstance(sidecar_digests, dict)
    value = bundle[name]
    sidecar_digests[f"{name}_sha256"] = _sha256(_canonical_bytes(value))


def apply_mutation(base: dict[str, object], mutation: str) -> dict[str, object]:
    bundle = copy.deepcopy(base)
    if mutation == "NONE":
        return bundle
    if mutation == "ARCHIVE_BYTE_FLIP":
        archive = bytearray(base64.b64decode(bundle["archive_base64"], validate=True))
        archive[-1] ^= 0x01
        bundle["archive_base64"] = base64.b64encode(bytes(archive)).decode("ascii")
        return bundle

    pmidx = bundle["pmidx"]
    pmsig = bundle["pmsig"]
    assert isinstance(pmidx, dict) and isinstance(pmsig, dict)

    if mutation == "PMIDX_ROOT_MISMATCH":
        merkle = pmidx["merkle"]
        assert isinstance(merkle, dict)
        merkle["root"] = _sha256(b"different-root")
        _rebind_sidecar_digest(bundle, "pmidx")
    elif mutation == "PMSIG_SUBJECT_MISMATCH":
        subject = pmsig["subject"]
        assert isinstance(subject, dict)
        subject["pmtiles_sha256"] = _sha256(b"different-archive")
        _rebind_sidecar_digest(bundle, "pmsig")
    elif mutation == "RANGE_OUT_OF_BOUNDS":
        ranges = pmidx["ranges"]
        assert isinstance(ranges, list) and isinstance(ranges[0], dict)
        archive = base64.b64decode(bundle["archive_base64"], validate=True)
        ranges[0]["offset"] = len(archive)
        _rebind_sidecar_digest(bundle, "pmidx")
    elif mutation == "TILE_DIGEST_MISMATCH":
        ranges = pmidx["ranges"]
        assert isinstance(ranges, list) and isinstance(ranges[0], dict)
        ranges[0]["sha256"] = _sha256(b"different-tile")
        _rebind_sidecar_digest(bundle, "pmidx")
    elif mutation == "MAPLIBRE_READY_OVERCLAIM":
        bundle["maplibre_boot_state"] = "READY"
        bundle["maplibre_boot_reason"] = "UNSUPPORTED_CLAIM"
    elif mutation == "RELEASE_AUTHORITY_OVERCLAIM":
        authority = bundle["authority"]
        assert isinstance(authority, dict)
        authority["release"] = True
    else:
        raise ValueError(f"unknown mutation: {mutation}")
    return bundle


def validate_fixture_suite(value: dict[str, object]) -> list[dict[str, object]]:
    if value.get("profile") != PROFILE:
        return [
            {
                "case_id": "fixture-root",
                "findings": ["MOBILE_PMTILES_FIXTURE_PROFILE_INVALID"],
                "matches_expected": False,
            }
        ]
    if value.get("source_idea") != "ML-Y-111":
        return [
            {
                "case_id": "fixture-root",
                "findings": ["MOBILE_PMTILES_SOURCE_ID_INVALID"],
                "matches_expected": False,
            }
        ]

    base = value.get("base")
    cases = value.get("cases")
    if not isinstance(base, dict) or not isinstance(cases, list) or not cases:
        return [
            {
                "case_id": "fixture-root",
                "findings": ["MOBILE_PMTILES_CASES_INVALID"],
                "matches_expected": False,
            }
        ]

    case_ids: set[str] = set()
    results: list[dict[str, object]] = []
    for item in cases:
        if not isinstance(item, dict):
            results.append(
                {
                    "case_id": "invalid-case",
                    "findings": ["MOBILE_PMTILES_CASE_INVALID"],
                    "matches_expected": False,
                }
            )
            continue
        case_id = item.get("case_id")
        mutation = item.get("mutation")
        expected = item.get("expected_findings")
        if (
            not isinstance(case_id, str)
            or not case_id
            or case_id in case_ids
            or not isinstance(mutation, str)
            or not isinstance(expected, list)
            or not all(isinstance(code, str) for code in expected)
        ):
            results.append(
                {
                    "case_id": str(case_id),
                    "findings": ["MOBILE_PMTILES_CASE_INVALID"],
                    "matches_expected": False,
                }
            )
            continue
        case_ids.add(case_id)
        try:
            candidate = apply_mutation(base, mutation)
        except (AssertionError, KeyError, TypeError, ValueError, binascii.Error):
            findings = ["MOBILE_PMTILES_MUTATION_INVALID"]
        else:
            findings = [finding.code for finding in validate_bundle(candidate)]
        results.append(
            {
                "case_id": case_id,
                "findings": findings,
                "matches_expected": findings == expected,
            }
        )
    return results


def _serialize(path: Path, results: list[dict[str, object]]) -> str:
    ok = all(bool(result.get("matches_expected")) for result in results)
    payload = {
        "file": path.as_posix(),
        "profile": PROFILE,
        "status": "PASS" if ok else "DENY",
        "authority": "NONE",
        "results": results,
        "holds": sorted(EXPECTED_HOLDS),
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def validate_file(path: Path) -> tuple[list[dict[str, object]], list[Finding]]:
    value, findings = _load_json(path)
    if value is None:
        return [], findings
    return validate_fixture_suite(value), []


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate the synthetic mobile PMTiles fixture packet."
    )
    parser.add_argument("file", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(list(sys.argv[1:] if argv is None else argv))
    if args.fixtures and args.file is not None:
        print("--fixtures cannot be combined with a file", file=sys.stderr)
        return 2
    path = FIXTURE_PATH if args.fixtures else args.file
    if path is None:
        print("a fixture file or --fixtures is required", file=sys.stderr)
        return 2

    results, parser_findings = validate_file(path)
    if parser_findings:
        payload = {
            "file": path.as_posix(),
            "profile": PROFILE,
            "status": "DENY",
            "authority": "NONE",
            "findings": [finding.code for finding in parser_findings],
        }
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return 1

    print(_serialize(path, results))
    return 0 if all(bool(result.get("matches_expected")) for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
