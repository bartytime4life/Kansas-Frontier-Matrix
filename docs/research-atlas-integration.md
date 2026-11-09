# Research atlas integration candidate

Status: **implemented candidate; not merged, deployed, or a data release**.

## Scope and identities

The requested `/labs` research atlas is added to the existing GoDaddy Node
composition, with links in welcome Options, the existing Kansas record section,
and the map's More menu. It retains the current welcome layout and topic/map
actions, newer geology and sky behavior, free exports, anonymous application
access, and the source observatory. Nine instrument implementations and thirteen
planned stories have separate source-availability states. Search, field filters,
story URLs, history, modal focus, source details, filtered CSV, and view receipts
are carried over from the local atlas. View receipts are not admission or release
receipts.

On 2026-11-09, public `/api/build` identified application `urdng3v1vk`, 1,232
application inputs, and digest
`sha256:84d98c945c3ee5cdcdae60211e6d0d2d2c0ff316f9e045ae2f350a88da6c7ed5`.
A clean checkout of hosting branch `a0-hosted-ai-web-20261017` at
`6366792b9ffb8d2e7a1b433a38e791850fc8aef8` independently produced that exact
digest and file count. The public build did not report a source commit, so the
match establishes application-input equality, not the provider's Published
commit or settings. The provider dashboard could not be read because Chrome
control failed. Reverify Published and Preview before deployment.

The local atlas source was recovered at `f9aa86027e29f68b72c6738906a2d57847422948`
with uncommitted atlas work. This candidate ports only its research UI, bounded
bundle validation, record instruments, and related tests onto the newer hosting
baseline. It does not replace that baseline with the older checkout, synchronize
the original private Sites project, or change any database/storage bindings.

## Data boundary

`stories` stays in `PENDING_DATASETS`, outside the production `DATASETS` allowlist.
The production application therefore provides the catalogue and instrument
interfaces, but no research snapshots are enabled by this change. Cards display
**Awaiting source release**, and opening a held instrument explains that no
released snapshot is available. No local-preview JSON, acquisition files,
pipeline database, preview-directory setting, or new production data-serving
route is included. The existing development-only middleware remains unchanged.

Client bundle validation is an input-integrity boundary, not a rights decision
or release verifier. It bounds bytes, rows, geometry and required climate
normals; missing or malformed snapshots cannot become a working visualization.
The existing governed delivery gate remains authoritative.

The local snapshot metadata inspected in this session records these holds:

| Instruments | Source metadata | Disposition |
| --- | --- | --- |
| Climate, earthquakes, tornadoes, county population, rivers | Federal-source/public-domain or government-work statements | Candidate snapshots still require the separate review and release decision; source metadata alone is not approval. |
| Deep Time & Fossils, Inland Sea | PBDB CC0 statement, generalized coordinates, protected coordinates withheld, source outlier flags | Sensitivity transforms and underlying scientific references need release review. |
| Iron Horse | Railroad source has no stated redistribution licence | Public redistribution held pending rights resolution. |
| Shifting Lines | Newberry CC BY-NC-SA 2.5 statement | Public/commercial use held pending rights review and applicable conditions. |

No admission, operational ingestion, relay activation, source refresh, DNS
change, model change, or data-publication approval follows from this UI change.

## Placement and review

Directory Rules v2 at `docs/doctrine/directory-rules.md`, accepted through
ADR-0029, assigns deployable user surfaces to `apps/` and explanation to `docs/`.
This checkout is the existing standalone composition of that application;
`app/`, `tests/`, and `docs/` retain their established responsibilities. No new
canonical schema, policy, registry, release, or dataset home is created. Synced
ChatGPT project sources remain read-only.

An open-PR search for labs/atlas found no matching open integration PR. This is
a bounded keyword check, not proof that no concurrent work exists. Existing
unfinished owner worktrees are preserved. The implementation was reviewed in
this session; independent review remains open.

## Validation and rollout

Initial candidate checks passed 45 focused tests, production build, TypeScript,
and 24 HTTP/runtime checks. Browser checks exercised search, a held instrument's
deep link and close behavior, return to the current welcome, and welcome Options
navigation into `/labs`. At 375 pixels the page had no horizontal overflow.

The first broad run used local Node 22.13.1: 2,772 passed, 14 failed, 25 skipped.
Thirteen failures involve unavailable SQLite `rtree`/`fts5` support; the remaining
identity failure followed a source edit after the build and requires a rebuilt
artifact. The installed Node 24.11.1 was checked in memory and supports both
SQLite modules. Final checks and any superseding broad-run result are recorded
in the PR; do not treat this initial run as passing. Hosted CI, GoDaddy preview,
live acceptance, complete accessibility and scientific/data-release review are
separate evidence.

Deploy only the reviewed application revision through the existing GoDaddy
composition. Recheck the provider's source, Preview and Published state, preserve
settings, and verify `/labs`, map navigation, browser assets, `www` redirects,
and `/api/build`. This candidate alone will not reproduce the private preview's
populated plots: research-source publication remains held.

Rollback is reversion of this application's integration commit and redeployment
through the same host, with source-identity readback. No data migration, deletion,
DNS reset, or original-Site rollback is needed.
