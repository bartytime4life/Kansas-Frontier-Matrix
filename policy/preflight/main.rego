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
  not input.gate == "F"
  msg := sprintf("Gate F invoked with wrong gate input: expected F, got %v", [input.gate])
}

deny contains msg if {
  some path in input.required
  not file_exists(path)
  msg := sprintf("Gate F missing required artifact: %s", [path])
}

deny contains msg if {
  some path in input.required
  err := parse_error(path)
  msg := sprintf("Gate F artifact parse error in %s: %s", [path, err])
}

# Gate F: Deploy preflight.

valid_target_env(env) if { env == "staging" }
valid_target_env(env) if { env == "prod" }

deny contains msg if {
  pf := file_json("artifacts/preflight_report.json")
  pf.status != "pass"
  msg := "preflight_report.status must be pass"
}

deny contains msg if {
  pf := file_json("artifacts/preflight_report.json")
  not valid_target_env(pf.target_env)
  msg := "preflight_report.target_env must be staging or prod"
}

deny contains msg if {
  pf := file_json("artifacts/preflight_report.json")
  not valid_sha256(pf.spec_hash)
  msg := "preflight_report.spec_hash must be a sha256 hex digest"
}

deny contains msg if {
  pf := file_json("artifacts/preflight_report.json")
  spec_hash := file_text_stripped("artifacts/spec_hash.txt")
  pf.spec_hash != spec_hash
  msg := "preflight_report.spec_hash must match artifacts/spec_hash.txt"
}

deny contains msg if {
  pf := file_json("artifacts/preflight_report.json")
  eb := file_json("artifacts/EvidenceBundle.json")
  pf.spec_hash != eb.spec_hash
  msg := "preflight_report.spec_hash must match EvidenceBundle.spec_hash"
}

deny contains msg if {
  pf := file_json("artifacts/preflight_report.json")
  not nonempty_array(pf.checks)
  msg := "preflight_report.checks must be a non-empty array"
}

deny contains msg if {
  pf := file_json("artifacts/preflight_report.json")
  some i
  check := pf.checks[i]
  check.status != "pass"
  msg := sprintf("preflight_report.checks[%v].status must be pass", [i])
}

deny contains msg if {
  pf := file_json("artifacts/preflight_report.json")
  some i
  check := pf.checks[i]
  not nonempty_string(check.name)
  msg := sprintf("preflight_report.checks[%v].name must be a non-empty string", [i])
}
