<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/kfm-synchronization-20261009
title: KFM PC, GitHub, Site and project-record synchronization
type: report
version: v1.0-draft
status: draft; source-reconciled; mirror-review-pending
owners: ["@bartytime4life via CODEOWNERS"]
created: 2026-10-09
updated: 2026-10-09
policy_label: repository-facing
owning_root: docs/
responsibility: Record exact synchronization identities, validation, recovery and unresolved boundaries.
truth_posture: CONFIRMED observations are scoped below; merge, mirror approval, source admission and release remain separate.
related:
  - apps/site/README.md
  - apps/site/source/docs/unified-download-workspace.md
  - docs/reports/documentation-enrichment-20261008.md
[/KFM_META_BLOCK_V2] -->

# KFM synchronization — 2026-10-09

This is a one-time owner-authorized KFM synchronization. It excludes MEGALODON,
plugin configuration, unfinished AI/installer work, dataset activation and
recurring synchronization. Delivery is [draft PR #4959](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4959);
the owner retains the merge decision.

## Source identities and reconciliation

| Surface | Verified identity and disposition |
|---|---|
| GitHub `main` and primary PC checkout | `d07557107863f60a95b44c6d720147deb16a55b9`; primary clean checkout fast-forwarded 43 commits |
| Repository source delivery | `8011ad127fae9b6f176ccf3022481bf70fc51fd4` on `codex/kfm-synchronization-20261009`; subsequent report-only commits do not change application bytes |
| Prior hosted Site | v186, source `83c81618b407675206ad880c8f9a607e36c23e6f`; existing project `appgprj_6aa0b1c41bc08191bfd86003920f1631` |
| Prior installed Explorer | `c06c4716fe7ab1cc252db5ab940ef282dfacdfc8`, retained directory `KFM-Explorer-Site-download-workspace-20261008-r2` |
| Reconciled standalone Site | `05dddb4e26daff98ea856ba03d34546afb503f81`; same Site history, based on v186 with selected download/timer commits |
| Submitted archive | Compressed SHA-256 `8ce90d58ff5aec4d4d55b7966e97aba359a04d7208d8a6f3bcdeddd4b90fff46`; 31,278,296 bytes; 398 files |
| Stored Site archive | Platform-returned tar SHA-256 `527b18e6a55d158a0a1b1901b4000ed5625588b589931253851ca79e6a534747`; 49,571,840 bytes; 398 files. This is the platform's stored representation, not the compressed upload digest |
| Published Site | v187; source `05dddb4e26daff98ea856ba03d34546afb503f81`; deployment `appgdep_6ac87df097788191838db81c548d8cbd` succeeded; environment revision 5 |
| Installed candidate | `KFM-Explorer-Site-sync-20261009`, all 810 tracked source files equal to the standalone commit |

GitHub and the standalone Site retain different Git histories. Byte comparison
establishes parity: 808 standalone files match `apps/site/source` exactly. The
remaining two already have canonical repository homes: `scripts/basemap-cache.py`
is byte-identical to `tools/local_data/basemap_cache.py`; its Python test matches
`tests/local_data/test_basemap_cache.py` except for the import path. They remain in
the standalone Site and canonical tools/test lanes, avoiding a new deployable
internal-store reference in the mirrored app. This mapping is review evidence,
not approval of the existing governed mirror receipt.

The unified Find data, My library and Activity views retain shared download
state, progress, cancellation and the browser timer binding repair. Overlaps were
resolved explicitly: pinned NMMR research links survive offline/empty discovery,
failed catalog reads retry on the next healthy poll, previews reset immediately
when the selected record changes, and library summary definitions retain valid
HTML. GitHub's interface, scene-effects, accessibility and audit work is retained.
No public API or saved-workspace format was introduced.

## Runtime and recovery

The stable local origin remains `http://127.0.0.1:4173`; the source alias is
`/home/bartytime/Projects/KFM-Explorer-Site-current`. The physical store remains
`/home/bartytime/Projects/KFM-Explorer-Site-v109/.wrangler/local-state`.
The application source, source-history bundle, previous build, service unit and
drop-ins, stopped-writer D1/R2 snapshot and file hashes are preserved outside app
source under `/home/bartytime/KFM-site-recovery/kfm-sync-20261009`.

The initial consistent snapshot verified 18,410 files and eight SQLite databases.
The copied-state rehearsal used port 4187. Both selected submission indexes are
present after migration, database integrity passes, and every user-table row is
unchanged. Runtime `_cf_METADATA` bookkeeping may advance. The retained R2 store
contains 15,840 object records; no dataset activation was performed.

Only `drizzle/0004_submission_list_order.sql` is selected for the live migration:
`idx_submissions_created_id(created_at,id)` and
`idx_submissions_owner_created_id(owner_key,created_at,id)`. Both are additive
`CREATE INDEX IF NOT EXISTS` statements. Migration files/history and stored rows
are preserved. Deployment success and hosted index verification are separate
observations.

Installation succeeded: all 398 installed build files equal the verified standalone
build, the alias selects the reconciled source, and the existing Explorer service
is active on loopback port 4173. The immediate pre-install stopped-writer snapshot
verified 18,412 files. Offline migration preserved every stored row and every R2
byte, verified both index definitions and retained SQLite integrity. Local
submission/review tables remain empty. Fresh browser readback connects to the
existing local operator, displays 1,695 catalog records and 12 recent transfers;
no new transfer was started.

[The existing private Site](https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site/downloads)
deployed successfully as v187, saved version
`appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_6055ea04b7a88191a697a6ec0a3136e5`.
Fresh readback confirms the exact source commit, `DB`/`BUCKET` declarations,
unchanged owner-only access policy revision 1, no viewers/groups, and anonymous
HTTP 403. The owner's browser loads the new download interface and library/activity
views. Hosted `DB` retains its table inventory and empty submission list. The
archive carries the selected migration and the deployment succeeded; the available
Sites database tools expose tables/rows but not index metadata or migration-ledger
queries, so independent hosted index introspection remains **unavailable**. This
limitation is not presented as a migration failure or an index verification pass.

Rollback selects the preserved local application source/build via the stable
alias, or prior private Site v186. Compatible additive indexes can remain. Never
restore an earlier database over later writes. Only the Explorer service may be
restarted for this installation; companion services are outside the change.

## Validation and security coverage

| Check | Evidence and limit |
|---|---|
| Site build, TypeScript and lint | Pass; zero lint errors, 45 existing warnings |
| Site tests | 766 pass, zero failures/skips; includes download races/timer context, catalog recovery, cancellation, source links and pagination with 75 tied-timestamp rows |
| Standalone cache tests | Eight Python tests pass; canonical repository implementation is unchanged |
| `make site-check` | Build/lint/types/766 tests passed; its smoke step correctly refused occupied port 4173. The identical smoke step was replayed at 4186 and passed 57 assertions across 47 routes; nine provider-only routes remain outside smoke coverage |
| Workflow security | Pass |
| Repository topology | Pass: zero invariants/new drift, 113 retained baseline warnings |
| Governance parity | `LANE_OUTCOME_MISMATCH` for `root-registry`; reproduced on unchanged main at `d07557107863`, not introduced by synchronization |
| Governed routes on copied state | Water/knowledge remain ABSTAIN with `NO_APPROVED_SNAPSHOT` / `NO_APPROVED_KNOWLEDGE`; Crop-CASMA remains `NO_APPROVED_SOIL_PACKAGE` |
| Local access boundary | Anonymous submissions return 401; injected hosted identity headers return 403; direct runtime binds loopback |
| Browser | Fresh download discovery, library/activity views, empty-search official links, keyboard activation, terrain/globe switching, scene preset and Escape, and Underground workspace exercised. Download and Underground layouts have no horizontal overflow at 390 pixels |
| Browser limits | CUA pointer activation was unreliable; keyboard activation worked. Real transfer progress/cancellation use deterministic harness coverage, not a newly acquired dataset. This is bounded interaction evidence, not exhaustive touch/visual/accessibility acceptance |
| Security | Required delegated preflight passes; pinned diff scan `28ee056c-cd8d-42fb-af9a-e76bcfdfd77b` covers `ecc8921b715959095bafcd7bc201bc4f14b5b7c6..05dddb4e26daff98ea856ba03d34546afb503f81`; sealed and read back at 05:40:18 UTC. All 74 changed source items reviewed; zero new reportable findings |

All 11 existing KFM security bundles validate without rewriting sealed results.
The new review covers changes introduced to GitHub or either runtime plus needed
supporting code; it is not a full repository audit. Sensitive evidence stays in
private managed scan artifacts. External companion enforcement, platform identity
sanitization and a full live-provider audit are explicit coverage gaps. No finding
is closed merely because a newer version was deployed. The three prior findings
have current fix evidence and 16 passing offline regressions, retained in a
separate private reconciliation artifact. Automated safety controls blocked one
dynamic candidate-validation attempt before execution; no runtime pass is claimed
and no alternate execution was attempted. Static disposition completed in the
sealed review. These are bounded review results, not a general security guarantee.

## Records and remaining decisions

[KFM Repository Workbench](https://app.notion.com/p/3c9a92021bf68195b8b1f3a8d694b447)
and [KFM System Chronicle](https://docs.google.com/document/d/1fBOUDqrcsHaPJiEfM5HmtJL7fBMKFr-rgoN2ge_uVrI/edit)
receive one dated checkpoint with current navigation. Existing historical entries
remain. Fresh GitHub readback confirms [PR #4941](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4941)
merged as `3b39b948919b51433db369b816e3ea748c54df1f`; its earlier draft/open labels
are historical.

The primary checkout stays on GitHub main while local and hosted runtimes may use
this unmerged draft source. AI worktree `8f5a` and installer worktree `998d` retain
their independent unfinished work. `MIRROR_REVIEW_REQUIRED`, source-admission,
activation and release decisions remain unchanged. Fresh comparison evidence is
pending owner review and does not replace an approved receipt.
