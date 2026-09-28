"""Offline BLM PLSS (CadNSDI) query planning and GeoJSON parsing; never fetches.

A PLSS township or first-division polygon is survey and cadastral *reference* geometry:
never county parcel ownership, legal title, deed authority, or access permission. This
module plans one canonical, paged ArcGIS REST ``query`` URL for Kansas features of one
CadNSDI layer and parses an *already supplied* GeoJSON page into frozen per-feature
candidates with properties kept verbatim.

The service path, layer ids, identifier fields and the ``STATEABBR`` attribute are NEEDS
VERIFICATION against current BLM service metadata: any unexpected shape or out-of-scope
feature rejects the whole page rather than being coerced. Pagination, dissolves, parcel
joins, persistence and publication belong to owning layers.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from hashlib import sha256
import json
import re
from urllib.parse import parse_qsl, urlencode, urlsplit

HOST = "https://gis.blm.gov"
SERVICE = "/arcgis/rest/services/Cadastral/BLM_Natl_PLSS_CadNSDI/MapServer"
STATE = "KS"
# layer name -> (layer id, identifier field). NEEDS VERIFICATION against service metadata.
LAYERS = {"township": (1, "PLSSID"), "first_division": (2, "FRSTDIVID")}
MAX_PAGE = 1000
MAX_OFFSET = 1_000_000
# Kansas extent (WGS84) with a small tolerance for boundary-straddling survey polygons.
BBOX = (Decimal("-102.10"), Decimal("36.95"), Decimal("-94.55"), Decimal("40.05"))
IDENTIFIER = re.compile(r"[A-Za-z0-9._-]{1,64}\Z")
# Legitimate payloads nest about 8 containers deep; anything past this is rejected
# before any recursive walk, independent of the interpreter's recursion limit.
MAX_NESTING = 20


class _SourceNumber(Decimal):
    """A decoded JSON non-integer number that remembers its exact source token."""

    def __new__(cls, token: str) -> "_SourceNumber":
        number = super().__new__(cls, token)
        number.token = token
        return number


class _SourceInt(int):
    """A decoded JSON integer that remembers its exact source token (e.g. ``-0``)."""

    def __new__(cls, token: str) -> "_SourceInt":
        number = super().__new__(cls, token)
        number.token = token
        return number


def _token(number: int | Decimal) -> str:
    return getattr(number, "token", None) or str(number)


def _plain(value: object) -> object:
    """Numbers as JSON-safe values; tokens JSON cannot re-emit exactly become strings."""
    if isinstance(value, dict):
        return {key: _plain(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_plain(item) for item in value]
    if isinstance(value, _SourceInt):
        return int(value) if value.token == str(int(value)) else value.token
    if isinstance(value, _SourceNumber):
        return value.token
    return value


def _dump(value: object) -> str:
    """Canonical JSON for verbatim storage; non-integer number tokens are kept as strings."""
    return json.dumps(_plain(value), sort_keys=True, ensure_ascii=True, separators=(",", ":"),
                      allow_nan=False)


class PlssInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for rejected candidate input."""


def _utc(value: object) -> str:
    try:
        if not isinstance(value, str) or len(value) > 40:
            raise ValueError
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError
        return result.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    except (ValueError, TypeError, OverflowError):
        raise PlssInputError("UTC_TIME") from None


@dataclass(frozen=True)
class QueryRequest:
    layer: str
    offset: int
    count: int


def _params(layer: str, offset: int, count: int) -> dict[str, str]:
    return {"where": f"STATEABBR='{STATE}'", "outFields": "*", "returnGeometry": "true",
            "outSR": "4326", "orderByFields": "OBJECTID", "resultOffset": str(offset),
            "resultRecordCount": str(count), "f": "geojson"}


def query_url(layer: str, *, offset: int = 0, count: int = MAX_PAGE) -> str:
    """Return one canonical paged query URL for Kansas features of a CadNSDI layer."""
    if layer not in LAYERS:
        raise PlssInputError("LAYER")
    if type(offset) is not int or not 0 <= offset <= MAX_OFFSET:
        raise PlssInputError("OFFSET")
    if type(count) is not int or not 1 <= count <= MAX_PAGE:
        raise PlssInputError("PAGE_SIZE")
    return (f"{HOST}{SERVICE}/{LAYERS[layer][0]}/query?"
            + urlencode(_params(layer, offset, count)))


def parse_request(source_url: object) -> QueryRequest:
    """Recover the request a planner URL encodes; anything non-canonical is refused."""
    if not isinstance(source_url, str) or len(source_url) > 2048 or any(
            ord(c) <= 32 for c in source_url):
        raise PlssInputError("SOURCE_URL")
    parsed = urlsplit(source_url)
    prefix = f"{SERVICE}/"
    if (parsed.scheme != "https" or parsed.netloc != urlsplit(HOST).netloc
            or not parsed.path.startswith(prefix) or not parsed.path.endswith("/query")
            or parsed.fragment):
        raise PlssInputError("SOURCE_URL")
    layer_id = parsed.path[len(prefix):-len("/query")]
    names = [name for name, (number, _) in LAYERS.items() if str(number) == layer_id]
    if len(names) != 1:
        raise PlssInputError("LAYER")
    try:
        values = dict(parse_qsl(parsed.query, keep_blank_values=True, strict_parsing=True))
        offset, count = int(values["resultOffset"]), int(values["resultRecordCount"])
    except (ValueError, KeyError):
        raise PlssInputError("SOURCE_URL") from None
    if query_url(names[0], offset=offset, count=count) != source_url:
        raise PlssInputError("SOURCE_URL_SCOPE")
    return QueryRequest(names[0], offset, count)


@dataclass(frozen=True)
class PlssFeature:
    object_id: int
    identifier: str
    geometry_type: str
    ring_count: int
    route: str
    reasons: tuple[str, ...]
    # Every source property verbatim; never log or render it.
    raw_properties_json: str
    feature_sha256: str
    source_role: str = "REFERENCE_GEOMETRY_CANDIDATE"
    # Survey reference only: never parcel ownership, title, deed, or access authority.
    title_authority: bool = False


@dataclass(frozen=True)
class PlssPageCandidate:
    source_url: str
    request: QueryRequest
    retrieved_at: str
    body_sha256: str
    features: tuple[PlssFeature, ...]
    more_pages: bool
    coverage: str = "NOT_ESTABLISHED"
    admission: str = "NOT_ADMITTED"


def _position(value: object) -> tuple[Decimal, Decimal]:
    # Exact Decimal comparison: ring closure and the extent check must not collapse
    # coordinates that differ only beyond binary float precision.
    if (not isinstance(value, list) or len(value) not in (2, 3)
            or any(isinstance(n, bool) or not isinstance(n, (int, Decimal)) for n in value)):
        raise PlssInputError("GEOMETRY_SHAPE")
    return Decimal(_token(value[0])), Decimal(_token(value[1]))


def _rings(geometry: object) -> tuple[str, list[list[tuple[float, float]]]]:
    if not isinstance(geometry, dict) or geometry.get("type") not in ("Polygon", "MultiPolygon"):
        raise PlssInputError("GEOMETRY_SHAPE")
    coordinates = geometry.get("coordinates")
    polygons = [coordinates] if geometry["type"] == "Polygon" else coordinates
    if not isinstance(polygons, list) or not polygons:
        raise PlssInputError("GEOMETRY_SHAPE")
    rings = []
    for polygon in polygons:
        if not isinstance(polygon, list) or not polygon:
            raise PlssInputError("GEOMETRY_SHAPE")
        for ring in polygon:
            if not isinstance(ring, list) or len(ring) > 100_000:
                raise PlssInputError("GEOMETRY_SHAPE")
            rings.append([_position(position) for position in ring])
    return geometry["type"], rings


def _feature(item: object, id_field: str) -> PlssFeature:
    if not isinstance(item, dict) or item.get("type") != "Feature":
        raise PlssInputError("FEATURE_SHAPE")
    properties = item.get("properties")
    if not isinstance(properties, dict):
        raise PlssInputError("FEATURE_SHAPE")
    if properties.get("STATEABBR") != STATE:
        raise PlssInputError("STATE_SCOPE")
    object_id, identifier = properties.get("OBJECTID"), properties.get(id_field)
    if isinstance(object_id, bool) or not isinstance(object_id, int) or object_id < 0:
        raise PlssInputError("OBJECT_ID")
    if not isinstance(identifier, str) or not IDENTIFIER.fullmatch(identifier):
        raise PlssInputError("IDENTIFIER")
    geometry_type, rings = _rings(item.get("geometry"))
    reasons: list[str] = []
    if any(len(ring) < 4 or ring[0] != ring[-1] for ring in rings):
        reasons.append("RING_NOT_CLOSED")
    west, south, east, north = BBOX
    if any(not (west <= x <= east and south <= y <= north) for ring in rings for x, y in ring):
        reasons.append("GEOMETRY_OUTSIDE_KANSAS_EXTENT")
    try:
        raw_properties, raw_feature = _dump(properties), _dump(item)
    except RecursionError:
        # Pathologically nested properties decode but cannot be re-serialized safely.
        raise PlssInputError("FEATURE_SHAPE") from None
    return PlssFeature(int(object_id), identifier, geometry_type, len(rings),
                       "QUARANTINE_CANDIDATE" if reasons else "RAW_CANDIDATE",
                       tuple(reasons), raw_properties,
                       "sha256:" + sha256(raw_feature.encode("ascii")).hexdigest())


def _exceeds_nesting(value: object, limit: int) -> bool:
    """Whether containers nest deeper than ``limit``; iterative, early-exit, and holding
    at most one iterator per level, so wide payloads cost no extra memory."""
    if not isinstance(value, (dict, list)):
        return False
    stack = [iter(value.values() if isinstance(value, dict) else value)]
    if len(stack) > limit:
        return True
    while stack:
        for child in stack[-1]:
            if isinstance(child, (dict, list)):
                if len(stack) + 1 > limit:
                    return True
                stack.append(iter(child.values() if isinstance(child, dict) else child))
                break
        else:
            stack.pop()
    return False


def _reject_constant(token: str) -> None:
    raise ValueError(token)


def parse_page(body: bytes, *, status: int, source_url: str, retrieved_at: str,
               max_bytes: int = 64 * 1024 * 1024) -> PlssPageCandidate:
    """Parse one supplied GeoJSON query page; reject it whole on shape or scope drift."""
    request = parse_request(source_url)
    retrieved = _utc(retrieved_at)
    if type(status) is not int or not isinstance(body, bytes) or len(body) > max_bytes:
        raise PlssInputError("RESPONSE_BOUND")
    if status != 200:
        raise PlssInputError("HTTP_STATUS")
    try:
        payload = json.loads(body.decode("utf-8"), parse_float=_SourceNumber,
                             parse_int=_SourceInt, parse_constant=_reject_constant)
    except RecursionError:
        # The decoder's own depth limit is interpreter-dependent; either way it is depth.
        raise PlssInputError("NESTING_DEPTH") from None
    except (UnicodeError, ValueError, InvalidOperation):
        raise PlssInputError("INVALID_JSON") from None
    if _exceeds_nesting(payload, MAX_NESTING):
        raise PlssInputError("NESTING_DEPTH")
    if not isinstance(payload, dict):
        raise PlssInputError("COLLECTION_SHAPE")
    if "error" in payload:
        # ArcGIS reports query failures inside a 200 body.
        raise PlssInputError("SERVICE_ERROR")
    features = payload.get("features")
    if payload.get("type") != "FeatureCollection" or not isinstance(features, list):
        raise PlssInputError("COLLECTION_SHAPE")
    if len(features) > request.count:
        raise PlssInputError("PAGE_BOUND")
    # ArcGIS GeoJSON reports truncation under the collection's ``properties``; some
    # versions also emit it top-level (NEEDS VERIFICATION). Either one marks more pages.
    collection_properties = payload.get("properties", {})
    if not isinstance(collection_properties, dict):
        raise PlssInputError("COLLECTION_SHAPE")
    flags = (payload.get("exceededTransferLimit", False),
             collection_properties.get("exceededTransferLimit", False))
    if any(not isinstance(flag, bool) for flag in flags):
        raise PlssInputError("COLLECTION_SHAPE")
    exceeded = any(flags)
    id_field = LAYERS[request.layer][1]
    parsed = tuple(_feature(item, id_field) for item in features)
    object_ids = [feature.object_id for feature in parsed]
    if object_ids != sorted(set(object_ids)):
        # orderByFields=OBJECTID makes paging stable only if ids are strictly increasing.
        raise PlssInputError("OBJECT_ID_ORDER")
    identifiers = [feature.identifier for feature in parsed]
    if len(set(identifiers)) != len(identifiers):
        raise PlssInputError("DUPLICATE_IDENTIFIER")
    return PlssPageCandidate(source_url, request, retrieved,
                             "sha256:" + sha256(body).hexdigest(), parsed,
                             exceeded or len(parsed) == request.count)
