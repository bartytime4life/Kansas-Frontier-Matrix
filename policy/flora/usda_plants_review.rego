package kfm.flora.usda_plants_review

deny contains "USDA_PLANTS_REVIEW_PUBLICATION_CLAIM" if { input.review_decision.publication_state != "not_published" }
deny contains "USDA_PLANTS_REVIEW_PROMOTION_CLAIM" if { input.review_decision.promotion_state != "not_promoted" }
deny contains "USDA_PLANTS_REVIEW_AUTO_MERGE_CLAIM" if { not "auto_merge" in input.review_decision.blocked_actions }
deny contains "USDA_PLANTS_REVIEW_AUTO_PR_CLAIM" if { not "auto_pr" in input.review_decision.blocked_actions }
deny contains "USDA_PLANTS_REVIEW_NON_HUMAN_APPROVAL" if { input.review_decision.decision == "approved_for_preflight"; input.review_decision.reviewer.reviewer_type != "human" }
deny contains "USDA_PLANTS_REVIEW_MISSING_DECISION_HASH" if { not input.review_decision.decision_hash }
deny contains "USDA_PLANTS_REVIEW_MISSING_SENSITIVITY_HASH" if { not input.sensitivity_review.sensitivity_hash }
deny contains "USDA_PLANTS_REVIEW_MISSING_RIGHTS_HASH" if { not input.rights_attestation.attestation_hash }
deny contains "USDA_PLANTS_REVIEW_MISSING_LEDGER_HASH" if { not input.audit_ledger.ledger_hash }
deny contains "USDA_PLANTS_REVIEW_COORDINATE_LEAK" if { input.sensitivity_review.sensitivity.contains_precise_coordinates }
deny contains "USDA_PLANTS_REVIEW_GEOMETRY_LEAK" if { input.sensitivity_review.sensitivity.contains_county_geometry }
deny contains "USDA_PLANTS_REVIEW_BAD_RIGHTS" if { input.rights_attestation.rights.license != "USDA / U.S. Public Domain" }
deny contains "USDA_PLANTS_REVIEW_BAD_RIGHTS" if { input.rights_attestation.rights.rightsHolder != "United States Department of Agriculture" }
deny contains "USDA_PLANTS_REVIEW_BAD_RIGHTS" if { input.rights_attestation.rights.policy_label != "public" }
deny contains "USDA_PLANTS_REVIEW_PUBLISHED_REF" if { some e in input.audit_ledger.entries; startswith(e.ref,"published/") }
