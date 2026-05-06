package kfm.fauna.ebird_test

import data.kfm.fauna.ebird

valid_row := {"object_type":"AggregateOccurrence","policy_label":"public_aggregate","aggregate":"huc12","huc12":"123","taxonKey":"t","occurrenceDate_month":"2025-01","checklist_count":10,"suppression_min_n":10,"kfm:spec_hash":"sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"}

valid_layer := {"policy_label":"public_aggregate","exact_points":"restricted","allowlist_fields":["huc12","taxonKey"],"suppression_min_n":10,"kfm:spec_hash":"sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"}

test_valid_row_passes if { count(ebird.deny with input as valid_row) == 0 }
test_low_checklist_denied if { some m in ebird.deny with input as object.union(valid_row,{"checklist_count":9}); contains(m,"checklist_count") }
test_exact_field_denied if { some m in ebird.deny with input as object.union(valid_row,{"decimalLatitude":1}); contains(m,"exact coordinate") }
test_layer_exact_points_denied if { some m in ebird.deny with input as object.union(valid_layer,{"exact_points":"public"}); contains(m,"exact_points") }
