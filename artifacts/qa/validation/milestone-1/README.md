# Milestone 1 validation inspection output

This compatibility QA-output directory holds the deterministic MRTS-06
`CIConformanceReport` inspection copy and bounded review/reconciliation
projections for the Machine-Readable Trust Spine milestone. The canonical
semantic contract is
[`contracts/governance/ci_conformance_report.md`](../../../../contracts/governance/ci_conformance_report.md),
and the handoff procedure is
[`docs/runbooks/mrts-06-ci-conformance-handoff.md`](../../../../docs/runbooks/mrts-06-ci-conformance-handoff.md).

## Tracked inspection artifacts

- [`ci_conformance_report.json`](./ci_conformance_report.json) is the
  deterministic, generated-style MRTS-06 inspection report. Its current record
  remains deliberately `BLOCKED`.
- [`mrts_milestone_reconciliation_2026-08-23.md`](./mrts_milestone_reconciliation_2026-08-23.md)
  is a human-readable current-main reconciliation and review handoff.
- [`mrts_reconciliation_status_2026-08-23.json`](./mrts_reconciliation_status_2026-08-23.json)
  is the machine-readable QA projection paired with that handoff.
- [`data/receipts/generated/genrec-mrts-milestone-reconciliation-b03c5963b80e.json`](../../../../data/receipts/generated/genrec-mrts-milestone-reconciliation-b03c5963b80e.json) records AI-authoring provenance
  and exact artifact hashes for this review packet.

These files are inspection and process-evidence surfaces only. They are not
canonical receipts, proofs, policy decisions, review approvals, lifecycle
records, release records, issue-close actions, milestone-close actions, or
publication authority. A current reconciliation artifact does not modify or
supersede the canonical report until the repository-owned generator, validator,
receipt, hosted evidence, and human-review requirements are satisfied.
