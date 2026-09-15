# Current Site identity and source alignment

## Current v40 readback

**CONFIRMED at 2026-09-15T17:26:23.271Z; source parity only.** This section supersedes
older present-tense version, mirror, base, archive and recovery-candidate claims.
The v37 checkpoint below and its original generated receipt remain historical.

| Surface | Observed identity |
|---|---|
| Canonical monorepo base / tree | `b18b7276faa3cdad15f2ed34270b6640559bdf27` / `8265b7a9afef5a515be12b53a47768d7acf3ddf7` |
| Existing project / audience | `appgprj_6aa0b1c41bc08191bfd86003920f1631`; custom owner-only, access revision 1 |
| Slug / URL | `kansas-frontier-matrix-explorer` / <https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site> |
| Saved version | `40`; `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_3d935d1123408191bf9743d174a9b7b9` |
| Sites source | `a4181a42a0a7c02f8e7d837242025f13cbf9a861` |
| Existing mirror | `agent/kfm-site-source-sync-20260912` at `c4e5ebe54cba9d7ca9bbee108b442bdf68763f58` |
| Equal complete source tree | `57af63be95a0322dac06b9872df82e5e790d48f9`; 136 tracked files |
| Saved archive, platform readback | TAR; 61 files; 11,192,320 bytes; `sha256:f57ec9072b284170d8afc03378ecc0f74d2d7cb54b4514ccbe688f9816d46b29` |
| Deployment readback | `appgdep_6aa9777b19a88191bc0865342215577e`; succeeded at `2026-09-15T16:52:19.838857Z`; environment revision 1 |
| Immediately prior saved version | `39`; `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_876c0d8d8ed48191b6872f6d1028f6ea` |
| Prior source / archive | `a498d70ea71f4dca68fe15698fb1d582659626bb`; `sha256:2c16720de9b848ece16f6ca008c40c201ae9a1024ca943c1c00f7c06e49de110`; 57 files, 11,161,600 bytes |
| Prior deployment | `appgdep_6aa96e6103588191bfbe9dbc69cfe629`; succeeded at `2026-09-15T16:13:12.454404Z` |
| Storage readback | D1 `DB`, tables `data_submissions` and `data_submission_reviews`; source declares R2 `BUCKET`; no rows or objects exported |

The existing mirror already matches v40; this convergence run makes no mirror
write. Its parent chain retains v39 `3d83dcaf5920bb97e849145f9e04a25bf9a87d6a`
and v38 `3ce5730c619c0d6ad12da46ab519f807a2bee855`. The immutable-tree checker
passes for all 136 paths. Source files and deployment-package files are distinct
inventories. The archive digest above is **platform-reported**, not an independently
verified TAR-byte hash. A local candidate has matching expanded size/file count
but different byte hashes; archive equivalence remains **NEEDS VERIFICATION**.
Version 39 is an available recovery candidate, not proof of rehearsed restoration.

Against the pinned monorepo app's 93 tracked files, 52 relative paths are shared:
21 identical and 31 different; 84 are Site-only and 41 monorepo-only. Whole-tree
replacement would discard monorepo-only safeguards. Retain the two existing
application boundaries and accepted package renderer seam. ADR-0005's proposed
canonical-shell choice is not accepted by this comparison. Identity correction
keeps monorepo D1/R2 null; it does not activate the Site's intake implementation.
Source-controlled examples, context metadata and schema/migrations require
separate rights, sensitivity, lifecycle and consumer disposition before import.

Repeat source comparison from this application directory:

```bash
node scripts/verify-sites-source-alignment.mjs /absolute/site-checkout a4181a42a0a7c02f8e7d837242025f13cbf9a861 /absolute/mirror-checkout c4e5ebe54cba9d7ca9bbee108b442bdf68763f58
```

The current run passes 40 focused source-parity, identity, receipt and build-wrapper
checks under Node 24.19.0. This runtime is outside the repository's declared Node
22 range; supported-runtime build/browser acceptance remains open. No production
build or browser proof is inferred. Ruleset 15484585 still has no required-status-
check rule, and no open PR was returned. #4024 remains branch-only; #4228 Stage 1B
HOLD, Stage 2 unauthorized, #3366 and #3396 acceptance remain open.

The fresh authoring receipt is
[`genrec-sites-source-alignment-v40-20260915.json`](../../../data/receipts/generated/genrec-sites-source-alignment-v40-20260915.json).
Correction is a new versioned commit on the existing alignment branch. The original
v37 receipt is unchanged; its claims must be assessed against its historical
artifact revision, not current working files. No Site version, audience, binding,
source, deployment, repository main, PR lifecycle, release, promotion or publication
was changed by this refresh.

## Historical v37 checkpoint

Everything below records the earlier v37 execution scope, not current Site state.

**Historical 2026-09-15 UTC — Site mirror aligned; monorepo integration held.**

The owner asked to align the existing Site and GitHub repository. This change
records the observed current Site as this application's target, advances the
already-existing standalone Site mirror, and preserves the monorepo's accepted
renderer and evidence boundaries. It does not identify the two historical Site
projects as aliases or assert who authorized the original replacement.

## Verified identities and histories

| Surface | Exact observation |
|---|---|
| Current Site project | `appgprj_6aa0b1c41bc08191bfd86003920f1631` |
| Slug | `kansas-frontier-matrix-explorer` |
| URL | `https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site` |
| Audience | Custom owner-only access; revision 1; current actor is owner |
| Saved and deployed version | `37` |
| Version ID | `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_b643c8272b1c8191992aaedf7c630639` |
| Sites source commit | `1cdabb970412b9d67270e04205918bb394a8318f` |
| Complete source tree | `5e419bf6079e1fc45037a955e58350e8cd8ffc2a` — 129 tracked files |
| Saved archive | SHA-256 `9a8fb1b23b46280d71ab9bf26de67880af48fd43b4cfcaa068cde159869ca7da`; 69 packaged files; 13,219,840 bytes |
| Deployment | `appgdep_6aa7377ce6bc81919eb0aaf3963c4aaf`; `succeeded`; 2026-09-13T23:54:33.700268Z; environment revision 1 |
| Canonical monorepo base | `32953ec3b662dba14546e224554c9621b72268de` |
| Existing Site mirror | `agent/kfm-site-source-sync-20260912` |
| Previous mirror commit | `4bc5233eca69030dafc8f7e8b85bbb0d505136ac` — version 33 |
| Aligned mirror commit | [`e2f513a7ff118eef0b83b5a403cbdfc8a143b039`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/e2f513a7ff118eef0b83b5a403cbdfc8a143b039) — version 37 |

The mirror update has the previous mirror commit as its sole parent. All 18
changed blobs and the full tree match the Sites source exactly. Neither Git
history was rewritten. Commit IDs differ because the histories are different;
tree IDs match because the committed source bytes match. Source files and
packaged deployment files are different inventories, so 129 and 69 are not a
count discrepancy. Archive integrity here is the Sites platform's reported
identity; this turn did not rebuild or independently rehash that archive.

The Site source history has 38 commits. Its root is
`f6d746287833a70f1c5789960e42e9919d22af46`, created 2026-09-09T01:11:49Z,
already carrying the current project ID. The old repository pin
`appgprj_6a870a079c1c8191abb7401ef092a181` returned `NOT_FOUND` in the connected
inspection. That result does not establish deletion, an alias, or the original
actor's authorization. The old ZIP, v1 receipt, and historical handoffs remain
lineage, never current execution inputs.

## Two source layouts, one explicit relationship

GitHub `main` is the canonical implementation and contributor-contract surface.
The existing mirror branch preserves the actual working Site at its standalone
repository root. **Do not open a pull request merging the mirror branch into
monorepo `main`**: its layout is different and such a merge is not an application
integration strategy.

The monorepo app under `apps/kansas-frontier-matrix-explorer/` still uses the
accepted `packages/maplibre/` facade and `NullMapRuntime`. The hosted source has
its own renderer, operational-context adapters, private D1/R2 intake, and newer
UI features. Source mirroring does not admit those capabilities into the
monorepo. It also does not resolve the separate synthetic Atlas candidate's
EvidenceBundle/API/Explorer/recovery integration.

The monorepo hosting manifest now selects the verified current project, but its
`d1` and `r2` stay null because this implementation does not own the hosted intake
schema. The Site's existing `DB` and `BUCKET` bindings stay intact. Copying either
manifest over the other would conflate identity with capability composition.
No live Site source, binding, dependency, access, version, or URL was changed.

At the pinned monorepo base, 51 relative paths are shared with the Site: 21 are
byte-identical and 30 differ. Another 78 paths are Site-only and 42 are
monorepo-only. The latter include error recovery, layer-library controls,
deployment validation, and build-input checks. These safeguards must survive
any later integration. `apps/explorer-web/` is a separate reusable application,
not the owning directory for this Site comparison.

## Repeatable source verification

From the monorepo application directory, pass two checkouts and immutable full
commit IDs (a checkout may contain both histories):

```bash
node scripts/verify-sites-source-alignment.mjs /absolute/site-checkout 1cdabb970412b9d67270e04205918bb394a8318f /absolute/mirror-checkout e2f513a7ff118eef0b83b5a403cbdfc8a143b039
node --test tests/sites-source-alignment.test.mjs tests/hosting-boundary.test.mjs tests/sites-deployment-receipt.test.mjs tests/sites-deployment-receipt-v2.test.mjs tests/build-verified.test.mjs
node scripts/validate-sites-deployment-receipt.mjs --current fixtures/sites-deployment-receipt/current-project-rehearsal.json
```

The checker reads committed objects, not unstaged working files or live runtime
state. It requires the current project identity and equal complete Git trees,
including paths present on only one side. `PASS` means committed Site-mirror
bytes match. A wrong project or differing tree gives `HOLD`; missing objects or
mutable/abbreviated refs give `ERROR`. Neither `PASS` nor a valid receipt grants
deployment or monorepo runtime parity.

For a future update: read current Sites version/deployment metadata; fetch its
exact source commit; compare with the current mirror tip; inspect changed paths
for secrets, private data, build debris, and unintended policy changes; and
advance only the existing mirror with a non-forced commit retaining its parent.
Read back the branch tree and verify it equals the exact Site source tree.
Never use an obsolete pin as proof of currentness or publish merely to make
commit timestamps resemble each other.

The alignment run passed 40 native identity, source-parity, receipt, and build-
boundary tests; both JSON Schema fixtures validated. After the existing locked
Site installation completed, 19 targeted Site tests passed. The topology ratchet
retains the same two inherited drift fingerprints and 125 warnings; the baseline
and frozen catalog are unchanged. These checks do not replace a new build or
production browser proof.

## Current receipt and deployment gate

[`sites-deployment-receipt-v2.schema.json`](../contracts/sites-deployment-receipt-v2.schema.json)
binds the current project and adds the exact Sites source commit, full source
tree, and mandatory source-alignment check. Use the validator's `--current`
mode for current operator receipts. The v1 schema and original fixture remain
byte-for-byte historical inputs; a valid v1 receipt is rejected by current mode.
The new fixture is explicitly synthetic, `HOLD`, and `NOT_RUN`; its placeholder
hashes and checks are not operational evidence.

Every current deployed/rolled-back readback requires source alignment, install,
build, tests, lint, desktop, mobile, restricted-state checks, and rollback
rehearsal to pass against the intended candidate. Retain the actual same-Site
rollback target and verify the current audience. Availability in version history
does not prove that restoration was rehearsed. Version 36 remains a recorded
recovery candidate, not an exercised rollback:
`appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_b8b485a7b5248191ac2e17d3a071734f`.

This change validates identity and source records. No new candidate was saved,
deployed, restored, or subjected to a production browser smoke. Existing version
37 stays deployed. Its older repository briefing is a historical snapshot with
a separate read-only main lookup; source mirroring does not refresh that UI.

## Remaining integration and release boundaries

1. Migrate the existing Site's renderer capabilities through the accepted package
   seam, retaining actual map interactions and the repository's negative states.
2. Reconcile the existing context/intake routes with API, evidence, rights,
   sensitivity, and source-admission contracts; preserve provider-context labels.
3. Verify standalone build assembly and dependency closure, including package
   source, worker/CSS assets, and browser behavior before selecting a candidate.
4. Close #4024's independent review and required-check enforcement proof before
   using an eligible PR path. This authoring path remains `VALIDATED_BRANCH_ONLY`.
5. Keep #4228 Stage 1B on `HOLD` and Stage 2 unauthorized. Keep milestone 1's
   deadline at 2026-09-18T00:00:00Z (September 17, 7 p.m. America/Chicago) and
   resolve its five acceptance holds explicitly. Finish the existing synthetic
   Atlas proof chain before expanding hydrology.

## Placement and correction

Accepted ADR-0029 and the exact adopted Directory Rules bytes govern placement.
Application identity, its schema projection, CLI, and focused tests stay under
the existing `apps/` responsibility. The generated-work receipt belongs under
`data/receipts/generated/`. No new root, renderer authority, lifecycle stage,
topology waiver, or publication decision is created.

If a correction is needed, revert the monorepo alignment change as a unit while
preserving its generated receipt and historical v1 files. Correct the mirror by
a new commit based on its current tip; do not force-push or erase version 33/37
lineage. A source correction does not itself roll back the deployed Site.
