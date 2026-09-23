"""Offline USGS request planning and immutable candidate parsing; never fetches.

Transport authentication, bounded reads/deadlines, source admission, persistence,
reconciliation and public release belong to existing owning layers. A validated
URL records intended provenance; it does not authenticate supplied response bytes.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from hashlib import sha256
import json
import math
import re
from urllib.parse import parse_qs, urlencode, urlsplit

HOST = "https://earthquake.usgs.gov"
EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)
# Context envelope, not the legal Kansas boundary or a completeness guarantee.
KANSAS_CONTEXT = (-102.1, 36.9, -94.5, 40.1)
FEEDS = frozenset(f"{level}_{period}.geojson" for level in
                  ("all", "1.0", "2.5", "4.5", "significant")
                  for period in ("hour", "day", "week", "month"))
IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,127}\Z")


class EarthquakeInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for rejected candidate input."""


def _integer(value: object, minimum: int, maximum: int) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise EarthquakeInputError("INTEGER_BOUND")
    return value


def _utc(value: str) -> datetime:
    try:
        if not isinstance(value, str) or len(value) > 40:
            raise ValueError
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError
        result = result.astimezone(timezone.utc)
        if result.microsecond % 1000:
            raise ValueError
        return result
    except (ValueError, TypeError, OverflowError):
        raise EarthquakeInputError("UTC_MILLISECOND_TIME") from None


def _iso(value: datetime) -> str:
    return value.isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _number(value: object) -> float:
    try:
        if type(value) not in (int, float) or not math.isfinite(value):
            raise ValueError
        return float(value)
    except (ValueError, OverflowError):
        raise EarthquakeInputError("FINITE_NUMBER") from None


def _bounds(value: tuple[float, float, float, float]) -> tuple[float, ...]:
    if not isinstance(value, (tuple, list)) or len(value) != 4:
        raise EarthquakeInputError("BBOX_SHAPE")
    west, south, east, north = map(_number, value)
    if not (-180 <= west < east <= 180 and -90 <= south < north <= 90):
        raise EarthquakeInputError("BBOX_RANGE")
    return west, south, east, north


def _milliseconds(value: object, *, nullable: bool = False) -> int | None:
    if value is None and nullable:
        return None
    try:
        if type(value) is not int:
            raise ValueError
        EPOCH + timedelta(milliseconds=value)
        return value
    except (ValueError, OverflowError):
        raise EarthquakeInputError("EPOCH_MILLISECONDS") from None


def _text(value: object, *, required: bool = False) -> str | None:
    if value is None and not required:
        return None
    if not isinstance(value, str) or not value or len(value) > 2048 or "\x00" in value:
        raise EarthquakeInputError("TEXT_SHAPE")
    return value


def live_url(period: str = "day", level: str = "all") -> str:
    """Return one official summary URL, not a network or scheduling operation."""
    name = f"{level}_{period}.geojson"
    if name not in FEEDS:
        raise EarthquakeInputError("FEED_NOT_ALLOWED")
    return f"{HOST}/earthquakes/feed/v1.0/summary/{name}"


@dataclass(frozen=True)
class HistoryWindow:
    """Half-open ownership window; USGS requests include both endpoints."""
    start: str
    end_exclusive: str
    query_url: str
    count_url: str
    limit: int


def history_windows(start: str, end: str, *, bounds=KANSAS_CONTEXT,
                    window_days: int = 31, limit: int = 1000,
                    max_windows: int = 2400) -> tuple[HistoryWindow, ...]:
    """Plan finite overlapping-endpoint requests; never imply complete history.

    Query results must be assigned to [start, end_exclusive), with counts, ties,
    truncation, revisions and deleted/superseded events reconciled separately.
    """
    first, stop = _utc(start), _utc(end)
    west, south, east, north = _bounds(bounds)
    _integer(window_days, 1, 31)
    _integer(limit, 1, 20000)
    _integer(max_windows, 1, 2400)
    if first >= stop:
        raise EarthquakeInputError("TIME_ORDER")
    span = timedelta(days=window_days)
    if (stop - first) > span * max_windows:
        raise EarthquakeInputError("WINDOW_CAPACITY")
    plans: list[HistoryWindow] = []
    cursor = first
    while cursor < stop:
        right = min(cursor + span, stop)
        params = {"format": "geojson", "starttime": _iso(cursor),
                  "endtime": _iso(right), "minlongitude": west,
                  "minlatitude": south, "maxlongitude": east,
                  "maxlatitude": north, "eventtype": "earthquake"}
        count_url = f"{HOST}/fdsnws/event/1/count?{urlencode(params)}"
        query = dict(params, limit=limit, offset=1, orderby="time-asc", nodata=204)
        plans.append(HistoryWindow(_iso(cursor), _iso(right),
                     f"{HOST}/fdsnws/event/1/query?{urlencode(query)}", count_url, limit))
        cursor = right
    return tuple(plans)


def _request_kind(url: str) -> tuple[str, int | None]:
    if not isinstance(url, str) or len(url) > 4096 or any(ord(c) <= 32 for c in url):
        raise EarthquakeInputError("SOURCE_URL")
    try:
        parsed = urlsplit(url)
        if parsed.scheme != "https" or parsed.netloc != "earthquake.usgs.gov" or parsed.fragment:
            raise ValueError
        prefix = "/earthquakes/feed/v1.0/summary/"
        if parsed.path.startswith(prefix) and parsed.path[len(prefix):] in FEEDS and not parsed.query:
            return "summary", None
        if parsed.path != "/fdsnws/event/1/query":
            raise ValueError
        params = parse_qs(parsed.query, strict_parsing=True, keep_blank_values=True)
        allowed = {"format", "starttime", "endtime", "minlongitude", "minlatitude",
                   "maxlongitude", "maxlatitude", "eventtype", "limit", "offset",
                   "orderby", "nodata", "minmagnitude", "maxmagnitude", "updatedafter",
                   "catalog", "contributor"}
        if set(params) - allowed or any(len(v) != 1 or not v[0] for v in params.values()):
            raise ValueError
        if params.get("format") != ["geojson"] or params.get("nodata") != ["204"]:
            raise ValueError
        limit = int(params["limit"][0])
        _integer(limit, 1, 20000)
        return "query", limit
    except (KeyError, ValueError, TypeError):
        raise EarthquakeInputError("SOURCE_URL") from None


def _object_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise EarthquakeInputError("DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def _constant(_: str) -> None:
    raise EarthquakeInputError("NONSTANDARD_JSON_NUMBER")


@dataclass(frozen=True)
class EventCandidate:
    event_id: str
    aliases: tuple[str, ...]
    origin_ms: int
    updated_ms: int | None
    longitude: float
    latitude: float
    depth_km: float | None
    magnitude: float | None
    magnitude_type: str | None
    event_type: str | None
    review_status: str | None
    # Normalized JSON retains every source field, including unknown ones. Never render as HTML.
    raw_feature_json: str
    feature_sha256: str


@dataclass(frozen=True)
class SnapshotCandidate:
    source_url: str
    retrieved_at: str
    generated_ms: int | None
    http_status: int
    body_sha256: str
    events: tuple[EventCandidate, ...]
    query_limit_reached: bool
    # Parsing proves neither catalog completeness nor permission to expose this material.
    coverage: str = "NOT_ESTABLISHED"
    admission: str = "NOT_ADMITTED"


def parse_snapshot(body: bytes, *, status: int, source_url: str,
                   retrieved_at: str, max_bytes: int = 8 * 1024 * 1024,
                   max_events: int = 20000) -> SnapshotCandidate:
    """Parse already obtained bytes; reject a whole malformed response, never silently drop rows."""
    kind, query_limit = _request_kind(source_url)
    retrieved = _iso(_utc(retrieved_at))
    _integer(max_bytes, 1, 16 * 1024 * 1024)
    _integer(max_events, 1, 20000)
    if type(status) is not int or not isinstance(body, bytes) or len(body) > max_bytes:
        raise EarthquakeInputError("RESPONSE_BOUND")
    digest = "sha256:" + sha256(body).hexdigest()
    if status == 204 and kind == "query" and not body:
        return SnapshotCandidate(source_url, retrieved, None, status, digest, (), False)
    if status != 200:
        raise EarthquakeInputError("HTTP_STATUS")
    try:
        payload = json.loads(body.decode("utf-8"), object_pairs_hook=_object_pairs,
                             parse_constant=_constant)
    except (UnicodeError, ValueError, RecursionError):
        raise EarthquakeInputError("INVALID_JSON") from None
    if not isinstance(payload, dict) or payload.get("type") != "FeatureCollection":
        raise EarthquakeInputError("COLLECTION_SHAPE")
    features, metadata = payload.get("features"), payload.get("metadata")
    if not isinstance(features, list) or len(features) > max_events or not isinstance(metadata, dict):
        raise EarthquakeInputError("COLLECTION_BOUND")
    if query_limit is not None and len(features) > query_limit:
        raise EarthquakeInputError("QUERY_LIMIT_EXCEEDED")
    if type(metadata.get("count")) is not int or metadata["count"] != len(features):
        raise EarthquakeInputError("COUNT_MISMATCH")
    if type(metadata.get("status")) is not int or metadata["status"] != 200:
        raise EarthquakeInputError("METADATA_STATUS")
    generated = _milliseconds(metadata.get("generated"))
    events: list[EventCandidate] = []
    seen: set[str] = set()
    for feature in features:
        if not isinstance(feature, dict) or feature.get("type") != "Feature":
            raise EarthquakeInputError("FEATURE_SHAPE")
        event_id = feature.get("id")
        if not isinstance(event_id, str) or not IDENTIFIER.fullmatch(event_id):
            raise EarthquakeInputError("EVENT_ID")
        props, geometry = feature.get("properties"), feature.get("geometry")
        if not isinstance(props, dict) or not isinstance(geometry, dict) or geometry.get("type") != "Point":
            raise EarthquakeInputError("EVENT_SHAPE")
        coordinates = geometry.get("coordinates")
        if not isinstance(coordinates, list) or len(coordinates) != 3:
            raise EarthquakeInputError("COORDINATE_SHAPE")
        lon, lat = _number(coordinates[0]), _number(coordinates[1])
        if not (-180 <= lon <= 180 and -90 <= lat <= 90):
            raise EarthquakeInputError("COORDINATE_RANGE")
        depth = None if coordinates[2] is None else _number(coordinates[2])
        mag = None if props.get("mag") is None else _number(props["mag"])
        raw_aliases = props.get("ids")
        if raw_aliases is None:
            aliases = (event_id,)
        else:
            _text(raw_aliases, required=True)
            parts = tuple(item for item in raw_aliases.split(",") if item)
            if len(parts) > 128 or any(not IDENTIFIER.fullmatch(item) for item in parts):
                raise EarthquakeInputError("EVENT_ALIASES")
            aliases = tuple(dict.fromkeys((event_id, *parts)))
        if seen.intersection(aliases):
            raise EarthquakeInputError("IDENTITY_CONFLICT")
        seen.update(aliases)
        try:
            raw_json = json.dumps(feature, sort_keys=True, ensure_ascii=True,
                                  separators=(",", ":"), allow_nan=False)
        except (ValueError, RecursionError):
            raise EarthquakeInputError("FEATURE_JSON") from None
        events.append(EventCandidate(event_id, aliases, _milliseconds(props.get("time")),
                      _milliseconds(props.get("updated"), nullable=True), lon, lat, depth, mag,
                      _text(props.get("magType")), _text(props.get("type")),
                      _text(props.get("status")), raw_json,
                      "sha256:" + sha256(raw_json.encode("utf-8")).hexdigest()))
    return SnapshotCandidate(source_url, retrieved, generated, status, digest, tuple(events),
                             query_limit is not None and len(events) >= query_limit)


def select_earthquakes(snapshot: SnapshotCandidate, *, start: str, end: str,
                       bounds=KANSAS_CONTEXT) -> tuple[EventCandidate, ...]:
    """Select exact earthquake types in a context bbox and a half-open time window.

    This is not a state-boundary join, authoritative event association or a count
    of all earthquakes that occurred. The original immutable snapshot is retained.
    """
    first, stop = _utc(start), _utc(end)
    west, south, east, north = _bounds(bounds)
    if first >= stop:
        raise EarthquakeInputError("TIME_ORDER")
    return tuple(event for event in snapshot.events if event.event_type == "earthquake"
                 and west <= event.longitude <= east and south <= event.latitude <= north
                 and first <= EPOCH + timedelta(milliseconds=event.origin_ms) < stop)
