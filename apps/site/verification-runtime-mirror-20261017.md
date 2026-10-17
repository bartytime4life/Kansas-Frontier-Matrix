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
