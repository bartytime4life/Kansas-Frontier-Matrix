"""Deterministic, no-network authority checks for water-planning geometry.

This validator checks a bounded fixture envelope.  It does not fetch sources,
construct geometry, create registry records, make release decisions, or publish.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


MAX_INPUT_BYTES = 1_000_000
IDENTITY_AUTHORITY_ID = "kwo:rac:regional-advisory-committees"
IDENTITY_SOURCE_LOCATOR = (
    "https://www.kwo.ks.gov/about-us/regional-advisory-committees"
)
REGION_ID_PATTERN = re.compile(r"^kwo-rac-(0[1-9]|1[0-4])$")
RAC_SHAPED_ID_PATTERN = re.compile(r"^kwo-rac-[0-9]{2}$")
DIGEST_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")
DATE_PATTERN = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")

EXPECTED_REGION_NAMES = (
    "Cimarron",
    "Equus-Walnut",
    "Great Bend Prairie",
    "Kansas",
    "Marais des Cygnes",
    "Missouri",
    "Neosho",
    "Red Hills",
    "Smoky Hill-Saline",
    "Solomon-Republican",
    "Upper Arkansas",
    "Upper Republican",
    "Upper Smoky Hill",
    "Verdigris",
)
EXPECTED_REGION_IDS = tuple(
    f"kwo-rac-{number:02d}" for number in range(1, len(EXPECTED_REGION_NAMES) + 1)
)
EXPECTED_REGION_NAME_BY_ID = dict(zip(EXPECTED_REGION_IDS, EXPECTED_REGION_NAMES))

TOP_LEVEL_FIELDS = frozenset(
    {
        "fixture_only",
        "network_access",
        "identity_authority",
        "geometry_authorities",
        "county_crosswalk_authorities",
        "regions",
        "projects",
        "blocked_behaviors",
    }
)
IDENTITY_AUTHORITY_FIELDS = frozenset(
    {
        "authority_id",
        "authority_kind",
        "source_locator",
        "source_observed_date",
        "source_version_posture",
        "record_version",
        "record_digest",
        "digest_scope",
        "record_posture",
        "correction_status",
        "supersedes_ref",
        "source_native_numeric_ids",
        "id_assignment_method",
        "use_boundary",
    }
)
REFERENCE_AUTHORITY_FIELDS = frozenset(
    {
        "authority_id",
        "authority_kind",
        "record_version",
        "record_digest",
        "record_posture",
        "reference_only",
        "use_boundary",
        "correction_status",
        "supersedes_ref",
    }
)
REGION_FIELDS = frozenset(
    {
        "region_id",
        "name",
        "rac_number",
        "geometry_ref",
        "geometry_confidence",
        "county_crosswalk_ref",
        "county_crosswalk_resolution_status",
        "source_ref",
    }
)
PROJECT_FIELDS = frozenset(
    {
        "project_id",
        "award_ref",
        "recipient_ref",
        "recipient_resolution_status",
        "location_ref",
        "geometry_confidence",
        "planning_region_ref",
        "planning_region_resolution_status",
        "source_publication_time",
        "source_ref",
    }
)
PROTECTED_INLINE_KEYS = frozenset(
    {
        "address",
        "bbox",
        "centroid",
        "contains",
        "containment",
        "coordinate",
        "coordinates",
        "counties",
        "county_membership",
        "geometry",
        "geojson",
        "lat",
        "latitude",
        "lng",
        "lon",
        "longitude",
        "multipolygon",
        "polygon",
        "street_address",
        "within",
    }
)
BLOCKED_BEHAVIOR_CODES = {
    "authenticated_portal": "AUTHENTICATED_PORTAL_BEHAVIOR_FORBIDDEN",
    "connector": "CONNECTOR_BEHAVIOR_FORBIDDEN",
    "deployment": "DEPLOYMENT_BEHAVIOR_FORBIDDEN",
    "geocoding": "GEOCODING_BEHAVIOR_FORBIDDEN",
    "geometry_construction": "GEOMETRY_CONSTRUCTION_BEHAVIOR_FORBIDDEN",
    "proof": "PROOF_BEHAVIOR_FORBIDDEN",
    "publication": "PUBLICATION_BEHAVIOR_FORBIDDEN",
    "real_applicant": "REAL_APPLICANT_BEHAVIOR_FORBIDDEN",
    "real_project": "REAL_PROJECT_BEHAVIOR_FORBIDDEN",
    "real_recipient": "REAL_RECIPIENT_BEHAVIOR_FORBIDDEN",
    "release": "RELEASE_BEHAVIOR_FORBIDDEN",
    "source_activation": "SOURCE_ACTIVATION_BEHAVIOR_FORBIDDEN",
}


@dataclass(frozen=True)
class Finding:
    """A finite, non-echoing validation finding."""

    code: str
    path: str


def _canonical_json(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def authority_record_digest(record: Mapping[str, Any]) -> str:
    """Return the digest for a reference-authority record."""

    payload = {key: value for key, value in record.items() if key != "record_digest"}
    return "sha256:" + hashlib.sha256(_canonical_json(payload)).hexdigest()


def identity_record_digest(
    authority: Mapping[str, Any], regions: Sequence[Any]
) -> str:
    """Pin the identity-authority metadata and the ordered RAC identity tuple."""

    authority_payload = {
        key: value for key, value in authority.items() if key != "record_digest"
    }
    identities = []
    for region in regions:
        if isinstance(region, Mapping):
            identities.append(
                {
                    "name": region.get("name"),
                    "rac_number": region.get("rac_number"),
                    "region_id": region.get("region_id"),
                }
            )
        else:
            identities.append(None)
    payload = {"authority": authority_payload, "identities": identities}
    return "sha256:" + hashlib.sha256(_canonical_json(payload)).hexdigest()


def _add(findings: list[Finding], code: str, path: str) -> None:
    findings.append(Finding(code=code, path=path))


def _finish(findings: Iterable[Finding]) -> tuple[Finding, ...]:
    return tuple(
        sorted(set(findings), key=lambda finding: (finding.path, finding.code))
    )


def _unexpected_fields(
    value: Mapping[str, Any],
    allowed: frozenset[str],
    path: str,
    findings: list[Finding],
) -> None:
    for key in sorted(set(value) - allowed):
        _add(findings, "UNEXPECTED_FIELD", f"{path}.{key}")


def _required_fields(
    value: Mapping[str, Any],
    required: Iterable[str],
    path: str,
    findings: list[Finding],
) -> None:
    for key in sorted(set(required) - set(value)):
        _add(findings, "FIELD_REQUIRED", f"{path}.{key}")


def _scan_inline_geometry(
    value: Any, path: str, findings: list[Finding]
) -> None:
    if isinstance(value, Mapping):
        for key in sorted(value):
            child_path = f"{path}.{key}"
            if key.casefold() in PROTECTED_INLINE_KEYS:
                _add(findings, "INLINE_GEOMETRY_OR_INFERENCE_FORBIDDEN", child_path)
            _scan_inline_geometry(value[key], child_path, findings)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _scan_inline_geometry(item, f"{path}[{index}]", findings)


def _valid_digest(value: Any) -> bool:
    return isinstance(value, str) and DIGEST_PATTERN.fullmatch(value) is not None


def _validate_correction(
    record: Mapping[str, Any], path: str, findings: list[Finding]
) -> None:
    status = record.get("correction_status")
    supersedes_ref = record.get("supersedes_ref")
    if status not in {"current", "corrected", "superseded"}:
        _add(findings, "CORRECTION_STATUS_INVALID", f"{path}.correction_status")
    if status == "current" and supersedes_ref is not None:
        _add(findings, "CURRENT_RECORD_HAS_SUPERSESSION", f"{path}.supersedes_ref")
    if status in {"corrected", "superseded"} and not (
        isinstance(supersedes_ref, str) and supersedes_ref
    ):
        _add(findings, "CORRECTION_LINEAGE_REQUIRED", f"{path}.supersedes_ref")


def _validate_identity_authority(
    authority: Any, regions: Sequence[Any], findings: list[Finding]
) -> str | None:
    path = "$.identity_authority"
    if not isinstance(authority, Mapping):
        _add(findings, "IDENTITY_AUTHORITY_TYPE_INVALID", path)
        return None

    _unexpected_fields(authority, IDENTITY_AUTHORITY_FIELDS, path, findings)
    _required_fields(authority, IDENTITY_AUTHORITY_FIELDS, path, findings)

    if authority.get("authority_id") != IDENTITY_AUTHORITY_ID:
        _add(findings, "IDENTITY_AUTHORITY_ID_INVALID", f"{path}.authority_id")
    if authority.get("authority_kind") != "region-identity":
        _add(findings, "IDENTITY_AUTHORITY_KIND_INVALID", f"{path}.authority_kind")
    if authority.get("source_locator") != IDENTITY_SOURCE_LOCATOR:
        _add(findings, "IDENTITY_SOURCE_LOCATOR_INVALID", f"{path}.source_locator")
    if not (
        isinstance(authority.get("source_observed_date"), str)
        and DATE_PATTERN.fullmatch(authority["source_observed_date"])
    ):
        _add(
            findings,
            "IDENTITY_SOURCE_OBSERVED_DATE_INVALID",
            f"{path}.source_observed_date",
        )
    expected_source_version_posture = (
        f"unversioned-public-page:observed-{authority.get('source_observed_date')}"
    )
    if authority.get("source_version_posture") != expected_source_version_posture:
        _add(
            findings,
            "IDENTITY_SOURCE_VERSION_POSTURE_INVALID",
            f"{path}.source_version_posture",
        )
    if not (
        isinstance(authority.get("record_version"), str)
        and authority["record_version"]
    ):
        _add(findings, "AUTHORITY_VERSION_REQUIRED", f"{path}.record_version")
    if authority.get("record_posture") != "source-grounded-candidate":
        _add(findings, "IDENTITY_RECORD_POSTURE_INVALID", f"{path}.record_posture")
    if (
        authority.get("digest_scope")
        != "authority-metadata-and-ordered-id-ordinal-name-tuples"
    ):
        _add(findings, "IDENTITY_DIGEST_SCOPE_INVALID", f"{path}.digest_scope")
    if authority.get("source_native_numeric_ids") is not False:
        _add(
            findings,
            "SOURCE_NATIVE_NUMERIC_ID_CLAIM_FORBIDDEN",
            f"{path}.source_native_numeric_ids",
        )
    if (
        authority.get("id_assignment_method")
        != "kfm-lexicographic-official-name-order-v1"
    ):
        _add(
            findings,
            "IDENTITY_ASSIGNMENT_METHOD_INVALID",
            f"{path}.id_assignment_method",
        )
    if authority.get("use_boundary") != "identity-reference-only":
        _add(findings, "IDENTITY_USE_BOUNDARY_INVALID", f"{path}.use_boundary")
    _validate_correction(authority, path, findings)

    digest = authority.get("record_digest")
    if not _valid_digest(digest):
        _add(findings, "AUTHORITY_DIGEST_INVALID", f"{path}.record_digest")
    elif digest != identity_record_digest(authority, regions):
        _add(findings, "IDENTITY_AUTHORITY_DIGEST_MISMATCH", f"{path}.record_digest")

    authority_id = authority.get("authority_id")
    return authority_id if isinstance(authority_id, str) else None


def _validate_reference_authorities(
    records: Any,
    path: str,
    allowed_kinds: frozenset[str],
    findings: list[Finding],
) -> dict[str, str]:
    valid: dict[str, str] = {}
    if not isinstance(records, list):
        _add(findings, "REFERENCE_AUTHORITY_LIST_INVALID", path)
        return valid

    seen: set[str] = set()
    for index, record in enumerate(records):
        record_path = f"{path}[{index}]"
        record_findings_before = len(findings)
        if not isinstance(record, Mapping):
            _add(findings, "REFERENCE_AUTHORITY_TYPE_INVALID", record_path)
            continue

        _unexpected_fields(record, REFERENCE_AUTHORITY_FIELDS, record_path, findings)
        _required_fields(record, REFERENCE_AUTHORITY_FIELDS, record_path, findings)
        authority_id = record.get("authority_id")
        authority_kind = record.get("authority_kind")

        if not (isinstance(authority_id, str) and authority_id):
            _add(
                findings,
                "REFERENCE_AUTHORITY_ID_REQUIRED",
                f"{record_path}.authority_id",
            )
        elif authority_id in seen:
            _add(
                findings,
                "REFERENCE_AUTHORITY_ID_DUPLICATE",
                f"{record_path}.authority_id",
            )
        else:
            seen.add(authority_id)

        if authority_kind not in allowed_kinds:
            _add(
                findings,
                "REFERENCE_AUTHORITY_KIND_INVALID",
                f"{record_path}.authority_kind",
            )
        if not (
            isinstance(record.get("record_version"), str)
            and record["record_version"]
        ):
            _add(
                findings,
                "AUTHORITY_VERSION_REQUIRED",
                f"{record_path}.record_version",
            )
        if record.get("record_posture") != "synthetic-fixture-only":
            _add(
                findings,
                "REFERENCE_AUTHORITY_POSTURE_INVALID",
                f"{record_path}.record_posture",
            )
        if record.get("reference_only") is not True:
            _add(
                findings,
                "REFERENCE_ONLY_AUTHORITY_REQUIRED",
                f"{record_path}.reference_only",
            )
        if record.get("use_boundary") != "synthetic-test-only":
            _add(
                findings,
                "REFERENCE_AUTHORITY_USE_BOUNDARY_INVALID",
                f"{record_path}.use_boundary",
            )
        _validate_correction(record, record_path, findings)

        digest = record.get("record_digest")
        if not _valid_digest(digest):
            _add(findings, "AUTHORITY_DIGEST_INVALID", f"{record_path}.record_digest")
        elif digest != authority_record_digest(record):
            _add(
                findings,
                "REFERENCE_AUTHORITY_DIGEST_MISMATCH",
                f"{record_path}.record_digest",
            )

        if (
            len(findings) == record_findings_before
            and isinstance(authority_id, str)
            and isinstance(authority_kind, str)
        ):
            valid[authority_id] = authority_kind
    return valid


def _validate_geometry_state(
    record: Mapping[str, Any],
    *,
    ref_key: str,
    confidence_key: str,
    expected_authority_kind: str,
    authorities: Mapping[str, str],
    path: str,
    prefix: str,
    findings: list[Finding],
) -> None:
    confidence = record.get(confidence_key)
    reference = record.get(ref_key)
    confidence_path = f"{path}.{confidence_key}"
    reference_path = f"{path}.{ref_key}"

    if confidence not in {"unresolved", "approximate", "confirmed"}:
        _add(findings, f"{prefix}_GEOMETRY_CONFIDENCE_INVALID", confidence_path)
        return
    if confidence == "unresolved":
        if reference is not None:
            _add(
                findings,
                f"UNRESOLVED_{prefix}_GEOMETRY_HAS_REFERENCE",
                reference_path,
            )
        return
    if not (isinstance(reference, str) and reference):
        _add(findings, f"{prefix}_GEOMETRY_REFERENCE_REQUIRED", reference_path)
        return
    if authorities.get(reference) != expected_authority_kind:
        _add(
            findings,
            f"{prefix}_GEOMETRY_AUTHORITY_UNRESOLVED",
            reference_path,
        )


def _validate_regions(
    regions: Any,
    identity_authority_id: str | None,
    geometry_authorities: Mapping[str, str],
    crosswalk_authorities: Mapping[str, str],
    findings: list[Finding],
) -> set[str]:
    if not isinstance(regions, list):
        _add(findings, "REGION_INVENTORY_TYPE_INVALID", "$.regions")
        return set()

    if len(regions) != 14:
        _add(findings, "REGION_COUNT_NOT_14", "$.regions")

    ids: list[str] = []
    numbers: list[int] = []
    for index, region in enumerate(regions):
        path = f"$.regions[{index}]"
        if not isinstance(region, Mapping):
            _add(findings, "REGION_RECORD_TYPE_INVALID", path)
            continue

        _unexpected_fields(region, REGION_FIELDS, path, findings)
        _required_fields(region, REGION_FIELDS, path, findings)
        region_id = region.get("region_id")
        rac_number = region.get("rac_number")

        valid_region_id = (
            isinstance(region_id, str)
            and REGION_ID_PATTERN.fullmatch(region_id) is not None
        )
        if isinstance(region_id, str):
            ids.append(region_id)
            if region_id.startswith("kwo-gmd-"):
                _add(findings, "REGION_NAMESPACE_FOREIGN", f"{path}.region_id")
            elif (
                RAC_SHAPED_ID_PATTERN.fullmatch(region_id) is not None
                and not valid_region_id
            ):
                _add(findings, "REGION_ID_OUT_OF_RANGE", f"{path}.region_id")
            elif not valid_region_id:
                _add(findings, "REGION_ID_INVALID", f"{path}.region_id")
        else:
            _add(findings, "REGION_ID_INVALID", f"{path}.region_id")

        valid_number = (
            isinstance(rac_number, int)
            and not isinstance(rac_number, bool)
            and 1 <= rac_number <= 14
        )
        if isinstance(rac_number, int) and not isinstance(rac_number, bool):
            numbers.append(rac_number)
        if not valid_number:
            _add(findings, "RAC_NUMBER_OUT_OF_RANGE", f"{path}.rac_number")

        if valid_number and region_id != f"kwo-rac-{rac_number:02d}":
            _add(findings, "REGION_ID_NUMBER_MISMATCH", f"{path}.region_id")

        if (
            valid_region_id
            and region.get("name") != EXPECTED_REGION_NAME_BY_ID[region_id]
        ):
            _add(findings, "REGION_NAME_NOT_SOURCE_GROUNDED", f"{path}.name")

        if region.get("source_ref") != identity_authority_id:
            _add(
                findings,
                "REGION_IDENTITY_AUTHORITY_UNRESOLVED",
                f"{path}.source_ref",
            )

        _validate_geometry_state(
            region,
            ref_key="geometry_ref",
            confidence_key="geometry_confidence",
            expected_authority_kind="region-geometry",
            authorities=geometry_authorities,
            path=path,
            prefix="REGION",
            findings=findings,
        )

        crosswalk_status = region.get("county_crosswalk_resolution_status")
        crosswalk_ref = region.get("county_crosswalk_ref")
        if crosswalk_status not in {"unresolved", "resolved"}:
            _add(
                findings,
                "COUNTY_CROSSWALK_STATUS_INVALID",
                f"{path}.county_crosswalk_resolution_status",
            )
        elif crosswalk_status == "unresolved":
            if crosswalk_ref is not None:
                _add(
                    findings,
                    "UNRESOLVED_COUNTY_CROSSWALK_HAS_REFERENCE",
                    f"{path}.county_crosswalk_ref",
                )
        elif not (isinstance(crosswalk_ref, str) and crosswalk_ref):
            _add(
                findings,
                "COUNTY_CROSSWALK_REFERENCE_REQUIRED",
                f"{path}.county_crosswalk_ref",
            )
        elif crosswalk_authorities.get(crosswalk_ref) != "county-crosswalk":
            _add(
                findings,
                "COUNTY_CROSSWALK_AUTHORITY_UNRESOLVED",
                f"{path}.county_crosswalk_ref",
            )

    id_counts = {region_id: ids.count(region_id) for region_id in set(ids)}
    number_counts = {number: numbers.count(number) for number in set(numbers)}
    for region_id, count in sorted(id_counts.items()):
        if count > 1:
            _add(findings, "REGION_ID_DUPLICATE", f"$.regions[{region_id}]")
    for number, count in sorted(number_counts.items()):
        if count > 1:
            _add(findings, "RAC_NUMBER_DUPLICATE", f"$.regions[{number}]")
    for region_id in EXPECTED_REGION_IDS:
        if region_id not in id_counts:
            _add(findings, "REGION_ID_MISSING", f"$.regions[{region_id}]")
    for number in range(1, 15):
        if number not in number_counts:
            _add(findings, "RAC_NUMBER_MISSING", f"$.regions[{number}]")

    return {region_id for region_id in ids if REGION_ID_PATTERN.fullmatch(region_id)}


def _validate_projects(
    projects: Any,
    region_ids: set[str],
    geometry_authorities: Mapping[str, str],
    findings: list[Finding],
) -> None:
    if not isinstance(projects, list):
        _add(findings, "PROJECT_LIST_TYPE_INVALID", "$.projects")
        return
    if not projects:
        _add(findings, "PROJECT_FIXTURE_REQUIRED", "$.projects")

    required = PROJECT_FIELDS - {"source_publication_time"}
    for index, project in enumerate(projects):
        path = f"$.projects[{index}]"
        if not isinstance(project, Mapping):
            _add(findings, "PROJECT_RECORD_TYPE_INVALID", path)
            continue

        _unexpected_fields(project, PROJECT_FIELDS, path, findings)
        _required_fields(project, required, path, findings)
        project_id = project.get("project_id")
        if not (
            isinstance(project_id, str)
            and project_id
            and "synthetic" in project_id.casefold()
        ):
            _add(findings, "REAL_PROJECT_INPUT_FORBIDDEN", f"{path}.project_id")
        if project.get("recipient_ref") is not None:
            _add(findings, "REAL_RECIPIENT_INPUT_FORBIDDEN", f"{path}.recipient_ref")

        region_status = project.get("planning_region_resolution_status")
        region_ref = project.get("planning_region_ref")
        if region_status not in {"unresolved", "resolved"}:
            _add(
                findings,
                "PROJECT_REGION_STATUS_INVALID",
                f"{path}.planning_region_resolution_status",
            )
        elif region_status == "unresolved":
            if region_ref is not None:
                _add(
                    findings,
                    "UNRESOLVED_PROJECT_REGION_HAS_REFERENCE",
                    f"{path}.planning_region_ref",
                )
        elif not (isinstance(region_ref, str) and region_ref):
            _add(
                findings,
                "PROJECT_REGION_REFERENCE_REQUIRED",
                f"{path}.planning_region_ref",
            )

        if region_ref is not None:
            if isinstance(region_ref, str) and region_ref.startswith("kwo-gmd-"):
                _add(
                    findings,
                    "PROJECT_REGION_NAMESPACE_FOREIGN",
                    f"{path}.planning_region_ref",
                )
            elif not (
                isinstance(region_ref, str)
                and REGION_ID_PATTERN.fullmatch(region_ref)
            ):
                _add(
                    findings,
                    "PROJECT_REGION_REFERENCE_INVALID",
                    f"{path}.planning_region_ref",
                )
            elif region_ref not in region_ids:
                _add(
                    findings,
                    "PROJECT_REGION_AUTHORITY_UNRESOLVED",
                    f"{path}.planning_region_ref",
                )

        _validate_geometry_state(
            project,
            ref_key="location_ref",
            confidence_key="geometry_confidence",
            expected_authority_kind="project-location-geometry",
            authorities=geometry_authorities,
            path=path,
            prefix="PROJECT",
            findings=findings,
        )


def _validate_blocked_behaviors(value: Any, findings: list[Finding]) -> None:
    path = "$.blocked_behaviors"
    if not isinstance(value, Mapping):
        _add(findings, "BLOCKED_BEHAVIORS_TYPE_INVALID", path)
        return
    allowed = frozenset(BLOCKED_BEHAVIOR_CODES)
    _unexpected_fields(value, allowed, path, findings)
    _required_fields(value, allowed, path, findings)
    for key, code in sorted(BLOCKED_BEHAVIOR_CODES.items()):
        if key in value and value[key] is not False:
            _add(findings, code, f"{path}.{key}")


def validate_document(document: Any) -> tuple[Finding, ...]:
    """Validate one parsed geometry-authority fixture envelope."""

    findings: list[Finding] = []
    if not isinstance(document, Mapping):
        return (Finding(code="DOCUMENT_TYPE_INVALID", path="$"),)

    _unexpected_fields(document, TOP_LEVEL_FIELDS, "$", findings)
    _required_fields(document, TOP_LEVEL_FIELDS, "$", findings)
    _scan_inline_geometry(document, "$", findings)

    if document.get("fixture_only") is not True:
        _add(findings, "FIXTURE_ONLY_REQUIRED", "$.fixture_only")
    if document.get("network_access") != "forbidden":
        _add(findings, "NETWORK_ACCESS_FORBIDDEN", "$.network_access")

    regions = document.get("regions")
    regions_for_digest = regions if isinstance(regions, list) else []
    identity_authority_id = _validate_identity_authority(
        document.get("identity_authority"),
        regions_for_digest,
        findings,
    )
    geometry_authorities = _validate_reference_authorities(
        document.get("geometry_authorities"),
        "$.geometry_authorities",
        frozenset({"region-geometry", "project-location-geometry"}),
        findings,
    )
    crosswalk_authorities = _validate_reference_authorities(
        document.get("county_crosswalk_authorities"),
        "$.county_crosswalk_authorities",
        frozenset({"county-crosswalk"}),
        findings,
    )
    region_ids = _validate_regions(
        regions,
        identity_authority_id,
        geometry_authorities,
        crosswalk_authorities,
        findings,
    )
    _validate_projects(
        document.get("projects"),
        region_ids,
        geometry_authorities,
        findings,
    )
    _validate_blocked_behaviors(document.get("blocked_behaviors"), findings)
    return _finish(findings)


def validate_file(path: Path | str) -> tuple[Finding, ...]:
    """Validate one UTF-8 JSON file without exposing its values."""

    input_path = Path(path)
    try:
        if input_path.stat().st_size > MAX_INPUT_BYTES:
            return (Finding(code="INPUT_TOO_LARGE", path="$"),)
        document = json.loads(input_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return (Finding(code="INPUT_NOT_FOUND", path="$"),)
    except (OSError, UnicodeError):
        return (Finding(code="INPUT_READ_ERROR", path="$"),)
    except json.JSONDecodeError:
        return (Finding(code="INVALID_JSON", path="$"),)
    return validate_document(document)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate water-planning region and geometry authority fixtures."
    )
    parser.add_argument("paths", nargs="+", help="JSON fixture files to validate")
    args = parser.parse_args(argv)

    rendered_findings = []
    sorted_paths = sorted(args.paths)
    for file_index, path in enumerate(sorted_paths):
        for finding in validate_file(path):
            rendered_findings.append(
                {
                    "code": finding.code,
                    "file_index": file_index,
                    "path": finding.path,
                }
            )

    if rendered_findings:
        result = {"findings": rendered_findings, "outcome": "VALIDATOR_FAIL"}
        print(json.dumps(result, separators=(",", ":"), sort_keys=True))
        return 1

    result = {"files": len(sorted_paths), "outcome": "VALIDATOR_PASS"}
    print(json.dumps(result, separators=(",", ":"), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
