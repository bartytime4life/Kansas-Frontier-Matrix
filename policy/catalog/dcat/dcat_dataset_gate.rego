package kfm.catalog.dcat

default allow := false

deny[msg] {
  input["@type"] != "dcat:Dataset"
  msg := "DCAT export must be dcat:Dataset"
}

deny[msg] {
  not input["dct:license"]
  msg := "dataset missing license"
}

deny[msg] {
  input["dct:license"] == "TODO"
  msg := "dataset license cannot be TODO"
}

deny[msg] {
  lower(input["dct:license"]) == "unknown"
  msg := "dataset license cannot be unknown"
}

deny[msg] {
  input["dct:accessRights"] != "public"
  msg := "public DCAT export requires dct:accessRights=public"
}

deny[msg] {
  input["kfm:policy_label"] != "public"
  msg := "public DCAT export requires kfm:policy_label=public"
}

deny[msg] {
  not input["dct:provenance"]
  msg := "dataset missing provenance pointer"
}

deny[msg] {
  not input["kfm:spec_hash"]
  msg := "dataset missing spec_hash"
}

deny[msg] {
  not input["kfm:evidence_ref"]
  msg := "dataset missing evidence_ref"
}

deny[msg] {
  not input["kfm:release_manifest_ref"]
  msg := "dataset missing release_manifest_ref"
}

deny[msg] {
  not input["dcat:distribution"]
  msg := "dataset missing distribution"
}

deny[msg] {
  count(input["dcat:distribution"]) == 0
  msg := "dataset distribution cannot be empty"
}

deny[msg] {
  some i
  distribution := input["dcat:distribution"][i]
  not distribution["dcat:accessURL"]
  msg := sprintf("distribution[%v] missing accessURL", [i])
}

deny[msg] {
  some i
  distribution := input["dcat:distribution"][i]
  not distribution["dct:license"]
  msg := sprintf("distribution[%v] missing license", [i])
}

deny[msg] {
  some i
  distribution := input["dcat:distribution"][i]
  lower(distribution["dct:license"]) == "unknown"
  msg := sprintf("distribution[%v] license cannot be unknown", [i])
}

deny[msg] {
  raw_ref(input)
  msg := "public DCAT export references RAW / WORK / QUARANTINE material"
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
