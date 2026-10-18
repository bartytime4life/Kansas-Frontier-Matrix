# GitHub and private Site reconciliation — 2026-10-13

The owner requested alignment with all recent GitHub changes and performance
enhancements. This reconciliation starts from owner-private Site v261,
`4a27cd72398ed321070a8bb7dcdd07a6a294f21e`, and GitHub main
`3d66e83e2dbe034c0ac51e07d98372b50b70fe39`. Both were checked live before
authoring. Separate clean checkouts preserve the original local repository,
previous Site source, local Explorer alias and stores. Synced `sources/` are
read-only and unchanged.

## Combined behavior

The Site retains its 17 subjects, shared layer/investigation/feature/function
filters and 13-reference almanac library. GitHub's existing source overlays are
carried forward, including Qwen question safeguards and knowledge/evaluation
tooling, owner-provisioned local-companion sessions, governed soil/storm-event/
earthquake routes and controls, water release expiry handling, and subsurface
static-delivery containment. No model evaluation against a real model is run
as part of this reconciliation.

The initial inventory identified 109 GitHub-only or GitHub-changed paths, two
overlapping files and 18 Site-only/changed paths. Two canonical cache operator/
test mappings are reconciled separately. Three-way merging preserves both the
new topic experience and GitHub's safeguards in `app/page.tsx`; its layer
regression also retains the three new governed controls. Reviewed soil joins
Agriculture/Water/Land/Science, storm reports join Weather/Hazards/History/Science,
and earthquakes join Geology/Hazards/Science. Filtering retains selected owners,
source status and eligibility; it does not activate a source.

Repository-dependent tests accept the existing absolute
`KFM_WEATHER_REPOSITORY_ROOT` test setting for policy/projection parity, the
canonical Intake Desk and local launcher.
Almanac deep-link filters are validated on the server and seed the first client
render directly, removing the extra post-hydration state update and its lint
error while retaining local search and recovery. Portable cache tests differ from the
canonical repository tests only in their import path. The launcher and Desk
remain in their existing repository responsibility homes.

## Preserved performance work

Fourteen implementation/regression files were compared by SHA-256 and are
byte-identical across v261, pinned GitHub main and this reconciled source. These
include bounded shared layer reads, a single hit query, map mutation caches,
water-flow frame batching, cutaway surface ownership, on-demand Underground
loading and terrain performance regressions. The current implementation is
retained rather than replaced with older topic-era source.

Twenty-five focused performance regressions passed. Replaying the existing
controlled lifecycle benchmark against its immutable pre-change baseline gave
6 versus 2 requests for six reads of two dates, and 24,000 versus 200 map
mutations for 100 opacity updates over a synthetic 24-layer/48-renderer registry.
These establish retention of the earlier optimizations, not a new speedup over
v261. Synthetic fixtures are not installed or served. Provider speed, browser
INP, real GPU FPS and physical-device endurance remain unmeasured here.

## Delivery and governance boundaries

GitHub already denies delivery of a statewide locator and 257 exact well/core
tiles. Their original bytes were checked against the prior receipt and an
owner-restricted recovery archive before removing them from this Site's static
delivery tree. The empty `PUBLICATION_HELD` manifest, worker abstention and
source/build/output containment checks now apply together. The separate survey
carrier remains unchanged. Historical Git/Site versions, old client snapshots
and caches are not erased or represented as purged.

The existing project ID, owner-only audience and DB/BUCKET bindings remain.
Database migration files are source only: no D1/R2 mutation, table migration,
package activation, rights approval, source admission or evidence release is
performed. Newly integrated governed controls report unavailable/held until
their actual storage and release conditions are satisfied. Modern almanac
ingestion remains held; the two images retain their source-specific credits
and reuse grounds.

The mirror receipt binds exact source and repository inventories, canonical
path mappings, predecessor evidence and validation. Its review remains pending;
content parity does not constitute human review, general hosted equivalence or
data release. Exact saved source/version, deployment, GitHub PR/head and hosted
checks are recorded separately in the delivery evidence.

## Validation, placement and rollback

Production build and TypeScript passed. The complete built Site suite passed
1,234 tests with zero failures; the 25 performance regressions are included.
Containment passed against both source `public` and built `dist/client` assets.
Nine portable Python cache tests passed. Browser checks and GitHub checks are
reported separately; unrun or inherited checks are not claimed passing.

Accepted ADR-0029 adopts the pinned Directory Rules v2 at
`docs/doctrine/directory-rules.md`. Implementation stays within
`apps/site/source/{app,public,scripts,tests,docs,drizzle}` in the monorepo and the
same homes in the standalone Site. Canonical operator/test mappings remain
`tools/local_data/` and `tests/local_data/`; receipt evidence remains under
`data/receipts/generated/`. No parallel registry, policy or data home is created.

Rollback reverts the new topic/almanac/integration changes while retaining the
GitHub subsurface delivery hold and current safeguards. Previous v261 source
and Git history are recoverable in a task-local, owner-restricted archive outside
Git/deployment assets. Recovery does not authorize serving held exact geometry.
No stored-data migration needs reversal. Source authoring, GitHub merge, private
deployment and owner acceptance remain separate actions.
