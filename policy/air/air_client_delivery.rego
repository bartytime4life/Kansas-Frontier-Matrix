package kfm.air.client_delivery

default allow := false
bad_path(x){ re_match("(?i)(data/raw/|data/work/|data/quarantine/|data/processed/air/)", x) }
deny contains "missing_public_index" if { not input.public_index }
deny contains "missing_public_status" if { not input.public_status }
deny contains "missing_read_model_version_index" if { not input.read_model_version_index }
deny contains "missing_sha256" if { some a in input.artifacts; not a.sha256 }
deny contains "bad_etag" if { some a in input.artifacts; a.etag != sprintf("\"sha256:%s\"",[a.sha256]) }
deny contains "unsafe_route_path" if { some r in input.routes; bad_path(json.marshal(r)) }
deny contains "fixture_published_delivery" if { input.delivery_status=="published_delivery"; input.fixture_backed }
deny contains "nowcast_truth_mislabel" if { contains(lower(json.marshal(input)),"validated aqs truth") }
allow if { count(deny)==0 }
