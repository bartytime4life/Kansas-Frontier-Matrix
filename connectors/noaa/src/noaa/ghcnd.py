"""NOAA GHCN Daily station capture primitives; no admission or publication."""
from __future__ import annotations

import calendar
from collections import Counter
from datetime import datetime, timezone
import gzip
import io
import math
import re
import time
from urllib.request import HTTPRedirectHandler, Request, build_opener

BASE = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/"
MIB = 1024 * 1024
METADATA = {"ghcnd-stations.txt": 16*MIB, "ghcnd-inventory.txt": 48*MIB,
            "by_station/": 32*MIB, "readme.txt": MIB,
            "readme-by_station.txt": MIB, "ghcnd-version.txt": MIB,
            "ghcnd-states.txt": MIB, "ghcnd-countries.txt": MIB}
STATION = re.compile(r"[A-Z0-9]{11}\Z")
STATION_BYTES = 8*MIB
EXPANDED_BYTES = 128*MIB


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def object_url(key):
    if key not in METADATA and not re.fullmatch(r"by_station/[A-Z0-9]{11}\.csv\.gz", key):
        raise ValueError("SOURCE_KEY_NOT_ALLOWED")
    return BASE + key


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def fetch(key, limit):
    url = object_url(key)
    if not 0 < limit <= METADATA.get(key, STATION_BYTES):
        raise ValueError("SOURCE_LIMIT_INVALID")
    start = time.monotonic()
    with build_opener(NoRedirect).open(Request(url, headers={
            "Accept-Encoding": "identity", "User-Agent": "KFM bounded Kansas station capture"}), timeout=30) as response:
        if response.status != 200 or response.geturl() != url:
            raise ValueError("SOURCE_RESPONSE_INVALID")
        declared = response.headers.get("Content-Length")
        if declared is not None and (not declared.isdigit() or int(declared) > limit):
            raise ValueError("SOURCE_SIZE_LIMIT")
        chunks, count = [], 0
        while True:
            if time.monotonic() - start > 90:
                raise ValueError("SOURCE_DEADLINE")
            chunk = response.read(min(65536, limit-count+1))
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
                                   "etag": response.headers.get("ETag"),
                                   "provider_checksum": None}


def kansas_stations(raw):
    selected = {}
    for line in raw.decode("utf-8").splitlines():
        if line[38:40] != "KS":
            continue
        sid = line[:11]
        lat, lon, elevation = float(line[12:20]), float(line[21:30]), float(line[31:37])
        if (not STATION.fullmatch(sid) or sid in selected or not all(map(math.isfinite, [lat, lon, elevation]))
                or not (36.9 <= lat <= 40.1 and -102.2 <= lon <= -94.4)):
            raise ValueError("KANSAS_STATION_INVALID")
        selected[sid] = {"station_id": sid, "latitude": lat, "longitude": lon,
                         "elevation_m": None if elevation == -999.9 else elevation,
                         "state": "KS", "name": line[41:71].strip(),
                         "network_flag": line[76:79].strip()}
    if not selected or len(selected) > 5000:
        raise ValueError("KANSAS_STATION_COUNT")
    return selected


def listed_sizes(raw):
    # Parse only exact station CSV links and their adjacent integer byte counts.
    pattern = (r'href="([A-Z0-9]{11})\.csv\.gz"[^<]*</a></td>\s*'
               r'<td align="right">[^<]*</td>\s*<td align="right">\s*(\d+)\s*</td>')
    pairs = re.findall(pattern, raw.decode("utf-8"))
    result = {sid: int(size) for sid, size in pairs}
    if not result or len(result) != len(pairs):
        raise ValueError("STATION_DIRECTORY_INVALID")
    return result


def inventory_ranges(raw, station_ids):
    result = {sid: {} for sid in station_ids}
    for line in raw.decode("ascii").splitlines():
        sid = line[:11]
        if sid in result:
            element, first, last = line[31:35], int(line[36:40]), int(line[41:45])
            if not re.fullmatch(r"[A-Z0-9]{4}", element) or not 1700 <= first <= last <= 2200:
                raise ValueError("INVENTORY_RANGE_INVALID")
            result[sid][element] = {"first_year": first, "last_year": last}
    return result


def inspect_station(raw, station_id, expanded_limit=EXPANDED_BYTES):
    """Verify gzip CRC and each row; summarize without expanding anything to disk.

    Values and M/Q/S flags remain untouched in the compressed source. Counts
    are inspection metadata, not normalized or released climate observations.
    """
    if not STATION.fullmatch(station_id) or not 0 < len(raw) <= STATION_BYTES:
        raise ValueError("STATION_INPUT_INVALID")
    rows = expanded = 0
    first, last = "99999999", "00000000"
    elements, quality, sources, measurements = Counter(), Counter(), Counter(), Counter()
    missing = 0
    month_lengths = {}
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as stream:
        while True:
            line = stream.readline(513)
            if not line:
                break
            expanded += len(line)
            if expanded > expanded_limit or len(line) > 512:
                raise ValueError("STATION_EXPANSION_LIMIT")
            fields = line.decode("ascii").rstrip("\r\n").split(",")
            if len(fields) != 8 or fields[0] != station_id:
                raise ValueError("STATION_ROW_ID_OR_SHAPE")
            _, day, element, value, mf, qf, sf, obs = fields
            if (not re.fullmatch(r"\d{8}", day) or not re.fullmatch(r"[A-Z0-9]{4}", element)
                    or not re.fullmatch(r"-?\d{1,6}", value) or any(len(f) > 1 for f in (mf, qf, sf))
                    or (obs and not re.fullmatch(r"\d{4}", obs))):
                raise ValueError("STATION_ROW_FORMAT")
            ym = day[:6]
            if ym not in month_lengths:
                year, month = int(day[:4]), int(day[4:6])
                if not 1700 <= year <= 2200 or not 1 <= month <= 12:
                    raise ValueError("STATION_DATE_INVALID")
                month_lengths[ym] = calendar.monthrange(year, month)[1]
            if not 1 <= int(day[6:]) <= month_lengths[ym]:
                raise ValueError("STATION_DATE_INVALID")
            rows += 1
            first, last = min(first, day), max(last, day)
            elements[element] += 1
            quality[qf or "blank"] += 1
            sources[sf or "blank"] += 1
            measurements[mf or "blank"] += 1
            missing += int(value == "-9999")
    if not rows:
        raise ValueError("STATION_EMPTY")
    return {"rows": rows, "expanded_bytes_checked": expanded, "first_date": first, "last_date": last,
            "elements": dict(elements), "quality_flags": dict(quality),
            "source_flags": dict(sources), "measurement_flags": dict(measurements),
            "missing_values": missing, "gzip_crc_checked": True}
