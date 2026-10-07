#!/usr/bin/env python3
"""Explicit, size-limited NWM capture in the private external KFM store."""
from __future__ import annotations

import argparse
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
from connectors.noaa.src.noaa import nwm as source
from tools.local_data.file_io import check_directory, hash_regular, read_regular, write_new
from tools.local_data.manage import canonical, external_root, initialized, store_lock

CAP = 512*source.MIB
RESERVE = 100*1024**3
REPORT_RESERVE = 8*source.MIB
GEOMETRY_CAP = 192*source.MIB
WORK_CAP = 64*source.MIB
LANES = ("raw/noaa-nwm", "work/noaa-nwm", "receipts/ingest/noaa-nwm")


def paths(root, run):
    if not re.fullmatch(r"20\d{6}T\d{6}Z", run):
        raise ValueError("RUN_ID_INVALID")
    return tuple(root/"data"/lane/run for lane in LANES)


def check_root(root):
    if not initialized(root) or root.stat().st_mode & 0o077:
        raise ValueError("PRIVATE_INITIALIZED_STORE_REQUIRED")


def usage(root):
    count = 0
    for lane in LANES:
        base = root/"data"/lane
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


def room(root, additional):
    if additional < 0 or usage(root)+additional+REPORT_RESERVE > CAP:
        raise ValueError("SOURCE_STORAGE_CAP")
    if shutil.disk_usage(root).free < additional+RESERVE+REPORT_RESERVE:
        raise ValueError("FREE_SPACE_RESERVE")


def ensure_file(root, path, body):
    if path.exists() or path.is_symlink():
        if read_regular(path, max(1, len(body))) != body:
            raise ValueError("IMMUTABLE_OUTPUT_MISMATCH")
    else:
        room(root, len(body)+4096)
        write_new(path, body)


def captured(root, run, name, url, limit, *, fetcher=source.fetch, expected=None):
    raw, _, receipts = paths(root, run)
    target, receipt = raw/name, receipts/(name+".json")
    if receipt.exists():
        ref = json.loads(read_regular(receipt, source.MIB))
        if ref["source_url"] != url or ref["path"] != str(target.relative_to(root)):
            raise ValueError("CAPTURE_RECEIPT_IDENTITY")
        digest, size = hash_regular(target, limit, expected_size=ref["bytes"])
        if digest != ref["sha256"]:
            raise ValueError("CAPTURE_HASH_MISMATCH")
        if expected and (size != expected["declared_bytes"] or ref["last_modified"] != expected["last_modified"]):
            raise ValueError("SOURCE_CHANGED_SINCE_PLAN")
        return ref
    if target.exists() or target.is_symlink():
        raise ValueError("UNRECEIPTED_CAPTURE_REQUIRES_INSPECTION")
    room(root, limit+8192)
    body, header = fetcher(url, limit)
    if not 0 < len(body) <= limit or header["source_url"] != url:
        raise ValueError("CAPTURE_SIZE_OR_URL")
    if expected and (len(body) != expected["declared_bytes"] or header["last_modified"] != expected["last_modified"]):
        raise ValueError("SOURCE_CHANGED_SINCE_PLAN")
    ref = {**header, "path": str(target.relative_to(root)), "bytes": len(body), "sha256": sha256(body).hexdigest(),
           "checksum_role": "captured-byte-identity-only", "source_admitted": False}
    write_new(target, body)
    write_new(receipt, canonical(ref))
    return ref


def checked_body(root, ref, limit):
    relative = Path(ref["path"])
    if relative.is_absolute() or ".." in relative.parts or not str(relative).startswith("data/raw/noaa-nwm/"):
        raise ValueError("CAPTURE_PATH_INVALID")
    body = read_regular(root/relative, limit)
    if len(body) != ref["bytes"] or sha256(body).hexdigest() != ref["sha256"]:
        raise ValueError("CAPTURE_HASH_MISMATCH")
    return body


def load_plan(root, run):
    _, work, _ = paths(root, run)
    plan = json.loads(read_regular(work/"plan-v2.json", 8*source.MIB))
    if (plan["run"] != run or plan["bbox"] != source.BBOX or plan["cap_bytes"] != CAP
            or plan["geometry_cap_bytes"] != GEOMETRY_CAP or plan["work_cap_bytes"] != WORK_CAP
            or plan["free_reserve_bytes"] != RESERVE):
        raise ValueError("PLAN_IDENTITY")
    expected = source.model_objects(plan["day"], plan["cycle_hour"])
    if len(plan["models"]) != len(expected):
        raise ValueError("PLAN_MODEL_COUNT")
    for actual, item in zip(plan["models"], expected):
        if any(actual.get(k) != v for k, v in item.items()) or not 0 < actual["head"]["declared_bytes"] <= source.CHANNEL_LIMIT:
            raise ValueError("PLAN_MODEL_IDENTITY")
    for ref in plan["metadata"].values():
        checked_body(root, ref, source.PAGE_LIMIT)
    ids = source.object_ids(checked_body(root, plan["metadata"]["flowline-ids.json"], source.PAGE_LIMIT))
    if plan["object_ids"] != ids:
        raise ValueError("PLAN_GEOMETRY_IDS")
    return plan


def prepare(root, run, *, fetcher=source.fetch):
    check_root(root)
    raw, work, _ = paths(root, run)
    with store_lock(root):
        if (work/"plan-v2.json").exists():
            return load_plan(root, run)
        # Metadata-only preflight; no forecast transfer until capture is invoked.
        room(root, 16*source.MIB)
        refs = {}
        def metadata(name, url):
            ref = captured(root, run, "metadata/"+name, url, source.PAGE_LIMIT, fetcher=fetcher)
            refs[name] = ref
            return checked_body(root, ref, source.PAGE_LIMIT)
        day = source.latest_day(metadata("prod.html", source.BASE))
        listing = metadata("short-range.html", f"{source.BASE}nwm.{day}/short_range/")
        hour = source.latest_complete_cycle(listing)
        for name, url in source.DOCS.items():
            metadata(name, url)
        layer = json.loads(metadata("flowline-layer.json", source.FLOWLINES+"?f=json"))
        if layer.get("objectIdField") != "oid" or layer.get("error"):
            raise ValueError("FLOWLINE_LAYER_INVALID")
        ids = source.object_ids(metadata("flowline-ids.json", source.ids_url()))
        models = source.model_objects(day, hour)
        for item in models:
            _, item["head"] = fetcher(item["url"], source.CHANNEL_LIMIT, head=True)
        total = sum(item["head"]["declared_bytes"] for item in models)
        room(root, total+GEOMETRY_CAP+WORK_CAP)
        plan = {"format": "kfm.noaa-nwm-local-plan/v2", "run": run, "prepared_at": source.now(),
                "day": day, "cycle_hour": hour, "bbox": source.BBOX, "selection": "Kansas envelope intersection; border reaches retained",
                "models": models, "metadata": refs, "object_ids": ids, "model_source_bytes": total,
                "cap_bytes": CAP, "free_reserve_bytes": RESERVE, "geometry_cap_bytes": GEOMETRY_CAP,
                "work_cap_bytes": WORK_CAP, "source_admitted": False, "published": False}
        ensure_file(root, work/"plan-v2.json", canonical(plan))
        return plan


def capture(root, run, *, fetcher=source.fetch):
    check_root(root)
    _, work, receipts = paths(root, run)
    started = time.monotonic()
    with store_lock(root):
        plan = load_plan(root, run)
        refs, geometry_bytes = [], 0
        for item in plan["models"]:
            if time.monotonic()-started > 1800:
                raise ValueError("CAPTURE_TIME_LIMIT")
            refs.append(captured(root, run, "models/"+item["name"], item["url"], source.CHANNEL_LIMIT,
                                 fetcher=fetcher, expected=item["head"]))
            print("model", item["name"], refs[-1]["bytes"], flush=True)
        for offset in range(0, len(plan["object_ids"]), source.PAGE_SIZE):
            if time.monotonic()-started > 1800:
                raise ValueError("CAPTURE_TIME_LIMIT")
            ids = plan["object_ids"][offset:offset+source.PAGE_SIZE]
            limit = min(source.PAGE_LIMIT, GEOMETRY_CAP-geometry_bytes)
            ref = captured(root, run, f"flowlines/{offset//source.PAGE_SIZE:04d}.json", source.page_url(ids), limit, fetcher=fetcher)
            page = json.loads(checked_body(root, ref, limit))
            if (page.get("error") or page.get("exceededTransferLimit") or
                    sorted(f["attributes"]["oid"] for f in page.get("features", [])) != ids):
                raise ValueError("FLOWLINE_PAGE_INCOMPLETE")
            refs.append(ref)
            geometry_bytes += ref["bytes"]
            if offset % (10*source.PAGE_SIZE) == 0:
                print("geometry", min(offset+source.PAGE_SIZE, len(plan["object_ids"])), "/", len(plan["object_ids"]), flush=True)
        report = {"format": "kfm.noaa-nwm-capture/v1", "run": run, "plan_sha256": sha256(canonical(plan)).hexdigest(),
                  "sources": refs, "source_bytes": sum(r["bytes"] for r in refs), "complete": True,
                  "source_admitted": False, "published": False}
        ensure_file(root, receipts/("capture-"+report["plan_sha256"][:16]+".json"), canonical(report))
        return report


def project(root, run):
    from pipelines.domains.hydrology.nwm_subset import subset
    check_root(root)
    _, work, receipts = paths(root, run)
    with store_lock(root):
        plan = load_plan(root, run)
        plan_hash = sha256(canonical(plan)).hexdigest()
        report = json.loads(read_regular(receipts/("capture-"+plan_hash[:16]+".json"), 4*source.MIB))
        if (not report.get("complete") or report["run"] != run
                or report["plan_sha256"] != sha256(canonical(plan)).hexdigest()):
            raise ValueError("CAPTURE_PLAN_MISMATCH")
        expected = [("models/"+item["name"], item["url"]) for item in plan["models"]]
        expected += [(f"flowlines/{i//source.PAGE_SIZE:04d}.json", source.page_url(plan["object_ids"][i:i+source.PAGE_SIZE]))
                     for i in range(0, len(plan["object_ids"]), source.PAGE_SIZE)]
        raw, _, _ = paths(root, run)
        if len(report["sources"]) != len(expected):
            raise ValueError("CAPTURE_SOURCE_COUNT")
        for ref, (name, url) in zip(report["sources"], expected):
            if ref["path"] != str((raw/name).relative_to(root)) or ref["source_url"] != url:
                raise ValueError("CAPTURE_SOURCE_IDENTITY")
            checked_body(root, ref, source.CHANNEL_LIMIT)
        room(root, WORK_CAP)
        outputs, summary = subset(plan, report, lambda ref: checked_body(root, ref, source.CHANNEL_LIMIT))
        if sum(len(b) for b in outputs.values()) > WORK_CAP:
            raise ValueError("WORK_BYTE_LIMIT")
        for name, body in outputs.items():
            ensure_file(root, work/name, body)
        verification = {"format": "kfm.noaa-nwm-verification/v1", "run": run,
                        "capture_sha256": sha256(canonical(report)).hexdigest(), **summary,
                        "outputs": [{"path": str((work/name).relative_to(root)), "bytes": len(body),
                                     "sha256": sha256(body).hexdigest()} for name, body in outputs.items()],
                        "source_admitted": False, "map_activated": False, "published": False}
        ensure_file(root, receipts/"verification.json", canonical(verification))
        return verification


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["prepare", "capture", "verify"])
    parser.add_argument("--root", default=os.environ.get("KFM_DATA_ROOT"))
    parser.add_argument("--run", required=True)
    args = parser.parse_args()
    root = external_root(args.root)
    result = {"prepare": prepare, "capture": capture, "verify": project}[args.action](root, args.run)
    summary = {k: v for k, v in result.items() if k not in {"models", "metadata", "object_ids", "sources"}}
    print(json.dumps({**summary, "retained_disk_bytes": usage(root), "free_disk_bytes": shutil.disk_usage(root).free}, indent=2))


if __name__ == "__main__":
    main()
