package kfm.air.reentry_release_candidate

default allow = false

unsafe_path(p){contains(lower(p),"data/raw/")} unsafe_path(p){contains(lower(p),"data/work/")} unsafe_path(p){contains(lower(p),"data/quarantine/")} unsafe_path(p){contains(lower(p),"data/processed/air/")} unsafe_path(p){contains(lower(p),"data/published/air/")}

deny[msg]{ not input.candidate_reentry_postcheck_report; msg:="missing candidate re-entry postcheck"}
deny[msg]{ input.candidate_reentry_postcheck_report.result=="deny"; msg:="candidate re-entry postcheck denied"}
deny[msg]{ input.candidate_reentry_audit_report.result=="deny"; msg:="candidate re-entry audit denied"}
deny[msg]{ some r in input.artifact_refs; unsafe_path(r.path); msg:="unsafe artifact path"}
deny[msg]{ contains(lower(json.marshal(input)),"nowcast"); contains(lower(json.marshal(input)),"validated_aqs_truth"); msg:="nowcast treated as validated aqs truth"}
allow { count(deny)==0 }
