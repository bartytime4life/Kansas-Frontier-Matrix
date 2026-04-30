package kfm.flora.usda_plants_external_deployment

deny contains reason if { not input.approval.approver; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_APPROVAL_MISSING" }
deny contains reason if { input.approval.approver_type != "human"; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_NON_HUMAN_APPROVAL" }
deny contains reason if { input.request.host_allowed != true; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_HOST_NOT_ALLOWED" }
deny contains reason if { input.plan.protected_environment != true; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_UNPROTECTED_ENV" }
deny contains reason if { some r in input.refs; contains(r,"/raw/"); reason := "USDA_PLANTS_EXTERNAL_DEPLOY_RAW_REF_LEAK" }
deny contains reason if { some r in input.refs; contains(r,"/work/"); reason := "USDA_PLANTS_EXTERNAL_DEPLOY_WORK_REF_LEAK" }
deny contains reason if { some r in input.refs; contains(r,"/quarantine/"); reason := "USDA_PLANTS_EXTERNAL_DEPLOY_QUARANTINE_REF_LEAK" }
deny contains reason if { input.claims.occurrence_coordinates == true; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_OCCURRENCE_COORDINATE_LEAK" }
deny contains reason if { input.claims.secret_values == true; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_SECRET_VALUE_LEAK" }
deny contains reason if { input.claims.unscoped_secret == true; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_UNSCOPED_SECRET" }
deny contains reason if { input.claims.long_lived_secret_unapproved == true; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_LONG_LIVED_SECRET_UNAPPROVED" }
deny contains reason if { input.claims.auto_merge == true; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_AUTO_MERGE_CLAIM" }
deny contains reason if { not input.hashes.registry_hash; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_MISSING_REGISTRY_HASH" }
deny contains reason if { not input.hashes.plan_hash; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_MISSING_PLAN_HASH" }
deny contains reason if { not input.hashes.provider_manifest_hash; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_MISSING_PROVIDER_MANIFEST_HASH" }
deny contains reason if { not input.hashes.receipt_hash; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_MISSING_RECEIPT_HASH" }
deny contains reason if { not input.hashes.verification_hash; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_MISSING_VERIFICATION_HASH" }
deny contains reason if { not input.hashes.ledger_hash; reason := "USDA_PLANTS_EXTERNAL_DEPLOY_MISSING_LEDGER_HASH" }
deny contains reason if { not contains(lower(input.attribution),"usda plants"); reason := "USDA_PLANTS_EXTERNAL_DEPLOY_BAD_ATTRIBUTION" }
