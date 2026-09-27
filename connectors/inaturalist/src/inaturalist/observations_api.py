"""Offline iNaturalist observation-search planning and supplied-page parsing; never fetches.

Transport, activation, taxonomy reconciliation, KFM sensitivity ranking,
redaction, persistence and publication belong to owning layers. Upstream
geoprivacy is preserved as evidence: obscured or private coordinates are never
repaired, re-centred, or treated as precise, and no record is public-safe here.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json
import math
import re
from urllib.parse import parse_qs, urlencode, urlsplit

HOST = "https://api.inaturalist.org"
SEARCH_PATH = "/v1/observations"
# The API serves at most 200 rows per page and refuses page-number paging past
# 10,000 rows, so captures walk an ascending id cursor (``id_above``) instead.
MAX_PAGE = 200
# Context envelope, not the legal Kansas boundary or a completeness guarantee.
KANSAS_CONTEXT = (-102.1, 36.9, -94.5, 40.1)
QUALITY_GRADES = frozenset({"research", "needs_id", "casual"})
GEOPRIVACY = {None: 0, "open": 0, "obscured": 1, "private": 2}
# Recognized observation licences; everything else (including null, which the
# platform uses for all-rights-reserved) is unresolved.
LICENSES = frozenset({"cc0", "cc-by", "cc-by-sa", "cc-by-nd", "cc-by-nc", "cc-by-nc-sa",
                      "cc-by-nc-nd"})
QUERY_KEYS = frozenset({"swlat", "swlng", "nelat", "nelng", "place_id", "taxon_id",
                        "quality_grade", "d1", "d2", "per_page", "order", "order_by",
                        "id_above"})
DATE = re.compile(r"\d{4}-\d{2}-\d{2}\Z")
# Personal data minimization: only these user fields are carried, as attribution.
USER_FIELDS = ("id", "login")
# Observation records are shallow; deeper nesting is malformed input, not data.
MAX_RECORD_DEPTH = 64


class ObservationInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for rejected candidate input."""


def _integer(value: object, minimum: int, maximum: int) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise ObservationInputError("INTEGER_BOUND")
    return value


def _utc(value: object) -> str:
    try:
        if not isinstance(value, str) or len(value) > 40:
            raise ValueError
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError
        return result.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    except (ValueError, TypeError, OverflowError):
        raise ObservationInputError("UTC_TIME") from None


def _text(value: object, *, limit: int = 2048) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value or len(value) > limit or "\x00" in value:
        raise ObservationInputError("TEXT_SHAPE")
    return value


def _finite(value: object) -> float:
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ObservationInputError("FINITE_NUMBER")
    return float(value)


def _bounds(value: object) -> tuple[float, float, float, float]:
    if not isinstance(value, (tuple, list)) or len(value) != 4:
        raise ObservationInputError("BBOX_SHAPE")
    west, south, east, north = map(_finite, value)
    if not (-180 <= west < east <= 180 and -90 <= south < north <= 90):
        raise ObservationInputError("BBOX_RANGE")
    return west, south, east, north


@dataclass(frozen=True)
class ObservationQuery:
    """One bounded capture scope; the bbox is a context filter, not a boundary join."""
    bounds: tuple[float, float, float, float] | None = KANSAS_CONTEXT
    place_id: int | None = None
    taxon_id: int | None = None
    quality_grade: str | None = None
    observed_from: str | None = None
    observed_to: str | None = None

    def params(self) -> dict[str, str]:
        if (self.bounds is None) == (self.place_id is None):
            raise ObservationInputError("SCOPE_EXACTLY_ONE")
        params: dict[str, str] = {}
        if self.bounds is not None:
            west, south, east, north = _bounds(self.bounds)
            params.update(swlat=repr(south), swlng=repr(west), nelat=repr(north),
                          nelng=repr(east))
        else:
            params["place_id"] = str(_integer(self.place_id, 1, 2**31 - 1))
        if self.taxon_id is not None:
            params["taxon_id"] = str(_integer(self.taxon_id, 1, 2**31 - 1))
        if self.quality_grade is not None:
            if self.quality_grade not in QUALITY_GRADES:
                raise ObservationInputError("QUALITY_GRADE")
            params["quality_grade"] = self.quality_grade
        for key, value in (("d1", self.observed_from), ("d2", self.observed_to)):
            if value is not None:
                if not isinstance(value, str) or not DATE.fullmatch(value):
                    raise ObservationInputError("OBSERVED_DATE")
                try:
                    datetime.strptime(value, "%Y-%m-%d")  # reject 2020-13-01, 2021-02-29
                except ValueError:
                    raise ObservationInputError("OBSERVED_DATE") from None
                params[key] = value
        if "d1" in params and "d2" in params and params["d1"] > params["d2"]:
            raise ObservationInputError("OBSERVED_DATE_ORDER")
        return params


def page_url(query: ObservationQuery, *, id_above: int = 0, per_page: int = MAX_PAGE) -> str:
    """Return one cursor page URL, not a network or scheduling operation."""
    _integer(id_above, 0, 2**53)
    _integer(per_page, 1, MAX_PAGE)
    return f"{HOST}{SEARCH_PATH}?" + urlencode(dict(
        query.params(), per_page=per_page, order="asc", order_by="id", id_above=id_above))


def _request(url: object) -> tuple[tuple[tuple[str, str], ...], int, int]:
    if not isinstance(url, str) or len(url) > 4096 or any(ord(c) <= 32 for c in url):
        raise ObservationInputError("SOURCE_URL")
    try:
        parsed = urlsplit(url)
        if (parsed.scheme != "https" or parsed.netloc != "api.inaturalist.org"
                or parsed.path != SEARCH_PATH or parsed.fragment):
            raise ValueError
        raw = parse_qs(parsed.query, strict_parsing=True, keep_blank_values=True)
        if set(raw) - QUERY_KEYS or any(len(v) != 1 or not v[0] for v in raw.values()):
            raise ValueError
        params = {key: value[0] for key, value in raw.items()}
        if params.pop("order") != "asc" or params.pop("order_by") != "id":
            raise ValueError
        per_page, id_above = int(params.pop("per_page")), int(params.pop("id_above"))
        _integer(per_page, 1, MAX_PAGE)
        _integer(id_above, 0, 2**53)
        return tuple(sorted(params.items())), per_page, id_above
    except (KeyError, ValueError, TypeError, ObservationInputError):
        raise ObservationInputError("SOURCE_URL") from None


def _object_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ObservationInputError("DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def _constant(_: str) -> None:
    raise ObservationInputError("NONSTANDARD_JSON_NUMBER")


@dataclass(frozen=True)
class ObservationCandidate:
    observation_id: int
    quality_grade: str | None
    license_code: str | None
    rights_holder: str | None
    taxon_id: int | None
    taxon_name: str | None
    taxon_rank: str | None
    observed_on: str | None
    updated_at: str | None
    # Coordinates exactly as supplied. For obscured records they are the
    # platform's randomized point, never an observation location.
    latitude: float | None
    longitude: float | None
    positional_accuracy_m: float | None
    geoprivacy_status: str
    precision_class: str
    route: str
    reasons: tuple[str, ...]
    # Minimized JSON: every source field except user profile data. Never log or render it.
    raw_record_json: str
    record_sha256: str
    sensitivity: str = "NOT_EVALUATED"
    admission: str = "NOT_ADMITTED"


def _minimize_users(value: object, depth: int = 0) -> object:
    """Project every nested ``user`` object (observer, identifiers, commenters) to id/login."""
    if depth > MAX_RECORD_DEPTH:
        raise ObservationInputError("RECORD_DEPTH")
    if isinstance(value, list):
        return [_minimize_users(item, depth + 1) for item in value]
    if not isinstance(value, dict):
        return value
    result = {}
    for key, item in value.items():
        if key == "user" and isinstance(item, dict):
            result[key] = {field: item[field] for field in USER_FIELDS if field in item}
        else:
            result[key] = _minimize_users(item, depth + 1)
    return result


def _point(record: dict[str, object]) -> tuple[float | None, float | None]:
    geojson = record.get("geojson")
    if geojson is None:
        return None, None
    if not isinstance(geojson, dict) or geojson.get("type") != "Point":
        raise ObservationInputError("GEOMETRY_SHAPE")
    coordinates = geojson.get("coordinates")
    if not isinstance(coordinates, list) or len(coordinates) != 2:
        raise ObservationInputError("GEOMETRY_SHAPE")
    lon, lat = _finite(coordinates[0]), _finite(coordinates[1])
    if not (-180 <= lon <= 180 and -90 <= lat <= 90):
        raise ObservationInputError("COORDINATE_RANGE")
    return lat, lon


def _classify(record: dict[str, object]) -> ObservationCandidate:
    observation_id = record.get("id")
    if type(observation_id) is not int or observation_id < 1:
        raise ObservationInputError("OBSERVATION_ID")
    reasons: list[str] = []
    grade = _text(record.get("quality_grade"), limit=16)
    if grade not in QUALITY_GRADES:
        reasons.append("QUALITY_GRADE_UNKNOWN")
    elif grade != "research":
        reasons.append("NOT_RESEARCH_GRADE")
    license_code = _text(record.get("license_code"), limit=32)
    license_code = license_code.lower() if license_code else None
    if license_code not in LICENSES:
        reasons.append("LICENSE_UNRESOLVED")
    else:
        if "-nc" in license_code:
            reasons.append("NONCOMMERCIAL_TERMS")
        if "-sa" in license_code:
            reasons.append("SHAREALIKE_TERMS")
        if "-nd" in license_code:
            reasons.append("NODERIVATIVES_TERMS")
    user = record.get("user")
    if user is not None and not isinstance(user, dict):
        raise ObservationInputError("USER_SHAPE")
    rights_holder = _text((user or {}).get("login"), limit=128)
    if rights_holder is None:
        reasons.append("ATTRIBUTION_MISSING")
    # The more restrictive of observer and taxon geoprivacy governs.
    states = (record.get("geoprivacy"), record.get("taxon_geoprivacy"))
    if any(state not in GEOPRIVACY for state in states):
        raise ObservationInputError("GEOPRIVACY_STATE")
    level = max(GEOPRIVACY[state] for state in states)
    obscured_flag = record.get("obscured")
    if obscured_flag not in (None, True, False):
        raise ObservationInputError("OBSCURED_FLAG")
    if obscured_flag is True:
        level = max(level, 1)
    status = ("open", "obscured", "private")[level]
    latitude, longitude = _point(record)
    if status == "private":
        reasons.append("GEOPRIVACY_PRIVATE")
        precision = "withheld" if latitude is None else "private_supplied"
    elif status == "obscured":
        reasons.append("GEOPRIVACY_OBSCURED")
        precision = "obscured_randomized"
    else:
        precision = "source_point" if latitude is not None else "absent"
    if latitude is None and status == "open":
        reasons.append("COORDINATES_ABSENT")
    accuracy = record.get("positional_accuracy")
    if accuracy is not None and (_finite(accuracy) < 0):
        raise ObservationInputError("POSITIONAL_ACCURACY")
    taxon = record.get("taxon")
    if taxon is not None and not isinstance(taxon, dict):
        raise ObservationInputError("TAXON_SHAPE")
    taxon_id = (taxon or {}).get("id")
    if taxon_id is not None and (type(taxon_id) is not int or taxon_id < 1):
        raise ObservationInputError("TAXON_ID")
    if taxon_id is None:
        reasons.append("TAXON_ABSENT")
    if record.get("captive") is True:
        reasons.append("CAPTIVE_OR_CULTIVATED")
    minimized = _minimize_users(record)
    try:
        raw_json = json.dumps(minimized, sort_keys=True, ensure_ascii=True,
                              separators=(",", ":"), allow_nan=False)
    except (ValueError, RecursionError):
        raise ObservationInputError("RECORD_JSON") from None
    # Licence obligations, grade, and captive state are carried as flags; unresolved
    # rights, attribution, taxon, or any geoprivacy restriction goes to quarantine.
    flags = {"NONCOMMERCIAL_TERMS", "SHAREALIKE_TERMS", "NODERIVATIVES_TERMS",
             "NOT_RESEARCH_GRADE", "CAPTIVE_OR_CULTIVATED"}
    blocking = [reason for reason in reasons if reason not in flags]
    return ObservationCandidate(
        observation_id, grade, license_code, rights_holder, taxon_id,
        _text((taxon or {}).get("name"), limit=512), _text((taxon or {}).get("rank"), limit=64),
        _text(record.get("observed_on"), limit=32), _text(record.get("updated_at"), limit=64),
        latitude, longitude, None if accuracy is None else float(accuracy), status, precision,
        "QUARANTINE_CANDIDATE" if blocking else "RAW_CANDIDATE", tuple(reasons), raw_json,
        "sha256:" + sha256(raw_json.encode("utf-8")).hexdigest())


@dataclass(frozen=True)
class PageCandidate:
    source_url: str
    query: tuple[tuple[str, str], ...]
    id_above: int
    per_page: int
    total_results: int
    retrieved_at: str
    body_sha256: str
    records: tuple[ObservationCandidate, ...]

    @property
    def is_last(self) -> bool:
        return len(self.records) < self.per_page

    @property
    def next_id_above(self) -> int | None:
        return None if self.is_last else self.records[-1].observation_id


def parse_page(body: bytes, *, status: int, source_url: str, retrieved_at: str,
               max_bytes: int = 16 * 1024 * 1024) -> PageCandidate:
    """Parse one supplied cursor page; reject a malformed page whole, never drop rows."""
    query, per_page, id_above = _request(source_url)
    retrieved = _utc(retrieved_at)
    _integer(max_bytes, 1, 64 * 1024 * 1024)
    if type(status) is not int or not isinstance(body, bytes) or len(body) > max_bytes:
        raise ObservationInputError("RESPONSE_BOUND")
    if status == 429:
        raise ObservationInputError("RATE_LIMITED")
    if status != 200:
        raise ObservationInputError("HTTP_STATUS")
    try:
        payload = json.loads(body.decode("utf-8"), object_pairs_hook=_object_pairs,
                             parse_constant=_constant)
    except (UnicodeError, ValueError, RecursionError):
        raise ObservationInputError("INVALID_JSON") from None
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
        raise ObservationInputError("PAGE_SHAPE")
    total, reported_per_page = payload.get("total_results"), payload.get("per_page")
    if type(total) is not int or total < 0 or type(reported_per_page) is not int:
        raise ObservationInputError("PAGE_METADATA")
    if reported_per_page != per_page or len(payload["results"]) > per_page:
        raise ObservationInputError("PAGE_WINDOW_MISMATCH")
    if len(payload["results"]) > total:
        raise ObservationInputError("COUNT_MISMATCH")
    records: list[ObservationCandidate] = []
    for record in payload["results"]:
        if not isinstance(record, dict):
            raise ObservationInputError("RECORD_SHAPE")
        records.append(_classify(record))
    ids = [item.observation_id for item in records]
    if any(left >= right for left, right in zip(ids, ids[1:])) or (ids and ids[0] <= id_above):
        raise ObservationInputError("CURSOR_ORDER")
    return PageCandidate(source_url, query, id_above, per_page, total, retrieved,
                         "sha256:" + sha256(body).hexdigest(), tuple(records))


def next_page_url(page: PageCandidate) -> str | None:
    """Return the next cursor URL for a parsed page, or None once the walk is finished."""
    if not isinstance(page, PageCandidate):
        raise ObservationInputError("PAGE_TYPE")
    if page.next_id_above is None:
        return None
    return f"{HOST}{SEARCH_PATH}?" + urlencode(dict(
        page.query, per_page=page.per_page, order="asc", order_by="id",
        id_above=page.next_id_above))


@dataclass(frozen=True)
class CaptureCandidate:
    outcome: str
    reasons: tuple[str, ...]
    reported_total: int
    records: tuple[ObservationCandidate, ...]
    page_sha256: tuple[str, ...]
    # Cursor continuity is not biological completeness, absence, or abundance.
    coverage: str = "NOT_ESTABLISHED"
    admission: str = "NOT_ADMITTED"


def reconcile(pages: tuple[PageCandidate, ...] | list[PageCandidate]) -> CaptureCandidate:
    """Join a cursor walk into one finite outcome.

    With ``id_above`` each page reports the records remaining past its cursor, so
    every page's ``total_results`` must equal the first page's minus the records
    already seen. ``CAPTURE_CANDIDATE`` requires an unbroken cursor chain from
    ``id_above=0`` to a short final page with no count drift; anything else is
    ``INCOMPLETE_CAPTURE`` and belongs in quarantine.
    """
    if not pages or any(not isinstance(page, PageCandidate) for page in pages):
        raise ObservationInputError("NO_PAGES" if not pages else "PAGE_TYPE")
    ordered = sorted(pages, key=lambda page: page.id_above)
    if len({(page.query, page.per_page) for page in ordered}) != 1:
        raise ObservationInputError("MIXED_QUERY")
    reasons: list[str] = []
    if ordered[0].id_above != 0:
        reasons.append("CURSOR_NOT_FROM_START")
    seen = 0
    for previous, page in zip([None, *ordered], ordered):
        if previous is not None and page.id_above != previous.next_id_above:
            reasons.append("CURSOR_GAP_OR_OVERLAP")
            break
        if page.total_results != ordered[0].total_results - seen:
            reasons.append("COUNT_DRIFT")
            break
        seen += len(page.records)
    if not ordered[-1].is_last:
        reasons.append("END_NOT_REACHED")
    if any(page.is_last for page in ordered[:-1]):
        reasons.append("EARLY_END")
    records = tuple(record for page in ordered for record in page.records)
    if seen == len(records) and not reasons and len(records) != ordered[0].total_results:
        reasons.append("COUNT_MISMATCH")
    return CaptureCandidate("INCOMPLETE_CAPTURE" if reasons else "CAPTURE_CANDIDATE",
                            tuple(dict.fromkeys(reasons)), ordered[0].total_results, records,
                            tuple(page.body_sha256 for page in ordered))
