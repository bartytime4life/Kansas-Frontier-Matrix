-- KFM HUC12 ↔ administrative boundary crosswalk schema
--
-- Provides PostGIS tables for:
--   - source snapshots
--   - processed HUC12 polygons
--   - processed administrative polygons
--   - generated crosswalk pair candidates
--
-- This schema is candidate-generation infrastructure only.
-- Publication and promotion remain separate governed steps.

CREATE SCHEMA IF NOT EXISTS kfm_crosswalk;

CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS kfm_crosswalk.source_snapshot (
  source_snapshot_id text PRIMARY KEY,
  source_id text NOT NULL,
  source_uri text NOT NULL,
  access_date timestamptz NOT NULL DEFAULT now(),
  checksum_or_etag text NOT NULL,
  vintage text NOT NULL,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS kfm_crosswalk.huc12_processed (
  huc12_id text PRIMARY KEY CHECK (huc12_id ~ '^[0-9]{12}$'),
  source_snapshot_id text NOT NULL REFERENCES kfm_crosswalk.source_snapshot(source_snapshot_id),
  geom geometry(MultiPolygon, 5070) NOT NULL,
  area_m2 double precision GENERATED ALWAYS AS (ST_Area(geom)) STORED,
  created_at timestamptz NOT NULL DEFAULT now(),

  CONSTRAINT huc12_processed_area_positive
    CHECK (ST_Area(geom) > 0),

  CONSTRAINT huc12_processed_valid_geom
    CHECK (ST_IsValid(geom))
);

CREATE TABLE IF NOT EXISTS kfm_crosswalk.admin_processed (
  admin_id text NOT NULL,
  admin_type text NOT NULL CHECK (
    admin_type IN ('county', 'place', 'county_subdivision', 'mcd')
  ),
  source_snapshot_id text NOT NULL REFERENCES kfm_crosswalk.source_snapshot(source_snapshot_id),
  geom geometry(MultiPolygon, 5070) NOT NULL,
  area_m2 double precision GENERATED ALWAYS AS (ST_Area(geom)) STORED,
  created_at timestamptz NOT NULL DEFAULT now(),

  PRIMARY KEY (admin_id, admin_type, source_snapshot_id),

  CONSTRAINT admin_processed_area_positive
    CHECK (ST_Area(geom) > 0),

  CONSTRAINT admin_processed_valid_geom
    CHECK (ST_IsValid(geom))
);

CREATE TABLE IF NOT EXISTS kfm_crosswalk.crosswalk_pairs (
  crosswalk_pair_id text PRIMARY KEY,

  huc12_id text NOT NULL CHECK (huc12_id ~ '^[0-9]{12}$'),
  admin_id text NOT NULL,
  admin_type text NOT NULL CHECK (
    admin_type IN ('county', 'place', 'county_subdivision', 'mcd')
  ),

  huc_area_m2 double precision NOT NULL CHECK (huc_area_m2 > 0),
  admin_area_m2 double precision NOT NULL CHECK (admin_area_m2 > 0),
  overlap_m2 double precision NOT NULL CHECK (overlap_m2 >= 0),

  overlap_pct_huc double precision NOT NULL CHECK (
    overlap_pct_huc >= 0 AND overlap_pct_huc <= 1
  ),
  overlap_pct_admin double precision NOT NULL CHECK (
    overlap_pct_admin >= 0 AND overlap_pct_admin <= 1
  ),
  weight double precision NOT NULL CHECK (
    weight >= 0 AND weight <= 1
  ),

  assignment_method text NOT NULL CHECK (
    assignment_method IN (
      'primary_overlap_ge_50pct_huc',
      'fractional_weight',
      'centroid_tie_break',
      'stable_fips_tie_break'
    )
  ),

  centroid_within_flag boolean NOT NULL DEFAULT false,
  shared_boundary_m double precision CHECK (
    shared_boundary_m IS NULL OR shared_boundary_m >= 0
  ),

  source_snapshot_ids text[] NOT NULL CHECK (
    array_length(source_snapshot_ids, 1) >= 2
  ),

  algorithm_version text NOT NULL,
  crs text NOT NULL DEFAULT 'EPSG:5070' CHECK (crs = 'EPSG:5070'),

  geometry_hash text NOT NULL CHECK (
    geometry_hash ~ '^sha256:[a-f0-9]{64}$'
  ),
  spec_hash text NOT NULL CHECK (
    spec_hash ~ '^sha256:[a-f0-9]{64}$'
  ),

  run_receipt_id text NOT NULL,

  intersection_geom geometry(MultiPolygon, 5070) NOT NULL,

  created_at timestamptz NOT NULL DEFAULT now(),

  CONSTRAINT crosswalk_overlap_not_gt_huc
    CHECK (overlap_m2 <= huc_area_m2),

  CONSTRAINT crosswalk_overlap_not_gt_admin
    CHECK (overlap_m2 <= admin_area_m2),

  CONSTRAINT crosswalk_intersection_valid_geom
    CHECK (ST_IsValid(intersection_geom)),

  CONSTRAINT crosswalk_intersection_area_positive
    CHECK (ST_Area(intersection_geom) > 0)
);

CREATE INDEX IF NOT EXISTS huc12_processed_geom_gix
  ON kfm_crosswalk.huc12_processed
  USING gist (geom);

CREATE INDEX IF NOT EXISTS admin_processed_geom_gix
  ON kfm_crosswalk.admin_processed
  USING gist (geom);

CREATE INDEX IF NOT EXISTS crosswalk_pairs_geom_gix
  ON kfm_crosswalk.crosswalk_pairs
  USING gist (intersection_geom);

CREATE INDEX IF NOT EXISTS crosswalk_pairs_huc12_idx
  ON kfm_crosswalk.crosswalk_pairs (huc12_id);

CREATE INDEX IF NOT EXISTS crosswalk_pairs_admin_idx
  ON kfm_crosswalk.crosswalk_pairs (admin_type, admin_id);

CREATE INDEX IF NOT EXISTS crosswalk_pairs_run_receipt_idx
  ON kfm_crosswalk.crosswalk_pairs (run_receipt_id);

CREATE INDEX IF NOT EXISTS crosswalk_pairs_spec_hash_idx
  ON kfm_crosswalk.crosswalk_pairs (spec_hash);

CREATE INDEX IF NOT EXISTS crosswalk_pairs_geometry_hash_idx
  ON kfm_crosswalk.crosswalk_pairs (geometry_hash);
