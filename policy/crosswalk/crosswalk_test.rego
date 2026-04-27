package kfm.crosswalk

valid_pair := {
  "huc12_id": "102701010101",
  "admin_id": "20001",
  "admin_type": "county",
  "huc_area_m2": 1000000,
  "admin_area_m2": 600000,
  "overlap_m2": 600000,
  "overlap_pct_huc": 0.6,
  "overlap_pct_admin": 1,
  "weight": 0.6,
  "assignment_method": "primary_overlap_ge_50pct_huc",
  "source_snapshot_ids": ["fixture:wbd:huc12", "fixture:tiger:county"],
  "algorithm_version": "huc12_admin_crosswalk_v0.1.0",
  "crs": "EPSG:5070",
  "geometry_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "spec_hash": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
  "run_receipt_id": "run_receipt:hydrology_huc12_admin_crosswalk_watch:test"
}

test_valid_pair_allowed {
  allow with input as valid_pair
}

test_bad_crs_denied {
  deny[_] with input as object.union(valid_pair, {"crs": "EPSG:4326"})
}

test_negative_overlap_denied {
  deny[_] with input as object.union(valid_pair, {"overlap_m2": -1})
}

test_overlap_gt_huc_denied {
  deny[_] with input as object.union(valid_pair, {"overlap_m2": 1000001})
}

test_overlap_gt_admin_denied {
  deny[_] with input as object.union(valid_pair, {"overlap_m2": 600001})
}

test_bad_huc12_denied {
  deny[_] with input as object.union(valid_pair, {"huc12_id": "bad"})
}

test_bad_admin_type_denied {
  deny[_] with input as object.union(valid_pair, {"admin_type": "unsupported"})
}

test_missing_source_snapshots_denied {
  deny[_] with input as object.union(valid_pair, {"source_snapshot_ids": ["fixture:wbd:huc12"]})
}

test_bad_geometry_hash_denied {
  deny[_] with input as object.union(valid_pair, {"geometry_hash": "sha256:not-valid"})
}

test_bad_spec_hash_denied {
  deny[_] with input as object.union(valid_pair, {"spec_hash": "sha256:not-valid"})
}

test_primary_assignment_below_threshold_denied {
  deny[_] with input as object.union(valid_pair, {
    "overlap_pct_huc": 0.49,
    "assignment_method": "primary_overlap_ge_50pct_huc"
  })
}

test_fractional_assignment_below_threshold_allowed {
  allow with input as object.union(valid_pair, {
    "overlap_pct_huc": 0.49,
    "weight": 0.49,
    "assignment_method": "fractional_weight"
  })
}
