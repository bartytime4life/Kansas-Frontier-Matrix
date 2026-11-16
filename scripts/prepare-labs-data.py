#!/usr/bin/env python3
"""Fetch public federal records and build the five offline-capable Labs snapshots.

Run from the application root: python3 scripts/prepare-labs-data.py
Raw responses stay in ignored work/labs-raw; only bounded Kansas derivatives ship.
No local database, pending relay dataset, credential or private preview is read.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MAX_RAW = 50_000_000
MAX_BUNDLE = 3_000_000
NOAA = "https://www.ncei.noaa.gov/pub/data/cirs/climdiv/"
PUBLIC_DOMAIN = "U.S. government data; credit the source; no warranty or endorsement"
DIVISIONS = ["Northwest", "North Central", "Northeast", "West Central", "Central", "East Central", "Southwest", "South Central", "Southeast"]


def encoded(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode()


def sha(value):
    return hashlib.sha256(value).hexdigest()


class Fetcher:
    def __init__(self, cache: Path, offline=False):
        self.cache, self.offline = cache, offline
        cache.mkdir(parents=True, exist_ok=True)

    def get(self, url):
        key = sha(url.encode())
        raw_file, meta_file = self.cache / (key + ".raw"), self.cache / (key + ".json")
        if self.offline:
            body, meta = raw_file.read_bytes(), json.loads(meta_file.read_text())
            assert meta["rawSha256"] == sha(body) and meta["url"] == url
            return body, meta
        request = Request(url, headers={"User-Agent": "Mozilla/5.0 (KFM public research snapshot)", "Accept": "*/*"})
        with urlopen(request, timeout=90) as response:
            if response.status != 200:
                raise ValueError(f"Unexpected HTTP {response.status}: {url}")
            body = response.read(MAX_RAW + 1)
            if len(body) > MAX_RAW:
                raise ValueError(f"Response exceeds acquisition limit: {url}")
            meta = {"url": url, "retrievedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    "rawSha256": sha(body), "rawBytes": len(body), "lastModified": response.headers.get("Last-Modified")}
        raw_file.write_bytes(body)
        meta_file.write_bytes(encoded(meta))
        return body, meta


def source(name, url, citation):
    return {"name": name, "url": url, "license": PUBLIC_DOMAIN, "citation": citation}


def bundle(story, data, sources, snapshots, observed):
    data.update(sourceSnapshot=snapshots[0], sourceSnapshots=snapshots)
    return {"format": "kfm-story-bundle-v1", "story": story, "version": 1,
            "built_at": max(s["retrievedAt"] for s in snapshots), "sources": sources, "observed": observed, "data": data}


def column(key, label, kind="number", unit=None):
    return {"key": key, "label": label, "type": kind, **({"unit": unit} if unit else {})}


def records(story, rows, columns, sources, snapshots, coverage, limits, **options):
    assert rows and len(rows) <= 10000 and len({str(row["id"]) for row in rows}) == len(rows)
    years = [r["year"] for r in rows]
    data = {"kind": "records", "records": rows, "columns": columns, "coverage": coverage,
            "yearField": "year", "temporalMode": "events", "limits": limits, **options}
    return bundle(story, data, sources, snapshots, {"from": str(min(years)), "to": str(max(years))})


def climate(fetch):
    stamp_raw, stamp_meta = fetch.get(NOAA + "procdate.txt")
    stamp = stamp_raw.decode().strip()
    assert re.fullmatch(r"20\d{6}", stamp)
    specs = {"tmpc": {"label": "Temperature", "unit": "°F", "scale": 10, "annual": "mean", "family": "heat"},
             "pcpn": {"label": "Precipitation", "unit": "in", "scale": 100, "annual": "sum", "family": "water"},
             "pdsi": {"label": "Drought index (PDSI)", "unit": "index", "scale": 100, "annual": "mean", "family": "water"}}
    jobs = [(element, suffix, NOAA + f"climdiv-{element}{suffix}-v1.0.0-{stamp}")
            for element in specs for suffix in ("st", "dv")]
    with ThreadPoolExecutor(max_workers=3) as pool:
        replies = list(pool.map(lambda job: fetch.get(job[2]), jobs))
    series, snapshots = {}, [stamp_meta]
    for (element, suffix, _), (raw, meta) in zip(jobs, replies):
        snapshots.append(meta)
        for line in raw.decode("ascii").splitlines():
            # NOAA's Kansas state code is 014 (FIPS 20); divisions are 1401–1409.
            area_code = line[:4]
            if (suffix == "st" and area_code != "0140") or (suffix == "dv" and area_code not in {f"140{i}" for i in range(1, 10)}):
                continue
            area = "20" if suffix == "st" else area_code
            year = int(line[6:10])
            months = [float(line[10 + i * 7:17 + i * 7]) for i in range(12)]
            series.setdefault(element, {}).setdefault(area, {})[year] = [None if value <= (-0.01 if element == "pcpn" else -99) else value for value in months]
    years = sorted(series["tmpc"]["20"])
    assert years[0] == 1895 and years == list(range(years[0], years[-1] + 1))
    areas = [{"id": "20", "name": "Kansas"}] + [{"id": f"140{i}", "name": name} for i, name in enumerate(DIVISIONS, 1)]
    values = {element: {area["id"]: [None if value is None else round(value * spec["scale"])
              for year in years for value in series[element][area["id"]][year]] for area in areas} for element, spec in specs.items()}
    # Explicitly computed monthly averages, not mislabeled as NOAA's published normals.
    baselines = {"1901-2000": (1901, 2000), "1991-2020": (1991, 2020)}
    normals = {}
    for name, (start, end) in baselines.items():
        normals[name] = {}
        for element in ("tmpc", "pcpn"):
            normals[name][element] = {}
            for area in areas:
                months = [[series[element][area["id"]][year][m] for year in range(start, end + 1)] for m in range(12)]
                assert all(all(value is not None for value in month) for month in months)
                normals[name][element][area["id"]] = [round(sum(month) / len(month) * specs[element]["scale"]) for month in months]
    latest = max((year, month + 1) for year in years for month, value in enumerate(series["tmpc"]["20"][year]) if value is not None)
    data = {"years": years, "areas": areas, "elements": specs, "values": values, "normals": normals,
            "baselines": list(baselines), "latest": {"year": latest[0], "month": latest[1]},
            "limits": ["NOAA area-weighted grid estimates, not measurements at an individual location; early station coverage is sparse.",
                       "Baseline monthly means are calculated from this same snapshot for 1901–2000 and 1991–2020, rounded to the stored precision. They are not NOAA's separately published normals.",
                       "PDSI is already an index and does not use the selected baseline. Recent NOAA values may be revised.",
                       f"The final year includes data only through {latest[0]}-{latest[1]:02d}; partial-year stripes compare the same available months.",
                       "This is a downloadable snapshot, not an automatically updating weather service."]}
    return bundle("climate-stripes", data, [source("NOAA NCEI nClimDiv", NOAA, "NOAA National Centers for Environmental Information, monthly statewide and climate-divisional temperature, precipitation and PDSI series.")], snapshots,
                  {"from": "1895-01", "to": f"{latest[0]}-{latest[1]:02d}"})


def census(fetch):
    url = "https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/counties/totals/co-est2025-alldata.csv"
    raw, meta = fetch.get(url)
    counties = [r for r in csv.DictReader(io.StringIO(raw.decode("cp1252"))) if r["STATE"] == "20" and r["SUMLEV"] == "050"]
    assert len(counties) == 105
    geo_url = "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer/1/query?" + urlencode({"where": "STATE='20'", "outFields": "GEOID,NAME", "outSR": "4326", "f": "geojson", "geometryPrecision": "3", "maxAllowableOffset": "0.015", "returnGeometry": "true"})
    geo_raw, geo_meta = fetch.get(geo_url)
    geo = json.loads(geo_raw)
    assert not geo.get("exceededTransferLimit") and len(geo["features"]) == 105
    geometries = {f["properties"]["GEOID"]: f["geometry"] for f in geo["features"]}
    rows = []
    for county in counties:
        geoid = county["STATE"] + county["COUNTY"]
        for year in range(2020, 2026):
            row = {"id": f"{geoid}-{year}", "name": county["CTYNAME"], "county": county["CTYNAME"], "fips": geoid, "year": year}
            for key, field in (("population", "POPESTIMATE"), ("births", "BIRTHS"), ("deaths", "DEATHS"), ("netMigration", "NETMIG"), ("naturalChange", "NATURALCHG")):
                value = county.get(f"{field}{year}")
                row[key] = int(value) if value not in (None, "", "X", "(X)") else None
            row["geometry"] = geometries[geoid]
            rows.append(row)
    return records("census-mosaic", rows, [column("name", "County", "string"), column("fips", "County FIPS", "string"), column("year", "Year", "year"),
                    column("population", "Population", unit="people"), column("births", "Births", unit="people"), column("deaths", "Deaths", unit="people"),
                    column("naturalChange", "Natural change", unit="people"), column("netMigration", "Net migration", unit="people")],
                   [source("U.S. Census Population Estimates, Vintage 2025", url, "U.S. Census Bureau, CO-EST2025-ALLDATA, Kansas county totals and components of change, 2020–2025."),
                    source("Census TIGERweb", geo_url, "U.S. Census Bureau, TIGERweb contemporary county boundaries; simplified for this display.")], [meta, geo_meta], "105 Kansas counties, six July 1 estimates (2020–2025)",
                   ["July 1 population estimates; this vintage can revise earlier years.", "2020 components describe a partial year. Components need not equal the population difference because of residual adjustments.",
                    "Contemporary county shapes are simplified display boundaries. Each selected year contains exactly one estimate per county; years must not be summed."],
                   temporalMode="snapshot", categoryField="name", valueField="population")


def rivers(fetch, end):
    url = "https://waterservices.usgs.gov/nwis/dv/?" + urlencode({"format": "json", "sites": "06892350,07144300,06887000", "startDT": "2020-01-01", "endDT": end, "parameterCd": "00060", "statCd": "00003", "siteStatus": "all"})
    raw, meta = fetch.get(url)
    rows, sites = [], set()
    for series in json.loads(raw)["value"]["timeSeries"]:
        site = series["sourceInfo"]
        code, name = site["siteCode"][0]["value"], site["siteName"]
        sites.add(code)
        assert series["variable"]["unit"]["unitCode"] == "ft3/s"
        location = site["geoLocation"]["geogLocation"]
        for group in series["values"]:
            for value in group["value"]:
                date = value["dateTime"][:10]
                number = float(value["value"])
                rows.append({"id": f"{code}-{date}", "name": name, "site": name, "siteCode": code, "date": date, "year": int(date[:4]),
                             "discharge": None if number == float(series["variable"]["noDataValue"]) else number,
                             "qualifiers": ", ".join(value.get("qualifiers", [])), "longitude": location["longitude"], "latitude": location["latitude"],
                             "url": f"https://waterdata.usgs.gov/monitoring-location/USGS-{code}/"})
    assert len(sites) == 3
    return records("river-memory", rows, [column("name", "Gauge", "string"), column("siteCode", "USGS site", "string"), column("date", "Date", "string"), column("year", "Year", "year"),
                   column("discharge", "Daily mean discharge", unit="ft³/s"), column("qualifiers", "Source qualifiers", "string"), column("url", "Source record", "string")],
                   [source("USGS daily mean discharge", url, "U.S. Geological Survey, daily mean discharge (00060, statistic 00003), Kansas River at De Soto, Arkansas River at Wichita, and Big Blue River near Manhattan.")], [meta], f"Three selected Kansas gauges, 2020-01-01 through {end}",
                   ["Three gauges are a selected comparison, not statewide coverage. Flow is daily mean discharge in cubic feet per second, not stage or a flood forecast.",
                    "A means approved and P means provisional. Other source qualifier codes are retained. Missing observations remain missing; no interpolation is applied.",
                    "Monthly trend values are means of available daily observations; differing missing days affect comparisons."],
                   categoryField="name", valueField="discharge", dateField="date", preferredView="chart")


def tornadoes(fetch):
    url = "https://www.spc.noaa.gov/wcm/data/1950-2025_actual_tornadoes.csv"
    raw, meta = fetch.get(url)
    rows = []
    for r in csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))):
        if r["st"] != "KS":
            continue
        lat, lon, elat, elon = (float(r[k]) for k in ("slat", "slon", "elat", "elon"))
        # The source repeats an OM identifier for two distinct 2002 records.
        # Retain both with source date/time and state sequence; never deduplicate by OM alone.
        row = {"id": f"{r['yr']}-{r['om']}-{r['date']}-{r['time']}-{r['stn']}", "name": f"{r['date']} · F/EF{r['mag']}", "date": r["date"], "year": int(r["yr"]),
               "sourceId": r["om"], "sourceTime": r["time"], "estimatedRatingFlag": int(r["fc"]),
               "rating": "Unknown" if int(r["mag"]) < 0 else f"F/EF{r['mag']}", "magnitude": None if int(r["mag"]) < 0 else int(r["mag"]),
               "length": float(r["len"]), "width": float(r["wid"]), "injuries": int(r["inj"]), "fatalities": int(r["fat"])}
        # Zero endpoints mean unknown; do not draw a fabricated line to the Gulf of Guinea.
        if lat and lon:
            row.update(longitude=lon, latitude=lat)
            if elat and elon:
                row["geometry"] = {"type": "LineString", "coordinates": [[lon, lat], [elon, elat]]}
        rows.append(row)
    return records("tornado-tracks", rows, [column("date", "Date", "string"), column("sourceTime", "Source time (source time zone)", "string"), column("sourceId", "SPC identifier", "string"), column("year", "Year", "year"), column("rating", "Rating", "string"), column("estimatedRatingFlag", "Source estimated-rating flag"),
                   column("length", "Path length", unit="mi"), column("width", "Path width", unit="yd"), column("injuries", "Reported injuries"), column("fatalities", "Reported fatalities")],
                   [source("NOAA Storm Prediction Center", url, "NOAA/NWS Storm Prediction Center, 1950–2025 actual tornado tracks, rows with starting state KS; retrieved as a source snapshot.")], [meta], "Whole tornadoes starting in Kansas, 1950–2025",
                   ["Actual-tornado rows count whole tracks once; tracks starting outside Kansas are excluded even if they enter the state. Whole tracks can extend outside Kansas.",
                    "Straight lines join reported endpoints and are not damage footprints. Missing endpoints are not invented.",
                    "F and EF ratings are categorical damage scales. Unknown ratings remain unknown. Earlier tornadoes are underreported; observation methods and population exposure change.",
                    "Source injuries and fatalities are reported values. The snapshot ends in 2025 and is not a live alert or forecast."], categoryField="rating", valueField="length")


def earthquakes(fetch, end):
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?" + urlencode({"format": "geojson", "starttime": "2010-01-01", "endtime": end,
          "minlatitude": "36.8", "maxlatitude": "40.1", "minlongitude": "-102.1", "maxlongitude": "-94.5", "minmagnitude": "1", "eventtype": "earthquake", "orderby": "time-asc", "limit": "10000"})
    raw, meta = fetch.get(url)
    catalog = json.loads(raw)
    assert 0 < len(catalog["features"]) < 10000, "Earthquake query needs pagination; never publish a capped catalog as complete"
    rows = []
    for f in catalog["features"]:
        p, xyz = f["properties"], f["geometry"]["coordinates"]
        date = datetime.fromtimestamp(p["time"] / 1000, timezone.utc).isoformat(timespec="seconds")
        rows.append({"id": f["id"], "name": p.get("place") or f["id"], "date": date, "year": int(date[:4]), "magnitude": p.get("mag"),
                     "magnitudeType": p.get("magType") or "Not recorded", "depth": xyz[2], "longitude": xyz[0], "latitude": xyz[1],
                     "status": p.get("status") or "Not recorded", "url": p["url"]})
    return records("shaking-ground", rows, [column("name", "Reported place", "string"), column("date", "UTC time", "string"), column("year", "Year", "year"),
                   column("magnitude", "Magnitude"), column("magnitudeType", "Magnitude type", "string"), column("depth", "Depth", unit="km"), column("status", "Review status", "string"), column("url", "USGS record", "string")],
                   [source("USGS ComCat", url, "U.S. Geological Survey, ANSS Comprehensive Earthquake Catalog (ComCat), earthquake events M≥1, 2010 onward, bounding box 36.8–40.1°N, 102.1–94.5°W.")], [meta], f"M≥1 earthquakes in Kansas and the immediate border region, 2010-01-01 through {end} UTC",
                   ["The bounding box includes neighboring states. Detection and magnitude thresholds vary over time and space; missing small events are not evidence of no seismicity.",
                    "Magnitude types differ; counts and spatial correlation do not establish cause. Depth is the source estimate, not a measured subsurface structure.",
                    "This catalog snapshot is not real time and is not a hazard prediction. USGS can revise reviewed and automatic events."], categoryField="magnitudeType", valueField="magnitude", dateField="date")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=ROOT / "work/labs-raw")
    parser.add_argument("--offline", action="store_true", help="Rebuild using hash-verified raw responses without fetching")
    parser.add_argument("--through", default=datetime.now(timezone.utc).date().isoformat())
    args = parser.parse_args()
    fetch = Fetcher(args.cache, args.offline)
    builders = [lambda: climate(fetch), lambda: census(fetch), lambda: rivers(fetch, args.through), lambda: tornadoes(fetch), lambda: earthquakes(fetch, args.through)]
    # Finish every acquisition before replacing any shipping snapshot or manifest.
    with ThreadPoolExecutor(max_workers=3) as pool:
        bundles = list(pool.map(lambda build: build(), builders))
    manifest, outputs = {}, {}
    for result in bundles:
        raw = encoded(result)
        assert 0 < len(raw) <= MAX_BUNDLE
        digest, story = sha(raw), result["story"]
        filename = f"{story}-{digest[:16]}.json"
        outputs[filename] = raw
        manifest[story] = {"path": "/labs-data/" + filename, "sha256": digest, "bytes": len(raw), "observed": result["observed"],
                           "retrievedAt": result["built_at"], "records": len(result["data"].get("records", [])) or None}
    target = ROOT / "public/labs-data"
    target.mkdir(parents=True, exist_ok=True)
    for filename, raw in outputs.items():
        (target / filename).write_bytes(raw)
    module = "// Generated by scripts/prepare-labs-data.py from public federal responses.\nexport const PUBLIC_LAB_SNAPSHOTS = Object.freeze(" + json.dumps(manifest, indent=2) + ");\n"
    # JavaScript's null is also JSON null; this is a literal object, never executable source input.
    (ROOT / "app/labs/public-snapshots.mjs").write_text(module)
    for old in target.glob("*.json"):
        if old.name not in outputs:
            old.unlink()
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
