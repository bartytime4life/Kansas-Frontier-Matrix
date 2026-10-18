# Focus Mode mirror reconciliation — 2026-10-18

Status: authored repair; repository review, merge and exact-head CI remain separate.
Publication stays on the owner's explicit hold. No application, data, dependency,
model, hosting or service change is part of this repair.

## Failure and bounded repair

At main `cefd19e66857f8bf98b4d6995174c14801deb629`, the selected
`site-v268-explorer-reference-layout-20261017.json` receipt omitted
`apps/site/source/tests/focus-mode-provenance.test.mjs`. The test was already
introduced by merged [PR #5247](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5247),
commit `f64a45a46e82b3c92dfd4e0a6047cb02a29e164a`. The mirror checker rejected
the unrecorded tracked path; all previously recorded bytes matched. The two
layout changes recorded by the predecessor still match their declared digests.
No open PR was returned at the initial and pre-authoring overlap readbacks.
Re-pin main and overlapping work before merge or local alignment.

The append-only successor
`data/receipts/generated/site-v268-focus-mode-test-reconciliation-20261018.json`
adds exactly that existing test as `repository_only_overlay`, with no historical
Site digest. Its SHA256 is
`58d3578d33c9a5479ba807f46397d08c3d1997c8a63dff1a687ff1aa4267277f`.
It is explicitly marked **not proposed in this change**. All 874 predecessor
comparison entries, source identity, canonical mappings, private boundaries and
pending review declarations are unchanged. The predecessor's exact SHA256 is
`1399b86c46f3f89e585774db1fc3a72d4bdc0fa7a232d90ec4ff2b38ac9602d3`.

The selector is updated without changing checker behavior or workflow gates.
The earlier layout regression is pinned to its historical receipt, preserving
its assertions; a new selected-receipt regression proves the exact addition,
lineage, digest, counts and unchanged authority. This does not remove the existing
Focus Mode test or change its bytes to make parity pass.

## Identity and authority

The successor inventory is
`c7c42c59b0a846afed17c5b8232601a5cad1ad5c99bfe0197e2a5f73e9ae6e37`:
875 mirrored paths, 827 identical, 36 inherited overlays, two safety overlays,
ten repository-only overlays; 258 historically withheld carriers remain absent.
The 867 historical source paths and canonical mappings are unchanged.

The original saved-only v268 source
`358280aee889e2e2cf832bd598155ca21653c8de` is retained as historical provenance.
The owner intentionally removed that native Explorer project; this repair does
not recreate or query it, nor equate it with Public Staging, the Node PC
composition or the public GoDaddy deployment.

`REVIEW_ONLY`, `CONTENT_PARITY_ONLY`, pending source/overlay review, false human
acceptance and false hosted equivalence remain explicit. Content parity is not
review acceptance, source admission, data activation, deployment or publication.

Placement follows the adopted Directory Rules and ADR-0029: generated receipts
stay in `data/receipts/generated`, checker selection in `tools/qa`, regression
evidence in `tests/qa`, and this implementation record in `docs/reports`. No new
responsibility root, contract or source authority is introduced.

## Verification in the isolated repair checkout

- Baseline mirror check reproduced `MIRROR_REVIEW_REQUIRED`. The new selected
  regression failed against the predecessor before the successor was selected.
- Repaired mirror check: PASS, `CONTENT_PARITY_ONLY`; review not evaluated and
  258 withheld paths confirmed absent.
- Python 3.12 water CI profile: **343 passed**, including **43 mirror tests**.
  Dependencies were installed with the committed hash-locked installer into an
  isolated virtual environment. An initial incomplete environment could not
  collect the broader suite; after isolation, two loopback tests needed ordinary
  socket permission. The complete suite then passed; no assertions were waived.
- Existing Node Focus Mode provenance test: **one passed**, using unchanged test
  and application bytes. The isolated checkout used an ignored dependency link;
  installed Site dependencies were not replaced.
- Synthetic fixture regeneration: **eight matching outputs**, `synthetic_only`,
  `reviewed_files_overwritten: false`, isolated temporary output only.
- Staged repository topology: PASS, zero new drift or invariant failures, 93
  inherited warnings; the trusted baseline is unchanged. Whitespace checks pass.

Exact-head GitHub checks are reported on the repair PR. A queued check is not a
pass. There is no new full application build, browser acceptance, full security
scan or performance claim: the repair changes receipt selection and regression
coverage, not runtime code, geometry, native values or detail controls.

## Preservation, alignment and rollback

The work is authored in an isolated checkout. The primary PC checkout on its
existing branch and the installed Node Site on port 4173 are preserved. A private
snapshot of the separate PC monorepo's tracked, untracked and material ignored
files, symlink targets and complete Git bundle precedes any checkout update.
An alignment is complete only after exact merged-head readback, clean status and
retained-file verification; its result is recorded separately from author tests.
No Worker mirror replaces the installed Node composition for cosmetic parity.

Rollback reverts the selector, successor receipt and new regression together to
the immutable layout predecessor. It reinstates the omitted-path hold unless the
existing test is otherwise reconciled. No runtime rollback, store migration,
reseed, source capture, data activation or publication is required. All current
public publication holds remain in force.
