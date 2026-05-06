"""
No-network fixture tests for the KFM HUC12 ↔ admin crosswalk watcher.

These tests require a PostGIS database.

Run manually:

  KFM_CROSSWALK_TEST_DSN="postgresql://postgres:postgres@localhost:5432/postgres" \
  python3 -m pytest -q tests/crosswalk/test_crosswalk_fixture.py
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
WATCHER_DIR = ROOT / "pipelines/watchers/hydrology_huc12_admin_crosswalk_watch"
RUNNER = WATCHER_DIR / "runner.py"
SCHEMA_SQL = WATCHER_DIR / "sql/001_schema.sql"


def require_command(name: str) -> None:
    if shutil.which(name) is None:
        pytest.skip(f"{name} is not installed")


def dsn() -> str:
    value = os.environ.get("KFM_CROSSWALK_TEST_DSN") or os.environ.get("DATABASE_URL")
    if not value:
        pytest.skip("KFM_CROSSWALK_TEST_DSN or DATABASE_URL is required for PostGIS fixture test")
    return value


def run(cmd: list[str], *, cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )


def psql(sql: str) -> str:
    result = run(["psql", dsn(), "-v", "ON_ERROR_STOP=1", "-Atc", sql])
    return result.stdout.strip()


def setup_fixture() -> None:
    run(["psql", dsn(), "-v", "ON_ERROR_STOP=1", "-f", str(SCHEMA_SQL)])

    psql(
        """
        TRUNCATE TABLE
          kfm_crosswalk.crosswalk_pairs,
          kfm_crosswalk.huc12_processed,
          kfm_crosswalk.admin_processed,
          kfm_crosswalk.source_snapshot
        CASCADE;

        INSERT INTO kfm_crosswalk.source_snapshot (
          source_snapshot_id,
          source_id,
          source_uri,
          checksum_or_etag,
          vintage,
          metadata
        )
        VALUES
          (
            'fixture:wbd:huc12',
            'usgs_wbd_huc12',
            'fixture://wbd/huc12',
            'sha256:fixture-wbd',
            'fixture',
            '{"fixture": true}'::jsonb
          ),
          (
            'fixture:tiger:county',
            'census_tiger_county',
            'fixture://tiger/county',
            'sha256:fixture-county',
            'fixture',
            '{"fixture": true}'::jsonb
          );

        INSERT INTO kfm_crosswalk.huc12_processed (
          huc12_id,
          source_snapshot_id,
          geom
        )
        VALUES (
          '102701010101',
          'fixture:wbd:huc12',
          ST_Multi(
            ST_MakeEnvelope(0, 0, 1000, 1000, 5070)
          )::geometry(MultiPolygon, 5070)
        );

        INSERT INTO kfm_crosswalk.admin_processed (
          admin_id,
          admin_type,
          source_snapshot_id,
          geom
        )
        VALUES
          (
            '20001',
            'county',
            'fixture:tiger:county',
            ST_Multi(
              ST_MakeEnvelope(0, 0, 600, 1000, 5070)
            )::geometry(MultiPolygon, 5070)
          ),
          (
            '20003',
            'county',
            'fixture:tiger:county',
            ST_Multi(
              ST_MakeEnvelope(600, 0, 1000, 1000, 5070)
            )::geometry(MultiPolygon, 5070)
          );
        """
    )


@pytest.mark.integration
def test_crosswalk_fixture_builds_pairs_and_receipt() -> None:
    require_command("psql")
    require_command("python3")

    if not RUNNER.exists():
        pytest.skip(f"missing watcher runner: {RUNNER}")

    setup_fixture()

    run_id = "pytest-crosswalk-fixture"
    receipt_path = ROOT / "data/receipts/crosswalk" / f"{run_id}.json"

    if receipt_path.exists():
        receipt_path.unlink()

    result = run(
        [
            "python3",
            str(RUNNER),
            "--dsn",
            dsn(),
            "--run-id",
            run_id,
            "--no-publish",
        ]
    )

    assert "run_receipt" in result.stdout
    assert receipt_path.exists()

    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))

    assert receipt["object_type"] == "run_receipt"
    assert receipt["run_id"] == run_id
    assert receipt["publication"]["published"] is False
    assert receipt["crs"] == "EPSG:5070"
    assert receipt["record_count"] == 2
    assert receipt["anomaly_count"] == 0

    row_count = int(
        psql(
            """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = 'run_receipt:hydrology_huc12_admin_crosswalk_watch:pytest-crosswalk-fixture';
            """
        )
    )

    assert row_count == 2


@pytest.mark.integration
def test_crosswalk_fixture_metrics_and_hashes_are_valid() -> None:
    require_command("psql")
    require_command("python3")

    setup_fixture()

    run_id = "pytest-crosswalk-fixture-metrics"

    run(
        [
            "python3",
            str(RUNNER),
            "--dsn",
            dsn(),
            "--run-id",
            run_id,
            "--no-publish",
        ]
    )

    failures = int(
        psql(
            """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = 'run_receipt:hydrology_huc12_admin_crosswalk_watch:pytest-crosswalk-fixture-metrics'
              AND (
                overlap_m2 < 0
                OR overlap_m2 > huc_area_m2
                OR overlap_m2 > admin_area_m2
                OR overlap_pct_huc < 0
                OR overlap_pct_huc > 1
                OR overlap_pct_admin < 0
                OR overlap_pct_admin > 1
                OR weight < 0
                OR weight > 1
                OR crs <> 'EPSG:5070'
                OR geometry_hash !~ '^sha256:[a-f0-9]{64}$'
                OR spec_hash !~ '^sha256:[a-f0-9]{64}$'
              );
            """
        )
    )

    assert failures == 0

    primary_count = int(
        psql(
            """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = 'run_receipt:hydrology_huc12_admin_crosswalk_watch:pytest-crosswalk-fixture-metrics'
              AND assignment_method = 'primary_overlap_ge_50pct_huc';
            """
        )
    )

    assert primary_count == 1

    total_weight = float(
        psql(
            """
            SELECT round(sum(weight)::numeric, 6)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = 'run_receipt:hydrology_huc12_admin_crosswalk_watch:pytest-crosswalk-fixture-metrics';
            """
        )
    )

    assert total_weight == 1.0
