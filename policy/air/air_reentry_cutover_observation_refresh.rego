package kfm.air.reentry_cutover_observation_refresh

deny[msg] { not input.ReentryDeploymentAuthorizationRefreshPostcheckReport; msg := "missing_authorization_refresh_postcheck" }
deny[msg] { input.ReentryDeploymentAuthorizationRefreshPostcheckReport.result == "deny"; msg := "authorization_refresh_postcheck_denied" }
deny[msg] { input.ReentryDeploymentAuthorizationRefreshPostcheckReport.result == "blocked"; msg := "authorization_refresh_postcheck_blocked" }
deny[msg] { not input.ReentryDeploymentAuthorizationRefreshAuditReport; msg := "missing_authorization_refresh_audit" }
deny[msg] { input.ReentryDeploymentAuthorizationRefreshAuditReport.result == "deny"; msg := "authorization_refresh_audit_denied" }
deny[msg] { contains(lower(json.marshal(input)), "data/published/air/"); msg := "published_path_forbidden" }
deny[msg] { contains(lower(json.marshal(input)), "data/published/air/read_model/"); msg := "published_read_model_forbidden" }
deny[msg] { re_match("(?i)(data/raw/|data/work/|data/quarantine/|data/processed/air/)", json.marshal(input)); msg := "unsafe_path_forbidden" }
deny[msg] { re_match("(?i)(secret|token|bearer|private[_-]?key|webhook|slack|pagerduty|calendar)", json.marshal(input)); msg := "secret_or_external_target_forbidden" }
deny[msg] { re_match("(?i)(deploy|publish|kubectl|terraform|dns|cache purge|cdn purge)", json.marshal(input)); msg := "live_operation_forbidden" }
