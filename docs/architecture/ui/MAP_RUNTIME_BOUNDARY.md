<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/ui/map-runtime-boundary
title: Map Runtime Boundary — Current Renderer-Neutral Bridge, Package-Owned Adapter Direction, and Renderer HOLD
type: architecture-reference
version: v2.0
status: draft; repository-grounded; bounded-executable; renderer-hold; non-publisher
owners:
  - "@bartytime4life — verified CODEOWNERS review route"
  - "NEEDS VERIFICATION — independent UI, map-runtime, accessibility, security, policy, evidence, dependency, and release stewardship"
created: 2026-05-14
updated: 2026-08-19
policy_label: public; architecture; ui; map-runtime; trust-membrane; no-release; no-publication
owning_root: docs/
current_path: docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
responsibility: Explain the current renderer-neutral map-interaction boundary, the package-owned future renderer seam, its trust and acquisition constraints, and its graduation requirements without creating contract, schema, dependency, policy, release, deployment, or publication authority.
truth_posture: cite-or-abstain; current-state claims are pinned to repository evidence; maintainer direction, proposed ADRs, future interfaces, dependency admission, runtime behavior, deployment, and public operation remain visibly bounded
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 75849a09b2d18113a9a9b6c78332b83d19eb5832
  target_prior_blob: baf929fdca617ea95ea4ce5bde4c7b8abd9ac6d5
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  adr_index_blob: 419ebd60db28404edb0d363125c85f6f15deaec0
  map_shell_blob: b0ae23f2399c019a737a27c6aaaf0d34323b1fb7
  map_selection_bridge_blob: 18d61ea0ef2fbe2fc2f3cc9d42291c101003037f
  click_bridge_readme_blob: de7219fcb58d257d81a6e50c3d060c932c9c35f2
  layer_manifest_admission_blob: 895100728c9eb676b9e2aef84680073142694b27
  explorer_manifest_blob: ddd201b74a06001d84a14bf54ac62a6cc3607a29
  explorer_adapter_blob: 663ba0f7a05498948f67d644387c73ab19d5c16c
  maplibre_package_manifest_blob: b0582955feeb51016327113692fa5c98ecad8816
  maplibre_package_entry_blob: 91664eb00583f9e3d0405eb7954fefa9a48f4ee9
  acquisition_inventory_blob: 2d5b9f0cf494ebb6f3cfc6e4f12acb497572edcf
  governed_api_architecture_blob: 06c5fd269fb8a326269f7f8ba98c6b8a75e0fd1a
  map_evidence_unit_test_blob: 953bf536f1d3062c194a09855ed3dde4bc9fa311
  map_evidence_browser_test_blob: 14164e00253f1db6cdaff65a4fd1fa8944f3041e
  explorer_adapter_boundary_test_blob: 97d44069b0a5ab4a82b1e1fc48665e905c08a287
  maplibre_decision_issue: 2957
  runtime_probe_issue: 2906
related:
  - docs/architecture/ui/README.md
  - docs/architecture/ui/BOUNDARIES.md
  - docs/architecture/ui/STATE_OWNERSHIP.md
  - docs/architecture/ui/LAYERING.md
  - docs/architecture/ui/ROUTE_MAP.md
  - docs/architecture/ui/CONTINUITY_NOTES.md
  - docs/architecture/map-shell.md
  - docs/architecture/maplibre-master.md
  - docs/architecture/governed-api.md
  - docs/doctrine/directory-rules.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - apps/explorer-web/src/features/map_runtime/index.tsx
  - apps/explorer-web/src/features/map_runtime/layer_manifest_admission.ts
  - apps/explorer-web/src/features/map_runtime/CLICK_EVIDENCE_BRIDGE.md
  - apps/explorer-web/src/adapters/MapLibreAdapter.ts
  - packages/maplibre/package.json
  - packages/maplibre/src/index.ts
  - tools/validators/maplibre/assess_acquisition_inventory.py
tags: [kfm, architecture, ui, map-runtime, maplibre, renderer-neutral, adapter, evidence-drawer, finite-outcomes, trust-membrane, renderer-hold, rollback]
notes:
  - "v2.0 replaces proposal-era and no-repository language with a current repository-grounded boundary."
  - "Current executable map-runtime behavior is renderer-neutral and fixture-first; no functioning MapRuntimePort or MapLibre adapter is established."
  - "Issue 2957 records maintainer direction for package home, dependency ownership, renderer family, consumer migration, version/admission separation, and rollback, while keeping ADR-0006/0007 proposed and runtime implementation blocked."
  - "The future concrete runtime importer is directed toward packages/maplibre; the comment-only Explorer MapLibreAdapter file must not become a second renderer importer."
  - "This document changes no app code, package, dependency, contract, schema, policy, source, lifecycle state, release, deployment, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="map-runtime-boundary"></a>

# Map Runtime Boundary

> **Operating rule.** The map renderer is downstream of evidence, policy, review, release, correction, and rollback. A map interaction may scope a governed request; it does not create a claim, resolve evidence, or authorize exposure.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-d4a72c?style=flat-square)
![current bridge](https://img.shields.io/badge/current%20bridge-renderer--neutral-0969da?style=flat-square)
![MapRuntimePort](https://img.shields.io/badge/MapRuntimePort-not%20implemented-6e7781?style=flat-square)
![MapLibre](https://img.shields.io/badge/MapLibre%20runtime-HOLD-b42318?style=flat-square)
![publication](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)

| Field | Current bounded result |
|---|---|
| **Evidence snapshot** | `main@75849a09b2d18113a9a9b6c78332b83d19eb5832` |
| **Document role** | Human-readable architecture reference; not semantic, schema, policy, dependency, release, or runtime authority |
| **Placement** | **CONFIRMED:** same existing path under `docs/architecture/ui/`; accepted ADR-0029 adopts Directory Rules v2 |
| **Current executable boundary** | **CONFIRMED / BOUNDED:** strict renderer-neutral map-feature selection, injected resolver, evidence-subset guard, finite Evidence Drawer projection, and fixture-only layer-manifest admission |
| **Current map stage** | **SYNTHETIC:** no functioning browser map renderer, real camera, released map layer, or MapLibre boot |
| **`MapRuntimePort`** | **PROPOSED / NOT IMPLEMENTED:** no concrete TypeScript port was verified |
| **Concrete adapter** | **BLOCKED:** future sole runtime importer is directed under `packages/maplibre/`; current Explorer adapter file is comment-only and must not become a second importer |
| **Renderer package** | **CONFIRMED scaffold:** private `@kfm/maplibre` `0.0.0`, no declared dependencies, placeholder export only |
| **Governed API** | **CONFIRMED scaffold:** `/bootstrap`, `/layers`, and `/evidence` return `ABSTAIN / NOT_IMPLEMENTED`; no live click-resolution transport exists |
| **Decision posture** | ADR-0006 and ADR-0007 remain **proposed**. Issue #2957 records maintainer direction but does not accept either ADR |
| **Gate posture** | Architecture direction recorded; acquisition evidence **HOLD**; ADR status open; runtime implementation blocked |
| **Deployment / public operation** | **UNKNOWN / not established** |
| **Review route** | `@bartytime4life` through CODEOWNERS; independent specialist review remains **NEEDS VERIFICATION** |

> [!IMPORTANT]
> **Repository-grounded does not mean renderer-ready.** Current code proves a bounded request-scoping and Evidence Drawer laboratory. It does not prove a functioning `MapRuntimePort`, concrete MapLibre adapter, admitted renderer dependency, live governed transport, released-layer flow, deployment, or public operation.

> [!CAUTION]
> **Issue #2957 maintainer direction is not an accepted ADR.** It provides coherent direction for the physical home and seam, but ADR-0006/0007 status, structural acquisition closure, dependency admission, and runtime proof remain separate gates.

> [!WARNING]
> **Rendering is not publication.** A browser feature, hit-test, screenshot, or successful performance probe is downstream technical evidence only. It does not establish claim truth, rights clearance, sensitivity approval, review approval, release, or publication safety.

## Quick jump

- [0. Current evidence snapshot](#0-current-evidence-snapshot)
- [1. Purpose](#1-purpose)
- [2. The one-sentence rule](#2-the-one-sentence-rule)
- [3. Scope & non-scope](#3-scope--non-scope)
- [4. The boundary, at a glance](#4-the-boundary-at-a-glance)
- [5. `MapRuntimePort` — contract](#5-mapruntimeport--the-contract-the-rest-of-the-ui-may-import)
- [6. `MapLibreAdapter` — single importer](#6-maplibreadapter--the-only-module-that-may-import-maplibre)
- [7. Feature click → claim resolution](#7-feature-click--claim-resolution)
- [8. `LayerDescriptor` requirements](#8-layerdescriptor-requirements)
- [9. Camera & time synchronization](#9-camera--time-synchronization)
- [10. Forbidden browser operations](#10-forbidden-browser-operations)
- [11. Negative states](#11-negative-states-first-class)
- [12. Validation & tests](#12-validation--tests)
- [13. Rollback](#13-rollback-path)
- [14. Related docs](#14-related-docs)
- [15. Open questions](#15-open-questions--verification-backlog)
- [Appendix A](#appendix-a--method-signature-sketch-illustrative)
- [Appendix B](#appendix-b--anti-patterns-this-boundary-forbids)

---

## 0. Current evidence snapshot

### 0.1 What exists now

| Surface | Verified repository evidence | Safe conclusion |
|---|---|---|
| [`map_runtime/index.tsx`](../../../apps/explorer-web/src/features/map_runtime/index.tsx) | Strict `kfm.explorer.map-feature-selection.v1` parser, exact fields, safe IDs, maximum 16 unique evidence refs, injected resolver, subset guard, finite local failures | A rendered-feature candidate can be represented and safely projected through a fixture resolver; it is not evidence itself |
| [`CLICK_EVIDENCE_BRIDGE.md`](../../../apps/explorer-web/src/features/map_runtime/CLICK_EVIDENCE_BRIDGE.md) | Explicit renderer-neutral, no-network, fixture-first boundary | Real renderer and transport wiring remain future work |
| [`layer_manifest_admission.ts`](../../../apps/explorer-web/src/features/map_runtime/layer_manifest_admission.ts) | Deterministic fixture evaluator with `PASS`, `HOLD`, `DENY`, `ERROR`; result always records no authority, registry mutation, or MapLibre source creation | Eligibility evaluation is not registration, release, rendering, or publication |
| [`map-shell.md`](../map-shell.md) | Current Explorer map stage is synthetic and MapLibre remains on HOLD | No real map boot or released-layer render is proved |
| [`MapLibreAdapter.ts`](../../../apps/explorer-web/src/adapters/MapLibreAdapter.ts) | Comment-only file; no import, export, or implementation | It is not a functioning adapter and must not become a second renderer importer |
| [`packages/maplibre/package.json`](../../../packages/maplibre/package.json) | Private package `@kfm/maplibre`, version `0.0.0`, no renderer dependency | Package identity exists; dependency and runtime admission do not |
| [`packages/maplibre/src/index.ts`](../../../packages/maplibre/src/index.ts) | Placeholder export only | No port, adapter, protocol registrar, or renderer lifecycle exists |
| [`governed-api.md`](../governed-api.md) | Current routes are ABSTAIN stubs | No live browser click-resolution API can be claimed |
| [`assess_acquisition_inventory.py`](../../../tools/validators/maplibre/assess_acquisition_inventory.py) | Bounded no-network renderer acquisition inventory | Structural evidence exists, but the accepted exact seam and complete negative coverage remain on HOLD |
| [ADR index](../../adr/INDEX.md) | ADR-0029 accepted; ADR-0006 and ADR-0007 proposed | Documentation and issue comments cannot silently accept renderer architecture |

### 0.2 Decision and gate state

Issue [#2957](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2957) records the following **maintainer direction**, without changing ADR status:

| Question | Direction | Remaining boundary |
|---|---|---|
| Physical implementation home | Retain `packages/maplibre/`; do not create a writable `packages/maplibre-runtime/` peer | ADR text still requires reviewed disposition |
| Adapter seam | Keep KFM-owned `MapRuntimePort` plus one concrete package-owned `MapLibreAdapter` | App stub must be removed, renamed, or renderer-neutral; exact importer module remains unresolved |
| Dependency ownership | Only `packages/maplibre/package.json` may own `maplibre-gl` and renderer-bound helpers | No package or version is admitted |
| Renderer family | MapLibre GL JS is the sole normal browser map/scene renderer family; a peer renderer requires a scoped exception/successor ADR | ADR-0007 remains proposed; mobile/native is not decided |
| Acquisition inventory | Repository-wide structural enforcement required | **HOLD:** coverage and exact-seam enforcement remain incomplete |
| Consumer migration | Consumers use KFM-owned types; no temporary direct renderer imports | No functioning consumer seam exists yet |
| Version/admission split | Architecture, dependency admission, and authenticated runtime proof are separate transitions | #2906 remains the runtime evidence owner |
| Rollback | Preserve the dependency-free scaffold and fake/null port as rollback baseline | Must be proved by later implementation tests |

**Gate state:** architecture direction recorded; structural acquisition evidence on **HOLD**; ADR status **OPEN**; runtime implementation **BLOCKED**.

### 0.3 Material corrections from v0.1

This revision removes or bounds earlier claims that were not current repository facts:

- no implemented `MapRuntimePort` is claimed;
- the app-local comment-only adapter is not treated as the future direct importer;
- proposed `/claims/resolve` and `/evidence/:ref` routes are not represented as live behavior;
- renderer-neutral selection is distinguished from MapLibre event wiring;
- layer admission is described as fixture eligibility, not source creation or release;
- issue #2957 direction is separated from accepted ADR authority;
- dependency admission and #2906 browser proof remain separate from architecture direction;
- deployment, public operation, and release are not inferred from source files or tests.

[Back to top](#top)

---

## 1. Purpose

This document explains the browser map-runtime boundary shared by Explorer Web, the future reusable renderer package, the governed API, and trust-visible UI surfaces. It answers four questions:

1. What map interaction is implemented today?
2. What future KFM-owned port and adapter seam has maintainer direction?
3. What evidence, policy, release, acquisition, and runtime gates must close before real rendering?
4. What is never allowed to become browser or renderer authority?

It does **not** define the canonical semantic contract or machine schema for `MapRuntimePort`, `LayerDescriptor`, `LayerManifest`, map events, or runtime outcomes. Those require their own accepted authority and executable closure.

### Placement basis

The tracked page already explains cross-cutting UI architecture to humans. Keeping it at `docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md` preserves its identity and the accepted `docs/` responsibility boundary under [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md). This same-path correction creates no new root, schema home, contract home, policy home, package, registry, release lane, or compatibility surface.

[Back to top](#top)

---

## 2. The one-sentence rule

> **UI code depends on KFM-owned map-runtime types; one accepted implementation module may acquire the renderer; every consequential claim still resolves through governed evidence and policy.**

The boundary is intentionally asymmetric:

```text
Explorer features / shell / Evidence Drawer
                 |
                 v
        KFM-owned port and event types
                 |
                 v
 package-owned concrete MapLibre adapter
                 |
                 v
       admitted MapLibre runtime
```

Renderer instances, events, source objects, layer objects, worker handles, protocol handles, and unreviewed URLs do not cross upward. Evidence, policy, review, release, correction, and rollback decisions do not move downward into the adapter.

### Authority order for this boundary

1. Accepted ADRs and Directory Rules for placement and architecture authority.
2. Semantic contracts, schemas, and policy for meaning, machine shape, and admissibility.
3. Current code, fixtures, tests, validators, package manifests, and workflows for implementation behavior.
4. Issue #2957 for recorded maintainer direction only.
5. This page for orientation.

[Back to top](#top)

---

## 3. Scope & non-scope

### 3.1 In scope

- renderer acquisition and dependency isolation;
- KFM-owned port, view, time, layer, event, and finite-result boundaries;
- translation from renderer hit testing into the existing strict feature-selection profile;
- release-aware source/layer/style admission requirements;
- camera and time ownership;
- allowed renderer effects, cleanup, telemetry, and rollback;
- negative states, accessibility, acquisition enforcement, tests, and graduation evidence.

### 3.2 Out of scope

- deciding truth, source authority, evidence sufficiency, rights, sensitivity, policy, review, release, or publication;
- reading RAW, WORK, QUARANTINE, canonical databases, internal object stores, proof stores, vector stores, graph stores, or model runtimes from the browser;
- inventing a live API route, DTO, contract, schema, renderer version, plugin list, or deployment;
- accepting ADR-0006/0007 through architecture prose;
- activating a source, registering a layer, releasing an artifact, deploying Explorer, or publishing a KFM claim;
- deciding mobile/native architecture or introducing a peer renderer.

### 3.3 Responsibility split

| Responsibility | Owning surface | Renderer/adaptor posture |
|---|---|---|
| Source identity, rights, sensitivity, evidence, review, release | Governed upstream services and records | Consume only public-safe projections; never decide |
| Semantic meaning | `contracts/` | Do not redefine in UI code |
| Machine shape | `schemas/` | Validate at appropriate boundaries; do not invent parallel shapes |
| Admissibility | `policy/` and reviewed decisions | Reflect finite outcome; do not evaluate policy locally |
| Reusable renderer implementation | Directed under `packages/maplibre/` after ADR closure | One exact importer; renderer types remain private |
| Deployable UI composition | `apps/explorer-web/` | Depend on KFM-owned types and projections only |
| Architecture explanation | `docs/architecture/` | Explain and connect; no runtime authority |
| Release decisions and rollback targets | `release/` plus governed accountability records | Adapter consumes released state; never promotes |

[Back to top](#top)

---

## 4. The boundary, at a glance

### 4.1 Current bounded path

```text
synthetic selection control
    -> strict MapFeatureSelection parser
    -> injected fixture resolver
    -> Evidence Drawer projection validator
    -> evidence-subset guard
    -> ANSWER / ABSTAIN / DENY / ERROR UI
```

Current code performs no renderer, network, source, policy, lifecycle, evidence-store, or model access in this bridge. The layer-manifest evaluator is also fixture-only and always reports no authority, registry mutation, or MapLibre source creation.

### 4.2 Directed target after governance and admission close

```text
released public-safe layer projection
    -> MapRuntimePort
    -> package-owned MapLibreAdapter
    -> admitted renderer source/layer/style effects

renderer hit test
    -> bounded MapFeatureSelection
    -> governed API request
    -> EvidenceRef -> EvidenceBundle resolution
    -> policy/review/release/correction checks
    -> finite response
    -> Evidence Drawer / Focus Mode / export
```

Each arrow is a boundary with its own contract, validation, negative states, and cleanup. No arrow may be replaced by direct client access to an internal store.

### 4.3 Boundary law

- **Selection is scope, not evidence.**
- **Admission is eligibility, not registration.**
- **Registration is not release.**
- **Release is not deployment.**
- **Deployment is not publication.**
- **Rendering is not truth.**

[Back to top](#top)

---

## 5. `MapRuntimePort` — the contract the rest of the UI may import

### 5.1 Current status

`MapRuntimePort` appears in architecture and decision prose, but no concrete TypeScript port implementation was verified at the evidence snapshot. The current renderer-neutral selection code is useful downstream behavior; it is not the port itself.

### 5.2 Directed ownership

The public interface and implementation should live in the accepted reusable package boundary under `packages/maplibre/`, unless a reviewed ADR explicitly selects another location. Explorer may own composition over that package, but it must not own a second renderer importer.

### 5.3 Minimum capability families

A future accepted port should expose KFM-owned shapes for:

| Capability | KFM-owned input/output | Authority limit |
|---|---|---|
| Lifecycle | initialize, ready state, dispose | No release or deployment decision |
| View | center, zoom, bearing, pitch, bounds | Camera state is not evidence |
| Time | valid/observed/release context | Adapter reflects time; it does not infer it |
| Layers | admit/remove/visibility/order through governed projections | No raw source URL or registry mutation |
| Selection | bounded feature identity plus approved evidence refs | No arbitrary properties or geometry leakage |
| Events | selection, view change, finite runtime state | No raw MapLibre event object |
| Results | finite success/hold/deny/error reason codes | No silent fallback to unsafe allow |

### 5.4 Port invariants

A conforming public API must not expose:

```text
maplibregl.Map
MapLibre source/layer/style/event types
raw rendered-feature objects
worker or protocol handles
unreviewed URL strings
internal-store clients
policy or release mutation
```

Consumers must compile and test against a fake or null implementation without MapLibre installed. That property is part of the rollback design, not only test convenience.

[Back to top](#top)

---

## 6. `MapLibreAdapter` — the only module that may import MapLibre

### 6.1 Current physical state

- `apps/explorer-web/src/adapters/MapLibreAdapter.ts` contains only a comment.
- `packages/maplibre/src/index.ts` exports only `placeholder = true`.
- neither package manifest declares `maplibre-gl`.
- no functioning adapter or approved exact importer module is established.

### 6.2 Corrected physical direction

Issue #2957 directs the eventual concrete importer under `packages/maplibre/`. The current app-local file must therefore be removed, renamed, or converted into renderer-neutral composition over the package API; it must not become a second implementation or direct renderer importer.

The exact package source module remains **NEEDS VERIFICATION** until the ADR text and structural validator agree. This page does not invent that path.

### 6.3 Dependency ownership

Only `packages/maplibre/package.json` may eventually own:

- `maplibre-gl`;
- renderer-bound plugins, protocols, overlays, custom-layer helpers, or workers;
- their exact lockfile closure.

This direction admits no version or dependency. Exact version, integrity, license, supply-chain, CSP/worker, browser-support, and removal evidence remain a separate reviewed transition.

### 6.4 Adapter responsibilities after admission

The concrete adapter may:

- initialize and dispose one map instance;
- translate KFM-owned view and time state into renderer calls;
- compile already-governed source/layer/style projections into bounded effects;
- translate renderer selection into `MapFeatureSelection` without widening evidence scope;
- register only admitted protocols/plugins in one auditable location;
- emit fixed, non-sensitive runtime reason codes and bounded telemetry;
- remove sources, layers, handlers, workers, and protocol registrations deterministically.

It must not:

- resolve evidence, evaluate policy, approve release, or write lifecycle state;
- fetch arbitrary URLs or internal stores;
- place sensitive geometry into delivered bytes and rely on style filters to hide it;
- expose raw renderer types to consumers;
- fall back to another renderer after failure;
- treat successful render as proof or publication.

### 6.5 Acquisition enforcement status

The current acquisition inventory detects several renderer acquisition classes and distinguishes `PASS`, `HOLD`, `FAIL`, and `ERROR`. It remains insufficient to authorize the seam because issue #2957 still requires:

- one exact approved importer rather than an entire package or app-adapter directory;
- complete negative coverage for re-exports, plugins/custom layers, workers, protocol registration, duplicate manifests, and lockfile ownership;
- explicit treatment or retirement of the CDN/global performance harness;
- fail-closed enforcement after an ADR is accepted.

Until those close, renderer acquisition remains **HOLD**.

[Back to top](#top)

---

## 7. Feature click → claim resolution

### 7.1 Current implemented flow

The strict current selection profile contains exactly:

| Field | Rule |
|---|---|
| `profile` | Must equal `kfm.explorer.map-feature-selection.v1` |
| `selection_id` | Safe bounded identifier |
| `layer_id` | Safe bounded identifier |
| `feature_id` | Safe bounded identifier |
| `evidence_refs` | At most 16 unique safe identifiers |

Unknown fields, unsafe identifiers, duplicate evidence refs, and oversized evidence-ref lists fail validation. An empty evidence list returns `ABSTAIN / MISSING_EVIDENCE` without calling the resolver.

The injected resolver result is projected through the Evidence Drawer validator. Returned evidence refs must be a subset of the refs declared by the selection; widening produces `ERROR / DRAWER_EVIDENCE_OUTSIDE_SELECTION` and no citation leakage.

### 7.2 Current authority limit

The bridge explicitly performs no network, renderer, source, policy, evidence-store, lifecycle, or model access. Browser tests prove synthetic keyboard selection, supported evidence, missing evidence, fixed sensitive denial copy, evidence-scope mismatch, and resolver-error behavior. They do not prove live data, API, MapLibre, release, or deployment.

### 7.3 Governed API correction

Earlier proposal text named live claim-resolution routes. Current governed API evidence instead shows `/bootstrap`, `/layers`, and `/evidence` as `ABSTAIN / NOT_IMPLEMENTED` scaffolds. A future click transport must be established by reviewed route/DTO/schema/policy/evidence/release tests before this page names it as operational.

### 7.4 Future renderer translation rule

A renderer hit test may contribute only the minimum released identity needed to form the strict selection profile. It must not send raw geometry, arbitrary feature properties, hidden sensitive fields, style metadata, or renderer objects into the Evidence Drawer or governed API.

```text
rendered candidate
    -> public-safe layer_id + feature_id + bounded evidence_refs
    -> governed resolution
    -> finite response
```

The resolver, not the renderer, determines whether evidence can support an answer.

[Back to top](#top)

---

## 8. `LayerDescriptor` requirements

### 8.1 Current implementation is a fixture admission profile

The current Explorer evaluator accepts a synthetic layer-manifest profile and returns an admission projection. It is not the canonical layer contract, active registry, released-layer loader, or renderer source compiler.

### 8.2 Current synthetic admission checks

The evaluator checks, among other bounded fields:

- allowed source class;
- lifecycle and release state;
- stale, withdrawn, and superseded posture;
- manifest/release/artifact/evidence/policy/review/promotion bindings;
- artifact integrity and signature posture;
- rollback reference.

Its result always states:

```text
authority = NONE
registryMutated = false
maplibreSourceCreated = false
```

### 8.3 Target descriptor/manifest obligations

Before a real layer reaches the port, a governed projection should establish at least:

- stable layer, source, artifact, and release identity;
- public-safe source class and delivery format;
- temporal scope and freshness;
- spatial support, CRS, precision, and generalization posture;
- rights, sensitivity, policy, and review state;
- EvidenceRef/EvidenceBundle support appropriate to the claim;
- integrity, signature/attestation where required, and released byte binding;
- correction, withdrawal, supersession, cache-invalidation, and rollback references;
- accessibility alternative and performance budget.

The canonical semantic and machine homes remain separate governance questions and must not be silently decided here.

### 8.4 Derived-carrier rule

PMTiles, MVT, COG, GeoParquet, TileJSON, style JSON, images, terrain, 3D assets, and search/graph projections are downstream carriers. Their presence, validity, or successful rendering does not make them evidence, policy, review, or release authority.

[Back to top](#top)

---

## 9. Camera & time synchronization

### 9.1 Current state

The current map stage is synthetic. No real camera, basemap, renderer lifecycle, or map-time synchronization was verified. Architecture prose must not describe these as implemented.

### 9.2 Target state ownership

| State | Owner | Adapter role |
|---|---|---|
| Camera/view intent | Shell or route-level KFM state | Apply and emit bounded view state |
| Valid/observed/release time | Governed temporal context | Reflect; never derive from tile timestamps alone |
| Layer visibility/order | KFM shell over admitted layer projections | Apply only admitted operations |
| Selection | KFM-owned selection contract | Translate renderer hit test into bounded identity |
| Evidence Drawer state | Evidence Drawer feature | No direct mutation by renderer |
| Correction/withdrawal state | Governed upstream response and cache policy | Remove/replace affected visual carriers |

### 9.3 Time discipline

Where material, valid time, observation time, source publication time, retrieval time, KFM release time, and correction time remain distinct. The renderer must not collapse them into one slider timestamp or infer currency from network success.

A time change should re-evaluate layer eligibility and evidence scope rather than merely restyle an unchanged source.

### 9.4 URL and replay posture

Shareable view state should use versioned KFM-owned shapes and bounded values. It must not embed:

- raw internal URLs or credentials;
- restricted coordinates or hidden source fields;
- renderer-specific serialized objects;
- unreviewed style/source payloads;
- evidence or release claims unsupported by the governed response.

Replay requires a compatible released layer set and finite failure when the referenced state is unavailable, withdrawn, superseded, or denied.

[Back to top](#top)

---

## 10. Forbidden browser operations

The Explorer browser and renderer adapter must not:

1. read RAW, WORK, QUARANTINE, canonical databases, internal object stores, proof stores, registries, or model runtimes directly;
2. resolve EvidenceRefs from an internal store without the governed API;
3. decide rights, sensitivity, policy, review, release, correction, or rollback;
4. fetch arbitrary source URLs supplied by feature data or user content;
5. expose raw errors, credentials, internal paths, sensitive reason detail, or hidden fields;
6. hide delivered sensitive geometry with opacity, zoom thresholds, or client filters;
7. register unreviewed plugins, protocols, workers, CDN scripts, globals, or custom layers;
8. allow a second renderer or direct consumer import as a temporary shortcut;
9. treat a hit-test, style match, successful render, screenshot, or performance result as truth or publication;
10. silently coerce `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` into an empty-success state;
11. write registry, catalog, receipt, proof, release, or published state;
12. publish from a watcher, test, pull request, merge, or deployment event.

### Allowed effect classes after admission

Only bounded, auditable effects are eligible:

- renderer lifecycle and cleanup;
- applying approved public-safe source/layer/style projections;
- KFM-owned camera/time/visibility operations;
- bounded selection translation;
- allowlisted protocol/plugin registration;
- non-sensitive performance and health telemetry;
- deterministic removal, cache invalidation, and rollback behavior.

[Back to top](#top)

---

## 11. Negative states (first-class)

### 11.1 Current selection bridge states

| Code | UI outcome | Meaning |
|---|---|---|
| `SUPPORTED` and other accepted drawer codes | `ANSWER` or bounded drawer outcome | Resolver returned valid evidence within clicked scope |
| `MISSING_EVIDENCE` | `ABSTAIN` | Selection has no governed evidence ref |
| `SELECTION_INVALID` | `ERROR` | Candidate shape is invalid |
| `DRAWER_EVIDENCE_OUTSIDE_SELECTION` | `ERROR` | Resolver attempted to widen evidence scope |
| `GOVERNED_RESOLVER_ERROR` | `ERROR` | Resolver failed; fixed no-leak copy is used |
| policy-sensitive drawer reason codes | `DENY` | Restricted detail is not exposed |

### 11.2 Current layer-admission states

| Outcome | Meaning | Side effect |
|---|---|---|
| `PASS` | Synthetic manifest is eligible for a later step | None |
| `HOLD` | Review, freshness, promotion, rollback, or related closure remains incomplete | None |
| `DENY` | Policy, lifecycle, evidence, release, or integrity posture blocks use | None |
| `ERROR` | Input or evaluator failure prevents a safe decision | None |

### 11.3 Future runtime states

A real port/adapter should expose finite KFM-owned states such as `UNINITIALIZED`, `INITIALIZING`, `READY`, `HELD`, `DENIED`, `DEGRADED`, `ERROR`, and `DISPOSED`, with stable reason codes. Exact vocabulary belongs to an accepted contract, not this page.

A renderer failure must never silently switch to a peer renderer, load an ungoverned source, or weaken evidence/policy requirements. A fake/null port is an explicit development and rollback implementation, not an invisible production fallback.

### 11.4 Non-equivalence table

| Observed result | Does not prove |
|---|---|
| Schema or descriptor `PASS` | Rights, sensitivity, policy, release, or public safety |
| Layer admission `PASS` | Registry mutation, renderer source creation, deployment, or publication |
| Evidence Drawer `ANSWER` fixture | Live EvidenceBundle resolution or released public claim |
| MapLibre import boundary `PASS` | Dependency integrity, browser readiness, or accepted ADR |
| Browser smoke `PASS` | Evidence closure, release approval, or production health |
| Pull request or merge | Promotion, release, deployment, or publication |

[Back to top](#top)

---

## 12. Validation & tests

### 12.1 Current executable proof surfaces

| Surface | What it proves | What it does not prove |
|---|---|---|
| [`map-evidence-drawer.test.ts`](../../../apps/explorer-web/tests/map-evidence-drawer.test.ts) | Strict selection parsing, evidence subset, finite fixture outcomes, no-leak behavior | Renderer, network, live API, release, deployment |
| [`map-evidence-drawer.spec.ts`](../../../apps/explorer-web/tests/browser/map-evidence-drawer.spec.ts) | Keyboard/browser interaction over synthetic fixture | MapLibre integration or production accessibility |
| `layer-manifest-admission.test.ts` | Deterministic fixture admission outcomes and no side effects | Active registry or renderer loading |
| [`test_explorer_web_adapter_boundary.py`](../../../tests/policy/test_explorer_web_adapter_boundary.py) | Bounded app import rule and no internal-store path literals | Exact package importer or complete acquisition modes |
| [`test_assess_acquisition_inventory.py`](../../../tests/maplibre/test_assess_acquisition_inventory.py) | Structural acquisition scanner cases | Accepted seam, admitted dependency, or runtime proof |
| issue #2906 probe plan | Separate authenticated browser/readiness gate | Architecture acceptance, release, or publication |

### 12.2 Focused commands for affected implementation work

These are repository-native targets to run in a later implementation PR; listing them here is not a claim that this documentation edit executed them:

```bash
pnpm --dir apps/explorer-web test -- map-evidence-drawer.test.ts layer-manifest-admission.test.ts
pnpm --dir apps/explorer-web test:browser -- map-evidence-drawer.spec.ts
python -m unittest tests.maplibre.test_assess_acquisition_inventory
python -m pytest tests/policy/test_explorer_web_adapter_boundary.py
python tools/validators/maplibre/assess_acquisition_inventory.py --repo-root .
```

The acquisition inventory may intentionally return `HOLD` while renderer acquisition exists without accepted architecture/admission closure. A green `HOLD` workflow must not be misreported as runtime admission.

### 12.3 Graduation ladder

| Gate | Required evidence | Current state |
|---|---|---|
| G0 — renderer-neutral selection | Strict shape, subset guard, finite drawer outcomes, keyboard fixture | **CONFIRMED / bounded** |
| G1 — fixture layer admission | Deterministic positive/negative cases and no-side-effect result | **CONFIRMED / bounded** |
| G2 — architecture decision | Reviewed ADR-0006/0007 source and index disposition | **OPEN** |
| G3 — exact acquisition seam | One exact importer plus complete negative fixtures/validator | **HOLD** |
| G4 — KFM-owned port | Public types, fake/null adapter, consumer compile/tests without MapLibre | **NOT IMPLEMENTED** |
| G5 — dependency admission | Exact version, lockfile, integrity, license, supply-chain, CSP/worker, removal review | **NOT ADMITTED** |
| G6 — concrete adapter | Package-owned lifecycle, layer, event, protocol/plugin, cleanup tests | **BLOCKED** |
| G7 — authenticated runtime proof | #2906 exact-head browser and long-session packet | **BLOCKED** |
| G8 — governed vertical slice | Released public-safe layer → port → click → EvidenceBundle → drawer; negative cases | **NOT ESTABLISHED** |
| G9 — operational release | Deployment, observability, incident, correction, rollback, public probe, review | **UNKNOWN / not established** |

### 12.4 Acceptance rule

No lower gate implies a higher one. In particular, fixture success, ADR direction, dependency admission, browser readiness, deployment, and publication remain distinct evidence transitions.

[Back to top](#top)

---

## 13. Rollback path

### 13.1 Documentation rollback

Revert the reviewed documentation commit or restore prior blob `baf929fdca617ea95ea4ce5bde4c7b8abd9ac6d5`, then rerun metadata, Markdown, anchor, relative-link, and generated-receipt checks. No runtime, source, data, cache, release, or public correction is required for this documentation-only change.

### 13.2 Runtime rollback baseline

Until later gates close, the safe runtime rollback baseline remains:

- dependency-free private `@kfm/maplibre` `0.0.0` scaffold;
- no functioning concrete adapter;
- renderer-neutral selection and fixture-only admission tests;
- fake/null port target for consumer compilation;
- no live MapLibre source, released layer, or public deployment.

A later implementation PR must record exact dependency and lockfile removal, consumer behavior without MapLibre, protocol/worker/listener cleanup, cache invalidation, and restoration commands.

### 13.3 Correction versus rollback

Renderer rollback addresses technical execution. It does not replace correction, withdrawal, or supersession of a released claim or artifact. Public correction lineage must propagate through governed manifests, APIs, caches, map layers, Evidence Drawer, Focus Mode, search, exports, and any other released carrier.

[Back to top](#top)

---

## 14. Related docs

### Architecture and doctrine

- [UI architecture index](./README.md)
- [UI boundaries](./BOUNDARIES.md)
- [State ownership](./STATE_OWNERSHIP.md)
- [UI layering](./LAYERING.md)
- [Route map](./ROUTE_MAP.md)
- [Continuity notes](./CONTINUITY_NOTES.md)
- [Map shell](../map-shell.md)
- [MapLibre master architecture](../maplibre-master.md)
- [Governed API architecture](../governed-api.md)
- [Directory Rules](../../doctrine/directory-rules.md)

### Decisions and coordination

- [ADR index](../../adr/INDEX.md)
- [ADR-0006 — proposed adapter/acquisition boundary](../../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md)
- [ADR-0007 — proposed sole browser renderer](<../../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>)
- [ADR-0029 — accepted Directory Rules v2](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Issue #2957 — decision packet and maintainer direction](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2957)
- [Issue #2906 — browser/runtime evidence HOLD](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2906)

### Current implementation evidence

- [Renderer-neutral map selection bridge](../../../apps/explorer-web/src/features/map_runtime/index.tsx)
- [Click-to-evidence boundary note](../../../apps/explorer-web/src/features/map_runtime/CLICK_EVIDENCE_BRIDGE.md)
- [Fixture-only layer admission](../../../apps/explorer-web/src/features/map_runtime/layer_manifest_admission.ts)
- [Explorer adapter stub](../../../apps/explorer-web/src/adapters/MapLibreAdapter.ts)
- [MapLibre package manifest](../../../packages/maplibre/package.json)
- [MapLibre package placeholder](../../../packages/maplibre/src/index.ts)
- [Acquisition inventory](../../../tools/validators/maplibre/assess_acquisition_inventory.py)

[Back to top](#top)

---

## 15. Open questions & verification backlog

| Priority | Question | Current status | Closure evidence |
|---|---|---|---|
| P0 | Will ADR-0006/0007 be revised and accepted with the #2957 physical-seam direction? | **OPEN** | Reviewed source ADR and index transition |
| P0 | What exact package source module is the sole approved renderer importer? | **NEEDS VERIFICATION** | Accepted ADR, implementation, exact-import validator |
| P0 | What happens to the current Explorer `MapLibreAdapter.ts` stub? | **OPEN** | Reviewed remove/rename/renderer-neutral composition change |
| P0 | Can acquisition enforcement cover re-exports, plugins/custom layers, workers, protocols, globals/CDNs, manifests, and lockfile ownership? | **HOLD** | Complete fixtures, validator, CI, exception register |
| P0 | Which exact MapLibre version and closure pass integrity, license, supply-chain, CSP/worker, browser, and rollback review? | **NOT ADMITTED** | Separate dependency-admission packet |
| P1 | What is the normative `MapRuntimePort` semantic contract and machine shape, if any? | **OPEN** | Contract/schema placement decision and tests |
| P1 | Which governed API route/DTO owns live selection resolution? | **NOT IMPLEMENTED** | Route, schema, policy, EvidenceBundle, release, negative tests |
| P1 | How do camera, time, layer, URL, and correction-aware cache keys compose? | **PROPOSED** | Port and shell integration tests |
| P1 | How does one released public-safe layer bind artifact, evidence, policy, review, correction, and rollback? | **NEEDS VERIFICATION** | No-network vertical fixture and closure proof |
| P1 | Do #2906 authenticated probes pass for an admitted exact head? | **BLOCKED** | Exact-head probe packet |
| P2 | Which plugins, protocols, overlays, and custom layers are allowed? | **OPEN** | Admission registry, security/license review, negative tests |
| P2 | What offline/cache behavior preserves withdrawal, supersession, correction, and rollback? | **OPEN** | Cache tests and rollback/correction drill |
| P2 | What accessible non-map alternative covers keyboard, screen reader, zoom, and reduced motion? | **NEEDS VERIFICATION** | Human and automated accessibility evidence |
| P2 | Is mobile/native parity in this boundary or a separate architecture? | **OPEN** | Scoped decision |
| P2 | What deployment, CSP, CORS, telemetry, SLO, incident, and public-probe evidence is required? | **UNKNOWN** | Operational architecture and measured evidence |

Do not silently resolve these questions in an implementation PR. Use the owning ADR, issue, contract/schema, validator, dependency-admission record, or release decision.

[Back to top](#top)

---

## Appendix A — Method-signature sketch (illustrative)

> [!NOTE]
> **Illustrative target only.** No concrete interface or source path is established by this appendix. The accepted contract and implementation must be derived from reviewed ADRs, current package structure, and the smallest proof-bearing slice.

```ts
// PROPOSED shape only — not the current repository API.
export interface MapRuntimePort {
  initialize(host: HTMLElement, options: PublicSafeRuntimeOptions): Promise<RuntimeResult>;
  dispose(): Promise<void>;

  applyView(view: MapViewState): Promise<RuntimeResult>;
  applyTimeContext(time: GovernedTimeContext): Promise<RuntimeResult>;

  admitLayer(layer: GovernedLayerProjection): Promise<RuntimeResult>;
  removeLayer(layerId: string): Promise<RuntimeResult>;
  setLayerVisibility(layerId: string, visible: boolean): Promise<RuntimeResult>;

  onSelection(listener: (selection: MapFeatureSelection) => void): Unsubscribe;
  onRuntimeState(listener: (state: SafeRuntimeState) => void): Unsubscribe;
}
```

The already-implemented `MapFeatureSelection` profile is the downstream compatibility target for future renderer event translation.

[Back to top](#top)

---

## Appendix B — Anti-patterns this boundary forbids

| Anti-pattern | Why it is unsafe or misleading | Required replacement |
|---|---|---|
| Turn the Explorer comment-only adapter into the direct importer | Creates a second physical authority contrary to #2957 direction | Package-owned exact importer; app composes KFM-owned API |
| Import `maplibre-gl` from feature code | Leaks renderer types and defeats rollback/enforcement | Depend on `MapRuntimePort` and KFM-owned types |
| Put renderer dependency in Explorer or root | Splits acquisition and dependency ownership | Reviewed package-owned dependency admission |
| Treat every file under `packages/maplibre/` as an approved importer | Makes the single-importer rule unenforceable | One exact implementation module and complete inventory |
| Show raw `feature.properties` as an answer | Turns renderer payload into a claim | Strict selection → governed resolution → Evidence Drawer |
| Widen selection with geometry or arbitrary fields | Can leak sensitive data and expand request scope | Public-safe identity plus bounded EvidenceRefs only |
| Assume a proposed route exists | Converts documentation into fake runtime evidence | Verify route, DTO, schema, policy, evidence, and tests |
| Treat layer-admission `PASS` as source creation or release | Collapses evaluation, mutation, release, and publication | Keep eligibility, registration, release, deployment distinct |
| Hide restricted locations through client styling | Sensitive bytes may already be delivered | Deny/generalize before artifact release |
| Let adapter compute policy or freshness | Splits authority and makes state non-reproducible | Reflect upstream governed decisions |
| Register arbitrary plugins, protocols, workers, or CDN paths | Bypasses dependency and security admission | One allowlisted package seam with integrity/CSP/rollback review |
| Fall back to another renderer | Silently creates peer-renderer architecture | Finite failure or accepted fake/null path |
| Treat successful render or probe as public truth | Rendering is downstream technical evidence only | Require evidence, policy, review, release, correction, rollback |
| Accept ADRs through this page | Architecture prose cannot create decision authority | Update reviewed ADR source and canonical index together |
| Publish from a watcher, test, PR, merge, or deployment | Collapses implementation and governed publication | Separate promotion/release/publication transition |

[Back to top](#top)

---

**Last updated:** `2026-08-19` · **Version:** `v2.0` · **Status:** `repository-grounded draft / renderer HOLD / no publication authority`

[Back to top](#top)
