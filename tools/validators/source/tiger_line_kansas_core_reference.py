#!/usr/bin/env python3
"""Validate the exact TIGER/Line 2025 Kansas core reference without network access.

The committed JSON is a connector-local inventory of an externally held operator
handoff.  This validator checks source identity, selection completeness, digests,
and fail-closed governance flags.  It does not fetch, extract, admit, activate,
publish, release, or bind any package to a map runtime.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, Mapping
from urllib.parse import urlsplit


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_MANIFEST_PATH = (
    REPO_ROOT
    / "connectors/census/tiger-line-2025-kansas-core.source-reference.json"
)
ARCHIVE_ROOT = "https://www2.census.gov/geo/tiger/TIGER2025/"
LANDING_PAGE = (
    "https://www.census.gov/geographies/mapping-files/time-series/geo/"
    "tiger-line-file.html"
)
EXPECTED_PACKAGE_COUNT = 326
EXPECTED_TOTAL_BYTES = 991_516_458
EXPECTED_PACKAGE_INDEX_SHA256 = (
    "sha256:711f30103c647c76241f6450e3c9ad71abc5d4efbdeed591b975c1bb9cda7fbe"
)
EXPECTED_SOURCE_MANIFEST_SHA256 = (
    "bfb69f7630e6df94495d82507cf9a47c5eb5bd320667fff78f7acc0ef8af577d"
)
EXPECTED_DELIVERY_INDEX_SHA256 = (
    "04624ea690e65280833ca6e44c01b8da66b8d60a4ff3405215dd3c5f03de410a"
)
EXPECTED_KANSAS_COUNTY_GEOIDS = tuple(f"20{code:03d}" for code in range(1, 210, 2))
COUNTY_PRODUCTS = {
    "AREAWATER": "areawater",
    "LINEARWATER": "linearwater",
    "ROADS": "roads",
}
SINGLETON_FILES = {
    "BG": "tl_2025_20_bg.zip",
    "COUNTY": "tl_2025_us_county.zip",
    "COUSUB": "tl_2025_20_cousub.zip",
    "PLACE": "tl_2025_20_place.zip",
    "PRIMARYROADS": "tl_2025_us_primaryroads.zip",
    "PRISECROADS": "tl_2025_20_prisecroads.zip",
    "RAILS": "tl_2025_us_rails.zip",
    "STATE": "tl_2025_us_state.zip",
    "TABBLOCK20": "tl_2025_20_tabblock20.zip",
    "TRACT": "tl_2025_20_tract.zip",
    "ZCTA520": "tl_2025_us_zcta520.zip",
}
EXPECTED_PRODUCT_COUNTS = {
    **{product: len(EXPECTED_KANSAS_COUNTY_GEOIDS) for product in COUNTY_PRODUCTS},
    **{product: 1 for product in SINGLETON_FILES},
}
EXPECTED_PRODUCT_COUNTS = dict(sorted(EXPECTED_PRODUCT_COUNTS.items()))
EXPECTED_FILES_BY_PRODUCT = {
    product: {
        f"tl_2025_{geoid}_{suffix}.zip" for geoid in EXPECTED_KANSAS_COUNTY_GEOIDS
    }
    for product, suffix in COUNTY_PRODUCTS.items()
}
EXPECTED_FILES_BY_PRODUCT.update(
    {product: {file_name} for product, file_name in SINGLETON_FILES.items()}
)
GOVERNANCE_KEYS = frozenset(
    {
        "source_descriptor_registered",
        "source_activated",
        "feature_class_allow_list_approved",
        "raw_admission_authorized",
        "rights_review_completed",
        "sensitivity_review_completed",
        "evidence_bundle_emitted",
        "release_authorized",
        "publication_authorized",
        "map_runtime_binding_allowed",
    }
)
PACKAGE_KEYS = frozenset(
    {
        "product",
        "file_name",
        "source_url",
        "byte_length",
        "sha256",
        "source_last_modified_at",
        "retrieved_at",
        "operator_zip_integrity",
    }
)
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")


class ReferenceValidationError(ValueError):
    """A stable, non-value-bearing local reference validation failure."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


def _mapping(value: object) -> Mapping[str, object] | None:
    return value if isinstance(value, dict) else None


def _parse_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        return None
    return parsed


def _package_index_sha256(packages: list[object]) -> str:
    encoded = json.dumps(
        packages,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _strings(value: object) -> Iterator[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, nested in value.items():
            yield str(key)
            yield from _strings(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from _strings(nested)


def _validate_package(package: Mapping[str, object], errors: list[str]) -> None:
    if set(package) != PACKAGE_KEYS:
        errors.append("PACKAGE_KEYS_INVALID")

    product = package.get("product")
    file_name = package.get("file_name")
    source_url = package.get("source_url")
    byte_length = package.get("byte_length")
    digest = package.get("sha256")
    last_modified = _parse_utc(package.get("source_last_modified_at"))
    retrieved_at = _parse_utc(package.get("retrieved_at"))

    if product not in EXPECTED_FILES_BY_PRODUCT:
        errors.append("PRODUCT_INVALID")
    if not isinstance(file_name, str) or not file_name.endswith(".zip"):
        errors.append("FILE_NAME_INVALID")
    if isinstance(product, str) and isinstance(file_name, str):
        expected_url = f"{ARCHIVE_ROOT}{product}/{file_name}"
        if source_url != expected_url:
            errors.append("SOURCE_URL_INVALID")
    if not isinstance(source_url, str):
        errors.append("SOURCE_URL_INVALID")
    else:
        try:
            parsed = urlsplit(source_url)
            port = parsed.port
        except ValueError:
            errors.append("SOURCE_URL_INVALID")
        else:
            if (
                parsed.scheme != "https"
                or parsed.hostname != "www2.census.gov"
                or parsed.username is not None
                or parsed.password is not None
                or port is not None
                or parsed.query
                or parsed.fragment
            ):
                errors.append("SOURCE_URL_INVALID")
    if isinstance(byte_length, bool) or not isinstance(byte_length, int) or byte_length < 1:
        errors.append("BYTE_LENGTH_INVALID")
    if not isinstance(digest, str) or SHA256_PATTERN.fullmatch(digest) is None:
        errors.append("SHA256_INVALID")
    if last_modified is None or retrieved_at is None:
        errors.append("PACKAGE_TIMESTAMP_INVALID")
    elif last_modified > retrieved_at:
        errors.append("PACKAGE_TIMESTAMP_ORDER_INVALID")
    if package.get("operator_zip_integrity") != "PASS":
        errors.append("ZIP_INTEGRITY_STATUS_INVALID")


def validate_manifest(document: object) -> list[str]:
    """Return deterministic failure codes for a parsed reference manifest."""
    errors: list[str] = []
    doc = _mapping(document)
    if doc is None:
        return ["DOCUMENT_NOT_OBJECT"]

    expected_top_keys = {
        "object_type",
        "schema_version",
        "manifest_id",
        "status",
        "source",
        "scope",
        "capture",
        "inventory",
        "governance",
    }
    if set(doc) != expected_top_keys:
        errors.append("TOP_LEVEL_KEYS_INVALID")
    if doc.get("object_type") != "TigerLineSourceReferenceManifest":
        errors.append("OBJECT_TYPE_INVALID")
    if doc.get("schema_version") != "1.0.0":
        errors.append("SCHEMA_VERSION_INVALID")
    if doc.get("manifest_id") != (
        "kfm://connector/census/tiger-line/source-reference/2025/kansas-core"
    ):
        errors.append("MANIFEST_ID_INVALID")
    if doc.get("status") != "PROPOSED_INACTIVE":
        errors.append("STATUS_INVALID")

    source = _mapping(doc.get("source"))
    expected_source = {
        "publisher": "U.S. Census Bureau",
        "product": "2025 TIGER/Line Shapefiles",
        "vintage": 2025,
        "media_type": "application/zip",
        "landing_page": LANDING_PAGE,
        "archive_root": ARCHIVE_ROOT,
    }
    if source != expected_source:
        errors.append("SOURCE_IDENTITY_INVALID")

    scope = _mapping(doc.get("scope"))
    expected_scope = {
        "label": "Kansas core candidate",
        "state_fips": "20",
        "state_abbreviation": "KS",
        "county_count": 105,
        "source_role": "CANDIDATE_REFERENCE_GEOMETRY_PACKAGES",
        "package_selection_status": "CANDIDATE_NOT_APPROVED",
        "rights_posture": "NEEDS_REVIEW",
        "sensitivity_posture": "NEEDS_REVIEW",
        "crs_topology_status": "NOT_INSPECTED",
        "notes": [
            "This inventory is not an accepted TIGER/Line feature-class allow-list.",
            "Road, rail, and water packages remain non-authoritative domain inputs.",
            "TIGER/Line is not demographic, cadastral, or legal-boundary authority.",
        ],
    }
    if scope != expected_scope:
        errors.append("SCOPE_INVALID")

    capture = _mapping(doc.get("capture"))
    expected_capture = {
        "retrieved_at_start": "2026-09-12T22:19:44Z",
        "retrieved_at_end": "2026-09-12T22:24:30Z",
        "operator_source_manifest_sha256": EXPECTED_SOURCE_MANIFEST_SHA256,
        "operator_delivery_index_sha256": EXPECTED_DELIVERY_INDEX_SHA256,
        "source_zip_integrity": "326_OF_326_PASS",
        "operator_handoff_readback": "VERIFIED",
        "intact_package_count": 325,
        "segmented_source_package_count": 1,
        "segment_count": 6,
        "private_locator_committed": False,
    }
    if capture != expected_capture:
        errors.append("CAPTURE_IDENTITY_INVALID")

    governance = _mapping(doc.get("governance"))
    if governance is None or set(governance) != GOVERNANCE_KEYS:
        errors.append("GOVERNANCE_KEYS_INVALID")
    elif any(governance[key] is not False for key in GOVERNANCE_KEYS):
        errors.append("GOVERNANCE_ESCALATION")

    inventory = _mapping(doc.get("inventory"))
    if inventory is None:
        errors.append("INVENTORY_INVALID")
        return sorted(set(errors))
    if set(inventory) != {
        "package_count",
        "total_bytes",
        "product_counts",
        "package_index_sha256",
        "packages",
    }:
        errors.append("INVENTORY_KEYS_INVALID")

    packages = inventory.get("packages")
    if not isinstance(packages, list):
        errors.append("PACKAGES_INVALID")
        return sorted(set(errors))
    if len(packages) != EXPECTED_PACKAGE_COUNT:
        errors.append("PACKAGE_COUNT_MISMATCH")
    if inventory.get("package_count") != EXPECTED_PACKAGE_COUNT:
        errors.append("PACKAGE_COUNT_MISMATCH")

    valid_packages: list[Mapping[str, object]] = []
    for package in packages:
        mapped = _mapping(package)
        if mapped is None:
            errors.append("PACKAGE_NOT_OBJECT")
            continue
        _validate_package(mapped, errors)
        valid_packages.append(mapped)

    package_order = [
        (str(package.get("product")), str(package.get("file_name")))
        for package in valid_packages
    ]
    if package_order != sorted(package_order):
        errors.append("PACKAGE_ORDER_INVALID")

    file_names = [package.get("file_name") for package in valid_packages]
    source_urls = [package.get("source_url") for package in valid_packages]
    if len(file_names) != len(set(map(str, file_names))):
        errors.append("DUPLICATE_FILE_NAME")
    if len(source_urls) != len(set(map(str, source_urls))):
        errors.append("DUPLICATE_SOURCE_URL")

    observed_counts = Counter(
        str(package.get("product")) for package in valid_packages
    )
    if dict(sorted(observed_counts.items())) != EXPECTED_PRODUCT_COUNTS:
        errors.append("PRODUCT_COUNTS_MISMATCH")
    if inventory.get("product_counts") != EXPECTED_PRODUCT_COUNTS:
        errors.append("PRODUCT_COUNTS_MISMATCH")

    observed_files: dict[str, set[str]] = {}
    for package in valid_packages:
        product = package.get("product")
        file_name = package.get("file_name")
        if isinstance(product, str) and isinstance(file_name, str):
            observed_files.setdefault(product, set()).add(file_name)
    if observed_files != EXPECTED_FILES_BY_PRODUCT:
        errors.append("PRODUCT_PACKAGE_SET_MISMATCH")

    actual_total = sum(
        value
        for package in valid_packages
        if isinstance((value := package.get("byte_length")), int)
        and not isinstance(value, bool)
    )
    if actual_total != EXPECTED_TOTAL_BYTES:
        errors.append("TOTAL_BYTES_MISMATCH")
    if inventory.get("total_bytes") != EXPECTED_TOTAL_BYTES:
        errors.append("TOTAL_BYTES_MISMATCH")

    calculated_index = _package_index_sha256(packages)
    if inventory.get("package_index_sha256") != calculated_index:
        errors.append("PACKAGE_INDEX_SHA256_MISMATCH")
    if inventory.get("package_index_sha256") != EXPECTED_PACKAGE_INDEX_SHA256:
        errors.append("PACKAGE_INDEX_IDENTITY_MISMATCH")

    private_markers = ("drive.google.com", "docs.google.com")
    if any(marker in value.lower() for value in _strings(doc) for marker in private_markers):
        errors.append("PRIVATE_LOCATOR_PRESENT")
    return sorted(set(errors))


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_payload_root(
    document: object,
    payload_root: Path,
    *,
    check_zip_crc: bool = False,
) -> dict[str, int | bool]:
    """Verify exact external bytes locally; never extract or perform network I/O."""
    errors = validate_manifest(document)
    if errors:
        raise ReferenceValidationError(errors[0])
    doc = _mapping(document)
    assert doc is not None
    inventory = _mapping(doc["inventory"])
    assert inventory is not None
    packages = inventory["packages"]
    assert isinstance(packages, list)

    if payload_root.is_symlink() or not payload_root.is_dir():
        raise ReferenceValidationError("PAYLOAD_ROOT_INVALID")
    resolved_root = payload_root.resolve(strict=True)

    verified_bytes = 0
    for package_value in packages:
        package = _mapping(package_value)
        assert package is not None
        product = str(package["product"])
        file_name = str(package["file_name"])
        product_root = payload_root / product
        path = payload_root / product / file_name
        if product_root.is_symlink() or path.is_symlink() or not path.is_file():
            raise ReferenceValidationError("PAYLOAD_FILE_INVALID")
        try:
            resolved_path = path.resolve(strict=True)
        except OSError as exc:
            raise ReferenceValidationError("PAYLOAD_FILE_INVALID") from exc
        if not resolved_path.is_relative_to(resolved_root):
            raise ReferenceValidationError("PAYLOAD_FILE_INVALID")
        size = path.stat().st_size
        if size != package["byte_length"]:
            raise ReferenceValidationError("PAYLOAD_SIZE_MISMATCH")
        if _sha256_file(path) != package["sha256"]:
            raise ReferenceValidationError("PAYLOAD_SHA256_MISMATCH")
        if check_zip_crc:
            try:
                with zipfile.ZipFile(path) as archive:
                    if archive.testzip() is not None:
                        raise ReferenceValidationError("PAYLOAD_ZIP_CRC_MISMATCH")
            except zipfile.BadZipFile as exc:
                raise ReferenceValidationError("PAYLOAD_ZIP_INVALID") from exc
        verified_bytes += size

    if verified_bytes != EXPECTED_TOTAL_BYTES:
        raise ReferenceValidationError("PAYLOAD_TOTAL_BYTES_MISMATCH")
    return {
        "payload_package_count": len(packages),
        "payload_total_bytes": verified_bytes,
        "zip_crc_checked": check_zip_crc,
    }


def validation_summary(
    document: object,
    payload_verification: Mapping[str, int | bool] | None = None,
) -> dict[str, object]:
    """Return a deterministic non-authoritative success summary."""
    errors = validate_manifest(document)
    if errors:
        raise ReferenceValidationError(errors[0])
    doc = _mapping(document)
    assert doc is not None
    inventory = _mapping(doc["inventory"])
    governance = _mapping(doc["governance"])
    assert inventory is not None and governance is not None
    return {
        "manifest_id": doc["manifest_id"],
        "status": "PASS",
        "package_count": inventory["package_count"],
        "total_bytes": inventory["total_bytes"],
        "package_index_sha256": inventory["package_index_sha256"],
        "payload_verification": dict(payload_verification or {}),
        "governance": dict(governance),
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    parser.add_argument(
        "--payload-root",
        type=Path,
        help="optional local root containing PRODUCT/source.zip payloads",
    )
    parser.add_argument(
        "--check-zip-crc",
        action="store_true",
        help="decompress each local ZIP to verify its CRC without extracting it",
    )
    return parser


def main() -> int:
    args = _parser().parse_args()
    if args.check_zip_crc and args.payload_root is None:
        print("PAYLOAD_ROOT_REQUIRED_FOR_ZIP_CRC", file=sys.stderr)
        return 2
    try:
        document = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        print("MANIFEST_READ_INVALID", file=sys.stderr)
        return 1

    errors = validate_manifest(document)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    try:
        verification = (
            verify_payload_root(
                document,
                args.payload_root,
                check_zip_crc=args.check_zip_crc,
            )
            if args.payload_root is not None
            else None
        )
        summary = validation_summary(document, verification)
    except (OSError, ReferenceValidationError) as exc:
        code = exc.code if isinstance(exc, ReferenceValidationError) else "PAYLOAD_READ_FAILED"
        print(code, file=sys.stderr)
        return 1
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
