#!/usr/bin/env python3
"""Validate the closed, synthetic Flora SpecimenRecord candidate profile."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from copy import deepcopy
from datetime import date
from pathlib import Path
from typing import Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    serialize_result,
    validate_fixture_file,
)

SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/flora/specimen_record.schema.json"
)
CASES_PATH = REPO_ROOT / "fixtures/domains/flora/specimen_record/cases.json"
SCOPE = "flora.specimen_record"

_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_SCHEMA_VALIDATOR = Draft202012Validator(
    _SCHEMA,
    format_checker=FormatChecker(),
)
_FORBIDDEN_GEOMETRY_KEYS = frozenset(
    {
        "coordinate",
        "coordinates",
        "decimallatitude",
        "decimallongitude",
        "geometry",
        "latitude",
        "longitude",
        "locality_text",
        "verbatim_coordinates",
        "wkt",
    }
)
_GOVERNANCE_EFFECTS = (
    "source_activated",
    "evidence_resolved",
    "policy_approved",
    "review_approved",
    "release_authorized",
    "published",
)


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def canonical_spec_hash(candidate: dict[str, object]) -> str:
    """Hash canonical JSON after removing only the top-level spec_hash."""

    payload = {key: value for key, value in candidate.items() if key != "spec_hash"}
    return f"sha256:{hashlib.sha256(_canonical_bytes(payload)).hexdigest()}"


def canonical_record_id(candidate: dict[str, object]) -> str | None:
    """Build the stable candidate identity from source and catalog identity."""

    source = candidate.get("source")
    if not isinstance(source, dict):
        return None
    keys = (
        "descriptor_ref",
        "institution_code",
        "collection_code",
        "catalog_number",
        "source_record_ref",
    )
    if any(not isinstance(source.get(key), str) for key in keys):
        return None
    identity = {key: source[key] for key in keys}
    digest = hashlib.sha256(_canonical_bytes(identity)).hexdigest()
    return f"kfm://candidate/flora/specimen/sha256:{digest}"


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _nested(candidate: object, *keys: str) -> object:
    value = candidate
    for key in keys:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def _scan_forbidden_fields(candidate: object) -> list[Finding]:
    findings: set[Finding] = set()
    pending: list[tuple[object, str]] = [(candidate, "$")]
    while pending:
        value, path = pending.pop()
        if isinstance(value, dict):
            for key, child in value.items():
                child_path = f"{path}.{key}"
                if key.lower() in _FORBIDDEN_GEOMETRY_KEYS:
                    add_finding(
                        findings,
                        "SPECIMEN_RECORD_RAW_GEOMETRY_FIELD_DENIED",
                        child_path,
                    )
                pending.append((child, child_path))
        elif isinstance(value, list):
            pending.extend(
                (child, f"{path}[{index}]")
                for index, child in enumerate(value)
            )
    return sorted(findings)


def _ordered_unique(
    findings: set[Finding],
    value: object,
    path: str,
    code: str,
) -> None:
    if isinstance(value, list) and (
        value != sorted(value) or len(value) != len(set(value))
    ):
        add_finding(findings, code, path)


def validate_document(candidate: object) -> list[Finding]:
    """Validate schema, identity, and specimen-specific trust boundaries."""

    findings: set[Finding] = set(_scan_forbidden_fields(candidate))

    if isinstance(candidate, dict):
        if _nested(candidate, "collection_event", "current_occurrence_claimed") is True:
            add_finding(
                findings,
                "SPECIMEN_RECORD_CURRENT_OCCURRENCE_OVERCLAIM",
                "$.collection_event.current_occurrence_claimed",
            )
        if _nested(candidate, "collection_event", "historical_evidence_only") is not True:
            add_finding(
                findings,
                "SPECIMEN_RECORD_HISTORICAL_BOUNDARY_REQUIRED",
                "$.collection_event.historical_evidence_only",
            )
        if _nested(candidate, "determination", "label_text_accepted_as_taxonomy") is True:
            add_finding(
                findings,
                "SPECIMEN_RECORD_LABEL_TAXONOMY_OVERCLAIM",
                "$.determination.label_text_accepted_as_taxonomy",
            )
        if _nested(candidate, "sensitivity", "exact_locality_public") is True:
            add_finding(
                findings,
                "SPECIMEN_RECORD_EXACT_LOCALITY_PUBLIC_DENIED",
                "$.sensitivity.exact_locality_public",
            )
        for effect in _GOVERNANCE_EFFECTS:
            if _nested(candidate, "governance", effect) is True:
                add_finding(
                    findings,
                    "SPECIMEN_RECORD_AUTHORITY_EFFECT_DENIED",
                    f"$.governance.{effect}",
                )

    schema_errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        add_finding(
            findings,
            "SPECIMEN_RECORD_SCHEMA_INVALID",
            _json_path(tuple(error.absolute_path)),
        )
    if schema_errors or not isinstance(candidate, dict):
        return sorted(findings)

    expected_record_id = canonical_record_id(candidate)
    if candidate["record_id"] != expected_record_id:
        add_finding(
            findings,
            "SPECIMEN_RECORD_IDENTITY_MISMATCH",
            "$.record_id",
        )
    if candidate["spec_hash"] != canonical_spec_hash(candidate):
        add_finding(
            findings,
            "SPECIMEN_RECORD_SPEC_HASH_MISMATCH",
            "$.spec_hash",
        )

    source_role = candidate["source_role"]
    record_class = candidate["record_class"]
    if (record_class == "synthetic") != (source_role == "synthetic"):
        add_finding(
            findings,
            "SPECIMEN_RECORD_SYNTHETIC_ROLE_MISMATCH",
            "$.source_role",
        )
    if (record_class == "candidate_record") != (source_role == "candidate"):
        add_finding(
            findings,
            "SPECIMEN_RECORD_CANDIDATE_ROLE_MISMATCH",
            "$.source_role",
        )

    collection = candidate["collection_event"]
    determination = candidate["determination"]
    rights = candidate["rights"]
    sensitivity = candidate["sensitivity"]
    projection = candidate["public_projection"]
    correction = candidate["correction"]
    assert isinstance(collection, dict)
    assert isinstance(determination, dict)
    assert isinstance(rights, dict)
    assert isinstance(sensitivity, dict)
    assert isinstance(projection, dict)
    assert isinstance(correction, dict)

    event_date = collection["event_date"]
    if source_role in {"observed", "regulatory"} and event_date is None:
        add_finding(
            findings,
            "SPECIMEN_RECORD_COLLECTION_DATE_REQUIRED",
            "$.collection_event.event_date",
        )
    if isinstance(event_date, str):
        try:
            date.fromisoformat(event_date)
        except ValueError:
            add_finding(
                findings,
                "SPECIMEN_RECORD_COLLECTION_DATE_INVALID",
                "$.collection_event.event_date",
            )

    locality_precision = collection["locality_precision"]
    restricted_geometry_ref = collection["restricted_geometry_ref"]
    if locality_precision in {"exact", "high_precision"} and restricted_geometry_ref is None:
        add_finding(
            findings,
            "SPECIMEN_RECORD_RESTRICTED_GEOMETRY_REF_REQUIRED",
            "$.collection_event.restricted_geometry_ref",
        )
    if locality_precision in {"withheld", "unknown"} and restricted_geometry_ref is not None:
        add_finding(
            findings,
            "SPECIMEN_RECORD_UNSUPPORTED_GEOMETRY_REF",
            "$.collection_event.restricted_geometry_ref",
        )

    if determination["status"] == "current" and (
        determination["taxon_ref"] is None
        or determination["crosswalk_ref"] is None
    ):
        add_finding(
            findings,
            "SPECIMEN_RECORD_CURRENT_DETERMINATION_UNRESOLVED",
            "$.determination",
        )

    candidate_projection = projection["candidate"]
    if not candidate_projection and (
        projection["geometry_ref"] is not None or projection["image_refs"]
    ):
        add_finding(
            findings,
            "SPECIMEN_RECORD_NONPUBLIC_PROJECTION_MUST_BE_EMPTY",
            "$.public_projection",
        )
    if candidate_projection:
        if source_role != "observed":
            add_finding(
                findings,
                "SPECIMEN_RECORD_PUBLIC_SOURCE_ROLE_INELIGIBLE",
                "$.source_role",
            )
        if rights["state"] != "open" or rights["public_metadata_allowed"] is not True:
            add_finding(
                findings,
                "SPECIMEN_RECORD_PUBLIC_RIGHTS_UNRESOLVED",
                "$.rights",
            )
        if sensitivity["state"] != "public_safe" or sensitivity["review_ref"] is None:
            add_finding(
                findings,
                "SPECIMEN_RECORD_PUBLIC_SENSITIVITY_UNRESOLVED",
                "$.sensitivity",
            )
        if locality_precision in {"exact", "high_precision"} and (
            sensitivity["redaction_receipt_ref"] is None
            or projection["geometry_ref"] is None
            or projection["geometry_ref"] == restricted_geometry_ref
        ):
            add_finding(
                findings,
                "SPECIMEN_RECORD_PUBLIC_REDACTION_REQUIRED",
                "$.public_projection.geometry_ref",
            )
        if projection["claim_posture"] != "historical_support":
            add_finding(
                findings,
                "SPECIMEN_RECORD_PUBLIC_CLAIM_POSTURE_INVALID",
                "$.public_projection.claim_posture",
            )
        if projection["image_refs"] and rights["image_reuse_allowed"] is not True:
            add_finding(
                findings,
                "SPECIMEN_RECORD_PUBLIC_IMAGE_RIGHTS_DENIED",
                "$.public_projection.image_refs",
            )

    if rights["state"] != "open" and (
        rights["public_metadata_allowed"] is True
        or rights["image_reuse_allowed"] is True
    ):
        add_finding(
            findings,
            "SPECIMEN_RECORD_RIGHTS_STATE_CONFLICT",
            "$.rights",
        )
    if sensitivity["rare_taxon"] is True and sensitivity["state"] != "restricted":
        add_finding(
            findings,
            "SPECIMEN_RECORD_RARE_TAXON_RESTRICTION_REQUIRED",
            "$.sensitivity.state",
        )
    if sensitivity["state"] != "public_safe" and candidate_projection:
        add_finding(
            findings,
            "SPECIMEN_RECORD_RESTRICTED_PUBLIC_PROJECTION_DENIED",
            "$.public_projection.candidate",
        )

    supersedes = correction["supersedes_record_ref"]
    correction_refs = correction["correction_refs"]
    if (supersedes is None) != (not correction_refs):
        add_finding(
            findings,
            "SPECIMEN_RECORD_CORRECTION_LINEAGE_INCOMPLETE",
            "$.correction",
        )

    _ordered_unique(
        findings,
        candidate["evidence_refs"],
        "$.evidence_refs",
        "SPECIMEN_RECORD_EVIDENCE_REF_ORDER_INVALID",
    )
    _ordered_unique(
        findings,
        projection["image_refs"],
        "$.public_projection.image_refs",
        "SPECIMEN_RECORD_IMAGE_REF_ORDER_INVALID",
    )
    _ordered_unique(
        findings,
        correction_refs,
        "$.correction.correction_refs",
        "SPECIMEN_RECORD_CORRECTION_REF_ORDER_INVALID",
    )

    return sorted(findings)


def validate_specimen_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_document)


def build_case_candidate(profile: dict[str, object], case: dict[str, object]) -> dict[str, object]:
    """Apply a bounded JSON-pointer mutation list to the shared base candidate."""

    candidate = deepcopy(profile["base_candidate"])
    assert isinstance(candidate, dict)
    mutations = case.get("mutations", [])
    assert isinstance(mutations, list)
    for mutation in mutations:
        assert isinstance(mutation, dict)
        pointer = mutation["path"]
        assert isinstance(pointer, str) and pointer.startswith("/")
        parts = pointer.removeprefix("/").split("/")
        target: object = candidate
        for part in parts[:-1]:
            assert isinstance(target, dict)
            target = target[part]
        assert isinstance(target, dict)
        target[parts[-1]] = deepcopy(mutation["value"])

    if case.get("rehash_record_id", True):
        record_id = canonical_record_id(candidate)
        assert record_id is not None
        candidate["record_id"] = record_id
    if case.get("rehash_spec_hash", True):
        candidate["spec_hash"] = canonical_spec_hash(candidate)
    return candidate


def replay_cases(path: Path = CASES_PATH) -> list[str]:
    """Replay exact expected fixture polarity and return mismatch descriptions."""

    payload = json.loads(path.read_text(encoding="utf-8"))
    mismatches: list[str] = []
    for case in payload["cases"]:
        actual = [
            finding.code
            for finding in validate_document(build_case_candidate(payload, case))
        ]
        expected = case["expected_codes"]
        if actual != expected:
            mismatches.append(
                f"{case['name']}: expected {expected!r}, observed {actual!r}"
            )
    return mismatches


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate synthetic Flora SpecimenRecord candidates."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument(
        "--fixtures",
        action="store_true",
        help="replay the canonical cases.json profile",
    )
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with file arguments")
        mismatches = replay_cases()
        if mismatches:
            for mismatch in mismatches:
                print(mismatch, file=sys.stderr)
            return 1
        print("SPECIMEN_RECORD_FIXTURES_VALID")
        return 0
    if not args.files:
        parser.print_usage(sys.stderr)
        return 2

    failed = False
    for path in sorted(args.files, key=lambda item: str(item)):
        findings = validate_specimen_file(path)
        failed = failed or bool(findings)
        print(serialize_result(SCOPE, path, findings))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
