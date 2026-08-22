<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://runbook/governance/mrts-06-ci-conformance-handoff
title: MRTS-06 CI Conformance and Closure Handoff
version: v1.0.0
type: runbook
status: proposed; blocked-handoff; non-release
owners: Validation/CI steward; Repository owner; Release steward
created: 2026-08-22
updated: 2026-08-22
responsibility_root: docs/
owning_root: docs/
responsibility: explain ownership inputs outputs validation correction rollback and closure limits for the MRTS-06 CI conformance report
policy_label: internal-governance; no-self-authority; no-network-validation
truth_posture: CONFIRMED current repository paths and bounded local observations / PROPOSED MRTS-06 implementation packet / UNKNOWN hosted exact-final-head results human approval branch protection and final closure / NEEDS VERIFICATION every false exit criterion
related:
  - ../../contracts/governance/ci_conformance_report.md
  - ../../schemas/contracts/v1/governance/ci_conformance_report.schema.json
  - ../../artifacts/qa/validation/milestone-1/ci_conformance_report.json
  - ../../tools/validators/governance/validate_ci_conformance_report.py
  - ../../data/receipts/generated/genrec-ci-conformance-report-mrts-06-20260822.json
[/KFM_META_BLOCK_V2] -->

# MRTS-06 CI conformance and closure handoff

## Current handoff

The initial report is a deterministic `BLOCKED` candidate. It records merged
MRTS-01 through MRTS-05 evidence, local focused checks, and inherited
repository-topology holds. It does not claim an exact
final SHA, hosted exact-head success, human approval, or milestone closure.

## Ownership

| Responsibility | Owner or route |
| --- | --- |
| Contract meaning and schema evolution | Contract and schema stewards |
| Validator, fixtures, workflow, and report generation | Validation/CI steward |
| Accepted repository authority and merge review | Repository owner through CODEOWNERS |
| Release, rollback, or correction decision | Governed release steward and required reviewers |
| Final issue/milestone state | Independently authorized GitHub closer |

No row delegates its authority to the report, workflow, validator, receipt, or
AI author.

## Inputs

- exact merged base commit;
- adopted Directory Rules and accepted ADR-0029 bytes;
- root, object-family, and validator registry versions and digests;
- CIConformanceReport and trust-spine-fixture schema versions and digests;
- policy-root and decision-vocabulary versions and digests;
- validator source digests;
- MRTS-05 fixture digest and review state;
- exact local or hosted command execution states and outcomes;
- inherited and introduced failure counts;
- generated artifact paths and digests;
- blocking unresolved items;
- exact final-head hosted run URLs and human review only after they exist.

## Outputs

- non-authoritative QA report:
  `artifacts/qa/validation/milestone-1/ci_conformance_report.json`;
- bounded generated authoring receipt under `data/receipts/generated/`;
- focused workflow summary that repeats the non-authority boundary;
- a future closure candidate only after every exit criterion has exact
  evidence.

## Validation

Run the complete bounded profile:

```bash
make ci-conformance-report
```

For focused inspection:

```bash
python tools/validators/governance/validate_ci_conformance_report.py
python tools/validators/governance/validate_ci_conformance_report.py --fixtures
python tools/validators/governance/validate_ci_conformance_report.py --render > /tmp/kfm-ci-conformance-report.json
```

The first two commands must pass. The rendered bytes must match the committed
report. Separately inspect the repository-governance parity and topology
diagnostics; do not hide an inherited hold behind this validator's integrity
pass.

## Final-head closure procedure

1. Wait until every prerequisite change is reviewed and merged.
2. Refresh from `main` and record its exact 40-character SHA as both
   `repository.final_sha` and `closure.target_sha`.
3. Recompute all base/candidate references against the intended final tree.
4. Fetch hosted workflow results for that exact SHA. Add direct run URLs only
   when conclusions are final and successful.
5. Record authenticated human review identity and time only from the review
   system of record.
6. Re-run required local checks and preserve failures or inherited holds.
7. Clear an unresolved item only when its cited evidence exists.
8. Change closure to `READY` only when every exit criterion is true, required
   checks are `PASS`, and unresolved count is zero.
9. A separately authorized closer may record `CLOSED`, closer, time, and closed
   milestone state after the actual GitHub action. Validation does not perform
   that action.

If any check was not run, keep `CHECK_NOT_RUN`. If a non-goal was deliberately
excluded, keep `SKIPPED`. Neither state is a pass.

## Correction

Forward-fix the current same-path report and recompute its digest. If a path or
version changed, update both the reference and its digest. Preserve prior
reviewed receipts and reports; add correction linkage rather than rewriting
history. Never fabricate a hosted URL, reviewer, closer, time, or final SHA.

## Rollback

Revert the MRTS-06 integration as one unit when its contract or placement is
wrong. This includes the contract, schema, report, fixtures, validator, tests,
workflow, Make target, registry entry, runbook, and generated receipt. The
rollback removes inspection tooling only; it must not delete prerequisite
evidence or alter release/runtime state.

## Known limits

- Local Git and filesystem validation cannot prove hosted workflow execution,
  branch-protection configuration, or reviewer identity.
- Workflow source presence is not evidence that a workflow ran or was required.
- A fixture dry run is not live source, production, release, or publication
  evidence.
- `artifacts/qa/` is a compatibility inspection lane, not a proof, receipt,
  policy, lifecycle, or release authority root.
- The initial candidate carries inherited topology debt and still lacks its
  own merge, exact-final-head hosted evidence, human review, and issue closure;
  milestone closure therefore remains blocked.
