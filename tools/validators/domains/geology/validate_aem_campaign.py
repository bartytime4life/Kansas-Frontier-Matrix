#!/usr/bin/env python3
"""Validate one frozen, announcement-bound GMD 3 AEM candidate profile.

The profile binds a document-specific 2026-05-11 KU News announcement. It
records the source-reported historical posture, keeps current campaign state
unknown, binds no acquisition or product evidence, and performs no network
access. The linked SourceDescriptor is an exact fixture input, not registry or
release authority.
"""

from __future__ import annotations

from datetime import datetime
import hashlib
from pathlib import Path
import re
import sys
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    find_undeclared_fields,
    is_nonempty_string,
    run_cli,
    validate_fixture_file,
)


PROFILE_ID = "kfm-geology-gmd3-aem-campaign-candidate-fixture-v1"
EXPECTED_CAMPAIGN_ID = (
    "kfm:geology:aem-campaign-candidate:"
    "ku-news-gmd3-announcement-2026-05-11"
)
EXPECTED_SOURCE_DESCRIPTOR_REF = (
    "src:ku-news-gmd3-aem-announcement-2026-05-11"
)
EXPECTED_SOURCE_DESCRIPTOR_VERSION = "0.3.0"
EXPECTED_SOURCE_DESCRIPTOR_SHA256 = (
    "31c9517dc042817fa280c19f370e9c3ef48e55855c421da983dcdadfff4e0e26"
)
EXPECTED_DOCUMENTATION_URL = (
    "https://news.ku.edu/news/article/airborne-electromagnetic-survey-of-"
    "ogallala-aquifer-conditions-planned-in-southwest-kansas-"
    "ARTICLE-B0R8YR-ARTICLE-B0R8YR"
)
DEFAULT_SOURCE_DESCRIPTOR_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/source/source_descriptor/valid/"
    "valid_ku_news_gmd3_aem_announcement_2026_05_11.json"
)
EXPECTED_REFERENCE_CANDIDATES = [
    "fixture://reference-candidate/geology/gmd3-aem/"
    "ku-news-announcement-2026-05-11"
]
REFERENCE_CANDIDATE_PATTERN = re.compile(
    r"^fixture://reference-candidate/geology/gmd3-aem/"
    r"[a-z0-9][a-z0-9._/-]{2,127}$"
)
CORRECTION_REF_PATTERN = re.compile(
    r"^kfm:geology:aem-campaign-candidate:[a-z0-9][a-z0-9._:-]{2,127}$"
)

ALLOWED_TOP_LEVEL_FIELDS = frozenset(
    {
        "profile_id",
        "id",
        "object_type",
        "source_descriptor_ref",
        "announcement_reported_state",
        "announcement_published_on",
        "current_campaign_state",
        "acquisition_evidence_state",
        "survey_method",
        "claim_scope",
        "supporting_reference_candidates",
        "review_state",
        "release_state",
        "limitations",
        "correction",
    }
)
FORBIDDEN_AMBIGUOUS_FIELDS = frozenset(
    {
        "campaign_state",
        "acquisition_state",
        "survey_counties",
        "planned_target_depth",
    }
)
FORBIDDEN_DOWNSTREAM_STAGE_FIELDS = frozenset(
    {
        "product_id",
        "horizontal_crs",
        "vertical_datum",
        "depth_reference",
        "depth_positive_direction",
        "processing_software_version",
        "inversion_software_version",
        "raw_source_ref",
        "resistivity_units",
        "no_data_value",
        "uncertainty",
        "frequency_system_ref",
        "footprint_geometry_ref",
    }
)
ALLOWED_CORRECTION_FIELDS = frozenset(
    {"supersedes_ref", "reason", "correction_time"}
)
REQUIRED_LIMITATIONS = [
    "fixture_profile_only",
    "announcement_context_only",
    "current_campaign_state_unknown",
    "no_acquisition_evidence_bound",
    "no_processing_or_inversion_product_evidence_bound",
    "not_a_groundwater_level_observation",
    "not_a_water_right_title_or_legal_record",
    "not_released",
]
EXPECTED_DESCRIPTOR_ALLOWED_ROLES = [
    "candidate_signal",
    "citation_support",
    "historical_context",
]
EXPECTED_DESCRIPTOR_PROHIBITED_ROLES = [
    "legal_status",
    "regulatory_context",
    "observed_event",
    "observation",
    "operational_context",
    "map_display",
]


def _is_utc_seconds_timestamp(value: object) -> bool:
    if not is_nonempty_string(value):
        return False
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return False
    return True


def _validate_declared_fields(
    findings: set[Finding], candidate: dict[object, object]
) -> None:
    for key in sorted(
        candidate,
        key=lambda value: (type(value).__name__, repr(value)),
    ):
        if key in ALLOWED_TOP_LEVEL_FIELDS:
            continue
        if key in FORBIDDEN_AMBIGUOUS_FIELDS:
            code = "AEM_AMBIGUOUS_ANNOUNCEMENT_FIELD_DENIED"
        elif key in FORBIDDEN_DOWNSTREAM_STAGE_FIELDS:
            code = "AEM_DOWNSTREAM_STAGE_FIELD_DENIED"
        else:
            code = "AEM_UNDECLARED_TOP_LEVEL_FIELD"
        add_finding(findings, code, f"$.{key}")


def _validate_reference_candidates(
    findings: set[Finding], value: object
) -> None:
    if (
        not isinstance(value, list)
        or len(value) != 1
        or not all(is_nonempty_string(item) for item in value)
    ):
        add_finding(
            findings,
            "AEM_REFERENCE_CANDIDATES_INVALID",
            "$.supporting_reference_candidates",
        )
        return
    for index, item in enumerate(value):
        if REFERENCE_CANDIDATE_PATTERN.fullmatch(item) is None:
            add_finding(
                findings,
                "AEM_REFERENCE_CANDIDATE_SCHEME_INVALID",
                f"$.supporting_reference_candidates[{index}]",
            )
            return
    if value != EXPECTED_REFERENCE_CANDIDATES:
        add_finding(
            findings,
            "AEM_REFERENCE_CANDIDATE_IDENTITY_INVALID",
            "$.supporting_reference_candidates",
        )


def _validate_correction(
    findings: set[Finding],
    correction: object,
    campaign_id: object,
) -> None:
    if not isinstance(correction, dict):
        add_finding(findings, "AEM_CORRECTION_INVALID", "$.correction")
        return
    find_undeclared_fields(
        findings,
        correction,
        ALLOWED_CORRECTION_FIELDS,
        "AEM_UNDECLARED_CORRECTION_FIELD",
        "$.correction",
    )
    supersedes_ref = correction.get("supersedes_ref")
    if not is_nonempty_string(supersedes_ref):
        add_finding(
            findings,
            "AEM_SUPERSEDES_REF_MISSING",
            "$.correction.supersedes_ref",
        )
    elif CORRECTION_REF_PATTERN.fullmatch(supersedes_ref) is None:
        add_finding(
            findings,
            "AEM_CORRECTION_REFERENCE_SCHEME_INVALID",
            "$.correction.supersedes_ref",
        )
    elif supersedes_ref == campaign_id:
        add_finding(
            findings,
            "AEM_SELF_SUPERSESSION_DENIED",
            "$.correction.supersedes_ref",
        )
    if not is_nonempty_string(correction.get("reason")):
        add_finding(
            findings,
            "AEM_CORRECTION_REASON_INVALID",
            "$.correction.reason",
        )
    if "correction_time" in correction and not _is_utc_seconds_timestamp(
        correction["correction_time"]
    ):
        add_finding(
            findings,
            "AEM_CORRECTION_TIME_INVALID",
            "$.correction.correction_time",
        )


def validate_candidate(candidate: object) -> list[Finding]:
    """Return sorted findings for one frozen campaign-candidate fixture."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("CANDIDATE_NOT_OBJECT", "$")]
    _validate_declared_fields(findings, candidate)
    expected_values = {
        "profile_id": (PROFILE_ID, "AEM_PROFILE_ID_INVALID"),
        "id": (EXPECTED_CAMPAIGN_ID, "AEM_CAMPAIGN_ID_INVALID"),
        "object_type": ("AemSurveyCampaign", "AEM_OBJECT_TYPE_INVALID"),
        "source_descriptor_ref": (
            EXPECTED_SOURCE_DESCRIPTOR_REF,
            "AEM_SOURCE_DESCRIPTOR_REF_INVALID",
        ),
        "announcement_reported_state": (
            "planned",
            "AEM_ANNOUNCEMENT_REPORTED_STATE_INVALID",
        ),
        "announcement_published_on": (
            "2026-05-11",
            "AEM_ANNOUNCEMENT_DATE_INVALID",
        ),
        "current_campaign_state": (
            "unknown",
            "AEM_CURRENT_CAMPAIGN_STATE_INVALID",
        ),
        "acquisition_evidence_state": (
            "not_bound_to_profile",
            "AEM_ACQUISITION_EVIDENCE_STATE_INVALID",
        ),
        "survey_method": (
            "airborne_electromagnetic",
            "AEM_SURVEY_METHOD_INVALID",
        ),
        "claim_scope": (
            "campaign_announcement",
            "AEM_CLAIM_SCOPE_INVALID",
        ),
        "review_state": ("needs_review", "AEM_REVIEW_STATE_INVALID"),
        "release_state": (
            "not_released",
            "AEM_DISABLED_PROFILE_RELEASE_DENIED",
        ),
    }
    for field, (wanted, code) in expected_values.items():
        if candidate.get(field) != wanted:
            add_finding(findings, code, f"$.{field}")

    _validate_reference_candidates(
        findings,
        candidate.get("supporting_reference_candidates"),
    )
    limitations = candidate.get("limitations")
    if (
        not isinstance(limitations, list)
        or not all(is_nonempty_string(item) for item in limitations)
        or len(limitations) != len(set(limitations))
    ):
        add_finding(findings, "AEM_LIMITATIONS_INVALID", "$.limitations")
    elif limitations != REQUIRED_LIMITATIONS:
        add_finding(
            findings,
            "AEM_REQUIRED_LIMITATION_MISSING",
            "$.limitations",
        )
    if "correction" in candidate:
        _validate_correction(findings, candidate["correction"], candidate.get("id"))
    return sorted(findings)


def _validate_descriptor_access(
    findings: set[Finding], candidate: dict[object, object], prefix: str
) -> None:
    access = candidate.get("access")
    if not isinstance(access, dict):
        add_finding(findings, "AEM_SOURCE_ACCESS_BLOCK_INVALID", f"{prefix}.access")
        return
    allowed_fields = {
        "access_method",
        "access_posture",
        "endpoints",
        "rate_limit_notes",
    }
    if any(field not in allowed_fields for field in access):
        add_finding(
            findings,
            "AEM_SOURCE_CREDENTIALLED_ACCESS_DENIED",
            f"{prefix}.access",
        )
    if (
        access.get("access_method") != "manual_archive"
        or access.get("access_posture") != "restricted"
    ):
        add_finding(
            findings,
            "AEM_SOURCE_ACCESS_POSTURE_INVALID",
            f"{prefix}.access",
        )
    expected_endpoints = [
        {
            "label": "KU News announcement published 2026-05-11",
            "uri": EXPECTED_DOCUMENTATION_URL,
            "purpose": "documentation",
        }
    ]
    if access.get("endpoints") != expected_endpoints:
        add_finding(
            findings,
            "AEM_LIVE_DATA_ENDPOINT_DENIED",
            f"{prefix}.access.endpoints",
        )


def _validate_descriptor_governance(
    findings: set[Finding], candidate: dict[object, object], prefix: str
) -> None:
    admissibility = candidate.get("admissibility_limits")
    if not isinstance(admissibility, dict):
        add_finding(
            findings,
            "AEM_SOURCE_ADMISSIBILITY_BLOCK_INVALID",
            f"{prefix}.admissibility_limits",
        )
    else:
        if admissibility.get("allowed_claim_roles") != EXPECTED_DESCRIPTOR_ALLOWED_ROLES:
            add_finding(
                findings,
                "AEM_SOURCE_ALLOWED_CLAIM_ROLES_INVALID",
                f"{prefix}.admissibility_limits.allowed_claim_roles",
            )
        if (
            admissibility.get("prohibited_claim_roles")
            != EXPECTED_DESCRIPTOR_PROHIBITED_ROLES
        ):
            add_finding(
                findings,
                "AEM_SOURCE_PROHIBITED_CLAIM_ROLES_INVALID",
                f"{prefix}.admissibility_limits.prohibited_claim_roles",
            )
        if admissibility.get("confidence_posture") != "candidate_only":
            add_finding(
                findings,
                "AEM_SOURCE_CONFIDENCE_POSTURE_INVALID",
                f"{prefix}.admissibility_limits.confidence_posture",
            )
        for field in (
            "review_required_before_use",
            "review_required_before_publication",
        ):
            if admissibility.get(field) is not True:
                add_finding(
                    findings,
                    "AEM_SOURCE_REVIEW_REQUIREMENT_MISSING",
                    f"{prefix}.admissibility_limits.{field}",
                )

    public_release = candidate.get("public_release")
    if not isinstance(public_release, dict):
        add_finding(findings, "AEM_PUBLIC_RELEASE_BLOCK_INVALID", f"{prefix}.public_release")
    else:
        for field, wanted in {
            "allowed": False,
            "requires_review": True,
            "redaction_required": True,
        }.items():
            if public_release.get(field) is not wanted:
                add_finding(
                    findings,
                    "AEM_PUBLIC_RELEASE_POSTURE_INVALID",
                    f"{prefix}.public_release.{field}",
                )
        conditions = public_release.get("release_conditions")
        if (
            not isinstance(conditions, list)
            or not conditions
            or not all(is_nonempty_string(item) for item in conditions)
        ):
            add_finding(
                findings,
                "AEM_PUBLIC_RELEASE_CONDITIONS_MISSING",
                f"{prefix}.public_release.release_conditions",
            )

    connectors = candidate.get("connectors")
    if not isinstance(connectors, dict):
        add_finding(
            findings,
            "AEM_CONNECTOR_NOT_DISABLED",
            f"{prefix}.connectors.activation_state",
        )
    else:
        if connectors.get("activation_state") != "disabled":
            add_finding(
                findings,
                "AEM_CONNECTOR_NOT_DISABLED",
                f"{prefix}.connectors.activation_state",
            )
        if any(
            field not in {"activation_state", "activation_notes"}
            for field in connectors
        ):
            add_finding(
                findings,
                "AEM_CONNECTOR_REFERENCE_DENIED",
                f"{prefix}.connectors",
            )


def validate_source_descriptor(candidate: object) -> list[Finding]:
    """Validate the document-specific, candidate-only descriptor posture."""

    findings: set[Finding] = set()
    prefix = "$.profile.source_descriptor"
    if not isinstance(candidate, dict):
        return [Finding("AEM_SOURCE_DESCRIPTOR_NOT_OBJECT", prefix)]
    expected_values = {
        "object_type": ("SourceDescriptor", "AEM_SOURCE_DESCRIPTOR_OBJECT_TYPE_INVALID"),
        "source_id": (EXPECTED_SOURCE_DESCRIPTOR_REF, "AEM_SOURCE_DESCRIPTOR_ID_INVALID"),
        "descriptor_version": (
            EXPECTED_SOURCE_DESCRIPTOR_VERSION,
            "AEM_SOURCE_DESCRIPTOR_VERSION_INVALID",
        ),
        "source_type": ("bibliography_or_report", "AEM_SOURCE_TYPE_INVALID"),
        "source_role": ("citation_source", "AEM_SOURCE_ROLE_UPCAST_DENIED"),
        "authority_rank": ("candidate_only", "AEM_SOURCE_AUTHORITY_UPCAST_DENIED"),
        "sensitivity_default": ("restricted", "AEM_SOURCE_SENSITIVITY_INVALID"),
        "review_state": ("needs_review", "AEM_SOURCE_REVIEW_STATE_INVALID"),
        "release_state": ("not_released", "AEM_SOURCE_RELEASE_STATE_INVALID"),
    }
    for field, (wanted, code) in expected_values.items():
        if candidate.get(field) != wanted:
            add_finding(findings, code, f"{prefix}.{field}")
    if candidate.get("domain_scope") != ["geology", "hydrology"]:
        add_finding(findings, "AEM_SOURCE_DOMAIN_SCOPE_INVALID", f"{prefix}.domain_scope")

    rights = candidate.get("rights")
    if not isinstance(rights, dict):
        add_finding(findings, "AEM_SOURCE_RIGHTS_BLOCK_INVALID", f"{prefix}.rights")
    else:
        for field, wanted in {
            "rights_status": "unknown",
            "redistribution_allowed": "unknown",
            "commercial_use_allowed": "unknown",
        }.items():
            if rights.get(field) != wanted:
                add_finding(
                    findings,
                    "AEM_SOURCE_RIGHTS_UNRESOLVED_POSTURE_INVALID",
                    f"{prefix}.rights.{field}",
                )

    cadence = candidate.get("cadence")
    if (
        not isinstance(cadence, dict)
        or cadence.get("update_cadence") != "static"
        or cadence.get("staleness_policy") != "deny_publication"
    ):
        add_finding(findings, "AEM_SOURCE_CADENCE_POSTURE_INVALID", f"{prefix}.cadence")

    _validate_descriptor_access(findings, candidate, prefix)
    _validate_descriptor_governance(findings, candidate, prefix)

    source_head = candidate.get("source_head")
    if not isinstance(source_head, dict):
        add_finding(findings, "AEM_SOURCE_HEAD_INVALID", f"{prefix}.source_head")
    else:
        if source_head.get("method") != "manual_review":
            add_finding(
                findings,
                "AEM_SOURCE_HEAD_LIVE_FETCH_DENIED",
                f"{prefix}.source_head.method",
            )
        if any(
            field
            not in {"observed_at", "method", "content_identity", "source_head_notes"}
            for field in source_head
        ):
            add_finding(
                findings,
                "AEM_SOURCE_HEAD_FIELD_DENIED",
                f"{prefix}.source_head",
            )

    lifecycle = candidate.get("lifecycle")
    if not isinstance(lifecycle, dict) or lifecycle.get("registry_state") != "proposed":
        add_finding(
            findings,
            "AEM_SOURCE_REGISTRY_STATE_NOT_PROPOSED",
            f"{prefix}.lifecycle.registry_state",
        )
    return sorted(findings)


def _decode_fixture(path: Path | str) -> tuple[object | None, list[Finding]]:
    captured: list[object] = []

    def capture(candidate: object) -> list[Finding]:
        captured.append(candidate)
        return []

    findings = validate_fixture_file(path, capture)
    return (captured[0] if captured else None, findings)


def validate_file(
    path: Path | str,
    *,
    source_descriptor_path: Path | str = DEFAULT_SOURCE_DESCRIPTOR_PATH,
) -> list[Finding]:
    """Validate one candidate plus its exact descriptor-fixture posture."""

    campaign, campaign_parse_findings = _decode_fixture(path)
    if campaign_parse_findings:
        return campaign_parse_findings
    descriptor, descriptor_parse_findings = _decode_fixture(source_descriptor_path)
    if descriptor_parse_findings:
        return [
            Finding(
                "AEM_SOURCE_DESCRIPTOR_FIXTURE_INVALID",
                "$.profile.source_descriptor",
            )
        ]

    findings = validate_candidate(campaign)
    findings.extend(validate_source_descriptor(descriptor))
    descriptor_digest = hashlib.sha256(
        Path(source_descriptor_path).read_bytes()
    ).hexdigest()
    if descriptor_digest != EXPECTED_SOURCE_DESCRIPTOR_SHA256:
        findings.append(
            Finding(
                "AEM_SOURCE_DESCRIPTOR_CONTENT_DRIFT",
                "$.profile.source_descriptor",
            )
        )
    if isinstance(campaign, dict) and isinstance(descriptor, dict):
        if campaign.get("source_descriptor_ref") != descriptor.get("source_id"):
            findings.append(
                Finding(
                    "AEM_CAMPAIGN_SOURCE_BINDING_INVALID",
                    "$.source_descriptor_ref",
                )
            )
    return sorted(set(findings))


def main(argv: Sequence[str] | None = None) -> int:
    return run_cli(
        argv=argv,
        description="Validate the frozen GMD 3 AEM announcement candidate.",
        scope="geology-gmd3-aem-announcement-candidate-fixture",
        validator=validate_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
