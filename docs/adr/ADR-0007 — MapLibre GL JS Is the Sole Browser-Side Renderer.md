<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0007-maplibre-sole-browser-renderer
title: "ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer"
type: adr
adr_id: ADR-0007
version: v1.4
status: accepted
effective_decision_status: accepted
owners: ["@bartytime4life"]
reviewers_required:
  - Architecture steward
  - Map/runtime steward
  - Security and supply-chain reviewer
  - Explorer Web subsystem owner
  - Docs steward
created: 2026-05-10
updated: 2026-09-12
accepted_on: 2026-08-21
policy_label: public
truth_posture: "ACCEPTED renderer-family architecture / scoped implementation observed / bounded evidence / no operational authority"
owning_root: docs/
responsibility_root: docs/
current_path: "docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
responsibility: "Record MapLibre GL JS as KFM's sole normal production browser map/scene renderer family, reconcile the current scoped implementation without conflating it with dependency or operational admission, classify peer renderers and subordinate capabilities, and retain independent source, runtime, release, deployment, and publication gates."
supersedes: []
superseded_by: []
decision_evidence:
  issue: 2957
  comment_id: 5361592217
  disposition: "ACCEPT ARCHITECTURE DIRECTION / PROHIBIT LEGACY CDN-GLOBAL ACQUISITION / ADR TEXT FOLLOW-UP REQUIRED / NO DEPENDENCY ADMISSION"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: f636df86eb4314b6a0c658bee8b9b11b5a3b99ed
  document_before_update_blob: 2482eea382fd97e68544bb04bc2e2ea1e1cedebe
  package_manifest_blob: 03a24dc1669151863192db30778f30faac0ec5b4
  lockfile_blob: ade374e32fee22866c0a92228329340de99c1196
  port_blob: 5a033319649d5fa55fabbab4d077e29d5235980c
  adapter_blob: e201a7717a0a10efc72440e1c71fd4e07fd919cc
  vite_adapter_blob: 57e0f7da9b13006cde2da2592869fc2ba06a4512
  explorer_composition_blob: 65e5e575f0c116fe60d70d83cf9d631eefe745ca
  explorer_style_blob: 8e45ea05e81c7c2375a6528e19e03759140f27e2
  legacy_harness_blob: ac2522686546b7428ad0cc5c8cd76860ab285998
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - packages/maplibre/README.md
  - packages/maplibre/package.json
  - packages/maplibre/src/map-runtime-port.ts
  - packages/maplibre/src/maplibre-adapter.ts
  - packages/maplibre/src/maplibre-vite-adapter.ts
  - apps/explorer-web/src/site/mount-living-atlas.ts
  - apps/explorer-web/src/features/living_atlas/map-style.ts
  - apps/explorer-web/tests/browser/living-atlas.spec.ts
  - apps/explorer-web/tests/browser/maplibre-webgl-probe.spec.ts
  - tests/policy/test_explorer_web_adapter_boundary.py
  - tests/maplibre/test_package_exports.py
  - tools/validators/maplibre/validate_v6_readiness.py
  - scripts/maplibre-smoke-perf.mjs
  - .github/workflows/maplibre-webgl-probe.yml
  - .github/workflows/maplibre-perf-governance.yml
tags: [kfm, adr, maplibre, browser-renderer, renderer-family, peer-renderer, currentness-correction, no-parallel-authority]
notes:
  - "v1.4 is a documentation-only current-source reconciliation. It preserves the accepted renderer-family decision and does not add, change, or admit a dependency, source, release, deployment, promotion, public serving, or publication."
  - "At the pinned source, private package @kfm/maplibre declares and the scoped lockfile resolves maplibre-gl 6.7.0; the package contains a concrete MapLibre adapter and a package-owned Vite worker helper."
  - "The current Explorer composition uses the package Vite adapter with an inline local style. That bounded source fact and its fixture evidence do not activate an external source, establish runtime readiness, or imply operational authorization."
  - "The reviewed package README is draft and contains stale 6.6.0 admission language that conflicts with the pinned 6.7.0 manifest and lockfile; this ADR does not resolve that governance conflict by assertion."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer

> **Accepted architecture; reconciled current source.** MapLibre GL JS remains KFM's sole normal production browser map/scene renderer family. At the pinned source snapshot, a private package-owned `maplibre-gl@6.7.0` implementation and Vite worker helper exist, and Explorer composes that helper. Those are bounded implementation facts—not a blanket dependency-admission, source-activation, readiness, release, deployment, or publication decision.

> [!IMPORTANT]
> **Family acceptance is distinct from exact dependency governance and operational authority.** ADR-0007 selects the browser-renderer family. It does not make a manifest entry, lockfile resolution, plug-in, protocol, worker, style, source, browser result, or hosted application automatically admitted, safe, operational, released, deployed, or public.

**Quick navigation:** [Status](#1-status) · [Decision](#2-decision-preserved) · [Current source](#3-current-source-snapshot) · [Boundary and conformance](#4-boundary-and-conformance) · [Evidence limits](#5-evidence-and-limits) · [Consequences](#6-consequences-and-open-work) · [References](#7-references-and-change-history)

---

## 1. Status

| Concern | State at `main@f636df86` | Safe conclusion |
|---|---|---|
| Renderer-family architecture | **ACCEPTED** | MapLibre GL JS is the one normal production browser map/scene renderer family in the scope of this ADR. |
| Scoped implementation | **PRESENT / BOUNDED** | `@kfm/maplibre` contains a concrete adapter and Vite worker helper; Explorer composes the latter. |
| Exact source configuration | **OBSERVED** | `packages/maplibre/package.json` and the `packages/maplibre` lockfile importer specify `maplibre-gl: 6.7.0`; the lockfile has a `maplibre-gl@6.7.0` resolution. |
| Formal dependency governance | **UNRESOLVED / CONFLICTED** | The accepted #2957 disposition says no dependency admission. The draft package README still claims a stale 6.6.0 admission. Neither is reconciled by this ADR edit. |
| Direct renderer boundary | **PARTIALLY STRUCTURALLY PROVED** | The reviewed runtime scope confines direct MapLibre imports to package-owned modules, while Explorer has a test against selected raw renderer imports. This is not a universal repository proof. |
| Peer renderer inventory | **BOUNDED OBSERVATION** | The reviewed manifest/lockfile terms show no direct `mapbox-gl`, `leaflet`, `deck.gl`, `@deck.gl`, `cesium`, `openlayers`, or `three` dependency. Term scans still find historical, documentation, and validator references. |
| External styles, sources, and transport | **NOT ACTIVATED** | The adapter rejects external style/resource locators; the current Living Atlas style is inline local data; its browser test rejects external requests. |
| Legacy CDN/global harness | **RETIRED / HOLD** | The former performance script exits with an explicit hold and directs bounded runtime evidence to the package-owned Vite fixture. It is no longer an active CDN acquisition path. |
| Browser/runtime evidence | **BOUNDED; NOT SUFFICIENT FOR OPERATIONS** | Tests and a review-only WebGL2 probe exercise a local fixture and record governance flags as false. They do not establish a support matrix, long-session readiness, or a deployment receipt. |
| Performance | **HOLD / NOT RUN** | The performance workflow and retired harness retain a finite hold pending deterministic fixtures, thresholds, artifact homes, and CI authority. |
| Release, deployment, promotion, public serving, publication | **NOT AUTHORIZED** | No such transition is performed or granted by this accepted ADR or by this documentation-only amendment. |

### 1.1 What changed in v1.4

The accepted renderer-family decision is preserved. The prior implementation narrative was stale: it described a dependency-free package, a placeholder app path, and a still-active nonconforming legacy CDN harness. The pinned source instead contains:

- the private `@kfm/maplibre` package, whose manifest and its scoped `pnpm-lock.yaml` importer both specify `maplibre-gl` `6.7.0`;
- the renderer-neutral `MapRuntimePort` and package root façade;
- `MapLibreAdapter`, which creates and disposes the browser map, checks WebGL2 availability, bounds initialization, synchronizes camera state, and fails closed on external style/resource locators;
- a package-owned Vite helper that sets the MapLibre worker URL and returns the adapter;
- Explorer's `mount-living-atlas.ts` composition of the `@kfm/maplibre/vite-adapter` subpath with a local inline style; and
- local unit, browser, export, boundary, and readiness-validation surfaces with intentionally limited scope.

The source snapshot is evidence of **what is present**, not evidence that all governing reviews or runtime requirements have closed.

### 1.2 Contradictory dependency language is a finding, not a promotion

The current `packages/maplibre/README.md` is itself `draft` and still says that an exact `6.6.0` dependency is admitted. That conflicts with the current `6.7.0` manifest and lockfile configuration, as well as with the #2957 acceptance disposition's explicit “NO DEPENDENCY ADMISSION” boundary.

This ADR therefore records the exact current source configuration only. A later dependency/supply-chain review must reconcile the authority, version, immutable closure, licence, provenance, vulnerability, upgrade, and rollback posture in the appropriate governing record. Do not infer that outcome from a package README label, a lockfile integrity field, or this architecture ADR.

[Back to top](#top)

---

## 2. Decision preserved

### 2.1 One normal browser renderer family

KFM accepts **MapLibre GL JS** as its sole normal production browser map/scene renderer family. The family choice is an architectural constraint for the browser map/scene lane; it does not claim that KFM presently operates a production browser service.

The current package seam remains governed by [ADR-0006](./ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md):

- `packages/maplibre/` owns the reusable concrete MapLibre implementation;
- the KFM-owned `MapRuntimePort` is the consumer-facing runtime contract;
- an app must not acquire `maplibre-gl` directly; and
- new browser renderer code must not form a parallel owner outside the accepted seam.

### 2.2 Subordinate capabilities

A MapLibre plug-in, custom protocol, worker helper, custom layer, overlay, terrain option, or other renderer-specific extension is subordinate only when all of the following hold:

1. it is owned by the package boundary or another expressly accepted extension boundary;
2. it has no independent truth, policy, evidence, source-admission, release, deployment, or publication authority;
3. its acquisition, lifecycle, input, output, error, and teardown behavior are explicitly reviewed; and
4. it does not introduce a peer browser renderer or bypass the governed API and source controls.

Classification as subordinate is not admission. In particular, this ADR does **not** admit any plug-in, source, tileset, glyphs endpoint, sprite, PMTiles protocol, external style, network transport, terrain dataset, 3D scene extension, custom layer, or worker configuration beyond the bounded source already observed.

### 2.3 Peer renderers and exceptions

A peer browser renderer is prohibited by default. Adding, preserving, or reviving one—including `mapbox-gl`, `leaflet`, `deck.gl`, `cesium`, `openlayers`, `three`, or a renderer hidden behind a generic visualisation wrapper—requires a separately accepted, scoped exception or successor ADR.

That later decision must state the owner, migration/compatibility model, bounded use case, non-overlap rule, dependency and supply-chain posture, source boundary, tests, rollback plan, and retirement condition. A package manifest, vendor SDK, plug-in, generated bundle, or product demo cannot create the exception implicitly.

### 2.4 Non-effects

The renderer family is downstream of KFM's trust membrane. It may render an already-authorized presentation; it does not determine whether a source is admitted, an observation is true, a claim is supported, a policy permits disclosure, a release is promotable, or anything may be published.

[Back to top](#top)

---

## 3. Current source snapshot

### 3.1 Package and lockfile observation

At the evidence snapshot:

| Source | Observed fact | What it does not establish |
|---|---|---|
| `packages/maplibre/package.json` | Private `@kfm/maplibre` v0.0.0 declares `maplibre-gl: 6.7.0` and exposes root, `./adapter`, and `./vite-adapter` subpaths. | Formal dependency admission, public npm distribution, or a supported runtime profile. |
| `pnpm-lock.yaml` | The `packages/maplibre` importer specifies and resolves `maplibre-gl` `6.7.0`; a `maplibre-gl@6.7.0` package resolution with an integrity value is present. | Licence/provenance approval, vulnerability disposition, upgrade authorization, or exhaustive supply-chain review. |
| `packages/maplibre/src/map-runtime-port.ts` | Defines KFM runtime values, finite states, camera and selection operations, listeners, errors, and disposal semantics without renderer construction. | That every app input and output is renderer-neutral. |
| `packages/maplibre/src/maplibre-adapter.ts` | Imports MapLibre CSS and map/style types; constructs the map; rejects external resource locators; synchronizes state; and tears down. | External source admission, data transport, plug-in/protocol approval, or live map readiness. |
| `packages/maplibre/src/maplibre-vite-adapter.ts` | Imports/configures the MapLibre worker URL and creates the package adapter. | A generic worker policy, CSP closure, or deployment configuration. |
| `apps/explorer-web/src/site/mount-living-atlas.ts` | Uses the KFM port plus the `vite-adapter` subpath to initialize a map in Explorer. | A fully migrated or operational Explorer. |
| `scripts/maplibre-smoke-perf.mjs` | Retires the former public-CDN harness and returns an explicit hold. | Performance evidence, an alternative harness, or a release gate. |

The phrases “current,” “declares,” and “resolves” in this table are scoped to the pinned repository snapshot. They are not a claim about an upstream MapLibre release, an external CDN, or any environment outside that tree.

### 3.2 Import and type boundary

Within the reviewed runtime source scope, direct `maplibre-gl` imports are package-owned:

| Module | Current direct MapLibre role |
|---|---|
| `packages/maplibre/src/maplibre-adapter.ts` | Map constructor, style type, and CSS acquisition. |
| `packages/maplibre/src/maplibre-vite-adapter.ts` | Worker URL configuration and adapter creation. |

Explorer imports the KFM root port and the package `vite-adapter` entry point; its policy test rejects direct raw imports for MapLibre and several named peer packages in `apps/explorer-web/src`. This is meaningful structural evidence, but its actual scan scope and literal package list bound the claim. It does not prove that no unreviewed generated, binary, dynamically resolved, or future path can acquire a renderer.

The root package façade remains renderer-neutral, but `apps/explorer-web/src/features/living_atlas/map-style.ts` imports the package's `MapLibreSafeStyle` type. That is a narrow renderer-specific style contract at the consumer seam. It is not a reason to create a second renderer owner, nor a basis to assert that all Explorer source is renderer-agnostic. If future consumers need a portable style description, it must be designed and reviewed as a KFM-owned contract rather than disguised as a MapLibre type alias.

### 3.3 Current fixture boundaries

The supplied Living Atlas style is local inline data, and the adapter deep-clones and rejects styles that contain external resource keys or resource locators such as HTTP(S), `data:`, `blob:`, `file:`, or `pmtiles:`. The browser test records no external requests, a rendered canvas, and a `READY` renderer state.

Those constraints intentionally prove a small local fixture. They do not activate a real data source, prove an external protocol, validate a public tile service, permit a CDN, or represent a data/release/publication receipt.

### 3.4 Bounded peer-renderer inventory

For this reconciliation, the current package manifest and `pnpm-lock.yaml` were searched for the named peer renderer dependency terms in `2.3`. No direct dependencies for those terms were found; code search yielded historical, documentation, and validator-policy references for some terms. This helps detect an obvious parallel package but is not an authoritative software-bill-of-materials analysis and does not change the peer-renderer rule.

[Back to top](#top)

---

## 4. Boundary and conformance

### 4.1 Required use of the accepted family

A normal browser map/scene capability must:

1. use the MapLibre family through the package-owned boundary;
2. preserve the `MapRuntimePort` lifecycle and finite-state semantics where it is a consumer;
3. keep raw renderer acquisition out of apps and ordinary consumer modules;
4. fail closed rather than silently substituting a peer renderer;
5. keep renderer activity downstream of governed API, evidence, policy, source, release, and publication boundaries; and
6. obtain separately recorded approval before adding an external source, plug-in, protocol, custom layer, worker mode, or other effectful extension.

### 4.2 Current conformance posture

The implementation partially conforms to the decision:

- `PASS / bounded`: package ownership, concrete adapter, Vite worker helper, app composition through package exports, local-only style enforcement, and tests that cover selected direct-import and fixture behavior;
- `HOLD`: dependency/supply-chain governance reconciliation, exhaustive acquisition inventory, portable style-input design, complete consumer migration, external source/layer/protocol review, wider browser/CSP support, long-session behavior, accessibility, performance, and operational controls;
- `NOT AUTHORIZED`: source activation, release, deployment, promotion, public serving, publication, and any peer-renderer exception.

A partial conformance result must remain partial. It does not rewrite a hold into a pass or convert test coverage into authority.

### 4.3 Legacy CDN/global path

The old smoke/performance script is not a grandfathered exception. Its current implementation reports that the prior flow obtained MapLibre 5.5.0 and glyphs from public CDNs, lacks its referenced fixtures, and lacks governed browser/performance/receipt/trust-artifact stages; it then exits with a finite hold.

No implementation may reactivate that CDN/global path without an accepted successor or scoped exception and its separate source, security, runtime, and operational evidence.

[Back to top](#top)

---

## 5. Evidence and limits

| Evidence surface | What it supports | Explicit limit |
|---|---|---|
| Package manifest and lockfile | Exact declared/resolved `6.7.0` source configuration at the snapshot. | Not dependency or supply-chain governance completion. |
| `MapRuntimePort`, adapter, Vite helper, and Explorer composition source | Scoped implementation placement and current local style/worker behavior. | Not repository-wide runtime behavior or an external deployment. |
| `tests/policy/test_explorer_web_adapter_boundary.py` | Explorer source rejects literal raw imports for the listed renderer packages. | Only the scanned directory and literal patterns. |
| `tests/maplibre/test_package_exports.py` | Package export map and renderer-neutral root façade expectations. | Not every consumer's type boundary or runtime behavior. |
| `apps/explorer-web/tests/browser/living-atlas.spec.ts` | Local Living Atlas can mount one canvas, report `READY`, and avoid external requests. | Synthetic/local fixture; not a source, release, or production proof. |
| `apps/explorer-web/tests/browser/maplibre-webgl-probe.spec.ts` and its workflow | Bounded WebGL2 capability and teardown receipt with `dependency_admission`, `source_activation`, `release`, `deployment`, and `publication` all recorded as `false`. | Browser capability at an exact test run; not a support matrix or operational authorization. |
| `tools/validators/maplibre/validate_v6_readiness.py` and workflow policy | Machine-checked readiness vocabulary and non-authorization constraints. | A validator outcome is not a deployment, source-admission, or publication authority. |
| Retired performance harness and performance workflow | The old route is fail-closed and performance remains held. | No performance baseline, threshold, or runtime comparison has been established. |

The source-derived test and workflow references above were inspected; this ADR edit does not rerun them. Any recorded run is historical unless it is tied to its exact tested revision, environment, fixture, outputs, and retained receipt.

[Back to top](#top)

---

## 6. Consequences and open work

### 6.1 Positive consequences

- The browser map/scene lane has one accepted renderer family and no implicit peer fallback.
- Package ownership gives MapLibre acquisition, worker configuration, lifecycle, and teardown a named implementation home.
- Consumers can target a KFM runtime port while the concrete renderer remains package-owned.
- The local style boundary makes absence of external transport an explicit, testable current fact rather than an assumption.

### 6.2 Costs and constraints

- MapLibre-specific concepts still require explicit containment; the current `MapLibreSafeStyle` import is a visible example of a narrow renderer-specific consumer seam.
- A single family does not remove the need to review every plug-in, worker, protocol, custom layer, source, and style resource.
- The retired CDN harness cannot be used as convenient evidence; a future performance path must be governed from inputs through retained artifacts.
- The draft package README's stale 6.6.0 “admitted” language must not be relied on until the dependency record is reconciled.

### 6.3 Required downstream work

| Work | Required outcome | Authority not granted by completion alone |
|---|---|---|
| Dependency reconciliation | Resolve the exact `6.7.0` closure, licence, provenance, security, upgrade, rollback, and owner disposition against #2957 and stale documentation. | Source activation, release, deployment, or publication. |
| Acquisition and peer inventory | Deterministically scan/attest direct, generated, plug-in, worker, and dynamic acquisition paths. | A peer-renderer exception. |
| Consumer/style boundary | Decide whether a KFM-owned portable style input is needed; remove or bound raw renderer type leakage deliberately. | A second renderer or unreviewed plug-in. |
| External resource admission | Review and bind any style, tile, glyph, sprite, data, protocol, worker, terrain, or custom-layer inputs. | A source/release/publication decision. |
| Browser and CSP support | Repeat bounded tests at exact heads and define supported environments, failure handling, accessibility, and long-session behavior. | Deployment or public operation. |
| Performance governance | Establish deterministic fixtures, thresholds, artifact homes, correction/rollback treatment, and CI authority. | A release claim. |
| Operations | Obtain separately governed release, deployment, promotion, public-serving, and publication decisions if needed. | Architecture changes or dependency upgrades. |

### 6.4 Rollback and supersession

A documentation correction can be reverted through normal review. If a later implementation violates this ADR, the implementation must be removed, disabled, or migrated through its own reviewed rollback without pretending that the historical family decision did not occur.

Replacing MapLibre as the sole normal browser renderer family, adding a durable peer renderer, or changing the exception rule requires a successor or explicit amendment ADR and synchronized index treatment. Do not create a competing runtime simply because an integration is inconvenient.

[Back to top](#top)

---

## 7. References and change history

### 7.1 Canonical repository references

- [Issue #2957 — MapLibre architecture governance](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2957)
- [Issue #2906 — browser/runtime readiness](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2906)
- [ADR-0006 — MapLibre package and adapter boundary](./ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md)
- [Canonical ADR index](./INDEX.md)
- [MapLibre package manifest](../../packages/maplibre/package.json)
- [Map runtime port](../../packages/maplibre/src/map-runtime-port.ts)
- [MapLibre adapter](../../packages/maplibre/src/maplibre-adapter.ts)
- [MapLibre Vite adapter](../../packages/maplibre/src/maplibre-vite-adapter.ts)
- [Explorer composition](../../apps/explorer-web/src/site/mount-living-atlas.ts)
- [Explorer inline style](../../apps/explorer-web/src/features/living_atlas/map-style.ts)
- [Explorer raw-renderer boundary test](../../tests/policy/test_explorer_web_adapter_boundary.py)
- [Living Atlas browser fixture](../../apps/explorer-web/tests/browser/living-atlas.spec.ts)
- [MapLibre WebGL2 probe](../../apps/explorer-web/tests/browser/maplibre-webgl-probe.spec.ts)
- [Readiness validator](../../tools/validators/maplibre/validate_v6_readiness.py)
- [Retired legacy performance harness](../../scripts/maplibre-smoke-perf.mjs)

### 7.2 Supporting design lineage — non-authoritative

The reviewed Notion and Drive materials are design/coordination lineage only. They reinforce that the map renderer is downstream of governed evidence and that 2D/local fixture work is not a source or operational authority. They do not establish current repository state, dependency admission, runtime results, release, deployment, or publication:

- [Close governed MapLibre runtime probe matrix (Notion)](https://www.notion.so/3c9a92021bf68146ab6aca4e03139382)
- [KFM Explorer — Kansas-First Layers, Animation, Live Updates, 3D & Performance Roadmap (Google Drive)](https://docs.google.com/document/d/1L8zsQgam1bdP7uUbX2zxOkTA01enXXu_tlHLKZRPvzQ/edit)
- [KFM Explorer — Living Atlas Interface, default views, animation and implementation design (Google Drive)](https://docs.google.com/document/d/1aivNyfMjQ8urQO6vjt4YvkT1ltF1t7fxCahEcnGV4Dw/edit)

### 7.3 Exact non-effects

This v1.4 documentation-only amendment does not modify a package, lockfile, source module, browser app, source descriptor, policy, contract, schema, test, fixture, validator, workflow, receipt, proof, artifact, release object, deployment, public service, publication target, access control, or repository setting. It does not activate a source, run a browser probe, admit a dependency, upgrade MapLibre, or grant any operational authority.

### 7.4 Change history

| Edition | Date | Disposition |
|---|---|---|
| `v1.2` | 2026-08-13 | Repository-grounded proposed decision and pre-acceptance evidence snapshot; preserved in Git history. |
| `v1.3` | 2026-08-21 | Accepted renderer-family source transition authorized by issue #2957; no dependency, runtime, release, deployment, or publication effect. |
| `v1.4` | 2026-09-12 | Documentation-only current-source reconciliation: records the scoped `6.7.0` package/lockfile configuration, package-owned adapter/worker, Explorer composition, retired CDN harness, and unresolved dependency-governance conflict; preserves the accepted family decision and all operational holds. |

---

_Last updated 2026-09-12 · Document version: v1.4 · Source metadata: `accepted` · Effective decision status: `accepted` · Implementation: present / bounded · Dependency governance: unresolved / conflicted · Operational effect: none · [Back to top](#top)_
