# AIR_CLIENT_DELIVERY_SLICE

## KFM Meta Block v2
- Status: fixture/candidate only
- Scope: governed client delivery from Public Read Model/Rebuild artifacts
- Network: none (offline fixtures only)

This slice consumes versioned `PublicIndex/PublicApiRecord/PublicStatus/PublicProvenanceTrace/PublicDeltaFeed` plus `ReadModelVersionIndex/ReadModelRebuildManifest` and emits client-safe artifacts: contract, routes, static responses, cache/ETag metadata, delta cursor, compatibility report, delivery manifest, and audit report.

Lifecycle: `RAW/WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLICATION_CANDIDATE -> PUBLISHED -> PUBLIC_READ_MODEL -> PUBLIC_OPS/AUDIT -> STEWARDSHIP/REMEDIATION -> READ_MODEL_REBUILD/VERSIONING -> CLIENT_DELIVERY`.

Public boundary: clients read only delivery artifacts; never dereference QA Summary, EvidenceBundle, PromotionDecision, ReleaseManifest, PublicationManifest, RAW, WORK, QUARANTINE, or PROCESSED.

Cache semantics: deterministic `sha256`, deterministic ETag derived from hash, immutable candidate artifacts, no CDN/cache purge.

Delta semantics: public-safe cursor only; retractions/invalidation are additive; no internal path encoding.

Gates: A `NowCast > 35 ug/m3`; B `NowCast > baseline + 2σ`; C `station coverage < 75%`; D signed attestation / override / steward approval.

AQS distinction: NowCast is operational evidence only; validated AQS rows use `24h_validated`; NowCast is never validated AQS truth.

PROPOSED / NEEDS_VERIFICATION: live API serving, production gateway/CDN/DNS/cache purge, production signatures, live source delivery, production client notifications.

This PR does **not** create a live public API or live public air-quality publication.
