"""Bounded NOAA NWM source capture; no admission, scheduling or publication."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
import json
import re
import time
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

MIB = 1024**2
BASE = "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/"
FLOWLINES = "https://maps.water.noaa.gov/server/rest/services/reference/static_nwm_flowlines/FeatureServer/0"
BBOX = [-102.052, 36.993, -94.588, 40.004]
CHANNEL_LIMIT = 16*MIB
PAGE_LIMIT = 4*MIB
MAX_REACHES = 125000
PAGE_SIZE = 500
DOCS = {"nwm-about.html": "https://water.noaa.gov/about/nwm",
        "output-file-contents.html": "https://water.noaa.gov/about/output_file_contents"}


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def cycle_time(day, hour):
    if not re.fullmatch(r"20\d{6}", day) or type(hour) is not int or not 0 <= hour <= 23:
        raise ValueError("CYCLE_INVALID")
    return datetime.strptime(day, "%Y%m%d").replace(hour=hour, tzinfo=timezone.utc)


def model_objects(day, hour):
    reference = cycle_time(day, hour)
    specs = []
    for lead in range(19):
        product = "short_range" if lead else "analysis_assim"
        suffix = f"f{lead:03d}" if lead else "tm00"
        name = f"nwm.t{hour:02d}z.{product}.channel_rt.{suffix}.conus.nc"
        specs.append({"name": name, "url": f"{BASE}nwm.{day}/{product}/{name}",
                      "product": product, "lead_hours": lead,
                      "filename_cycle_time": reference.isoformat().replace("+00:00", "Z"),
                      "valid_time": (reference+timedelta(hours=lead)).isoformat().replace("+00:00", "Z")})
    return specs


def latest_day(body):
    days = re.findall(r'href="nwm\.(20\d{6})/"', body.decode("utf-8"))
    if not days:
        raise ValueError("NO_DATED_RUNS")
    return max(days)


def latest_complete_cycle(body):
    matches = re.findall(r'href="nwm\.t(\d{2})z\.short_range\.channel_rt\.f(\d{3})\.conus\.nc"', body.decode("utf-8"))
    cycles = {int(h) for h, _ in matches if 0 <= int(h) <= 23}
    complete = [h for h in cycles if {int(f) for c, f in matches if int(c) == h} == set(range(1, 19))]
    if not complete:
        raise ValueError("NO_COMPLETE_18_HOUR_CYCLE")
    return max(complete)


def ids_url():
    return FLOWLINES+"/query?"+urlencode({"f": "json", "where": "1=1", "geometry": ",".join(map(str, BBOX)),
        "geometryType": "esriGeometryEnvelope", "inSR": "4326", "spatialRel": "esriSpatialRelIntersects",
        "returnIdsOnly": "true"})


def page_url(ids):
    if not 0 < len(ids) <= PAGE_SIZE or any(type(i) is not int or i <= 0 for i in ids) or len(set(ids)) != len(ids):
        raise ValueError("OBJECT_IDS_INVALID")
    return FLOWLINES+"/query?"+urlencode({"f": "json", "objectIds": ",".join(map(str, ids)),
        "outFields": "oid,feature_id,name,strm_order,huc6,nwm_vers", "outSR": "4326",
        "returnGeometry": "true", "orderByFields": "oid ASC"})


def object_ids(body):
    obj = json.loads(body)
    ids = obj.get("objectIds", [])
    if (obj.get("objectIdFieldName") != "oid" or obj.get("error") or obj.get("exceededTransferLimit")
            or not 0 < len(ids) <= MAX_REACHES or any(type(i) is not int or i <= 0 for i in ids)
            or len(set(ids)) != len(ids)):
        raise ValueError("FLOWLINE_IDS_INVALID")
    return sorted(ids)


def allowed_url(url):
    if url in DOCS.values() or url == BASE or url == FLOWLINES+"?f=json" or url == ids_url():
        return True
    if url.startswith(BASE):
        key = url[len(BASE):]
        if re.fullmatch(r"nwm\.20\d{6}/short_range/", key):
            return True
        match = re.fullmatch(r"nwm\.(20\d{6})/(analysis_assim|short_range)/(nwm\.t(\d{2})z\.[^/]+\.nc)", key)
        if match:
            try:
                return url in {o["url"] for o in model_objects(match[1], int(match[4]))}
            except ValueError:
                return False
    # Queries are built internally; no redirects or alternate hosts are accepted.
    parsed = urlsplit(url)
    return (url.startswith(FLOWLINES+"/query?") and parsed.fragment == ""
            and re.fullmatch(r"f=json&objectIds=\d+(?:%2C\d+)*&outFields=oid%2Cfeature_id%2Cname%2Cstrm_order%2Chuc6%2Cnwm_vers&outSR=4326&returnGeometry=true&orderByFields=oid\+ASC", parsed.query) is not None)


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def fetch(url, limit, *, head=False):
    if not allowed_url(url) or not 0 < limit <= CHANNEL_LIMIT:
        raise ValueError("SOURCE_REQUEST_NOT_ALLOWED")
    started = time.monotonic()
    request = Request(url, method="HEAD" if head else "GET", headers={
        "User-Agent": "KFM bounded Kansas NWM capture", "Accept-Encoding": "identity"})
    with build_opener(NoRedirect).open(request, timeout=30) as response:
        if response.status != 200 or response.geturl() != url:
            raise ValueError("SOURCE_RESPONSE_INVALID")
        declared = response.headers.get("Content-Length")
        declared = declared.strip() if declared is not None else None
        if declared is not None and (not declared.isdigit() or not 0 < int(declared) <= limit):
            raise ValueError("SOURCE_BYTE_LIMIT")
        headers = {"source_url": url, "retrieved_at": now(), "declared_bytes": int(declared) if declared else None,
                   "last_modified": response.headers.get("Last-Modified"), "etag": response.headers.get("ETag"),
                   "provider_checksum": None}
        if head:
            if declared is None:
                raise ValueError("SOURCE_SIZE_UNKNOWN")
            return b"", headers
        chunks, count = [], 0
        while True:
            if time.monotonic()-started > 120:
                raise ValueError("SOURCE_DEADLINE")
            chunk = response.read(min(65536, limit-count+1))
            if not chunk:
                break
            count += len(chunk)
            if count > limit:
                raise ValueError("SOURCE_BYTE_LIMIT")
            chunks.append(chunk)
        if not count or (declared is not None and count != int(declared)):
            raise ValueError("SOURCE_SIZE_MISMATCH")
        return b"".join(chunks), headers
