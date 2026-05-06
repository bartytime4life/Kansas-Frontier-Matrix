package kfm.release

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
  input.policy_label != "public"
  msg := "ReleaseManifest requires policy_label=public"
}

deny[msg] {
  input.review_state != "reviewed"
  input.review_state != "published"
  msg := "ReleaseManifest requires review_state reviewed or published"
}

deny[msg] {
  not input.artifacts
  msg := "ReleaseManifest missing artifacts"
}

deny[msg] {
  count(input.artifacts) == 0
  msg := "ReleaseManifest artifacts cannot be empty"
}

deny[msg] {
  some i
  artifact := input.artifacts[i]
  not artifact.artifact_ref
  msg := sprintf("artifacts[%v] missing artifact_ref", [i])
}

deny[msg] {
  some i
  artifact := input.artifacts[i]
  not artifact.spec_hash
  msg := sprintf("artifacts[%v] missing spec_hash", [i])
}

deny[msg] {
  some i
  artifact := input.artifacts[i]
  not artifact.evidence_ref
  msg := sprintf("artifacts[%v] missing evidence_ref", [i])
}

deny[msg] {
  some i
  artifact := input.artifacts[i]
  not artifact.provenance_ref
  msg := sprintf("artifacts[%v] missing provenance_ref", [i])
}

deny[msg] {
  some i
  artifact := input.artifacts[i]
  not artifact.stac_ref
  msg := sprintf("artifacts[%v] missing stac_ref", [i])
}

deny[msg] {
  some i
  artifact := input.artifacts[i]
  not artifact.dcat_ref
  msg := sprintf("artifacts[%v] missing dcat_ref", [i])
}

deny[msg] {
  some i
  artifact := input.artifacts[i]
  artifact.policy_label != "public"
  msg := sprintf("artifacts[%v] requires policy_label=public", [i])
}

deny[msg] {
  some i
  artifact := input.artifacts[i]
  artifact.review_state != "reviewed"
  artifact.review_state != "published"
  msg := sprintf("artifacts[%v] requires review_state reviewed or published", [i])
}

deny[msg] {
  some i
  artifact := input.artifacts[i]
  artifact.sensitivity
  artifact.sensitivity != "public"
  msg := sprintf("artifacts[%v] requires sensitivity=public when provided", [i])
}

deny[msg] {
  input.spec_hash
  some i
  artifact := input.artifacts[i]
  artifact.spec_hash != input.spec_hash
  msg := sprintf("artifacts[%v] spec_hash does not match manifest spec_hash", [i])
}

deny[msg] {
  some i
  artifact := input.artifacts[i]
  is_blocked_public_value(artifact.artifact_ref)
  msg := sprintf("artifacts[%v] artifact_ref cannot be TODO, unknown, restricted, deny, or empty", [i])
}

deny[msg] {
  raw_ref(input)
  msg := "public ReleaseManifest references RAW / WORK / QUARANTINE material"
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
