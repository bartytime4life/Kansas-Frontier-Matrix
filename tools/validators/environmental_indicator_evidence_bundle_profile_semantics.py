"""Semantic checks for fixture-only environmental-indicator EvidenceBundle profiles.

The functions in this module operate on in-memory synthetic candidates. They
perform deterministic local checks only and create no source, observation,
evidence-resolution, policy, review, lifecycle, release, or publication authority.
"""

from __future__ import annotations

import sys
from collections.abc import Mapping
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages" / "hashing" / "src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import CanonicalizationFailure, compute_spec_hash
from tools.validators.environmental_indicator_evidence_bundle_profile_model import (
    Finding,
    _hash_projection,
    _is_placeholder_hash,
    _list,
    _mapping,
    _parse_aware_datetime,
    _reference_ids,
    _stored_hash,
    _string_list,
)
from tools.validators.environmental_indicator_evidence_bundle_profile_ordering import (
    _ordering_findings,
)


def semantic_findings(
    candidate: Mapping[str, object],
) -> tuple[set[Finding], str | None, str | None]:
    findings: set[Finding] = set()
    analysis_id = candidate.get("analysis_id")
    indicator = _mapping(candidate.get("environmental_indicator"))
    bundle = _mapping(candidate.get("bundle"))
    source = _mapping(indicator.get("source"))
    threshold_profile = _mapping(indicator.get("threshold_profile"))
    summary = _mapping(indicator.get("cluster_summary"))
    rows = [_mapping(item) for item in _list(indicator.get("ranked_rows"))]
    clusters = [_mapping(item) for item in _list(summary.get("clusters"))]
    counties = _string_list(indicator.get("county_fips"))

    findings.update(_ordering_findings(indicator, bundle))

    source_time = _parse_aware_datetime(source.get("source_time"))
    retrieved_at = _parse_aware_datetime(source.get("retrieved_at"))
    computed_at = _parse_aware_datetime(indicator.get("computed_at"))
    if (
        source_time is not None
        and retrieved_at is not None
        and source_time > retrieved_at
    ):
        findings.add(Finding("SOURCE_TIME_ORDER_INVALID", "/environmental_indicator/source/retrieved_at"))
    if (
        retrieved_at is not None
        and computed_at is not None
        and retrieved_at > computed_at
    ):
        findings.add(Finding("COMPUTED_BEFORE_RETRIEVAL", "/environmental_indicator/computed_at"))

    asset_refs = _string_list(source.get("asset_refs"))
    etag_digests = _string_list(source.get("etag_digests"))
    if len(asset_refs) != len(etag_digests):
        findings.add(
            Finding(
                "ASSET_ETAG_CARDINALITY_MISMATCH",
                "/environmental_indicator/source/etag_digests",
            )
        )

    for index, digest in enumerate(etag_digests):
        if _is_placeholder_hash(digest):
            findings.add(
                Finding(
                    "DIGEST_PLACEHOLDER_DENIED",
                    f"/environmental_indicator/source/etag_digests/{index}",
                )
            )

    try:
        expected_threshold_hash = compute_spec_hash(_hash_projection(threshold_profile))
    except (CanonicalizationFailure, TypeError, ValueError):
        findings.add(
            Finding(
                "CANONICALIZATION_ERROR",
                "/environmental_indicator/threshold_profile",
            )
        )
        expected_threshold_hash = None
    stored_threshold_hash = _stored_hash(threshold_profile.get("spec_hash"))
    if expected_threshold_hash is not None and stored_threshold_hash != expected_threshold_hash:
        findings.add(
            Finding(
                "THRESHOLD_PROFILE_HASH_MISMATCH",
                "/environmental_indicator/threshold_profile/spec_hash/value",
            )
        )

    evidence_ids, evidence_set, _ = _reference_ids(bundle)
    for index, row in enumerate(rows):
        row_refs = set(_string_list(row.get("evidence_ref_ids")))
        if not row_refs or not row_refs.issubset(evidence_set):
            findings.add(
                Finding(
                    "EVIDENCE_REF_UNRESOLVED",
                    f"/environmental_indicator/ranked_rows/{index}/evidence_ref_ids",
                )
            )
    for index, cluster in enumerate(clusters):
        cluster_refs = set(_string_list(cluster.get("evidence_ref_ids")))
        if not cluster_refs or not cluster_refs.issubset(evidence_set):
            findings.add(
                Finding(
                    "EVIDENCE_REF_UNRESOLVED",
                    f"/environmental_indicator/cluster_summary/clusters/{index}/evidence_ref_ids",
                )
            )

    if summary.get("cluster_count") != len(clusters):
        findings.add(
            Finding(
                "CLUSTER_COUNT_MISMATCH",
                "/environmental_indicator/cluster_summary/cluster_count",
            )
        )

    county_set = set(counties)
    ranked_counties = [
        row.get("county_fips")
        for row in rows
        if isinstance(row.get("county_fips"), str)
    ]
    if len(ranked_counties) != len(set(ranked_counties)):
        findings.add(
            Finding(
                "RANKED_COUNTY_DUPLICATE",
                "/environmental_indicator/ranked_rows",
            )
        )
    if not set(ranked_counties).issubset(county_set):
        findings.add(
            Finding(
                "RANKED_COUNTY_SCOPE_INVALID",
                "/environmental_indicator/ranked_rows",
            )
        )

    cluster_members: list[str] = []
    for index, cluster in enumerate(clusters):
        member_counties = _string_list(cluster.get("county_fips"))
        cluster_members.extend(member_counties)
        if cluster.get("member_count") != len(member_counties):
            findings.add(
                Finding(
                    "CLUSTER_MEMBER_COUNT_MISMATCH",
                    f"/environmental_indicator/cluster_summary/clusters/{index}/member_count",
                )
            )
        if not set(member_counties).issubset(county_set):
            findings.add(
                Finding(
                    "CLUSTER_COUNTY_SCOPE_INVALID",
                    f"/environmental_indicator/cluster_summary/clusters/{index}/county_fips",
                )
            )

    if len(cluster_members) != len(set(cluster_members)):
        findings.add(
            Finding(
                "CLUSTER_MEMBERSHIP_OVERLAP",
                "/environmental_indicator/cluster_summary/clusters",
            )
        )

    data_state = indicator.get("data_state")
    if data_state == "POPULATED":
        populated_valid = (
            bool(counties)
            and bool(rows)
            and bool(clusters)
            and set(ranked_counties) == county_set
            and set(cluster_members) == county_set
        )
        if not populated_valid:
            findings.add(
                Finding(
                    "DATA_STATE_CONTENT_INVALID",
                    "/environmental_indicator/data_state",
                )
            )
    elif data_state in {"EMPTY", "NO_DATA"}:
        if (
            counties
            or rows
            or clusters
            or summary.get("cluster_count") != 0
        ):
            findings.add(
                Finding(
                    "DATA_STATE_CONTENT_INVALID",
                    "/environmental_indicator/data_state",
                )
            )

    source_descriptor_ref = source.get("source_descriptor_ref")
    source_records = _string_list(bundle.get("source_records"))
    if not isinstance(source_descriptor_ref, str) or source_descriptor_ref not in source_records:
        findings.add(Finding("SOURCE_RECORD_BINDING_INVALID", "/bundle/source_records"))

    try:
        expected_indicator_hash = compute_spec_hash(_hash_projection(indicator))
    except (CanonicalizationFailure, TypeError, ValueError):
        findings.add(Finding("CANONICALIZATION_ERROR", "/environmental_indicator"))
        expected_indicator_hash = None

    stored_indicator_hash = _stored_hash(indicator.get("spec_hash"))
    if (
        expected_indicator_hash is not None
        and stored_indicator_hash != expected_indicator_hash
    ):
        findings.add(
            Finding(
                "INDICATOR_SPEC_HASH_MISMATCH",
                "/environmental_indicator/spec_hash/value",
            )
        )

    if expected_indicator_hash is not None:
        expected_analysis_id = "kfm:environmental-indicator:" + expected_indicator_hash
        if analysis_id != expected_analysis_id:
            findings.add(Finding("ANALYSIS_ID_MISMATCH", "/analysis_id"))
        checksums = _mapping(bundle.get("checksums"))
        if checksums.get("environmental_indicator_profile") != expected_indicator_hash:
            findings.add(
                Finding(
                    "BUNDLE_INDICATOR_CHECKSUM_MISMATCH",
                    "/bundle/checksums/environmental_indicator_profile",
                )
            )
        if bundle.get("claim_scope") != f"environmental_indicator:{expected_analysis_id}":
            findings.add(Finding("CLAIM_SCOPE_BINDING_INVALID", "/bundle/claim_scope"))

    try:
        expected_bundle_hash = compute_spec_hash(_hash_projection(bundle))
    except (CanonicalizationFailure, TypeError, ValueError):
        findings.add(Finding("CANONICALIZATION_ERROR", "/bundle"))
        expected_bundle_hash = None

    stored_bundle_hash = _stored_hash(bundle.get("spec_hash"))
    if expected_bundle_hash is not None and stored_bundle_hash != expected_bundle_hash:
        findings.add(Finding("BUNDLE_SPEC_HASH_MISMATCH", "/bundle/spec_hash/value"))

    digest_values = [
        stored_threshold_hash,
        stored_indicator_hash,
        stored_bundle_hash,
    ]
    digest_values.extend(
        value
        for value in _mapping(bundle.get("checksums")).values()
        if isinstance(value, str)
    )
    if any(_is_placeholder_hash(value) for value in digest_values):
        findings.add(Finding("DIGEST_PLACEHOLDER_DENIED", "/"))

    return findings, (
        expected_indicator_hash if expected_indicator_hash is not None else None
    ), (
        expected_bundle_hash if expected_bundle_hash is not None else None
   )


