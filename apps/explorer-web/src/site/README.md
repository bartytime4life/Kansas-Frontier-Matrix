# Explorer composition shell

This directory contains the repository-grounded composition layer for the KFM Explorer site.

## Scope

The composition:

- replaces the minimal default page with a map-first, trust-visible landing shell;
- inventories the current Explorer feature families and their conservative maturity state;
- exposes the thirteen domain families already represented under `src/features/domains/`;
- presents KFM's evidence, finite-outcome, time, correction, accessibility, and trust-membrane principles;
- mounts the existing renderer-neutral `map_runtime` selection-to-Evidence-Drawer bridge with deterministic synthetic cases;
- mounts the exact-one governed `/layers` projection through the package-owned Vite MapLibre adapter and finite runtime-status presenter;
- provides a keyboard-operable feature list that reuses the renderer selection identity and resolves `/evidence` into the existing Evidence Drawer;
- falls back once to the dependency-free `NullMapRuntime` on initialization or post-initialization renderer failure while retaining the accessible evidence path;
- records the bounded slice as active while preserving broader MapLibre readiness at `HOLD`;
- projects its existing public anchors through a code-owned workspace registry; and
- composes existing finite-state features into one text-first public trust surface.

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
- Explorer browser runtime activation: bounded exact-one synthetic slice only
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

The concrete package-owned adapter is activated for the bounded exact-one synthetic Explorer slice. Broader renderer/source admission, authenticated browser readiness, production operation, release, deployment, and publication remain separate governed changes on `HOLD` or `UNKNOWN` as applicable.

## Renderer-neutral runtime status

The map workspace now exposes the finite runtime-state presenter at its normal point of use. The canonical synthetic layer is parsed strictly, bound through `InlineGeoJsonMapRuntimePort`, and selected through either package-owned pointer hit testing or the accessible list. Both paths publish the same layer, feature, selection, and evidence identities.

The app-owned transport is restricted to same-origin `GET /layers` and `GET /evidence`, byte-bounds JSON before strict parsing, applies one absolute per-request deadline across headers and body streaming, uses `no-store`, and aborts timed-out work or all active work on teardown. Evidence returned outside the selected reference subset fails closed. Runtime selection invalidation and newer-request versioning prevent late or withdrawn evidence from remaining visible. This bounded synthetic slice does not establish arbitrary source loading, external styles, tiles, broader renderer readiness, release, deployment, or publication authority; those remain on `HOLD` or `UNKNOWN` as applicable.

Implementation basis: branch-local draft slice; exact base and head SHAs belong in the draft PR evidence. This statement is not a `main`, release, deployment, or publication claim.

## Validation

Run from `apps/explorer-web/` with the repository's locked toolchain:

```bash
pnpm run build
pnpm run test:unit
pnpm run test:browser
```

The catalog tests check identifier/path uniqueness, the thirteen-domain inventory, sensitive-domain safeguards, filtering, exact refreshed snapshot/link binding, and preservation of the broader MapLibre HOLD. Governed map tests cover strict layer parsing, bounded same-origin transport, byte-limit cancellation, unresolved-header and stalled-body deadlines, transport abort, pointer/keyboard identity reuse, full Evidence Drawer content, subset rejection, stale-response suppression, initialization and post-initialization fallback, semantic negative states, and repeated mount/teardown cleanup. Trust-surface and Evidence Drawer tests continue to cover the consistent public grammar, finite negative states, unique DOM identity, focus, no-leak rendering, and browser presentation.

## Rollback

For this website-data refresh, revert the `catalog.ts`, catalog test, and this README change together to restore the prior repository snapshot. No source, data-lifecycle, renderer-activation, API, policy, review, release, deployment, promotion, or publication transition is required.

For UI-02, restore `src/main.ts`, remove `trust-state-primitives.ts`, `trust-surface.ts`, `site-trust.css`, and their tests, restore this README, and revert the bounded Evidence Drawer identity/error-presentation repair. UI-01 navigation/context behavior and the independently merged Focus Mode request surface remain intact. No data migration, renderer transition, API transition, source transition, policy action, release action, deployment action, or publication action is required.

For the renderer-neutral runtime-status slice, restore `mount-explorer-site.ts` and `site-map.css`, remove its bounded browser test, and restore this README. The reusable port and presenter remain intact, and rollback requires no data, dependency, renderer, API, source, release, deployment, or publication transition.
