<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/explorer/esbuild-policy-guard-review
title: esbuild repair policy-guard review
type: app-maintenance-review
version: 0.1.0
status: branch candidate; independent review pending
owning_root: apps/
responsibility: review findings and regression coverage for the paired dependency repair
truth_posture: author review is not independent approval or alert closure
updated: 2026-09-05
[/KFM_META_BLOCK_V2] -->

# esbuild repair: policy-guard review

This addendum reviews repair head `f1d48190f27a2b7f47692e0e186142afbf1dc9cb`
against main `5f03c5c8129d9fc86b3cb7b19a48aaa3c1420a4f` (PR #4299).
It supplements the [remediation record](esbuild-security-remediation.md), not its
historical execution results. The two additional main commits change only
three temporal/workspace files; no dependency or policy path overlaps the repair.
The branch reconciliation preserves those current-main files unchanged.

## Finding and correction

**CONFIRMED test-coverage gap, not an observed policy weakening.** The old test
looked for the six allow/deny lines as substrings. In disposable local copies,
the complete old static test suite returned exit 0 after an extra package build
approval was inserted, and after a denied package was allowed while its old
denial remained in a comment. Its dependency checks therefore did not prove
that the effective policy had stayed unchanged.

The [guard](../tests/esbuild-security.test.mjs) now compares the complete small
workspace file to the exact reviewed snapshot, including the parent-qualified
override. Six synthetic mutations cover additional approval, comment-spoofed
approval, commented-out denial, a duplicate policy section, a broadened override,
and a vulnerable replacement version. The two full-suite bypass reproductions
now exit 1; the unchanged fixture exits 0. No mutated policy was installed or
committed. Both dependency locks, both override declarations, and all six
allow/deny decisions remain byte-identical to the prior repair head.

The snapshot is a deliberately strict regression assertion, not another policy
home or a YAML interpreter. Even a benign formatting or workspace change needs
an explicit expected-snapshot update during review. The authoritative policy
remains `pnpm-workspace.yaml`; this test does not inspect global configuration,
environment/CLI overrides, or every possible installer execution context.

## Validation scope

Local checks used Node 22.16.0 without dependency installation: the old test was
recovered as exact Git blob `7a0d72b39aefbb0741be1f5837ebcc624e6f9c84`;
the reviewed static fixture passed, both negative full-suite fixtures failed as
expected, all six in-test mutations were rejected, and syntax checking passed.
Runtime probes were explicitly skipped locally. A local Git fetch failed on DNS;
no local full-checkout or frozen-install success is claimed.

The [read-only workflow](../../../.github/workflows/esbuild-security.yml) retains
both installer jobs and their runtime probes. It also runs Explorer unit and
Playwright tests, the Sites application build from the complete workspace, and
post-command policy/lock checks. A separate job uses the existing locked Python
installer and native GeneratedReceipt validator, including exact-ancestor replay
for the two immutable historical receipts. These jobs authenticate no reviewer
and authorize no PR transition. Final-head hosted outcomes must be read from the
actual run, not inferred from this file or a pre-run receipt.

The historical same-base run `33981346520` remains evidence for main `3d6b8a6...`
and its recorded integration tree only. Its seven Explorer TypeScript diagnostics
and missing-sibling MapLibre app-only export failure remain failures. The phrase
"complete pnpm workspace build passes" in the earlier note means only the Sites
application's filtered build within that workspace, not a root-workspace build.
Neither the full Explorer production build nor the isolated npm export build is
added to this targeted passing gate. No new passing result for either is claimed.
The historical fflate finding is not dismissed or represented as a fresh audit.

## Review boundary, placement, and rollback

This is an author-side adversarial review and corrective test change, not
independent human approval. The contributor contract and #4024 delivery controls
still require an eligible independent draft-creation path. A continuation request,
closed issue metadata, or green CI is not that evidence. #4228 remains separate.
No merge, settings change, deployment, source admission, publication, or alert
closure follows from this change.

Accepted [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and the adopted [Directory Rules](../../../docs/doctrine/directory-rules.md)
place this app-local review/test under `apps/`, read-only orchestration under
`.github/`, and the [new authoring receipt](../../../data/receipts/generated/esbuild-policy-guard-review-20260905.json)
under the existing `data/receipts/generated/` lane. No new responsibility root,
schema, policy, source, or release authority is introduced.

To undo only this follow-up, revert its guard, workflow, note and receipt delta;
retain the dependency repair and current-main temporal changes. The broader
security rollback remains the paired-manifest/lock procedure in the remediation
record: preserve Babel 7.29.7 and do not re-enable vulnerable development serving.
