package kfm.air.delivery_deployment

default allow := false
bad_path(x){ re_match("(?i)(data/raw/|data/work/|data/quarantine/|data/processed/air/)", x) }
secret_like(x){ re_match("(?i)(bearer |api[_-]?key|secret|private[_-]?key|token)", x) }
live_instr(x){ re_match("(?i)(kubectl|terraform apply|cloudflare|route53|cdn purge|webhook|https://)", x) }
deny contains "missing_required_artifact" if { some k in ["client_delivery_manifest","client_delivery_contract","client_route_manifest","static_response_bundle","client_cache_manifest","client_compatibility_report"]; not input[k] }
deny contains "compatibility_denied" if { input.client_compatibility_report.result=="deny" }
deny contains "missing_sha256" if { some a in input.artifacts; not a.sha256 }
deny contains "bad_etag" if { some a in input.artifacts; a.etag != sprintf("\"sha256:%s\"",[a.sha256]) }
deny contains "unsafe_path" if { bad_path(lower(json.marshal(input))) }
deny contains "fixture_marked_production" if { contains(lower(json.marshal(input)),"fixture"); contains(lower(json.marshal(input)),"production") }
deny contains "fixture_public_readable_route" if { some r in input.routes; r.visibility=="public_readable"; input.fixture_backed }
deny contains "secret_detected" if { secret_like(lower(json.marshal(input))) }
deny contains "live_instruction" if { live_instr(lower(json.marshal(input))) }
deny contains "nowcast_truth_mislabel" if { contains(lower(json.marshal(input)),"validated aqs truth") }
allow if { count(deny)==0 }
