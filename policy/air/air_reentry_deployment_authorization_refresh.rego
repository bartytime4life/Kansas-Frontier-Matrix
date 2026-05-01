package kfm.air.reentry_deployment_authorization_refresh

default allow = false

deny[msg] { not input.ReentryDeploymentReadinessRefreshPostcheckReport; msg := "missing readiness postcheck" }
deny[msg] { input.ReentryDeploymentReadinessRefreshPostcheckReport.result == "deny"; msg := "readiness denied" }
deny[msg] { input.ReentryDeploymentRefreshExecutionReceipt.execution_mode == "production"; msg := "production execution blocked" }
deny[msg] { some p in input.artifact_refs; contains(lower(p),"data/published/air/"); msg := "published path forbidden" }
allow { count(deny)==0 }
