"""NOAA USCRN daily01 capture primitives for the Kansas soil pilot; no admission or publication.

Columns are read only through ``PROFILE``, the published daily01 (CRND0103)
layout. The capture also fetches NOAA's ``headers.txt`` and refuses the
capture unless it names exactly these fields in this order, so a layout change
upstream fails closed instead of mislabeling values. Every data row must carry
the expected WBAN number. Source tokens are kept verbatim beside parsed values;
the missing sentinels (-99.000 for soil moisture, -9999.0 otherwise) never
become zero.
"""
from __future__ import annotations

from datetime import datetime, timezone
import re
import time
from urllib.request import HTTPRedirectHandler, Request, build_opener

BASE = "https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/"
HEADERS_KEY = "headers.txt"
MIB = 1024 * 1024
HEADERS_BYTES = 64 * 1024
STATION_YEAR_BYTES = MIB
# Kansas USCRN stations: WBAN number -> daily01 file station name.
STATIONS = {"53974": "KS_Manhattan_6_SSW", "03067": "KS_Oakley_19_SSW"}
DEPTHS_CM = (5, 10, 20, 50, 100)
# Published daily01 field order (28 whitespace-separated fields).
PROFILE = (
    "WBANNO", "LST_DATE", "CRX_VN", "LONGITUDE", "LATITUDE",
    "T_DAILY_MAX", "T_DAILY_MIN", "T_DAILY_MEAN", "T_DAILY_AVG", "P_DAILY_CALC", "SOLARAD_DAILY",
    "SUR_TEMP_DAILY_TYPE", "SUR_TEMP_DAILY_MAX", "SUR_TEMP_DAILY_MIN", "SUR_TEMP_DAILY_AVG",
    "RH_DAILY_MAX", "RH_DAILY_MIN", "RH_DAILY_AVG",
    *(f"SOIL_MOISTURE_{d}_DAILY" for d in DEPTHS_CM),
    *(f"SOIL_TEMP_{d}_DAILY" for d in DEPTHS_CM),
)
INDEX = {name: position for position, name in enumerate(PROFILE)}
MOISTURE_MISSING = "-99.000"
NUMBER_MISSING = "-9999.0"
MOISTURE_TOKEN = re.compile(r"-?\d{1,2}\.\d{3}\Z")
TEMP_TOKEN = re.compile(r"-?\d{1,4}\.\d\Z")
COORDINATE_TOKEN = re.compile(r"-?\d{1,3}\.\d{2,4}\Z")
YEAR_KEY = re.compile(r"(\d{4})/CRND0103-(\d{4})-(KS_[A-Za-z0-9_]+)\.txt\Z")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def station_year_key(year: int, wban: str) -> str:
    if wban not in STATIONS or not 2000 <= year <= 2200:
        raise ValueError("SOURCE_KEY_NOT_ALLOWED")
    return f"{year}/CRND0103-{year}-{STATIONS[wban]}.txt"


def object_url(key: str) -> str:
    match = YEAR_KEY.fullmatch(key) if key != HEADERS_KEY else None
    if key != HEADERS_KEY and not (match and match[1] == match[2] and match[3] in STATIONS.values()):
        raise ValueError("SOURCE_KEY_NOT_ALLOWED")
    return BASE + key


def object_limit(key: str) -> int:
    return HEADERS_BYTES if key == HEADERS_KEY else STATION_YEAR_BYTES


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def fetch(key: str, limit: int):
    """One bounded, host-locked GET with no redirects; returns (bytes, metadata)."""
    url = object_url(key)
    if not 0 < limit <= object_limit(key):
        raise ValueError("SOURCE_LIMIT_INVALID")
    start = time.monotonic()
    with build_opener(NoRedirect).open(Request(url, headers={
            "Accept-Encoding": "identity", "User-Agent": "KFM bounded Kansas soil station capture"}), timeout=30) as response:
        if response.status != 200 or response.geturl() != url:
            raise ValueError("SOURCE_RESPONSE_INVALID")
        declared = response.headers.get("Content-Length")
        if declared is not None and (not declared.isdigit() or int(declared) > limit):
            raise ValueError("SOURCE_SIZE_LIMIT")
        chunks, count = [], 0
        while True:
            if time.monotonic() - start > 90:
                raise ValueError("SOURCE_DEADLINE")
            chunk = response.read(min(65536, limit - count + 1))
            if not chunk:
                break
            count += len(chunk)
            if count > limit:
                raise ValueError("SOURCE_SIZE_LIMIT")
            chunks.append(chunk)
        if count == 0 or (declared is not None and count != int(declared)):
            raise ValueError("SOURCE_SIZE_MISMATCH")
        return b"".join(chunks), {"source_url": url, "retrieved_at": utc_now(),
                                   "last_modified": response.headers.get("Last-Modified"),
                                   "etag": response.headers.get("ETag")}


def check_headers(raw: bytes) -> None:
    """Refuse unless NOAA's headers.txt lists exactly PROFILE, numbered 1..28."""
    try:
        lines = [line.split() for line in raw.decode("ascii").splitlines() if line.strip()]
    except UnicodeDecodeError:
        raise ValueError("HEADER_PROFILE_MISMATCH") from None
    if len(lines) < 2 or lines[0] != [str(n) for n in range(1, len(PROFILE) + 1)] or tuple(lines[1]) != PROFILE:
        raise ValueError("HEADER_PROFILE_MISMATCH")


def rows(raw: bytes, wban: str):
    """Yield the 28 fields of each data row, checked for shape and station identity."""
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError:
        raise ValueError("STATION_ROW_FORMAT") from None
    for line in text.splitlines():
        if not line.strip():
            continue
        fields = line.split()
        if len(fields) != len(PROFILE) or fields[INDEX["WBANNO"]] != wban:
            raise ValueError("STATION_ROW_ID_OR_SHAPE")
        if (not re.fullmatch(r"\d{8}", fields[INDEX["LST_DATE"]])
                or not all(COORDINATE_TOKEN.fullmatch(fields[INDEX[c]]) for c in ("LONGITUDE", "LATITUDE"))
                or not all(MOISTURE_TOKEN.fullmatch(fields[INDEX[f"SOIL_MOISTURE_{d}_DAILY"]]) for d in DEPTHS_CM)
                or not all(TEMP_TOKEN.fullmatch(fields[INDEX[f"SOIL_TEMP_{d}_DAILY"]]) for d in DEPTHS_CM)):
            raise ValueError("STATION_ROW_FORMAT")
        yield fields
