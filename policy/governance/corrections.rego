package governance.corrections

default allow := false
forbidden_path(p) if { lp := lower(p); contains(lp,"raw") or contains(lp,"work") or contains(lp,"quarantine") or contains(lp,"candidate") or contains(lp,"private") }
allow if { input.object_type=="CorrectionNotice"; input.reason_code!=""; input.authority.actor!=""; input.affected_artifact.release_id!=""; input.prior_decision_log_ref!=""; input.new_receipt_ref!=""; input.mutates_original_receipt==false }
allow if { input.object_type=="WithdrawalNotice"; input.authority.actor!=""; input.preserve_audit_chain==true }
allow if { input.object_type=="RollbackPlan"; input.target_release_id!=""; not forbidden_path(input.target_public_path) }
deny[msg] if { input.mutates_original_receipt==true; msg := "deny mutation" }
deny[msg] if { input.object_type=="RollbackPlan"; forbidden_path(input.target_public_path); msg := "deny rollback unsafe path" }
deny[msg] if { input.object_type=="PublicCorrectionIndex"; some i; forbidden_path(input.items[i].public_notice_path); msg := "public correction index must be public-safe" }
