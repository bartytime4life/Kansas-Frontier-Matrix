package kfm.hydrology.huc12_comid_release

load(path) = x if { x := json.unmarshal(io.read_file(path)) }

test_allow_published { allow with input as load("tests/fixtures/hydrology/huc12_comid_release/policy/input_allow_published.json") }
test_deny_raw_uri { deny[_] with input as load("tests/fixtures/hydrology/huc12_comid_release/policy/input_deny_raw_uri.json") }
test_deny_work_uri { deny[_] with input as load("tests/fixtures/hydrology/huc12_comid_release/policy/input_deny_work_uri.json") }
test_deny_quarantine_uri { deny[_] with input as load("tests/fixtures/hydrology/huc12_comid_release/policy/input_deny_quarantine_uri.json") }
test_deny_missing_evidence { deny[_] with input as load("tests/fixtures/hydrology/huc12_comid_release/policy/input_deny_missing_evidence.json") }
test_deny_digest_mismatch { deny[_] with input as load("tests/fixtures/hydrology/huc12_comid_release/policy/input_deny_digest_mismatch.json") }
test_deny_pending_review { deny[_] with input as load("tests/fixtures/hydrology/huc12_comid_release/policy/input_deny_pending_steward_review.json") }
test_deny_overlap { deny[_] with input as load("tests/fixtures/hydrology/huc12_comid_release/policy/input_deny_overlapping_conflict.json") }
test_deny_unpublished { deny[_] with input as load("tests/fixtures/hydrology/huc12_comid_release/policy/input_deny_unpublished_for_public.json") }
