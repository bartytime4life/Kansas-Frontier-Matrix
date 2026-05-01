package kfm.air.stewardship

default allow = false

deny[msg] { not input.incident_record; msg := "incident record is missing" }
deny[msg] { input.decision.decision == "approve_retraction"; not input.retraction_request; msg := "retraction request missing" }
deny[msg] { not input.publication_manifest; msg := "publication manifest missing" }
deny[msg] { not input.decision.signature; msg := "steward decision lacks signature" }
deny[msg] { input.execution_mode == "production_proposed"; input.decision.signature_type == "fixture_signature"; msg := "fixture signature used for real execution" }
deny[msg] { contains(json.marshal(input),"data/published/air/"); msg := "mutate published air directly" }
deny[msg] { contains(lower(json.marshal(input)),"data/raw") or contains(lower(json.marshal(input)),"data/work") or contains(lower(json.marshal(input)),"data/quarantine"); msg := "unsafe public ref" }
deny[msg] { contains(lower(json.marshal(input)),"data/processed/air/"); msg := "processed exposure" }
deny[msg] { contains(lower(json.marshal(input)),"validated aqs truth"); msg := "nowcast labelled validated aqs truth" }
allow { count(deny)==0 }
