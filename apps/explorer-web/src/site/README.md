# Explorer composition shell

This directory contains the repository-grounded composition layer for the KFM Explorer site.

## Scope

The composition:

- replaces the minimal default page with a map-first, trust-visible landing shell;
- inventories the current Explorer feature families and their conservative maturity state;
- exposes the thirteen domain families already represented under `src/features/domains/`;
- presents KFM's evidence, finite-outcome, time, correction, accessibility, and trust-membrane principles;
- mounts the existing renderer-neutral `map_runtime` selection-to-Evidence-Drawer bridge with deterministic synthetic cases;
- mounts the existing finite `MapRuntimePort` trust-status presenter in the normal map workspace through the dependency-free `NullMapRuntime`;
- records the current MapLibre package, candidate, and HOLD posture without activating `maplibre-gl` in Explorer;
- projects its existing public anchors through a code-owned workspace registry;
- builds the fixed illustrative SVG stage with namespace-aware DOM nodes and text content rather than parsing an HTML string; and
- composes existing finite-state features into one text-first public trust surface.

## DOM safety boundary

The illustrative map is a fixed browser composition, not an HTML template. The renderer creates SVG nodes in the SVG namespace, sets attributes individually, and assigns visible labels through text content. Keep dynamic trust-bearing material out of this helper; evidence and state continue through the existing typed, text-first projections. This hardening does not activate MapLibre or establish a governed data path.

## Unified Workspace UI-01 bounded slice

The first Unified Workspace implementation slice is intentionally public, no-network, and composition-owned:

- `workspace-registry.ts` defines the four existing public workspace destinations and binds them to the current `#map`, `#knowledge`, `#features`, and `#trust` anchors.
- `workspace-navigation.ts` mounts those descriptors into the existing shell without creating routes or privileged actions.
- `workspace-context.ts` defines a strict UI-owned public context projection for workspace, domain, place, released-layer IDs, renderer-neutral camera and selection, material time, compare references, and story position.
- The context parser reuses `@kfm/maplibre` camera and selection validators, rejects extra fields, requires `publicSafe: true`, and keeps URL context synchronized with the compatible workspace hash.
- Evidence references remain available for bounded in-memory context transfer, but URL serialization and parsing reject any selection that carries them because this browser-owned projection cannot prove release or access eligibility. Shareable links retain the public selection identifier; a governed interface must resolve admissible evidence after navigation.
- Unit and browser tests cover registry integrity, feature references, deterministic URL round-trip, evidence-reference exclusion, malformed/oversized/duplicated context, public-safety exclusions, hash mismatch, and rendered anchor navigation.

UI-01 is a bounded browser-composition contract. It is not a canonical semantic contract, source registry, policy rule, evidence object, review decision, release record, deployment record, or publication artifact.

Implementation baseline for UI-01: `main@f732cbd1003898dc765a7afe4b635d710e295d17`.

## Unified Workspace UI-02 bounded slice

UI-02 adds the smallest app-local shared trust grammar without moving component ownership or creating a new authority root:

- `trust-state-primitives.ts` strictly validates and renders the same visible labels for outcome, evidence, freshness, coarse sensitivity, release, and correction.
- `trust-surface.ts` composes the existing Trust Header, Time Banner, Citation Pill, Evidence Drawer, and Denial Reason Explorer around deterministic supported, unresolved, restricted, stale, error, and loading cases.
- Extra or inconsistent trust-state metadata fails closed to fixed error copy. The primitive never reflects unknown fields.
- The `LOADING` case is explicitly a transient browser condition, not a governed finite outcome or evidence/release claim.
- Coarse sensitivity values are already-supplied presentation metadata. The browser does not infer sensitivity or evaluate policy.
- Negative cases suppress citation and time affordances, retain text labels rather than color-only signals, and expose no override, approval, promotion, or publication action.
- Multiple Evidence Drawer mounts allocate document-unique panel, label, and title IDs while preserving the original IDs for the first compatible instance.
- Evidence Drawer `ERROR` views suppress release and correction labels when a resolver failure prevents a reliable user-facing interpretation; policy and freshness cues remain visible.
- Unit and browser tests verify the shared six-label grammar, alignment with the existing strict governed projection, loading separation, malformed-input denial, no-network behavior, keyboard-operable case selection, unique accessible drawer relationships, error-detail suppression, and absence of privileged controls.

UI-02 remains under `apps/explorer-web/src/site/` because it has one verified consumer: the Explorer composition. `packages/ui/` remains the future extraction home if another application requires the primitive. This follows the existing app-source and shared-package responsibility boundaries rather than creating a parallel UI root.

Implementation baseline for UI-02: `main@4671f53533cbb1c0757c01d4f90ae60733d544e8`.

Reconciliation baseline for the current UI-02 branch: `main@265b99b81f9526a885caaf799e17c89b5424f9f2`. The reconciliation preserves the separately merged synthetic Focus Mode request surface and repairs shared Evidence Drawer identity and error-state presentation without granting new authority.

## Evidence snapshot

The website feature catalog is refreshed against:

- repository: `bartytime4life/Kansas-Frontier-Matrix`
- ref: `main`
- commit: `90e8a1b231b2c07ae6346ce75ecd42a172ef67e7`
- recorded at: `2026-08-28T14:33:53Z`
- Explorer path: `apps/explorer-web/`
- MapLibre package home: `packages/maplibre/`
- exact MapLibre package version present: `6.6.0`
- package-owned `MapLibreAdapter`: present
- Explorer browser runtime activated: no
- authenticated browser evidence complete: no
- readiness state: `HOLD`

`catalog.ts` is the code-owned website projection for this snapshot. Repository source links generated by the Explorer now resolve against the refreshed exact commit instead of the prior August 19 snapshot.

The prior public catalog snapshot `main@67cf9bcd8d4044beb2f7ec4ec17e1bf162ca30aa` remains available through Git history as lineage only; it is no longer presented as the current website snapshot.

Refresh `catalog.ts` again when repository authority, feature inventory, or maturity changes. A repository snapshot describes website data at one exact state; it does not create runtime, source-admission, review, release, deployment, promotion, or publication authority.

## Trust boundary

This composition does not:

- read `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, candidate, canonical, graph, vector, object, or private lifecycle stores;
- activate or ingest a live source;
- call a model provider or local model runtime;
- perform policy, review, release, correction, rollback, or publication transitions;
- infer evidence from rendered features, pixels, route state, generated text, or a presentation badge;
- infer sensitivity or expand protected detail from a coarse public label;
- serialize prompts, reviewer notes, restricted coordinates, evidence excerpts, credentials, or private payloads into public workspace URLs;
- import `maplibre-gl` or create a second renderer acquisition seam; or
- claim that fixture-first feature slices are live production routes.

The concrete package-owned adapter is present, but Explorer activation and browser-readiness evidence remain separate governed changes after their own gates close.

## Renderer-neutral runtime status

The map workspace now exposes the existing finite runtime-state presenter at its normal point of use. The synthetic controls exercise `IDLE`, `READY`, `STALE`, `WITHDRAWN`, and `ERROR` through `NullMapRuntime`; every non-`READY` state blocks candidate-selection eligibility, and critical states remain text-first assertive alerts.

This is consumer-migration and accessibility proof for the KFM-owned port only. It performs no network, DOM renderer, WebGL, worker, tile, source, evidence, policy, release, deployment, or publication work. The package and initial `MapLibreAdapter` are present, but this Explorer composition still uses `NullMapRuntime`; activation and issue #2906 browser readiness remain on HOLD.

Implementation baseline: `main@8c943018a0cd59b06b5a623e15b9a9068a3513f4`.

## Validation

Run from `apps/explorer-web/` with the repository's locked toolchain:

```bash
pnpm run build
pnpm run test:unit
pnpm run test:browser
```

The catalog tests check identifier/path uniqueness, the thirteen-domain inventory, sensitive-domain safeguards, filtering, exact refreshed snapshot/link binding, and preservation of the MapLibre HOLD. Workspace tests cover registry/context/URL behavior. The Explorer runtime-status browser test covers normal-shell mounting, text-first state and reason fields, selection blocking, assertive critical states, recovery, and preservation of the renderer HOLD. Trust-surface and Evidence Drawer tests cover the consistent public grammar, finite negative states, malformed metadata, no-network boundaries, unique DOM identity, accessible trigger relationships, error-state suppression, and browser presentation.

## Rollback

For this website-data refresh, revert the `catalog.ts`, catalog test, and this README change together to restore the prior repository snapshot. No source, data-lifecycle, renderer-activation, API, policy, review, release, deployment, promotion, or publication transition is required.

For UI-02, restore `src/main.ts`, remove `trust-state-primitives.ts`, `trust-surface.ts`, `site-trust.css`, and their tests, restore this README, and revert the bounded Evidence Drawer identity/error-presentation repair. UI-01 navigation/context behavior and the independently merged Focus Mode request surface remain intact. No data migration, renderer transition, API transition, source transition, policy action, release action, deployment action, or publication action is required.

For the renderer-neutral runtime-status slice, restore `mount-explorer-site.ts` and `site-map.css`, remove its bounded browser test, and restore this README. The reusable port and presenter remain intact, and rollback requires no data, dependency, renderer, API, source, release, deployment, or publication transition.
