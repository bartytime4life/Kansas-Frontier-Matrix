<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/apps-explorer-web-layer-lineage-timeline
title: Explorer Layer Lineage Timeline
type: component-readme
version: v1.0.0
status: proposed; fixture-first; public-safe projection; non-authoritative
owners: OWNER_TBD - Explorer UI steward; release steward; provenance steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public
owning_root: apps/
responsibility: render a bounded chronological view of layer release, correction, withdrawal, and rollback lineage
related: [../../adapters/LayerLineageProjection.ts, ../../../../docs/architecture/publication/ROLLBACK.md, ../../../../docs/architecture/publication/rollback-and-correction.md]
[/KFM_META_BLOCK_V2] -->

# Explorer Layer Lineage Timeline

This fixture-first component implements the read-only surface proposed by Pass 32 card `KFM-P32-FEAT-0020`: previous artifact digests, correction receipts, rollback targets, and current release state for a promoted layer.

## Boundary

The timeline displays a bounded upstream projection. It does not resolve a release manifest, verify a receipt or digest, execute rollback/correction, mutate lifecycle state, evaluate policy, authenticate review, authorize release, deploy, or publish.

- Only exact `ANSWER / LINEAGE_AVAILABLE` payloads may carry lineage.
- The first entry must be `RELEASED`; later entries must be contiguous and strictly chronological.
- Corrections require a unique correction receipt and the preceding artifact digest.
- Rollbacks require an earlier release target whose artifact digest equals the restored digest.
- Withdrawals preserve the preceding digest and require a correction receipt or earlier rollback target.
- The final entry must close over the top-level current release and state.
- Negative outcomes carry no layer, release, receipt, rollback, digest, timestamp, or free-form diagnostic detail.

The DOM contains no buttons or mutation callbacks. Its lifecycle vocabulary is descriptive only and grants no release-plane authority.

## Directory Rules basis

UI code remains under `apps/explorer-web/`; synthetic public-safe inputs remain under `fixtures/ui/`; source reconciliation remains under `docs/intake/exploratory/`; authoring accountability remains under `data/receipts/generated/`. Existing rollback/release doctrine is referenced rather than copied or amended.

## Validation

```bash
pnpm --filter explorer-web run test:unit
pnpm --filter explorer-web run build
```

The hosted UI workflow installs a browser and exercises the companion Playwright fixture.

## Rollback

Revert this additive component packet. It mutates no data, lifecycle, evidence, policy, review, release, deployment, or publication state.
