<!-- [KFM_META_BLOCK_V2]
doc_id: kfm.docs.runbooks.index.v1
title: Runbooks
type: standard
version: v1
status: active
owners: kfm-maintainers
created: 2026-04-28
updated: 2026-04-28
policy_label: evidence_first
related:
  - docs/README.md
  - docs/runbooks/repository-next-steps.md
  - docs/runbooks/foundation-strategy.md
  - docs/runbooks/markdown-remediation-plan.md
  - docs/runbooks/markdown-debt-backlog.md
  - docs/runbooks/publication.md
  - docs/runbooks/correction.md
  - docs/runbooks/stale_projection.md
  - docs/runbooks/rollback.md
  - docs/runbooks/reliability/trigger-retry-matrix.md
[/KFM_META_BLOCK_V2] -->

# Runbooks

Operator playbooks for trust-critical operational actions in Kansas Frontier Matrix.

## Directory map

- [`../adr/README.md`](../adr/README.md): architecture decisions and authority boundaries that runbooks must obey.
- [`../registers/README.md`](../registers/README.md): control-plane registers for drift, authority, and verification gaps.
- [`publication.md`](./publication.md): promote and publish safely.
- [`correction.md`](./correction.md): correct published errors with lineage.
- [`stale_projection.md`](./stale_projection.md): handle stale derived/public projections.
- [`rollback.md`](./rollback.md): restore last known-good state.
- [`reliability/trigger-retry-matrix.md`](./reliability/trigger-retry-matrix.md): retry posture by trigger class.
- [`repository-next-steps.md`](./repository-next-steps.md): near-term execution sequence.
- [`foundation-strategy.md`](./foundation-strategy.md): strategic sequencing guidance.
- [`markdown-remediation-plan.md`](./markdown-remediation-plan.md): docs cleanup process.
- [`markdown-debt-backlog.md`](./markdown-debt-backlog.md): debt tracking and triage backlog.

## Operating expectations

1. Prefer evidence-first and fail-closed behavior.
2. Keep every runbook reversible and validation-backed.
3. Preserve auditability: correction/supersession history must remain visible.
4. Do not treat projections, summaries, or generated text as canonical truth.

## Minimum runbook shape

Each runbook in this directory should include:

- trigger conditions
- preconditions or assumptions
- ordered execution steps
- explicit validation checks
- failure/rollback or escalation path
- named output artifacts/logs
