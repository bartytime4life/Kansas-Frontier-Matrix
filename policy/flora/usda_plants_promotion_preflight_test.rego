package kfm.flora.usda_plants_promotion_preflight_test
import data.kfm.flora.usda_plants_promotion_preflight

test_valid_no_denies if { count(usda_plants_promotion_preflight.deny with input as {"gates":{"publication":"blocked","promotion":"blocked","review_decision":"pass","sensitivity_review":"pass","rights_attestation":"pass"},"eligibility":{"eligible_for_publication":false,"requires_additional_human_approval":true},"preflight_hash":"x","release_candidate_ref":"releases/x.json","blocked_actions":["publish","promote","auto_merge","auto_pr"]})==0 }

test_publication_gate_denied if { "USDA_PLANTS_PREFLIGHT_PUBLICATION_NOT_BLOCKED" in usda_plants_promotion_preflight.deny with input as {"gates":{"publication":"open","promotion":"blocked","review_decision":"pass","sensitivity_review":"pass","rights_attestation":"pass"},"eligibility":{"eligible_for_publication":false,"requires_additional_human_approval":true},"preflight_hash":"x","release_candidate_ref":"releases/x.json","blocked_actions":["publish","promote","auto_merge","auto_pr"]} }
