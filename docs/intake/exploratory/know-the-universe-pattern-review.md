<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/know-the-universe-pattern-review
title: Know the Universe interaction and trust-disclosure source map
type: exploratory-intake-source-map
version: v1.0.1
status: triaged; corrective-reconciliation; non-authoritative; non-publisher
owners: OWNER_TBD - Explorer UI steward; MapLibre steward; evidence steward; accessibility steward
created: 2026-09-02
updated: 2026-09-02
policy_label: public
owning_root: docs/
responsibility: reconcile public Know the Universe interaction patterns with current KFM Explorer authorities and one bounded fixture-first implementation
truth_posture: CONFIRMED source-review observations and repository evidence / PROPOSED KFM adaptation / UNKNOWN exact private source tree, reusable license, and production architecture
source_review_snapshot: main@4f41d9aa6123ea38207f21cd74dd1d704fef48f4
repository_snapshot: main@596f105e7dfd3e6963e04ed076b3ebb7f68c78fc
implementation_origin: PR #4225; merge commit 596f105e7dfd3e6963e04ed076b3ebb7f68c78fc
correction_status: corrective draft; exact-head hosted validation pending
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

The original source review inspected `main@4f41d9aa6123ea38207f21cd74dd1d704fef48f4`. PR #4225 later introduced the bounded Explorer interaction slice and was merged as `main@596f105e7dfd3e6963e04ed076b3ebb7f68c78fc`.

At the current repository snapshot:

- `apps/explorer-web/src/features/evidence_drawer/index.tsx` resolves a closed public-safe projection into finite `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` states;
- the projection carries `source_role`, including `derived`, and the supported drawer now exposes a prominent derived-representation disclosure;
- `MapRuntimePort` remains the renderer-neutral camera and feature-selection boundary and was not expanded by this slice;
- `workspace-context.ts` remains the strict public-safe camera, selection, time, compare, and story deep-link authority;
- StoryManifest, the fixture-first Story Player, the time banner, and the click-to-Evidence-Drawer bridge remain the integration surfaces; and
- PR #4225 added app-local exploration-mode, view-context, crosshair-candidate, and synthetic point-cloud benchmark modules without acquiring a renderer or activating a live source.

## Implemented boundary

The bounded fixture-first implementation consists of:

1. **Derived-representation disclosure.** A supported Evidence Drawer result whose trusted source role is `derived` receives a prominent semantic note: “Computed from upstream evidence; not a source-observed relationship or event.” Negative outcomes retain fixed no-leak copy.
2. **Explicit exploration modes.** An app-local controller models `ORIENT`, `INSPECT`, `TRAVERSE`, and `STORY`, bounded traversal speed, discoverable conflict-safe shortcuts, reduced-motion fallback, persistent Escape state, and interruption on drawer, route, visibility, or runtime-error events. It does not request pointer lock or change `MapRuntimePort`.
3. **What-you-are-seeing projection.** A closed public-safe view context composes place, time, mode, visible-layer count, representation role, release state, freshness, and correction state into a finite strip view model. It does not infer state from pixels or renderer properties.
4. **Crosshair candidate handoff.** A strict public-visible candidate becomes the existing map-selection wire shape. Zero candidates abstain, multiple candidates require explicit disambiguation, and malformed, hidden, private, duplicate, or expanded payloads fail closed.
5. **Synthetic high-density benchmark contract.** A deterministic 50,000 / 250,000 / 1,000,000-point plan, streaming sample generator, and finite result evaluator define performance and safety gates without allocating a million-point fixture, executing GPU work, admitting a source, or adding a renderer dependency.

## Corrective reconciliation after PR #4225

The merged exact-head checks did **not** establish a valid implementation handoff. Current GitHub evidence identifies the following bounded defects:

- `point-cloud-benchmark.ts` contained a non-UTF-8 binary suffix and an extra closing parenthesis in seed validation;
- `exploration-mode.ts` called an undefined `buttton` identifier and contained a public-runtime guard trigger in commentary;
- `crosshair-selection.ts` called the nonexistent `replaceChildrer` method;
- the Evidence Drawer workflow continued to validate a historical receipt against current bytes after the Evidence Drawer implementation changed; and
- this source map described authoring checks without recording the exact hosted failures that followed the merge.

The failed exact-head workflow runs for the PR #4225 head were:

| Workflow | Run | Failed step |
|---|---:|---|
| `validator-suite` | `33664974091` | Run repository topology ratchet |
| `maplibre-acquisition-inventory` | `33664974188` | Run scanner tests and controlled-remote remediation rehearsal |
| `evidence-drawer-payload` | `33664974212` | Validate evidence-drawer production artifact digests |
| `MapLibre Perf Governance` | `33664973768` | Validate runtime and policy implementation |
| `policy-boundary-guards` | `33664973893` | Run policy boundary guards |
| `ui-build` | `33664973915` | Run Explorer tests |

The policy-boundary JUnit artifact specifically confirmed the non-UTF-8 point-cloud file and the forbidden path-shaped literal. The remaining failed steps are treated as exact-head evidence to re-run after the corrective branch is complete; their root causes are not broadened beyond currently verified evidence.

## Directory Rules basis

- App-local interaction, rendering controls, and view-model code remain under `apps/explorer-web/src/features/`.
- Explorer tests remain under `apps/explorer-web/tests/`.
- External idea reconciliation remains under `docs/intake/exploratory/`.
- Generated authoring receipts remain under the established `data/receipts/generated/` lifecycle responsibility.
- Existing evidence, contract, schema, policy, release, StoryManifest, workspace-context, and MapRuntimePort authorities are referenced rather than copied or redefined.
- No compatibility root, schema home, policy home, source registry, release home, or public data path is added.

## Trust and accessibility invariants

- A renderer candidate scopes a governed request; it is not evidence.
- Derived, modeled, classified, interpolated, clustered, or nearest-neighbour graphics must not be presented as observed relationships or events.
- `Esc` remains an explicit exit from traversal-like state.
- Single-key shortcuts do not activate in text-entry contexts or with browser or system modifiers.
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

The corrective branch must run, at its exact head:

```bash
pnpm --dir apps/explorer-web test:unit
pnpm --dir apps/explorer-web build
git diff --check
```

It must also re-run the repository-native topology, policy-boundary, MapLibre acquisition, performance-governance, Evidence Drawer receipt-integrity, schema, policy, and baseline checks that cover the changed paths.

**No hosted check is represented as passing in this document until exact-head workflow evidence exists.** Local reconstruction and hash calculations establish only candidate source integrity and receipt preparation.

Rollback is a focused revert of the corrective branch. The historical PR #4225 receipts remain immutable lineage records; successor receipts identify the corrected current bytes. No source, lifecycle data, evidence membership, policy decision, human review, release, deployment, publication, or repository setting is changed.
