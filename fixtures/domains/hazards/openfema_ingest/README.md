<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixtures/hazards/openfema-ingest
title: Synthetic OpenFEMA Ingest Walks
type: fixture-guide
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Hazards steward · FEMA source steward · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public-metadata; private-administrative-context; not-for-life-safety; no-eligibility-authority
owning_root: fixtures/
responsibility: describe sealed administrative-context capture fixtures
truth_posture: CONFIRMED bounded supplied-page replay; PROPOSED candidate profile; NEEDS VERIFICATION human review, source admission and any downstream use
[/KFM_META_BLOCK_V2] -->

# Synthetic OpenFEMA ingest walks

Three packets seal exact original capture-envelope text, its SHA-256 and the
complete expected held candidate. Data, titles, IDs, provider hashes, designated
areas and program flags are invented. These are not FEMA actions or eligibility
information. Source times are fixed separately from KFM page capture times.

- `complete.json`: two supplied pages, three records. One unknown incident end
  stays null; one record retains additive schema drift and an impossible closeout
  time, producing explicit flags and quarantine without losing its source snapshot.
- `count-drift.json`: the same records, with a changed remaining count on page two.
  The walk remains incomplete and held; it is not silently reconciled as complete.
- `empty.json`: one short first page with count zero; coverage remains unestablished.

Use the [runbook](../../../../docs/runbooks/openfema-fixture-ingest.md). Golden
changes require deliberate review. Capture conformance grants no source admission,
provider completeness, hazard-absence, observed-event or public-use authority.
