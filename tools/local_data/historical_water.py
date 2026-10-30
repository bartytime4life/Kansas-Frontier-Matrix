"""Prepare one pinned historical USGS water collection for private review, offline."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path

from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes, utc_time
from pipelines.domains.hydrology.normalize import normalize_capture
from pipelines.domains.hydrology.validate import validate_candidate
from tools.local_data.file_io import read_regular, write_new
from tools.local_data.manage import external_root, initialized, store_lock
from tools.local_data.review_packages import relative

PROFILE = "kfm-historical-water-review/v1"
FIELDS = ["station_id", "observed_at", "value", "unit", "approval_status", "provisional", "qualifiers",
          "provider_revision_at", "retrieved_at", "page_digest", "record_digest"]
SOURCE_FILES = {"README.md", "accuracy-review.json", "rights-review.json", "captured-discharge-observations.csv",
                "discharge-stations-captured-20260929-30.geojson"}
AUTHORITY = {"admission": False, "activation": False, "release": False, "publication": False}


def _digest(value):
    import re
    if not isinstance(value, str) or not re.fullmatch(r"[a-f0-9]{64}", value):
        raise ValueError("HISTORICAL_DIGEST_INVALID")
    return value


def prepare(source_root: Path, source_manifest: str, manifest_sha256: str, capture_id: str):
    """Verify the selected package and replay original pages; perform no writes."""
    path = relative(source_manifest)
    if path.parts[:3] != ("data", "work", "hydrology") or path.name != "review-manifest.json":
        raise ValueError("HISTORICAL_SOURCE_PATH_INVALID")
    raw_manifest = read_regular(source_root / path, 256 * 1024)
    if hashlib.sha256(raw_manifest).hexdigest() != _digest(manifest_sha256):
        raise ValueError("HISTORICAL_MANIFEST_CHANGED")
    manifest = decode_object(raw_manifest, limit=256 * 1024)
    if (manifest.get("profile") != "kfm-private-collection-readiness/v1" or manifest.get("review_state") != "PENDING"
            or any(manifest.get(k) is not False for k in ("released", "published", "source_admitted"))):
        raise ValueError("HISTORICAL_SOURCE_AUTHORITY_INVALID")
    rows = manifest.get("outputs")
    if (not isinstance(rows, list) or len(rows) != len(SOURCE_FILES)
            or {r.get("file") for r in rows if isinstance(r, dict)} != SOURCE_FILES):
        raise ValueError("HISTORICAL_SOURCE_MEMBERS_INVALID")
    members, total = {}, 0
    for row in rows:
        if type(row.get("bytes")) is not int or not 0 < row["bytes"] <= 2 * 1024**2:
            raise ValueError("HISTORICAL_SOURCE_LIMIT")
        total += row["bytes"]
        if total > 2 * 1024**2:
            raise ValueError("HISTORICAL_SOURCE_LIMIT")
        raw = read_regular(source_root / path.parent / row["file"], row["bytes"])
        if len(raw) != row["bytes"] or hashlib.sha256(raw).hexdigest() != _digest(row.get("sha256")):
            raise ValueError("HISTORICAL_SOURCE_MEMBER_CHANGED")
        members[row["file"]] = raw
    if manifest.get("output_bytes") != total:
        raise ValueError("HISTORICAL_SOURCE_LIMIT")
    if not isinstance(capture_id, str) or not capture_id.startswith("sha256:"):
        raise ValueError("HISTORICAL_CAPTURE_INVALID")
    capture_hash = _digest(capture_id[7:])
    capture_raw = read_regular(source_root / "data/quarantine/usgs-nwis/runs" / capture_hash / "manifest.json", 256 * 1024)
    capture = decode_object(capture_raw, limit=256 * 1024)
    if capture.get("capture_id") != capture_id:
        raise ValueError("HISTORICAL_CAPTURE_INVALID")
    pages = capture.get("pages")
    if not isinstance(pages, list) or not 4 <= len(pages) <= 12:
        raise ValueError("HISTORICAL_CAPTURE_LIMIT")
    objects, total = {}, 0
    for page in pages:
        digest = page.get("sha256", "")
        if not isinstance(digest, str) or not digest.startswith("sha256:"):
            raise ValueError("HISTORICAL_CAPTURE_INVALID")
        object_hash = _digest(digest[7:])
        raw = read_regular(source_root / "data/quarantine/usgs-nwis/objects/sha256" / object_hash / "payload", 2 * 1024**2)
        total += len(raw)
        if total > 8 * 1024**2 or digest_bytes(raw) != digest:
            raise ValueError("HISTORICAL_CAPTURE_LIMIT_OR_CHANGED")
        objects[digest] = raw
    candidate = normalize_capture(capture, objects)
    validation = validate_candidate(candidate)
    table = csv.DictReader(io.StringIO(members["captured-discharge-observations.csv"].decode("utf-8")))
    if table.fieldnames != FIELDS:
        raise ValueError("HISTORICAL_TABLE_SCHEMA_CHANGED")
    expected = [{k: json.dumps(o[k], separators=(",", ":")) if k == "qualifiers"
                 else str(o[k]) if o[k] is not None else "" for k in FIELDS} for o in candidate["observations"]]
    if list(table) != expected:
        raise ValueError("HISTORICAL_TABLE_REPLAY_MISMATCH")
    inputs = {"source_manifest_sha256": manifest_sha256, "capture_id": capture_id,
              "capture_manifest_sha256": hashlib.sha256(capture_raw).hexdigest(),
              "candidate_id": candidate["candidate_id"], "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "normalizer_sha256": hashlib.sha256(Path(normalize_capture.__code__.co_filename).read_bytes()).hexdigest(),
              "validator_sha256": hashlib.sha256(Path(validate_candidate.__code__.co_filename).read_bytes()).hexdigest()}
    return candidate, validation, members, inputs


def derive(source_root: Path, root: Path, source_manifest: str, manifest_sha256: str, capture_id: str):
    source_root, root = external_root(str(source_root)), external_root(str(root))
    if source_root == root or source_root in root.parents or root in source_root.parents:
        raise ValueError("HISTORICAL_SEPARATE_DESTINATION_REQUIRED")
    if not initialized(root):
        raise ValueError("STORE_NOT_INITIALIZED_RUN_INIT")
    candidate, validation, members, inputs = prepare(source_root, source_manifest, manifest_sha256, capture_id)
    identity = hashlib.sha256(canonical_bytes(inputs)).hexdigest()
    location = Path("data/work/hydrology/historical-water") / identity
    observations = candidate["observations"]
    times = [o["observed_at"] for o in observations]
    coverage = {"profile": PROFILE, "use": "HISTORICAL_CONTEXT", "topics": ["water", "weather", "disaster", "science"],
                "observations": len(observations), "stations": len(candidate["stations"]),
                "observed_from": min(times, key=utc_time, default=None), "observed_through": max(times, key=utc_time, default=None),
                "requested_from": candidate["start"], "requested_through": candidate["end"],
                "retrieved_at": candidate["retrieved_at"], "units": sorted({o["unit"] for o in observations}),
                "missing_values": sum(o["value"] is None for o in observations),
                "provisional_observations": sum(o["provisional"] for o in observations),
                "authority": AUTHORITY, "inputs": inputs,
                "limitations": "Frozen provider observations; not current river conditions, warnings or forecasts. Provider positions are approximate; geometry is retained without another datum conversion."}
    features = [{"type": "Feature", "id": s["id"], "geometry": s["geometry"],
                 "properties": {"station_id": s["id"], "name": s["name"], "historical": True,
                                "observations": sum(o["station_id"] == s["id"] for o in observations),
                                "source_page_digest": s["page_digest"]}} for s in candidate["stations"]]
    outputs = {"coverage.json": canonical_bytes(coverage), "candidate.json": canonical_bytes(candidate),
               "validation.json": canonical_bytes(validation), "observations.csv": members["captured-discharge-observations.csv"],
               "stations.geojson": canonical_bytes({"type": "FeatureCollection", "features": features}),
               "source-rights-review.json": members["rights-review.json"],
               "README.md": (f"# Historical USGS water context\n\n{len(observations)} measurements from {len(features)} stations, "
                             f"{coverage['observed_from']} through {coverage['observed_through']}.\n\n"
                             "All source clocks, units, missingness and provisional flags are retained. The CSV matches a fresh replay of the original captured pages. "
                             "Open coverage.json for provenance and limits; observations.csv is the complete dated table. "
                             "Stations are provider positions, not surveyed locations. No coordinate transformation was applied.\n\n"
                             "Private enrichment candidate only. Source admission, activation, release and publication remain pending. "
                             "The source rights review is retained as a dated assessment, not a new approval.\n").encode()}
    records = [{"file": name, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()} for name, raw in sorted(outputs.items())]
    manifest = {"profile": PROFILE, "review_state": "PENDING", "released": False, "published": False,
                "source_admitted": False, "output_bytes": sum(r["bytes"] for r in records), "outputs": records,
                "source_role": f"Historical USGS discharge, {coverage['observed_from']} through {coverage['observed_through']}; provider-provisional observations, not current conditions.",
                "rights": "See the retained dated source rights review; no new approval.", "inputs": inputs}
    outputs["review-manifest.json"] = canonical_bytes(manifest)
    with store_lock(root):
        target = root / location
        if target.exists() and {p.name for p in target.iterdir()} - set(outputs):
            raise ValueError("HISTORICAL_OUTPUT_CLOSURE_CHANGED")
        for name, raw in outputs.items():
            path = target / name
            try:
                write_new(path, raw)
            except FileExistsError:
                if read_regular(path, max(len(raw), 1)) != raw:
                    raise ValueError("HISTORICAL_OUTPUT_CHANGED") from None
    digest = hashlib.sha256(outputs["review-manifest.json"]).hexdigest()
    return {"profile": PROFILE, "state": "PREPARED_FOR_PRIVATE_REVIEW", "binding": str(location / "review-manifest.json") + "@" + digest,
            "observations": len(observations), "stations": len(features), "authority": AUTHORITY}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("source-root", "root", "source-manifest", "manifest-sha256", "capture-id"):
        parser.add_argument("--" + name, required=True)
    args = parser.parse_args()
    print(json.dumps(derive(Path(args.source_root), Path(args.root), args.source_manifest, args.manifest_sha256, args.capture_id)))


if __name__ == "__main__":
    main()
