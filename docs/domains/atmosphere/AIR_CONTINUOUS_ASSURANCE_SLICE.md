# AIR Continuous Assurance Slice

## KFM Meta Block v2
- Doctrine: cite-or-abstain, evidence-first, fail-closed.
- Scope: fixture-backed, no-network continuous assurance after operational handoff/release closure.

This slice consumes operational handoff and release closure evidence, creates a continuous assurance plan, performs archive integrity rechecks, reviews runbook candidates, observes fixture drift, prepares periodic recertification, maintenance window planning, deprecation candidates, and builds a continuous assurance summary.

Lifecycle: RAW/WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLICATION_CANDIDATE → PUBLISHED → PUBLIC_READ_MODEL → PUBLIC_OPS/AUDIT → STEWARDSHIP/REMEDIATION → READ_MODEL_REBUILD/VERSIONING → CLIENT_DELIVERY → DEPLOYMENT_READINESS → DEPLOYMENT_AUTHORIZATION → CUTOVER_OBSERVATION/RELEASE_LEDGER → OPERATIONAL_HANDOFF/RELEASE_CLOSURE → CONTINUOUS_ASSURANCE.

No live deployment, no live monitoring, no notices, no external archive/storage, no API calls.
NowCast is operational evidence only; validated AQS rows use `24h_validated`.

## Gates
- Gate A: NowCast > 35 µg/m³
- Gate B: NowCast > baseline + 2σ
- Gate C: station coverage < 75%
- Gate D: signed attestation / override / steward approval / release-manager authorization / operational acceptance / closure approval / recertification approval

## PROPOSED / NEEDS_VERIFICATION
Live serving, production gateway deploy, CDN/cache purge, DNS routing, cloud deployment, production signatures, ticketing integrations, IdP verification, live AirNow/AQS/Mesonet delivery, post-deploy monitoring, notifications, external archive, production handoff/closure/recertification/maintenance/deprecation.
