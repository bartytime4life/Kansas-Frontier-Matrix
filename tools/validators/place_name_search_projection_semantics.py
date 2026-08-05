from __future__ import annotations

import re
import unicodedata
from datetime import datetime
from typing import Any, Mapping

from tools.validators.place_name_search_projection_common import (
    Finding,
    arr,
    canonical_spec_hash,
    canonical_strings,
    obj,
)

ZERO_DIGEST = "sha256:" + ("0" * 64)


def _time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo else None


def _normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).casefold()
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def _within(as_of: datetime, start: datetime | None, end: datetime | None) -> bool:
    return (start is None or start <= as_of) and (end is None or as_of <= end)


def semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    inputs, query = obj(candidate.get("input")), obj(candidate.get("query"))
    candidates, reasons = arr(candidate.get("candidates")), arr(candidate.get("reason_codes"))
    summary, provenance, governance = (
        obj(candidate.get("summary")), obj(candidate.get("provenance")), obj(candidate.get("governance"))
    )
    outcome = candidate.get("outcome")

    supplied = candidate.get("spec_hash")
    if isinstance(supplied, str) and supplied != canonical_spec_hash(candidate):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if inputs.get("graph_packet_digest") == ZERO_DIGEST:
        findings.append(Finding("DIGEST_PLACEHOLDER", "/input/graph_packet_digest"))

    arrays = [
        ("/input/authority_decision_refs", arr(inputs.get("authority_decision_refs"))),
        ("/reason_codes", reasons),
        ("/provenance/input_refs", arr(provenance.get("input_refs"))),
    ]
    arrays += [
        (f"/candidates/{index}/evidence_refs", arr(item.get("evidence_refs")))
        for index, item in enumerate(candidates)
        if isinstance(item, dict)
    ]
    for field, values in arrays:
        if not canonical_strings(values):
            findings.append(Finding("REFS_OR_REASONS_NOT_CANONICAL", field))

    text, key = query.get("query_text"), query.get("normalized_query_key")
    if isinstance(text, str) and isinstance(key, str) and _normalize(text) != key:
        findings.append(Finding("QUERY_NORMALIZATION_MISMATCH", "/query/normalized_query_key"))

    requested, as_of, recorded = (
        _time(query.get("requested_at")), _time(query.get("as_of_time")), _time(provenance.get("recorded_at"))
    )
    if requested and recorded and requested > recorded:
        findings.append(Finding("TIMING_ORDER_INVALID", "/query/requested_at"))
    if as_of and requested and as_of > requested:
        findings.append(Finding("AS_OF_TIME_IN_FUTURE", "/query/as_of_time"))

    ranks = [item.get("rank") for item in candidates if isinstance(item, dict)]
    if ranks != list(range(1, len(candidates) + 1)):
        findings.append(Finding("CANDIDATE_RANKS_INVALID", "/candidates"))
    assertion_refs = [item.get("assertion_ref") for item in candidates if isinstance(item, dict)]
    if not canonical_strings(assertion_refs):
        findings.append(Finding("CANDIDATES_NOT_CANONICAL", "/candidates"))

    ambiguity_count = sum(1 for item in candidates if isinstance(item, dict) and item.get("ambiguity") != "NONE")
    withheld_count = sum(
        1 for item in candidates if isinstance(item, dict) and item.get("sensitivity") in {"WITHHELD", "REVIEW_ONLY"}
    )
    for field, actual in (
        ("candidate_count", len(candidates)),
        ("ambiguity_count", ambiguity_count),
        ("withheld_count", withheld_count),
    ):
        if summary.get(field) != actual:
            findings.append(Finding("SUMMARY_COUNT_MISMATCH", f"/summary/{field}"))

    out_of_time = query_mismatch = unsafe = evidence_unresolved = False
    feature_sets: dict[str, set[str]] = {}
    mode = query.get("search_mode")
    for index, item in enumerate(candidates):
        if not isinstance(item, dict):
            continue
        candidate_key, feature_ref = item.get("normalized_name_key"), item.get("feature_ref")
        if isinstance(candidate_key, str) and isinstance(feature_ref, str):
            feature_sets.setdefault(candidate_key, set()).add(feature_ref)
        start, end = _time(item.get("valid_from")), _time(item.get("valid_to"))
        if start and end and start > end:
            findings.append(Finding("TIME_INTERVAL_INVALID", f"/candidates/{index}"))
        if as_of and not _within(as_of, start, end):
            out_of_time = True
        if isinstance(candidate_key, str) and isinstance(key, str):
            query_mismatch |= (
                candidate_key != key if mode in {"EXACT", "HISTORICAL_AS_OF"} else not candidate_key.startswith(key)
            )
        unsafe |= (
            item.get("ambiguity") != "NONE"
            or item.get("sensitivity") not in {"PUBLIC", "GENERALIZED"}
            or item.get("binding_confidence") not in {"CONFIRMED", "PROVISIONAL"}
            or feature_ref is None
        )
        evidence_unresolved |= item.get("evidence_resolution") != "RESOLVED"
    homonym = any(len(features) > 1 for features in feature_sets.values())

    if outcome == "ANSWER":
        if query.get("audience") != "STEWARD":
            findings.append(Finding("PUBLIC_ANSWER_UNAUTHORIZED", "/query/audience"))
        if not candidates:
            findings.append(Finding("ANSWER_REQUIRES_CANDIDATE", "/candidates"))
        if out_of_time:
            findings.append(Finding("ANSWER_CANDIDATE_OUTSIDE_TIME", "/candidates"))
        if query_mismatch:
            findings.append(Finding("ANSWER_QUERY_MISMATCH", "/candidates"))
        if unsafe:
            findings.append(Finding("ANSWER_CANDIDATE_UNSAFE", "/candidates"))
        if evidence_unresolved:
            findings.append(Finding("ANSWER_EVIDENCE_UNRESOLVED", "/candidates"))
        if homonym:
            findings.append(Finding("HOMONYM_COLLISION_UNREVIEWED", "/candidates"))
    elif outcome == "ABSTAIN":
        if candidates:
            findings.append(Finding("ABSTAIN_MUST_NOT_EMIT_CANDIDATES", "/candidates"))
        if not set(reasons) & {"AMBIGUOUS_HOMONYM", "DISPUTED_NAME", "EVIDENCE_UNRESOLVED", "NO_SUPPORTED_MATCH", "OUT_OF_VALID_TIME", "UNBOUND_NAME"}:
            findings.append(Finding("ABSTAIN_REASON_INVALID", "/reason_codes"))
    elif outcome == "DENY":
        if candidates:
            findings.append(Finding("DENY_MUST_NOT_EMIT_CANDIDATES", "/candidates"))
        if not set(reasons) & {"AUDIENCE_NOT_AUTHORIZED", "POLICY_REVIEW_REQUIRED", "SENSITIVE_NAME_WITHHELD"}:
            findings.append(Finding("DENY_REASON_INVALID", "/reason_codes"))
    elif outcome == "ERROR":
        if candidates:
            findings.append(Finding("ERROR_MUST_NOT_EMIT_CANDIDATES", "/candidates"))
        if not set(reasons) & {"INPUT_INVALID", "RESOLVER_ERROR"}:
            findings.append(Finding("ERROR_REASON_INVALID", "/reason_codes"))

    flags = (
        "source_admitted", "evidence_closure_claimed", "policy_evaluated",
        "feature_identity_created", "geometry_authority_created", "legal_status_created",
        "ownership_authority_created", "public_search_authorized", "promotion_authorized",
        "release_authorized", "publication_authorized",
    )
    if any(governance.get(field) is not False for field in flags) or governance.get("release_ref") is not None:
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return findings
