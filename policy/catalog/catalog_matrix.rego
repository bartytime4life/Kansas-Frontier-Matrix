package kfm.catalog.matrix

default pass := false

required_refs := {
  "stac_item_ref",
  "dcat_dataset_ref",
  "prov_sidecar_ref",
  "release_manifest_ref",
  "proof_pack_ref",
}

deny[msg] {
  some key in required_refs
  not input[key]
  msg := sprintf("catalog matrix missing %v", [key])
}

deny[msg] {
  input["closure_status"] != "closed"
  msg := "catalog matrix closure_status must be closed"
}

deny[msg] {
  raw_ref(input)
  msg := "catalog matrix references RAW / WORK / QUARANTINE material"
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

pass {
  count(deny) == 0
}
