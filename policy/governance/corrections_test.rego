package governance.corrections

test_allow_correction if { allow with input as {"object_type":"CorrectionNotice","reason_code":"DATA_FIX","authority":{"actor":"x"},"affected_artifact":{"release_id":"r"},"prior_decision_log_ref":"d","new_receipt_ref":"n","mutates_original_receipt":false} }
test_deny_unsafe_rollback if { deny[_] with input as {"object_type":"RollbackPlan","target_release_id":"r","target_public_path":"data/work/candidate/x.json"} }
