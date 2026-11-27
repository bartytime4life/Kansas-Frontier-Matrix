#!/usr/bin/env python3
"""Reproduce bounded Kansas daily AQI display data from public EPA captures.

Original national ZIPs stay outside every Git checkout. This prepares provider
context; it does not activate ingestion, admit a KFM dataset, or approve release.
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
import urllib.error
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://aqs.epa.gov/aqsweb/airdata/"
YEARS = tuple(range(2020, 2026))
PERIOD = {"from": "2020-01-01", "to": "2025-12-31"}
HEADER = ["State Name", "county Name", "State Code", "County Code", "Date", "AQI", "Category", "Defining Parameter", "Defining Site", "Number of Sites Reporting"]
CATEGORIES = ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"]
POLLUTANTS = ["CO", "NO2", "Ozone", "PM10", "PM2.5", "SO2"]
PLAN = ("file_list.csv", "FileFormats.html", *(f"daily_aqi_by_county_{year}.zip" for year in YEARS))
MAX_OBJECT, MAX_TOTAL, MAX_MEMBER = 8 * 1024**2, 32 * 1024**2, 96 * 1024**2
MAX_ROWS, MAX_DISPLAY = 1_500_000, 6 * 1024**2


def encoded(value):
    return (json.dumps(value, separators=(",", ":"), ensure_ascii=True) + "\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def private_path(folder):
    folder = Path(folder)
    if not folder.is_absolute() or folder.is_symlink():
        raise ValueError("Use an absolute, non-symlink capture directory outside Git.")
    resolved = folder.resolve()
    if any((parent / ".git").exists() for parent in (resolved, *resolved.parents)):
        raise ValueError("Original captures must stay outside Git checkouts.")
    return resolved


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("EPA capture redirects are not accepted.")


def capture(folder):
    folder = private_path(folder)
    if folder.exists():
        raise ValueError("Capture directory already exists; preserve it and choose a new one.")
    folder.mkdir(parents=True, mode=0o700)
    opener = urllib.request.build_opener(NoRedirect())
    total, sources = 0, {}
    for name in PLAN:
        url = BASE + name
        request = urllib.request.Request(url, headers={"User-Agent": "KFM-DailyAirQuality/1.0 (bounded public research capture)", "Accept-Encoding": "identity"})
        deadline = time.monotonic() + 90
        with opener.open(request, timeout=20) as response:
            if response.url != url or response.status != 200:
                raise ValueError("Unexpected EPA capture response.")
            chunks, size = [], 0
            while chunk := response.read(128 * 1024):
                size += len(chunk)
                total += len(chunk)
                if size > MAX_OBJECT or total > MAX_TOTAL or time.monotonic() > deadline:
                    raise ValueError("EPA capture exceeded its byte or time budget.")
                chunks.append(chunk)
            raw = b"".join(chunks)
            if not raw:
                raise ValueError("EPA returned an empty source.")
            target = folder / name
            with target.open("xb") as stream:
                stream.write(raw)
            target.chmod(0o600)
            sources[name] = {"url": url, "bytes": len(raw), "sha256": sha(raw),
                             "capturedAt": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
                             "lastModified": response.headers.get("Last-Modified")}
            print(f"Captured {name}: {len(raw):,} bytes", flush=True)
    target = folder / "capture.json"
    target.write_bytes(encoded({"schema": "kfm.daily-air-quality-capture/v1", "sources": sources}))
    target.chmod(0o600)


def verified_sources(folder):
    folder = private_path(folder)
    receipt = folder / "capture.json"
    if receipt.is_symlink() or not receipt.is_file() or receipt.stat().st_size > 64 * 1024:
        raise ValueError("Missing or oversized capture receipt.")
    capture_meta = json.loads(receipt.read_bytes())
    sources = capture_meta.get("sources")
    if capture_meta.get("schema") != "kfm.daily-air-quality-capture/v1" or not isinstance(sources, dict) or set(sources) != set(PLAN):
        raise ValueError("Unexpected EPA capture plan.")
    out, total = {}, 0
    for name in PLAN:
        path = folder / name
        if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_OBJECT:
            raise ValueError(f"Missing, linked or oversized source: {name}")
        raw, meta = path.read_bytes(), sources[name]
        total += len(raw)
        if total > MAX_TOTAL or not isinstance(meta, dict) or meta.get("url") != BASE + name or meta.get("bytes") != len(raw) or meta.get("sha256") != sha(raw):
            raise ValueError(f"Source integrity mismatch: {name}")
        if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", meta.get("capturedAt", "")):
            raise ValueError("Invalid capture time.")
        datetime.fromisoformat(meta["capturedAt"].replace("Z", "+00:00"))
        out[name] = (raw, meta)
    return out


def file_index(raw):
    reader = csv.reader(io.StringIO(raw.decode("utf-8-sig"), newline=""))
    if next(reader, None) != ["Filename", "Rows", "Size", "Created"]:
        raise ValueError("EPA file index columns changed.")
    wanted = set(PLAN[2:])
    found = {}
    for row in reader:
        if len(row) != 4:
            raise ValueError("Malformed EPA file index row.")
        if row[0] not in wanted:
            continue
        if row[0] in found or not row[1].isdigit() or not 0 < int(row[1]) <= MAX_ROWS or not re.fullmatch(r"\d{4}-\d\d-\d\d", row[3]):
            raise ValueError("Invalid or duplicate EPA file index entry.")
        date.fromisoformat(row[3])
        found[row[0]] = {"providerRows": int(row[1]), "providerCreated": row[3]}
    if set(found) != wanted:
        raise ValueError("EPA file index is incomplete.")
    return found


def category(aqi):
    return CATEGORIES[next((i for i, boundary in enumerate((50, 100, 150, 200, 300)) if aqi <= boundary), 5)]


def county_rows(raw, year, expected_rows):
    """Read the one bounded CSV without extracting an archive onto disk."""
    csv.field_size_limit(4096)
    for encoding in ("utf-8-sig", "latin-1"):
        try:
            with zipfile.ZipFile(io.BytesIO(raw)) as archive:
                members = archive.infolist()
                if (len(members) != 1 or members[0].filename != f"daily_aqi_by_county_{year}.csv"
                        or members[0].is_dir() or members[0].flag_bits & 1 or not 0 < members[0].file_size <= MAX_MEMBER):
                    raise ValueError("Unexpected or oversized EPA ZIP member.")
                with archive.open(members[0]) as binary, io.TextIOWrapper(binary, encoding=encoding, newline="") as stream:
                    reader = csv.reader(stream)
                    if next(reader, None) != HEADER:
                        raise ValueError("EPA daily county AQI columns changed.")
                    records, seen, national = [], set(), 0
                    for line, row in enumerate(reader, 2):
                        national += 1
                        if national > MAX_ROWS or len(row) != len(HEADER):
                            raise ValueError("Malformed or excessive EPA CSV rows.")
                        if row[2] != "20":
                            continue
                        state, name, _, code, day, raw_aqi, label, pollutant, site, raw_count = row
                        ordinal = int(code) if re.fullmatch(r"\d{3}", code) else 0
                        if (state != "Kansas" or not 1 <= ordinal <= 209 or ordinal % 2 != 1
                                or not re.fullmatch(r"[A-Za-z][A-Za-z .'-]{0,50}", name)
                                or not re.fullmatch(rf"{year}-\d\d-\d\d", day)):
                            raise ValueError("Unexpected Kansas county/date identity.")
                        date.fromisoformat(day)
                        if (not re.fullmatch(r"\d{1,5}", raw_aqi) or not 0 <= int(raw_aqi) <= 10000
                                or label != category(int(raw_aqi)) or pollutant not in POLLUTANTS
                                or not 1 <= len(site) <= 256 or not re.fullmatch(r"\d{2}-\d{3}-\d{4}(?:[,;| /]+\d{2}-\d{3}-\d{4})*", site)
                                or any(value[:2] + value[3:6] != "20" + code for value in re.findall(r"\d{2}-\d{3}-\d{4}", site))
                                or not re.fullmatch(r"\d{1,4}", raw_count) or not 1 <= int(raw_count) <= 1000):
                            raise ValueError(f"Invalid EPA daily AQI record: {year}/{code}/{day}")
                        identity = ("20" + code, day)
                        if identity in seen:
                            raise ValueError("Duplicate EPA county/date record.")
                        seen.add(identity)
                        records.append((identity[0], name, day, [raw_aqi, label, pollutant, site, raw_count, line]))
                    if national != expected_rows or not records:
                        raise ValueError("EPA index row count does not match the complete CSV.")
                    return records, encoding
        except UnicodeDecodeError:
            if encoding == "latin-1":
                raise
    raise ValueError("EPA CSV encoding could not be read.")


def build(sources):
    index = file_index(sources["file_list.csv"][0])
    dates = []
    day = date.fromisoformat(PERIOD["from"])
    while day.isoformat() <= PERIOD["to"]:
        dates.append(day.isoformat())
        day += timedelta(days=1)
    positions = {day: i for i, day in enumerate(dates)}
    counties, provenance, coverage = {}, [], {}
    for year in YEARS:
        name = f"daily_aqi_by_county_{year}.zip"
        raw, meta = sources[name]
        rows, encoding = county_rows(raw, year, index[name]["providerRows"])
        provenance.append({"year": year, **meta, **index[name], "encoding": encoding})
        coverage[str(year)] = {"reportedCountyDays": len(rows), "reportingCounties": len({r[0] for r in rows})}
        for fips, label, day, value in rows:
            county = counties.setdefault(fips, {"id": fips, "name": label + " County", "values": [None] * len(dates)})
            if county["name"] != label + " County" or county["values"][positions[day]] is not None:
                raise ValueError("Conflicting county identity or date.")
            county["values"][positions[day]] = value
    ordered = sorted(counties.values(), key=lambda c: c["id"])
    snapshot = {"schema": "kfm.daily-air-quality/v1", "period": PERIOD, "provider": "U.S. EPA AirData AQS",
                "scope": "provider-context", "dates": dates, "sources": provenance, "counties": ordered}
    raw = encoded(snapshot)
    if len(raw) > MAX_DISPLAY:
        raise ValueError("Kansas display snapshot exceeds its size budget.")
    digest = sha(raw)
    manifest = {"schema": "kfm.daily-air-quality-manifest/v1", "provider": snapshot["provider"], "period": PERIOD,
                "scope": "provider-context", "review": "PENDING", "admission": "PENDING", "release": "UNRELEASED",
                "documentation": "https://www.epa.gov/outdoor-air-quality-data/about-airdata-reports",
                "categoryDocumentation": "https://www.epa.gov/outdoor-air-quality-data/airdata-basic-information",
                "rights": "https://edg.epa.gov/EPA_Data_License.html", "sources": provenance,
                "fileIndexSource": sources["file_list.csv"][1], "documentationSource": sources["FileFormats.html"][1],
                "snapshot": {"id": "kansas", "url": f"/science-data/daily-air-quality/kansas-{digest[:16]}.json",
                             "sha256": digest, "bytes": len(raw), "records": sum(v["reportedCountyDays"] for v in coverage.values()),
                             "calendarDates": len(dates)},
                "counties": [{"id": c["id"], "name": c["name"], "reportedDays": sum(v is not None for v in c["values"])} for c in ordered],
                "coverageByYear": coverage, "generatedAt": max(source["capturedAt"] for source in provenance)}
    return raw, manifest


def prepare(folder):
    raw, manifest = build(verified_sources(folder))
    targets = [(ROOT / "public" / manifest["snapshot"]["url"].lstrip("/"), raw),
               (ROOT / "app/labs/daily-air-quality/snapshot-manifest.json", encoded(manifest))]
    # Validate everything before writing either derived artifact. Originals are
    # immutable; content-hashed old display files are never removed here.
    for path, body in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)
    print(f"Prepared {manifest['snapshot']['records']:,} reported county-days across {len(manifest['counties'])} reporting counties.")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--capture-dir", type=Path)
    group.add_argument("--source-dir", type=Path)
    args = parser.parse_args()
    folder = args.capture_dir or args.source_dir
    if args.capture_dir:
        capture(folder)
    prepare(folder)


if __name__ == "__main__":
    main()
