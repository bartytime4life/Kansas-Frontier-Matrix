# Governed Evidence Tooltip

**Status:** PROPOSED implementation on a review branch  
**Owner root:** `apps/`  
**Public-release effect:** none

## Goal

Provide a small hover/focus trust snapshot that is subordinate to the existing Evidence Drawer and fails closed for every non-supported state.

The source packet proposes a three-part UI pattern: a quick Evidence Tooltip, a full Receipt Drawer, and a Policy Badge. This slice adopts the quick-tooltip behavior but binds it to the repository's existing strict `GovernedEvidenceDrawerProjection` rather than introducing a parallel map-feature metadata contract.

## Trust boundary

The module:

- accepts only the existing governed browser projection parsed by `GovernedClient.ts`;
- renders a tooltip only for `ANSWER / SUPPORTED` with `ALLOW`, `REVIEWED`, `RELEASED`, and `CURRENT` trust state;
- requires at least one evidence reference and one validated citation;
- withdraws the tooltip for malformed, abstained, denied, errored, stale, unreleased, pending-review, or superseded states;
- uses DOM `textContent` and does not interpolate HTML;
- performs no network requests and reads no RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED storage directly;
- delegates the detailed view to the existing Evidence Drawer callback rather than opening a receipt URL from the tooltip.

The tooltip is not evidence authority, policy authority, release authority, or a replacement for the Evidence Drawer.

## Why the packet was adapted

The packet's illustrative GeoJSON shape includes fields such as `source_label`, `spec_hash`, and `run_receipt_url`. The current repository already has a stricter, fixture-only governed projection and a tested Evidence Drawer. This implementation therefore reuses current repository truth and does not invent or duplicate those fields. A later map adapter can invoke this module after it has obtained a governed projection through an approved interface.

## Files

- `index.ts` - finite resolver and DOM controller.
- `../../../tests/evidence-tooltip.test.ts` - no-network, no-leak unit tests.
- `../../../tests/browser/evidence-tooltip.*` - keyboard, pointer, drawer-delegation, and negative-state browser tests.

## Directory Rules basis

`apps/explorer-web/src/features/` owns browser feature behavior in the canonical Explorer application. App-local tests remain under `apps/explorer-web/tests/`. The generated provenance receipt is stored under the established `data/receipts/generated/` receipt family. No root, authority family, schema, contract, policy, or lifecycle path is created or moved.

## Validation

```bash
cd apps/explorer-web
npm run build
npm run test:unit
npm run test:e2e
```

The repository's existing `ui-build` workflow owns hosted execution of those commands. Unit and browser tests use synthetic fixtures only and require no live source or model runtime.

## Rollback

Revert the feature commit. The module is additive and is not wired into a public map route by this slice, so rollback does not require data migration, cache invalidation, release withdrawal, or publication correction.
