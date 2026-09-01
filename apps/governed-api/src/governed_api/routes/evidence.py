from governed_api.provider import (
    EVIDENCE_REF,
    FEATURE_ID,
    LAYER_ID,
    EvidenceResolution,
    SliceProvider,
)
from governed_api.request import InvalidRequest, parse_exact_identifier_query
from governed_api.routes import RouteResponse

PATH = "/evidence"
PROFILE = "kfm.explorer.evidence-drawer.public-safe.v1"
PINNED_FIXTURE_CITATION = (
    "https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/"
    "d1f7ed51cf4d9c9c2fdf94cdc81644744ae464ce/fixtures/ui/"
    "evidence_drawer_payload/valid/answer-corrected.json"
)

_EMPTY_HISTORY = {"negative_outcomes": [], "corrections": []}


def _trust_state(
    *,
    policy: str,
    review: str,
    release: str,
    freshness: str,
    correction: str,
) -> dict:
    return {
        "source_role": "official" if policy == "ALLOW" else "context",
        "policy": policy,
        "review": review,
        "release": release,
        "freshness": freshness,
        "correction": correction,
    }


def _answer_payload() -> dict:
    return {
        "profile": PROFILE,
        "id": "kfm:ui:evidence-drawer:answer-001",
        "outcome": "ANSWER",
        "reason_code": "SUPPORTED",
        "title": "Synthetic streamflow observation",
        "summary": (
            "A synthetic, generalized flow observation is supported by the cited fixture evidence."
        ),
        "evidence_refs": ["kfm:evidence:synthetic:flow-001"],
        "citations": [
            {
                "label": "Synthetic fixture evidence",
                "href": PINNED_FIXTURE_CITATION,
            }
        ],
        "limitations": [
            "Fixture-only demonstration; not a live observation or life-safety instruction."
        ],
        "trust_state": _trust_state(
            policy="ALLOW",
            review="REVIEWED",
            release="RELEASED",
            freshness="CURRENT",
            correction="CORRECTED",
        ),
        "history": {
            "negative_outcomes": [
                {
                    "evidence_ref": "kfm:evidence:synthetic:flow-000",
                    "state": "SUPERSEDED",
                    "reason_code": "SUPERSEDED_EVIDENCE",
                    "recorded_at": "2026-08-01T00:00:00Z",
                    "visible_in_runtime": True,
                    "resolvable_as_current": False,
                }
            ],
            "corrections": [
                {
                    "prior_evidence_ref": "kfm:evidence:synthetic:flow-000",
                    "active_evidence_ref": "kfm:evidence:synthetic:flow-001",
                    "status": "ACTIVE_CORRECTION",
                    "recorded_at": "2026-08-01T00:00:00Z",
                }
            ],
        },
    }


def _negative_payload(
    *,
    projection_id: str,
    outcome: str,
    reason_code: str,
    title: str,
    summary: str,
    limitation: str,
) -> dict:
    policy = outcome if outcome in {"ABSTAIN", "DENY", "ERROR"} else "ERROR"
    return {
        "profile": PROFILE,
        "id": projection_id,
        "outcome": outcome,
        "reason_code": reason_code,
        "title": title,
        "summary": summary,
        "evidence_refs": [],
        "citations": [],
        "limitations": [limitation],
        "trust_state": _trust_state(
            policy=policy,
            review="PENDING" if outcome != "ABSTAIN" else "NOT_APPLICABLE",
            release="UNRELEASED",
            freshness="UNKNOWN",
            correction="NONE",
        ),
        "history": {key: list(value) for key, value in _EMPTY_HISTORY.items()},
    }


def _abstain_payload() -> dict:
    return _negative_payload(
        projection_id="kfm:ui:evidence-drawer:abstain-unresolved-001",
        outcome="ABSTAIN",
        reason_code="MISSING_EVIDENCE",
        title="Evidence not sufficient",
        summary="The requested synthetic evidence could not be resolved as current support.",
        limitation="No unsupported claim is shown.",
    )


def _deny_payload() -> dict:
    return _negative_payload(
        projection_id="kfm:ui:evidence-drawer:deny-sensitive-001",
        outcome="DENY",
        reason_code="SENSITIVE_DETAIL_RESTRICTED",
        title="Restricted map detail",
        summary="The requested detail is restricted by policy.",
        limitation="Protected spatial detail is not exposed.",
    )


def _error_payload(projection_id: str, *, reason_code: str = "UPSTREAM_ERROR") -> dict:
    return _negative_payload(
        projection_id=projection_id,
        outcome="ERROR",
        reason_code=reason_code,
        title="Evidence unavailable",
        summary="The governed evidence request could not be completed safely.",
        limitation="No partial or unsupported claim is shown.",
    )


def evidence(query_string: object, provider: SliceProvider) -> RouteResponse:
    try:
        query = parse_exact_identifier_query(
            query_string,
            ("layer_id", "feature_id", "evidence_ref"),
        )
    except InvalidRequest:
        return RouteResponse(
            "400 Bad Request",
            _error_payload("kfm:ui:evidence-drawer:error-request-001"),
        )

    try:
        resolution = provider.resolve_evidence(
            layer_id=query["layer_id"],
            feature_id=query["feature_id"],
            evidence_ref=query["evidence_ref"],
        )
    except Exception:
        return RouteResponse(
            "500 Internal Server Error",
            _error_payload("kfm:ui:evidence-drawer:error-provider-001"),
        )

    if resolution is EvidenceResolution.ANSWER:
        if query != {
            "layer_id": LAYER_ID,
            "feature_id": FEATURE_ID,
            "evidence_ref": EVIDENCE_REF,
        }:
            return RouteResponse(
                "400 Bad Request",
                _error_payload("kfm:ui:evidence-drawer:error-scope-001"),
            )
        return RouteResponse("200 OK", _answer_payload())
    if resolution is EvidenceResolution.ABSTAIN:
        return RouteResponse("200 OK", _abstain_payload())
    if resolution is EvidenceResolution.DENY:
        return RouteResponse("200 OK", _deny_payload())
    if resolution is EvidenceResolution.ERROR:
        return RouteResponse(
            "400 Bad Request",
            _error_payload(
                "kfm:ui:evidence-drawer:error-provider-scope-001",
                reason_code="PROVIDER_SCOPE_ERROR",
            ),
        )

    return RouteResponse(
        "500 Internal Server Error",
        _error_payload("kfm:ui:evidence-drawer:error-provider-001"),
    )
