#!/usr/bin/env python3
"""Bounded Kansas GHCN Daily capture to the existing private KFM store."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from connectors.noaa.src.noaa import ghcnd as source
from tools.local_data.file_io import check_directory, hash_regular, read_regular, write_new
from tools.local_data.manage import canonical, external_root, initialized, store_lock

DEFAULT_CAP = 384*source.MIB
DEFAULT_RESERVE = 100*1024**3
REPORT_RESERVE = 16*source.MIB
RUN = re.compile(r"[0-9]{8}T[0-9]{6}Z\Z")


def paths(root, run):
    if not RUN.fullmatch(run):
        raise ValueError("RUN_ID_INVALID")
    return (root / "data/raw/noaa-ghcnd" / run,
            root / "data/work/noaa-ghcnd" / run,
            root / "data/receipts/ingest/noaa-ghcnd" / run)


def check_root(root):
    if not initialized(root) or root.stat().st_mode & 0o077:
        raise ValueError("PRIVATE_INITIALIZED_STORE_REQUIRED")


def usage(root):
    """Count all retained runs and metadata, including unknown files and blocks."""
    count = 0
    for lane in ("raw/noaa-ghcnd", "work/noaa-ghcnd", "receipts/ingest/noaa-ghcnd"):
        base = root / "data" / lane
        if not base.exists() and not base.is_symlink():
            continue
        check_directory(base)
        for directory, dirs, files in os.walk(base, followlinks=False):
            for name in dirs:
                check_directory(Path(directory)/name)
            for name in files:
                info = (Path(directory)/name).lstat()
                if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                    raise ValueError("SOURCE_STORE_UNSAFE_FILE")
                count += max(info.st_size, getattr(info, "st_blocks", 0)*512)
    return count


def room(root, used, additional, cap, reserve):
    if used + additional + REPORT_RESERVE > cap:
        raise ValueError("SOURCE_STORAGE_CAP")
    if shutil.disk_usage(root).free < additional + reserve + REPORT_RESERVE:
        raise ValueError("FREE_SPACE_RESERVE")


def verified(root, ref):
    relative = Path(ref["path"])
    if relative.is_absolute() or ".." in relative.parts or not str(relative).startswith("data/raw/noaa-ghcnd/"):
        raise ValueError("CAPTURE_PATH_INVALID")
    digest, size = hash_regular(root/relative, max(source.METADATA.values()), expected_size=ref["bytes"])
    if digest != ref["sha256"]:
        raise ValueError("CAPTURE_HASH_MISMATCH")
    return size


def save(root, path, body, header):
    write_new(path, body)
    return {**header, "path": str(path.relative_to(root)), "bytes": len(body),
            "sha256": sha256(body).hexdigest(), "checksum_role": "captured-byte-identity-only"}


def load_plan(root, run):
    _, work, _ = paths(root, run)
    plan = json.loads(read_regular(work/"plan.json", 8*source.MIB))
    if plan["run"] != run or plan["scope"] != "Kansas state code KS":
        raise ValueError("PLAN_IDENTITY")
    for ref in plan["metadata"]:
        verified(root, ref)
    return plan


def prepare(root, run, cap=DEFAULT_CAP, reserve=DEFAULT_RESERVE, fetcher=source.fetch):
    check_root(root)
    raw, work, receipts = paths(root, run)
    with store_lock(root):
        if (work/"plan.json").exists():
            return load_plan(root, run)
        used = usage(root)
        room(root, used, sum(source.METADATA.values()), cap, reserve)
        refs, bodies = [], {}
        for key, bound in source.METADATA.items():
            name = "by-station.html" if key == "by_station/" else key
            receipt = receipts/"metadata"/(name+".json")
            if receipt.exists():
                ref = json.loads(read_regular(receipt, source.MIB))
                if ref["path"] != str((raw/"metadata"/name).relative_to(root)) or ref["source_url"] != source.object_url(key):
                    raise ValueError("METADATA_RECEIPT_IDENTITY")
                verified(root, ref)
                body = read_regular(root/ref["path"], bound)
            else:
                if (raw/"metadata"/name).exists():
                    raise ValueError("UNRECEIPTED_CAPTURE_REQUIRES_INSPECTION")
                body, header = fetcher(key, bound)
                if not 0 < len(body) <= bound:
                    raise ValueError("METADATA_SIZE_LIMIT")
                ref = save(root, raw/"metadata"/name, body, header)
                write_new(receipt, canonical(ref))
            refs.append(ref)
            bodies[key] = body
        stations = source.kansas_stations(bodies["ghcnd-stations.txt"])
        sizes = source.listed_sizes(bodies["by_station/"])
        ranges = source.inventory_ranges(bodies["ghcnd-inventory.txt"], stations)
        missing = sorted(set(stations)-set(sizes))
        if missing:
            raise ValueError("STATION_DIRECTORY_INCOMPLETE")
        for sid, station in stations.items():
            if not 0 < sizes[sid] <= source.STATION_BYTES:
                raise ValueError("STATION_LISTED_SIZE_LIMIT")
            station.update(listed_bytes=sizes[sid], inventory_elements=ranges[sid])
        selected_bytes = sum(sizes[sid] for sid in stations)
        used = usage(root)
        # Allow filesystem block rounding, per-station receipts, and a small source revision margin.
        room(root, used, int(selected_bytes*1.05)+len(stations)*8192, cap, reserve)
        plan = {"format": "kfm-ghcnd-local-plan-v1", "run": run,
                "scope": "Kansas state code KS", "created_at": source.utc_now(),
                "storage_cap_bytes": cap, "minimum_free_bytes": reserve,
                "selected_station_bytes": selected_bytes, "metadata": refs,
                "stations": [stations[sid] for sid in sorted(stations)],
                "source_admitted": False, "released": False, "published": False}
        write_new(work/"plan.json", canonical(plan))
        return plan


def capture(root, run, fetcher=source.fetch, cap=DEFAULT_CAP, reserve=DEFAULT_RESERVE):
    check_root(root)
    raw, work, receipts = paths(root, run)
    started = time.monotonic()
    with store_lock(root):
        plan = load_plan(root, run)
        cap, reserve = min(cap, plan["storage_cap_bytes"]), max(reserve, plan["minimum_free_bytes"])
        used = usage(root)
        entries, pending, failures = [], [], []
        for station in plan["stations"]:
            sid = station["station_id"]
            if not source.STATION.fullmatch(sid):
                raise ValueError("PLAN_STATION_INVALID")
            record = receipts/"stations"/(sid+".json")
            if record.exists():
                ref = json.loads(read_regular(record, source.MIB))
                if ref["station_id"] != sid or ref["source_url"] != source.object_url("by_station/"+sid+".csv.gz"):
                    raise ValueError("STATION_RECEIPT_IDENTITY")
                if ref["path"] != str((raw/"stations"/(sid+".csv.gz")).relative_to(root)):
                    raise ValueError("STATION_RECEIPT_PATH")
                verified(root, ref)
                entries.append(ref)
            else:
                if (raw/"stations"/(sid+".csv.gz")).exists():
                    raise ValueError("UNRECEIPTED_CAPTURE_REQUIRES_INSPECTION")
                pending.append(station)
        room(root, used, 2*source.STATION_BYTES, cap, reserve)

        def retrieve(station):
            sid = station["station_id"]
            try:
                body, header = fetcher("by_station/"+sid+".csv.gz", source.STATION_BYTES)
                inspection = source.inspect_station(body, sid)
                return station, body, header, inspection, None
            except (OSError, ValueError, EOFError) as error:
                return station, None, None, None, type(error).__name__

        # Only two in-flight requests; no unbounded executor queue or automatic retries.
        with ThreadPoolExecutor(max_workers=2) as pool:
            for offset in range(0, len(pending), 2):
                if time.monotonic()-started > 1800:
                    raise ValueError("CAPTURE_DEADLINE")
                room(root, used, 2*source.STATION_BYTES, cap, reserve)
                for station, body, header, inspection, error in pool.map(retrieve, pending[offset:offset+2]):
                    sid = station["station_id"]
                    if error:
                        failures.append({"station_id": sid, "error_type": error})
                        continue
                    room(root, used, len(body)+8192, cap, reserve)
                    ref = {**save(root, raw/"stations"/(sid+".csv.gz"), body, header),
                           "station_id": sid, "inspection": inspection,
                           "listed_bytes_at_planning": station["listed_bytes"]}
                    write_new(receipts/"stations"/(sid+".json"), canonical(ref))
                    entries.append(ref)
                    used += ((len(body)+4095)//4096)*4096+8192
                if offset % 50 == 0:
                    print(json.dumps({"captured": len(entries), "selected": len(plan["stations"]),
                                      "failures": len(failures)}), flush=True)
                time.sleep(0.05)
        entries.sort(key=lambda row: row["station_id"])
        report = {"format": "kfm-ghcnd-local-capture-v1", "run": run, "finished_at": source.utc_now(),
                  "status": "CAPTURED_UNREVIEWED" if len(entries) == len(plan["stations"]) else "PARTIAL",
                  "selected_stations": len(plan["stations"]), "captured_stations": len(entries),
                  "compressed_station_bytes": sum(e["bytes"] for e in entries),
                  "observation_rows": sum(e["inspection"]["rows"] for e in entries),
                  "first_date": min((e["inspection"]["first_date"] for e in entries), default=None),
                  "last_date": max((e["inspection"]["last_date"] for e in entries), default=None),
                  "storage_cap_bytes": cap, "minimum_free_bytes": reserve,
                  "free_bytes_after": shutil.disk_usage(root).free, "failures": failures,
                  "source_admitted": False, "reviewed": False, "released": False, "published": False,
                  "metadata": plan["metadata"], "stations": entries}
        # Each attempt is immutable; a retry never overwrites a previous partial report.
        attempt = source.utc_now().replace("-", "").replace(":", "")
        write_new(receipts/("capture-"+attempt+".json"), canonical(report))
        return report


def verify(root, run):
    check_root(root)
    raw, work, receipts = paths(root, run)
    plan = load_plan(root, run)
    features, missing, rows = [], [], 0
    for station in plan["stations"]:
        sid = station["station_id"]
        receipt = receipts/"stations"/(sid+".json")
        if not receipt.exists():
            missing.append(sid)
            continue
        ref = json.loads(read_regular(receipt, source.MIB))
        if ref["path"] != str((raw/"stations"/(sid+".csv.gz")).relative_to(root)):
            raise ValueError("STATION_RECEIPT_PATH")
        verified(root, ref)
        # Independently re-read every compressed stream and compare the saved inspection.
        inspection = source.inspect_station(read_regular(root/ref["path"], source.STATION_BYTES), sid)
        if inspection != ref["inspection"]:
            raise ValueError("STATION_INSPECTION_MISMATCH")
        rows += inspection["rows"]
        features.append({"type": "Feature", "id": sid,
                         "geometry": {"type": "Point", "coordinates": [station["longitude"], station["latitude"]]},
                         "properties": {**station, "first_date": inspection["first_date"],
                                        "last_date": inspection["last_date"], "observation_rows": inspection["rows"],
                                        "quality_flagged_rows": inspection["rows"]-inspection["quality_flags"].get("blank", 0),
                                        "source_url": ref["source_url"], "sha256": ref["sha256"],
                                        "local_raw_path": ref["path"], "review_status": "unreviewed"}})
    preview = {"type": "FeatureCollection", "name": "Kansas GHCN Daily capture index",
               "source_admitted": False, "released": False, "features": features}
    body = canonical(preview)
    name = "station-index-"+sha256(body).hexdigest()[:16]+".geojson"
    with store_lock(root):
        room(root, usage(root), len(body), plan["storage_cap_bytes"], plan["minimum_free_bytes"])
        if (work/name).exists():
            if read_regular(work/name, 8*source.MIB) != body:
                raise ValueError("INDEX_CONFLICT")
        else:
            write_new(work/name, body)
    return {"status": "VERIFIED_CAPTURE" if not missing else "PARTIAL", "stations": len(features),
            "missing": missing, "rows_checked": rows, "index": str(work/name),
            "retained_disk_bytes": usage(root), "free_disk_bytes": shutil.disk_usage(root).free,
            "source_admitted": False, "released": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("prepare", "capture", "verify"))
    parser.add_argument("--root", required=True)
    parser.add_argument("--run", required=True)
    args = parser.parse_args()
    result = globals()[args.operation](external_root(args.root), args.run)
    if args.operation == "prepare":
        result = {key: result[key] for key in ("run", "selected_station_bytes", "storage_cap_bytes", "minimum_free_bytes")} | {
            "station_count": len(result["stations"])}
    elif args.operation == "capture":
        result = {key: value for key, value in result.items() if key not in {"stations", "metadata"}}
    print(json.dumps(result, indent=2))
    return 2 if result.get("status") == "PARTIAL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
