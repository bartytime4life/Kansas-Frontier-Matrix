"""Offline NWS API alert-collection planning and parsing as official-source context; never fetches.

KFM is not an alerting system. NWS remains the issuing public-safety
authority. This module preserves NWS-authored alert messages source-faithfully
and computes freshness *as of a caller-supplied instant* as evidence for
downstream review. It never labels a message "current", never surfaces
instruction text as a field, never merges messages, and never emits a KFM
alert, notification, or directive. The seven-day ``/alerts`` surface is not an
archive and parsing it proves no completeness.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime, timezone
from hashlib import sha256
import json
import re
from urllib.parse import parse_qs, urlencode, urlsplit

HOST = "https://api.weather.gov"
AREA = re.compile(r"[A-Z]{2}\Z")
STATUSES = frozenset({"Actual", "Exercise", "System", "Test", "Draft"})
MESSAGE_TYPES = frozenset({"Alert", "Update", "Cancel", "Ack", "Error"})
AUTHORITY = "NWS_ISSUED_CONTEXT_ONLY"
CACHE_HEADERS = ("Cache-Control", "Date", "Expires", "Last-Modified", "ETag")


class NwsInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for rejected candidate input."""


def _instant(value: object, code: str = "TIME_FORMAT") -> datetime:
    try:
        if not isinstance(value, str) or len(value) > 40:
            raise ValueError
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError
        return result.astimezone(timezone.utc)
    except (ValueError, TypeError, OverflowError):
        raise NwsInputError(code) from None


def alerts_url(area: str = "KS", *, active: bool = True) -> str:
    """Return one area-filtered alerts URL; never adds cache-busting parameters."""
    if not isinstance(area, str) or not AREA.fullmatch(area):
        raise NwsInputError("AREA")
    path = "/alerts/active" if active else "/alerts"
    return f"{HOST}{path}?" + urlencode({"area": area})


def _request(url: object) -> tuple[str, str]:
    if not isinstance(url, str) or len(url) > 2048 or any(ord(c) <= 32 for c in url):
        raise NwsInputError("SOURCE_URL")
    parsed = urlsplit(url)
    if (parsed.scheme != "https" or parsed.netloc != "api.weather.gov"
            or parsed.path not in ("/alerts", "/alerts/active") or parsed.fragment):
        raise NwsInputError("SOURCE_URL")
    try:
        raw = parse_qs(parsed.query, strict_parsing=True)
    except ValueError:
        raise NwsInputError("SOURCE_URL") from None
    if set(raw) != {"area"} or len(raw["area"]) != 1 or not AREA.fullmatch(raw["area"][0]):
        raise NwsInputError("SOURCE_URL")
    return parsed.path, raw["area"][0]


@dataclass(frozen=True)
class AlertCandidate:
    alert_id: str
    canonical_url: str
    event: str
    status: str
    message_type: str
    sender: str | None
    severity: str | None
    certainty: str | None
    urgency: str | None
    sent: str
    effective: str | None
    onset: str | None
    expires: str | None
    ends: str | None
    references: tuple[str, ...]
    ugc_codes: tuple[str, ...]
    has_geometry: bool
    # Instruction text stays inside raw_feature_json as NWS-authored content only.
    has_instruction: bool
    freshness_as_of: str
    freshness_state: str
    route: str
    reasons: tuple[str, ...]
    raw_feature_json: str
    feature_sha256: str
    authority: str = AUTHORITY
    life_safety_authority: bool = False
    admission: str = "NOT_ADMITTED"


@dataclass(frozen=True)
class AlertCollectionCandidate:
    source_url: str
    area: str
    active_endpoint: bool
    retrieved_at: str
    http_status: int
    cache_headers: tuple[tuple[str, str], ...]
    body_sha256: str | None
    alerts: tuple[AlertCandidate, ...]
    outcome: str
    reasons: tuple[str, ...]
    coverage: str = "NOT_ESTABLISHED"


def _optional_time(props: dict[str, object], key: str) -> datetime | None:
    value = props.get(key)
    return None if value is None else _instant(value)


def _freshness(as_of: datetime, effective: datetime | None, expires: datetime | None,
               ends: datetime | None, message_type: str, superseded: bool) -> str:
    # Order matters: a message replaced or cancelled by a later one in the same
    # collection is never reported by its own window alone.
    if superseded:
        return "SUPERSEDED_IN_COLLECTION"
    if message_type == "Cancel":
        return "CANCELLATION_MESSAGE"
    if ends is not None and ends <= as_of:
        return "ENDED"
    if expires is not None and expires <= as_of:
        return "EXPIRED"
    if effective is not None and effective > as_of:
        return "NOT_YET_EFFECTIVE"
    if expires is None and ends is None:
        return "UNKNOWN_NO_END_TIME"
    return "WITHIN_SOURCE_WINDOW_AT_AS_OF"


def _feature(feature: object, area: str) -> tuple[AlertCandidate, datetime | None,
                                                  datetime | None, datetime | None, datetime]:
    if not isinstance(feature, dict) or feature.get("type") != "Feature":
        raise NwsInputError("FEATURE_SHAPE")
    props = feature.get("properties")
    if not isinstance(props, dict):
        raise NwsInputError("FEATURE_SHAPE")
    alert_id, canonical = props.get("id"), feature.get("id")
    if (not isinstance(alert_id, str) or not alert_id.startswith("urn:oid:")
            or len(alert_id) > 256 or not isinstance(canonical, str)
            or canonical != f"{HOST}/alerts/{alert_id}"):
        raise NwsInputError("ALERT_IDENTITY")
    status, message_type = props.get("status"), props.get("messageType")
    if (not isinstance(status, str) or not isinstance(message_type, str)
            or status not in STATUSES or message_type not in MESSAGE_TYPES):
        raise NwsInputError("ALERT_ENUM")
    event = props.get("event")
    if not isinstance(event, str) or not event or len(event) > 256:
        raise NwsInputError("ALERT_EVENT")
    sent = _instant(props.get("sent"))
    effective, onset = _optional_time(props, "effective"), _optional_time(props, "onset")
    expires, ends = _optional_time(props, "expires"), _optional_time(props, "ends")
    references = props.get("references") or []
    if not isinstance(references, list):
        raise NwsInputError("REFERENCES_SHAPE")
    reference_ids = []
    for reference in references:
        identifier = reference.get("identifier") if isinstance(reference, dict) else None
        if not isinstance(identifier, str) or not identifier.startswith("urn:oid:"):
            raise NwsInputError("REFERENCES_SHAPE")
        reference_ids.append(identifier)
    geocode = props.get("geocode") or {}
    ugc = geocode.get("UGC", []) if isinstance(geocode, dict) else None
    if not isinstance(ugc, list) or any(not isinstance(code, str) for code in ugc):
        raise NwsInputError("GEOCODE_SHAPE")
    geometry = feature.get("geometry")
    if geometry is not None and (not isinstance(geometry, dict)
                                 or geometry.get("type") not in ("Polygon", "MultiPolygon")):
        raise NwsInputError("GEOMETRY_SHAPE")
    reasons: list[str] = []
    if status != "Actual":
        reasons.append("STATUS_NOT_ACTUAL")
    if not any(code.startswith(area) for code in ugc):
        reasons.append("OUTSIDE_REQUESTED_AREA")
    if expires is not None and expires < sent:
        reasons.append("EXPIRES_BEFORE_SENT")
    if message_type in ("Update", "Cancel") and not reference_ids:
        reasons.append("LINEAGE_REFERENCE_MISSING")
    try:
        raw_json = json.dumps(feature, sort_keys=True, ensure_ascii=True,
                              separators=(",", ":"), allow_nan=False)
    except (ValueError, RecursionError):
        raise NwsInputError("FEATURE_JSON") from None
    iso = lambda value: None if value is None else value.isoformat().replace("+00:00", "Z")  # noqa: E731
    candidate = AlertCandidate(
        alert_id, canonical, event, status, message_type,
        props.get("sender") if isinstance(props.get("sender"), str) else None,
        *(props.get(k) if isinstance(props.get(k), str) else None
          for k in ("severity", "certainty", "urgency")),
        iso(sent), iso(effective), iso(onset), iso(expires), iso(ends),
        tuple(reference_ids), tuple(ugc), geometry is not None,
        isinstance(props.get("instruction"), str) and bool(props["instruction"]),
        "", "", "QUARANTINE_CANDIDATE" if reasons else "RAW_CANDIDATE",
        tuple(reasons), raw_json, "sha256:" + sha256(raw_json.encode("utf-8")).hexdigest())
    return candidate, effective, expires, ends, sent


def parse_alerts(body: bytes, *, status: int, source_url: str, retrieved_at: str,
                 as_of: str | None = None, headers: dict[str, str] | None = None,
                 max_bytes: int = 16 * 1024 * 1024,
                 max_features: int = 2000) -> AlertCollectionCandidate:
    """Parse one supplied alert collection; freshness is computed at ``as_of``.

    ``as_of`` defaults to ``retrieved_at``; it may not precede retrieval, and
    any later reuse must recompute freshness rather than trust a stored state.
    """
    path, area = _request(source_url)
    retrieved = _instant(retrieved_at, "UTC_TIME")
    at = retrieved if as_of is None else _instant(as_of, "UTC_TIME")
    if at < retrieved:
        raise NwsInputError("AS_OF_BEFORE_RETRIEVAL")
    cache = tuple((name, headers[name]) for name in CACHE_HEADERS
                  if headers and isinstance(headers.get(name), str))
    stamp = retrieved.isoformat().replace("+00:00", "Z")
    if type(status) is not int or not isinstance(body, bytes) or len(body) > max_bytes:
        raise NwsInputError("RESPONSE_BOUND")
    if status == 304:
        return AlertCollectionCandidate(source_url, area, path.endswith("active"), stamp, 304,
                                        cache, None, (), "NO_OP", ("NOT_MODIFIED",))
    if status == 429:
        raise NwsInputError("RATE_LIMITED")
    if status != 200:
        raise NwsInputError("HTTP_STATUS")
    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeError, ValueError, RecursionError):
        raise NwsInputError("INVALID_JSON") from None
    if not isinstance(payload, dict) or payload.get("type") != "FeatureCollection":
        raise NwsInputError("COLLECTION_SHAPE")
    features = payload.get("features")
    if not isinstance(features, list) or len(features) > max_features:
        raise NwsInputError("COLLECTION_BOUND")
    parsed = [_feature(feature, area) for feature in features]
    ids = [item[0].alert_id for item in parsed]
    if len(set(ids)) != len(ids):
        raise NwsInputError("DUPLICATE_ALERT_ID")
    referenced = {ref for item in parsed for ref in item[0].references}
    alerts = []
    for candidate, effective, expires, ends, _ in parsed:
        state = _freshness(at, effective, expires, ends, candidate.message_type,
                           candidate.alert_id in referenced)
        alerts.append(replace(candidate, freshness_as_of=at.isoformat().replace("+00:00", "Z"),
                              freshness_state=state))
    reasons: list[str] = []
    pagination = payload.get("pagination")
    if isinstance(pagination, dict) and pagination.get("next"):
        reasons.append("PARTIAL_COLLECTION_MORE_PAGES")
    if not path.endswith("active"):
        reasons.append("SEVEN_DAY_WINDOW_NOT_ARCHIVE")
    return AlertCollectionCandidate(source_url, area, path.endswith("active"), stamp, 200,
                                    cache, "sha256:" + sha256(body).hexdigest(),
                                    tuple(alerts),
                                    # A known further page means this capture is partial.
                                    "INCOMPLETE_CAPTURE"
                                    if "PARTIAL_COLLECTION_MORE_PAGES" in reasons
                                    else "CAPTURE_CANDIDATE", tuple(reasons))
