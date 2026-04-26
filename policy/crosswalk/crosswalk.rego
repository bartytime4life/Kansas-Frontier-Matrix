package kfm.crosswalk

default allow := false

# -----------------------------
# Core geometry / CRS rules
# -----------------------------

deny[msg] {
  input.crs != "EPSG:5070"
  msg := "crosswalk must use EPSG:5070 for area math"
}

deny[msg] {
  input.overlap_m2 < 0
  msg := "overlap_m2 cannot be negative"
}

deny[msg] {
  input.overlap_m2 > input.huc_area_m2
  msg := "overlap exceeds HUC area"
}

deny[msg] {
  input.overlap_m2 > input.admin_area_m2
  msg := "overlap exceeds admin area"
}

# -----------------------------
# Percent + weight constraints
# -----------------------------

deny[msg] {
  input.overlap_pct_huc < 0
  msg := "overlap_pct_huc < 0"
}

deny[msg] {
  input.overlap_pct_huc > 1
  msg := "overlap_pct_huc > 1"
}

deny[msg] {
  input.overlap_pct_admin < 0
  msg := "overlap_pct_admin < 0"
}

deny[msg] {
  input.overlap_pct_admin > 1
  msg := "overlap_pct_admin > 1"
}

deny[msg] {
  input.weight < 0
  msg := "weight < 0"
}

deny[msg] {
  input.weight > 1
  msg := "weight > 1"
}

# -----------------------------
# Deterministic identity
# -----------------------------

deny[msg] {
  not startswith(input.geometry_hash, "sha256:")
  msg := "missing geometry_hash"
}

deny[msg] {
  not startswith(input.spec_hash, "sha256:")
  msg := "missing spec_hash"
}

# -----------------------------
# Provenance / source control
# -----------------------------

deny[msg] {
  count(input.source_snapshot_ids) < 2
  msg := "must include both source snapshot ids"
}

# -----------------------------
# Assignment sanity
# -----------------------------

deny[msg] {
  input.assignment_method == "primary_overlap_ge_50pct_huc"
  input.overlap_pct_huc < 0.50
  msg := "primary assignment requires >= 50% HUC overlap"
}

# -----------------------------
# Required fields presence
# -----------------------------

deny[msg] {
  not input.huc12_id
  msg := "missing huc12_id"
}

deny[msg] {
  not input.admin_id
  msg := "missing admin_id"
}

deny[msg] {
  not input.admin_type
  msg := "missing admin_type"
}

deny[msg] {
  not input.run_receipt_id
  msg := "missing run_receipt_id"
}

# -----------------------------
# Allow rule
# -----------------------------

allow {
  count(deny) == 0
}
