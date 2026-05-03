# AIR Stewardship/Remediation Slice

## KFM Meta Block v2
- Status: PROPOSED / fixture-only
- Scope: Steward review, remediation packaging, fixture tombstone + invalidation artifacts.
- Boundary: No live public mutation, no network, no alerting.

This layer consumes ops incidents and retraction requests, builds steward queue, records steward decisions, packages remediation evidence, applies **fixture-only** tombstones as additive immutable outputs, and emits read-model invalidation notices.

Lifecycle: RAW/WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLICATION_CANDIDATE → PUBLISHED → PUBLIC_READ_MODEL → PUBLIC_OPS/AUDIT → STEWARDSHIP/REMEDIATION.

Public boundary remains PublicIndex/PublicApiRecord/PublicStatus/PublicProvenanceTrace only. Remediation outputs are governance evidence; no in-place publication manifest mutation.

Gates: A >35 µg/m³, B > baseline+2σ, C station coverage <75%, D signed attestation/override/steward approval.

NowCast is operational evidence only; validated AQS rows use `24h_validated`; NowCast must never be labeled validated AQS truth.

Production signatures/live steward identity/live tombstone mutation/live alerting/live source remediation/live read-model invalidation are **PROPOSED / NEEDS_VERIFICATION**.
