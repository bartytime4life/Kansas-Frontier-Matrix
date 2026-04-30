package kfm.flora.usda_plants_promotion_preflight

deny contains "USDA_PLANTS_PREFLIGHT_PUBLICATION_NOT_BLOCKED" if { input.gates.publication != "blocked" }
deny contains "USDA_PLANTS_PREFLIGHT_PROMOTION_NOT_BLOCKED" if { input.gates.promotion != "blocked" }
deny contains "USDA_PLANTS_PREFLIGHT_ELIGIBLE_FOR_PUBLICATION" if { input.eligibility.eligible_for_publication }
deny contains "USDA_PLANTS_PREFLIGHT_MISSING_HUMAN_APPROVAL_REQUIREMENT" if { not input.eligibility.requires_additional_human_approval }
deny contains "USDA_PLANTS_PREFLIGHT_MISSING_HASH" if { not input.preflight_hash }
deny contains "USDA_PLANTS_PREFLIGHT_REVIEW_NOT_PASS" if { input.gates.review_decision != "pass" }
deny contains "USDA_PLANTS_PREFLIGHT_SENSITIVITY_NOT_PASS" if { input.gates.sensitivity_review != "pass" }
deny contains "USDA_PLANTS_PREFLIGHT_RIGHTS_NOT_PASS" if { input.gates.rights_attestation != "pass" }
deny contains "USDA_PLANTS_PREFLIGHT_LEDGER_NOT_PASS" if { input.gates.audit_ledger == "fail" }
deny contains "USDA_PLANTS_PREFLIGHT_PUBLISHED_REF" if { startswith(input.release_candidate_ref,"published/") }
deny contains "USDA_PLANTS_PREFLIGHT_AUTO_ACTION_CLAIM" if { not "auto_merge" in input.blocked_actions }
deny contains "USDA_PLANTS_PREFLIGHT_AUTO_ACTION_CLAIM" if { not "auto_pr" in input.blocked_actions }
