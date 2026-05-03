# Layer 11 Remediation + Rollback Controller

## Plan-only
`python soilgrids_remediation_controller.py --current-distribution-manifest ... --current-distribution-receipt ... --monitor-snapshot ... --drift-report ... --alert-envelope ... --output-dir remediation/current --mode plan-only`

## Dry-run
`python soilgrids_remediation_controller.py ... --mode dry-run`

## Rollback with approval token
`python soilgrids_remediation_controller.py ... --mode rollback --execute --allow-remote-network --approval-token APPROVED_CHANGE_123`

Includes examples for IncidentCase.v1, RemediationPlan.v1, RemediationDecisionEnvelope.v1, RollbackReceipt.v1, RecoveryValidationReport.v1, ledger chain hash, and exit codes.

Warning: this layer mutates only approved mutable pointers and never repairs immutable objects.
