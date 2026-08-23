# Explorer composition shell

This directory contains the repository-grounded composition layer for the KFM Explorer site.

## Scope

The composition:

- replaces the minimal default page with a map-first, trust-visible landing shell;
- inventories the current Explorer feature families and their conservative maturity state;
- exposes the thirteen domain families already represented under `src/features/domains/`;
- presents KFM's evidence, finite-outcome, time, correction, accessibility, and trust-membrane principles;
- mounts the existing renderer-neutral `map_runtime` selection-to-Evidence-Drawer bridge with deterministic synthetic cases;
- records the current MapLibre package, candidate, and HOLD posture without importing or admitting `maplibre-gl`; and
- projects its existing public anchors through a code-owned workspace registry.

## Unified Workspace UI-01 bounded slice

The first Unified Workspace implementation slice is intentionally public, no-network, and composition-owned:

- `workspace-registry.ts` defines the four existing public workspace destinations and binds them to the current `#map`, `#knowledge`, `#features`, and `#trust` anchors.
- `workspace-navigation.ts` mounts those descriptors into the existing shell without creating routes or privileged actions.
- `workspace-context.ts` defines a strict UI-owned public context projection for workspace, domain, place, released-layer IDs, renderer-neutral camera and selection, material time, compare references, and story position.
- The context parser reuses `@kfm/maplibre` camera and selection validators, rejects extra fields, requires `publicSafe: true`, and keeps URL context synchronized with the compatible workspace hash.
- Unit and browser tests cover registry integrity, feature references, deterministic URL round-trip, malformed/oversized/duplicated context, public-safety exclusions, hash mismatch, and rendered anchor navigation.

This is a bounded browser-composition contract. It is not a canonical semantic contract, source registry, policy rule, evidence object, review decision, release record, deployment record, or publication artifact.

Implementation baseline for this slice: `main@565af2021254c27ea3626724106ad6b1eae800df`.

## Evidence snapshot

The feature catalog is pinned to:

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
- serialize prompts, reviewer notes, restricted coordinates, evidence excerpts, credentials, or private payloads into public workspace URLs;
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

The catalog tests check identifier/path uniqueness, the thirteen-domain inventory, sensitive-domain safeguards, filtering, and preservation of the MapLibre HOLD. The workspace tests add registry, context, URL, negative-input, and browser-navigation coverage.

## Rollback

Revert this slice by restoring `src/main.ts`, removing `workspace-registry.ts`, `workspace-navigation.ts`, `workspace-context.ts`, and their tests, and restoring this README. The original `mount-explorer-site.ts` anchor navigation remains unchanged as the compatibility fallback, so rollback does not require a renderer, API, source, policy, release, deployment, or publication transition.
