import math
import re

from governed_api.provider import (
    EVIDENCE_REF,
    FEATURE_COORDINATES,
    FEATURE_ID,
    FEATURE_TITLE,
    LAYER_ID,
    LAYER_DESCRIPTION,
    LAYER_TITLE,
    MAP_FEATURE_SELECTION_PROFILE,
    SELECTION_ID,
    SOURCE_ID,
    PublicFeature,
    PublicLayer,
    SliceProvider,
)
from governed_api.request import (
    InvalidRequest,
    is_safe_identifier,
    parse_exact_identifier_query,
)
from governed_api.routes import RouteResponse

PATH = "/layers"
PROFILE = "kfm.governed-api.synthetic-layer-slice.v1"
_CONTROL_CHARACTER = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def _bounded_text(value: object, maximum: int) -> bool:
    return (
        isinstance(value, str)
        and 0 < len(value) <= maximum
        and value.strip() == value
        and _CONTROL_CHARACTER.search(value) is None
    )


def _valid_coordinate(value: object, *, minimum: float, maximum: float) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
        and minimum <= value <= maximum
    )


def _project_feature(feature: object) -> tuple[dict, dict]:
    if not isinstance(feature, PublicFeature):
        raise ValueError("invalid-provider-result")
    if feature.feature_id != FEATURE_ID or not is_safe_identifier(feature.feature_id):
        raise ValueError("invalid-provider-result")
    if feature.selection_id != SELECTION_ID or not is_safe_identifier(feature.selection_id):
        raise ValueError("invalid-provider-result")
    if feature.title != FEATURE_TITLE or not _bounded_text(feature.title, 160):
        raise ValueError("invalid-provider-result")
    if not isinstance(feature.coordinates, tuple) or len(feature.coordinates) != 2:
        raise ValueError("invalid-provider-result")
    longitude, latitude = feature.coordinates
    if not _valid_coordinate(longitude, minimum=-180, maximum=180):
        raise ValueError("invalid-provider-result")
    if not _valid_coordinate(latitude, minimum=-90, maximum=90):
        raise ValueError("invalid-provider-result")
    if feature.coordinates != FEATURE_COORDINATES:
        raise ValueError("invalid-provider-result")
    if feature.evidence_refs != (EVIDENCE_REF,):
        raise ValueError("invalid-provider-result")

    geojson_feature = {
        "type": "Feature",
        "id": feature.feature_id,
        "geometry": {
            "type": "Point",
            "coordinates": [longitude, latitude],
        },
        "properties": None,
    }
    selection = {
        "profile": MAP_FEATURE_SELECTION_PROFILE,
        "selection_id": feature.selection_id,
        "layer_id": LAYER_ID,
        "feature_id": feature.feature_id,
        "evidence_refs": sorted(feature.evidence_refs),
    }
    return geojson_feature, selection


def _project_layers(records: object) -> list[dict]:
    if not isinstance(records, tuple) or len(records) != 1:
        raise ValueError("invalid-provider-result")

    layer = records[0]
    if not isinstance(layer, PublicLayer):
        raise ValueError("invalid-provider-result")
    if layer.source_id != SOURCE_ID or not is_safe_identifier(layer.source_id):
        raise ValueError("invalid-provider-result")
    if layer.layer_id != LAYER_ID or not is_safe_identifier(layer.layer_id):
        raise ValueError("invalid-provider-result")
    if layer.kind != "circle":
        raise ValueError("invalid-provider-result")
    if layer.title != LAYER_TITLE or layer.description != LAYER_DESCRIPTION:
        raise ValueError("invalid-provider-result")
    if not _bounded_text(layer.title, 160) or not _bounded_text(layer.description, 500):
        raise ValueError("invalid-provider-result")
    if not isinstance(layer.features, tuple) or len(layer.features) != 1:
        raise ValueError("invalid-provider-result")

    projected_features = [_project_feature(feature) for feature in layer.features]
    features = sorted((item[0] for item in projected_features), key=lambda item: item["id"])
    selections = sorted(
        (item[1] for item in projected_features),
        key=lambda item: item["selection_id"],
    )
    return [
        {
            "source_id": layer.source_id,
            "layer_id": layer.layer_id,
            "kind": layer.kind,
            "title": layer.title,
            "description": layer.description,
            "geojson": {
                "type": "FeatureCollection",
                "features": features,
            },
            "selection": selections[0],
        }
    ]


def _payload(outcome: str, reason_code: str, layer_items: list[dict]) -> dict:
    return {
        "profile": PROFILE,
        "scope": "slice-local",
        "outcome": outcome,
        "reason_code": reason_code,
        "layers": layer_items,
        "limitations": [
            "Fixture-only synthetic demonstration; not live data, release authority, or life-safety guidance."
        ],
    }


def layers(query_string: object, provider: SliceProvider) -> RouteResponse:
    try:
        parse_exact_identifier_query(query_string, ())
    except InvalidRequest:
        return RouteResponse(
            "400 Bad Request",
            _payload("ERROR", "INVALID_REQUEST", []),
        )

    try:
        layer_items = _project_layers(provider.list_layers())
    except Exception:
        return RouteResponse(
            "500 Internal Server Error",
            _payload("ERROR", "UPSTREAM_ERROR", []),
        )

    return RouteResponse("200 OK", _payload("ANSWER", "SUPPORTED", layer_items))
