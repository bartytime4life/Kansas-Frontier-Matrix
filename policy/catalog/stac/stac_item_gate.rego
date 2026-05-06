package kfm.catalog.stac

default allow := false

blocked_public_values := {
  "todo",
  "unknown",
  "needs-verification",
  "restricted",
  "deny",
  "",
}

deny[msg] {
  input["type"] != "Feature"
  msg := "STAC item must be a GeoJSON Feature"
}

deny[msg] {
  input["stac_version"] == ""
  msg := "STAC item missing stac_version"
}

deny[msg] {
  not input["properties"]["datetime"]
  msg := "STAC item missing properties.datetime"
}

deny[msg] {
  input["properties"]["kfm:policy_label"] != "public"
  msg := "public STAC export requires properties.kfm:policy_label=public"
}

deny[msg] {
  input["properties"]["kfm:sensitivity"]
  input["properties"]["kfm:sensitivity"] != "public"
  msg := "public STAC export requires properties.kfm:sensitivity=public when provided"
}

deny[msg] {
  not input["properties"]["kfm:spec_hash"]
  msg := "STAC item missing properties.kfm:spec_hash"
}

deny[msg] {
  not input["properties"]["kfm:evidence_ref"]
  msg := "STAC item missing properties.kfm:evidence_ref"
}

deny[msg] {
  not input["properties"]["kfm:release_manifest_ref"]
  msg := "STAC item missing properties.kfm:release_manifest_ref"
}

deny[msg] {
  not input["properties"]["kfm:source_role"]
  msg := "STAC item missing properties.kfm:source_role"
}

deny[msg] {
  review := input["properties"]["kfm:review_state"]
  review != "reviewed"
  review != "published"
  msg := "public STAC export requires properties.kfm:review_state reviewed or published"
}

deny[msg] {
  not input["assets"]["provenance"]
  msg := "STAC item missing assets.provenance"
}

deny[msg] {
  raw_ref(input)
  msg := "public STAC export references RAW / WORK / QUARANTINE material"
}

is_blocked_public_value(value) {
  is_string(value)
  blocked_public_values[lower(value)]
}

deny[msg] {
  license := input["properties"]["license"]
  is_blocked_public_value(license)
  msg := "STAC item properties.license cannot be TODO, unknown, restricted, deny, or empty"
}

raw_ref(x) {
  is_string(x)
  contains(lower(x), "data/raw/")
}

raw_ref(x) {
  is_string(x)
  contains(lower(x), "data/work/")
}

raw_ref(x) {
  is_string(x)
  contains(lower(x), "data/quarantine/")
}

raw_ref(x) {
  is_object(x)
  some k
  raw_ref(x[k])
}

raw_ref(x) {
  is_array(x)
  some i
  raw_ref(x[i])
}

allow {
  count(deny) == 0
}
