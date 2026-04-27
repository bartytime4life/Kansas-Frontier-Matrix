package kfm.catalog.dcat

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
  input["@type"] != "dcat:Dataset"
  msg := "DCAT export must be dcat:Dataset"
}

deny[msg] {
  not input["dct:license"]
  msg := "dataset missing license"
}

deny[msg] {
  is_blocked_public_value(input["dct:license"])
  msg := "dataset license cannot be TODO, unknown, restricted, deny, or empty"
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
  input["kfm:sensitivity"]
  input["kfm:sensitivity"] != "public"
  msg := "public DCAT export requires kfm:sensitivity=public when provided"
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
  not input["kfm:source_role"]
  msg := "dataset missing source_role"
}

deny[msg] {
  input["kfm:review_state"] != "reviewed"
  input["kfm:review_state"] != "published"
  msg := "DCAT public export requires kfm:review_state reviewed or published"
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
  distribution["@type"] != "dcat:Distribution"
  msg := sprintf("distribution[%v] must be dcat:Distribution", [i])
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
  is_blocked_public_value(distribution["dct:license"])
  msg := sprintf("distribution[%v] license cannot be TODO, unknown, restricted, deny, or empty", [i])
}

deny[msg] {
  some i
  distribution := input["dcat:distribution"][i]
  distribution["dct:license"] != input["dct:license"]
  msg := sprintf("distribution[%v] license differs from dataset license; reviewed exception is not represented", [i])
}

deny[msg] {
  raw_ref(input)
  msg := "public DCAT export references RAW / WORK / QUARANTINE material"
}

is_blocked_public_value(value) {
  is_string(value)
  blocked_public_values[lower(value)]
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
