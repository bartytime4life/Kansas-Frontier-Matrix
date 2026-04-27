package kfm.catalog.stac

default allow := false

deny[msg] {
  input.type != "Feature"
  msg := "STAC item must be GeoJSON Feature"
}

deny[msg] {
  not input.stac_version
  msg := "STAC item missing stac_version"
}

deny[msg] {
  not input.id
  msg := "STAC item missing id"
}

deny[msg] {
  not input.properties
  msg := "STAC item missing properties"
}

deny[msg] {
  input.properties["kfm:policy_label"] != "public"
  msg := "public STAC export requires kfm:policy_label=public"
}

deny[msg] {
  not input.properties["kfm:spec_hash"]
  msg := "STAC item missing spec_hash"
}

deny[msg] {
  not input.properties["kfm:evidence_ref"]
  msg := "STAC item missing evidence_ref"
}

deny[msg] {
  not input.properties["kfm:run_receipt_url"]
  msg := "STAC item missing run_receipt_url"
}

deny[msg] {
  not input.properties["kfm:release_manifest_ref"]
  msg := "STAC item missing release_manifest_ref"
}

deny[msg] {
  not input.properties["processing:software"]
  msg := "STAC item missing processing software"
}

deny[msg] {
  not input.properties["processing:version"]
  msg := "STAC item missing processing version"
}

deny[msg] {
  not input.properties["processing:datetime"]
  msg := "STAC item missing processing datetime"
}

deny[msg] {
  not has_link_rel("provenance")
  msg := "STAC item missing provenance link"
}

deny[msg] {
  not has_link_rel("evidence")
  msg := "STAC item missing evidence link"
}

deny[msg] {
  not has_link_rel("release-manifest")
  msg := "STAC item missing release-manifest link"
}

deny[msg] {
  not input.assets.data
  msg := "STAC item missing data asset"
}

deny[msg] {
  not input.assets.provenance
  msg := "STAC item missing provenance asset"
}

deny[msg] {
  raw_ref(input)
  msg := "public STAC export references RAW / WORK / QUARANTINE material"
}

has_link_rel(rel) {
  some i
  input.links[i].rel == rel
}

raw_ref(x) {
  is_string(x)
  contains(lower(x), "/raw/")
}

raw_ref(x) {
  is_string(x)
  contains(lower(x), "/work/")
}

raw_ref(x) {
  is_string(x)
  contains(lower(x), "/quarantine/")
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
