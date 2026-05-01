package kfm.air.cutover_observation

deny[msg] { not input.deployment_authorization_ref; msg := "missing deployment authorization" }
deny[msg] { input.accepted_environment == "production"; msg := "production acceptance blocked" }
deny[msg] { input.signature_type == "fixture_signature"; input.accepted_environment == "production_proposed"; msg := "fixture signature cannot authorize production" }
