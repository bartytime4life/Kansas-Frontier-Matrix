#!/usr/bin/env python3
"""
KFM TIGER administrative boundary ingest.

Loads a local Census TIGER polygon file into:

  kfm_crosswalk.admin_processed

This script is local-file first. It does not download live data, publish outputs,
or create release artifacts.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


TARGET_SRID = "5070"
DEFAULT_TABLE = "kfm_crosswalk.admin_processed"


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def psql(dsn: str, sql: str) -> None:
    run(["psql", dsn, "-v", "ON_ERROR_STOP=1", "-c", sql])


def sql_quote(value: str) -> str:
    return value.replace("'", "''")


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

    CREATE TABLE IF NOT EXISTS kfm_crosswalk.admin_processed (
      admin_id text NOT NULL,
      admin_type text NOT NULL CHECK (admin_type IN ('county', 'place', 'county_subdivision', 'mcd')),
      source_snapshot_id text NOT NULL REFERENCES kfm_crosswalk.source_snapshot(source_snapshot_id),
      geom geometry(MultiPolygon, 5070) NOT NULL,
      area_m2 double precision GENERATED ALWAYS AS (ST_Area(geom)) STORED,
      PRIMARY KEY (admin_id, admin_type, source_snapshot_id)
    );

    CREATE INDEX IF NOT EXISTS admin_processed_geom_gix
      ON kfm_crosswalk.admin_processed USING gist (geom);
    """
    psql(dsn, sql)


def register_snapshot(
    dsn: str,
    source_snapshot_id: str,
    source_uri: str,
    checksum_or_etag: str,
    vintage: str,
    admin_type: str,
) -> None:
    source_id = f"census_tiger_{admin_type}"

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
      '{sql_quote(source_snapshot_id)}',
      '{sql_quote(source_id)}',
      '{sql_quote(source_uri)}',
      '{sql_quote(checksum_or_etag)}',
      '{sql_quote(vintage)}',
      '{{"ingest": "ingest_tiger_admin.py", "role": "administrative_boundary_source", "admin_type": "{sql_quote(admin_type)}"}}'::jsonb
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


def normalize_admin(
    dsn: str,
    raw_table: str,
    admin_id_column: str,
    admin_type: str,
    source_snapshot_id: str,
    replace_existing: bool,
) -> None:
    delete_sql = ""
    if replace_existing:
        delete_sql = f"""
        DELETE FROM kfm_crosswalk.admin_processed
        WHERE source_snapshot_id = '{sql_quote(source_snapshot_id)}'
          AND admin_type = '{sql_quote(admin_type)}';
        """

    sql = f"""
    {delete_sql}

    INSERT INTO kfm_crosswalk.admin_processed (
      admin_id,
      admin_type,
      source_snapshot_id,
      geom
    )
    SELECT
      {admin_id_column}::text AS admin_id,
      '{sql_quote(admin_type)}' AS admin_type,
      '{sql_quote(source_snapshot_id)}' AS source_snapshot_id,
      ST_Multi(
        ST_CollectionExtract(
          ST_MakeValid(
            ST_Transform(geom, {TARGET_SRID})
          ),
          3
        )
      )::geometry(MultiPolygon, {TARGET_SRID}) AS geom
    FROM {raw_table}
    WHERE {admin_id_column} IS NOT NULL
      AND geom IS NOT NULL
      AND NOT ST_IsEmpty(geom)
    ON CONFLICT (admin_id, admin_type, source_snapshot_id) DO UPDATE SET
      geom = EXCLUDED.geom;
    """
    psql(dsn, sql)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ingest local Census TIGER administrative polygons into KFM crosswalk PostGIS tables."
    )

    parser.add_argument("--dsn", required=True, help="PostgreSQL DSN")
    parser.add_argument("--input", required=True, help="Local TIGER polygon file path")
    parser.add_argument("--layer", default=None, help="Optional OGR layer name")
    parser.add_argument(
        "--admin-type",
        required=True,
        choices=["county", "place", "county_subdivision", "mcd"],
        help="Administrative boundary type",
    )
    parser.add_argument(
        "--admin-id-column",
        default="geoid",
        help="TIGER identifier column, usually GEOID/geoid",
    )
    parser.add_argument("--source-snapshot-id", required=True)
    parser.add_argument("--source-uri", required=True)
    parser.add_argument("--checksum-or-etag", required=True)
    parser.add_argument("--vintage", required=True)
    parser.add_argument(
        "--raw-table",
        default="kfm_crosswalk.tiger_admin_raw",
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
        admin_type=args.admin_type,
    )

    load_raw_layer(
        dsn=args.dsn,
        input_path=input_path,
        raw_table=args.raw_table,
        layer_name=args.layer,
    )

    normalize_admin(
        dsn=args.dsn,
        raw_table=args.raw_table,
        admin_id_column=args.admin_id_column,
        admin_type=args.admin_type,
        source_snapshot_id=args.source_snapshot_id,
        replace_existing=args.replace_existing,
    )

    print(
        "ingest_tiger_admin: completed "
        f"source_snapshot_id={args.source_snapshot_id} "
        f"admin_type={args.admin_type} "
        f"target_table={DEFAULT_TABLE}"
    )

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"Command failed with exit code {exc.returncode}: {exc.cmd}", file=sys.stderr)
        raise
