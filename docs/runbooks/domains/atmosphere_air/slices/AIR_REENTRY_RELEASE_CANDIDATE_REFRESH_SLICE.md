# AIR Re-Entry Release Candidate Refresh Slice

## KFM Meta Block v2
- Status: PROPOSED / NEEDS_VERIFICATION
- Mode: no-network, fixture-backed, fail-closed.
- Domain: atmosphere.air.

This slice consumes candidate re-entry refresh outputs and assembles governed refreshed release-candidate artifacts, revalidates QA locally, builds evidence bundle refresh, candidate catalog/triplets, release-manifest refresh candidate, decision, lineage bridge, manifest, ledger, postcheck, and audit. It does not publish or deploy.

Public boundary constraints: no writes to `data/published/air/` or `data/published/air/read_model/`; no live API, monitoring, notifications, or route removal.

Lifecycle includes: RAW/WORK/QUARANTINE → PROCESSED → ... → REENTRY_CANDIDATE_REENTRY_REFRESH → REENTRY_RELEASE_CANDIDATE_REFRESH.

NowCast is operational evidence only; validated AQS uses `24h_validated`.
