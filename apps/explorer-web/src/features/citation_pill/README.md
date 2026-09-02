# Governed Inline Citation Pill

**Status:** PROPOSED implementation on a review branch  
**Owner root:** `apps/`  
**Public-release effect:** none

## Goal

Adapt the **Collapsed Citation Pill → Inline EvidenceRef** micro-pattern from `New Ideas 3-4-26.pdf` into a small Explorer feature that keeps narrative and map-adjacent text readable while making one governed evidence reference available with one click.

The source packet proposes a compact evidence/status pill, inline expansion, a timestamped KFM evidence deep link, keyboard operation, `aria-expanded`, and deterministic copy feedback. This implementation preserves those interaction goals while refusing to invent a new evidence status, route, schema, or policy decision.

## Why the source pattern was narrowed

The packet names `VERIFIED`, `PROPOSED`, and `UNKNOWN` citation states. The current Explorer governed evidence projection has authoritative fields for supported, reviewed, released, current evidence, but it does not define a canonical three-state citation-pill vocabulary. This slice therefore emits only `VERIFIED` when every current trust gate passes. All other states expose no pill.

Likewise, the packet's `kfm://evidence/...?...` form is implemented as a copy-only app-local formatting convention. It is not declared a canonical URI schema and is not wired to a route. A later governed route adapter must validate and interpret it before navigation is introduced.

## Trust boundary

The pill renders only when the existing `parseEvidenceDrawerProjection` boundary yields:

- `ANSWER / SUPPORTED`;
- at least one evidence reference and one citation;
- policy `ALLOW`;
- review `REVIEWED`;
- release `RELEASED`;
- freshness `CURRENT`;
- correction state other than `SUPERSEDED`;
- one unambiguous, syntactically bounded KFM evidence reference; and
- an explicitly supplied UTC timestamp at whole-second precision.

Missing, malformed, ambiguous, abstained, denied, errored, stale, unreleased, unreviewed, policy-blocked, superseded, unbound, or invalid-timestamp state exposes no toggle, inline region, evidence reference, or copied link.

The module:

- performs no network request;
- performs no navigation;
- reads no browser persistence;
- reads no RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED store;
- makes no evidence, policy, review, freshness, correction, or release decision;
- uses DOM text nodes rather than HTML interpolation; and
- delegates evidence authority to the existing governed projection.

## Interaction contract

- The collapsed button displays `Evidence` (or a bounded caller label) plus a shape-and-text `■ VERIFIED` chip.
- The button binds `aria-expanded` to a labeled inline region.
- One click reveals the title, `EvidenceRef`, and proposed deep link.
- The copy button uses an injected copy boundary, the Clipboard API when available, or a hidden-textarea fallback.
- Copy success is announced as `Link copied.` through a polite live region.
- Escape collapses the region and restores focus to the toggle.
- Multiple evidence references require an explicit caller selection that must be present in the governed payload; silent first-item selection is denied.

## Files

- `index.ts` — strict resolver, deep-link formatter, and DOM controller.
- `../../../tests/citation-pill.test.ts` — trust-gate, ambiguity, deep-link, no-leak, and no-network unit tests.
- `../../../tests/browser/citation-pill.*` — keyboard, expansion, copy, Escape, and negative-state browser tests.

Existing synthetic Evidence Drawer fixtures are reused. No duplicate evidence fixture family is introduced.

## Directory Rules basis

`apps/explorer-web/src/features/` owns app-local Explorer feature behavior. App-local unit and browser tests remain under `apps/explorer-web/tests/`. AI-authoring provenance remains in the established `data/receipts/generated/` family. No root, lifecycle phase, contract home, schema home, policy home, source registry, release home, proof home, or compatibility authority is created or moved.

## Validation

```bash
cd apps/explorer-web
pnpm run build
pnpm run test:unit
pnpm run test:browser
```

The existing `ui-build`, accessibility, CodeQL, policy, release-dry-run, rollback-drill, and broader repository workflows own hosted validation. The feature and tests are deterministic and use synthetic fixtures only.

## Rollback

Revert the feature commit. This slice is additive and is not wired into a public route, so rollback requires no data migration, cache invalidation, source correction, release withdrawal, or publication correction.
