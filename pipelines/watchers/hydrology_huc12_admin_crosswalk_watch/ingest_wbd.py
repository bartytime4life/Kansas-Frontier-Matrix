#!/usr/bin/env python3
"""
KFM HUC12 WBD ingest.

Loads a local WBD polygon file into:

  kfm_crosswalk.huc12_processed

This script is intentionally local-file first. It does not download live data,
publish outputs, or create release artifacts.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


DEFAULT_TABLE = "kfm_crosswalk.huc12_processed"
DEFAULT_SOURCE_TABLE = "kfm_crosswalk.source_snapshot"
TARGET_SRID = "5070"


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def psql(dsn: str, sql: str) -> None:
    run(["psql", dsn, "-v", "ON_ERROR_STOP=1", "-c", sql])


def require_file(path: Path) -> None:
    if not path.exists():
        raise SystemExit(f"Input file does not exist: {path}")
    if not path.is_file():
        raise SystemExit(f"Input path is not a file: {path}")


def ensure_schema(dsn: str) -> None:
    sql = """
    CREATE SCHEMA IF NOT EXISTS kfm_crosswalk;

    CREATE EXTENSION IF NOT EXISTS postgis;

    CREATE TABLE IF NOT EXISTS kfm_crosswalk.source_snapshot (
      source_snapshot_id text PRIMARY KEY,
      source_id text NOT NULL,
      source_uri text NOT NULL,
      access_date timestamptz NOT NULL DEFAULT now(),
      checksum_or_etag text NOT NULL,
      vintage text NOT NULL,
      metadata jsonb NOT NULL DEFAULT '{}'::jsonb
    );

    CREATE TABLE IF NOT EXISTS kfm_crosswalk.huc12_processed (
      huc12_id text PRIMARY KEY CHECK (huc12_id ~ '^[0-9]{12}$'),
      source_snapshot_id text NOT NULL REFERENCES kfm_crosswalk.source_snapshot(source_snapshot_id),
      geom geometry(MultiPolygon, 5070) NOT NULL,
      area_m2 double precision GENERATED ALWAYS AS (ST_Area(geom)) STORED
    );

    CREATE INDEX IF NOT EXISTS huc12_processed_geom_gix
      ON kfm_crosswalk.huc12_processed USING gist (geom);
    """
    psql(dsn, sql)


def register_snapshot(
    dsn: str,
    source_snapshot_id: str,
    source_uri: str,
    checksum_or_etag: str,
    vintage: str,
) -> None:
    sql = f"""
    INSERT INTO kfm_crosswalk.source_snapshot (
      source_snapshot_id,
      source_id,
      source_uri,
      checksum_or_etag,
      vintage,
      metadata
    )
    VALUES (
      '{source_snapshot_id}',
      'usgs_wbd_huc12',
      '{source_uri}',
      '{checksum_or_etag}',
      '{vintage}',
      '{{"ingest": "ingest_wbd.py", "role": "hydrologic_boundary_source"}}'::jsonb
    )
    ON CONFLICT (source_snapshot_id) DO UPDATE SET
      source_uri = EXCLUDED.source_uri,
      checksum_or_etag = EXCLUDED.checksum_or_etag,
      vintage = EXCLUDED.vintage,
      metadata = EXCLUDED.metadata;
    """
    psql(dsn, sql)


def load_raw_layer(
    dsn: str,
    input_path: Path,
    raw_table: str,
    layer_name: str | None,
) -> None:
    table_name = raw_table.split(".", 1)[1]

    psql(dsn, f"DROP TABLE IF EXISTS {raw_table};")

    cmd = [
        "ogr2ogr",
        "-f",
        "PostgreSQL",
        f"PG:{dsn}",
        str(input_path),
        "-nln",
        raw_table,
        "-overwrite",
        "-lco",
        "GEOMETRY_NAME=geom",
        "-lco",
        "FID=ogc_fid",
        "-nlt",
        "PROMOTE_TO_MULTI",
    ]

    if layer_name:
        cmd.append(layer_name)

    run(cmd)

    psql(
        dsn,
        f"""
        ALTER TABLE {raw_table}
          ALTER COLUMN geom TYPE geometry(MultiPolygon, ST_SRID(geom))
          USING ST_Multi(ST_CollectionExtract(ST_MakeValid(geom), 3));
        """,
    )


def normalize_huc12(
    dsn: str,
    raw_table: str,
    huc12_column: str,
    source_snapshot_id: str,
    replace_existing: bool,
) -> None:
    delete_sql = ""
    if replace_existing:
        delete_sql = f"""
        DELETE FROM kfm_crosswalk.huc12_processed
        WHERE source_snapshot_id = '{source_snapshot_id}';
        """

    sql = f"""
    {delete_sql}

    INSERT INTO kfm_crosswalk.huc12_processed (
      huc12_id,
      source_snapshot_id,
      geom
    )
    SELECT
      {huc12_column}::text AS huc12_id,
      '{source_snapshot_id}' AS source_snapshot_id,
      ST_Multi(
        ST_CollectionExtract(
          ST_MakeValid(
            ST_Transform(geom, {TARGET_SRID})
          ),
          3
        )
      )::geometry(MultiPolygon, {TARGET_SRID}) AS geom
    FROM {raw_table}
    WHERE {huc12_column} IS NOT NULL
      AND {huc12_column}::text ~ '^[0-9]{{12}}$'
      AND geom IS NOT NULL
      AND NOT ST_IsEmpty(geom)
    ON CONFLICT (huc12_id) DO UPDATE SET
      source_snapshot_id = EXCLUDED.source_snapshot_id,
      geom = EXCLUDED.geom;
    """
    psql(dsn, sql)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ingest local USGS WBD HUC12 polygons into KFM crosswalk PostGIS tables."
    )
    parser.add_argument("--dsn", required=True, help="PostgreSQL DSN")
    parser.add_argument("--input", required=True, help="Local WBD file path")
    parser.add_argument("--layer", default=None, help="Optional OGR layer name")
    parser.add_argument("--huc12-column", default="huc12", help="HUC12 attribute column")
    parser.add_argument("--source-snapshot-id", required=True)
    parser.add_argument("--source-uri", required=True)
    parser.add_argument("--checksum-or-etag", required=True)
    parser.add_argument("--vintage", required=True)
    parser.add_argument(
        "--raw-table",
        default="kfm_crosswalk.wbd_huc12_raw",
        help="Temporary raw table name",
    )
    parser.add_argument(
        "--replace-existing",
        action="store_true",
        help="Delete rows from the same source snapshot before loading",
    )

    args = parser.parse_args()
    input_path = Path(args.input).resolve()

    require_file(input_path)
    ensure_schema(args.dsn)
    register_snapshot(
        dsn=args.dsn,
        source_snapshot_id=args.source_snapshot_id,
        source_uri=args.source_uri,
        checksum_or_etag=args.checksum_or_etag,
        vintage=args.vintage,
    )
    load_raw_layer(
        dsn=args.dsn,
        input_path=input_path,
        raw_table=args.raw_table,
        layer_name=args.layer,
    )
    normalize_huc12(
        dsn=args.dsn,
        raw_table=args.raw_table,
        huc12_column=args.huc12_column,
        source_snapshot_id=args.source_snapshot_id,
        replace_existing=args.replace_existing,
    )

    print(
        "ingest_wbd: completed "
        f"source_snapshot_id={args.source_snapshot_id} "
        f"target_table={DEFAULT_TABLE}"
    )

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"Command failed with exit code {exc.returncode}: {exc.cmd}", file=sys.stderr)
        raise
