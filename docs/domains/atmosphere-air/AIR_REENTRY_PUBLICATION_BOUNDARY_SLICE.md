# AIR Re-Entry Publication Boundary Slice

## KFM Meta Block v2
- **Domain:** atmosphere.air
- **Layer:** Re-Entry Publication Boundary
- **Mode:** fixture/candidate only
- **Network:** disabled by policy and implementation intent
- **Status:** PROPOSED / NEEDS_VERIFICATION for any production operation

This layer consumes re-entry release-candidate outputs, refreshes Gate D attestation, records/refreshes AQS reconciliation, performs publication-boundary review, decides publication eligibility, builds publication-candidate artifacts, creates publication-manifest candidate preview, bridges lineage, writes append-only ledger artifacts, and runs postchecks.

It does **not** publish, deploy, notify, remove routes, delete artifacts, or write to `data/published/air/`.

NowCast is operational evidence and not validated AQS truth. Validated AQS uses `24h_validated`.

Gate D fixture signatures are non-production and cannot authorize production publication.
