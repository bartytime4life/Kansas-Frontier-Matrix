# AIR_MAINTENANCE_ROLLFORWARD_SLICE

## KFM Meta Block v2
- Status: Fixture/candidate governance evidence only.
- Domain: `atmosphere.air`.
- Live operations: **PROPOSED / NEEDS_VERIFICATION** only.

This layer consumes maintenance/remediation/deprecation outputs and prepares governed maintenance closure, remediation roll-forward planning, candidate artifact refresh, candidate read-model refresh, client delivery refresh, sunset delta/notice candidates, assurance baseline rotation, append-only roll-forward ledger, and local roll-forward postcheck. It does not deploy, publish, notify, purge caches, alter DNS, or activate production maintenance.

Lifecycle extension: `... -> CONTINUOUS_ASSURANCE -> MAINTENANCE_REMEDIATION -> MAINTENANCE_ROLLFORWARD`.

Guardrails: no RAW/WORK/QUARANTINE refs, no direct PROCESSED exposure, no writes to `data/published/air/`, fixture signatures are non-production, all changes are additive/non-destructive candidate outputs, old versions preserved, NowCast remains operational evidence and never validated AQS truth; validated AQS rows are `24h_validated`.

Gates: A (`NowCast > 35 µg/m³`), B (`NowCast > baseline + 2σ`), C (`coverage <75%`), D (signed approvals/authorization/closure chain).

This PR explicitly does **not** create live deployment, live maintenance, route retirement, production roll-forward, or production baseline rotation.
