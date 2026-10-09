"""Offline inverse projections for the coordinate systems common in Kansas data.

Only closed-form ellipsoidal formulas are used; no grid shift, datum
transformation, or network lookup occurs. NAD83 and WGS84 are treated as
coincident (sub-metre to ~2 m difference), which is adequate for extent
screening and never for survey or legal positioning. Unsupported systems
return ``None`` so callers can record an explicit gap instead of guessing.
"""
from __future__ import annotations

import math
import re

GRS80 = (6378137.0, 1 / 298.257222101)
WGS84 = (6378137.0, 1 / 298.257223563)
CLARKE1866 = (6378206.4, 1 / 294.978698214)
US_FOOT = 1200 / 3937

# Kansas envelope (WGS84 degrees) with a small tolerance for boundary geometry.
KANSAS_BBOX = (-102.0517, 36.9930, -94.5884, 40.0031)
_TOLERANCE = 0.05


def _lcc(lat0, lon0, sp1, sp2, fe, fn, unit=1.0, ellipsoid=GRS80):
    return {"kind": "lcc", "lat0": lat0, "lon0": lon0, "sp1": sp1, "sp2": sp2,
            "fe": fe, "fn": fn, "unit": unit, "ellipsoid": ellipsoid}


# Projected systems with a known closed form. Geographic codes are handled separately.
PROJECTED = {
    # NAD83 / Kansas North and South (metres, then US survey feet).
    26977: _lcc(38 + 1 / 3, -98.0, 39 + 47 / 60, 38 + 43 / 60, 400000.0, 0.0),
    26978: _lcc(36 + 2 / 3, -98.5, 38 + 34 / 60, 37 + 16 / 60, 400000.0, 400000.0),
    3419: _lcc(38 + 1 / 3, -98.0, 39 + 47 / 60, 38 + 43 / 60, 400000.0, 0.0, US_FOOT),
    3420: _lcc(36 + 2 / 3, -98.5, 38 + 34 / 60, 37 + 16 / 60, 400000.0, 400000.0, US_FOOT),
    # NAD83(HARN) / NAD83(2011) Kansas variants share the same parameters.
    2796: _lcc(38 + 1 / 3, -98.0, 39 + 47 / 60, 38 + 43 / 60, 400000.0, 0.0),
    2797: _lcc(36 + 2 / 3, -98.5, 38 + 34 / 60, 37 + 16 / 60, 400000.0, 400000.0),
    6466: _lcc(38 + 1 / 3, -98.0, 39 + 47 / 60, 38 + 43 / 60, 400000.0, 0.0),
    6468: _lcc(36 + 2 / 3, -98.5, 38 + 34 / 60, 37 + 16 / 60, 400000.0, 400000.0),
    6467: _lcc(38 + 1 / 3, -98.0, 39 + 47 / 60, 38 + 43 / 60, 400000.0, 0.0, US_FOOT),
    6469: _lcc(36 + 2 / 3, -98.5, 38 + 34 / 60, 37 + 16 / 60, 400000.0, 400000.0, US_FOOT),
    # CONUS Albers Equal Area (NAD83 and its ESRI alias).
    5070: {"kind": "aea", "lat0": 23.0, "lon0": -96.0, "sp1": 29.5, "sp2": 45.5, "fe": 0.0, "fn": 0.0, "ellipsoid": GRS80},
    102039: {"kind": "aea", "lat0": 23.0, "lon0": -96.0, "sp1": 29.5, "sp2": 45.5, "fe": 0.0, "fn": 0.0, "ellipsoid": GRS80},
    3857: {"kind": "merc"},
    900913: {"kind": "merc"},
}
for _zone in (13, 14, 15):
    PROJECTED[26900 + _zone] = {"kind": "utm", "zone": _zone, "ellipsoid": GRS80}
    PROJECTED[32600 + _zone] = {"kind": "utm", "zone": _zone, "ellipsoid": WGS84}
    PROJECTED[26700 + _zone] = {"kind": "utm", "zone": _zone, "ellipsoid": CLARKE1866, "approximate_datum": True}
    PROJECTED[6330 + _zone] = {"kind": "utm", "zone": _zone, "ellipsoid": GRS80}  # NAD83(2011) UTM 13-15N

GEOGRAPHIC = {4326: "WGS 84", 4269: "NAD83", 4267: "NAD27", 4152: "NAD83(HARN)", 6318: "NAD83(2011)", 4258: "ETRS89"}

# WKT name fragments (normalized) for shapefile .prj files without an AUTHORITY clause.
_WKT_NAMES = [
    (r"kansas[_ ]north.*(ft|feet|foot)", 3419), (r"kansas[_ ]south.*(ft|feet|foot)", 3420),
    (r"kansas[_ ]north", 26977), (r"kansas[_ ]south", 26978),
    (r"albers.*(conus|contiguous|usa|us)|(usa|us)[_ ]contiguous[_ ]albers", 5070),
    (r"web[_ ]mercator|pseudo[_ ]mercator|popular[_ ]visualisation", 3857),
]


def _ecc(ellipsoid):
    a, f = ellipsoid
    e2 = f * (2 - f)
    return a, e2, math.sqrt(e2)


def _tsfn(phi, e):
    s = e * math.sin(phi)
    return math.tan(math.pi / 4 - phi / 2) / ((1 - s) / (1 + s)) ** (e / 2)


def _msfn(phi, e2):
    return math.cos(phi) / math.sqrt(1 - e2 * math.sin(phi) ** 2)


def _phi_from_t(t, e):
    phi = math.pi / 2 - 2 * math.atan(t)
    for _ in range(15):
        s = e * math.sin(phi)
        nxt = math.pi / 2 - 2 * math.atan(t * ((1 - s) / (1 + s)) ** (e / 2))
        if abs(nxt - phi) < 1e-12:
            return nxt
        phi = nxt
    return phi


def _lcc_constants(p):
    a, e2, e = _ecc(p["ellipsoid"])
    p1, p2, p0 = (math.radians(p[k]) for k in ("sp1", "sp2", "lat0"))
    m1, m2 = _msfn(p1, e2), _msfn(p2, e2)
    t1, t2, t0 = _tsfn(p1, e), _tsfn(p2, e), _tsfn(p0, e)
    n = (math.log(m1) - math.log(m2)) / (math.log(t1) - math.log(t2))
    big_f = m1 / (n * t1 ** n)
    return a, e, n, big_f, a * big_f * t0 ** n


def lcc_forward(p, lon, lat):
    """Forward Lambert Conformal Conic 2SP (EPSG 9802); used for verification."""
    a, e, n, big_f, rho0 = _lcc_constants(p)
    rho = a * big_f * _tsfn(math.radians(lat), e) ** n
    theta = n * math.radians(lon - p["lon0"])
    return ((p["fe"] + rho * math.sin(theta)) / p["unit"],
            (p["fn"] + rho0 - rho * math.cos(theta)) / p["unit"])


def _lcc_inverse(p, x, y):
    a, e, n, big_f, rho0 = _lcc_constants(p)
    dx = x * p["unit"] - p["fe"]
    dy = rho0 - (y * p["unit"] - p["fn"])
    rho = math.copysign(math.hypot(dx, dy), n)
    theta = math.atan2(dx, dy) if n > 0 else math.atan2(-dx, -dy)
    t = (rho / (a * big_f)) ** (1 / n)
    return p["lon0"] + math.degrees(theta / n), math.degrees(_phi_from_t(t, e))


def _aea_q(phi, e, e2):
    s = math.sin(phi)
    return (1 - e2) * (s / (1 - e2 * s * s) - (1 / (2 * e)) * math.log((1 - e * s) / (1 + e * s)))


def _aea_constants(p):
    a, e2, e = _ecc(p["ellipsoid"])
    p1, p2, p0 = (math.radians(p[k]) for k in ("sp1", "sp2", "lat0"))
    m1, m2 = _msfn(p1, e2), _msfn(p2, e2)
    q1, q2, q0 = (_aea_q(v, e, e2) for v in (p1, p2, p0))
    n = (m1 * m1 - m2 * m2) / (q2 - q1)
    c = m1 * m1 + n * q1
    return a, e, e2, n, c, a * math.sqrt(c - n * q0) / n


def aea_forward(p, lon, lat):
    a, e, e2, n, c, rho0 = _aea_constants(p)
    rho = a * math.sqrt(c - n * _aea_q(math.radians(lat), e, e2)) / n
    theta = n * math.radians(lon - p["lon0"])
    return p["fe"] + rho * math.sin(theta), p["fn"] + rho0 - rho * math.cos(theta)


def _aea_inverse(p, x, y):
    a, e, e2, n, c, rho0 = _aea_constants(p)
    dx, dy = x - p["fe"], rho0 - (y - p["fn"])
    rho = math.hypot(dx, dy)
    theta = math.atan2(dx, dy)
    q = (c - (rho * n / a) ** 2) / n
    phi = math.asin(max(-1.0, min(1.0, q / 2)))
    for _ in range(25):
        s = math.sin(phi)
        delta = ((1 - e2 * s * s) ** 2 / (2 * math.cos(phi))) * (
            q / (1 - e2) - s / (1 - e2 * s * s) + (1 / (2 * e)) * math.log((1 - e * s) / (1 + e * s)))
        phi += delta
        if abs(delta) < 1e-12:
            break
    return p["lon0"] + math.degrees(theta / n), math.degrees(phi)


def utm_forward(p, lon, lat):
    a, e2, _ = _ecc(p["ellipsoid"])
    k0, lon0 = 0.9996, math.radians(-183 + 6 * p["zone"])
    phi, lam = math.radians(lat), math.radians(lon)
    ep2 = e2 / (1 - e2)
    n = a / math.sqrt(1 - e2 * math.sin(phi) ** 2)
    t, c = math.tan(phi) ** 2, ep2 * math.cos(phi) ** 2
    aa = math.cos(phi) * (lam - lon0)
    m = a * ((1 - e2 / 4 - 3 * e2 ** 2 / 64 - 5 * e2 ** 3 / 256) * phi
             - (3 * e2 / 8 + 3 * e2 ** 2 / 32 + 45 * e2 ** 3 / 1024) * math.sin(2 * phi)
             + (15 * e2 ** 2 / 256 + 45 * e2 ** 3 / 1024) * math.sin(4 * phi)
             - (35 * e2 ** 3 / 3072) * math.sin(6 * phi))
    x = k0 * n * (aa + (1 - t + c) * aa ** 3 / 6 + (5 - 18 * t + t * t + 72 * c - 58 * ep2) * aa ** 5 / 120) + 500000
    y = k0 * (m + n * math.tan(phi) * (aa * aa / 2 + (5 - t + 9 * c + 4 * c * c) * aa ** 4 / 24
                                       + (61 - 58 * t + t * t + 600 * c - 330 * ep2) * aa ** 6 / 720))
    return x, y


def _utm_inverse(p, x, y):
    a, e2, _ = _ecc(p["ellipsoid"])
    k0, lon0 = 0.9996, -183 + 6 * p["zone"]
    ep2 = e2 / (1 - e2)
    m = y / k0
    mu = m / (a * (1 - e2 / 4 - 3 * e2 ** 2 / 64 - 5 * e2 ** 3 / 256))
    e1 = (1 - math.sqrt(1 - e2)) / (1 + math.sqrt(1 - e2))
    phi1 = (mu + (3 * e1 / 2 - 27 * e1 ** 3 / 32) * math.sin(2 * mu)
            + (21 * e1 ** 2 / 16 - 55 * e1 ** 4 / 32) * math.sin(4 * mu)
            + (151 * e1 ** 3 / 96) * math.sin(6 * mu) + (1097 * e1 ** 4 / 512) * math.sin(8 * mu))
    n1 = a / math.sqrt(1 - e2 * math.sin(phi1) ** 2)
    t1, c1 = math.tan(phi1) ** 2, ep2 * math.cos(phi1) ** 2
    r1 = a * (1 - e2) / (1 - e2 * math.sin(phi1) ** 2) ** 1.5
    d = (x - 500000) / (n1 * k0)
    lat = phi1 - (n1 * math.tan(phi1) / r1) * (
        d * d / 2 - (5 + 3 * t1 + 10 * c1 - 4 * c1 * c1 - 9 * ep2) * d ** 4 / 24
        + (61 + 90 * t1 + 298 * c1 + 45 * t1 * t1 - 252 * ep2 - 3 * c1 * c1) * d ** 6 / 720)
    lon = (d - (1 + 2 * t1 + c1) * d ** 3 / 6
           + (5 - 2 * c1 + 28 * t1 - 3 * c1 * c1 + 8 * ep2 + 24 * t1 * t1) * d ** 5 / 120) / math.cos(phi1)
    return lon0 + math.degrees(lon), math.degrees(lat)


def _merc_inverse(x, y):
    r = 6378137.0
    return math.degrees(x / r), math.degrees(2 * math.atan(math.exp(y / r)) - math.pi / 2)


def supported(epsg: int | None) -> bool:
    return epsg in GEOGRAPHIC or epsg in PROJECTED


def to_wgs84(epsg: int, x: float, y: float) -> tuple[float, float]:
    if epsg in GEOGRAPHIC:
        return x, y
    p = PROJECTED[epsg]
    if p["kind"] == "lcc":
        return _lcc_inverse(p, x, y)
    if p["kind"] == "aea":
        return _aea_inverse(p, x, y)
    if p["kind"] == "utm":
        return _utm_inverse(p, x, y)
    return _merc_inverse(x, y)


def bbox_to_wgs84(epsg: int | None, bbox: list[float] | tuple[float, ...] | None):
    """Transform a native bbox by densifying its edges; ``None`` when unsupported."""
    if bbox is None or epsg is None or not supported(epsg):
        return None
    x0, y0, x1, y1 = bbox
    if not all(math.isfinite(v) for v in bbox) or x1 < x0 or y1 < y0:
        return None
    points = []
    for i in range(9):
        f = i / 8
        points += [(x0 + (x1 - x0) * f, y0), (x0 + (x1 - x0) * f, y1),
                   (x0, y0 + (y1 - y0) * f), (x1, y0 + (y1 - y0) * f)]
    try:
        out = [to_wgs84(epsg, x, y) for x, y in points]
    except (ValueError, ZeroDivisionError, OverflowError):
        return None
    lons, lats = [p[0] for p in out], [p[1] for p in out]
    result = [min(lons), min(lats), max(lons), max(lats)]
    if not all(math.isfinite(v) for v in result) or result[0] < -180.5 or result[2] > 180.5 or result[1] < -90.5 or result[3] > 90.5:
        return None
    return [round(v, 7) for v in result]


def kansas_relation(bbox_wgs84) -> str:
    """Classify a WGS84 bbox against the Kansas envelope."""
    if bbox_wgs84 is None:
        return "unknown"
    x0, y0, x1, y1 = bbox_wgs84
    kx0, ky0, kx1, ky1 = KANSAS_BBOX
    if x1 < kx0 - _TOLERANCE or x0 > kx1 + _TOLERANCE or y1 < ky0 - _TOLERANCE or y0 > ky1 + _TOLERANCE:
        return "outside"
    if x0 >= kx0 - _TOLERANCE and x1 <= kx1 + _TOLERANCE and y0 >= ky0 - _TOLERANCE and y1 <= ky1 + _TOLERANCE:
        return "inside"
    return "overlaps"


def epsg_from_wkt(wkt: str) -> int | None:
    """Best-effort EPSG code from an ESRI/OGC WKT string (e.g. a shapefile .prj)."""
    found = re.findall(r'AUTHORITY\[\s*"EPSG"\s*,\s*"?(\d{4,6})"?\s*\]', wkt, re.IGNORECASE)
    if found:
        return int(found[-1])
    lowered = wkt.lower().replace("\\", "")
    head = re.match(r'\s*(projcs|geogcs|projcrs|geogcrs)\s*\[\s*"([^"]*)"', lowered)
    if head and head.group(1).startswith("geog"):
        name = head.group(2)
        if "1927" in name or "nad27" in name or "nad_1927" in name:
            return 4267
        if "1983" in name or "nad83" in name:
            return 4269
        if "wgs" in name and "84" in name:
            return 4326
        return None
    name = head.group(2) if head else lowered[:400]
    utm = re.search(r"utm[_ ]zone[_ ]?(\d{1,2})\s*n", name)
    if utm:
        zone = int(utm.group(1))
        base = 26700 if ("1927" in name or "nad27" in name) else 26900 if ("1983" in name or "nad83" in name) else 32600
        return base + zone
    for pattern, code in _WKT_NAMES:
        if re.search(pattern, name):
            return code
    return None
