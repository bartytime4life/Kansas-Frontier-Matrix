"""Deterministic ordering checks for the environmental profile."""

from __future__ import annotations

from collections.abc import Mapping

from tools.validators.environmental_indicator_evidence_bundle_profile_model import (
    Finding,
    _list,
    _mapping,
    _reference_ids,
    _string_list,
)


def _ordering_findings(
    indicator: Mapping[str, object],
    bundle: Mapping[str, object],
) -> set[Finding]:
    findings: set[Finding] = set()

    thresholds = [_mapping(item) for item in _list(indicator.get("thresholds"))]
    threshold_ids = [
        item.get("threshold_id")
        for item in thresholds
        if isinstance(item.get("threshold_id"), str)
    ]
    if threshold_ids != sorted(threshold_ids) or len(threshold_ids) != len(
        set(threshold_ids)
    ):
        findings.add(Finding("THRESHOLD_ORDER_INVALID", "/environmental_indicator/thresholds"))

    counties = _string_list(indicator.get("county_fips"))
    if counties != sorted(counties) or len(counties) != len(set(counties)):
        findings.add(Finding("COUNTY_ORDER_INVALID", "/environmental_indicator/county_fips"))

    rows = [_mapping(item) for item in _list(indicator.get("ranked_rows"))]
    ranks = [item.get("rank") for item in rows]
    if ranks != list(range(1, len(rows) + 1)):
        findings.add(Finding("RANK_SEQUENCE_INVALID", "/environmental_indicator/ranked_rows"))

    for index, row in enumerate(rows):
        refs = _string_list(row.get("evidence_ref_ids"))
        if refs != sorted(refs) or len(refs) != len(set(refs)):
            findings.add(
                Finding(
                    "REFERENCE_ORDER_INVALID",
                    f"/environmental_indicator/ranked_rows/{index}/evidence_ref_ids",
                )
            )

    summary = _mapping(indicator.get("cluster_summary"))
    clusters = [_mapping(item) for item in _list(summary.get("clusters"))]
    cluster_ids = [
        item.get("cluster_id")
        for item in clusters
        if isinstance(item.get("cluster_id"), str)
    ]
    if cluster_ids != sorted(cluster_ids) or len(cluster_ids) != len(set(cluster_ids)):
        findings.add(
            Finding(
                "CLUSTER_ORDER_INVALID",
                "/environmental_indicator/cluster_summary/clusters",
            )
        )
    for index, cluster in enumerate(clusters):
        member_counties = _string_list(cluster.get("county_fips"))
        if member_counties != sorted(member_counties) or len(member_counties) != len(
            set(member_counties)
        ):
            findings.add(
                Finding(
                    "COUNTY_ORDER_INVALID",
                    f"/environmental_indicator/cluster_summary/clusters/{index}/county_fips",
                )
            )
        refs = _string_list(cluster.get("evidence_ref_ids"))
        if refs != sorted(refs) or len(refs) != len(set(refs)):
            findings.add(
                Finding(
                    "REFERENCE_ORDER_INVALID",
                    f"/environmental_indicator/cluster_summary/clusters/{index}/evidence_ref_ids",
                )
            )

    evidence_ids, _, evidence_shape_valid = _reference_ids(bundle)
    if (
        not evidence_shape_valid
        or evidence_ids != sorted(evidence_ids)
        or len(evidence_ids) != len(set(evidence_ids))
    ):
        findings.add(Finding("EVIDENCE_REF_ORDER_INVALID", "/bundle/evidence_refs"))

    for field in ("source_records", "citations"):
        values = _string_list(bundle.get(field))
        if values != sorted(values) or len(values) != len(set(values)):
            findings.add(Finding("REFERENCE_ORDER_INVALID", f"/bundle/{field}"))
    return findings


