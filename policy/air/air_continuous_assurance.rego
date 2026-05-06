package kfm.air.continuous_assurance

default deny := []

unsafe_paths := ["data/raw/","data/work/","data/quarantine/","data/processed/air/"]

has_unsafe(x) if { some p in unsafe_paths; contains(lower(json.marshal(x)), p) }

deny contains "unsafe path reference" if has_unsafe(input)
deny contains "production recertification blocked" if input.recertification.decision == "recertify_candidate"
deny contains "fixture signature cannot authorize production" if input.recertification.signature_type == "fixture_signature"; contains(lower(input.recertification.signature), "production")
