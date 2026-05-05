# AIR Re-Entry Publication Materialization Slice

## KFM Meta Block v2
- Domain: atmosphere.air
- Slice: REENTRY_PUBLICATION_MATERIALIZATION
- Posture: fixture/candidate only, fail-closed
- Live ops/publication/deployment/read-model rebuild: **not performed in this slice**

This slice consumes governed re-entry publication-boundary artifacts and prepares dry-run materialization outputs only: plan, immutable preview manifest/artifacts, manifest finalization candidate, receipt candidate, read-model refresh request, delta seed, append-only ledger, and postcheck/audit artifacts. It writes only to explicit output directories and does not mutate published truth.
