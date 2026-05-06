-- KFM HUC12 ↔ Admin Crosswalk Fixture
-- No-network deterministic fixture for local + CI validation
-- Creates a single HUC12 split across two admin units

-- Ensure schema + PostGIS exist (safe if already applied)
CREATE SCHEMA IF NOT EXISTS kfm_crosswalk;
CREATE EXTENSION IF NOT EXISTS postgis;

-- Ensure required tables exist (aligns with 001_schema.sql)
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

CREATE TABLE IF NOT EXISTS kfm_crosswalk.admin_processed (
  admin_id text NOT NULL,
  admin_type text NOT NULL CHECK (admin_type IN ('county', 'place', 'county_subdivision', 'mcd')),
  source_snapshot_id text NOT NULL REFERENCES kfm_crosswalk.source_snapshot(source_snapshot_id),
  geom geometry(MultiPolygon, 5070) NOT NULL,
  area_m2 double precision GENERATED ALWAYS AS (ST_Area(geom)) STORED,
  PRIMARY KEY (admin_id, admin_type, source_snapshot_id)
);

CREATE TABLE IF NOT EXISTS kfm_crosswalk.crosswalk_pairs (
  crosswalk_pair_id text PRIMARY KEY,
  huc12_id text NOT NULL,
  admin_id text NOT NULL,
  admin_type text NOT NULL,
  huc_area_m2 double precision NOT NULL,
  admin_area_m2 double precision NOT NULL,
  overlap_m2 double precision NOT NULL,
  overlap_pct_huc double precision NOT NULL,
  overlap_pct_admin double precision NOT NULL,
  weight double precision NOT NULL,
  assignment_method text NOT NULL,
  centroid_within_flag boolean NOT NULL DEFAULT false,
  shared_boundary_m double precision,
  source_snapshot_ids text[] NOT NULL,
  algorithm_version text NOT NULL,
  crs text NOT NULL DEFAULT 'EPSG:5070',
  geometry_hash text NOT NULL,
  spec_hash text NOT NULL,
  run_receipt_id text NOT NULL,
  intersection_geom geometry(MultiPolygon, 5070) NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);

-- Reset state for deterministic runs
TRUNCATE TABLE
  kfm_crosswalk.crosswalk_pairs,
  kfm_crosswalk.huc12_processed,
  kfm_crosswalk.admin_processed,
  kfm_crosswalk.source_snapshot
CASCADE;

-- Register fixture source snapshots
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

-- Create one HUC12 polygon (1000m x 1000m square)
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

-- Create two admin polygons splitting the HUC
-- Left: 60% overlap
-- Right: 40% overlap
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

-- Verification (optional)
-- Expect:
-- - HUC area = 1,000,000 m²
-- - Admin areas = 600,000 and 400,000 m²
-- - Overlaps sum to HUC area

-- SELECT ST_Area(geom) FROM kfm_crosswalk.huc12_processed;
-- SELECT admin_id, ST_Area(geom) FROM kfm_crosswalk.admin_processed;
