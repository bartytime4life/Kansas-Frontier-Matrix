"""Replay pinned archived NOAA monthly normals into a private, tabular collection."""
from __future__ import annotations

import argparse
import csv
from datetime import datetime
import hashlib
import io
import json
import re
from pathlib import Path

from connectors.noaa.src.noaa import climate_normals as parser
from connectors.noaa.src.noaa.climate_normals_capture import canonical_bytes
from pipelines.domains.atmosphere.noaa_normals import normalize_capture
from tools.local_data.file_io import read_regular, write_new
from tools.local_data.manage import external_root, initialized, store_lock
from tools.local_data.review_packages import relative

PROFILE = "kfm-historical-climate-normals-review/v1"
AUTHORITY = {"admission": False, "activation": False, "release": False, "publication": False}
FIELDS = ["station_id", "station_name", "latitude", "longitude", "normal_period", "calendar_month", "variable", "unit",
          "element_published_at_station", "value_text", "source_raw_value", "measurement_flag", "completeness_flag",
          "years", "source_sha256", "source_url", "retrieved_at", "source_role", "review_state", "released"]
TABLES = {"temperature_f": "degF", "precipitation_in": "in"}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def checked_hash(value):
    if not isinstance(value, str) or not re.fullmatch(r"[a-f0-9]{64}", value):
        raise ValueError("NORMALS_DIGEST_INVALID")
    return value


def rows(candidate, capture, variable):
    """Keep absent elements distinct from published elements with a missing value."""
    entries = {e["station_id"]: e for e in capture["station_objects"]}
    for station in candidate["stations"]:
        entry = entries[station["station_id"]]
        for month in station["months"]:
            element = month[variable]
            values = [station["station_id"], station["name"], station["latitude"], station["longitude"], "1991-2020",
                      month["month"], variable, TABLES[variable], element is not None,
                      element["value"] if element else None, element["raw"] if element else None,
                      element["measurement_flag"] if element else None, element["completeness_flag"] if element else None,
                      element["years"] if element else None, station["source_sha256"], parser.object_url(entry["key"]),
                      entry["retrieved_at"], "station climate normal aggregate", "PENDING", False]
            yield {k: "" if v is None else str(v) for k, v in zip(FIELDS, values)}


def prepare(source_root: Path, source_manifest: str, manifest_sha256: str, capture_id: str, capture_manifest_sha256: str):
    """Validate selected source tables against a full offline replay of the capture."""
    path = relative(source_manifest)
    if path.parts[:3] != ("data", "work", "atmosphere") or path.name != "review-manifest.json":
        raise ValueError("NORMALS_SOURCE_PATH_INVALID")
    raw = read_regular(source_root / path, 256 * 1024)
    if digest(raw) != checked_hash(manifest_sha256):
        raise ValueError("NORMALS_MANIFEST_CHANGED")
    source = json.loads(raw)
    if (source.get("profile") != "kfm-private-collection-readiness/v1" or source.get("review_state") != "PENDING"
            or any(source.get(k) is not False for k in ("released", "published", "source_admitted"))):
        raise ValueError("NORMALS_SOURCE_AUTHORITY_INVALID")
    declared = source.get("outputs")
    if not isinstance(declared, list) or not 3 <= len(declared) <= 64:
        raise ValueError("NORMALS_SOURCE_MEMBERS_INVALID")
    names = [r.get("file") for r in declared if isinstance(r, dict)]
    if len(names) != len(declared) or len(set(names)) != len(names):
        raise ValueError("NORMALS_SOURCE_MEMBERS_INVALID")
    selected = {"tables/" + v + ".csv" for v in TABLES} | {"rights-review.json"}
    members = {}
    for name in sorted(selected):
        matches = [r for r in declared if r["file"] == name]
        if len(matches) != 1:
            raise ValueError("NORMALS_SOURCE_MEMBERS_INVALID")
        row = matches[0]
        if type(row.get("bytes")) is not int or not 0 < row["bytes"] <= 8 * 1024**2:
            raise ValueError("NORMALS_SOURCE_MEMBER_LIMIT")
        body = read_regular(source_root / path.parent / name, row["bytes"])
        if len(body) != row["bytes"] or digest(body) != checked_hash(row.get("sha256")):
            raise ValueError("NORMALS_SOURCE_MEMBER_CHANGED")
        members[name] = body
    if not isinstance(capture_id, str) or not capture_id.startswith("sha256:"):
        raise ValueError("NORMALS_CAPTURE_ID_INVALID")
    capture_hash = checked_hash(capture_id[7:])
    raw = read_regular(source_root / "data/quarantine/noaa-climate-normals/runs" / capture_hash / "manifest.json", 256 * 1024)
    if digest(raw) != checked_hash(capture_manifest_sha256):
        raise ValueError("NORMALS_CAPTURE_MANIFEST_CHANGED")
    capture = json.loads(raw)
    body = {k: v for k, v in capture.items() if k != "capture_id"}
    if (capture.get("capture_id") != capture_id or "sha256:" + digest(canonical_bytes(body)) != capture_id
            or capture.get("release_state") != "UNRELEASED" or capture.get("inventory", {}).get("key") != parser.INVENTORY_KEY):
        raise ValueError("NORMALS_CAPTURE_ID_INVALID")
    entries = capture.get("station_objects")
    if not isinstance(entries, list) or not 1 <= len(entries) <= 1000:
        raise ValueError("NORMALS_CAPTURE_LIMIT")
    objects, total = {}, 0
    for index, ref in enumerate([capture["inventory"], *entries]):
        sha = ref.get("sha256", "")
        if not isinstance(sha, str) or not sha.startswith("sha256:"):
            raise ValueError("NORMALS_DIGEST_INVALID")
        object_hash = checked_hash(sha[7:])
        limit = 2 * 1024**2 if index == 0 else 128 * 1024
        if type(ref.get("bytes")) is not int or not 0 < ref["bytes"] <= limit:
            raise ValueError("NORMALS_CAPTURE_LIMIT")
        raw = read_regular(source_root / "data/quarantine/noaa-climate-normals/objects/sha256" / object_hash / "payload", limit)
        total += len(raw)
        if total > 32 * 1024**2 or len(raw) != ref["bytes"] or digest(raw) != object_hash:
            raise ValueError("NORMALS_OBJECT_CHANGED_OR_LIMIT")
        if ref.get("status") != 200 or not isinstance(ref.get("retrieved_at"), str):
            raise ValueError("NORMALS_RETRIEVAL_INVALID")
        stamp = datetime.fromisoformat(ref["retrieved_at"].replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            raise ValueError("NORMALS_RETRIEVAL_INVALID")
        objects[sha] = raw
    candidate = normalize_capture(capture, objects)
    for variable in TABLES:
        table = csv.DictReader(io.StringIO(members["tables/" + variable + ".csv"].decode("utf-8")), strict=True)
        if table.fieldnames != FIELDS or list(table) != list(rows(candidate, capture, variable)):
            raise ValueError("NORMALS_TABLE_REPLAY_MISMATCH")
    inputs = {"source_manifest": str(path), "source_manifest_sha256": manifest_sha256, "capture_id": capture_id,
              "capture_manifest_sha256": capture_manifest_sha256, "candidate_id": candidate["candidate_id"],
              "generator_sha256": digest(Path(__file__).read_bytes()), "parser_sha256": digest(Path(parser.__file__).read_bytes()),
              "normalizer_sha256": digest(Path(normalize_capture.__code__.co_filename).read_bytes()),
              "canonicalizer_sha256": digest(Path(canonical_bytes.__code__.co_filename).read_bytes()),
              "selected_source_members": sorted(selected), "raw_object_count": len(entries) + 1, "raw_bytes": total}
    return candidate, capture, members, inputs


def derive(source_root: Path, root: Path, source_manifest: str, manifest_sha256: str, capture_id: str, capture_manifest_sha256: str):
    source_root, root = external_root(str(source_root)), external_root(str(root))
    if source_root == root or source_root in root.parents or root in source_root.parents:
        raise ValueError("NORMALS_SEPARATE_DESTINATION_REQUIRED")
    if not initialized(root):
        raise ValueError("STORE_NOT_INITIALIZED_RUN_INIT")
    candidate, capture, members, inputs = prepare(source_root, source_manifest, manifest_sha256, capture_id, capture_manifest_sha256)
    location = Path("data/work/atmosphere/historical-normals") / digest(canonical_bytes(inputs))
    summaries = {}
    for variable, unit in TABLES.items():
        cells = [m[variable] for s in candidate["stations"] for m in s["months"]]
        summaries[variable] = {"unit": unit, "cells": len(cells), "values_present": sum(e is not None and e["value"] is not None for e in cells),
                               "element_not_published": sum(e is None for e in cells),
                               "published_value_missing": sum(e is not None and e["value"] is None for e in cells),
                               "completeness_flags": {flag: sum(e is not None and e["completeness_flag"] == flag for e in cells)
                                                      for flag in sorted(parser.FLAGS)}}
    coverage = {"profile": PROFILE, "use": "HISTORICAL_CLIMATE_CONTEXT", "normal_period": "1991-2020", "calendar_months": list(range(1, 13)),
                "stations": candidate["station_count"], "variables": summaries, "captured_at": capture["captured_at"],
                "topics": ["weather", "water", "agriculture", "science", "disaster"], "native_coordinate_crs": "NAD83",
                "authority": AUTHORITY, "inputs": inputs,
                "limitations": "Station monthly climate aggregates, not current observations, forecasts, a continuous surface or an annual time series. Native NAD83 coordinates are tabular only; no transformation or GeoJSON generated. Missingness is not zero. Source rights notes are dated assessments, not new approval."}
    outputs = {"coverage.json": canonical_bytes(coverage), "candidate.json": canonical_bytes(candidate),
               "validation.json": canonical_bytes({"state": "OFFLINE_REPLAY_MATCH", "tables_checked": list(TABLES), "inputs": inputs, "authority": AUTHORITY}),
               "source-rights-review.json": members["rights-review.json"],
               **{v + ".csv": members["tables/" + v + ".csv"] for v in TABLES},
               "README.md": (f"# Historical NOAA climate context\n\n1991–2020 monthly station normals for {candidate['station_count']} Kansas stations, captured {capture['captured_at']}.\n\n"
                             "Temperature (degF) and precipitation (in) tables match a fresh offline replay of every captured station file. "
                             "The twelve months are long-term calendar-month aggregates. Absent station elements and published missing values remain distinct; raw tokens, flags, years and retrieval dates are retained.\n\n"
                             "Native NAD83 coordinates are tabular only. These are not current weather, forecasts, an annual time series or an interpolated map. "
                             "See coverage.json for counts, provenance and limits.\n\nPrivate review only: admission, activation, release and publication remain pending. "
                             "Source rights notes are retained as a dated assessment.\n").encode()}
    records = [{"file": name, "bytes": len(raw), "sha256": digest(raw)} for name, raw in sorted(outputs.items())]
    outputs["review-manifest.json"] = canonical_bytes({"profile": PROFILE, "review_state": "PENDING", "released": False,
        "published": False, "source_admitted": False, "outputs": records, "output_bytes": sum(r["bytes"] for r in records),
        "source_role": "NOAA 1991–2020 station monthly climate aggregates; historical context only.",
        "rights": "Retained dated source rights assessment; no new approval.", "inputs": inputs})
    with store_lock(root):
        target = root / location
        if target.exists() and {p.name for p in target.iterdir()} - set(outputs):
            raise ValueError("NORMALS_OUTPUT_CLOSURE_CHANGED")
        for name, raw in outputs.items():
            try:
                write_new(target / name, raw)
            except FileExistsError:
                if read_regular(target / name, max(1, len(raw))) != raw:
                    raise ValueError("NORMALS_OUTPUT_CHANGED") from None
    return {"profile": PROFILE, "state": "PREPARED_FOR_PRIVATE_REVIEW", "stations": candidate["station_count"],
            "variables": summaries, "binding": str(location / "review-manifest.json") + "@" + digest(outputs["review-manifest.json"]), "authority": AUTHORITY}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    for name in ("source-root", "root", "source-manifest", "manifest-sha256", "capture-id", "capture-manifest-sha256"):
        cli.add_argument("--" + name, required=True)
    args = vars(cli.parse_args())
    args["source_root"], args["root"] = Path(args["source_root"]), Path(args["root"])
    print(json.dumps(derive(**args)))


if __name__ == "__main__":
    main()
