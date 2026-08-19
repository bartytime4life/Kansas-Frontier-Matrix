# Explorer composition shell

This directory contains the repository-grounded composition layer for the KFM Explorer site.

## Scope

The composition:

- replaces the minimal default page with a map-first, trust-visible landing shell;
- inventories the current Explorer feature families and their conservative maturity state;
- exposes the thirteen domain families already represented under `src/features/domains/`;
- presents KFM's evidence, finite-outcome, time, correction, accessibility, and trust-membrane principles;
- mounts the existing renderer-neutral `map_runtime` selection-to-Evidence-Drawer bridge with deterministic synthetic cases; and
- records the current MapLibre package, candidate, and HOLD posture without importing or admitting `maplibre-gl`.

## Evidence snapshot

The catalog is pinned to:

- repository: `bartytime4life/Kansas-Frontier-Matrix`
- ref: `main`
- commit: `67cf9bcd8d4044beb2f7ec4ec17e1bf162ca30aa`
- Explorer path: `apps/explorer-web/`
- MapLibre package home: `packages/maplibre/`
- MapLibre readiness candidate: `6.4.0`
- concrete runtime/dependency posture: `HOLD / not admitted / not implemented`

Refresh `catalog.ts` when repository authority, feature inventory, or maturity changes. Do not silently convert a repository snapshot into runtime authority.

## Trust boundary

This composition does not:

- read `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, candidate, canonical, graph, vector, object, or private lifecycle stores;
- activate or ingest a live source;
- call a model provider or local model runtime;
- perform policy, review, release, correction, rollback, or publication transitions;
- infer evidence from rendered features, pixels, route state, or generated text;
- import `maplibre-gl` or create a second renderer acquisition seam; or
- claim that fixture-first feature slices are live production routes.

The concrete renderer remains a separate governed implementation and dependency-admission change after ADR and acquisition enforcement close.

## Validation

Run from `apps/explorer-web/` with the repository's locked toolchain:

```bash
pnpm run build
pnpm run test:unit
pnpm run test:browser
```

The added catalog test checks identifier/path uniqueness, the thirteen-domain inventory, sensitive-domain safeguards, filtering, and preservation of the MapLibre HOLD.
