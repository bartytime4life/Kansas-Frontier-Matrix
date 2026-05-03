# AIR Read Model Rebuild Slice

## KFM Meta Block v2
- Domain: atmosphere.air
- Layer: READ_MODEL_REBUILD/VERSIONING
- Posture: fixture-backed, candidate-only, fail-closed.

This layer consumes steward-approved tombstones + invalidation notices, generates a rebuild plan, writes a new immutable read-model version into explicit output directories, emits public-safe delta feeds/client notices, and audits that retracted records are no longer active.

Lifecycle: RAW/WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLICATION_CANDIDATE → PUBLISHED → PUBLIC_READ_MODEL → PUBLIC_OPS/AUDIT → STEWARDSHIP/REMEDIATION → READ_MODEL_REBUILD/VERSIONING.

Public boundary: clients read only PublicIndex/PublicApiRecord/PublicStatus/PublicProvenanceTrace/PublicDeltaFeed/ClientInvalidationNotice; old versions are superseded not deleted; tombstones/invalidation notices are additive; source manifests/read-model are not mutated in place.

Gates: A NowCast >35 µg/m³, B NowCast > baseline +2σ, C station coverage <75%, D signed attestation/override/steward approval.

Workflow: incident → retraction request → steward decision → remediation package → tombstone/invalidation → rebuild plan → new version → delta feed → auditor pass/deny.

AQS distinction: NowCast is operational evidence; validated AQS rows use `24h_validated`; NowCast must never be labelled validated AQS truth.

PROPOSED / NEEDS_VERIFICATION: production index rotation, CDN/cache purge, live client notification, production signatures, real public tombstone application, live AirNow/AQS/Mesonet ops, production publication.

This PR does not perform live public mutation or live public air-quality publication.
