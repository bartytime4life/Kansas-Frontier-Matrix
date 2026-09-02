#!/usr/bin/env python3
"""Build a deterministic fixture-only soil yearly-diff candidate.

The helper consumes two local synthetic snapshot manifests. It performs no
network access, source activation, lifecycle promotion, release, or
publication. Output is written only when ``--write`` is supplied.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
HASH_SRC = ROOT / "packages/hashing/src"
for import_root in (ROOT, HASH_SRC):
    if str(import_root) not in sys.path:
        sys.path.insert(0, str(import_root))

from hashing import compute_spec_hash
from tools.validators.domains.soil import (
    validate_ssurgo_yearly_diff_profile as profile_validator,
)

MAX_INPUT_BYTES = 8 * 1024 * 1024
MAX_RECORDS = 50_000
MAX_PROPERTIES = 256
PROPERTY_RE = re.compile(r"^[a-z][a-z0-9_]{1,63}$")
RECORD_KEY_RE = re.compile(r"^[A-Za-z0-9_.:-]{1,128}$")
SHA256_RE = re.compile(r"^sha256:[a-f0-9]{64}$")
MANIFEST_KEYS = {
    "artifact_ref",
    "artifact_sha256",
    "dataset_year",
    "fixture_only",
    "network_mode",
    "normalization",
    "object_type",
    "prov_entity_ref",
    "records",
    "schema_version",
    "snapshot_receipt_ref",
    "source_descriptor_ref",
    "source_family",
    "stac_item_ref",
    "support_type",
    "validation_receipt_ref",
}
SOURCE_PROFILES = {
    "GNATSGO": (
        "GRIDDED_DERIVATIVE_SOIL",
        "GNATSGO_GRID_METADATA_DIFF_V1",
        "data/registry/sources/soil/nrcs-gnatsgo.yaml",
    ),
    "SSURGO": (
        "AUTHORITATIVE_STATIC_SOIL_SURVEY",
        "SSURGO_KEYED_RECORD_DIFF_V1",
        "data/registry/sources/soil/nrcs-ssurgo.yaml",
    ),
}
GOVERNANCE = {
    "network_authorized": False,
    "promotion_authorized": False,
    "publication_authorized": False,
    "raw_admission_authorized": False,
    "release_authorized": False,
    "source_activation_authorized": False,
}


class DuplicateKeyError(ValueError):
    """Input JSON repeated an object key."""


class NonFiniteNumberError(ValueError):
    """Input JSON contained a non-standard or non-finite number."""


@dataclass(frozen=True)
class BuildFailure(ValueError):
    code: str

    def __str__(self) -> str:
        return self.code


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def read_manifest(path: Path) -> dict[str, Any]:
    try:
        if path.is_symlink():
            raise BuildFailure("INPUT_SYMLINK_DENIED")
        if not path.is_file():
            raise BuildFailure("INPUT_NOT_FILE")
        if path.stat().st_size > MAX_INPUT_BYTES:
            raise BuildFailure("INPUT_TOO_LARGE")
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except BuildFailure:
        raise
    except DuplicateKeyError as exc:
        raise BuildFailure("JSON_DUPLICATE_KEY") from exc
    except NonFiniteNumberError as exc:
        raise BuildFailure("JSON_NONFINITE_NUMBER") from exc
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise BuildFailure("JSON_INVALID") from exc
    except OSError as exc:
        raise BuildFailure("INPUT_READ_ERROR") from exc
    if not isinstance(value, dict):
        raise BuildFailure("ROOT_NOT_OBJECT")
    validate_manifest(value)
    return value


def _validate_normalization(value: Any) -> None:
    if not isinstance(value, dict) or set(value) != {
        "attributes_changed",
        "geometry_changed",
        "transform_receipt_refs",
    }:
        raise BuildFailure("NORMALIZATION_INVALID")
    if not isinstance(value["attributes_changed"], bool) or not isinstance(
        value["geometry_changed"], bool
    ):
        raise BuildFailure("NORMALIZATION_INVALID")
    refs = value["transform_receipt_refs"]
    if not isinstance(refs, list) or refs != sorted(set(refs)):
        raise BuildFailure("TRANSFORM_RECEIPTS_NOT_CANONICAL")
    if not all(
        isinstance(ref, str) and ref.startswith("kfm://receipt/transform/")
        for ref in refs
    ):
        raise BuildFailure("TRANSFORM_RECEIPT_REF_INVALID")
    changed = value["attributes_changed"] or value["geometry_changed"]
    if changed != bool(refs):
        raise BuildFailure("TRANSFORM_RECEIPT_POSTURE_INVALID")


def validate_manifest(value: Mapping[str, Any]) -> None:
    if set(value) != MANIFEST_KEYS:
        raise BuildFailure("MANIFEST_FIELDS_INVALID")
    if value.get("object_type") != "SoilSyntheticSnapshotManifest":
        raise BuildFailure("OBJECT_TYPE_INVALID")
    if value.get("schema_version") != "1.0.0":
        raise BuildFailure("SCHEMA_VERSION_INVALID")
    if value.get("fixture_only") is not True or value.get("network_mode") != "DENY":
        raise BuildFailure("FIXTURE_BOUNDARY_INVALID")

    source_family = value.get("source_family")
    expected = SOURCE_PROFILES.get(source_family)
    actual = (value.get("support_type"), value.get("source_descriptor_ref"))
    if expected is None or actual != (expected[0], expected[2]):
        raise BuildFailure("SOURCE_ROLE_INVALID")

    year = value.get("dataset_year")
    if isinstance(year, bool) or not isinstance(year, int) or not 1900 <= year <= 2200:
        raise BuildFailure("DATASET_YEAR_INVALID")
    if not isinstance(value.get("artifact_sha256"), str) or not SHA256_RE.fullmatch(
        value["artifact_sha256"]
    ):
        raise BuildFailure("SNAPSHOT_HASH_INVALID")
    for field in (
        "artifact_ref",
        "prov_entity_ref",
        "snapshot_receipt_ref",
        "stac_item_ref",
        "validation_receipt_ref",
    ):
        item = value.get(field)
        if not isinstance(item, str) or ":" not in item or any(char.isspace() for char in item):
            raise BuildFailure("SNAPSHOT_REF_INVALID")

    _validate_normalization(value.get("normalization"))
    records = value.get("records")
    if not isinstance(records, list) or not 0 <= len(records) <= MAX_RECORDS:
        raise BuildFailure("RECORDS_INVALID")
    keys: list[str] = []
    for record in records:
        if not isinstance(record, dict) or set(record) != {"properties", "record_key"}:
            raise BuildFailure("RECORD_INVALID")
        key = record.get("record_key")
        properties = record.get("properties")
        if not isinstance(key, str) or not RECORD_KEY_RE.fullmatch(key):
            raise BuildFailure("RECORD_KEY_INVALID")
        if not isinstance(properties, dict) or not 1 <= len(properties) <= MAX_PROPERTIES:
            raise BuildFailure("RECORD_PROPERTIES_INVALID")
        if not all(isinstance(name, str) and PROPERTY_RE.fullmatch(name) for name in properties):
            raise BuildFailure("PROPERTY_NAME_INVALID")
        keys.append(key)
    if keys != sorted(set(keys)):
        raise BuildFailure("RECORD_KEYS_NOT_CANONICAL")


def _snapshot(value: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "artifact_ref": value["artifact_ref"],
        "artifact_sha256": value["artifact_sha256"],
        "dataset_year": value["dataset_year"],
        "prov_entity_ref": value["prov_entity_ref"],
        "snapshot_receipt_ref": value["snapshot_receipt_ref"],
        "stac_item_ref": value["stac_item_ref"],
        "validation_receipt_ref": value["validation_receipt_ref"],
    }


def _record_diff(
    previous: Mapping[str, Any], current: Mapping[str, Any]
) -> dict[str, Any]:
    previous_records = {item["record_key"]: item for item in previous["records"]}
    current_records = {item["record_key"]: item for item in current["records"]}
    previous_keys = set(previous_records)
    current_keys = set(current_records)
    modified: list[dict[str, Any]] = []
    changed_property_names: set[str] = set()
    for key in sorted(previous_keys & current_keys):
        before = previous_records[key]["properties"]
        after = current_records[key]["properties"]
        changed = sorted(
            name
            for name in set(before) | set(after)
            if before.get(name) != after.get(name)
        )
        if changed:
            changed_property_names.update(changed)
            modified.append(
                {
                    "changed_property_names": changed,
                    "current_record_hash": compute_spec_hash(current_records[key]),
                    "previous_record_hash": compute_spec_hash(previous_records[key]),
                    "record_key": key,
                }
            )
    return {
        "added_record_keys": sorted(current_keys - previous_keys),
        "changed_property_names": sorted(changed_property_names),
        "current_snapshot_sha256": current["artifact_sha256"],
        "current_year": current["dataset_year"],
        "modified_records": modified,
        "object_type": "SoilSyntheticRecordDiff",
        "previous_snapshot_sha256": previous["artifact_sha256"],
        "previous_year": previous["dataset_year"],
        "removed_record_keys": sorted(previous_keys - current_keys),
        "schema_version": "1.0.0",
        "source_family": current["source_family"],
    }


def build_result(
    previous: Mapping[str, Any],
    current: Mapping[str, Any],
    *,
    target_zone: str = "WORK",
) -> dict[str, Any]:
    validate_manifest(previous)
    validate_manifest(current)
    for field in ("source_family", "support_type", "source_descriptor_ref"):
        if previous[field] != current[field]:
            raise BuildFailure("SNAPSHOT_SOURCE_MISMATCH")
    if current["dataset_year"] != previous["dataset_year"] + 1:
        raise BuildFailure("YEAR_SEQUENCE_INVALID")
    if target_zone not in {"QUARANTINE", "WORK"}:
        raise BuildFailure("TARGET_ZONE_INVALID")

    family = current["source_family"]
    slug = family.lower()
    previous_year = previous["dataset_year"]
    current_year = current["dataset_year"]
    details = _record_diff(previous, current)
    detail_hash = compute_spec_hash(details)
    profile = {
        "canonicalization_profile": "RFC8785-JCS",
        "current_snapshot": _snapshot(current),
        "diff": {
            "added_records": len(details["added_record_keys"]),
            "changed_property_names": details["changed_property_names"],
            "computation_profile": SOURCE_PROFILES[family][1],
            "diff_artifact_ref": (
                f"artifact:soil/{slug}/{previous_year}-{current_year}/synthetic-record-diff"
            ),
            "diff_artifact_sha256": detail_hash,
            "modified_records": len(details["modified_records"]),
            "observed_property_relabelled": False,
            "removed_records": len(details["removed_record_keys"]),
        },
        "execution_mode": "FIXTURE_ONLY",
        "governance": copy.deepcopy(GOVERNANCE),
        "network_mode": "DENY",
        "normalization": copy.deepcopy(current["normalization"]),
        "object_type": "SoilYearlyDiffProfile",
        "output": {
            "promotion_required": True,
            "prov_chain_complete": True,
            "stac_pair_complete": True,
            "target_zone": target_zone,
        },
        "previous_snapshot": _snapshot(previous),
        "profile_id": "kfm.soil.ssurgo-gnatsgo-yearly-diff.fixture.v1",
        "provenance": {
            "diff_activity_ref": (
                f"kfm://prov/activity/diff/soil-{slug}-{previous_year}-{current_year}"
            ),
            "fetch_activity_ref": f"kfm://prov/activity/fetch/soil-{slug}-{current_year}",
            "publication_activity_ref": None,
            "validation_activity_ref": (
                f"kfm://prov/activity/validation/soil-{slug}-{current_year}"
            ),
        },
        "schema_version": "1.0.0",
        "source_descriptor_ref": current["source_descriptor_ref"],
        "source_family": family,
        "status": "PROPOSED_INACTIVE",
        "support_type": current["support_type"],
        "version": "0.1.0",
    }
    profile["spec_hash"] = compute_spec_hash(profile)
    validation = profile_validator.validate_payload(profile)
    if not validation.ok:
        raise BuildFailure("GENERATED_PROFILE_INVALID")
    return {
        "governance": copy.deepcopy(GOVERNANCE),
        "object_type": "SoilYearlyDiffBuildResult",
        "profile": profile,
        "record_diff": details,
        "record_diff_sha256": detail_hash,
        "schema_version": "1.0.0",
        "status": "CANDIDATE",
    }


def _encoded(value: Mapping[str, Any]) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def write_result(value: Mapping[str, Any], path: Path, *, force: bool = False) -> None:
    if path.is_symlink():
        raise BuildFailure("OUTPUT_SYMLINK_DENIED")
    if path.exists() and not force:
        raise BuildFailure("OUTPUT_EXISTS")
    if path.exists() and not path.is_file():
        raise BuildFailure("OUTPUT_NOT_FILE")
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(_encoded(value), encoding="utf-8")
    except OSError as exc:
        raise BuildFailure("OUTPUT_WRITE_ERROR") from exc


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build a local fixture-only soil yearly-diff candidate."
    )
    parser.add_argument("previous", type=Path)
    parser.add_argument("current", type=Path)
    parser.add_argument("--target-zone", choices=("QUARANTINE", "WORK"), default="WORK")
    parser.add_argument("--write", type=Path, metavar="PATH")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)
    if args.force and args.write is None:
        parser.error("--force requires --write")
    try:
        result = build_result(
            read_manifest(args.previous),
            read_manifest(args.current),
            target_zone=args.target_zone,
        )
        if args.write is None:
            sys.stdout.write(_encoded(result))
        else:
            write_result(result, args.write, force=args.force)
            print(
                json.dumps(
                    {"outcome": "generated", "path": args.write.as_posix()},
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
    except BuildFailure as exc:
        print(
            json.dumps(
                {"outcome": "blocked", "reason": exc.code},
                sort_keys=True,
                separators=(",", ":"),
            ),
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
