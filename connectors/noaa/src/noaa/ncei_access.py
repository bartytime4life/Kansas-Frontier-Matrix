"""Bounded NCEI Access Data Service capture; no admission or release authority.

Requests always use the fixed HTTPS v1 endpoint. Imports and request planning
are inert. Exact JSON response bytes and native product flags are preserved;
inspection is not domain normalization, coverage certification, or publication.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
import json
import os
import re
import time
from types import MappingProxyType
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, build_opener

from connectors_core.captured_json import canonical_bytes, digest_bytes, utc_time
from .ghcnd import NoRedirect, utc_now

ENDPOINT = "https://www.ncei.noaa.gov/access/services/data/v1"
DOCUMENTATION = "https://www.ncei.noaa.gov/access/search/documentation/data-service/"
PROFILE = "kfm.ncei-access-capture/v1"
MAX_BYTES = 16 * 1024 * 1024
MAX_ROWS = 10000
MAX_STATIONS = 25
KANSAS_BBOX = "40.1,-102.2,36.9,-94.4"  # N,W,S,E; border envelope, not state membership.
PILOT_STATIONS = ("USW00003928", "USW00013985", "USW00013996", "USW00023065")


@dataclass(frozen=True)
class Product:
    role: str
    period: str
    elements: tuple[str, ...]
    baseline: str | None = None


PRODUCTS = MappingProxyType({
    "daily-summaries": Product("observation", "day", ("PRCP", "TMAX", "TMIN", "SNOW", "SNWD")),
    "global-summary-of-the-month": Product("aggregate", "month", ("PRCP", "TMAX", "TMIN", "TAVG", "SNOW")),
    "global-summary-of-the-year": Product("aggregate", "year", ("PRCP", "TMAX", "TMIN", "TAVG", "SNOW")),
    "normals-daily-1991-2020": Product("aggregate", "normal-day", ("DLY-TMAX-NORMAL", "DLY-TMIN-NORMAL"), "1991-2020"),
    "normals-monthly-1991-2020": Product("aggregate", "normal-month", ("MLY-PRCP-NORMAL", "MLY-TMAX-NORMAL", "MLY-TMIN-NORMAL"), "1991-2020"),
    "normals-annualseasonal-1991-2020": Product("aggregate", "normal-year", ("ANN-PRCP-NORMAL", "ANN-TMAX-NORMAL", "ANN-TMIN-NORMAL"), "1991-2020"),
})


def _date(value: str) -> date:
    try:
        parsed = date.fromisoformat(value)
    except (TypeError, ValueError):
        raise ValueError("REQUEST_DATE_INVALID") from None
    if parsed.isoformat() != value or not 1700 <= parsed.year <= 2200:
        raise ValueError("REQUEST_DATE_INVALID")
    return parsed


@dataclass(frozen=True)
class Query:
    dataset: str
    stations: tuple[str, ...] = PILOT_STATIONS
    start: str | None = None
    end: str | None = None
    elements: tuple[str, ...] | None = None
    units: str = "metric"
    max_bytes: int = 1024 * 1024

    def parameters(self) -> dict[str, str]:
        if not isinstance(self.dataset, str) or self.dataset not in PRODUCTS:
            raise ValueError("REQUEST_DATASET_NOT_ALLOWED")
        product = PRODUCTS[self.dataset]
        if (not isinstance(self.stations, tuple) or not 1 <= len(self.stations) <= MAX_STATIONS
                or any(not isinstance(s, str) or re.fullmatch(r"US[A-Z0-9]{9}", s) is None for s in self.stations)
                or len(set(self.stations)) != len(self.stations)):
            raise ValueError("REQUEST_STATIONS_INVALID")
        elements = product.elements if self.elements is None else self.elements
        if (not isinstance(elements, tuple) or not elements or len(elements) > len(product.elements)
                or any(not isinstance(e, str) or e not in product.elements for e in elements)
                or len(set(elements)) != len(elements)):
            raise ValueError("REQUEST_ELEMENTS_NOT_ALLOWED")
        if self.units not in ("metric", "standard"):
            raise ValueError("REQUEST_UNITS_INVALID")
        if type(self.max_bytes) is not int or not 1 <= self.max_bytes <= MAX_BYTES:
            raise ValueError("REQUEST_BYTE_LIMIT_INVALID")
        params = {"dataset": self.dataset, "stations": ",".join(sorted(self.stations)),
                  "dataTypes": ",".join(sorted(elements)), "bbox": KANSAS_BBOX,
                  "format": "json", "units": self.units, "includeAttributes": "true",
                  "includeStationName": "true", "includeStationLocation": "true"}
        if product.period in ("normal-month", "normal-year"):
            if self.start is not None or self.end is not None:
                raise ValueError("NORMAL_BASELINE_NOT_OBSERVATION_WINDOW")
        else:
            start, end = _date(self.start), _date(self.end)
            if start > end:
                raise ValueError("REQUEST_DATE_ORDER")
            if product.period in ("day", "normal-day") and (end - start).days >= 366:
                raise ValueError("REQUEST_WINDOW_LIMIT")
            if product.period == "normal-day" and start.year != end.year:
                raise ValueError("NORMAL_DAY_SINGLE_CALENDAR_YEAR_REQUIRED")
            params.update(startDate=self.start, endDate=self.end)
        return params

    def url(self) -> str:
        return ENDPOINT + "?" + urlencode(self.parameters())

    def plan(self) -> dict:
        params = self.parameters()
        product = PRODUCTS[self.dataset]
        return {"profile": PROFILE, "source_id": "noaa.ncei-access." + self.dataset,
                "parameters": params, "url": self.url(), "source_role": product.role,
                "period_kind": product.period, "baseline_period": product.baseline,
                "max_bytes": self.max_bytes, "max_rows": MAX_ROWS,
                "expected_bytes": None, "network": False,
                "source_admitted": False, "released": False, "published": False}


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("RESPONSE_DUPLICATE_KEY")
        result[key] = value
    return result


def _nonfinite(_value):
    raise ValueError("RESPONSE_NONFINITE_NUMBER")


def _number(token: str) -> Decimal:
    try:
        value = Decimal(token)
        if not value.is_finite():
            raise ValueError
        return value
    except (InvalidOperation, ValueError):
        raise ValueError("RESPONSE_NUMBER_INVALID") from None


def _period(row: dict, query: Query) -> str:
    kind = PRODUCTS[query.dataset].period
    token = row.get("DATE")
    if kind == "normal-year":
        # The verified annual-normal response has no DATE field.
        if token is not None:
            raise ValueError("RESPONSE_NORMAL_PERIOD_DRIFT")
        return "annual"
    if not isinstance(token, str):
        raise ValueError("RESPONSE_DATE_MISSING")
    try:
        if kind == "day":
            _date(token)
            valid = query.start <= token <= query.end
        elif kind == "month":
            _date(token + "-01")
            valid = query.start[:7] <= token <= query.end[:7]
        elif kind == "year":
            _date(token + "-01-01")
            valid = query.start[:4] <= token <= query.end[:4]
        elif kind == "normal-month":
            valid = re.fullmatch(r"0[1-9]|1[0-2]", token) is not None
        else:
            _date("2000-" + token)  # leap year validates the cyclic normal day.
            valid = query.start[5:] <= token <= query.end[5:]
    except ValueError:
        raise ValueError("RESPONSE_DATE_INVALID") from None
    if not valid:
        raise ValueError("RESPONSE_DATE_OUTSIDE_QUERY")
    return token


def inspect_response(raw: bytes, query: Query) -> dict:
    params = query.parameters()
    if not isinstance(raw, bytes) or not 0 < len(raw) <= query.max_bytes:
        raise ValueError("RESPONSE_BYTE_LIMIT")
    try:
        rows = json.loads(raw, object_pairs_hook=_unique, parse_constant=_nonfinite)
    except (UnicodeError, ValueError, RecursionError):
        raise ValueError("RESPONSE_JSON_INVALID") from None
    if not isinstance(rows, list) or len(rows) > MAX_ROWS:
        raise ValueError("RESPONSE_ROWS_INVALID")
    elements = params["dataTypes"].split(",")
    allowed = {"STATION", "NAME", "DATE", "LATITUDE", "LONGITUDE", "ELEVATION", *elements}
    if PRODUCTS[query.dataset].baseline:
        allowed.update(prefix + e for e in elements for prefix in ("meas_flag_", "comp_flag_", "years_"))
    else:
        allowed.update(e + "_ATTRIBUTES" for e in elements)
    counts, periods, seen = {}, {}, set()
    missing_elements = set()
    for row in rows:
        if (not isinstance(row, dict) or set(row) - allowed
                or any(not isinstance(v, str) or len(v) > 256 or any(ord(c) < 32 for c in v) for v in row.values())):
            raise ValueError("RESPONSE_FIELD_DRIFT")
        station = row.get("STATION")
        if station not in query.stations:
            raise ValueError("RESPONSE_STATION_OUTSIDE_QUERY")
        name = row.get("NAME", "")
        if not name.endswith(", KS US"):
            raise ValueError("RESPONSE_KANSAS_IDENTITY_INVALID")
        if not {"LATITUDE", "LONGITUDE", "ELEVATION"}.issubset(row):
            raise ValueError("RESPONSE_LOCATION_MISSING")
        if not (Decimal("36.9") <= _number(row["LATITUDE"]) <= Decimal("40.1")
                and Decimal("-102.2") <= _number(row["LONGITUDE"]) <= Decimal("-94.4")):
            raise ValueError("RESPONSE_LOCATION_OUTSIDE_KANSAS_ENVELOPE")
        _number(row["ELEVATION"])
        period = _period(row, query)
        if (station, period) in seen:
            raise ValueError("RESPONSE_DUPLICATE_STATION_PERIOD")
        seen.add((station, period))
        counts[station] = counts.get(station, 0) + 1
        periods.setdefault(station, []).append(period)
        for element in elements:
            if element not in row:
                missing_elements.add(element)
                continue
            if row[element].strip():
                _number(row[element])
            if not PRODUCTS[query.dataset].baseline and element + "_ATTRIBUTES" not in row:
                raise ValueError("RESPONSE_ATTRIBUTES_MISSING")
            if PRODUCTS[query.dataset].baseline and any(prefix + element not in row
                    for prefix in ("meas_flag_", "comp_flag_", "years_")):
                raise ValueError("RESPONSE_NORMAL_FLAGS_MISSING")
    return {"row_count": len(rows), "station_counts": counts,
            "periods": {s: sorted(v) for s, v in sorted(periods.items())},
            "missing_station_ids": sorted(set(query.stations) - set(counts)),
            "elements_absent_in_some_rows": sorted(missing_elements),
            "coverage_certified": False, "normalization_performed": False,
            "outcome": "CAPTURED" if rows else "EMPTY"}


def fetch(query: Query, *, opener=None, monotonic=time.monotonic, clock=utc_now):
    """One request, no retries/redirects; bounded bytes, socket time and wall time."""
    url = query.url()
    if os.environ.get("KFM_NO_NETWORK") == "1":
        raise ValueError("NETWORK_DISABLED")
    request = Request(url, headers={"Accept": "application/json", "Accept-Encoding": "identity",
                                   "User-Agent": "KFM bounded NCEI Access capture"})
    transport = opener or build_opener(NoRedirect)
    started = monotonic()
    try:
        with transport.open(request, timeout=15) as response:
            if response.status != 200 or response.geturl() != url:
                raise ValueError("RESPONSE_STATUS_OR_URL_INVALID")
            if response.headers.get("Content-Type", "").split(";", 1)[0].strip().lower() != "application/json":
                raise ValueError("RESPONSE_MEDIA_TYPE_INVALID")
            if response.headers.get("Content-Encoding", "identity").lower() != "identity":
                raise ValueError("RESPONSE_ENCODING_NOT_ALLOWED")
            declared = response.headers.get("Content-Length")
            if declared is not None and (not declared.isascii() or not declared.isdigit() or int(declared) > query.max_bytes):
                raise ValueError("RESPONSE_BYTE_LIMIT")
            chunks, count = [], 0
            # read1 performs at most one underlying read, allowing wall-time checks
            # between chunks rather than filling a large read under a trickling peer.
            reader = response.read1
            while True:
                if monotonic() - started >= 60:
                    raise ValueError("RESPONSE_DEADLINE")
                chunk = reader(min(65536, query.max_bytes - count + 1))
                if monotonic() - started >= 60:
                    raise ValueError("RESPONSE_DEADLINE")
                if not chunk:
                    break
                count += len(chunk)
                if count > query.max_bytes:
                    raise ValueError("RESPONSE_BYTE_LIMIT")
                chunks.append(chunk)
            if not count or declared is not None and count != int(declared):
                raise ValueError("RESPONSE_SIZE_MISMATCH")
            return b"".join(chunks), {"url": url, "retrieved_at": clock(), "status": 200,
                    "content_type": response.headers.get("Content-Type"),
                    "etag": response.headers.get("ETag"), "last_modified": response.headers.get("Last-Modified")}
    except HTTPError as exc:
        status = exc.code
        exc.close()
        reason = {400: "REQUEST_REJECTED", 404: "PRODUCT_NOT_FOUND", 429: "PROVIDER_RATE_LIMITED"}.get(status, "PROVIDER_HTTP_ERROR")
        raise ValueError(reason) from None
    except (URLError, OSError):
        raise ValueError("PROVIDER_UNAVAILABLE") from None


@dataclass(frozen=True)
class Capture:
    manifest: dict
    raw: bytes


def capture(query: Query, *, fetcher=fetch) -> Capture:
    plan = query.plan()
    raw, meta = fetcher(query)
    if (not isinstance(meta, dict) or meta.get("url") != plan["url"] or meta.get("status") != 200
            or not isinstance(meta.get("content_type"), str)
            or meta["content_type"].split(";", 1)[0].strip().lower() != "application/json"):
        raise ValueError("CAPTURE_RESPONSE_METADATA_INVALID")
    utc_time(meta.get("retrieved_at"))
    summary = inspect_response(raw, query)
    manifest = {**plan, "network": True, "retrieved_at": meta["retrieved_at"],
                "response": {"sha256": digest_bytes(raw), "bytes": len(raw), "status": 200,
                             "content_type": meta["content_type"], "etag": meta.get("etag"),
                             "last_modified": meta.get("last_modified"), "provider_checksum": None},
                "inspection": summary, "review_state": "pending", "release_state": "UNRELEASED"}
    manifest["capture_id"] = digest_bytes(canonical_bytes(manifest))
    return Capture(manifest, raw)


def verify_capture(acquired: Capture) -> dict:
    """Rebuild the complete manifest from its exact bytes before storage/replay."""
    manifest = acquired.manifest
    if not isinstance(manifest, dict):
        raise ValueError("CAPTURE_MANIFEST_INVALID")
    try:
        params = manifest["parameters"]
        query = Query(params["dataset"], tuple(params["stations"].split(",")),
                      params.get("startDate"), params.get("endDate"), tuple(params["dataTypes"].split(",")),
                      params["units"], manifest["max_bytes"])
        response = manifest["response"]
        rebuilt = capture(query, fetcher=lambda _q: (acquired.raw, {
            "url": manifest["url"], "retrieved_at": manifest["retrieved_at"], "status": response["status"],
            "content_type": response["content_type"], "etag": response["etag"], "last_modified": response["last_modified"]}))
    except (KeyError, TypeError, AttributeError):
        raise ValueError("CAPTURE_MANIFEST_INVALID") from None
    if canonical_bytes(rebuilt.manifest) != canonical_bytes(manifest):
        raise ValueError("CAPTURE_IDENTITY_MISMATCH")
    return rebuilt.manifest["inspection"]
