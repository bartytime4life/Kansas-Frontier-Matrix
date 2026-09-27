"""Offline NRCS SCAN station-data planning and parsing via the AWDB REST API; never fetches.

A SCAN value is a station sensor observation at one depth and cadence, not an area,
field, or soil-map-unit truth. This module plans one canonical AWDB ``data`` URL for
Kansas SCAN-network stations and parses an *already supplied* JSON response into frozen
per-value candidates. Source value tokens and QC/QA flags are kept verbatim, a missing
value stays missing (never zero), and each series keeps its element, depth, duration and
unit exactly as the source states them.

The response layout, element codes, units, depth sign convention and flag vocabularies
are NEEDS VERIFICATION against current NWCC documentation: any unexpected shape rejects
the whole response rather than being coerced. Tribal SCAN stations are out of scope until
tribal review; only the ``SCAN`` network is planned. Station metadata review, activation,
persistence, aggregation and interpolation belong to owning layers.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation
from hashlib import sha256
import json
import math
import re
from urllib.parse import parse_qsl, urlencode, urlsplit

HOST = "https://wcc.sc.egov.usda.gov"
PATH = "/awdbRestApi/services/v1/data"
STATE = "KS"
NETWORK = "SCAN"
DURATIONS = {"DAILY": 366, "HOURLY": 31}  # duration -> maximum inclusive days per request
MAX_STATIONS = 10
MAX_ELEMENTS = 12
STATION_ID = re.compile(r"[1-9]\d{0,5}\Z")
# Source-native element code with optional ordinal/height-depth, e.g. ``SMS:-2``.
ELEMENT = re.compile(r"[A-Z][A-Z0-9]{1,5}(?::-?\d{1,4}){0,2}\Z")
DAY = re.compile(r"\d{4}-\d{2}-\d{2}\Z")
PARAMS = ("stationTriplets", "elements", "duration", "beginDate", "endDate")


class ScanInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for rejected candidate input."""


def _day(value: object) -> date:
    if not isinstance(value, str) or not DAY.fullmatch(value):
        raise ScanInputError("DATE_FORMAT")
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        raise ScanInputError("DATE_FORMAT") from None


def _utc(value: object) -> str:
    try:
        if not isinstance(value, str) or len(value) > 40:
            raise ValueError
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError
        return result.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    except (ValueError, TypeError, OverflowError):
        raise ScanInputError("UTC_TIME") from None


@dataclass(frozen=True)
class DataRequest:
    station_ids: tuple[str, ...]
    elements: tuple[str, ...]
    duration: str
    begin_date: str
    end_date: str

    @property
    def triplets(self) -> tuple[str, ...]:
        return tuple(f"{station}:{STATE}:{NETWORK}" for station in self.station_ids)


def _validate(station_ids: object, elements: object, duration: object, begin_date: object,
              end_date: object) -> DataRequest:
    if (not isinstance(station_ids, tuple) or not 1 <= len(station_ids) <= MAX_STATIONS
            or len(set(station_ids)) != len(station_ids)
            or any(not isinstance(s, str) or not STATION_ID.fullmatch(s) for s in station_ids)):
        raise ScanInputError("STATION")
    if (not isinstance(elements, tuple) or not 1 <= len(elements) <= MAX_ELEMENTS
            or len(set(elements)) != len(elements)
            or any(not isinstance(e, str) or not ELEMENT.fullmatch(e) for e in elements)):
        raise ScanInputError("ELEMENT")
    if duration not in DURATIONS:
        raise ScanInputError("DURATION")
    begin, end = _day(begin_date), _day(end_date)
    if not date(1980, 1, 1) <= begin <= end or (end - begin).days + 1 > DURATIONS[duration]:
        raise ScanInputError("DATE_RANGE")
    return DataRequest(station_ids, elements, duration, begin_date, end_date)


def data_url(station_ids: tuple[str, ...], elements: tuple[str, ...], *, duration: str,
             begin_date: str, end_date: str) -> str:
    """Return the one canonical AWDB data URL for Kansas SCAN stations and elements."""
    request = _validate(station_ids, elements, duration, begin_date, end_date)
    query = urlencode({"stationTriplets": ",".join(request.triplets),
                       "elements": ",".join(request.elements), "duration": duration,
                       "beginDate": begin_date, "endDate": end_date})
    return f"{HOST}{PATH}?{query}"


def parse_request(source_url: object) -> DataRequest:
    """Recover the request a planner URL encodes; anything non-canonical is refused."""
    if not isinstance(source_url, str) or len(source_url) > 2048 or any(
            ord(c) <= 32 for c in source_url):
        raise ScanInputError("SOURCE_URL")
    parsed = urlsplit(source_url)
    if (parsed.scheme != "https" or parsed.netloc != urlsplit(HOST).netloc
            or parsed.path != PATH or parsed.fragment):
        raise ScanInputError("SOURCE_URL")
    try:
        pairs = parse_qsl(parsed.query, keep_blank_values=True, strict_parsing=True)
    except ValueError:
        raise ScanInputError("SOURCE_URL") from None
    if tuple(key for key, _ in pairs) != PARAMS:
        raise ScanInputError("SOURCE_URL")
    values = dict(pairs)
    stations = []
    for triplet in values["stationTriplets"].split(","):
        station, state, network = (triplet.split(":") + ["", ""])[:3]
        if triplet.count(":") != 2 or state != STATE or network != NETWORK:
            raise ScanInputError("STATION_SCOPE")
        stations.append(station)
    request = _validate(tuple(stations), tuple(values["elements"].split(",")),
                        values["duration"], values["beginDate"], values["endDate"])
    if data_url(request.station_ids, request.elements, duration=request.duration,
                begin_date=request.begin_date, end_date=request.end_date) != source_url:
        raise ScanInputError("SOURCE_URL_SCOPE")
    return request


@dataclass(frozen=True)
class ScanValue:
    date: str
    raw: str | None
    value: Decimal | None
    missing: bool
    qc_flag: str | None
    qa_flag: str | None
    route: str
    reasons: tuple[str, ...]


@dataclass(frozen=True)
class ScanSeries:
    station_triplet: str
    element_code: str
    ordinal: int | None
    height_depth_raw: str | None
    duration: str
    stored_unit: str | None
    values: tuple[ScanValue, ...]
    reasons: tuple[str, ...]
    # Every source field of the element header verbatim; never log or render it.
    raw_element_json: str
    element_sha256: str


@dataclass(frozen=True)
class ScanDataCandidate:
    source_url: str
    request: DataRequest
    retrieved_at: str
    body_sha256: str
    series: tuple[ScanSeries, ...]
    # Parsing proves neither station-metadata validity nor completeness of the period.
    coverage: str = "NOT_ESTABLISHED"
    admission: str = "NOT_ADMITTED"


def _text(value: object, code: str, limit: int = 64) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or len(value) > limit:
        raise ScanInputError(code)
    return value


def _value(item: object, request: DataRequest) -> ScanValue:
    if not isinstance(item, dict) or not isinstance(item.get("date"), str):
        raise ScanInputError("VALUE_SHAPE")
    stamp = item["date"]
    try:
        day = datetime.strptime(stamp[:10], "%Y-%m-%d").date()
    except ValueError:
        raise ScanInputError("VALUE_DATE") from None
    if not _day(request.begin_date) <= day <= _day(request.end_date) or len(stamp) > 20:
        raise ScanInputError("VALUE_DATE")
    qc = _text(item.get("qcFlag"), "FLAG_SHAPE", 8)
    qa = _text(item.get("qaFlag"), "FLAG_SHAPE", 8)
    raw_value = item.get("value")
    if raw_value is None:
        return ScanValue(stamp, None, None, True, qc, qa, "RAW_CANDIDATE", ("VALUE_MISSING",))
    if isinstance(raw_value, bool) or not isinstance(raw_value, (int, float)) or (
            isinstance(raw_value, float) and not math.isfinite(raw_value)):
        return ScanValue(stamp, json.dumps(raw_value)[:32], None, False, qc, qa,
                         "QUARANTINE_CANDIDATE", ("VALUE_NOT_NUMERIC",))
    token = json.dumps(raw_value)
    try:
        parsed = Decimal(token)
    except InvalidOperation:  # pragma: no cover - json numbers are always Decimal-safe
        raise ScanInputError("VALUE_FORMAT") from None
    return ScanValue(stamp, token, parsed, False, qc, qa, "RAW_CANDIDATE", ())


def _series(station: dict, element: object, request: DataRequest) -> ScanSeries:
    if not isinstance(element, dict):
        raise ScanInputError("ELEMENT_SHAPE")
    header, values = element.get("stationElement"), element.get("values")
    if not isinstance(header, dict) or not isinstance(values, list):
        raise ScanInputError("ELEMENT_SHAPE")
    code = header.get("elementCode")
    if not isinstance(code, str) or code not in {e.split(":")[0] for e in request.elements}:
        raise ScanInputError("ELEMENT_NOT_REQUESTED")
    if header.get("durationName") != request.duration:
        raise ScanInputError("DURATION_MISMATCH")
    ordinal = header.get("ordinal")
    if ordinal is not None and (type(ordinal) is not int or not 0 <= ordinal <= 99):
        raise ScanInputError("ELEMENT_SHAPE")
    depth = header.get("heightDepth")
    if depth is not None and (isinstance(depth, bool) or not isinstance(depth, (int, float))):
        raise ScanInputError("ELEMENT_SHAPE")
    parsed = tuple(_value(item, request) for item in values)
    stamps = [value.date for value in parsed]
    if len(set(stamps)) != len(stamps):
        raise ScanInputError("DUPLICATE_VALUE_DATE")
    reasons = ["EMPTY_SERIES_NOT_ABSENCE"] if not parsed else []
    if depth is None and code.startswith(("SMS", "STO")):
        reasons.append("DEPTH_NOT_STATED")
    raw_json = json.dumps(header, sort_keys=True, ensure_ascii=True, separators=(",", ":"),
                          allow_nan=False)
    return ScanSeries(station["stationTriplet"], code, ordinal,
                      None if depth is None else json.dumps(depth), request.duration,
                      _text(header.get("storedUnitCode"), "ELEMENT_SHAPE", 16), parsed,
                      tuple(reasons), raw_json,
                      "sha256:" + sha256(raw_json.encode("ascii")).hexdigest())


def _reject_constant(token: str) -> None:
    # NaN/Infinity are not JSON; they must never read as a missing or numeric value.
    raise ValueError(token)


def parse_data(body: bytes, *, status: int, source_url: str, retrieved_at: str,
               max_bytes: int = 16 * 1024 * 1024,
               max_values: int = 200_000) -> ScanDataCandidate:
    """Parse one supplied AWDB data response; reject it whole on shape or scope drift."""
    request = parse_request(source_url)
    retrieved = _utc(retrieved_at)
    if type(status) is not int or not isinstance(body, bytes) or len(body) > max_bytes:
        raise ScanInputError("RESPONSE_BOUND")
    if status != 200:
        raise ScanInputError("HTTP_STATUS")
    try:
        payload = json.loads(body.decode("utf-8"), parse_constant=_reject_constant)
    except (UnicodeError, ValueError, RecursionError):
        raise ScanInputError("INVALID_JSON") from None
    if not isinstance(payload, list):
        raise ScanInputError("RESPONSE_SHAPE")
    series: list[ScanSeries] = []
    seen_stations: set[str] = set()
    try:
        for station in payload:
            if not isinstance(station, dict) or not isinstance(station.get("data"), list):
                raise ScanInputError("STATION_SHAPE")
            triplet = station.get("stationTriplet")
            if triplet not in request.triplets:
                raise ScanInputError("STATION_NOT_REQUESTED")
            if triplet in seen_stations:
                raise ScanInputError("DUPLICATE_STATION")
            seen_stations.add(triplet)
            for element in station["data"]:
                series.append(_series(station, element, request))
    except (TypeError, ValueError) as error:
        if isinstance(error, ScanInputError):
            raise
        raise ScanInputError("RESPONSE_SHAPE") from None
    if sum(len(item.values) for item in series) > max_values:
        raise ScanInputError("VALUE_BOUND")
    return ScanDataCandidate(source_url, request, retrieved,
                             "sha256:" + sha256(body).hexdigest(), tuple(series))
