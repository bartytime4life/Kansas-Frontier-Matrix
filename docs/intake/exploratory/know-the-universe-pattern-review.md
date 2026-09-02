<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/know-the-universe-pattern-review
title: Know the Universe interaction and trust-disclosure source map
type: exploratory-intake-source-map
version: v1.0.0
status: triaged; implementation-mapped; non-authoritative; non-publisher
owners: OWNER_TBD - Explorer UI steward; MapLibre steward; evidence steward; accessibility steward
created: 2026-09-02
updated: 2026-09-02
policy_label: public
owning_root: docs/
responsibility: reconcile public Know the Universe interaction patterns with current KFM Explorer authorities and one bounded fixture-first implementation
truth_posture: CONFIRMED source-review observations and repository overlap / PROPOSED KFM adaptation / UNKNOWN exact private source tree, reusable license, and production architecture
repository_snapshot: main@4f41d9aa6123ea38207f21cd74dd1d704fef48f4
source_url: https://knowtheuniverse.com/?sel=13094770-2323017
related:
  - ./README.md
  - ../../../apps/explorer-web/src/features/evidence_drawer/index.tsx
  - ../../../apps/explorer-web/src/features/map_runtime/exploration-mode.ts
  - ../../../apps/explorer-web/src/features/map_runtime/view-context-strip.ts
  - ../../../apps/explorer-web/src/features/map_runtime/crosshair-selection.ts
  - ../../../apps/explorer-web/src/features/map_runtime/point-cloud-benchmark.ts
  - ../../architecture/evidence-drawer.md
  - ../../architecture/map-shell.md
  - ../../doctrine/map-first.md
[/KFM_META_BLOCK_V2] -->

# Know the Universe interaction and trust-disclosure source map

## Source boundary

The public *Know the Universe* experience was reviewed for transferable interaction ideas. The inspected experience combines orbit and fly-style navigation, searchable object selection, a crosshair while traversing, visual presets, guided story movement, contextual orientation, a high-density point cloud, and computed graph lines. The creator's first-party technical discussion describes the graph lines as computed aids rather than physical connections.

No public source repository, source map, package manifest, production test suite, or reusable code license for the exact application was established during the review. This record therefore maps **behavioral patterns**, not reusable implementation. KFM must not copy JavaScript, shaders, assets, text, data, or private build configuration from the site.

## Current repository reconciliation

At inspected `main@4f41d9aa6123ea38207f21cd74dd1d704fef48f4`:

- `apps/explorer-web/src/features/evidence_drawer/index.tsx` already resolves a closed public-safe projection into finite `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` states;
- the projection already carries `source_role`, including `derived`, but the supported drawer previously rendered that role only as one trust-list entry;
- `MapRuntimePort` already owns renderer-neutral camera and feature-selection values and should not be expanded for an unproved traversal prototype;
- `workspace-context.ts` already owns strict public-safe camera, selection, time, compare, and story deep-link state, so no second URL grammar is justified;
- StoryManifest, the fixture-first Story Player, the time banner, and the click-to-Evidence-Drawer bridge already exist; and
- no canonical crosshair-selection or continuous-traverse implementation was established in the bounded search.

The smallest dependency-closed gap is to make derived representation status prominent, then add app-local renderer-neutral primitives for later integration without acquiring a renderer or changing shared contracts.

## Implemented boundary

This source map accompanies one bounded fixture-first implementation:

1. **Derived-representation disclosure.** A supported Evidence Drawer result whose trusted source role is `derived` receives a prominent semantic note: “Computed from upstream evidence; not a source-observed relationship or event.” Negative outcomes never receive the disclosure and continue to use fixed no-leak copy.
2. **Explicit exploration modes.** An app-local controller models `ORIENT`, `INSPECT`, `TRAVERSE`, and `STORY`, bounded traversal speed, discoverable conflict-safe shortcuts, reduced-motion fallback, persistent Escape state, and interruption on drawer, route, visibity, or runtime-error events. It does not request pointer lock or change `MapRuntimePort`.
3. **What-you-are-seeing projection.** A closed public-safe view context composes place, time, mode, visible-layer count, representation role, release, freshness, and correction into a finite strip view model. It does not infer state from pixels or renderer properties.
4. **Crosshair candidate handoff.** A strict public-visible candidate becomes the existing map-selection wire shape. Zero candidates abstain, multiple candidates require explicit disambiguation, and malformed, hidden, private, duplicate, or expanded payloads fail closed.
5. **Synthetic high-density benchmark contract.** A deterministic 50,000 / 250,000 / 1,000,000-point plan, streaming sample generator, and finite result evaluator define performance and safety gates without allocating a million-point fixture, executing GAU work, admitting a source, or adding a renderer dependency.

## Directory Rules basis

- App-local interaction, rendering controls, and view-model code remain under `apps/explorer-web/src/features/`.
- Explorer tests remain under `apps/explorer-web/tests/`.
- External idea reconciliation remains under `docs/intake/exploratory/`.
- Existing evidence, contract, schema, policy, receipt, release, StoryManifest, workspace-context, and MapRuntimePort authorities are referenced rather than copied or redefined.
- No compatibility root, schema home, policy home, source registry, release home, or public data path is added.

## Trust and accessibility invariants

- A renderer candidate scopes a governed request; it is not evidence.
- Derived, modeled, classified, interpolated, clustered, or nearest-neighbour graphics must not be presented as observed relationships or events.
- `Esc` remains an explicit exit from traversal-like state.
- Single-key shortcuts do not activate in text-entry contexts or with browser/system modifiers.
- Reduced-motion preference prevents traversal activation.
- Multiple crosshair hits are never silently resolved by array order.
- Public-safe context rejects private and unknown fields.
- Synthetic benchmark results have no release, renderer-admission, or production-readiness authority.
- Existing 2D, Evidence Drawer, correction, and rollback paths remain the inspectable baseline.

## Deferred integration
The following remain intentionally held behind existing runtime, source, rights, accessibility, and performance gates:

- actual pointer lock or first-person camera motion;
- concrete MapLibre crosshair hit testing;
- GPU point-cloud rendering, shader controls, or computed graph layers;
- new public presets or a second saved-workspace format;
- live sources, real galaxy data, or imported site assets;
- StoryManifest camera playback changes;
- a versioned shared `MapRuntimePort` expansion;
- release, deployment, promotion, or publication.

Future integration should reuse the current StoryManifest, `kfm-context`, MapRuntimePort, layer admission, Evidence Drawer, and governed API boundaries rather than create parallel systems.

## Validation and rollback

Changed-area validation is:

```bash
pnpm --dir apps/explorer-web test:unit
pnpm --dir apps/explorer-web build
git diff --check
```

The authoring environment additionally performed strict TypeScript no-emit checking of the changed production modules and a Node runtime assertion pass over the app-local controller, context, crosshair, and benchmark functions. Repository-native Vitest, Vite, Playwright, topology, governance, and accessibility results remain exact-head hosted checks until reported by CI.

Rollback is a focused revert of this additive source map, the app-local modules/tests, and the Evidence Drawer view-model/DOM change. No source, lifecycle data, evidence membership, policy decision, review, release, deployment, publication, or repository setting is changed.
