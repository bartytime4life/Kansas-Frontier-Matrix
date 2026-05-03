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
- [`validation-entrypoints.md`](./validation-entrypoints.md): quick validation command/index reference.

## Operating expectations

1. Prefer evidence-first and fail-closed behavior.
2. Keep every runbook reversible and validation-backed.
3. Preserve auditability: correction/supersession history must remain visible.
4. Do not treat projections, summaries, or generated text as canonical truth.

## Validation entrypoints (confirmed paths)

- Python test discovery: [`../../pytest.ini`](../../pytest.ini)
- Pytest suites: [`../../tests/`](../../tests/)
- Web app tests (vitest script): [`../../apps/web/package.json`](../../apps/web/package.json)
- Governance/policy tests: [`../../tests/policy/`](../../tests/policy/) and [`../../policy/tests/`](../../policy/tests/)
- Consolidated validation quick reference: [`validation-entrypoints.md`](./validation-entrypoints.md)

## Minimum runbook shape

Each runbook in this directory should include:

- trigger conditions
- preconditions or assumptions
- ordered execution steps
- explicit validation checks
- failure/rollback or escalation path
- named output artifacts/logs

## Reorg note
Use `docs/registers/reorg/rollback_plan.sh` for sprint rollback commands.

## Reorg runbook note
- Use `docs/registers/reorg/rollback_plan.sh` for targeted documentation move rollback.

## Reorg sprint linkage

See `docs/registers/reorg/REORG_SPRINT_MANIFEST.md` for current repository organization controls and rollback plan.


## Reorg operations
- Use `docs/registers/reorg/rollback_plan.sh` for targeted path rollback during documentation-lane reorganizations.
- Treat promotion and lifecycle transitions as governed events, never as plain file movement.

## Reorg linkage
- Reorg and authority maps: `docs/registers/reorg/` and `docs/registers/*authority_map.md`.

## Reorg runbook references
See `docs/registers/reorg/rollback_plan.sh` for repository-organization rollback commands.

## Reorg sprint runbook linkage
See `docs/registers/reorg/REORG_SPRINT_MANIFEST.md` and `docs/registers/reorg/rollback_plan.sh`.

## Domain Runbook Consolidation (2026-05-03)
- Atmosphere air runbook slices moved to `docs/runbooks/domains/atmosphere_air/slices/`.

## Reorg control-plane linkage
- Reorg rollback: use `docs/registers/reorg/rollback_plan.sh` before broader lane-by-lane move execution.


## REORG sprint (2026-05-03)
- See `docs/registers/reorg/REORG_SPRINT_MANIFEST.md` for manifest, move plan, reference plan, validation report, and rollback plan.
