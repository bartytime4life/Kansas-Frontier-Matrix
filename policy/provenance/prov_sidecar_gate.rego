package kfm.provenance

default allow := false

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
  artifact_id := input.wasGeneratedBy["prov:entity"]
  artifact := input.entity[artifact_id]
  not artifact["dct:license"]
  msg := "artifact missing license"
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
  artifact["kfm:sensitivity"] == "restricted"
  input.kfm_publication_context == "public"
  msg := "restricted artifact cannot publish to public context"
}

deny[msg] {
  activity_id := input.wasGeneratedBy["prov:activity"]
  activity := input.activity[activity_id]
  not activity["prov:used"]
  msg := "pipeline activity missing used inputs"
}

allow {
  count(deny) == 0
}
