<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0007-maplibre-sole-browser-renderer
title: "ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer"
type: adr
adr_id: ADR-0007
version: v1.1
status: legacy-proposed
effective_decision_status: proposed
owners:
  - "OWNER_TBD — architecture stewardship assignment is not verified"
reviewers_required:
  - Architecture steward
  - Map/runtime steward
  - Security and supply-chain reviewer
  - Explorer Web subsystem owner
  - Docs steward
created: 2026-05-10
updated: 2026-07-23
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
current_path: "docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
supersedes:
  - "KFM-P2-FEAT-0012 — proposed dual-renderer planning posture; non-ADR lineage only"
superseded_by: null
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 9ab50d9a94e36320b12b1deb9035ea5a3d315815
  target_prior_blob: c753f09db18e12081f99405b42cd79ebb89d0ac3
  adr_index_blob: cf08fae322ac53426f7394d97897fdb942253049
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  adr_0006_blob: 2e40267d80a474dc53ceda81e5bbf9fce3939149
  maplibre_architecture_blob: ff4b4754e5dc7beae22620ee669d3fdc240c44d7
  packages_root_blob: 154e1c9a8b841397bceb52e6b4933b241906ab9a
  package_readme_blob: 3ba48e7d61b013a659ed51b9336eee788d06b8f2
  package_metadata_blob: b0582955feeb51016327113692fa5c98ecad8816
  package_entry_blob: 91664eb00583f9e3d0405eb7954fefa9a48f4ee9
  root_package_blob: 62f45306aef7376a2d68042b0c9e7f556edf0e78
  smoke_harness_blob: 699dd4cf42d355dd2ed7620852b7fd1f3000bbe2
  app_boundary_test_blob: 97d44069b0a5ab4a82b1e1fc48665e905c08a287
  maplibre_workflow_blob: bfb36a84ba72bec68d964976dc7964cde7f5d603
  external_research_checked: 2026-07-23
  upstream_maplibre_latest_release: v6.0.0
  upstream_maplibre_latest_release_date: 2026-07-22
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md
  - docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/maplibre.md
  - docs/architecture/map-shell.md
  - docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - packages/README.md
  - packages/maplibre/README.md
  - packages/maplibre/package.json
  - packages/maplibre/src/index.ts
  - scripts/maplibre-smoke-perf.mjs
  - tests/policy/test_explorer_web_adapter_boundary.py
  - .github/workflows/maplibre-perf-governance.yml
tags: [kfm, adr, maplibre, browser-renderer, renderer-boundary, plugin-admission, 3d, globe, terrain, supply-chain, no-parallel-authority]
notes:
  - "v1.1 is a same-path, documentation-only, repository-grounded modernization; it does not accept the ADR or change runtime behavior."
  - "ADR-0007 numbering and the exact tracked path are confirmed by docs/adr/INDEX.md; source metadata remains legacy-proposed and effective decision status remains proposed."
  - "The current repository contains a private @kfm/maplibre 0.0.0 scaffold with a placeholder export, not a functioning renderer adapter or an accepted MapLibre version."
  - "Current upstream MapLibre GL JS is v6.0.0, while the repository smoke harness still loads v5.5.0 from a public CDN; this is version and acquisition drift, not an implementation decision."
  - "packages/cesium/ and packages/maplibre-runtime/ were absent at checked main paths; absence does not prove repository-wide conformance or acceptance."
  - "The previously referenced docs/architecture/maplibre-3d.md path was absent at the checked main ref; docs/architecture/maplibre.md currently overstates the sole-renderer posture relative to this proposed ADR."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer

> **Proposed decision.** KFM will use MapLibre GL JS as its default and sole browser-side renderer family. Native MapLibre capabilities and explicitly admitted plugins or custom-layer integrations may operate behind the governed MapLibre adapter seam. A second peer renderer requires a separately accepted, scoped exception ADR with dependency, policy, evidence, release, correction, and rollback treatment.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#1)
[![Repository: scaffold](https://img.shields.io/badge/repository-renderer__scaffold-6e7781?style=flat-square)](#22-current-repository-evidence)
[![Upstream: v6.0.0](https://img.shields.io/badge/upstream-MapLibre%20v6.0.0-1f6feb?style=flat-square)](#23-current-upstream-snapshot)
[![Enforcement: incomplete](https://img.shields.io/badge/enforcement-incomplete-b42318?style=flat-square)](#81-current-enforcement-snapshot)

> [!IMPORTANT]
> **Repository configuration is not reviewed decision authority.** The tree contains MapLibre-oriented doctrine, a private package scaffold, an app-local boundary test, a CDN-based performance harness, and a readiness workflow. Those surfaces neither accept this ADR nor prove that a sole-renderer architecture, plugin admission system, package dependency boundary, or released browser runtime is implemented.

**Quick navigation:** [Status](#1) · [Context](#2) · [Decision](#3) · [Evidence](#4) · [Directory Rules](#5) · [Consequences](#6) · [Alternatives](#7) · [Validation](#8) · [Rollback](#9) · [Open work](#10) · [Migration](#11) · [Truth summary](#12) · [No-loss ledger](#appendix-a--no-loss-modernization-ledger)

---

<a id="1"></a>

## 1. Status

### 1.1 Decision and document state

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0007` — unique and confirmed in the canonical human [`INDEX.md`](./INDEX.md) |
| **Tracked path** | `docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md` |
| **Source metadata** | `legacy-proposed` |
| **Effective decision status** | `proposed` — the repository index explicitly states that no numbered ADR is accepted at its recorded snapshot |
| **Created** | 2026-05-10 |
| **Updated** | 2026-07-23 |
| **Decision scope** | Browser-side renderer-family selection and additional-renderer exception governance |
| **Related seam decision** | [`ADR-0006`](./ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) — where renderer dependencies may be acquired or imported |
| **Publication effect** | None. A Markdown edit, package scaffold, test, performance run, pull request, or upstream release does not publish KFM data or accept this ADR. |

### 1.2 Current implementation posture

| Concern | Status | Safe conclusion |
|---|---|---|
| ADR number and filename | **CONFIRMED** | The exact record is indexed as ADR-0007. The old numbering-conflict question is closed. |
| Sole-renderer decision | **PROPOSED** | The record exists but is not accepted. |
| Current renderer package | **CONFIRMED scaffold** | [`packages/maplibre/package.json`](../../packages/maplibre/package.json) declares private package `@kfm/maplibre` version `0.0.0`. |
| Package implementation | **NOT ESTABLISHED** | [`packages/maplibre/src/index.ts`](../../packages/maplibre/src/index.ts) exports only `placeholder = true`. |
| Package-home doctrine | **CONFLICTED** | Current implementation evidence uses `packages/maplibre/`; Directory Rules proposes `packages/maplibre-runtime/`. Do not create both as active peers. |
| MapLibre version decision | **UNRESOLVED** | The repository does not pin MapLibre in the package scaffold. The root smoke harness loads `5.5.0`, while upstream released `6.0.0` on 2026-07-22. |
| Cesium package at checked path | **ABSENT AT CHECKED PATH** | `packages/cesium/` was not found on `main`; this is not a complete import/dependency inventory. |
| Renderer-family enforcement | **PARTIAL / INCOMPLETE** | Existing testing is app-local and import-text based; no repository-wide peer-renderer validator is established. |
| Current released browser runtime | **UNKNOWN** | No accepted package pin, lockfile, build output, deployed app, released layer flow, or production log proves browser runtime behavior. |

### 1.3 Acceptance gates

ADR-0007 SHOULD NOT move to `accepted` until equivalent evidence closes every applicable gate.

| Gate | Required evidence | Fail-closed result when missing |
|---|---|---|
| **A — Decision and index coherence** | Reviewed status transition in this ADR and matching canonical ADR index entry | Remain `proposed` |
| **B — Renderer vocabulary** | A reviewed definition of `renderer`, `plugin`, `custom-layer integration`, `protocol`, and `peer renderer` | Treat ambiguous technologies as unadmitted |
| **C — One physical adapter home** | Resolution of `packages/maplibre/` versus `packages/maplibre-runtime/`, with migration and compatibility posture | Do not create a second active package |
| **D — Version and distribution decision** | Accepted MapLibre major/version range, package manager, lockfile, ESM/CSP/worker strategy, browser support matrix, and rollback | Do not claim buildability or support |
| **E — Complete dependency inventory** | Recursive inventory of package manifests, imports, dynamic acquisition, workers, CDN scripts, globals, plugins, custom layers, examples, and tests | Treat sole-renderer conformance as unproven |
| **F — Plugin and integration admission** | Per-dependency license, provenance, version, supply-chain, capability, policy, test, and removal evidence | DENY plugin/integration use |
| **G — Structural enforcement** | Repository-wide deterministic validator, positive/negative fixtures, tests, and CI invocation | Direct review remains insufficient |
| **H — Governed runtime proof** | At least one consumer builds through the accepted adapter and demonstrates released-input, negative-state, evidence, policy, correction, and rollback behavior | Hold operational acceptance |
| **I — Documentation reconciliation** | Architecture lane, package docs, ADR-0006, test docs, and drift/backlog records agree with the accepted status and physical package home | Keep conflicting docs visibly proposed |
| **J — Human review** | Required reviewers approve and acceptance evidence is recorded | Remain `proposed` |

[Back to top](#top)

---

<a id="2"></a>

## 2. Context

### 2.1 The problem this ADR addresses

KFM needs one explicit answer to this question:

> **Which browser renderer family is the normal governed path, and what burden applies before another renderer can enter that path?**

Without a decision, a repository can accumulate multiple browser rendering SDKs, duplicated adapters, parallel camera and interaction models, multiple plugin/supply-chain inventories, and divergent release behavior. That fragmentation is especially risky for KFM because rendered surfaces are downstream carriers of evidence, policy, sensitivity transforms, review state, release state, correction lineage, and rollback—not independent truth systems.

The decision is intentionally narrower than a complete MapLibre implementation:

- It selects a renderer family.
- It defines what counts as part of that family.
- It defines the burden for a peer renderer or exception.
- It does **not** admit a specific plugin, package version, endpoint, layer, dataset, or public release.

### 2.2 Current repository evidence

The prior revision treated most implementation details as unknown. Current evidence allows a more precise statement.

| Surface | Confirmed state | Boundary |
|---|---|---|
| [`docs/adr/INDEX.md`](./INDEX.md) | ADR-0007 is indexed at the exact current filename; effective status `proposed`, source metadata `legacy-proposed` | Inventory is not acceptance |
| [`ADR-0006`](./ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) | Repository-grounded proposed import/acquisition seam | Does not choose or implement the renderer family |
| [`packages/README.md`](../../packages/README.md) | Confirms `packages/maplibre/` scaffold and checked absence of `packages/cesium/` and `packages/maplibre-runtime/`; records path conflict | Bounded inventory, not exhaustive conformance |
| [`packages/maplibre/README.md`](../../packages/maplibre/README.md) | Describes a private scaffold, unresolved dependency/API/distribution posture, and no functioning adapter | Documentation is not implementation |
| [`packages/maplibre/package.json`](../../packages/maplibre/package.json) | `@kfm/maplibre`, private, `0.0.0`; no dependencies or scripts | No accepted MapLibre pin or build |
| [`packages/maplibre/src/index.ts`](../../packages/maplibre/src/index.ts) | Placeholder export only | No renderer implementation |
| [`package.json`](../../package.json) | Root lint/test/build are `echo TODO`; MapLibre performance commands live at repository root | Command presence is not package or release proof |
| [`scripts/maplibre-smoke-perf.mjs`](../../scripts/maplibre-smoke-perf.mjs) | Loads `maplibre-gl@5.5.0` from UNPKG and uses the global runtime | Known test-harness divergence from the proposed package seam and current upstream v6 |
| [`test_explorer_web_adapter_boundary.py`](../../tests/policy/test_explorer_web_adapter_boundary.py) | Scans Explorer Web only and permits MapLibre/Cesium imports anywhere under app-local `adapters/` | Does not enforce a sole renderer or package-only seam repo-wide |
| [`maplibre-perf-governance.yml`](../../.github/workflows/maplibre-perf-governance.yml) | No-network syntax/negative checks plus an explicit HOLD on browser performance, proof, release, correction, and rollback claims | Not a renderer-family conformance gate |
| [`docs/architecture/maplibre.md`](../architecture/maplibre.md) | Declares MapLibre sole renderer and Cesium retired while this ADR remains proposed; references missing `docs/architecture/maplibre-3d.md` | **CONFLICTED documentation posture** requiring reconciliation, not silent promotion |

### 2.3 Current upstream snapshot

Current external research changes the baseline’s version framing:

- MapLibre GL JS **v6.0.0** is the latest upstream release as of 2026-07-23 and was released on 2026-07-22.
- v6 is **ESM-only**, removes the v5 UMD and separate CSP bundles, requires WebGL2, changes import and worker-handling expectations, and carries other breaking API changes.
- The official MapLibre examples still demonstrate terrain, globe, custom layers, three.js models, and a 3D Tiles custom-layer integration.
- The official plugins page lists integrations for deck.gl, three.js, LiDAR, COG, PMTiles, vector-text protocols, contours, and other extensions.

These facts support the availability of capability families. They do **not** establish KFM compatibility, package admission, license clearance, performance fitness, accessibility, sensitivity safety, evidence parity, or release readiness.

### 2.4 Terminology

| Term | Meaning in this ADR |
|---|---|
| **MapLibre GL JS** | The selected browser renderer library family. A major-version pin is a separate implementation decision. |
| **Adapter seam** | The accepted package boundary implementing KFM-owned map runtime ports; governed by ADR-0006. |
| **Native capability** | Functionality supplied by the accepted MapLibre package version without a third-party renderer integration. |
| **Plugin / protocol** | A separately versioned dependency extending MapLibre sources, controls, protocols, or layer behavior. |
| **Custom-layer integration** | A library such as three.js or Babylon.js hosted inside MapLibre’s custom-layer lifecycle. |
| **Peer renderer** | A browser rendering SDK with its own primary map/scene lifecycle, camera, event, source/layer model, or public rendering authority parallel to MapLibre. |
| **Admitted renderer set** | MapLibre plus explicitly approved plugins and custom-layer integrations. A documentation mention is not admission. |

### 2.5 Scope

**In scope**

- Browser-side map and scene renderer-family selection.
- 2D, 2.5D, terrain, globe, custom-layer, 3D Tiles, glTF, point-cloud, and visualization-overlay paths.
- Additional-renderer and plugin admission burden.
- Dependency, version, supply-chain, policy, test, documentation, migration, and rollback expectations.
- Relationship to ADR-0006, Explorer Web, the package boundary, and public released artifacts.

**Out of scope**

- Selecting the accepted MapLibre major or exact version.
- Admitting any specific plugin/version.
- Authoring plugin contracts, schemas, Rego, validators, fixtures, or package code.
- Declaring mobile/MapLibre Native support.
- Declaring any layer, scene, point cloud, plugin, package, app, release, or public dataset operational.
- Solving subsurface volumetric stratigraphy or every future visualization requirement.
- Accepting this ADR through a documentation-only pull request.

[Back to top](#top)

---

<a id="3"></a>

## 3. Decision

### 3.1 Sole browser-renderer rule

If accepted:

> **MapLibre GL JS is KFM’s default and sole browser-side renderer family.** Browser map and scene behavior in the normal governed path runs through the accepted MapLibre adapter seam. Native capabilities and admitted plugins or custom-layer integrations remain subordinate to that seam. A peer renderer is denied unless a separately accepted exception ADR authorizes a precisely bounded use case.

“Sole” means:

- one normal browser map/scene lifecycle;
- one KFM-owned port and adapter family;
- one accepted primary camera and interaction model;
- one renderer dependency and supply-chain boundary;
- one plugin/integration admission process;
- one release-manifest renderer vocabulary;
- no unreviewed peer renderer hidden in an app, package, test, example, CDN script, worker, custom element, or plugin wrapper.

“Sole” does **not** mean:

- every capability must be native;
- every plugin is automatically allowed;
- MapLibre is truth, evidence, policy, review, release, or publication authority;
- the renderer can fetch canonical/internal or unreleased stores;
- an accepted ADR can be replaced by a README assertion or package scaffold.

### 3.2 Relationship to ADR-0006

| ADR | Question answered |
|---|---|
| **ADR-0006** | Where may renderer runtime dependencies be acquired, imported, initialized, and exposed? |
| **ADR-0007** | Which renderer family is the normal browser path, what belongs inside its admitted set, and how is a peer renderer governed? |

Acceptance and implementation are independent:

- Accepting ADR-0007 would not prove ADR-0006 is implemented.
- Implementing an adapter seam would not accept ADR-0007.
- A test-only harness can be a bounded exception to ADR-0006 without becoming a peer renderer under ADR-0007, but the exception must be explicit and reviewed.
- A plugin can remain inside the MapLibre renderer set while still requiring separate admission and supply-chain evidence.

### 3.3 Version independence and current v6 pressure

This ADR selects the **MapLibre GL JS family**, not a permanent major version.

An implementation decision MUST separately record:

- accepted major/version range and update policy;
- package manager and lockfile;
- ESM, worker, CSP, bundler, and asset-loading posture;
- WebGL2/browser support matrix;
- relevant breaking changes and migration tests;
- plugin compatibility matrix;
- deterministic build and rollback target;
- license and supply-chain evidence;
- public-network and self-hosting posture.

The current repository does not satisfy that burden. The package scaffold has no dependency pin, while the smoke harness still acquires v5.5.0 from a public CDN and upstream has released v6.0.0.

### 3.4 Admitted plugins and custom-layer integrations

A plugin or custom-layer library is inside the renderer set only after a reviewed admission record establishes:

1. package identity, version, source, maintainer, and license;
2. role: source/protocol, control, native-style extension, custom layer, scene integration, analysis overlay, or test-only tool;
3. why native MapLibre capability is insufficient;
4. contract and manifest effects;
5. policy and sensitivity effects;
6. network, worker, CSP, asset, and endpoint behavior;
7. supply-chain evidence and lockfile closure;
8. positive, negative, performance, accessibility, and rollback tests;
9. allowed consumers and runtime state;
10. expiry/review date and removal path.

The official plugin catalog or an upstream example is discovery evidence—not KFM admission.

### 3.5 Additional-renderer exception path

A peer renderer MAY enter only through a separately accepted exception ADR that:

1. names a specific use case, dataset class, audience, and allowed environment;
2. proves the accepted MapLibre and admitted-plugin paths cannot satisfy the use case;
3. defines the peer renderer’s lifecycle, camera, interaction, event, source/layer, evidence, policy, and release boundaries;
4. identifies exact dependencies, editions, versions, licenses, endpoints, workers, and assets;
5. attaches supply-chain and vulnerability evidence;
6. defines source-role, evidence, rights, sensitivity, review, and release obligations;
7. preserves KFM-owned identity and finite negative states;
8. proves no normal public path reads RAW, WORK, QUARANTINE, canonical/internal stores, or direct model output;
9. defines telemetry, correction, cache invalidation, withdrawal, and rollback;
10. remains scoped—an exception does not become the default renderer by implication.

### 3.6 Default-deny behavior

Until a dependency or peer renderer is admitted:

- package introduction is denied;
- direct/imported/CDN/worker acquisition is denied outside an approved bounded test exception;
- public release manifests cannot claim it;
- production runtime paths cannot load it;
- docs must label it `PROPOSED`, `NEEDS VERIFICATION`, or `DENIED`, not implemented;
- passing visual output cannot substitute for evidence, policy, review, or release state.

[Back to top](#top)

---

<a id="4"></a>

## 4. Evidence basis

### 4.1 Repository evidence

Repository evidence supports only the bounded implementation conclusions in §2.2:

- the ADR number/path and proposed status are confirmed;
- a private MapLibre package scaffold exists;
- the scaffold has no renderer dependency or functional adapter;
- the checked Cesium and `maplibre-runtime` package paths are absent;
- a root CDN harness uses MapLibre 5.5.0;
- an app-local import test mentions MapLibre and Cesium;
- a readiness workflow explicitly holds browser-runtime and trust-object claims;
- the architecture lane currently overstates the renderer decision relative to the canonical ADR index.

No inspected repository artifact proves a complete renderer inventory, accepted version, admitted plugin set, buildable package, consumer migration, released browser runtime, or production sole-renderer behavior.

### 4.2 Attached doctrine and lineage

The attached KFM corpus supports the governing posture that:

- renderers are downstream carriers, not truth authorities;
- public clients use governed APIs and released artifacts;
- 2D/2.5D/3D representations preserve evidence identity and reality-boundary labels;
- sensitive geometry is transformed upstream, not hidden by style;
- plugins and additional runtimes require policy, supply-chain, validation, review, release, correction, and rollback;
- the prior dual-renderer idea is lineage that may be superseded by a reviewed ADR rather than deleted.

The corpus does not prove current repository implementation or acceptance.

### 4.3 Authoritative external evidence

The external snapshot is limited to official primary sources:

- MapLibre GL JS releases and the v5-to-v6 migration guide;
- MapLibre GL JS official examples and API documentation;
- the MapLibre-maintained plugins catalog.

External evidence answers “what the upstream project exposes.” It does not answer “what KFM has admitted, implemented, tested, or released.”

### 4.4 Capability map

| Capability family | Upstream evidence | KFM status under this ADR |
|---|---|---|
| 2D vector and raster rendering | Core MapLibre GL JS and Style Specification | Selected renderer-family capability; implementation not established |
| Terrain mesh | `raster-dem` plus `setTerrain` | Native upstream capability; KFM version/data/release tests required |
| Hillshade | `hillshade` layer | Native upstream capability; context layer is not evidence by itself |
| Globe, sky, atmosphere | Projection and style APIs | Native upstream capability; KFM view-state and evidence-parity tests required |
| 2.5D extrusion | `fill-extrusion` | Native upstream capability; must be labeled 2.5D, not true 3D |
| Camera and cinematic state | Map camera APIs | Native upstream capability; KFM-owned serializable state required |
| Custom WebGL layers | Custom layer lifecycle | Native extension seam; every integration separately admitted |
| 3D Tiles | Official three.js + `3d-tiles-renderer` example | Integration capability; not admitted or production-proven |
| glTF models | Official three.js examples and plugin catalog | Integration capability; not admitted |
| Point clouds / EPT | Plugin catalog entries | Plugin capability; not admitted |
| deck.gl overlays | Plugin catalog / integration documentation | Overlay capability; not a peer renderer when admitted inside MapLibre |
| COG | `maplibre-cog-protocol` in plugin catalog | Protocol capability; not admitted |
| PMTiles | PMTiles protocol integration in plugin catalog/examples | Protocol capability; not admitted |
| Vector-text protocols | Plugin catalog | Protocol capability; not admitted |
| Contours | Plugin catalog | Plugin capability; not admitted |
| Babylon.js custom scenes | Official examples | Integration capability; not admitted |
| Subsurface volumetric stratigraphy | No accepted KFM implementation evidence | `UNKNOWN`; not promised by this ADR |

### 4.5 Evidence limits

This ADR does not claim:

- current performance or accessibility;
- compatibility between upstream v6 and any plugin;
- a current license inventory for all plugins;
- production suitability at Kansas, county, or focus-mode scale;
- complete browser/device support;
- package-manager or lockfile availability;
- current CI success;
- deployment or public release.

[Back to top](#top)

---

<a id="5"></a>

## 5. Directory Rules basis

### 5.1 Why this belongs under `docs/adr/`

Directory Rules place human-facing decisions under `docs/adr/`. Renderer-family selection changes a cross-cutting implementation and governance commitment, affects package/dependency direction, and constrains future peer-renderer paths. That burden requires an ADR rather than an architecture note or package README.

The target path is confirmed by the canonical ADR index; this revision does not rename it.

### 5.2 Responsibility-root routing

| Responsibility | Owning root | ADR-0007 relationship |
|---|---|---|
| Decision record | `docs/adr/` | This document |
| Architecture explanation | `docs/architecture/` | Explains the accepted/proposed renderer posture; cannot accept it |
| Reusable adapter implementation | `packages/` | Physical home must be resolved without parallel packages |
| Browser shell | `apps/explorer-web/` | Consumer of KFM-owned port; not renderer authority |
| Semantic meaning | `contracts/` | Plugin/admission/manifest meaning |
| Machine shape | `schemas/` | Admission and manifest schemas |
| Admissibility | `policy/` | Plugin, renderer, sensitivity, rights, release decisions |
| Validation | `tools/validators/` | Reusable deterministic checks |
| Enforceability | `tests/` and fixtures | Positive/negative proof |
| Release decisions | `release/` | Promotion, correction, withdrawal, rollback |
| Lifecycle artifacts | `data/` | Receipts/proofs/published artifacts; not defined by this ADR |

### 5.3 Current path conflict

Directory Rules propose `packages/maplibre-runtime/`, while the repository contains `packages/maplibre/`. That conflict is not resolved by this ADR and MUST NOT be “fixed” by creating a second active package.

Resolution requires a reviewed migration or a later placement decision that:

- selects one canonical implementation home;
- inventories consumers and backlinks;
- records compatibility treatment;
- prevents independent evolution;
- updates tests/workflows/docs atomically;
- preserves rollback.

### 5.4 No new authority roots

This documentation-only revision:

- creates no root;
- changes no lifecycle phase;
- creates no schema, contract, policy, test, fixture, validator, package, workflow, data, proof, receipt, or release object;
- does not promote a compatibility root;
- does not accept the renderer decision.

[Back to top](#top)

---

<a id="6"></a>

## 6. Consequences

### 6.1 Positive consequences if accepted

- **One normal rendering lifecycle.** Camera, selection, time, layer, and negative-state behavior have one primary browser seam.
- **Lower authority fragmentation.** Fewer opportunities for parallel contracts, schemas, policies, release fields, or evidence handling.
- **Centralized dependency governance.** Renderer and plugin acquisition can be inspected at one package boundary.
- **Clearer tests.** A peer renderer, unadmitted plugin, direct CDN runtime, or raw renderer type has a deterministic review outcome.
- **Renderer replacement remains possible.** A successor ADR can replace MapLibre, and a scoped exception ADR can admit a bounded peer without silently changing the default.
- **AI and UI remain subordinate.** Renderer capability does not elevate map pixels, feature properties, scenes, or generated descriptions into proof.

### 6.2 Costs and accepted tradeoffs

- **Adapter and admission burden.** New capabilities require KFM-owned types, contracts, policy, fixtures, and tests rather than direct SDK use.
- **Plugin maturity risk.** Some integrations may be less mature than peer-renderer equivalents.
- **Version migration burden.** Upstream v6 introduces real breaking changes; the repository must not treat a v5 CDN harness as a current implementation plan.
- **Reduced convenience for experiments.** Direct renderer imports and browser globals require a bounded test exception instead of ad hoc use.
- **Potential capability gap.** A future use case may require a peer renderer; the exception ADR deliberately makes that decision costly and reviewable.
- **Documentation reconciliation work.** Existing docs currently state stronger sole-renderer conclusions than the proposed ADR status supports.

### 6.3 Unchanged KFM invariants

This ADR never relaxes:

- `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`;
- public-client use of governed interfaces and released artifacts;
- cite-or-abstain;
- EvidenceRef-to-EvidenceBundle resolution for consequential claims;
- upstream sensitivity transformation;
- 2D/2.5D/3D reality-boundary labeling;
- correction, withdrawal, and rollback;
- AI as interpretive rather than authoritative;
- release review and separation of duties.

[Back to top](#top)

---

<a id="7"></a>

## 7. Alternatives considered

| Alternative | Disposition | Reason |
|---|---|---|
| **A — Preserve an explicit MapLibre + Cesium dual-renderer default** | Rejected by the proposed decision | Duplicates lifecycle, dependency, camera, event, supply-chain, policy, release, and testing burdens; repository evidence does not establish a functional need or implementation. |
| **B — Let each feature select a renderer** | Rejected | Recreates ambient authority and makes conformance impossible to reason about repo-wide. |
| **C — Use deck.gl as the primary renderer** | Rejected | deck.gl can be an admitted MapLibre overlay, but a second primary lifecycle would fragment the normal path. |
| **D — Use three.js or Babylon.js as the primary renderer** | Rejected | Those libraries may be custom-layer integrations; making either primary would create a separate scene lifecycle and governance surface. |
| **E — Keep MapLibre as de facto default without an ADR** | Rejected | Convention cannot resolve prior dual-renderer lineage, package boundaries, exception burden, or future peer-renderer admission. |
| **F — Ban all third-party rendering integrations** | Rejected | Native capability alone may not cover 3D Tiles, point clouds, or specialized overlays; explicit admission is safer than hidden workarounds. |
| **G — Accept the ADR immediately because no Cesium package was found** | Rejected | Absence at checked paths is bounded evidence, not acceptance, complete inventory, runtime proof, or policy enforcement. |
| **H — Defer all documentation until a functional package exists** | Rejected | The decision and acceptance gates should guide implementation, but documentation must remain visibly proposed. |
| **I — Select a permanent MapLibre major in this ADR** | Rejected | Renderer-family selection should outlive one upstream major; version adoption belongs to implementation/package governance. |

[Back to top](#top)

---

<a id="8"></a>

## 8. Validation

### 8.1 Current enforcement snapshot

| Surface | Confirmed state | Boundary |
|---|---|---|
| ADR index validator | Canonical ADR inventory and status normalization exist | Does not accept the ADR |
| ADR-0006 | Proposed import/acquisition seam with repository evidence | Does not establish a functional renderer or sole-renderer rule |
| Explorer Web boundary test | Scans app source and confines “maplibre”/“cesium” import lines to app-local adapters | Does not scan packages, scripts, workers, HTML/CDN, manifests, globals, or peer SDKs |
| Package manifests | MapLibre scaffold has no dependencies; root package has performance tooling dependencies only | No accepted renderer dependency or lockfile |
| Smoke harness | Direct CDN acquisition of MapLibre 5.5.0 | Known version/acquisition divergence |
| MapLibre readiness workflow | Static syntax/negative checks and explicit HOLD | No browser performance, proof, release, correction, or renderer-family conformance |
| Architecture lane | States sole renderer and Cesium retired | Conflicts with proposed ADR status and missing companion path |
| Cesium checked package path | Not found | Not a complete repository inventory |

### 8.2 Required validation classes before acceptance

| Class | Minimum evidence |
|---|---|
| **Inventory** | Recursive file/import/manifest/worker/CDN/global/plugin/custom-layer scan with machine-readable results |
| **Package boundary** | Accepted physical home, dependency pin, lockfile, exports, build, browser matrix, CSP/worker policy, consumer map |
| **Renderer-family classification** | Finite vocabulary and classifier for native capability, plugin, protocol, custom-layer integration, test-only harness, and peer renderer |
| **Negative tests** | Non-adapter import, unadmitted peer renderer, unadmitted plugin, CDN acquisition, worker acquisition, raw type leakage, missing exception ADR |
| **Positive tests** | Accepted adapter imports MapLibre; admitted integration passes; test-only exception remains bounded; consumer uses KFM-owned port |
| **Governed runtime** | Released manifest input, evidence lookup, policy negative states, correction/withdrawal, rollback, accessibility, telemetry |
| **Supply chain** | License, provenance, lockfile, vulnerability posture, SBOM/attestation where required, deterministic rollback |
| **Documentation** | ADR/index/package/architecture/tests/workflow docs agree and use correct truth labels |

### 8.3 Proposed checks

The following names are **PROPOSED** until an existing equivalent is found or the path is reviewed under Directory Rules:

- `tools/validators/validate_renderer_family_boundary.*`
- `tests/governance/test_renderer_family_boundary.*`
- `tests/governance/test_renderer_exception_adr.*`
- `tests/packages/maplibre/test_public_types_do_not_leak_renderer.*`
- `tests/packages/maplibre/test_plugin_admission.*`

A proposed path is not implementation proof. Reuse existing validator/test homes when equivalent behavior exists.

### 8.4 Scoped commands

Run from repository root on the proposed revision:

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
python -m pytest tests/policy/test_explorer_web_adapter_boundary.py -q
node --check scripts/maplibre-smoke-perf.mjs
```

When the package and dependency strategy becomes real, add repository-native locked install, build, typecheck, unit, browser, and no-network commands. Do not invent them while root scripts remain placeholders.

### 8.5 Reviewer checklist

- [ ] Is ADR-0007 still represented as `proposed` unless human acceptance evidence exists?
- [ ] Does the change preserve ADR-0006’s distinct import/acquisition question?
- [ ] Is one physical adapter package home selected without creating a parallel sibling?
- [ ] Is the MapLibre major/version decision explicit and tested?
- [ ] Are v6 ESM, worker, CSP, WebGL2, and breaking-change implications addressed?
- [ ] Does every plugin/integration have an admission record and removal path?
- [ ] Does the inventory include imports, manifests, workers, CDN scripts, globals, examples, and tests?
- [ ] Are renderer outputs still downstream of evidence, policy, review, release, correction, and rollback?
- [ ] Are sensitive geometry and restricted data transformed upstream?
- [ ] Are architecture docs corrected so they do not state a proposed decision as accepted doctrine?
- [ ] Can a peer renderer be denied deterministically without hiding an unsafe fallback?

[Back to top](#top)

---

<a id="9"></a>

## 9. Rollback

### 9.1 Document rollback

If this modernization is inaccurate, restore prior blob:

`c753f09db18e12081f99405b42cd79ebb89d0ac3`

or revert the eventual implementation commit. The ADR remains in history; do not delete it.

### 9.2 Rollback before acceptance

Before acceptance, rollback means:

- leave the decision `proposed`;
- close or abandon implementation branches through normal review controls;
- retain the current package scaffold unless a separate reviewed change removes it;
- preserve conflicting evidence and backlog records rather than rewriting history.

### 9.3 Scoped exception after acceptance

A scoped exception does not automatically supersede ADR-0007. The exception ADR:

- forward-links from this record;
- names its exact scope;
- preserves MapLibre as the normal path;
- records dependency and release consequences;
- contains a removal/rollback target.

### 9.4 Full reversal after acceptance

A future default-path peer or replacement renderer requires a superseding ADR that:

- marks ADR-0007 `superseded` and links forward;
- updates the canonical ADR index;
- inventories contracts, schemas, policy, fixtures, tests, packages, apps, workflows, docs, receipts, proofs, and releases;
- supplies old-to-new compatibility and migration maps;
- preserves released-artifact correction, withdrawal, and rollback;
- does not rewrite or delete this decision history.

### 9.5 Runtime rollback

Runtime rollback, if implementation later exists, must be governed through package/release controls:

1. restore the last accepted package/version and lockfile;
2. restore the last accepted manifest and adapter behavior;
3. withdraw incompatible public artifacts where required;
4. invalidate caches and derived outputs through release procedures;
5. emit correction/rollback evidence appropriate to the affected scope.

[Back to top](#top)

---

<a id="10"></a>

## 10. Open questions

The ADR number and tracked path are no longer open questions. Current open work is implementation, versioning, documentation reconciliation, and acceptance.

### OQ-A7-01 — Physical package home (`CONFLICTED`)

Which path becomes the accepted adapter package: current `packages/maplibre/` or proposed `packages/maplibre-runtime/`? Resolve through one reviewed migration; do not create both as independent authorities.

### OQ-A7-02 — Accepted MapLibre version (`NEEDS VERIFICATION`)

Upstream is now v6.0.0, the root harness still loads v5.5.0, and the package scaffold pins nothing. Decide version range, lockfile, ESM/CSP/worker strategy, browser/WebGL2 support, plugin compatibility, migration tests, and rollback.

### OQ-A7-03 — Complete renderer/dependency inventory (`NEEDS VERIFICATION`)

Bounded search and checked paths do not establish a recursive inventory. Scan all manifests, source files, workers, HTML templates, scripts, examples, test harnesses, generated assets, CDN references, globals, and branches relevant to release.

### OQ-A7-04 — Companion architecture document (`CONFLICTED`)

`docs/architecture/maplibre.md` references `docs/architecture/maplibre-3d.md`, but the checked path is absent and the lane entry point states the sole-renderer decision more strongly than the ADR index permits. Decide whether to create, consolidate, or redirect that companion in a separately authorized documentation packet.

### OQ-A7-05 — Plugin and custom-layer admission contract (`OPEN`)

Define the finite object and status vocabulary for plugin/integration admission, including source, version, license, role, capabilities, policy effects, tests, review date, and removal path.

### OQ-A7-06 — Test-only runtime acquisition (`OPEN`)

Determine whether the root CDN smoke harness is migrated behind the adapter, replaced with a locked local package path, or retained as a tightly bounded test exception. The current v5.5.0 global runtime must not be mistaken for the accepted package or current upstream.

### OQ-A7-07 — Peer-renderer classifier (`OPEN`)

Define how KFM distinguishes a plugin/overlay from a peer renderer. Camera ownership, map/scene lifecycle, source/layer model, event system, worker/runtime ownership, and direct public rendering authority are candidate dimensions.

### OQ-A7-08 — Existing Cesium lineage (`NEEDS VERIFICATION`)

No `packages/cesium/` path was found, but docs and tests still mention Cesium. Inventory any contracts, schemas, policy, examples, fixtures, generated artifacts, or historical release references before claiming retirement is complete.

### OQ-A7-09 — Mobile and native (`UNKNOWN`)

This ADR governs the browser. Decide separately whether MapLibre Native shares object contracts, manifests, plugin admission, evidence parity, and release controls without turning platform parity into an implied browser exception.

### OQ-A7-10 — Subsurface volumetric representation (`UNKNOWN`)

No production-quality KFM browser implementation is established. Keep reality-boundary labels and do not infer physical truth from 2.5D or scene reconstruction.

Track implementation questions in [`VERIFICATION_BACKLOG.md`](../registers/VERIFICATION_BACKLOG.md) and confirmed structural/documentation conflicts in [`DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md).

[Back to top](#top)

---

<a id="11"></a>

## 11. Migration plan

The migration is staged. This documentation-only revision performs none of the implementation steps below.

| # | Step | Required result |
|---|---|---|
| 1 | Preserve ADR-0007 as proposed and reconcile its evidence snapshot | No status promotion by documentation edit |
| 2 | Inventory renderer and integration dependencies repo-wide | Machine-readable current-state report with bounded exclusions |
| 3 | Resolve `packages/maplibre/` versus `packages/maplibre-runtime/` | One canonical home, compatibility/migration map, rollback |
| 4 | Decide the accepted MapLibre version and package strategy | Lockfile, ESM/worker/CSP/browser posture, build and rollback |
| 5 | Define renderer/plugin vocabulary and admission record | Finite statuses and reason codes |
| 6 | Classify current dependencies, scripts, examples, docs, and tests | Canonical, admitted, test-only exception, transitional, deprecated, conflicting |
| 7 | Implement or complete ADR-0006 adapter seam | KFM-owned port/types; no raw renderer leakage |
| 8 | Migrate at least one real consumer | Build/test through accepted adapter only |
| 9 | Add structural validator and positive/negative tests | Deterministic repository-wide enforcement |
| 10 | Reconcile architecture/package/test/workflow docs | No proposed decision stated as accepted |
| 11 | Prove a governed runtime slice | Released input, evidence lookup, finite policy state, correction, rollback |
| 12 | Review ADR-0007 for acceptance | ADR and index transition together with human evidence |

Every migration step is reversible, and no step treats generated output, successful rendering, or a passing import test as release or truth authority.

[Back to top](#top)

---

<a id="12"></a>

## 12. Truth-label summary

| Claim | Status |
|---|---|
| ADR-0007 number and exact path | **CONFIRMED** |
| Effective decision status | **CONFIRMED `proposed`** |
| Current `@kfm/maplibre` package scaffold | **CONFIRMED** |
| Functional adapter or accepted consumer | **NOT ESTABLISHED / UNKNOWN** |
| `packages/cesium/` at checked path | **CONFIRMED absent at checked path** |
| Complete absence of Cesium or peer renderer references | **UNKNOWN** |
| Current upstream MapLibre release v6.0.0 on 2026-07-22 | **CONFIRMED external fact** |
| Accepted KFM MapLibre version | **UNKNOWN / NEEDS VERIFICATION** |
| Current harness acquisition of MapLibre 5.5.0 | **CONFIRMED repository evidence** |
| Complete renderer-family enforcement | **NOT ESTABLISHED** |
| MapLibre capability families in upstream docs/examples | **CONFIRMED external capability evidence** |
| KFM plugin admission, performance fitness, accessibility, public safety, or release readiness | **PROPOSED / UNKNOWN** |
| Subsurface volumetric browser rendering | **UNKNOWN** |
| This revision accepts or publishes anything | **False** |

> [!CAUTION]
> **A sole-renderer policy is not proof of a renderer.** Until the package, dependency, adapter, consumer, validation, policy, and release gates are real, ADR-0007 remains a proposed governance decision over a scaffolded implementation surface.

[Back to top](#top)

---

## References

### Repository evidence

- [Canonical ADR index](./INDEX.md)
- [ADR-0006 — MapLibre import/acquisition boundary](./ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md)
- [Directory Rules](../doctrine/directory-rules.md)
- [MapLibre architecture lane](../architecture/maplibre.md)
- [Map shell architecture](../architecture/map-shell.md)
- [Map runtime boundary](../architecture/ui/MAP_RUNTIME_BOUNDARY.md)
- [Packages root](../../packages/README.md)
- [MapLibre package boundary](../../packages/maplibre/README.md)
- [MapLibre package metadata](../../packages/maplibre/package.json)
- [MapLibre placeholder entry point](../../packages/maplibre/src/index.ts)
- [Root package commands](../../package.json)
- [MapLibre smoke harness](../../scripts/maplibre-smoke-perf.mjs)
- [Explorer Web adapter-boundary test](../../tests/policy/test_explorer_web_adapter_boundary.py)
- [MapLibre readiness workflow](../../.github/workflows/maplibre-perf-governance.yml)
- [MapLibre test-lane README](../../tests/maplibre/README.md)

### Authoritative external sources

- [MapLibre GL JS releases](https://github.com/maplibre/maplibre-gl-js/releases)
- [MapLibre GL JS v5-to-v6 migration guide](https://github.com/maplibre/maplibre-gl-js/blob/v6.0.0/docs/guides/v5-to-v6-migration-guide.md)
- [MapLibre GL JS documentation](https://maplibre.org/maplibre-gl-js/docs/)
- [MapLibre GL JS examples](https://maplibre.org/maplibre-gl-js/docs/examples/)
- [MapLibre GL JS plugins catalog](https://maplibre.org/maplibre-gl-js/docs/plugins/)
- [Official 3D Tiles using three.js example](https://maplibre.org/maplibre-gl-js/docs/examples/add-3d-tiles-using-threejs/)

The external links document upstream capabilities and migration facts. They are not KFM dependency approval, plugin admission, or release evidence.

---

<a id="appendix-a--no-loss-modernization-ledger"></a>

<details>
<summary><strong>Appendix A — No-loss modernization ledger</strong></summary>

| Baseline element | v1.1 disposition |
|---|---|
| ADR identity, H1, `ADR-0007`, and exact tracked filename | Preserved |
| Proposed sole-renderer decision | Preserved and made version-independent |
| Prior dual-renderer lineage / `KFM-P2-FEAT-0012` | Preserved as non-ADR lineage; no claim that repository register updates are complete |
| MapLibre capability matrix | Preserved, reorganized, and truth-bounded as upstream capability evidence rather than KFM admission |
| Plugin admission concept | Preserved and expanded into a finite evidence burden |
| Default-deny on peer renderers | Preserved and clarified |
| Exception-ADR path | Preserved and expanded |
| Directory Rules rationale | Preserved and reconciled with current path evidence |
| Positive and negative consequences | Preserved and updated for v6/version drift |
| Alternatives A–E | Preserved in substance; expanded to nine alternatives |
| Contract/schema/policy/validator/build test ideas | Preserved as proposed validation classes and paths |
| Additive exception and full-supersession rollback | Preserved |
| OQ-A7 numbering conflict | Closed using canonical ADR index evidence |
| Plugin licensing, pre-existing artifacts, subsurface, Category W, receipt-shape questions | Preserved and reorganized into current open questions |
| Migration plan | Preserved and grounded in current package/version/documentation conflicts |
| Truth-label summary | Preserved and made repository-specific |
| Badge strip | Reduced to four evidence-bearing orientation badges; no CI badge claim |
| Placeholder owner/spec hash | Replaced with visible `OWNER_TBD` and no invented hash |
| Missing `maplibre-3d.md` reference | Preserved as a documented conflict, not silently treated as present |

</details>

<a id="appendix-b--beforeafter-upgrade-matrix"></a>

<details>
<summary><strong>Appendix B — Before/after upgrade matrix</strong></summary>

| Area | Before | After |
|---|---|---|
| ADR slot/path | Marked as needing live-set verification | Confirmed through canonical index |
| Repository posture | Broadly unknown | Package scaffold, placeholder implementation, root harness, partial test, readiness workflow, and documentation conflict are pinned |
| Upstream version | Framed around MapLibre 5.x | Current v6.0.0 and v5-to-v6 migration pressure recorded; KFM pin remains unresolved |
| Renderer decision | Conflated capability availability with sufficiency | Separates renderer-family selection, upstream capability, KFM admission, and implementation proof |
| Plugin model | Named plugin set with illustrative future paths | Admission record burden, classifier, expiry, removal, network, accessibility, supply-chain, and negative tests |
| Package placement | Assumed `packages/maplibre-runtime/` | Records conflict with current `packages/maplibre/`; forbids active siblings |
| Enforcement | Mostly proposed per-file checks | Adds complete acquisition/dependency inventory and repository-wide classifier expectations |
| Companion docs | Assumed `maplibre-3d.md` exists | Records missing path and overstatement in current lane entry point |
| Rollback | General additive exception | Exact prior blob plus pre-acceptance, exception, full-reversal, and runtime rollback |
| Presentation | Ten badges, stale placeholder CI badge | Four bounded badges, stable quick navigation, alerts, tables, and appendices |

</details>

---

_Last updated 2026-07-23 · Source metadata: `legacy-proposed` · Effective decision status: `proposed` · Implementation maturity: renderer scaffold / enforcement incomplete · [Back to top](#top)_
