import json
from dataclasses import replace
from pathlib import Path
from urllib.parse import urlencode
from wsgiref.util import setup_testing_defaults

import pytest

from governed_api.main import app, create_app
from governed_api.provider import (
    DeterministicSliceProvider,
    EvidenceResolution,
)
from tools.validators.ui.validate_evidence_drawer_payload import validate_payload


REPO_ROOT = Path(__file__).resolve().parents[3]
ANSWER_FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures"
    / "ui"
    / "evidence_drawer_payload"
    / "valid"
    / "answer-corrected.json"
)

SUPPORTED_QUERY = urlencode(
    {
        "layer_id": "layer:synthetic-streamflow",
        "feature_id": "feature:flow-001",
        "evidence_ref": "kfm:evidence:synthetic:flow-001",
    }
)
RESTRICTED_QUERY = urlencode(
    {
        "layer_id": "layer:synthetic-restricted",
        "feature_id": "feature:restricted",
        "evidence_ref": "kfm:evidence:synthetic:restricted",
    }
)
PINNED_FIXTURE_CITATION = (
    "https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/"
    "d1f7ed51cf4d9c9c2fdf94cdc81644744ae464ce/fixtures/ui/"
    "evidence_drawer_payload/valid/answer-corrected.json"
)


def _call_app(application, path: str, *, query: str = "", method: str = "GET"):
    environ = {}
    setup_testing_defaults(environ)
    environ["REQUEST_METHOD"] = method
    environ["PATH_INFO"] = path
    environ["QUERY_STRING"] = query

    response = {}

    def start_response(status, headers):
        response["status"] = status
        response["headers"] = dict(headers)

    body = b"".join(application(environ, start_response))
    response["body"] = body
    response["payload"] = json.loads(body.decode("utf-8"))
    return response


class CountingProvider(DeterministicSliceProvider):
    def __init__(self) -> None:
        self.layer_calls = 0
        self.evidence_calls = 0

    def list_layers(self):
        self.layer_calls += 1
        return super().list_layers()

    def resolve_evidence(self, *, layer_id, feature_id, evidence_ref):
        self.evidence_calls += 1
        return super().resolve_evidence(
            layer_id=layer_id,
            feature_id=feature_id,
            evidence_ref=evidence_ref,
        )


class FailingProvider:
    def list_layers(self):
        raise RuntimeError("PRIVATE_PROVIDER_CANARY /private/provider/trace")

    def resolve_evidence(self, *, layer_id, feature_id, evidence_ref):
        raise RuntimeError("PRIVATE_PROVIDER_CANARY /private/provider/trace")


class InvalidResolutionProvider(DeterministicSliceProvider):
    def resolve_evidence(self, *, layer_id, feature_id, evidence_ref):
        return "ANSWER"


class UnboundAnswerProvider(DeterministicSliceProvider):
    def resolve_evidence(self, *, layer_id, feature_id, evidence_ref):
        return EvidenceResolution.ANSWER


class OverwideLayerProvider(DeterministicSliceProvider):
    def list_layers(self):
        layers = super().list_layers()
        return layers + layers


class UnsafeLayerProvider(DeterministicSliceProvider):
    def list_layers(self):
        layer = super().list_layers()[0]
        feature = layer.features[0]
        return (
            replace(
                layer,
                title="/private/provider/secret",
                description="https://private.invalid/provider-token",
                features=(replace(feature, coordinates=(0.0, 0.0)),),
            ),
        )


def test_layers_returns_one_stable_slice_local_geojson_projection() -> None:
    first = _call_app(app, "/layers")
    second = _call_app(app, "/layers")

    assert first["status"] == "200 OK"
    assert first["body"] == second["body"]
    assert first["headers"]["Content-Type"] == "application/json"
    assert int(first["headers"]["Content-Length"]) == len(first["body"])

    payload = first["payload"]
    assert set(payload) == {
        "profile",
        "scope",
        "outcome",
        "reason_code",
        "layers",
        "limitations",
    }
    assert payload["profile"] == "kfm.governed-api.synthetic-layer-slice.v1"
    assert payload["scope"] == "slice-local"
    assert payload["outcome"] == "ANSWER"
    assert payload["reason_code"] == "SUPPORTED"
    assert len(payload["layers"]) == 1

    layer = payload["layers"][0]
    assert set(layer) == {
        "source_id",
        "layer_id",
        "kind",
        "title",
        "description",
        "geojson",
        "selection",
    }
    assert layer["source_id"] == "source:synthetic-streamflow"
    assert layer["layer_id"] == "layer:synthetic-streamflow"
    assert layer["kind"] == "circle"
    assert layer["geojson"] == {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "feature:flow-001",
                "geometry": {"type": "Point", "coordinates": [-98.5, 38.5]},
                "properties": None,
            }
        ],
    }
    assert layer["selection"] == {
        "profile": "kfm.explorer.map-feature-selection.v1",
        "selection_id": "selection:flow-001",
        "layer_id": "layer:synthetic-streamflow",
        "feature_id": "feature:flow-001",
        "evidence_refs": ["kfm:evidence:synthetic:flow-001"],
    }


def test_evidence_answer_matches_existing_public_safe_explorer_projection() -> None:
    response = _call_app(app, "/evidence", query=SUPPORTED_QUERY)
    expected = json.loads(ANSWER_FIXTURE_PATH.read_text(encoding="utf-8"))
    expected["citations"][0]["href"] = PINNED_FIXTURE_CITATION

    assert response["status"] == "200 OK"
    assert response["payload"] == expected
    assert response["payload"]["citations"][0]["href"] == PINNED_FIXTURE_CITATION
    assert response["payload"]["evidence_refs"] == [
        "kfm:evidence:synthetic:flow-001"
    ]
    assert response["payload"]["history"]["negative_outcomes"][0][
        "resolvable_as_current"
    ] is False
    assert response["payload"]["history"]["corrections"][0][
        "active_evidence_ref"
    ] == "kfm:evidence:synthetic:flow-001"
    assert not {
        "spec_hash",
        "version",
        "issued_at",
        "policy_state",
        "freshness",
        "correction_state",
    }.intersection(response["payload"])


def test_evidence_unresolved_reference_abstains_without_claim_support() -> None:
    query = urlencode(
        {
            "layer_id": "layer:synthetic-streamflow",
            "feature_id": "feature:flow-001",
            "evidence_ref": "kfm:evidence:synthetic:missing",
        }
    )
    response = _call_app(app, "/evidence", query=query)

    assert response["status"] == "200 OK"
    assert response["payload"]["outcome"] == "ABSTAIN"
    assert response["payload"]["reason_code"] == "MISSING_EVIDENCE"
    assert response["payload"]["evidence_refs"] == []
    assert response["payload"]["citations"] == []
    assert response["payload"]["trust_state"]["policy"] == "ABSTAIN"


def test_restricted_synthetic_feature_returns_no_leak_deny() -> None:
    response = _call_app(app, "/evidence", query=RESTRICTED_QUERY)

    assert response["status"] == "200 OK"
    assert response["payload"]["outcome"] == "DENY"
    assert response["payload"]["reason_code"] == "SENSITIVE_DETAIL_RESTRICTED"
    assert response["payload"]["evidence_refs"] == []
    assert response["payload"]["citations"] == []
    assert response["payload"]["history"] == {
        "negative_outcomes": [],
        "corrections": [],
    }
    assert "synthetic:restricted" not in response["body"].decode("utf-8")


@pytest.mark.parametrize(
    "query",
    [
        "",
        "layer_id=layer%3Asynthetic-streamflow&feature_id=feature%3Aflow-001",
        (
            "layer_id=layer%3Asynthetic-streamflow&"
            "feature_id=feature%3Aflow-001&debug=true"
        ),
        SUPPORTED_QUERY + "&debug=true",
        (
            "layer_id=layer%3Asynthetic-streamflow&"
            "layer_id=layer%3Asynthetic-streamflow&"
            "evidence_ref=kfm%3Aevidence%3Asynthetic%3Aflow-001"
        ),
        (
            "layer_id=bad+identifier&feature_id=feature%3Aflow-001&"
            "evidence_ref=kfm%3Aevidence%3Asynthetic%3Aflow-001"
        ),
        (
            "layer_id=layer%ZZsynthetic-streamflow&feature_id=feature%3Aflow-001&"
            "evidence_ref=kfm%3Aevidence%3Asynthetic%3Aflow-001"
        ),
        urlencode(
            {
                "layer_id": "layer:" + "x" * 200,
                "feature_id": "feature:flow-001",
                "evidence_ref": "kfm:evidence:synthetic:flow-001",
            }
        ),
        "x" * 641,
    ],
)
def test_malformed_unknown_duplicate_invalid_and_oversized_queries_fail_before_provider(
    query: str,
) -> None:
    provider = CountingProvider()
    response = _call_app(create_app(provider), "/evidence", query=query)

    assert response["status"] == "400 Bad Request"
    assert response["payload"]["outcome"] == "ERROR"
    assert response["payload"]["reason_code"] == "UPSTREAM_ERROR"
    assert response["payload"]["evidence_refs"] == []
    assert provider.evidence_calls == 0


def test_unsupported_valid_identity_combination_fails_closed() -> None:
    query = urlencode(
        {
            "layer_id": "layer:synthetic-streamflow",
            "feature_id": "feature:mismatch",
            "evidence_ref": "kfm:evidence:synthetic:flow-001",
        }
    )
    response = _call_app(app, "/evidence", query=query)

    assert response["status"] == "400 Bad Request"
    assert response["payload"]["outcome"] == "ERROR"
    assert response["payload"]["id"] == "kfm:ui:evidence-drawer:error-scope-001"
    assert "feature:mismatch" not in response["body"].decode("utf-8")


def test_known_cross_scope_evidence_combination_fails_closed() -> None:
    query = urlencode(
        {
            "layer_id": "layer:synthetic-streamflow",
            "feature_id": "feature:flow-001",
            "evidence_ref": "kfm:evidence:synthetic:restricted",
        }
    )
    response = _call_app(app, "/evidence", query=query)

    assert response["status"] == "400 Bad Request"
    assert response["payload"]["outcome"] == "ERROR"
    assert response["payload"]["id"] == "kfm:ui:evidence-drawer:error-scope-001"
    assert "synthetic:restricted" not in response["body"].decode("utf-8")


def test_layers_rejects_every_query_without_calling_provider() -> None:
    provider = CountingProvider()
    response = _call_app(
        create_app(provider),
        "/layers",
        query="limit=1",
    )

    assert response["status"] == "400 Bad Request"
    assert response["payload"] == {
        "profile": "kfm.governed-api.synthetic-layer-slice.v1",
        "scope": "slice-local",
        "outcome": "ERROR",
        "reason_code": "INVALID_REQUEST",
        "layers": [],
        "limitations": [
            "Fixture-only synthetic demonstration; not live data, release "
            "authority, or life-safety guidance."
        ],
    }
    assert provider.layer_calls == 0


@pytest.mark.parametrize("path,query", [("/layers", ""), ("/evidence", SUPPORTED_QUERY)])
def test_provider_failures_return_fixed_errors_without_internal_detail(
    path: str,
    query: str,
) -> None:
    response = _call_app(create_app(FailingProvider()), path, query=query)
    serialized = response["body"].decode("utf-8")

    assert response["status"] == "500 Internal Server Error"
    assert response["payload"]["outcome"] == "ERROR"
    assert "PRIVATE_PROVIDER_CANARY" not in serialized
    assert "/private/provider/trace" not in serialized
    assert "Traceback" not in serialized
    assert "RuntimeError" not in serialized


def test_unknown_provider_resolution_cannot_create_an_answer() -> None:
    response = _call_app(
        create_app(InvalidResolutionProvider()),
        "/evidence",
        query=SUPPORTED_QUERY,
    )

    assert response["status"] == "500 Internal Server Error"
    assert response["payload"]["outcome"] == "ERROR"
    assert response["payload"]["evidence_refs"] == []


def test_provider_answer_is_bound_to_the_supported_request_tuple() -> None:
    query = urlencode(
        {
            "layer_id": "layer:unrelated",
            "feature_id": "feature:unrelated",
            "evidence_ref": "kfm:evidence:unrelated",
        }
    )
    response = _call_app(
        create_app(UnboundAnswerProvider()),
        "/evidence",
        query=query,
    )

    assert response["status"] == "400 Bad Request"
    assert response["payload"]["outcome"] == "ERROR"
    assert response["payload"]["evidence_refs"] == []
    assert "unrelated" not in response["body"].decode("utf-8")


def test_provider_cannot_widen_the_one_layer_slice() -> None:
    response = _call_app(create_app(OverwideLayerProvider()), "/layers")

    assert response["status"] == "500 Internal Server Error"
    assert response["payload"]["outcome"] == "ERROR"
    assert response["payload"]["reason_code"] == "UPSTREAM_ERROR"
    assert response["payload"]["layers"] == []


def test_provider_cannot_change_or_leak_the_exact_public_layer_projection() -> None:
    response = _call_app(create_app(UnsafeLayerProvider()), "/layers")
    serialized = response["body"].decode("utf-8")

    assert response["status"] == "500 Internal Server Error"
    assert response["payload"]["outcome"] == "ERROR"
    assert response["payload"]["layers"] == []
    assert "/private/provider/secret" not in serialized
    assert "private.invalid" not in serialized


def test_every_evidence_outcome_is_explorer_projection_compatible(tmp_path) -> None:
    unresolved_query = urlencode(
        {
            "layer_id": "layer:synthetic-streamflow",
            "feature_id": "feature:flow-001",
            "evidence_ref": "kfm:evidence:synthetic:missing",
        }
    )
    scope_error_query = urlencode(
        {
            "layer_id": "layer:synthetic-streamflow",
            "feature_id": "feature:mismatch",
            "evidence_ref": "kfm:evidence:synthetic:flow-001",
        }
    )
    cases = (
        ("answer", app, SUPPORTED_QUERY),
        ("abstain", app, unresolved_query),
        ("deny", app, RESTRICTED_QUERY),
        ("request-error", app, ""),
        ("scope-error", app, scope_error_query),
        ("provider-error", create_app(FailingProvider()), SUPPORTED_QUERY),
    )

    observed_outcomes = set()
    for name, application, query in cases:
        response = _call_app(application, "/evidence", query=query)
        observed_outcomes.add(response["payload"]["outcome"])
        payload_path = tmp_path / f"{name}.json"
        payload_path.write_text(
            json.dumps(response["payload"]),
            encoding="utf-8",
        )
        assert validate_payload(payload_path) == ()

    assert observed_outcomes == {"ANSWER", "ABSTAIN", "DENY", "ERROR"}


def test_non_get_slice_methods_remain_bounded_runtime_errors() -> None:
    for path in ("/layers", "/evidence"):
        response = _call_app(app, path, method="POST")
        assert response["status"] == "405 Method Not Allowed"
        assert response["payload"]["outcome"] == "ERROR"
        assert response["payload"]["reason_code"] == "SAFE_RUNTIME_ERROR"


def test_resolution_enum_is_finite() -> None:
    assert {item.value for item in EvidenceResolution} == {
        "ANSWER",
        "ABSTAIN",
        "DENY",
        "ERROR",
    }
