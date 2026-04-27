-- Crosswalk SQL validator
-- Returns validation failure counts by rule

SELECT 'negative_overlap' AS check_name, count(*) AS failures
FROM kfm_crosswalk.crosswalk_pairs
WHERE overlap_m2 < 0

UNION ALL

SELECT 'overlap_gt_huc_area', count(*)
FROM kfm_crosswalk.crosswalk_pairs
WHERE overlap_m2 > huc_area_m2

UNION ALL

SELECT 'overlap_gt_admin_area', count(*)
FROM kfm_crosswalk.crosswalk_pairs
WHERE overlap_m2 > admin_area_m2

UNION ALL

SELECT 'overlap_pct_huc_out_of_bounds', count(*)
FROM kfm_crosswalk.crosswalk_pairs
WHERE overlap_pct_huc < 0 OR overlap_pct_huc > 1

UNION ALL

SELECT 'overlap_pct_admin_out_of_bounds', count(*)
FROM kfm_crosswalk.crosswalk_pairs
WHERE overlap_pct_admin < 0 OR overlap_pct_admin > 1

UNION ALL

SELECT 'weight_out_of_bounds', count(*)
FROM kfm_crosswalk.crosswalk_pairs
WHERE weight < 0 OR weight > 1

UNION ALL

SELECT 'invalid_crs', count(*)
FROM kfm_crosswalk.crosswalk_pairs
WHERE crs <> 'EPSG:5070'

UNION ALL

SELECT 'missing_geometry_hash', count(*)
FROM kfm_crosswalk.crosswalk_pairs
WHERE geometry_hash !~ '^sha256:[a-f0-9]{64}$'

UNION ALL

SELECT 'missing_spec_hash', count(*)
FROM kfm_crosswalk.crosswalk_pairs
WHERE spec_hash !~ '^sha256:[a-f0-9]{64}$'

UNION ALL

SELECT 'missing_source_snapshots', count(*)
FROM kfm_crosswalk.crosswalk_pairs
WHERE array_length(source_snapshot_ids, 1) < 2

UNION ALL

SELECT 'invalid_assignment_primary_rule', count(*)
FROM kfm_crosswalk.crosswalk_pairs
WHERE assignment_method = 'primary_overlap_ge_50pct_huc'
  AND overlap_pct_huc < 0.5;
