package kfm.fauna.ebird_test

import data.kfm.fauna.ebird

valid_input := {
  "schema_version": "v1",
  "object_type": "EvidenceBundle",
  "domain": "fauna",
  "source": "ebird",
  "source_uri": "https://example.org/ebird.csv",
  "query_predicate": "complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10",
  "kfm:spec_hash": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
  "aggregate": "huc12",
  "suppression_min_n": 10,
  "policy_label": "public",
  "exact_points": "restricted",
  "public_fields": ["huc12", "count"]
}

test_valid_passes if {
  count(ebird.deny with input as valid_input) == 0
}

test_missing_source_uri_denied if {
  some msg in ebird.deny with input as object.remove(valid_input, "source_uri")
  contains(msg, "source_uri")
}

test_missing_query_predicate_denied if {
  some msg in ebird.deny with input as object.remove(valid_input, "query_predicate")
  contains(msg, "query_predicate")
}

test_missing_spec_hash_denied if {
  some msg in ebird.deny with input as object.remove(valid_input, "kfm:spec_hash")
  contains(msg, "spec_hash")
}

test_malformed_spec_hash_denied if {
  some msg in ebird.deny with input as object.union(valid_input, {"kfm:spec_hash": "sha256:xyz"})
  contains(msg, "malformed")
}

test_suppression_below_10_denied if {
  some msg in ebird.deny with input as object.union(valid_input, {"suppression_min_n": 9})
  contains(msg, "suppression_min_n")
}

test_public_exact_fields_denied if {
  some msg in ebird.deny with input as object.union(valid_input, {"public_fields": ["decimalLatitude", "huc12"]})
  contains(msg, "exact field")
}

test_public_exact_points_not_restricted_denied if {
  some msg in ebird.deny with input as object.union(valid_input, {"exact_points": "public"})
  contains(msg, "exact_points")
}

test_query_predicate_constraints_denied if {
  bad := object.union(valid_input, {"query_predicate": "complete==TRUE"})
  count(ebird.deny with input as bad) >= 1
}
