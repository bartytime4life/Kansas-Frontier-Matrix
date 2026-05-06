package kfm.provenance

default allow := false

blocked_public_values := {
  "TODO",
  "todo",
  "UNKNOWN",
  "unknown",
  "NEEDS-VERIFICATION",
  "restricted",
  "deny",
}

deny[msg] {
  not input.entity
  msg := "missing entity block"
}

deny[msg] {
  not input.activity
  msg := "missing activity block"
}

deny[msg] {
  not input.agent
  msg := "missing agent block"
}

deny[msg] {
  not input.wasGeneratedBy
  msg := "missing wasGeneratedBy relation"
}

deny[msg] {
  not input.wasAttributedTo
  msg := "missing wasAttributedTo relation"
}

deny[msg] {
  artifact_id := input.wasGeneratedBy["prov:entity"]
  not input.entity[artifact_id]
  msg := sprintf("wasGeneratedBy references missing entity: %v", [artifact_id])
}

deny[msg] {
  activity_id := input.wasGeneratedBy["prov:activity"]
  not input.activity[activity_id]
  msg := sprintf("wasGeneratedBy references missing activity: %v", [activity_id])
}

deny[msg] {
  agent_id := input.wasAttributedTo["prov:agent"]
  not input.agent[agent_id]
  msg := sprintf("wasAttributedTo references missing agent: %v", [agent_id])
}

deny[msg] {
  input.wasAttributedTo["prov:entity"] != input.wasGeneratedBy["prov:entity"]
  msg := "wasAttributedTo entity must match generated artifact entity"
}

deny[msg] {
  artifact_id := input.wasGeneratedBy["prov:entity"]
  artifact := input.entity[artifact_id]
  artifact["prov:type"] != "kfm:EvidenceBundle"
  msg := "generated artifact must be prov:type kfm:EvidenceBundle"
}

deny[msg] {
  artifact_id := input.wasGeneratedBy["prov:entity"]
  artifact := input.entity[artifact_id]
  not artifact["dct:license"]
  msg := "artifact missing license"
}

deny[msg] {
  artifact_id := input.wasGeneratedBy["prov:entity"]
  artifact := input.entity[artifact_id]
  blocked_public_values[artifact["dct:license"]]
  msg := "artifact license cannot be TODO, unknown, restricted, or deny"
}

deny[msg] {
  artifact_id := input.wasGeneratedBy["prov:entity"]
  artifact := input.entity[artifact_id]
  not artifact["kfm:spec_hash"]
  msg := "artifact missing spec_hash"
}

deny[msg] {
  artifact_id := input.wasGeneratedBy["prov:entity"]
  artifact := input.entity[artifact_id]
  artifact["kfm:policy_label"] != "public"
  msg := "published artifact provenance requires kfm:policy_label=public"
}

deny[msg] {
  artifact_id := input.wasGeneratedBy["prov:entity"]
  artifact := input.entity[artifact_id]
  artifact["kfm:sensitivity"] != "public"
  msg := "published artifact provenance requires kfm:sensitivity=public"
}

deny[msg] {
  input["kfm:publication_context"] == "public"
  artifact_id := input.wasGeneratedBy["prov:entity"]
  artifact := input.entity[artifact_id]
  artifact["kfm:policy_label"] != "public"
  msg := "public publication context requires artifact kfm:policy_label=public"
}

deny[msg] {
  input["kfm:publication_context"] == "public"
  artifact_id := input.wasGeneratedBy["prov:entity"]
  artifact := input.entity[artifact_id]
  artifact["kfm:sensitivity"] != "public"
  msg := "public publication context requires artifact kfm:sensitivity=public"
}

deny[msg] {
  activity_id := input.wasGeneratedBy["prov:activity"]
  activity := input.activity[activity_id]
  not activity["prov:used"]
  msg := "pipeline activity missing used inputs"
}

deny[msg] {
  activity_id := input.wasGeneratedBy["prov:activity"]
  activity := input.activity[activity_id]
  count(activity["prov:used"]) == 0
  msg := "pipeline activity used inputs cannot be empty"
}

deny[msg] {
  activity_id := input.wasGeneratedBy["prov:activity"]
  activity := input.activity[activity_id]
  some i
  used_entity_id := activity["prov:used"][i]
  not input.entity[used_entity_id]
  msg := sprintf("activity prov:used references missing entity: %v", [used_entity_id])
}

deny[msg] {
  some i
  relation := input.used[i]
  not input.activity[relation["prov:activity"]]
  msg := sprintf("used[%v] references missing activity", [i])
}

deny[msg] {
  some i
  relation := input.used[i]
  not input.entity[relation["prov:entity"]]
  msg := sprintf("used[%v] references missing entity", [i])
}

deny[msg] {
  some i
  relation := input.wasDerivedFrom[i]
  not input.entity[relation["prov:generatedEntity"]]
  msg := sprintf("wasDerivedFrom[%v] references missing generated entity", [i])
}

deny[msg] {
  some i
  relation := input.wasDerivedFrom[i]
  not input.entity[relation["prov:usedEntity"]]
  msg := sprintf("wasDerivedFrom[%v] references missing used entity", [i])
}

deny[msg] {
  some i
  relation := input.wasDerivedFrom[i]
  relation["prov:activity"]
  not input.activity[relation["prov:activity"]]
  msg := sprintf("wasDerivedFrom[%v] references missing activity", [i])
}

deny[msg] {
  raw_ref(input)
  msg := "public provenance sidecar references RAW / WORK / QUARANTINE material"
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
