<!-- [KFM_META_BLOCK_V2]
doc_id: kfm.runbook.stale_projection.v1
title: Stale Projection Runbook
type: runbook
version: v1
status: active
owners: kfm-maintainers
created: 2026-04-28
updated: 2026-04-28
policy_label: freshness_required
related:
  - docs/runbooks/README.md
  - docs/runbooks/publication.md
  - docs/runbooks/reliability/trigger-retry-matrix.md
[/KFM_META_BLOCK_V2] -->

# Stale Projection Runbook

Use this runbook when derived/public projections lag canonical promoted truth.

## Trigger signals

- Freshness SLA breach for derived cache/index/projection.
- Canonical and projected checksums or record counts diverge.
- User-facing stale markers or complaints.

## Procedure

1. Confirm divergence with reproducible query/check.
2. Classify scope (single tenant, dataset, region, or global).
3. Mark affected surface as stale-visible.
4. Rebuild or re-sync the projection from the canonical source.
5. Verify parity after rebuild.
6. Remove stale-visible marker and publish incident summary.

## Validation checklist

- [ ] Freshness timestamp updated.
- [ ] Parity check passes for key sample records.
- [ ] Any stale warning cleared.
- [ ] Event logged in ops history.
