<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/apps-explorer-web-redaction-preview
title: Explorer Redaction Preview
type: component-readme
version: v1.0.0
status: proposed; fixture-first; public-safe projection; non-authoritative
owners: OWNER_TBD - Explorer UI steward; sensitivity steward; redaction steward; release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public
owning_root: apps/
responsibility: render a read-only pre-release summary of declared public-safe redaction transforms from a governed projection
truth_posture: CONFIRMED fixture-first finite projection and no-leak tests / PROPOSED app-local reviewer surface / UNKNOWN production composition, governed-service integration, and runtime proof
related: [../../adapters/RedactionPreviewProjection.ts, ../../../../contracts/shared/redaction_receipt.md, ../../../../docs/standards/REDACTION_DETERMINISM.md, ../../../../policy/redaction/profiles.yaml]
[/KFM_META_BLOCK_V2] -->

# Explorer Redaction Preview

This fixture-first component implements the bounded reviewer surface proposed by Pass 32 card `KFM-P32-FEAT-0012`. It summarizes four public-safe properties declared by an upstream governed projection: geometry generalization, low-count suppression, maximum public zoom, and abstraction class.

## Boundary

The preview is a read-only release-review aid. It is not redaction policy, a transform executor, a sufficiency determination, review approval, release approval, publication authority, or canonical source truth.

- `RedactionPreviewProjection.ts` accepts an exact app-local projection and rejects unknown fields.
- Only `ANSWER / PREVIEW_READY` carries digest-bound candidate, policy-decision, and redaction-receipt references plus finite transform summaries.
- `ABSTAIN`, `DENY`, and `ERROR` carry no references or preview detail and render fixed copy.
- Raw or generalized geometry payloads, coordinates, counts, min-n thresholds, hidden values, reversal parameters, free-form diagnostics, and credentials are outside the projection grammar.
- The browser performs no network access, policy evaluation, lifecycle-store reads, transform execution, persistence, review decision, release, or publication.
- Receipt inspection delegates the already-parsed projection to a caller-supplied callback; the component cannot approve or release anything.

## Directory Rules basis

The UI adapter and component live under `apps/explorer-web/`; public-safe synthetic payloads live under `fixtures/ui/`; tests live beside the Explorer test harness; exploratory source reconciliation lives under `docs/intake/exploratory/`; authoring accountability lives under `data/receipts/generated/`. Existing redaction meaning, schema, policy, receipt, and release authorities remain in their current roots and are not copied here.

## Validation

```bash
pnpm --filter explorer-web run test:unit
pnpm --filter explorer-web run build
```

The hosted UI workflow installs a browser and exercises the companion Playwright fixture. Local browser execution may be skipped when Chromium is unavailable.

## Rollback

Revert this additive component packet. No source, restricted geometry, count, policy, receipt, review, release, deployment, publication, or public artifact requires restoration.
