#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from packages.evidence.evidencebundle_hash import canonical_json, compute_spec_hash
from tools.validators.fauna.validate_evidencebundle import main as validate_bundle_main

DENIED_FIELDS = {"decimallatitude", "decimallongitude", "latitude", "longitude", "lat", "lon", "raw_latitude", "raw_longitude", "point", "geom", "geometry"}


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(2)


def sha256_file(path: Path) -> str:
    d = hashlib.sha256()
    with path.open("rb") as f:
        for c in iter(lambda: f.read(65536), b""):
            d.update(c)
    return f"sha256:{d.hexdigest()}"


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="kfm-ebird-aggregate", description="Layer 4 KFM eBird aggregate adapter")
    p.add_argument("--observations", required=True)
    p.add_argument("--evidencebundle", required=True)
    p.add_argument("--aggregate", required=True, choices=("county", "huc12"))
    p.add_argument("--suppression", type=int, default=10)
    p.add_argument("--out", required=True)
    p.add_argument("--manifest", required=True)
    p.add_argument("--suppression-receipt", required=True)
    p.add_argument("--format", choices=("jsonl", "csv"), default="jsonl")
    p.add_argument("--regions-file")
    p.add_argument("--limit", type=int)
    return p.parse_args(argv)


def point_in_ring(x: float, y: float, ring: list[list[float]]) -> bool:
    inside = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i]
        xj, yj = ring[j]
        if (yi > y) != (yj > y):
            cross = (xj - xi) * (y - yi) / ((yj - yi) or 1e-12) + xi
            if x < cross:
                inside = not inside
        j = i
    return inside


def point_in_polygon(lon: float, lat: float, poly: list[list[list[float]]]) -> bool:
    if not poly:
        return False
    if not point_in_ring(lon, lat, poly[0]):
        return False
    for hole in poly[1:]:
        if point_in_ring(lon, lat, hole):
            return False
    return True


def main() -> None:
    a = parse_args(sys.argv[1:])
    if a.suppression < 10:
        fail("--suppression must be >= 10")
    if a.limit is not None and a.limit <= 0:
        fail("--limit must be positive")
    obs_path = Path(a.observations)
    eb_path = Path(a.evidencebundle)
    for p in (obs_path, eb_path):
        if not p.exists():
            fail(f"Missing input file: {p}")
    if "data/published" in Path(a.suppression_receipt).as_posix():
        fail("--suppression-receipt cannot be under data/published")

    old = sys.argv
    try:
        sys.argv = ["validate_evidencebundle.py", str(eb_path)]
        validate_bundle_main()
    except SystemExit as e:
        if e.code != 0:
            fail("EvidenceBundle validation failed")
    finally:
        sys.argv = old

    bundle = json.loads(eb_path.read_text(encoding="utf-8"))
    spec_hash = bundle["kfm:spec_hash"]
    query_predicate = bundle.get("query_predicate")

    features = []
    if a.regions_file:
        fc = json.loads(Path(a.regions_file).read_text(encoding="utf-8"))
        for f in fc.get("features", []):
            props = f.get("properties", {})
            if a.aggregate == "huc12":
                rid = props.get("HUC12") or props.get("huc12") or props.get("huc_12") or props.get("name")
            else:
                rid = props.get("GEOID") or props.get("geoid") or props.get("county_fips") or props.get("countyFips") or props.get("name")
            geom = f.get("geometry") or {}
            typ, coords = geom.get("type"), geom.get("coordinates")
            if rid and typ in {"Polygon", "MultiPolygon"}:
                polys = [coords] if typ == "Polygon" else coords
                b = [180, 90, -180, -90]
                for p in polys:
                    for r in p:
                        for x, y in r:
                            b[0] = min(b[0], x); b[1] = min(b[1], y); b[2] = max(b[2], x); b[3] = max(b[3], y)
                features.append((str(rid), polys, tuple(b)))

    groups: dict[tuple[str, str, str], dict[str, Any]] = {}
    counts = defaultdict(int)
    method_field = method_geo = False

    with obs_path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            counts["rows_seen"] += 1
            if a.limit and counts["rows_seen"] > a.limit:
                break
            row = json.loads(line)
            try:
                month = str(row["occurrenceDate"])[:7]
                taxon = str(row["taxonKey"])
                ds = str(row["kfm:dataset_key"])
                lat = float(row["decimalLatitude"])
                lon = float(row["decimalLongitude"])
            except Exception:
                counts["rows_invalid"] += 1
                continue
            rid = None
            if a.aggregate == "huc12":
                rid = row.get("huc12") or row.get("HUC12") or row.get("huc_12")
            else:
                rid = row.get("county_fips") or row.get("countyFips") or row.get("GEOID") or row.get("geoid")
            if rid:
                method_field = True
            if not rid and features:
                for frid, polys, (minx, miny, maxx, maxy) in features:
                    if lon < minx or lon > maxx or lat < miny or lat > maxy:
                        continue
                    if any(point_in_polygon(lon, lat, p) for p in polys):
                        rid = frid
                        method_geo = True
                        break
            if not rid:
                counts["rows_unassigned"] += 1
                continue
            counts["rows_assigned"] += 1
            key = (str(rid), taxon, month)
            g = groups.setdefault(key, {"datasets": set(), "sum": 0, "unknown": 0, "row_count": 0})
            g["datasets"].add(ds)
            ic = row.get("individualCount")
            if isinstance(ic, (int, float)):
                g["sum"] += int(ic)
            elif ic is None:
                g["unknown"] += 1
                counts["observation_count_unknown"] += 1
            g["row_count"] += 1

    out_rows, suppressed = [], []
    for (rid, taxon, month), g in groups.items():
        cc = len(g["datasets"])
        counts["groups_seen"] += 1
        if cc < a.suppression:
            counts["groups_suppressed"] += 1
            basis = {"aggregate": a.aggregate, "aggregate_id": rid, "taxonKey": taxon, "occurrenceDate_month": month, "kfm_spec_hash": spec_hash}
            gh = hashlib.sha256(canonical_json(basis).encode("utf-8")).hexdigest()
            suppressed.append({"group_hash": f"sha256:{gh}", "checklist_count": cc, "reason": "below_suppression_min_n"})
            continue
        counts["groups_published"] += 1
        r = {
            "schema_version": "v1", "object_type": "AggregateOccurrence", "domain": "fauna", "source": "ebird", "policy_label": "public_aggregate",
            "aggregate": a.aggregate, "taxonKey": taxon, "occurrenceDate_month": month,
            "checklist_count": cc, "observation_count_sum": g["sum"], "observation_count_unknown_count": g["unknown"], "species_count": 1,
            "suppression_min_n": a.suppression, "kfm:spec_hash": spec_hash, "evidence_bundle_uri": bundle.get("source_uri", str(eb_path)),
        }
        r["huc12" if a.aggregate == "huc12" else "county_fips"] = rid
        bad = DENIED_FIELDS.intersection({k.lower() for k in r.keys()})
        if bad:
            fail(f"Public row contains denied fields: {sorted(bad)}")
        out_rows.append(r)

    outp = Path(a.out); outp.parent.mkdir(parents=True, exist_ok=True)
    if a.format == "jsonl":
        with outp.open("w", encoding="utf-8") as f:
            for r in out_rows:
                f.write(json.dumps(r) + "\n")
    else:
        fields = list(out_rows[0].keys()) if out_rows else ["schema_version","object_type","domain","source","policy_label","aggregate",("huc12" if a.aggregate=="huc12" else "county_fips"),"taxonKey","occurrenceDate_month","checklist_count","observation_count_sum","observation_count_unknown_count","species_count","suppression_min_n","kfm:spec_hash","evidence_bundle_uri"]
        with outp.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(out_rows)

    receipt = {
        "schema_version": "v1", "object_type": "SuppressionReceipt", "domain": "fauna", "source": "ebird", "policy_label": "restricted",
        "aggregate": a.aggregate, "suppression_min_n": a.suppression, "query_predicate": query_predicate, "kfm:spec_hash": spec_hash,
        "evidencebundle_path": str(eb_path),
        "counts": {k: counts[k] for k in ["groups_seen","groups_published","groups_suppressed","rows_seen","rows_assigned","rows_unassigned","rows_invalid"]},
        "suppressed_groups": suppressed,
    }
    rpath = Path(a.suppression_receipt); rpath.parent.mkdir(parents=True, exist_ok=True); rpath.write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n", encoding="utf-8")

    method = "observation_field" if method_field and not method_geo else "geojson_spatial_join" if method_geo and not method_field else "mixed" if method_field and method_geo else "observation_field"
    manifest = {
        "schema_version":"v1","object_type":"AggregateManifest","domain":"fauna","source":"ebird","policy_label":"public_aggregate","public_safe":True,
        "observations_path":str(obs_path),"observations_sha256":sha256_file(obs_path),"evidencebundle_path":str(eb_path),"evidencebundle_sha256":sha256_file(eb_path),
        "output_path":str(outp),"output_sha256":sha256_file(outp),"suppression_receipt_path":str(rpath),"suppression_receipt_sha256":sha256_file(rpath),
        "aggregate":a.aggregate,"suppression_min_n":a.suppression,"query_predicate":query_predicate,"kfm:spec_hash":spec_hash,
        "region_assignment_method":method,"output_fields":list(out_rows[0].keys()) if out_rows else [],
        "denied_public_fields_checked":sorted(DENIED_FIELDS),"counts":{**{k:counts[k] for k in ["rows_seen","rows_assigned","rows_unassigned","rows_invalid","groups_seen","groups_published","groups_suppressed","observation_count_unknown"]}},
        "started_at":datetime.utcnow().isoformat()+"Z","completed_at":datetime.utcnow().isoformat()+"Z"
    }
    if a.regions_file:
        manifest["regions_file"] = a.regions_file
        manifest["regions_file_sha256"] = sha256_file(Path(a.regions_file))
    mpath = Path(a.manifest); mpath.parent.mkdir(parents=True, exist_ok=True); mpath.write_text(json.dumps(manifest, indent=2, sort_keys=True)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()
