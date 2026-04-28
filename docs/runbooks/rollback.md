<!-- [KFM_META_BLOCK_V2]
doc_id: kfm.runbook.rollback.v1
title: Rollback Runbook
type: runbook
version: v1
status: active
owners: kfm-maintainers
created: 2026-04-28
updated: 2026-04-28
policy_label: rollback_first
related:
  - docs/runbooks/README.md
  - docs/runbooks/publication.md
  - docs/runbooks/correction.md
[/KFM_META_BLOCK_V2] -->

# Rollback Runbook

Use this runbook to return to the last known-good release when a new promotion is unsafe.

## Trigger

- Post-release checks fail with material impact.
- Runtime reliability falls below service thresholds.
- Policy or contract breakage is detected in production.

## Procedure

1. Declare rollback and assign incident lead.
2. Identify last known-good version (tag/commit/artifact).
3. Pause ongoing promotions.
4. Execute rollback deployment.
5. Run smoke checks and critical-path tests.
6. Announce rollback completion and residual impact.

## Validation checklist

- [ ] Target version identifier is recorded.
- [ ] Restored version passes health checks.
- [ ] Error rate/latency return to baseline bounds.
- [ ] Follow-up correction ticket is opened.

## Exit criteria

- Service is stable on known-good version.
- Root-cause work is tracked before re-attempting promotion.
