-- KFM HUC12 ↔ administrative boundary crosswalk builder
--
-- Required psql variables:
--   run_receipt_id
--   algorithm_version
--
-- Inputs:
--   kfm_crosswalk.huc12_processed
--   kfm_crosswalk.admin_processed
--
-- Output:
--   kfm_crosswalk.crosswalk_pairs

WITH intersections AS (
  SELECT
    h.huc12_id,
    a.admin_id,
    a.admin_type,
    h.area_m2 AS huc_area_m2,
    a.area_m2 AS admin_area_m2,
    h.source_snapshot_id AS huc_snapshot_id,
    a.source_snapshot_id AS admin_snapshot_id,
    ST_Multi(
      ST_CollectionExtract(
        ST_MakeValid(
          ST_Intersection(h.geom, a.geom)
        ),
        3
      )
    )::geometry(MultiPolygon, 5070) AS intersection_geom,
    ST_Contains(a.geom, ST_PointOnSurface(h.geom)) AS centroid_within_flag
  FROM kfm_crosswalk.huc12_processed h
  JOIN kfm_crosswalk.admin_processed a
    ON ST_Intersects(h.geom, a.geom)
),

measured AS (
  SELECT
    *,
    ST_Area(intersection_geom) AS overlap_m2
  FROM intersections
  WHERE intersection_geom IS NOT NULL
    AND NOT ST_IsEmpty(intersection_geom)
),

ranked AS (
  SELECT
    *,
    overlap_m2 / NULLIF(huc_area_m2, 0) AS overlap_pct_huc,
    overlap_m2 / NULLIF(admin_area_m2, 0) AS overlap_pct_admin,
    overlap_m2 / NULLIF(huc_area_m2, 0) AS weight,
    ROW_NUMBER() OVER (
      PARTITION BY huc12_id, admin_type
      ORDER BY
        CASE
          WHEN overlap_m2 / NULLIF(huc_area_m2, 0) >= 0.50 THEN 0
          ELSE 1
        END,
        centroid_within_flag DESC,
        overlap_m2 DESC,
        admin_id ASC
    ) AS assignment_rank
  FROM measured
),

classified AS (
  SELECT
    *,
    CASE
      WHEN overlap_pct_huc >= 0.50 THEN 'primary_overlap_ge_50pct_huc'
      WHEN centroid_within_flag AND assignment_rank = 1 THEN 'centroid_tie_break'
      WHEN assignment_rank = 1 THEN 'stable_fips_tie_break'
      ELSE 'fractional_weight'
    END AS assignment_method
  FROM ranked
  WHERE overlap_m2 > 0
),

hashed AS (
  SELECT
    *,
    ARRAY[huc_snapshot_id, admin_snapshot_id] AS source_snapshot_ids,
    'EPSG:5070' AS crs,
    :'algorithm_version'::text AS algorithm_version_value,
    :'run_receipt_id'::text AS run_receipt_id_value,
    'sha256:' || encode(
      digest(ST_AsEWKB(intersection_geom), 'sha256'),
      'hex'
    ) AS geometry_hash
  FROM classified
),

speced AS (
  SELECT
    *,
    'sha256:' || encode(
      digest(
        jsonb_build_object(
          'huc12_id', huc12_id,
          'admin_id', admin_id,
          'admin_type', admin_type,
          'overlap_m2', round(overlap_m2::numeric, 6),
          'overlap_pct_huc', round(overlap_pct_huc::numeric, 12),
          'overlap_pct_admin', round(overlap_pct_admin::numeric, 12),
          'weight', round(weight::numeric, 12),
          'assignment_method', assignment_method,
          'algorithm_version', algorithm_version_value,
          'crs', crs,
          'source_snapshot_ids', source_snapshot_ids
        )::text,
        'sha256'
      ),
      'hex'
    ) AS spec_hash
  FROM hashed
)

INSERT INTO kfm_crosswalk.crosswalk_pairs (
  crosswalk_pair_id,
  huc12_id,
  admin_id,
  admin_type,
  huc_area_m2,
  admin_area_m2,
  overlap_m2,
  overlap_pct_huc,
  overlap_pct_admin,
  weight,
  assignment_method,
  centroid_within_flag,
  shared_boundary_m,
  source_snapshot_ids,
  algorithm_version,
  crs,
  geometry_hash,
  spec_hash,
  run_receipt_id,
  intersection_geom
)
SELECT
  'sha256:' || encode(
    digest(
      huc12_id || '|' ||
      admin_id || '|' ||
      admin_type || '|' ||
      geometry_hash || '|' ||
      spec_hash,
      'sha256'
    ),
    'hex'
  ) AS crosswalk_pair_id,
  huc12_id,
  admin_id,
  admin_type,
  huc_area_m2,
  admin_area_m2,
  overlap_m2,
  overlap_pct_huc,
  overlap_pct_admin,
  weight,
  assignment_method,
  centroid_within_flag,
  ST_Length(ST_Boundary(intersection_geom)) AS shared_boundary_m,
  source_snapshot_ids,
  algorithm_version_value,
  crs,
  geometry_hash,
  spec_hash,
  run_receipt_id_value,
  intersection_geom
FROM speced
ON CONFLICT (crosswalk_pair_id) DO UPDATE SET
  huc_area_m2 = EXCLUDED.huc_area_m2,
  admin_area_m2 = EXCLUDED.admin_area_m2,
  overlap_m2 = EXCLUDED.overlap_m2,
  overlap_pct_huc = EXCLUDED.overlap_pct_huc,
  overlap_pct_admin = EXCLUDED.overlap_pct_admin,
  weight = EXCLUDED.weight,
  assignment_method = EXCLUDED.assignment_method,
  centroid_within_flag = EXCLUDED.centroid_within_flag,
  shared_boundary_m = EXCLUDED.shared_boundary_m,
  source_snapshot_ids = EXCLUDED.source_snapshot_ids,
  algorithm_version = EXCLUDED.algorithm_version,
  crs = EXCLUDED.crs,
  geometry_hash = EXCLUDED.geometry_hash,
  spec_hash = EXCLUDED.spec_hash,
  run_receipt_id = EXCLUDED.run_receipt_id,
  intersection_geom = EXCLUDED.intersection_geom,
  created_at = now();
