#!/usr/bin/env python3
"""
Emit KFM catalog candidates for the HUC12 ↔ administrative crosswalk lane.

Outputs:
  data/catalog/stac/crosswalk/<run_id>.json
  data/catalog/dcat/crosswalk/<run_id>.json
  data/catalog/prov/crosswalk/<run_id>.json
  data/catalog/crosswalk/<run_id>.manifest.json

This script emits catalog candidates only. It does not publish.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path


WATCHER = "hydrology_huc12_admin_crosswalk_watch"
COLLECTION_ID = "kfm-huc12-admin-crosswalk"


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )


def sql_quote(value: str) -> str:
    return value.replace("'", "''")


def scalar_psql(dsn: str, sql: str) -> str:
    result = run(["psql", dsn, "-v", "ON_ERROR_STOP=1", "-Atc", sql])
    return result.stdout.strip()


def rows_psql(dsn: str, sql: str) -> list[list[str]]:
    result = run(["psql", dsn, "-v", "ON_ERROR_STOP=1", "-At", "-F", "|", "-c", sql])
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    return [line.split("|") for line in lines]


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def build_catalog(
    *,
    dsn: str,
    run_id: str,
    repo_root: Path,
    public_base_href: str,
) -> dict:
    receipt_id = f"run_receipt:{WATCHER}:{run_id}"
    safe_receipt_id = sql_quote(receipt_id)

    record_count = int(
        scalar_psql(
            dsn,
            f"""
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{safe_receipt_id}';
            """,
        )
        or 0
    )

    if record_count == 0:
        raise SystemExit(f"No crosswalk rows found for {receipt_id}")

    bbox_text = scalar_psql(
        dsn,
        f"""
        SELECT array_to_string(ARRAY[
          ST_XMin(extent)::text,
          ST_YMin(extent)::text,
          ST_XMax(extent)::text,
          ST_YMax(extent)::text
        ], ',')
        FROM (
          SELECT ST_Extent(intersection_geom)::box2d AS extent
          FROM kfm_crosswalk.crosswalk_pairs
          WHERE run_receipt_id = '{safe_receipt_id}'
        ) q;
        """,
    )

    bbox = [float(x) for x in bbox_text.split(",")] if bbox_text else []

    source_rows = rows_psql(
        dsn,
        f"""
        SELECT DISTINCT unnest(source_snapshot_ids)
        FROM kfm_crosswalk.crosswalk_pairs
        WHERE run_receipt_id = '{safe_receipt_id}'
        ORDER BY 1;
        """,
    )

    source_snapshot_ids = [row[0] for row in source_rows]

    algorithm_version = scalar_psql(
        dsn,
        f"""
        SELECT algorithm_version
        FROM kfm_crosswalk.crosswalk_pairs
        WHERE run_receipt_id = '{safe_receipt_id}'
        LIMIT 1;
        """,
    )

    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    stac_path = repo_root / "data/catalog/stac/crosswalk" / f"{run_id}.json"
    dcat_path = repo_root / "data/catalog/dcat/crosswalk" / f"{run_id}.json"
    prov_path = repo_root / "data/catalog/prov/crosswalk" / f"{run_id}.json"
    manifest_path = repo_root / "data/catalog/crosswalk" / f"{run_id}.manifest.json"

    stac = {
        "type": "Collection",
        "stac_version": "1.0.0",
        "id": f"{COLLECTION_ID}-{run_id}",
        "title": "KFM HUC12 Administrative Crosswalk",
        "description": "Candidate catalog record for HUC12 to administrative boundary crosswalk pairs.",
        "license": "proposed-rights-review-required",
        "extent": {
            "spatial": {
                "bbox": [bbox]
            },
            "temporal": {
                "interval": [[now, now]]
            }
        },
        "links": [
            {
                "rel": "self",
                "href": f"{public_base_href.rstrip('/')}/data/catalog/stac/crosswalk/{run_id}.json",
                "type": "application/json"
            }
        ],
        "kfm:object_type": "catalog_candidate",
        "kfm:run_receipt_id": receipt_id,
        "kfm:algorithm_version": algorithm_version,
        "kfm:source_snapshot_ids": source_snapshot_ids,
        "kfm:record_count": record_count,
        "kfm:publication_state": "candidate_no_publish"
    }

    dcat = {
        "@context": {
            "dcat": "http://www.w3.org/ns/dcat#",
            "dct": "http://purl.org/dc/terms/",
            "kfm": "https://kfm.local/ns#"
        },
        "@id": f"kfm://catalog/dcat/crosswalk/{run_id}",
        "@type": "dcat:Dataset",
        "dct:title": "KFM HUC12 Administrative Crosswalk",
        "dct:description": "Candidate dataset metadata for governed HUC12 to administrative boundary crosswalk pairs.",
        "dct:identifier": f"{COLLECTION_ID}-{run_id}",
        "dct:issued": now,
        "dct:modified": now,
        "kfm:run_receipt_id": receipt_id,
        "kfm:algorithm_version": algorithm_version,
        "kfm:source_snapshot_ids": source_snapshot_ids,
        "kfm:record_count": record_count,
        "kfm:publication_state": "candidate_no_publish"
    }

    prov = {
        "@context": {
            "prov": "http://www.w3.org/ns/prov#",
            "kfm": "https://kfm.local/ns#"
        },
        "@id": f"kfm://catalog/prov/crosswalk/{run_id}",
        "@type": "prov:Bundle",
        "prov:wasGeneratedBy": {
            "@id": receipt_id,
            "@type": "prov:Activity",
            "kfm:watcher": WATCHER,
            "kfm:algorithm_version": algorithm_version
        },
        "prov:used": [
            {
                "@id": snapshot_id,
                "@type": "prov:Entity"
            }
            for snapshot_id in source_snapshot_ids
        ],
        "prov:generated": {
            "@id": f"kfm://dataset/crosswalk/{run_id}",
            "@type": "prov:Entity",
            "kfm:record_count": record_count
        },
        "kfm:publication_state": "candidate_no_publish"
    }

    manifest = {
        "object_type": "crosswalk_catalog_manifest",
        "run_id": run_id,
        "run_receipt_id": receipt_id,
        "watcher": WATCHER,
        "algorithm_version": algorithm_version,
        "record_count": record_count,
        "source_snapshot_ids": source_snapshot_ids,
        "bbox_epsg_5070": bbox,
        "catalog_outputs": {
            "stac": str(stac_path),
            "dcat": str(dcat_path),
            "prov": str(prov_path)
        },
        "publication": {
            "published": False,
            "state": "candidate_no_publish",
            "reason": "catalog closure candidate only; promotion is separate"
        },
        "created_at": now
    }

    write_json(stac_path, stac)
    write_json(dcat_path, dcat)
    write_json(prov_path, prov)
    write_json(manifest_path, manifest)

    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Emit crosswalk STAC/DCAT/PROV catalog candidates.")
    parser.add_argument("--dsn", default=os.environ.get("DATABASE_URL"))
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--public-base-href", default="https://example.invalid/kfm")
    args = parser.parse_args()

    if not args.dsn:
        raise SystemExit("DATABASE_URL or --dsn is required")

    watcher_dir = Path(__file__).resolve().parent
    repo_root = watcher_dir.parents[2]

    manifest = build_catalog(
        dsn=args.dsn,
        run_id=args.run_id,
        repo_root=repo_root,
        public_base_href=args.public_base_href,
    )

    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"Command failed with exit code {exc.returncode}: {exc.cmd}", file=sys.stderr)
        if exc.stdout:
            print(exc.stdout, file=sys.stderr)
        if exc.stderr:
            print(exc.stderr, file=sys.stderr)
        raise
