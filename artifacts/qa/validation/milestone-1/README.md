# Milestone 1 validation inspection output

This compatibility QA-output directory holds the deterministic MRTS-06
`CIConformanceReport` inspection copy and a bounded machine-readable
reconciliation projection for the Machine-Readable Trust Spine milestone. The
canonical semantic contract is
[`contracts/governance/ci_conformance_report.md`](../../../../contracts/governance/ci_conformance_report.md),
and the operational review/closure procedure is
[`docs/runbooks/mrts-06-ci-conformance-handoff.md`](../../../../docs/runbooks/mrts-06-ci-conformance-handoff.md).

## Tracked inspection artifacts

- [2026-10-08 successor report](./ci_conformance_report_2026-10-08.json)
  records bounded local checks at `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`:
  topology `PASS`, governance parity `HOLD_INHERITED`, and four remaining
  closure blockers. Its [execution evidence](./ci_conformance_evidence_2026-10-08.json)
  binds commands, times, actual execution head/tree, prerequisite state and
  exact-main hosted observations. [Review and rollback handoff](../../../../docs/runbooks/mrts-06-conformance-refresh-2026-10-08.md).
- [`ci_conformance_report.json`](./ci_conformance_report.json) is the
  immutable historical MRTS-06 inspection report for `main@c653d573…`, observed
  August 22. Its `BLOCKED` result and older topology counts remain historical.
- [`mrts_reconciliation_status_2026-08-23.json`](./mrts_reconciliation_status_2026-08-23.json)
  is the current-main machine-readable QA projection paired with the runbook.
- [`data/receipts/generated/genrec-mrts-milestone-reconciliation-b03c5963b80e.json`](../../../../data/receipts/generated/genrec-mrts-milestone-reconciliation-b03c5963b80e.json)
  records AI-authoring provenance and exact artifact hashes for the
  reconciliation update.

These files are inspection and process-evidence surfaces only. They are not
canonical receipts, proofs, policy decisions, review approvals, lifecycle
records, release records, issue-close actions, milestone-close actions, or
publication authority. The reconciliation projection does not modify or
supersede the canonical report until its repository-owned generator, validator,
receipt, hosted-evidence, and human-review requirements are satisfied.
