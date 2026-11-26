#!/usr/bin/env python3
"""Capture fixed official history privately, then prepare bounded provider-context displays.

No credentials, dataset admission, release, or hosted deployment. Capture and
offline preparation are separate. Original bytes and transport receipts stay
outside the checkout; only selected observations and provenance enter the app.
"""
from __future__ import annotations

import argparse
import csv
from datetime import date, datetime, timedelta, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import time
from urllib.parse import urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
YEARS = tuple(range(2020, 2026))
PERIOD = {"from": "2020-01-01", "to": "2025-12-31"}
DEPTHS = (5, 10, 20, 50, 100)
STATIONS = {"53974": "KS_Manhattan_6_SSW", "03067": "KS_Oakley_19_SSW"}
USCRN = "https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/"
USDM = "https://usdmdataservices.unl.edu/api/CountyStatistics/GetDroughtSeverityStatisticsByAreaPercent"
DROUGHT_DOC = "https://droughtmonitor.unl.edu/DmData/DataDownload/WebServiceInfo.aspx"
ATTRIBUTION = ("The U.S. Drought Monitor is jointly produced by the National Drought Mitigation Center at the "
               "University of Nebraska-Lincoln, the U.S. Department of Agriculture, the National Oceanic and "
               "Atmospheric Administration and NASA. Data courtesy of NDMC, via https://droughtmonitor.unl.edu.")
PROFILE = ("WBANNO", "LST_DATE", "CRX_VN", "LONGITUDE", "LATITUDE", "T_DAILY_MAX", "T_DAILY_MIN",
           "T_DAILY_MEAN", "T_DAILY_AVG", "P_DAILY_CALC", "SOLARAD_DAILY", "SUR_TEMP_DAILY_TYPE",
           "SUR_TEMP_DAILY_MAX", "SUR_TEMP_DAILY_MIN", "SUR_TEMP_DAILY_AVG", "RH_DAILY_MAX", "RH_DAILY_MIN",
           "RH_DAILY_AVG", *(f"SOIL_MOISTURE_{d}_DAILY" for d in DEPTHS), *(f"SOIL_TEMP_{d}_DAILY" for d in DEPTHS))
COUNTIES = {f"20{n:03d}" for n in range(1, 210, 2)}
MIB = 1024 * 1024


def encode(value):
    return (json.dumps(value, ensure_ascii=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def tuesdays(year):
    day = date(year, 1, 1)
    day += timedelta(days=(1 - day.weekday()) % 7)
    out = []
    while day.year == year:
        out.append(day.isoformat())
        day += timedelta(days=7)
    return out


def plans():
    out = []
    for year in YEARS:
        first, last = [date.fromisoformat(d) for d in (tuesdays(year)[0], tuesdays(year)[-1])]
        # The API selects overlapping validity intervals. Start on the first
        # Tuesday to exclude the previous year's assessment from annual files.
        query = urlencode({"aoi": "KS", "startdate": f"{first.month}/{first.day}/{year}",
                           "enddate": f"{last.month}/{last.day}/{year}", "statisticsType": 1})
        out.append((f"drought-{year}.csv", USDM + "?" + query, 2 * MIB))
    out.extend((("uscrn-headers.txt", USCRN + "headers.txt", 64 * 1024),
                ("uscrn-readme.txt", USCRN + "README.txt", 128 * 1024)))
    for wban, name in STATIONS.items():
        for year in YEARS:
            out.append((f"soil-{wban}-{year}.txt", f"{USCRN}{year}/CRND0103-{year}-{name}.txt", MIB))
    return out


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def capture(folder):
    folder = folder.resolve()
    if folder.is_relative_to(ROOT):
        raise ValueError("Original captures must be outside the repository")
    folder.mkdir(mode=0o700, parents=True, exist_ok=False)
    pages, total = [], 0
    for key, url, limit in plans():
        started = time.monotonic()
        with build_opener(NoRedirect).open(Request(url, headers={"Accept": "text/csv" if key.endswith(".csv") else "text/plain",
                "Accept-Encoding": "identity", "User-Agent": "KFM bounded historical science display capture"}), timeout=30) as response:
            if response.status != 200 or response.geturl() != url:
                raise ValueError("SOURCE_RESPONSE_INVALID")
            length = response.headers.get("Content-Length")
            if length is not None and (not length.isdigit() or int(length) > limit):
                raise ValueError("SOURCE_SIZE_LIMIT")
            chunks, count = [], 0
            while True:
                if time.monotonic() - started > 90:
                    raise ValueError("SOURCE_DEADLINE")
                part = response.read(min(65536, limit - count + 1))
                if not part:
                    break
                count += len(part)
                if count > limit:
                    raise ValueError("SOURCE_SIZE_LIMIT")
                chunks.append(part)
            raw = b"".join(chunks)
            total += count
            if not raw or (length is not None and count != int(length)) or total > 24 * MIB:
                raise ValueError("SOURCE_SIZE_MISMATCH")
            target = folder / key
            target.write_bytes(raw)
            target.chmod(0o600)
            pages.append({"key": key, "url": url, "sha256": sha(raw), "bytes": count, "capturedAt": now(),
                          "lastModified": response.headers.get("Last-Modified"), "etag": response.headers.get("ETag")})
        print(f"Captured {key}: {count} bytes", flush=True)
    (folder / "capture.json").write_bytes(encode({"schema": "kfm.historical-science-capture/v1", "pages": pages}))
    (folder / "capture.json").chmod(0o600)


def verified(folder):
    folder = folder.resolve()
    if folder.is_relative_to(ROOT):
        raise ValueError("Original captures must be outside the repository")
    manifest = json.loads((folder / "capture.json").read_bytes())
    pages = manifest.get("pages")
    expected = plans()
    if (manifest.get("schema") != "kfm.historical-science-capture/v1" or not isinstance(pages, list)
            or [p.get("key") for p in pages if isinstance(p, dict)] != [p[0] for p in expected]):
        raise ValueError("CAPTURE_SCOPE_MISMATCH")
    out = {}
    for page, (key, url, limit) in zip(pages, expected):
        path = folder / key
        if path.is_symlink() or path.stat().st_size > limit:
            raise ValueError("CAPTURE_FILE_INVALID")
        raw = path.read_bytes()
        if (page.get("url") != url or page.get("bytes") != len(raw) or sha(raw) != page.get("sha256")
                or not raw or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", str(page.get("capturedAt", "")))):
            raise ValueError("CAPTURE_DIGEST_MISMATCH")
        out[key] = (raw, {k: v for k, v in page.items() if k != "key"})
    return out


def parse_drought(raw, year):
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))
    fields = ["MapDate", "FIPS", "County", "State", "None", "D0", "D1", "D2", "D3", "D4", "ValidStart", "ValidEnd", "StatisticFormatID"]
    if reader.fieldnames != fields:
        raise ValueError("DROUGHT_HEADER_MISMATCH")
    out, names, days = {}, {}, set(tuesdays(year))
    for row in reader:
        if None in row or any(value is None for value in row.values()):
            raise ValueError("DROUGHT_ROW_SHAPE")
        identity, day = row["FIPS"], row["ValidStart"]
        if (identity not in COUNTIES or row["State"] != "KS" or row["StatisticFormatID"] != "1"
                or day not in days or row["MapDate"] != day.replace("-", "")
                or row["ValidEnd"] != (date.fromisoformat(day) + timedelta(days=6)).isoformat()
                or not re.fullmatch(r"[A-Za-z][A-Za-z .'-]{0,50} County", row["County"])):
            raise ValueError("DROUGHT_ID_OR_DATE")
        if (identity, day) in out or (identity in names and names[identity] != row["County"]):
            raise ValueError("DROUGHT_DUPLICATE_OR_NAME")
        tokens = [row[key] for key in ("None", "D0", "D1", "D2", "D3", "D4")]
        if any(not re.fullmatch(r"\d{1,3}\.\d{2}", value) or not 0 <= float(value) <= 100 for value in tokens):
            raise ValueError("DROUGHT_PERCENT_INVALID")
        values = [float(token) for token in tokens]
        if abs(values[0] + values[1] - 100) > 0.011 or any(a < b for a, b in zip(values[1:], values[2:])):
            raise ValueError("DROUGHT_CUMULATIVE_INVALID")
        names[identity] = row["County"]
        out[(identity, day)] = values
    if set(names) != COUNTIES or len(out) != len(COUNTIES) * len(days):
        raise ValueError("DROUGHT_COVERAGE_INCOMPLETE")
    return names, out


def parse_soil(raw, wban, year):
    out, coordinates = {}, set()
    for line in raw.decode("ascii").splitlines():
        if not line.strip():
            continue
        fields = line.split()
        if len(fields) != 28 or fields[0] != wban or not re.fullmatch(r"\d{8}", fields[1]):
            raise ValueError("SOIL_ROW_ID_OR_SHAPE")
        day = datetime.strptime(fields[1], "%Y%m%d").date()
        if day.year != year or day.isoformat() in out or not re.fullmatch(r"(?:\d{1,2}\.\d{1,3}|-9\.000)", fields[2]):
            raise ValueError("SOIL_DATE_OR_VERSION")
        lon, lat = float(fields[3]), float(fields[4])
        if not -102.2 <= lon <= -94.4 or not 36.9 <= lat <= 40.1:
            raise ValueError("SOIL_LOCATION_INVALID")
        coordinates.add((lon, lat))
        moisture, temperature = fields[18:23], fields[23:28]
        if (any(not re.fullmatch(r"-?\d{1,2}\.\d{3}", token) for token in moisture)
                or any(not re.fullmatch(r"-?\d{1,4}\.\d", token) for token in temperature)):
            raise ValueError("SOIL_TOKEN_INVALID")
        # Keep source tokens verbatim; sentinels and range exceptions are
        # classified in the analysis, never silently coerced or interpolated.
        out[day.isoformat()] = {"date": day.isoformat(), "version": fields[2], "moisture": moisture, "temperature": temperature}
    expected = (date(year + 1, 1, 1) - date(year, 1, 1)).days
    if len(out) != expected or len(coordinates) != 1:
        raise ValueError("SOIL_COVERAGE_OR_LOCATION")
    return out, next(iter(coordinates))


def asset(kind, identity, snapshot, outputs):
    raw = encode(snapshot)
    digest = sha(raw)
    name = f"{identity}-{digest[:16]}.json"
    folder = ROOT / "public/science-data" / kind
    outputs[folder / name] = raw
    return {"id": identity, "url": f"/science-data/{kind}/{name}", "sha256": digest, "bytes": len(raw)}


def prepare(folder):
    sources = verified(folder)
    outputs = {}
    names, rows, drought_sources = {}, {}, []
    weeks = [day for year in YEARS for day in tuesdays(year)]
    for year in YEARS:
        raw, source = sources[f"drought-{year}.csv"]
        annual_names, annual_rows = parse_drought(raw, year)
        if names and annual_names != names:
            raise ValueError("DROUGHT_COUNTY_INVENTORY_CHANGED")
        names, rows = annual_names, {**rows, **annual_rows}
        drought_sources.append({"year": year, **source})
    counties = [{"id": identity, "name": names[identity], "values": [rows[(identity, day)] for day in weeks]} for identity in sorted(COUNTIES)]
    snapshot = {"schema": "kfm.county-drought/v1", "period": PERIOD, "weeks": weeks, "sources": drought_sources,
                "counties": counties, "statisticsType": 1, "attribution": ATTRIBUTION}
    drought_manifest = {"schema": "kfm.county-drought-manifest/v1", "period": PERIOD, "provider": "U.S. Drought Monitor",
                        "documentation": DROUGHT_DOC, "permission": "https://droughtmonitor.unl.edu/About/Permission.aspx",
                        "scope": "provider-context", "attribution": ATTRIBUTION, "sources": drought_sources,
                        "counties": [{"id": c["id"], "name": c["name"]} for c in counties],
                        "snapshot": {**asset("county-drought", "kansas", snapshot, outputs), "records": len(rows), "weeks": len(weeks)},
                        "generatedAt": max(s["capturedAt"] for s in drought_sources)}
    drought_path = ROOT / "app/labs/county-drought/snapshot-manifest.json"
    outputs[drought_path] = encode(drought_manifest)

    headers, header_source = sources["uscrn-headers.txt"]
    lines = [line.split() for line in headers.decode("ascii").splitlines() if line.strip()]
    if len(lines) < 2 or lines[0] != [str(i) for i in range(1, 29)] or tuple(lines[1]) != PROFILE:
        raise ValueError("SOIL_HEADER_PROFILE_MISMATCH")
    descriptors = []
    for wban, name in STATIONS.items():
        records, coordinates, station_sources = {}, set(), []
        for year in YEARS:
            raw, source = sources[f"soil-{wban}-{year}.txt"]
            annual_rows, coordinate = parse_soil(raw, wban, year)
            records.update(annual_rows)
            coordinates.add(coordinate)
            station_sources.append({"year": year, **source})
        if len(coordinates) != 1:
            raise ValueError("SOIL_STATION_MOVED")
        lon, lat = next(iter(coordinates))
        station = {"id": wban, "name": name.removeprefix("KS_").replace("_", " "), "longitude": lon, "latitude": lat, "utcOffsetHours": -6}
        snapshot = {"schema": "kfm.soil-profile/v1", "station": station, "period": PERIOD, "depthsCm": list(DEPTHS),
                    "sources": station_sources, "records": [records[day] for day in sorted(records)]}
        descriptors.append({**station, **asset("soil-profile", wban, snapshot, outputs), "records": len(records), "sources": station_sources})
    soil_manifest = {"schema": "kfm.soil-profile-manifest/v1", "provider": "NOAA NCEI U.S. Climate Reference Network",
                     "period": PERIOD, "depthsCm": list(DEPTHS), "documentation": USCRN + "README.txt", "scope": "provider-context",
                     "headerSource": header_source, "documentationSource": sources["uscrn-readme.txt"][1], "stations": descriptors,
                     "citation": "Diamond et al. (2013), U.S. Climate Reference Network after one decade of operations, doi:10.1175/BAMS-D-12-00170.1; Bell et al. (2013), U.S. Climate Reference Network soil moisture and temperature observations, doi:10.1175/JHM-D-12-0146.1.",
                     "generatedAt": max(s["capturedAt"] for d in descriptors for s in d["sources"])}
    soil_path = ROOT / "app/labs/soil-profile/snapshot-manifest.json"
    outputs[soil_path] = encode(soil_manifest)
    # Validate both families before writing any display artifact. A failed
    # source check cannot leave a partly refreshed pair of manifests behind.
    for path, raw in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    print(json.dumps({"drought": drought_manifest["snapshot"], "soil": [{k: d[k] for k in ("id", "url", "sha256", "bytes", "records")} for d in descriptors]}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--capture-dir", type=Path, help="NEW private directory outside repository; capture only")
    choice.add_argument("--source-dir", type=Path, help="Verified capture directory; prepare offline")
    args = parser.parse_args()
    if args.capture_dir:
        capture(args.capture_dir)
    else:
        prepare(args.source_dir)


if __name__ == "__main__":
    main()
