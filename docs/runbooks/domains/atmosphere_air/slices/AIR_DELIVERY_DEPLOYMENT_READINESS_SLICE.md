# AIR Delivery Deployment Readiness Slice

## KFM Meta Block v2
- Domain: atmosphere.air
- Layer: DeploymentReadiness (fixture/candidate only)
- Mode: evidence-first, fail-closed, no-network, no-deploy

Consumes governed Client Delivery Package artifacts and emits deployment-readiness governance artifacts only: deployment environment, static hosting manifest, deployment plan, readiness report, synthetic probe spec/report, cache invalidation plan, rollback plan, and change/audit records.

Lifecycle: RAW/WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLICATION_CANDIDATE → PUBLISHED → PUBLIC_READ_MODEL → PUBLIC_OPS/AUDIT → STEWARDSHIP/REMEDIATION → READ_MODEL_REBUILD/VERSIONING → CLIENT_DELIVERY → DEPLOYMENT_READINESS.

Public boundary: this slice does not deploy, does not publish live API, and keeps internal artifacts non-dereferenceable by clients.

No-network/no-deploy rules: no live API calls, no CDN purge, no DNS/cloud calls, no GitHub Actions dispatch, no credentials.

Cache semantics: deterministic sha256 and ETag; immutable candidate artifacts; invalidation is plan-only (PROPOSED / NEEDS_VERIFICATION).

Synthetic probes: local file checks only, no live HTTP; verify hashes/ETags/route safety/NowCast-vs-AQS semantics.

Rollback semantics: candidate evidence only; supersede old versions (no deletion); no source mutation.

Gates: A (>35 µg/m³), B (>baseline + 2σ), C (coverage <75%), D (signed attestation/override/steward approval).

AQS distinction: NowCast is operational evidence only; validated AQS uses `24h_validated`; never label NowCast as validated AQS truth.

PROPOSED / NEEDS_VERIFICATION: live API serving, production gateway deployment, CDN purge, DNS routing, cloud deployment, production signatures, live source delivery, production notifications.
