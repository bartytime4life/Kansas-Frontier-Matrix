package kfm.flora.usda_plants_review_test
import data.kfm.flora.usda_plants_review

test_valid_no_denies if { count(usda_plants_review.deny with input as {"review_decision":{"publication_state":"not_published","promotion_state":"not_promoted","blocked_actions":["publish","promote","auto_merge","auto_pr"],"decision":"approved_for_preflight","reviewer":{"reviewer_type":"human"},"decision_hash":"x"},"sensitivity_review":{"sensitivity_hash":"x","sensitivity":{"contains_precise_coordinates":false,"contains_county_geometry":false}},"rights_attestation":{"attestation_hash":"x","rights":{"license":"USDA / U.S. Public Domain","rightsHolder":"United States Department of Agriculture","policy_label":"public"}},"audit_ledger":{"ledger_hash":"x","entries":[{"ref":"review/x.json"}]}})==0 }

test_publication_denied if { "USDA_PLANTS_REVIEW_PUBLICATION_CLAIM" in usda_plants_review.deny with input as {"review_decision":{"publication_state":"published","promotion_state":"not_promoted","blocked_actions":[],"decision":"abstain","reviewer":{"reviewer_type":"human"}}} }
