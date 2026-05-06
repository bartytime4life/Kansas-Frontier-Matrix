package kfm.air.deployment_authorization

default deny := []

deny contains "production blocked" if { input.deployment_authorization.authorized_environment == "production" }
deny contains "fixture signature cannot authorize production" if { input.deployment_authorization.signature_type == "fixture_signature"; input.deployment_authorization.authorized_environment == "production_proposed" }
deny contains "missing release manager decision" if { not input.release_manager_decision }
