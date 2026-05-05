package main

import rego.v1

file(path) := f if {
  f := input.files[path]
}

file_exists(path) if {
  f := file(path)
  f.exists == true
}

directory_nonempty(path) if {
  f := file(path)
  f.exists == true
  f.kind == "directory"
  f.child_count > 0
}

has_parse_error(path) if {
  f := file(path)
  f.exists == true
  f.kind == "file"
  nonempty_string(f.parse_error)
}

parse_error(path) := msg if {
  f := file(path)
  msg := f.parse_error
  nonempty_string(msg)
}

file_json(path) := doc if {
  f := file(path)
  f.exists == true
  f.kind == "file"
  not has_parse_error(path)
  doc := f.json
}

file_text_stripped(path) := txt if {
  f := file(path)
  f.exists == true
  f.kind == "file"
  txt := f.text_stripped
}

nonempty_string(x) if {
  is_string(x)
  count(x) > 0
}

nonempty_array(xs) if {
  is_array(xs)
  count(xs) > 0
}

nonempty_object(obj) if {
  is_object(obj)
  count(obj) > 0
}

valid_sha256(x) if {
  is_string(x)
  regex.match("^[a-fA-F0-9]{64}$", x)
}

has_key(obj, key) if {
  _ := obj[key]
}

deny contains msg if {
  not input.gate == "E"
  msg := sprintf("Gate E invoked with wrong gate input: expected E, got %v", [input.gate])
}

deny contains msg if {
  some path in input.required
  not file_exists(path)
  msg := sprintf("Gate E missing required artifact: %s", [path])
}

deny contains msg if {
  some path in input.required
  err := parse_error(path)
  msg := sprintf("Gate E artifact parse error in %s: %s", [path, err])
}

# Gate E: Stewardship and promotion approvals.

deny contains msg if {
  dl := file_json("artifacts/decision_log.json")
  not nonempty_string(dl.decision_id)
  msg := "decision_log.decision_id must be a non-empty string"
}

deny contains msg if {
  dl := file_json("artifacts/decision_log.json")
  not nonempty_string(dl.promotion_target)
  msg := "decision_log.promotion_target must be a non-empty string"
}

deny contains msg if {
  dl := file_json("artifacts/decision_log.json")
  dl.owners_approved != true
  msg := "decision_log.owners_approved must be true"
}

deny contains msg if {
  dl := file_json("artifacts/decision_log.json")
  dl.codeowners_reviewed != true
  msg := "decision_log.codeowners_reviewed must be true"
}

deny contains msg if {
  dl := file_json("artifacts/decision_log.json")
  not nonempty_array(dl.approvals)
  msg := "decision_log.approvals must be a non-empty array"
}

deny contains msg if {
  dl := file_json("artifacts/decision_log.json")
  some i
  approval := dl.approvals[i]
  approval.decision != "approved"
  msg := sprintf("decision_log.approvals[%v].decision must be approved", [i])
}

deny contains msg if {
  dl := file_json("artifacts/decision_log.json")
  some i
  approval := dl.approvals[i]
  not nonempty_string(approval.approver)
  msg := sprintf("decision_log.approvals[%v].approver must be a non-empty string", [i])
}

deny contains msg if {
  dl := file_json("artifacts/decision_log.json")
  some i
  approval := dl.approvals[i]
  not nonempty_string(approval.role)
  msg := sprintf("decision_log.approvals[%v].role must be a non-empty string", [i])
}

deny contains msg if {
  dl := file_json("artifacts/decision_log.json")
  some i
  approval := dl.approvals[i]
  not nonempty_string(approval.timestamp)
  msg := sprintf("decision_log.approvals[%v].timestamp must be a non-empty string", [i])
}

deny contains msg if {
  dl := file_json("artifacts/decision_log.json")
  nonempty_array(dl.outstanding_blockers)
  msg := "decision_log.outstanding_blockers must be empty or omitted"
}
