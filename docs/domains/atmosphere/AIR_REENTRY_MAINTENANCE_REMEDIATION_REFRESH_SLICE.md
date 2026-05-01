# AIR Re-Entry Maintenance/Remediation Refresh Slice

## KFM Meta Block v2
- Domain: atmosphere.air
- Slice: REENTRY_MAINTENANCE_REMEDIATION_REFRESH
- Status: proposed
- Mode: fixture-backed, candidate-only, no-network
- Truth boundary: non-public, non-production

This layer consumes re-entry continuous-assurance refresh outputs plus governed handoff/cutover/client-delivery refresh artifacts, then prepares candidate-only maintenance/remediation/deprecation planning evidence.

## Scope
- Collect assurance refresh findings (additive evidence only).
- Prepare maintenance refresh authorization (fixture signatures are non-production only).
- Build governance-only maintenance execution plan (descriptive, non-executable).
- Run local fixture simulation and produce fixture receipt.
- Record additive remediation evidence.
- Review deprecation refresh candidates (review/planning only).
- Build client sunset refresh plans (no route removal, no notices).
- Build maintenance refresh manifest, decision, ledger, postcheck, and audit.

## Lifecycle chain
RAW/WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLICATION_CANDIDATE → PUBLISHED → PUBLIC_READ_MODEL → PUBLIC_OPS/AUDIT → STEWARDSHIP/REMEDIATION → READ_MODEL_REBUILD/VERSIONING → CLIENT_DELIVERY → DEPLOYMENT_READINESS → DEPLOYMENT_AUTHORIZATION → CUTOVER_OBSERVATION/RELEASE_LEDGER → OPERATIONAL_HANDOFF/RELEASE_CLOSURE → CONTINUOUS_ASSURANCE → MAINTENANCE_REMEDIATION → MAINTENANCE_ROLLFORWARD → CANDIDATE_REENTRY → REENTRY_RELEASE_CANDIDATE → REENTRY_PUBLICATION_BOUNDARY → REENTRY_PUBLICATION_MATERIALIZATION → REENTRY_PUBLIC_READ_MODEL_REFRESH → REENTRY_CLIENT_DELIVERY_REFRESH → REENTRY_DEPLOYMENT_READINESS_REFRESH → REENTRY_DEPLOYMENT_AUTHORIZATION_REFRESH → REENTRY_CUTOVER_OBSERVATION_REFRESH → REENTRY_OPERATIONAL_HANDOFF_REFRESH → REENTRY_CONTINUOUS_ASSURANCE_REFRESH → REENTRY_MAINTENANCE_REMEDIATION_REFRESH.

## Public boundary assertions
- This PR does not publish, deploy, or activate live maintenance.
- This PR does not write to `data/published/air/` or `data/published/air/read_model/`.
- This PR does not remove routes, delete artifacts, send notices, run rollback, or call external services.
- Clients continue to read only previously governed client-safe delivery artifacts.

## No-network / no-live-ops rules
No live AirNow/AQS/Mesonet/NOAA, no external API calls, no CDN purge, DNS, cloud, ticketing, GitHub Actions dispatch, monitoring/alerting, external archive/storage, stakeholder messaging, or calendar scheduling.

## Semantics
- Assurance findings: additive evidence, deterministic severity, fail-closed on hard violations.
- Authorization: fixture signatures are explicitly non-production; production maintenance blocked.
- Remediation records: candidate evidence only; no silent mutation.
- Deprecation/sunset: review/planning only; no artifact deletion, no route removal, no notices.
- Gate D and AQS carry-forward remain upstream-governed; NowCast is operational evidence only, never validated AQS truth.

## Gates
- Gate A: NowCast > 35 µg/m³
- Gate B: NowCast > baseline + 2σ
- Gate C: station coverage < 75%
- Gate D: signed attestation/override/steward + release-manager + authorization chain through refresh lifecycle.

## AQS distinction
- NowCast is operational evidence.
- Validated AQS rows use `24h_validated`.
- NowCast must never be labeled validated AQS truth.

## PROPOSED / NEEDS_VERIFICATION
All live ingestion, live reconciliation, production signatures, publication, deployment, gateway/CDN/DNS operations, notification, and production maintenance/remediation/roll-forward/re-entry actions remain PROPOSED / NEEDS_VERIFICATION.
