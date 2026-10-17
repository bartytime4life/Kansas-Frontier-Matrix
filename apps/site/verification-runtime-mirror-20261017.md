# Explorer runtime and recorded-mirror CI repair

Base: `main@e30566dfa299fd3e540da239a5c9ec018b2fd4cc` (merged #5221). This is a repository repair only; no Site deployment, private data operation, source admission or human review approval is performed.

## Failures and repairs

The [previous Explorer run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39005752061/job/117317768099) built successfully but its local-runtime test failed with `STARTUP_FAILED`. The launcher called `validateSubsurfacePublic` without importing it. Restoring the import lets the existing containment validator execute before configuration, credentials or runtime initialization. The unmodified validator still rejects withheld assets. A new launcher regression uses only a synthetic forbidden file and verifies the explicit `SUBSURFACE_PUBLICATION_HELD` denial before private configuration is read. Existing HTTP tests retain forged-identity, rebound-host and archive-authorization denials.

The [previous water-conformance run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39005752055/job/117317768007) passed its Python tests and stopped at `MIRROR_REVIEW_REQUIRED`. That is the mirror command's generic failure code: its selected manifest no longer matched merged main. Diagnosis found 21 changed files and four added paths, with no deleted or restored-withheld files. The launcher repair restores its exact recorded source bytes; this change additionally updates the existing runtime test. The new dated manifest records all 874 tracked Site files and preserves each historical Site digest. Its reconciliation identifies 25 updated entries and the exact launcher restoration, with predecessor hashes, current-main hashes and commit provenance. The previous receipt remains byte-for-byte unchanged.

`tools/qa/site_mirror.py` changes only its selected receipt path. Its file-set, hash, symlink, path, count and withheld-file checks are unchanged. The selected receipt retains the same 258 withheld paths, source identity, owner-only audience, canonical mappings and pending-review declarations. A regression binds its predecessor digest and checks those retained fields and the distinction between Site bytes and repository overlays.

The final overlap search found [PR #5222](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5222) at `164f8d1b9287bfb93788b7e1823bde71994fa691`, prepared from older main `2b22ed1115`. Its launcher restoration is byte-identical to this repair. Its manifest covers #5218 and predates the merged #5220/#5221 layout changes, so it cannot establish current-main parity. This candidate records those newer bytes and adds the containment/provenance regressions. No change was made to #5222. Both touch the selector; retain the current-main manifest when reconciling them rather than reverting to the older file inventory.

## Validation before opening the draft

| Check | Result |
|---|---|
| Original runtime HTTP test before repair | FAIL reproduced: `STARTUP_FAILED` |
| Runtime suite after repair | PASS: 10 tests, including the new containment denial |
| Fresh production build and static containment | PASS |
| Complete Explorer suite | 1,372 passed, zero failed; two existing Linux `/proc` tests skipped on macOS |
| TypeScript | PASS |
| Focused runtime/test ESLint | PASS: zero errors or warnings |
| Whole Site ESLint | Zero errors; 77 existing warnings in unchanged files |
| Mirror suite | PASS: 39 tests, including negative drift, withheld-path and receipt cases |
| Combined water and smoke-preflight suites | 344 passed; one Linux-specific smoke harness failed because macOS lacks `/usr/bin/setsid`. All water-conformance tests passed. |
| Synthetic fixture regeneration | PASS: eight outputs in temporary storage; reviewed fixtures not overwritten |
| Recorded content parity | PASS: 874 files, 258 withheld paths confirmed absent |
| Source/overlay review | PENDING; human acceptance remains false |
| Hosted equivalence | False; not established by parity or tests |
| Exact-head Linux CI and full backend smoke | Pending draft PR; see its checks and final description |

The local full Node run uses a canonical temporary directory to satisfy filesystem checks on macOS. Temporary HTTP stores and synthetic fixtures are separate from operator storage. No existing D1/R2 data, credentials, browser state, audience, storage binding, API policy, application layout or deployed source was modified. The original checkouts and unrelated document changes remain untouched.

## Post-merge reconciliation — October 17, 2026

The owner requested reconciliation and conditional merge after checks pass. A
fresh readback found both original PRs already merged: #5222 at
`da5bc7b0ae14a9383efec17f9c9dfb0e9c4039eb`, then #5223 head
`17d198550f1bd9e2b63f9325fc9073ce18533dcf` at
`1f92e4ff2340cca4115a2d20ffbf3233aaf2694b`. The earlier overlap paragraph describes
an old #5222 head; its final `02db0d2` head already covered 874 files and passed
100 checks with four skipped. Both historical receipts remain intact.

The later #5223 changes removed `RECEIPT` from the checker. Water-conformance and
full Python collection then failed because `TOOL.RECEIPT` was absent; topology
also lost the receipt used to resolve upstream-backed names. The launcher import
was already restored correctly. The forward repair restores only the selector
to `site-v268-current-main-runtime-reconciliation-20261017.json`, which includes
#5223's containment test and binds all 874 current paths. The checker now matches
its original #5223 artifact digest `7d27db66…` again. No new mirror receipt or
baseline change is required because application bytes are unchanged.

Local Python 3.12 validation passed all 339 water-conformance tests and regenerated
eight synthetic fixtures in isolated output. The restored checker passes
`CONTENT_PARITY_ONLY`, confirms 258 withheld paths absent, and retains pending
review, human acceptance false and hosted equivalence false. Topology must be
checked against the staged index; a run before staging still sees the deleted
selector and correctly fails. The subsequent staged check passed all four
components with zero invariants/new drift and 93 unchanged baselined warnings.
Final exact-head CI and merged-main CI remain
separate gates recorded in the follow-up PR.

The installed Node composition and its preserved API capsule already contain the
correct launcher bytes (`6f7eb010…`). They are separate from this Worker mirror;
do not replace their application tree, data or bindings to achieve byte parity.
The original hosted Explorer was intentionally removed by the owner. Existing
Public Staging and GoDaddy publication are separate and are not republished by
this repository repair. Other working copies and private stores are preserved.

## Placement and rollback

The launcher and adjacent regression remain in `apps/site/source`; repository parity selection remains in `tools/qa`, with its tests in `tests/qa`. The dated manifest and generated provenance receipt remain under `data/receipts/generated`. This record follows the existing `apps/site/verification-*.md` lane. Directory Rules v2 and accepted ADR-0029 retain these established ownership boundaries.

Restore the previous receipt selector to roll back reconciliation; it will correctly report the current repository drift again. Revert the launcher/test change only with a replacement forward fix because the missing import prevents startup. Neither rollback requires a deployment or data migration. Review, merge, source activation and deployment remain separate actions.


## Forward lineage correction after both PRs merged — October 17, 2026

CONFIRMED against `main@12bfe5e9da7b46e06379c574d6db194d940e40ff`:
#5222 merged at `da5bc7b0ae14a9383efec17f9c9dfb0e9c4039eb`; #5223's
final head was `17d198550f1bd9e2b63f9325fc9073ce18533dcf` and merged at
`1f92e4ff2340cca4115a2d20ffbf3233aaf2694b`. #5225 and #5226 restored the
receipt selector. No original candidate remains open to consolidate or retire.
The earlier comparison in this record describes a historical head, not the final
#5222 implementation. The GitHub review threads were resolved by the owner;
resolution does not itself prove that the provenance discrepancy was corrected.

The selected current-main receipt still named the a11y receipt as its predecessor.
Its actual parent had already selected the local-port receipt from #5222. Comparing
those inventories shows exactly one changed mirror path:
`tests/local-worker-runtime.test.mjs`. The other 24 paths in #5223's historical
reconciliation were already recorded by #5222, and the launcher import was already
restored. #5222's automated review examined `164f8d1`, not final head `02db0d2`;
#5223's automated reviews examined final head `17d1985`. Neither original PR has a
submitted GitHub approval in this readback. This report supplies no retroactive
merge authorization.

The [successor receipt](../../data/receipts/generated/site-v268-consolidated-runtime-lineage-20261017.json)
preserves the base-selected runtime receipt as its immediate predecessor, bound by
SHA-256. Its explicit historical correction also binds the local-port receipt and
records the true #5223 delta. All historical receipts and generated receipts remain
byte-for-byte intact. Twenty-four per-path provenance notes are restored from
#5222; the successor's own application delta is empty. Its full manifest repeats
the established format because the parity checker consumes a complete inventory,
not a patch. This preserves compatibility without a second receipt mechanism.

All 874 mirror paths and hashes, 46 overlays, source identities, canonical mappings,
258 withheld paths, review restrictions and safety regressions remain unchanged.
Content parity is `CONTENT_PARITY_ONLY`; source/overlay review is pending, human
acceptance is false and hosted equivalence is false. This correction changes no
application, source, storage, publication or activation state.

Local verification for this successor: 40 mirror regressions passed; the filtered Node test
could not load because this clean checkout lacks generated
`dist/server/wrangler.json`. A direct containment probe was also blocked by the
local sandbox (`spawnSync EPERM`) before its child process ran. Neither attempt
is claimed as passing. Exact-head Linux CI must run the existing containment
regression and full runtime smoke. The new regression distinguishes the actual
parent's one-path delta from the preserved historical 25-path comparison and checks
both predecessor hashes. Exact-head hosted water, Explorer and validator results
belong in the follow-up PR's checks and description; they are not inherited from
prior heads. No full local Explorer build or full repository test run is claimed.

Placement uses Directory Rules v2, adopted by ADR-0029: §10.1 keeps repository QA
under `tools/`; §11.2–11.3 keeps durable provenance in `data/receipts/`; §9.1 keeps
human guidance in its established lane. The supplied Directory Rules PDF §4 and
§5 likewise route by responsibility. This existing application verification record
stays in the established `apps/site/verification-*.md` lane. ADR-0048 continues to
resolve the single selected mirror manifest. No roots or authority homes change.

Rollback this forward correction as one commit to restore the base-selected
`site-v268-current-main-runtime-reconciliation-20261017.json`. That retains the
same runtime bytes and safety regression while restoring the historical provenance
discrepancy. The earlier local-port/a11y receipts are historical evidence nodes,
not this correction's immediate rollback target. Human review, owner merge
authorization, Site publication and source activation remain separate and pending.


The broader local water command completed with 338 passed and two failed. Both
failures stop at loopback socket creation with `PermissionError: Operation not
permitted` in this sandbox. Initial collection attempts also lacked checkout-local
package imports; the completed run used the existing `packages/*/src` directories
and governed API source explicitly. No passing full local water run is claimed;
the exact-head Linux workflow must resolve these environmental limitations.
