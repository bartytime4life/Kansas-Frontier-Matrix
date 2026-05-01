package kfm.fauna.gbif

deny[msg] if { not input.evidence_bundle_id; msg := "missing EvidenceBundle" }
deny[msg] if { not input["kfm:spec_hash"]; msg := "missing kfm:spec_hash" }
deny[msg] if { not input.source_uri; msg := "source_uri missing" }
deny[msg] if { not input.download_key; msg := "download_key missing" }
deny[msg] if { not input.query_predicate; msg := "query_predicate missing" }

deny[msg] if {
  input.outputs.publication_target == "public"
  some r in input.outputs.normalized_records
  r.sensitive == true
  msg := "public exact sensitive coordinates denied"
}

deny[msg] if {
  input.outputs.publication_target == "public"
  some l in input.license_summary
  not l in {"CC0","CC-BY"}
  msg := "unknown or disallowed public license"
}

deny[msg] if {
  input.outputs.publication_target == "public"
  input.records_count < 10
  msg := "public aggregate with n < 10 denied"
}
