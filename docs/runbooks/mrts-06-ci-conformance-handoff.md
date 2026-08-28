<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://runbook/governance/mrts-06-ci-conformance-handoff
title: MRTS-06 CI Conformance and Closure Handoff
version: v1.1.0
type: runbook
status: proposed; current-main-reconciled; blocked-handoff; non-release
owners: Validation/CI steward; Repository owner; Release steward
created: 2026-08-22
updated: 2026-08-23
responsibility_root: docs/
owning_root: docs/
responsibility: explain ownership inputs outputs validation correction rollback issue reconciliation and closure limits for the MRTS-06 CI conformance report
policy_label: internal-governance; no-self-authority; no-network-validation
truth_posture: CONFIRMED current repository paths merged implementation lineage and exact repository snapshot 8d852fb1a97478cd68631f1dfa4643515aa62e3b / PROPOSED review and closure sequence / UNKNOWN hosted exact-target results human approval branch protection deployment release and public behavior / NEEDS VERIFICATION exact-current-main topology governance parity and every false exit criterion
related:
  - ../../contracts/governance/ci_conformance_report.md
  - ../../schemas/contracts/v1/governance/ci_conformance_report.schema.json
  - ../../artifacts/qa/validation/milestone-1/ci_conformance_report.json
  - ../../artifacts/qa/validation/milestone-1/mrts_reconciliation_status_2026-08-23.json
  - ../../tools/validators/governance/validate_ci_conformance_report.py
  - ../../tools/validators/validate_generated_receipt.py
  - ../../data/receipts/generated/genrec-ci-conformance-report-mrts-06-20260822.json
  - ../../data/receipts/generated/genrec-mrts-milestone-reconciliation-b03c5963b80e.json
notes:
  - The canonical CIConformanceReport remains regenerate-only and is not hand-edited by this reconciliation.
  - A pull request, merge, report, receipt, green check, or this runbook cannot approve review or close an issue or milestone.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MRTS-06 CI conformance and closure handoff

## Current handoff

The canonical report is a deterministic `BLOCKED` checkpoint bound to
`c653d573c1641503215844c5c4fc85bc15060ced`. It records merged MRTS-01
through MRTS-06 evidence, local focused checks, an older inherited
repository-topology checkpoint, hosted `CHECK_NOT_RUN`, and human review
`PENDING`.

Current repository inspection is pinned separately to
`main@8d852fb1a97478cd68631f1dfa4643515aa62e3b`. That newer repository
snapshot does not make the older report current and does not supply an
unexecuted exact-main topology or hosted result.

> [!IMPORTANT]
> The canonical report has `edit_policy=regenerate_only`. Refresh it only
> through the repository-owned generator and validator after an exact target,
> exact execution evidence, and review evidence exist.

## Current MRTS reconciliation

| Issue | Merged implementation posture | Current handoff |
|---|---|---|
| [#3359 — MRTS-02](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3359) | Registry normalization and append-only receipt follow-up are merged | `READY_FOR_HUMAN_REVIEW`; six intentionally `ABSENT` registries, unsupported owners `UNKNOWN`, and the document-authority conflict remain explicit |
| [#3360 — MRTS-03](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3360) | Object-family catalog implementation is merged | `READY_FOR_HUMAN_REVIEW`; `CONFLICTED`, `PARTIAL`, `ABSENT`, and `NOT_INSPECTED` remain valid classifications |
| [#3361 — MRTS-04](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3361) | Ratchet/parity implementation and IIIF authority migration are merged | `REVIEW_PENDING / HOLD_INHERITED`; exact-current-main topology still needs execution |
| [#3363 — MRTS-05](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3363) | Deterministic no-network cross-family fixture slice is merged | `READY_FOR_HUMAN_REVIEW`; fixture success grants no source, lifecycle, release, or publication authority |
| [#3364 — MRTS-06](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3364) | Contract, schema, validator, fixtures, tests, workflow, report, receipt, and handoff are merged | `IMPLEMENTED / STALE HANDOFF / BLOCKED`; select exact checkpoint and regenerate only after required evidence exists |

PR #3429 established the latest verified candidate topology checkpoint:
`0 new / 132 baselined / 0 stale`, zero introduced findings, and governance
parity `HOLD_INHERITED`. Current `main` later advanced, so those numbers are
lineage evidence, not an exact-current-main execution result.

The paired machine-readable review projection is
[`mrts_reconciliation_status_2026-08-23.json`](../../artifacts/qa/validation/milestone-1/mrts_reconciliation_status_2026-08-23.json).
It is process evidence only and does not replace the canonical report.

## Ownership

| Responsibility | Owner or route |
| --- | --- |
| Contract meaning and schema evolution | Contract and schema stewards |
| Validator, fixtures, workflow, and report generation | Validation/CI steward |
| Accepted repository authority and merge review | Repository owner through CODEOWNERS |
| Independent semantic/governance review | Accountable reviewer recorded by the review system |
| Release, rollback, or correction decision | Governed release steward and required reviewers |
| Final issue/milestone state | Independently authorized GitHub closer |

No row delegates its authority to the report, workflow, validator, receipt, pull
request, or AI author.

## Inputs

- exact merged base or selected final checkpoint;
- adopted Directory Rules and accepted ADR-0029 bytes;
- root, object-family, and validator registry versions and digests;
- CIConformanceReport and trust-spine-fixture schema versions and digests;
- policy-root and decision-vocabulary versions and digests;
- validator source digests;
- MRTS-05 fixture digest and review state;
- exact local or hosted command execution states and outcomes;
- inherited and introduced failure counts;
- generated artifact paths and digests;
- exact ancestor commits for replaying historical authoring receipts after
  shared successor files advance;
- blocking unresolved items;
- exact final-head hosted run URLs and human review only after they exist.

## Outputs

- canonical non-authoritative QA report:
  `artifacts/qa/validation/milestone-1/ci_conformance_report.json`;
- bounded generated authoring receipts under `data/receipts/generated/`;
- focused workflow summary that repeats the non-authority boundary;
- current review projections that remain subordinate to the canonical report;
- a future closure candidate only after every exit criterion has exact evidence.

## Validation

Run the complete bounded profile from a clean checkout pinned to the intended
target:

```bash
make repository-topology
make repository-governance-parity
make ci-conformance-report
```

For focused inspection:

```bash
python tools/validators/governance/validate_ci_conformance_report.py
python tools/validators/governance/validate_ci_conformance_report.py --fixtures
python tools/validators/governance/validate_ci_conformance_report.py --render > /tmp/kfm-ci-conformance-report.json
diff -u artifacts/qa/validation/milestone-1/ci_conformance_report.json /tmp/kfm-ci-conformance-report.json

make control-plane-registry-packet
make trust-spine-fixture-slice
make validator-registry-check
make workflow-security
```

The focused validator and fixture polarity must pass. The rendered bytes must
match the committed report. Separately preserve topology and governance-parity
outcomes; do not hide an inherited hold behind report-integrity success.

Historical receipts that bind mutable shared paths are replayed without changing
their stored hashes:

```bash
python tools/validators/validate_generated_receipt.py <receipt.json> \
  --repo-root . --artifact-git-ref <exact-40-character-ancestor-commit>
```

The pinned commit must exist, be an ancestor of the tested head, and contain
every declared artifact as a regular blob with the receipt's exact digest.

## Final-head closure procedure

1. Wait until every prerequisite change is reviewed and merged.
2. Select one exact final checkpoint and record its 40-character SHA as both
   `repository.final_sha` and `closure.target_sha`.
3. Recompute every base/candidate reference against that intended final tree.
4. Execute every closure-required local check at that exact checkpoint.
5. Fetch hosted workflow results for that exact SHA and add direct successful
   run URLs only after conclusions settle.
6. Record authenticated human review identity and time only from the review
   system of record.
7. Resolve inherited topology debt or record an explicit authorized governance
   decision changing its closure treatment. Regeneration alone cannot waive it.
8. Clear an unresolved item only when its cited evidence exists.
9. Change closure to `READY` only when every exit criterion is true, every
   closure-required check is `PASS`, and unresolved count is zero.
10. A separately authorized closer may record `CLOSED`, closer, time, and closed
    milestone state after the actual GitHub action.

If any check was not run, keep `CHECK_NOT_RUN`. If a non-goal was deliberately
excluded, keep `SKIPPED`. If inherited debt blocks conformance, keep
`HOLD_INHERITED`. None is a pass.

## Correction

Forward-fix the current same-path report and recompute its digest. If a path or
version changed, update both the reference and its digest. Preserve prior
reviewed receipts and reports; add correction lineage rather than rewriting
history. Never fabricate a hosted URL, reviewer, closer, time, final SHA, or
execution result.

## Rollback

Revert the MRTS-06 integration as one unit when its contract or placement is
wrong. This includes the contract, schema, report, fixtures, validator, tests,
workflow, Make target, registry entry, runbook, and generated receipt. A
documentation-only reconciliation may instead be reverted or forward-corrected
with its paired QA projection and authoring receipt. Neither rollback changes
release/runtime/public state unless those separate systems were independently
mutated.

## Known limits

- Connector and file inspection cannot prove exact-current-main command
  execution, branch-protection configuration, or reviewer identity.
- Exact-ancestor receipt replay proves historical bytes and receipt integrity;
  it does not claim those historical bytes are the current implementation.
- Workflow source presence is not evidence that a workflow ran or was required.
- A fixture dry run is not live source, production, release, or publication
  evidence.
- `artifacts/qa/` is a compatibility inspection lane, not a proof, receipt,
  policy, lifecycle, or release authority root.
- The merged implementation still lacks the exact selected checkpoint's full
  hosted evidence, approved human review, zero blockers, and authorized issue
  closure; milestone closure therefore remains blocked.

[Back to top](#top)
