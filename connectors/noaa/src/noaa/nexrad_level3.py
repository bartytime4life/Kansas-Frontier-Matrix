"""NOAA NEXRAD Level III storm-product capture primitives; no admission or publication.

NCEI's NEXRAD product page points public users to the NOAA Open Data
Dissemination copies of the archive. This module reads only the Unidata Level III
bucket and only two small text-bearing products for Kansas-area WSR-88D sites:

* ``NST`` storm tracking information (product 58): storm-cell positions, past
  positions and 15-60 minute forecast positions.
* ``NMD`` mesocyclone detection (product 141): rotation detections, strength
  rank and the algorithm's tornado-vortex-signature flag.

Each product is usually 0.1-15 KB, so a whole Kansas storm day fits in a few
megabytes. Radar reflectivity volumes are deliberately not captured here.
Detections are algorithm output, not confirmed tornadoes, hail or damage.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
import math
import re
import struct
import time
from urllib.parse import quote, urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener

BUCKET = "https://unidata-nexrad-level3.s3.amazonaws.com/"
SOURCE_PAGE = "https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar"
KIB, MIB = 1024, 1024 * 1024
PRODUCT_BYTES = 256 * KIB
LIST_BYTES = 2 * MIB
MAX_KEYS_PER_DAY = 1000

# Locations as reported in each site's own product description block
# (latitude/longitude in 1/1000 degree, height in feet MSL incl. tower).
RADARS = {
    "ICT": {"site": "KICT", "name": "Wichita", "state": "KS", "lat": 37.654, "lon": -97.443, "height_ft": 1400},
    "DDC": {"site": "KDDC", "name": "Dodge City", "state": "KS", "lat": 37.761, "lon": -99.969, "height_ft": 2671},
    "GLD": {"site": "KGLD", "name": "Goodland", "state": "KS", "lat": 39.367, "lon": -101.700, "height_ft": 3717},
    "TWX": {"site": "KTWX", "name": "Topeka", "state": "KS", "lat": 38.997, "lon": -96.232, "height_ft": 1415},
    "EAX": {"site": "KEAX", "name": "Kansas City / Pleasant Hill", "state": "MO", "lat": 38.810, "lon": -94.264, "height_ft": 1092},
    "UEX": {"site": "KUEX", "name": "Hastings", "state": "NE", "lat": 40.321, "lon": -98.442, "height_ft": 2057},
    "VNX": {"site": "KVNX", "name": "Vance AFB", "state": "OK", "lat": 36.741, "lon": -98.128, "height_ft": 1258},
    "INX": {"site": "KINX", "name": "Tulsa", "state": "OK", "lat": 36.175, "lon": -95.564, "height_ft": 749},
}
KANSAS_RADARS = ("ICT", "DDC", "GLD", "TWX")
PRODUCTS = {"NST": 58, "NMD": 141}
KEY = re.compile(r"(?P<radar>[A-Z]{3})_(?P<product>[A-Z0-9]{3})_(?P<stamp>\d{4}_\d{2}_\d{2}_\d{2}_\d{2}_\d{2})\Z")
NM_KM = 1.852
EARTH_KM = 6371.0088


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def check_day(day):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", day or ""):
        raise ValueError("DAY_INVALID")
    parsed = datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    if parsed.strftime("%Y-%m-%d") != day or not datetime(1991, 1, 1, tzinfo=timezone.utc) <= parsed <= datetime.now(timezone.utc):
        raise ValueError("DAY_INVALID")
    return day


def key_time(key):
    """Return the UTC volume time encoded in an exact allowed object key."""
    match = KEY.fullmatch(key or "")
    if not match or match["radar"] not in RADARS or match["product"] not in PRODUCTS:
        raise ValueError("SOURCE_KEY_NOT_ALLOWED")
    try:
        return datetime.strptime(match["stamp"], "%Y_%m_%d_%H_%M_%S").replace(tzinfo=timezone.utc)
    except ValueError as error:
        raise ValueError("SOURCE_KEY_NOT_ALLOWED") from error


def object_url(key):
    key_time(key)
    return BUCKET + key


def list_url(radar, product, day, token=None):
    if radar not in RADARS or product not in PRODUCTS:
        raise ValueError("SOURCE_KEY_NOT_ALLOWED")
    query = {"list-type": "2", "prefix": f"{radar}_{product}_{check_day(day).replace('-', '_')}_", "max-keys": str(MAX_KEYS_PER_DAY)}
    if token is not None:
        if not re.fullmatch(r"[A-Za-z0-9+/=_-]{1,1024}", token):
            raise ValueError("LIST_TOKEN_INVALID")
        query["continuation-token"] = token
    return BUCKET + "?" + urlencode(query, quote_via=quote)


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def get(url, limit, deadline=60):
    """Bounded, redirect-free GET of one exact public-bucket URL."""
    if not url.startswith(BUCKET) or not 0 < limit <= LIST_BYTES:
        raise ValueError("SOURCE_LIMIT_INVALID")
    start = time.monotonic()
    request = Request(url, headers={"Accept-Encoding": "identity", "User-Agent": "KFM bounded Kansas NEXRAD Level III capture"})
    with build_opener(NoRedirect).open(request, timeout=30) as response:
        if response.status != 200 or response.geturl() != url:
            raise ValueError("SOURCE_RESPONSE_INVALID")
        declared = response.headers.get("Content-Length")
        if declared is not None and (not declared.isdigit() or int(declared) > limit):
            raise ValueError("SOURCE_SIZE_LIMIT")
        chunks, count = [], 0
        while True:
            if time.monotonic() - start > deadline:
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
                                   "etag": response.headers.get("ETag"), "provider_checksum": None}


def fetch(key, limit=PRODUCT_BYTES):
    if not 0 < limit <= PRODUCT_BYTES:
        raise ValueError("SOURCE_LIMIT_INVALID")
    return get(object_url(key), limit)


def parse_listing(raw, radar, product, day):
    """Parse one S3 ListObjectsV2 page; every key must be an exact same-day product."""
    text = raw.decode("utf-8")
    if "<!DOCTYPE" in text or "<!ENTITY" in text or "<ListBucketResult" not in text:
        raise ValueError("LISTING_INVALID")
    rows = []
    for block in re.findall(r"<Contents>(.*?)</Contents>", text, re.S):
        key = re.search(r"<Key>([^<]{1,64})</Key>", block)
        size = re.search(r"<Size>(\d{1,9})</Size>", block)
        if not key or not size:
            raise ValueError("LISTING_INVALID")
        when = key_time(key[1])
        if not key[1].startswith(f"{radar}_{product}_") or when.strftime("%Y-%m-%d") != day:
            raise ValueError("LISTING_KEY_SCOPE")
        if not 0 < int(size[1]) <= PRODUCT_BYTES:
            raise ValueError("LISTING_SIZE_LIMIT")
        rows.append({"key": key[1], "bytes": int(size[1]), "volume_time": when.isoformat().replace("+00:00", "Z")})
    truncated = re.search(r"<IsTruncated>(true|false)</IsTruncated>", text)
    token = re.search(r"<NextContinuationToken>([^<]{1,1024})</NextContinuationToken>", text)
    if not truncated or (truncated[1] == "true") != bool(token):
        raise ValueError("LISTING_INVALID")
    return rows, token[1] if token else None


def list_day(radar, product, day, getter=get):
    rows, token = [], None
    for _ in range(4):
        raw, _header = getter(list_url(radar, product, day, token), LIST_BYTES)
        page, token = parse_listing(raw, radar, product, day)
        rows.extend(page)
        if token is None:
            break
    else:
        raise ValueError("LISTING_PAGE_LIMIT")
    if len(rows) > MAX_KEYS_PER_DAY or len({row["key"] for row in rows}) != len(rows):
        raise ValueError("LISTING_INVALID")
    return sorted(rows, key=lambda row: row["key"])


def _nexrad_time(days, seconds):
    if not 1 <= days <= 40000 or not 0 <= seconds < 86400:
        raise ValueError("PRODUCT_TIME_INVALID")
    return datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(days=days - 1, seconds=seconds)


def destination(lat, lon, azimuth_deg, distance_km):
    """Great-circle point at a bearing/distance; adequate within radar range."""
    phi, lam, theta = map(math.radians, (lat, lon, azimuth_deg))
    delta = distance_km / EARTH_KM
    phi2 = math.asin(math.sin(phi) * math.cos(delta) + math.cos(phi) * math.sin(delta) * math.cos(theta))
    lam2 = lam + math.atan2(math.sin(theta) * math.sin(delta) * math.cos(phi), math.cos(delta) - math.sin(phi) * math.sin(phi2))
    return round(math.degrees(lam2), 4), round(math.degrees(phi2), 4)


def _ij_point(site, i, j):
    """Convert symbology I/J (1/4 km east/north of the radar) to lon/lat."""
    east, north = i / 4, j / 4
    return destination(site["lat"], site["lon"], math.degrees(math.atan2(east, north)) % 360, math.hypot(east, north))


def _tabular_pages(message, offset):
    start = offset * 2
    if start <= 0 or start + 132 > len(message):
        raise ValueError("TABULAR_BLOCK_INVALID")
    divider, block_id, length = struct.unpack(">hhi", message[start:start + 8])
    if divider != -1 or block_id != 3 or not 132 <= length <= len(message) - start:
        raise ValueError("TABULAR_BLOCK_INVALID")
    position = start + 8 + 120
    divider, count = struct.unpack(">hh", message[position:position + 4])
    if divider != -1 or not 0 <= count <= 64:
        raise ValueError("TABULAR_BLOCK_INVALID")
    position += 4
    pages = []
    for _ in range(count):
        lines = []
        while True:
            if position + 2 > start + length:
                raise ValueError("TABULAR_BLOCK_INVALID")
            (size,) = struct.unpack(">h", message[position:position + 2])
            position += 2
            if size == -1:
                break
            if not 0 <= size <= 80 or position + size > start + length:
                raise ValueError("TABULAR_BLOCK_INVALID")
            lines.append(message[position:position + size].decode("ascii"))
            position += size
        pages.append(lines)
    return pages


def _packets(data, position, end, depth=0):
    """Yield (code, payload) from NST/NMD symbology packets with 2-byte lengths."""
    while position < end:
        if position + 4 > end:
            raise ValueError("SYMBOLOGY_INVALID")
        code, length = struct.unpack(">hh", data[position:position + 4])
        if code not in (1, 2, 3, 4, 6, 8, 11, 12, 15, 19, 20, 23, 24, 25, 26) or not 0 <= length <= end - position - 4:
            raise ValueError("SYMBOLOGY_INVALID")
        payload = data[position + 4:position + 4 + length]
        if code in (23, 24):
            if depth:
                raise ValueError("SYMBOLOGY_INVALID")
            yield code, list(_packets(payload, 0, length, depth + 1))
        else:
            yield code, payload
        position += 4 + length


def _storm_geometry(message, offset, site):
    start = offset * 2
    if start <= 0 or start + 10 > len(message):
        raise ValueError("SYMBOLOGY_INVALID")
    divider, block_id, length, layers = struct.unpack(">hhih", message[start:start + 10])
    if divider != -1 or block_id != 1 or not 10 <= length <= len(message) - start or not 0 <= layers <= 18:
        raise ValueError("SYMBOLOGY_INVALID")
    storms, position, current = {}, start + 10, None
    for _ in range(layers):
        divider, layer_length = struct.unpack(">hi", message[position:position + 6])
        if divider != -1 or not 0 <= layer_length <= start + length - position - 6:
            raise ValueError("SYMBOLOGY_INVALID")
        for code, payload in _packets(message, position + 6, position + 6 + layer_length):
            if code == 15:
                if len(payload) != 6:
                    raise ValueError("SYMBOLOGY_INVALID")
                i, j = struct.unpack(">hh", payload[:4])
                storm_id = payload[4:6].decode("ascii")
                if not re.fullmatch(r"[A-Z][0-9]", storm_id):
                    raise ValueError("STORM_ID_INVALID")
                current = storms.setdefault(storm_id, {"current": _ij_point(site, i, j), "past": [], "forecast": []})
            elif code in (23, 24) and current is not None:
                points = [_ij_point(site, *struct.unpack(">hh", inner[:4])) for inner_code, inner in payload if inner_code == 2 and len(inner) >= 4]
                current["past" if code == 23 else "forecast"].extend(points)
        position += 6 + layer_length
    return storms


def _compass(degrees):
    return ("N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW")[round(degrees / 22.5) % 16]


def _motion(direction_from, knots):
    toward = (direction_from + 180) % 360
    return {"toward_deg": toward, "toward": _compass(toward), "speed_kt": knots, "speed_mph": round(knots * 1.15078)}


STORM_ROW = re.compile(r"\s+(?P<id>[A-Z][0-9])\s+(?P<az>\d{1,3})/\s*(?P<rng>\d{1,3})\s+(?:(?P<dir>\d{1,3})/\s*(?P<spd>\d{1,3})|NEW)\s+.*?(?P<err>\d+\.\d)/\s*(?P<mean>\d+\.\d)\s*")
MESO_ROW = re.compile(
    r"\s*(?P<circ>\d{1,4})\s+(?P<az>\d{1,3})/\s*(?P<rng>\d{1,3})\s+(?P<rank>\d{1,2})(?P<low>L?)\s+(?:(?P<storm>[A-Z][0-9])\s+)?"
    r"(?P<llrv>\d{1,3})\s+(?P<lldv>\d{1,3})\s+(?P<base>[<>]?\s*\d{1,2})\s+(?P<depth>[<>]?\s*\d{1,2})\s+(?P<rel>\d{1,3})\s+"
    r"(?P<maxh>\d{1,2})\s+(?P<maxrv>\d{1,3})\s+(?P<tvs>[YN])\s+(?:(?P<dir>\d{1,3})/\s*(?P<spd>\d{1,3})\s+)?(?P<msi>\d{1,6})\s*")


def rotation_class(rank, low_level, tvs):
    if tvs:
        return "tornado_signature"
    if rank >= 5:
        return "strong_low" if low_level else "strong_aloft"
    return "weak"


ROTATION_LABELS = {
    "tornado_signature": "Tornado vortex signature (algorithm flag, not a confirmed tornado)",
    "strong_low": "Strong rotation reaching low levels",
    "strong_aloft": "Strong rotation aloft",
    "weak": "Weak rotation",
}


def parse_product(raw, key):
    """Parse one exact NST or NMD file into storm-cell or rotation detections.

    The WMO/AWIPS envelope, product code, radar identity, message length and the
    volume time encoded in the key must agree; otherwise the file is rejected.
    """
    when = key_time(key)
    match = KEY.fullmatch(key)
    radar, product = match["radar"], match["product"]
    site = RADARS[radar]
    if not 0 < len(raw) <= PRODUCT_BYTES:
        raise ValueError("PRODUCT_SIZE_LIMIT")
    header = re.match(rb"SDUS[0-9]{2} K[A-Z]{3} \d{6}\r\r\n([A-Z0-9]{6})\r\r\n", raw)
    if not header or header[1].decode("ascii") != product + radar:
        raise ValueError("PRODUCT_ENVELOPE_INVALID")
    message = raw[header.end():]
    if len(message) < 120:
        raise ValueError("PRODUCT_ENVELOPE_INVALID")
    code, _date, _time, length, _source, _destination, blocks = struct.unpack(">hhiihhh", message[:18])
    fields = struct.unpack(">hiihhhhhhhihi", message[18:52])
    divider, lat, lon, height, product_code = fields[:5]
    volume_date, volume_seconds = fields[9], fields[10]
    offsets = struct.unpack(">iii", message[108:120])
    if code != PRODUCTS[product] or product_code != code or length != len(message) or divider != -1 or not 2 <= blocks <= 5:
        raise ValueError("PRODUCT_HEADER_INVALID")
    if abs(lat / 1000 - site["lat"]) > 0.01 or abs(lon / 1000 - site["lon"]) > 0.01 or abs(height - site["height_ft"]) > 50:
        raise ValueError("PRODUCT_RADAR_MISMATCH")
    volume = _nexrad_time(volume_date, volume_seconds)
    if volume != when:
        raise ValueError("PRODUCT_TIME_MISMATCH")
    stamp = volume.isoformat().replace("+00:00", "Z")
    common = {"radar": site["site"], "radar_name": site["name"], "product": product, "volume_time": stamp, "source_key": key}
    lines = [line for page in (_tabular_pages(message, offsets[2]) if offsets[2] else []) for line in page]
    detections = []
    if product == "NST":
        # The graphic symbology carries every identified cell; the text table can
        # stop early on busy volumes. Merge both and record any truncation.
        geometry = _storm_geometry(message, offsets[0], site) if offsets[0] else {}
        rows = {}
        for line in lines:
            row = STORM_ROW.fullmatch(line)
            if row and row["id"] not in rows:
                rows[row["id"]] = row
        declared = re.search(r"NUMBER OF STORM CELLS\s+(\d+)", "\n".join(lines))
        identifiers = sorted(set(geometry) | set(rows))
        if declared and len(identifiers) != int(declared[1]):
            raise ValueError("STORM_TABLE_INCOMPLETE")
        for storm_id in identifiers:
            row, shape = rows.get(storm_id), geometry.get(storm_id)
            if row:
                fallback = destination(site["lat"], site["lon"], int(row["az"]), int(row["rng"]) * NM_KM)
            detections.append({**common, "kind": "storm_cell", "storm_id": storm_id,
                               "position": shape["current"] if shape else fallback,
                               "past": shape["past"] if shape else [], "forecast": shape["forecast"] if shape else [],
                               "azimuth_deg": int(row["az"]) if row else None, "range_nm": int(row["rng"]) if row else None,
                               "motion": _motion(int(row["dir"]), int(row["spd"])) if row and row["dir"] else None,
                               "new_cell": bool(row) and row["dir"] is None,
                               "forecast_error_nm": float(row["err"]) if row else None, "in_text_table": bool(row)})
    else:
        for line in lines:
            row = MESO_ROW.fullmatch(line)
            if not row:
                continue
            rank, low, tvs = int(row["rank"]), bool(row["low"]), row["tvs"] == "Y"
            kind = rotation_class(rank, low, tvs)
            detections.append({**common, "kind": "rotation", "circulation_id": int(row["circ"]), "storm_id": row["storm"],
                               "position": destination(site["lat"], site["lon"], int(row["az"]), int(row["rng"]) * NM_KM),
                               "azimuth_deg": int(row["az"]), "range_nm": int(row["rng"]), "strength_rank": rank,
                               "low_level": low, "tvs": tvs, "rotation_class": kind, "label": ROTATION_LABELS[kind],
                               "base_kft": row["base"].replace(" ", ""), "depth_kft": row["depth"].replace(" ", ""),
                               "motion": _motion(int(row["dir"]), int(row["spd"])) if row["dir"] else None})
        if len(detections) != sum(bool(re.match(r"\s*\d{1,4}\s+\d{1,3}/", line)) for line in lines):
            raise ValueError("ROTATION_TABLE_INCOMPLETE")
    return {"radar": site["site"], "product": product, "product_code": code, "volume_time": stamp,
            "radar_lat": lat / 1000, "radar_lon": lon / 1000, "radar_height_ft": height,
            "detections": detections}


def _round(point):
    return [round(point[0], 3), round(point[1], 3)]


def feature_collection(parsed_products, name):
    """Build one compact display GeoJSON index; review state is collection-wide.

    Coordinates are rounded to 0.001 degree (about 100 m), well inside radar
    position uncertainty. Track lines carry only the keys needed to join them
    to their storm-cell point.
    """
    features = []
    skip = {"position", "past", "forecast", "radar_name", "label", "product"}
    for product in parsed_products:
        for item in product["detections"]:
            props = {key: value for key, value in item.items() if key not in skip and value is not None}
            link = {"radar": item["radar"], "volume_time": item["volume_time"], "storm_id": item.get("storm_id")}
            features.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": _round(item["position"])},
                             "properties": props})
            for part in ("past", "forecast"):
                if item["kind"] == "storm_cell" and item[part]:
                    features.append({"type": "Feature",
                                     "geometry": {"type": "LineString", "coordinates": [_round(item["position"]), *map(_round, item[part])]},
                                     "properties": {**link, "kind": f"storm_{part}_track"}})
    return {"type": "FeatureCollection", "name": name, "source_page": SOURCE_PAGE, "source_bucket": BUCKET,
            "evidence_role": "EXTERNAL_CONTEXT_ONLY", "review_status": "unreviewed", "source_admitted": False, "released": False,
            "radars": {value["site"]: {"name": value["name"], "lat": value["lat"], "lon": value["lon"]} for value in RADARS.values()},
            "rotation_labels": ROTATION_LABELS,
            "limitation": "NEXRAD storm-cell and mesocyclone algorithm detections. They are not confirmed tornadoes, hail, damage or warnings.",
            "features": features}
