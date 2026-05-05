# AIR Re-Entry Publication Boundary Refresh Slice

## KFM Meta Block v2
- Doctrine: cite-or-abstain, evidence-first, fail-closed.
- Mode: fixture-backed, no-network, candidate-only.
- Status: PROPOSED / NEEDS_VERIFICATION for all production behaviors.

This layer consumes governed re-entry release-candidate refresh outputs, refreshes Gate D attestation and AQS reconciliation checkpoint state, runs publication-boundary refresh review, records publication eligibility refresh decision, prepares candidate manifests, builds lineage bridge + manifest + ledger + postcheck, and does **not** publish/deploy.

No writes to `data/published/air/` or `data/published/air/read_model/`.
NowCast is operational evidence and never validated AQS truth; validated AQS rows require `24h_validated`.
