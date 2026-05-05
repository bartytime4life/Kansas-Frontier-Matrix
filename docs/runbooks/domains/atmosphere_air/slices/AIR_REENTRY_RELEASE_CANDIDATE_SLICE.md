# AIR Re-Entry Release Candidate Slice

## KFM Meta Block v2
- Status: PROPOSED / NEEDS_VERIFICATION for any live integration.
- Scope: fixture-backed, no-network, local governance artifacts only.

This layer consumes candidate re-entry outputs and assembles governed re-entry release-candidate artifacts: package, QA revalidation, evidence bundle, catalog refresh, release manifest, decision, lineage bridge, ledger, postcheck, and audit.

It does **not** publish, deploy, notify, remove routes, delete artifacts, rotate production baselines, or mutate `data/published/air/`.

Lifecycle chain preserved:
RAW/WORK/QUARANTINE → PROCESSED → ... → CANDIDATE_REENTRY → REENTRY_RELEASE_CANDIDATE.

NowCast is operational evidence only; validated AQS must use `24h_validated`.
