"""Validate the bounded Fauna public-safe fixture profile.

This validator is deliberately narrower than an OccurrencePublic validator. It
accepts only synthetic, fixture-only candidates that are explicitly ineligible
for promotion or publication. A pass does not establish taxonomic identity,
source admission, rights clearance, sensitivity review, evidence closure,
policy approval, release readiness, or safe public use.

The profile is deterministic, uses only the Python standard library, performs
no network access, and never reads lifecycle or source payloads.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence


FORBIDDEN_LOCATION_KEYS = frozenset(
    {
        "address",
        "coordinates",
        "den",
        "geometry",
        "geohash",
        "hibernaculum",
        "latitude",
        "locality",
        "longitude",
        "nest",
        "private_land_join",
        "roost",
        "site",
        "spawning_site",
        "telemetry",
    }
)

SAFE_SPATIAL_KINDS = frozenset({"withheld"})

ALLOWED_TOP_LEVEL_KEYS = frozenset(
    {
        "evidence_refs",
        "fixture_id",
        "fixture_only",
        "governance",
        "network_access",
        "public_caveats",
        "reality_boundary",
        "record_type",
        "rights_state",
        "sensitivity_state",
        "source_descriptor_ref",
        "source_role",
        "spatial_support",
        "taxon_ref",
        "taxonomy_state",
    }
)

ALLOWED_SPATIAL_KEYS = frozenset({"kind", "label"})

ALLOWED_GOVERNANCE_KEYS = frozenset(
    {
        "correction_state",
        "evidence_state",
        "geoprivacy_state",
        "policy_state",
        "promotion_state",
        "release_state",
        "review_state",
        "rollback_state",
    }
)


@dataclass(frozen=True, order=True)
class Finding:
    """A stable, machine-comparable fixture validation finding."""

    code: str
    path: str


def _is_nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _walk(value: object, path: tuple[str, ...] = ()):
    if isinstance(value, Mapping):
        for key in sorted(value, key=str):
            child_path = (*path, str(key))
            yield child_path, key, value[key]
            yield from _walk(value[key], child_path)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            child_path = (*path, str(index))
            yield child_path, index, item
            yield from _walk(item, child_path)


def _add(findings: list[Finding], code: str, path: str) -> None:
    finding = Finding(code=code, path=path)
    if finding not in findings:
        findings.append(finding)


def validate_candidate(candidate: object) -> tuple[Finding, ...]:
    """Return deterministic findings for one synthetic fixture candidate."""

    findings: list[Finding] = []

    if not isinstance(candidate, Mapping):
        return (Finding("DOCUMENT_NOT_OBJECT", "$"),)

    if candidate.get("record_type") != "fauna_public_safe_validation_candidate":
        _add(findings, "RECORD_TYPE_INVALID", "$.record_type")
    fixture_id = candidate.get("fixture_id")
    if not _is_nonempty_string(fixture_id):
        _add(findings, "FIXTURE_ID_MISSING", "$.fixture_id")
    elif not fixture_id.startswith("fixture:fauna:"):
        _add(findings, "FIXTURE_ID_NOT_SYNTHETIC", "$.fixture_id")
    if candidate.get("fixture_only") is not True:
        _add(findings, "FIXTURE_ONLY_REQUIRED", "$.fixture_only")
    if candidate.get("reality_boundary") != "synthetic-test-fixture":
        _add(findings, "REALITY_BOUNDARY_REQUIRED", "$.reality_boundary")
    if candidate.get("network_access") != "forbidden":
        _add(findings, "NETWORK_ACCESS_NOT_FORBIDDEN", "$.network_access")

    source_ref = candidate.get("source_descriptor_ref")
    if not _is_nonempty_string(source_ref):
        _add(findings, "SOURCE_DESCRIPTOR_REF_MISSING", "$.source_descriptor_ref")
    elif not source_ref.startswith("fixture:source:fauna:"):
        _add(
            findings,
            "SOURCE_DESCRIPTOR_REF_NOT_SYNTHETIC",
            "$.source_descriptor_ref",
        )
    if candidate.get("source_role") != "synthetic":
        _add(findings, "SOURCE_ROLE_NOT_SYNTHETIC", "$.source_role")
    if candidate.get("rights_state") != "fixture-only":
        _add(findings, "RIGHTS_STATE_UNRESOLVED", "$.rights_state")

    taxon_ref = candidate.get("taxon_ref")
    if not _is_nonempty_string(taxon_ref):
        _add(findings, "TAXON_REF_MISSING", "$.taxon_ref")
    elif not taxon_ref.startswith("fixture:taxon:fauna:"):
        _add(findings, "TAXON_REF_NOT_SYNTHETIC", "$.taxon_ref")
    if candidate.get("taxonomy_state") != "synthetic-resolved":
        _add(findings, "TAXONOMY_UNRESOLVED", "$.taxonomy_state")

    if candidate.get("sensitivity_state") != "public-safe-synthetic":
        _add(findings, "SENSITIVITY_NOT_PUBLIC_SAFE", "$.sensitivity_state")

    spatial_support = candidate.get("spatial_support")
    if not isinstance(spatial_support, Mapping):
        _add(findings, "SPATIAL_SUPPORT_NOT_OBJECT", "$.spatial_support")
    else:
        for key in sorted(set(spatial_support) - ALLOWED_SPATIAL_KEYS):
            _add(
                findings,
                "UNDECLARED_SPATIAL_FIELD",
                f"$.spatial_support.{key}",
            )
        if spatial_support.get("kind") not in SAFE_SPATIAL_KINDS:
            _add(
                findings,
                "SPATIAL_SUPPORT_NOT_PUBLIC_SAFE",
                "$.spatial_support.kind",
            )
        label = spatial_support.get("label")
        if not (
            _is_nonempty_string(label)
            and label.startswith("synthetic-area-")
        ):
            _add(
                findings,
                "SPATIAL_SUPPORT_LABEL_INVALID",
                "$.spatial_support.label",
            )

    evidence_refs = candidate.get("evidence_refs")
    if not isinstance(evidence_refs, list) or not evidence_refs:
        _add(findings, "EVIDENCE_REF_MISSING", "$.evidence_refs")
    else:
        for index, evidence_ref in enumerate(evidence_refs):
            if not (
                _is_nonempty_string(evidence_ref)
                and evidence_ref.startswith("fixture:evidence:fauna:")
            ):
                _add(
                    findings,
                    "EVIDENCE_REF_NOT_SYNTHETIC",
                    f"$.evidence_refs.{index}",
                )

    governance = candidate.get("governance")
    if not isinstance(governance, Mapping):
        _add(findings, "GOVERNANCE_STATE_MISSING", "$.governance")
    else:
        for key in sorted(set(governance) - ALLOWED_GOVERNANCE_KEYS):
            _add(
                findings,
                "UNDECLARED_GOVERNANCE_FIELD",
                f"$.governance.{key}",
            )
        required_states = {
            "evidence_state": ("fixture-only", "EVIDENCE_STATE_UNRESOLVED"),
            "policy_state": (
                "not-evaluated-fixture",
                "POLICY_STATE_UNRESOLVED",
            ),
            "geoprivacy_state": (
                "not-applicable-no-location",
                "GEOPRIVACY_STATE_UNRESOLVED",
            ),
            "review_state": ("fixture-only", "REVIEW_STATE_NOT_FIXTURE_ONLY"),
            "release_state": ("not-released", "RELEASE_STATE_NOT_HELD"),
            "promotion_state": (
                "not-eligible",
                "PROMOTION_STATE_NOT_HELD",
            ),
            "correction_state": (
                "fixture-only",
                "CORRECTION_STATE_NOT_FIXTURE_ONLY",
            ),
            "rollback_state": (
                "fixture-only",
                "ROLLBACK_STATE_NOT_FIXTURE_ONLY",
            ),
        }
        for field, (expected, code) in required_states.items():
            if governance.get(field) != expected:
                _add(findings, code, f"$.governance.{field}")

    for key in sorted(set(candidate) - ALLOWED_TOP_LEVEL_KEYS):
        _add(findings, "UNDECLARED_TOP_LEVEL_FIELD", f"$.{key}")

    for path, key, value in _walk(candidate):
        dotted_path = "$." + ".".join(path)
        if isinstance(key, str) and key.lower() in FORBIDDEN_LOCATION_KEYS:
            _add(findings, "PRECISE_LOCATION_FIELD_FORBIDDEN", dotted_path)
        if isinstance(value, str) and value.lower().startswith(
            ("http://", "https://")
        ):
            _add(findings, "LIVE_URL_FORBIDDEN", dotted_path)

    return tuple(sorted(findings))


def validate_file(path: Path) -> tuple[Finding, ...]:
    """Load and validate one UTF-8 JSON fixture."""

    try:
        candidate = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return (Finding("FIXTURE_JSON_INVALID", "$"),)
    return validate_candidate(candidate)


def _serialize(path: Path, findings: Sequence[Finding]) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in findings
            ],
            "outcome": "PASS" if not findings else "FAIL",
            "scope": "synthetic-public-safe-fixture-only",
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate synthetic Fauna public-safe fixtures."
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        findings = validate_file(path)
        print(_serialize(path, findings))
        failed = failed or bool(findings)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
