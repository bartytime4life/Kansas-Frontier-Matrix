package kfm.crosswalk

default allow := false

valid_admin_types := {
  "county",
  "place",
  "county_subdivision",
  "mcd",
}

valid_assignment_methods := {
  "primary_overlap_ge_50pct_huc",
  "fractional_weight",
  "centroid_tie_break",
  "stable_fips_tie_break",
}

# -----------------------------
# Required fields
# -----------------------------

deny[msg] {
  not input.huc12_id
  msg := "missing huc12_id"
}

deny[msg] {
  not regex.match("^[0-9]{12}$", input.huc12_id)
  msg := "huc12_id must be 12 digits"
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
  input.admin_type
  not valid_admin_types[input.admin_type]
  msg := "invalid admin_type"
}

deny[msg] {
  not input.run_receipt_id
  msg := "missing run_receipt_id"
}

# -----------------------------
# Core geometry / CRS rules
# -----------------------------

deny[msg] {
  input.crs != "EPSG:5070"
  msg := "crosswalk must use EPSG:5070 for area math"
}

deny[msg] {
  input.huc_area_m2 <= 0
  msg := "huc_area_m2 must be positive"
}

deny[msg] {
  input.admin_area_m2 <= 0
  msg := "admin_area_m2 must be positive"
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
  not input.geometry_hash
  msg := "missing geometry_hash"
}

deny[msg] {
  input.geometry_hash
  not regex.match("^sha256:[a-f0-9]{64}$", input.geometry_hash)
  msg := "invalid geometry_hash"
}

deny[msg] {
  not input.spec_hash
  msg := "missing spec_hash"
}

deny[msg] {
  input.spec_hash
  not regex.match("^sha256:[a-f0-9]{64}$", input.spec_hash)
  msg := "invalid spec_hash"
}

# -----------------------------
# Provenance / source control
# -----------------------------

deny[msg] {
  not input.source_snapshot_ids
  msg := "missing source_snapshot_ids"
}

deny[msg] {
  count(input.source_snapshot_ids) < 2
  msg := "must include both source snapshot ids"
}

# -----------------------------
# Assignment sanity
# -----------------------------

deny[msg] {
  not input.assignment_method
  msg := "missing assignment_method"
}

deny[msg] {
  input.assignment_method
  not valid_assignment_methods[input.assignment_method]
  msg := "invalid assignment_method"
}

deny[msg] {
  input.assignment_method == "primary_overlap_ge_50pct_huc"
  input.overlap_pct_huc < 0.50
  msg := "primary assignment requires >= 50% HUC overlap"
}

# -----------------------------
# Allow rule
# -----------------------------

allow {
  count(deny) == 0
}
