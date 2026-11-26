#!/usr/bin/env python3
"""Prepare bounded, source-qualified NOAA display snapshots; no source admission.

Capture originals outside Git, then reproduce derivatives without a network:
  python3 scripts/prepare-daily-climate.py --capture-dir /private/new/capture
  python3 scripts/prepare-daily-climate.py --source-dir /private/new/capture
"""
from __future__ import annotations

import argparse
import calendar
from datetime import date, datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/"
STATIONS = ("USW00013985", "USW00003928", "USW00013996")
FROM, TO = date(2020, 1, 1), date(2025, 12, 31)
ELEMENTS = ("TMAX", "TMIN", "PRCP")
MAX_SOURCE = 24 * 1024 * 1024
MAX_CAPTURE = 64 * 1024 * 1024
PROFILE = "kfm.daily-climate/v1"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, separators=(",", ":"), ensure_ascii=True) + "\n").encode()


def capture(directory):
    directory = directory.resolve()
    if directory.is_relative_to(ROOT) or directory.exists():
        raise ValueError("Capture must use a new directory outside application source.")
    directory.mkdir(mode=0o700, parents=True)
    captured = {}
    total = 0
    names = ["ghcnd-stations.txt", "ghcnd-version.txt", "readme.txt"] + [f"all/{sid}.dly" for sid in STATIONS]
    for name in names:
        url = BASE + name
        request = urllib.request.Request(url, headers={"User-Agent": "KFM-DailyClimate/1.0 (bounded public research capture)"})
        with urllib.request.urlopen(request, timeout=30) as response:
            final = urllib.parse.urlparse(response.url)
            if final.scheme != "https" or final.hostname != "www.ncei.noaa.gov":
                raise ValueError("Unexpected source redirect.")
            chunks, length = [], 0
            while chunk := response.read(256 * 1024):
                length += len(chunk)
                total += len(chunk)
                if length > MAX_SOURCE or total > MAX_CAPTURE:
                    raise ValueError("NOAA capture exceeded the byte budget.")
                chunks.append(chunk)
            raw = b"".join(chunks)
            target = directory / Path(name).name
            with target.open("xb") as output:
                output.write(raw)
            target.chmod(0o600)
            captured[target.name] = {"url": url, "sha256": sha(raw), "bytes": len(raw),
                "capturedAt": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
                "lastModified": response.headers.get("Last-Modified")}
        print(f"Captured {name}: {length:,} bytes")
    (directory / "capture.json").write_bytes(encoded({"schema": "kfm.daily-climate-capture/v1", "sources": captured}))
    (directory / "capture.json").chmod(0o600)


def read_verified(directory, name, receipt):
    path = directory / name
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_SOURCE:
        raise ValueError(f"Unavailable or oversized captured input: {name}")
    raw = path.read_bytes()
    meta = receipt["sources"][name]
    expected_url = BASE + ("all/" if name.endswith(".dly") else "") + name
    if meta["url"] != expected_url or meta["bytes"] != len(raw) or meta["sha256"] != sha(raw):
        raise ValueError(f"Captured bytes do not match their receipt: {name}")
    datetime.fromisoformat(meta["capturedAt"].replace("Z", "+00:00"))
    return raw, meta


def metadata(raw):
    stations = {}
    for line in raw.decode("ascii").splitlines():
        if line[:11] not in STATIONS:
            continue
        sid, lat, lon = line[:11], float(line[12:20]), float(line[21:30])
        if sid in stations:
            raise ValueError("Duplicate station metadata.")
        if line[38:40] != "KS" or not (36.9 <= lat <= 40.1 and -102.1 <= lon <= -94.5):
            raise ValueError("Station metadata is outside Kansas.")
        stations[sid] = {"id": sid, "name": line[41:71].strip(), "latitude": lat,
            "longitude": lon, "elevationM": float(line[31:37])}
    if set(stations) != set(STATIONS):
        raise ValueError("Missing or duplicate Kansas station metadata.")
    return stations


def parse_station(raw, station_id):
    by_date = {}
    seen = set()
    for line in raw.decode("ascii").splitlines():
        if len(line) != 269 or line[:11] != station_id:
            raise ValueError("Invalid station or fixed-width NOAA record.")
        year, month, element = int(line[11:15]), int(line[15:17]), line[17:21]
        if not 1 <= month <= 12:
            raise ValueError("Invalid NOAA month.")
        if year < FROM.year or year > TO.year or element not in ELEMENTS:
            continue
        key = (year, month, element)
        if key in seen:
            raise ValueError("Duplicate station/month/element; no implicit revision selection.")
        seen.add(key)
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            offset = 21 + (day - 1) * 8
            value, flags = line[offset:offset + 5], line[offset + 5:offset + 8]
            if not re.fullmatch(r" *-?\d+", value) or any(ord(flag) < 32 or ord(flag) > 126 for flag in flags):
                raise ValueError("Invalid NOAA value or flag.")
            by_date.setdefault(date(year, month, day).isoformat(), {})[element.lower()] = [int(value), *[flag.strip() for flag in flags]]
    rows, current = [], FROM
    while current <= TO:
        day = current.isoformat()
        rows.append({"date": day, **{element.lower(): by_date.get(day, {}).get(element.lower()) for element in ELEMENTS}})
        current += timedelta(days=1)
    if not seen:
        raise ValueError("No selected NOAA records.")
    return rows


def prepare(directory, output_root=ROOT):
    receipt = json.loads((directory / "capture.json").read_text())
    if receipt.get("schema") != "kfm.daily-climate-capture/v1":
        raise ValueError("Unsupported capture receipt.")
    station_raw, station_source = read_verified(directory, "ghcnd-stations.txt", receipt)
    version_raw, version_source = read_verified(directory, "ghcnd-version.txt", receipt)
    _, docs_source = read_verified(directory, "readme.txt", receipt)
    stations = metadata(station_raw)
    target = output_root / "public/science-data/daily-climate"
    target.mkdir(parents=True, exist_ok=True)
    version = re.search(r"\b\d+\.\d+-upd-\d{10}\b", version_raw.decode("ascii"))
    if version is None:
        raise ValueError("Unrecognized NOAA GHCN-Daily version record.")
    manifest = {"schema": "kfm.daily-climate-manifest/v1", "provider": "NOAA NCEI GHCN-Daily",
        "version": version.group(), "documentation": BASE + "readme.txt",
        "scope": "provider-context", "period": {"from": FROM.isoformat(), "to": TO.isoformat()},
        "rights": "NOAA public US station observations; retain source attribution. No KFM admission or release implied.",
        "metadataSource": station_source, "versionSource": version_source, "documentationSource": docs_source,
        "stations": []}
    for sid in STATIONS:
        raw, source = read_verified(directory, sid + ".dly", receipt)
        snapshot = {"schema": PROFILE, "station": stations[sid], "period": manifest["period"],
            "source": source, "records": parse_station(raw, sid)}
        content = encoded(snapshot)
        digest = sha(content)
        name = f"{sid.lower()}-{digest[:16]}.json"
        path = target / name
        if path.exists() and path.read_bytes() != content:
            raise ValueError("Existing snapshot name has different bytes.")
        path.write_bytes(content)
        manifest["stations"].append({**stations[sid], "url": "/science-data/daily-climate/" + name,
            "sha256": digest, "bytes": len(content), "records": len(snapshot["records"]), "source": source})
    manifest["generatedAt"] = max(item["source"]["capturedAt"] for item in manifest["stations"])
    manifest_path = output_root / "app/labs/heat-and-rain/snapshot-manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_bytes(encoded(manifest))
    print(json.dumps({"stations": len(STATIONS), "daysPerStation": len(snapshot["records"]),
        "displayBytes": sum(item["bytes"] for item in manifest["stations"]), "manifest": str(manifest_path)}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--capture-dir", type=Path, help="New private directory outside Git; captures six fixed NOAA objects.")
    mode.add_argument("--source-dir", type=Path, help="Existing captured bytes and receipt; prepares display derivatives offline.")
    args = parser.parse_args()
    if args.capture_dir:
        capture(args.capture_dir)
        print("Capture complete. Run --source-dir on this directory to prepare display snapshots.")
    else:
        prepare(args.source_dir)
