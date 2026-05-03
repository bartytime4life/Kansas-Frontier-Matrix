# AIR Maintenance Remediation Slice

## KFM Meta Block v2
- Status: Candidate fixture governance slice.
- Scope: Continuous Assurance -> Maintenance/Remediation planning evidence.
- Mode: No-network, no-live-ops, fail-closed.

This layer consumes governed continuous assurance outputs and prepares assurance findings, maintenance authorization, governance-only execution planning, fixture simulation receipts, additive remediation evidence, deprecation review, sunset planning, append-only maintenance ledger, postchecks, and maintenance audit artifacts. It does not deploy, mutate public truth, remove routes, delete artifacts, or send notices.

NowCast is operational evidence only; validated AQS truth must use `24h_validated` rows.

All live operations (API serving, DNS/CDN/cache changes, cloud deploy, signatures for production, ticketing, identity verification, alerting, notifications, calendar operations, production maintenance/deprecation) are **PROPOSED / NEEDS_VERIFICATION**.
