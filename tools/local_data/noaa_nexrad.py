#!/usr/bin/env python3
"""Bounded Kansas NEXRAD Level III storm-product capture to the private KFM store.

Captures only the small NST (storm tracks) and NMD (rotation) products for one
UTC day and an optional hour window. Listings are planned first so the byte
total is known and checked against a hard storage cap before anything is
downloaded. Nothing here admits, releases or publishes data.
"""
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
from connectors.noaa.src.noaa import nexrad_level3 as source
from tools.local_data.file_io import check_directory, hash_regular, read_regular, write_new
from tools.local_data.manage import canonical, external_root, initialized, store_lock

LANE = "noaa-nexrad-l3"
DEFAULT_CAP = 64 * source.MIB
DEFAULT_RESERVE = 20 * 1024**3
REPORT_RESERVE = 8 * source.MIB
BLOCK = 4096
MAX_PRODUCTS = 6000
BATCH = 50
RUN = re.compile(r"[0-9]{8}T[0-9]{6}Z\Z")


def paths(root, run):
    if not RUN.fullmatch(run):
        raise ValueError("RUN_ID_INVALID")
    return (root / "data/raw" / LANE / run, root / "data/work" / LANE / run,
            root / "data/receipts/ingest" / LANE / run)


def check_root(root):
    if not initialized(root) or root.stat().st_mode & 0o077:
        raise ValueError("PRIVATE_INITIALIZED_STORE_REQUIRED")


def usage(root):
    """Count every retained file in this source's lanes, rounded to disk blocks."""
    count = 0
    for lane in ("raw/" + LANE, "work/" + LANE, "receipts/ingest/" + LANE):
        base = root / "data" / lane
        if not base.exists() and not base.is_symlink():
            continue
        check_directory(base)
        for directory, dirs, files in os.walk(base, followlinks=False):
            for name in dirs:
                check_directory(Path(directory) / name)
            for name in files:
                info = (Path(directory) / name).lstat()
                if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                    raise ValueError("SOURCE_STORE_UNSAFE_FILE")
                count += max(info.st_size, getattr(info, "st_blocks", 0) * 512)
    return count


def on_disk(size):
    return max(BLOCK, -(-size // BLOCK) * BLOCK)


def room(root, used, additional, cap, reserve):
    if used + additional + REPORT_RESERVE > cap:
        raise ValueError("SOURCE_STORAGE_CAP")
    if shutil.disk_usage(root).free < additional + reserve + REPORT_RESERVE:
        raise ValueError("FREE_SPACE_RESERVE")


def selection(radars, products, start_hour, hours):
    radars, products = tuple(radars), tuple(products)
    if not radars or len(set(radars)) != len(radars) or any(r not in source.RADARS for r in radars):
        raise ValueError("RADAR_SELECTION_INVALID")
    if not products or len(set(products)) != len(products) or any(p not in source.PRODUCTS for p in products):
        raise ValueError("PRODUCT_SELECTION_INVALID")
    if not (0 <= start_hour <= 23 and 1 <= hours <= 24 and start_hour + hours <= 24):
        raise ValueError("HOUR_WINDOW_INVALID")
    return radars, products


def load_plan(root, run):
    _, work, _ = paths(root, run)
    plan = json.loads(read_regular(work / "plan.json", 4 * source.MIB))
    if plan.get("run") != run or plan.get("format") != "kfm-nexrad-l3-local-plan-v1":
        raise ValueError("PLAN_IDENTITY")
    return plan


def prepare(root, run, day, radars=source.KANSAS_RADARS, products=("NST", "NMD"), start_hour=0, hours=24,
            cap=DEFAULT_CAP, reserve=DEFAULT_RESERVE, getter=source.get):
    """List exact keys and sizes; download no product bytes."""
    check_root(root)
    day = source.check_day(day)
    radars, products = selection(radars, products, start_hour, hours)
    _, work, _ = paths(root, run)
    with store_lock(root):
        if (work / "plan.json").exists():
            return load_plan(root, run)
        room(root, usage(root), 0, cap, reserve)
        selected, listings = [], []
        for radar in radars:
            for product in products:
                rows = source.list_day(radar, product, day, getter=getter)
                kept = [row for row in rows if start_hour <= int(row["volume_time"][11:13]) < start_hour + hours]
                listings.append({"radar": radar, "product": product, "listed": len(rows), "selected": len(kept),
                                 "request": source.list_url(radar, product, day)})
                selected.extend(kept)
        if len(selected) > MAX_PRODUCTS:
            raise ValueError("PRODUCT_COUNT_LIMIT")
        selected_bytes = sum(row["bytes"] for row in selected)
        disk_bytes = sum(on_disk(row["bytes"]) for row in selected)
        # Receipts are written in batches, so allow one block per batch plus revisions.
        room(root, usage(root), int(disk_bytes * 1.05) + (len(selected) // BATCH + 2) * BLOCK * 2, cap, reserve)
        plan = {"format": "kfm-nexrad-l3-local-plan-v1", "run": run, "day": day, "utc_hours": [start_hour, start_hour + hours],
                "radars": [source.RADARS[r] | {"id": r} for r in radars], "products": list(products),
                "source_page": source.SOURCE_PAGE, "source_bucket": source.BUCKET, "created_at": source.utc_now(),
                "storage_cap_bytes": cap, "minimum_free_bytes": reserve, "selected_products": len(selected),
                "selected_product_bytes": selected_bytes, "estimated_disk_bytes": disk_bytes,
                "listings": listings, "objects": sorted(selected, key=lambda row: row["key"]),
                "source_admitted": False, "released": False, "published": False}
        write_new(work / "plan.json", canonical(plan))
        return plan


def receipted(root, run, plan):
    raw, _, receipts = paths(root, run)
    planned = {row["key"]: row for row in plan["objects"]}
    refs = {}
    batches = receipts / "batches"
    if batches.exists():
        check_directory(batches)
        for name in sorted(os.listdir(batches)):
            if not re.fullmatch(r"\d{5}\.json", name):
                raise ValueError("RECEIPT_NAME_INVALID")
            for ref in json.loads(read_regular(batches / name, 4 * source.MIB)):
                if ref["key"] not in planned or ref["key"] in refs or ref["path"] != str((raw / ref["key"]).relative_to(root)):
                    raise ValueError("RECEIPT_IDENTITY")
                refs[ref["key"]] = ref
    return refs


def verified(root, ref):
    relative = Path(ref["path"])
    if relative.is_absolute() or ".." in relative.parts or relative.parts[:3] != ("data", "raw", LANE):
        raise ValueError("CAPTURE_PATH_INVALID")
    digest, _ = hash_regular(root / relative, source.PRODUCT_BYTES, expected_size=ref["bytes"])
    if digest != ref["sha256"]:
        raise ValueError("CAPTURE_HASH_MISMATCH")
    return read_regular(root / relative, source.PRODUCT_BYTES)


def capture(root, run, fetcher=source.fetch, cap=DEFAULT_CAP, reserve=DEFAULT_RESERVE, deadline=1800):
    check_root(root)
    raw, _, receipts = paths(root, run)
    started = time.monotonic()
    with store_lock(root):
        plan = load_plan(root, run)
        cap, reserve = min(cap, plan["storage_cap_bytes"]), max(reserve, plan["minimum_free_bytes"])
        refs = receipted(root, run, plan)
        pending = []
        for row in plan["objects"]:
            if row["key"] in refs:
                continue
            if (raw / row["key"]).exists():
                raise ValueError("UNRECEIPTED_CAPTURE_REQUIRES_INSPECTION")
            pending.append(row)
        used, failures = usage(root), []
        batch_number = len(os.listdir(receipts / "batches")) if (receipts / "batches").exists() else 0

        def retrieve(row):
            try:
                body, header = fetcher(row["key"], source.PRODUCT_BYTES)
                parsed = source.parse_product(body, row["key"])
                return row, body, header, parsed, None
            except (OSError, ValueError, EOFError, UnicodeDecodeError) as error:
                return row, None, None, None, f"{type(error).__name__}:{error}"[:120]

        # Four small in-flight requests; no unbounded queue and no automatic retries.
        with ThreadPoolExecutor(max_workers=4) as pool:
            for offset in range(0, len(pending), BATCH):
                if time.monotonic() - started > deadline:
                    failures.append({"key": None, "error_type": "CAPTURE_DEADLINE"})
                    break
                chunk = pending[offset:offset + BATCH]
                room(root, used, sum(on_disk(row["bytes"]) for row in chunk) + 2 * BLOCK, cap, reserve)
                batch = []
                for row, body, header, parsed, error in pool.map(retrieve, chunk):
                    if error:
                        failures.append({"key": row["key"], "error_type": error})
                        continue
                    write_new(raw / row["key"], body)
                    used += on_disk(len(body))
                    batch.append({**header, "key": row["key"], "path": str((raw / row["key"]).relative_to(root)),
                                  "bytes": len(body), "sha256": sha256(body).hexdigest(),
                                  "checksum_role": "captured-byte-identity-only", "listed_bytes": row["bytes"],
                                  "volume_time": parsed["volume_time"], "detections": len(parsed["detections"])})
                if batch:
                    body = canonical(batch)
                    write_new(receipts / "batches" / f"{batch_number:05d}.json", body)
                    used += on_disk(len(body))
                    batch_number += 1
                    refs.update({ref["key"]: ref for ref in batch})
                print(json.dumps({"captured": len(refs), "selected": plan["selected_products"], "failures": len(failures)}), flush=True)
        report = {"format": "kfm-nexrad-l3-local-capture-v1", "run": run, "finished_at": source.utc_now(),
                  "status": "CAPTURED_UNREVIEWED" if len(refs) == plan["selected_products"] else "PARTIAL",
                  "selected_products": plan["selected_products"], "captured_products": len(refs),
                  "captured_bytes": sum(ref["bytes"] for ref in refs.values()),
                  "retained_disk_bytes": usage(root), "storage_cap_bytes": cap, "minimum_free_bytes": reserve,
                  "free_bytes_after": shutil.disk_usage(root).free, "failures": failures[:200], "failure_count": len(failures),
                  "source_admitted": False, "reviewed": False, "released": False, "published": False}
        attempt = source.utc_now().replace("-", "").replace(":", "")
        write_new(receipts / f"capture-{attempt}.json", canonical(report))
        return report


def summarize(parsed):
    cells = [d for p in parsed for d in p["detections"] if d["kind"] == "storm_cell"]
    rotations = [d for p in parsed for d in p["detections"] if d["kind"] == "rotation"]
    classes = {}
    for item in rotations:
        classes[item["rotation_class"]] = classes.get(item["rotation_class"], 0) + 1
    times = sorted(p["volume_time"] for p in parsed)
    return {"products": len(parsed), "storm_cell_detections": len(cells), "rotation_detections": len(rotations),
            "rotation_classes": dict(sorted(classes.items())), "first_volume": times[0] if times else None,
            "last_volume": times[-1] if times else None}


def verify(root, run):
    check_root(root)
    _, work, _ = paths(root, run)
    plan = load_plan(root, run)
    refs = receipted(root, run, plan)
    parsed, missing = [], []
    for row in plan["objects"]:
        ref = refs.get(row["key"])
        if ref is None:
            missing.append(row["key"])
            continue
        # Re-hash and independently re-parse every retained original.
        result = source.parse_product(verified(root, ref), row["key"])
        if result["volume_time"] != ref["volume_time"] or len(result["detections"]) != ref["detections"]:
            raise ValueError("CAPTURE_PARSE_MISMATCH")
        parsed.append(result)
    collection = source.feature_collection(parsed, f"Kansas NEXRAD storm detections {plan['day']}")
    collection["summary"] = summarize(parsed)
    body = canonical(collection)
    name = "storm-detections-" + sha256(body).hexdigest()[:16] + ".geojson"
    with store_lock(root):
        room(root, usage(root), on_disk(len(body)), plan["storage_cap_bytes"], plan["minimum_free_bytes"])
        if (work / name).exists():
            if read_regular(work / name, 64 * source.MIB) != body:
                raise ValueError("INDEX_CONFLICT")
        else:
            write_new(work / name, body)
        # The index is derived and reproducible from RAW; keep only the newest
        # one so repeated verification never accumulates storage.
        for stale in work.glob("storm-detections-*.geojson"):
            if stale.name != name and stale.is_file() and not stale.is_symlink():
                stale.unlink()
    return {"status": "VERIFIED_CAPTURE" if not missing else "PARTIAL", **collection["summary"],
            "missing": missing[:50], "missing_count": len(missing), "index": str(work / name),
            "index_bytes": len(body), "retained_disk_bytes": usage(root), "storage_cap_bytes": plan["storage_cap_bytes"],
            "source_admitted": False, "released": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("operation", choices=("prepare", "capture", "verify"))
    parser.add_argument("--root", required=True)
    parser.add_argument("--run", required=True)
    parser.add_argument("--day", help="UTC day for prepare, e.g. 2024-05-19")
    parser.add_argument("--radars", default=",".join(source.KANSAS_RADARS), help="comma list from: " + ",".join(source.RADARS))
    parser.add_argument("--products", default="NST,NMD")
    parser.add_argument("--start-hour", type=int, default=0)
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--cap-mib", type=int, default=DEFAULT_CAP // source.MIB)
    args = parser.parse_args(argv)
    root = external_root(args.root)
    cap = args.cap_mib * source.MIB
    if not 1 <= args.cap_mib <= 1024:
        parser.error("--cap-mib must be between 1 and 1024")
    if args.operation == "prepare":
        if not args.day:
            parser.error("prepare requires --day")
        plan = prepare(root, args.run, args.day, args.radars.split(","), args.products.split(","), args.start_hour, args.hours, cap=cap)
        result = {key: plan[key] for key in ("run", "day", "utc_hours", "selected_products", "selected_product_bytes",
                                             "estimated_disk_bytes", "storage_cap_bytes")}
    elif args.operation == "capture":
        result = capture(root, args.run, cap=cap)
    else:
        result = verify(root, args.run)
    print(json.dumps(result, indent=2))
    return 2 if result.get("status") == "PARTIAL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
