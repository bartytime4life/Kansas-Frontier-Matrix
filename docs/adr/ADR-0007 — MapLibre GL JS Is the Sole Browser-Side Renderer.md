<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0007-maplibre-sole-browser-renderer
title: "ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer"
type: adr
adr_id: ADR-0007
version: v1.2
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
updated: 2026-08-13
policy_label: public
truth_posture: cite-or-abstain
owning_root: docs/
responsibility_root: docs/
current_path: "docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
responsibility: "Record the proposed browser renderer-family decision, its admission and exception boundaries, acceptance evidence, migration obligations, and rollback without granting implementation, release, or publication authority."
supersedes:
  - "KFM-P2-FEAT-0012 — proposed dual-renderer planning posture; non-ADR lineage only"
superseded_by: null
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 59143eaeb7b92884b5f97621a15ef04a30a8da8e
  base_tree: 4d278ccf65877884071495238d4e8de008f61c17
  docs_adr_tree: 3942461775b80b959e2b2fb2ff749dad003eafa2
  target_prior_blob: d1efbbec4b245037f884d2b614f6d6693d7162cb
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  adr_readme_blob: b497be1714b88550d2f1eb151bc20a6351e99dec
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: 3ba5f902ffe20a65a259cb0a7dab07f1725d204b
  adr_0006_blob: 2e40267d80a474dc53ceda81e5bbf9fce3939149
  maplibre_architecture_blob: ff4b4754e5dc7beae22620ee669d3fdc240c44d7
  packages_root_blob: 7b672f4d834b648f4b30ce7e2e9a5e214efa2c71
  package_readme_blob: 3ba48e7d61b013a659ed51b9336eee788d06b8f2
  package_metadata_blob: b0582955feeb51016327113692fa5c98ecad8816
  package_entry_blob: 91664eb00583f9e3d0405eb7954fefa9a48f4ee9
  app_adapter_blob: 663ba0f7a05498948f67d644387c73ab19d5c16c
  app_package_blob: ddd201b74a06001d84a14bf54ac62a6cc3607a29
  root_package_blob: 5cba790c88c40b885cc65fe2d585f3205aa1ef9d
  pnpm_lock_blob: 69a45e6aaca1ea6521e01ff274e4f1b3e1bf3975
  smoke_harness_blob: 699dd4cf42d355dd2ed7620852b7fd1f3000bbe2
  app_boundary_test_blob: 97d44069b0a5ab4a82b1e1fc48665e905c08a287
  maplibre_workflow_blob: 306040e1c9283be5a95de76c09d205a58038f380
  schemas_maplibre_readme_blob: 9560ed016077964b56988d7fb4c02fe34e42fb28
  briefing_campaign_blob: 7a73f5ad044a4e496d8e897b160e9b5c79e1dd94
  v6_readiness_validator_blob: 88bc8bcfb894eaa7871e53d130a93a2e0258be49
  v6_readiness_test_blob: 2e0b6a4b9fe237e13bde9a09f057bcdb6a03a066
  v6_readiness_fixture_blob: 1bf82ae6c8966be3b1baf01620bf8f4deb7be95b
  latest_applicable_maplibre_run_head: 9205823798b19f37ba7c4dc2761850584948b027
  latest_applicable_maplibre_run: "31759518767 — success with explicit WORKFLOW_HOLD"
  latest_applicable_maplibre_job: "94642665467"
  external_research_checked: 2026-08-13
  upstream_maplibre_latest_release: v6.0.0
  upstream_maplibre_latest_release_date: 2026-07-22
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md
  - docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/maplibre.md
  - docs/architecture/map-shell.md
  - docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - packages/README.md
  - packages/maplibre/README.md
  - packages/maplibre/package.json
  - packages/maplibre/src/index.ts
  - apps/explorer-web/src/adapters/MapLibreAdapter.ts
  - apps/explorer-web/package.json
  - pnpm-lock.yaml
  - scripts/maplibre-smoke-perf.mjs
  - schemas/maplibre/README.md
  - tests/policy/test_explorer_web_adapter_boundary.py
  - tests/maplibre/test_validate_v6_readiness.py
  - fixtures/maplibre/v6_readiness/cases.json
  - tools/validators/maplibre/validate_v6_readiness.py
  - .github/workflows/maplibre-perf-governance.yml
  - .github/workflows/briefing-implementation-campaign.yml
tags: [kfm, adr, maplibre, browser-renderer, renderer-boundary, plugin-admission, v6-readiness, workflow-hold, 3d, globe, terrain, supply-chain, no-parallel-authority]
notes:
  - "v1.2 is a same-path, documentation-only, repository-grounded reconciliation; it does not accept ADR-0007, admit a dependency or plugin, or change runtime behavior."
  - "ADR-0029 is accepted and adopts Directory Rules v2; ADR-0007 remains legacy-proposed and effectively proposed among the other 33 proposed numbered records."
  - "The private @kfm/maplibre 0.0.0 package, its placeholder export, and the comment-only Explorer adapter remain dependency-free and non-functional even though the pnpm workspace and Explorer build/test scripts now exist."
  - "The deterministic v6-readiness lane is implemented and fixture-tested, but the current-tree scan returns HOLD because MapLibre is unpinned and all six browser probes remain NOT_RUN."
  - "The latest applicable MapLibre performance job concluded success while explicitly recording WORKFLOW_HOLD; it ran no dependency install, browser, server, receipt, proof, release, correction, rollback, or artifact-upload stage."
  - "Current upstream MapLibre GL JS remains v6.0.0, while the smoke harness still loads v5.5.0 from a public CDN; this is version and acquisition drift, not an implementation decision."
  - "packages/cesium/, packages/maplibre-runtime/, docs/architecture/maplibre-3d.md, and configs/maplibre/v6-probe-results.json were absent at the pinned tree; bounded absence is not acceptance or complete conformance."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer

> **Proposed decision.** KFM will use MapLibre GL JS as its default and sole browser-side renderer family. Native MapLibre capabilities and explicitly admitted plugins or custom-layer integrations may operate behind the governed MapLibre adapter seam. A second peer renderer requires a separately accepted, scoped exception ADR with dependency, policy, evidence, release, correction, and rollback treatment.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#1)
[![Repository: scaffold + hold](https://img.shields.io/badge/repository-scaffold_%2B_readiness__hold-6e7781?style=flat-square)](#22-current-repository-evidence)
[![Upstream: v6.0.0](https://img.shields.io/badge/upstream-MapLibre%20v6.0.0-1f6feb?style=flat-square)](#23-current-upstream-snapshot)
[![Enforcement: bounded](https://img.shields.io/badge/enforcement-bounded_%2B_incomplete-b42318?style=flat-square)](#81-current-enforcement-snapshot)

> [!IMPORTANT]
> **Repository configuration is not reviewed decision authority.** The tree contains MapLibre-oriented doctrine, a dependency-free package scaffold, a comment-only Explorer adapter, bounded import and v6-readiness checks, a live-CDN performance harness, eight permissive performance schemas, and workflows that intentionally hold runtime claims. Those surfaces neither accept this ADR nor prove a sole-renderer implementation, admitted plugin set, functioning adapter, browser execution, release, or publication.

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
| **Effective decision status** | `proposed` — the current index has 34 numbered records; ADR-0029 alone is accepted and the other 33, including ADR-0007, remain proposed |
| **Created** | 2026-05-10 |
| **Updated** | 2026-08-13 |
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
| Explorer adapter | **CONFIRMED placeholder** | [`MapLibreAdapter.ts`](../../apps/explorer-web/src/adapters/MapLibreAdapter.ts) contains one boundary comment and no implementation. |
| Package-home decision | **OPEN / lineage conflicted** | The repository uses `packages/maplibre/`; supplied design lineage proposes `packages/maplibre-runtime/`. Accepted Directory Rules select `packages/` as the responsibility root but do not select this product-lane name. Do not create both as active peers. |
| Workspace/toolchain | **CONFIRMED bounded** | Root `package.json` pins `pnpm@11.17.0`, Node 22, and `apps/*`/`packages/*`; a workspace lock exists. Root aggregate lint/test/build fail closed with `WORKFLOW_HOLD`. Explorer has real Vite, TypeScript, Vitest, and Playwright scripts but no MapLibre dependency. |
| MapLibre version decision | **UNRESOLVED** | The repository does not pin MapLibre in the package scaffold. The root smoke harness loads `5.5.0`, while upstream released `6.0.0` on 2026-07-22. |
| Cesium package at checked path | **ABSENT AT CHECKED PATH** | `packages/cesium/` was not found on `main`; this is not a complete import/dependency inventory. |
| v6 readiness classifier | **CONFIRMED executable / current HOLD** | The deterministic validator, five fixture cases, seven unit tests, and campaign wiring exist. The current-tree scan returns `HOLD` with `MAPLIBRE_DEPENDENCY_UNPINNED` and `RUNTIME_PROBES_PENDING`; all six browser probes are `NOT_RUN`. |
| Performance-governance workflow | **SUCCESS + EXPLICIT HOLD** | Latest applicable reviewed run `31759518767`, job `94642665467`, passed static and negative checks while recording `WORKFLOW_SKIPPED_EXPLICIT` and `WORKFLOW_HOLD`. No dependency install or browser run occurred. |
| Renderer-family enforcement | **PARTIAL / INCOMPLETE** | The v6 classifier scans the Explorer and package source boundaries for direct `maplibre-gl` imports and internal `map.transform` use. It is not a complete peer-renderer, dynamic-acquisition, plugin, generated-output, or release inventory. |
| Current released browser runtime | **NOT ESTABLISHED** | No accepted MapLibre pin, functional adapter, browser-probe record, build output, released layer flow, deployed app, or production trace proves runtime behavior. |

### 1.3 Acceptance gates

ADR-0007 SHOULD NOT move to `accepted` until equivalent evidence closes every applicable gate.

| Gate | Required evidence | Fail-closed result when missing |
|---|---|---|
| **A — Decision and index coherence** | Reviewed status transition in this ADR and matching canonical ADR index entry | Remain `proposed` |
| **B — Renderer vocabulary** | A reviewed definition of `renderer`, `plugin`, `custom-layer integration`, `protocol`, and `peer renderer` | Treat ambiguous technologies as unadmitted |
| **C — One physical adapter home** | Resolution of current `packages/maplibre/` versus supplied-lineage `packages/maplibre-runtime/`, including API identity, consumers, migration, compatibility, and rollback | Do not create a second active package |
| **D — Version and distribution decision** | Accepted exact initial MapLibre pin and update policy, pinned workspace manager/lock closure, ESM/CSP/worker strategy, browser support matrix, and rollback | Keep the readiness outcome on hold; do not claim buildability or support |
| **E — Complete dependency inventory** | Recursive inventory of package manifests, imports, dynamic acquisition, workers, CDN scripts, globals, plugins, custom layers, examples, and tests | Treat sole-renderer conformance as unproven |
| **F — Plugin and integration admission** | Per-dependency license, provenance, version, supply-chain, capability, policy, test, and removal evidence | DENY plugin/integration use |
| **G — Structural enforcement** | Expansion beyond the bounded v6 classifier to a repository-wide renderer/acquisition validator, positive/negative fixtures, tests, and CI invocation | Direct review and bounded scanning remain insufficient |
| **H — Governed runtime proof** | Reviewed six-probe record plus at least one consumer that builds through the accepted adapter and demonstrates released-input, negative-state, evidence, policy, correction, and rollback behavior | Hold operational acceptance |
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
| [`docs/adr/INDEX.md`](./INDEX.md) | ADR-0007 is indexed at the exact current filename; effective status `proposed`, source metadata `legacy-proposed`; ADR-0029 alone is accepted among 34 numbered records | Inventory is not acceptance; the adjacent ADR README still carries stale 30-record counts |
| [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules](../doctrine/directory-rules.md) | Adopt the exact Directory Rules v2 bytes and confirm `packages/` as the shared-implementation responsibility root | Do not select MapLibre, accept ADR-0007, or name a MapLibre child package |
| [`ADR-0006`](./ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) | Repository-grounded proposed import/acquisition seam | Does not choose or implement the renderer family |
| [`packages/README.md`](../../packages/README.md) | Confirms 21 direct package lanes, the `packages/maplibre/` scaffold, adopted package-root authority, workspace lock posture, and unresolved MapLibre naming/adapter/consumer decisions | Bounded inventory, not exhaustive conformance or an alternate child-name decision |
| [`packages/maplibre/README.md`](../../packages/maplibre/README.md) | Describes a private scaffold, unresolved dependency/API/distribution posture, and no functioning adapter | Documentation is not implementation |
| [`packages/maplibre/package.json`](../../packages/maplibre/package.json) | `@kfm/maplibre`, private, `0.0.0`; no dependencies or scripts | No accepted MapLibre pin or build |
| [`packages/maplibre/src/index.ts`](../../packages/maplibre/src/index.ts) | Placeholder export only | No renderer implementation |
| [`MapLibreAdapter.ts`](../../apps/explorer-web/src/adapters/MapLibreAdapter.ts) | One boundary comment, with no imports, types, exports, initialization, or adapter behavior | No Explorer renderer implementation |
| [`apps/explorer-web/package.json`](../../apps/explorer-web/package.json) | Real Vite/TypeScript/Vitest/Playwright scripts and pinned development dependencies; no `maplibre-gl` dependency | App toolchain presence is not a renderer consumer |
| [`package.json`](../../package.json) and [`pnpm-lock.yaml`](../../pnpm-lock.yaml) | Root pins pnpm and Node, declares app/package workspaces, carries MapLibre QA commands, and fails generic lint/test/build closed with `WORKFLOW_HOLD` | Lock and command presence are dependency-state evidence only; no MapLibre install or aggregate build proof |
| [`scripts/maplibre-smoke-perf.mjs`](../../scripts/maplibre-smoke-perf.mjs) | Loads `maplibre-gl@5.5.0` from UNPKG and uses the global runtime | Known test-harness divergence from the proposed package seam and current upstream v6 |
| [`test_explorer_web_adapter_boundary.py`](../../tests/policy/test_explorer_web_adapter_boundary.py) | Scans Explorer Web import lines and permits MapLibre/Cesium imports anywhere under app-local `adapters/` | Does not enforce a package-only seam, dynamic acquisition, or sole renderer repo-wide |
| [`validate_v6_readiness.py`](../../tools/validators/maplibre/validate_v6_readiness.py), [fixtures](../../fixtures/maplibre/v6_readiness/cases.json), and [tests](../../tests/maplibre/test_validate_v6_readiness.py) | Deterministically classify exact-v6 pinning, ESM/ES2022 posture, direct import boundary, internal `map.transform` use, six finite probe states, and forbidden authority declarations | Current scan is `HOLD`; synthetic `READY` is fixture evidence, not current runtime proof |
| [`briefing-implementation-campaign.yml`](../../.github/workflows/briefing-implementation-campaign.yml) | Runs seven readiness unit tests, five synthetic fixture cases, and asserts the current repository exits `3` with dependency-unpinned and probes-pending reasons | No live dependency upgrade, browser probe, release, deployment, or publication |
| [`schemas/maplibre/README.md`](../../schemas/maplibre/README.md) | Records eight identical accept-any-object performance-schema placeholders and a held migration/readiness boundary | Schema syntax and filenames do not implement renderer governance or trust objects |
| [`maplibre-perf-governance.yml`](../../.github/workflows/maplibre-perf-governance.yml) | No-network syntax/negative/readiness-inventory checks plus an explicit HOLD on browser performance, proof, release, correction, rollback, and artifact claims | Latest applicable job success is not a renderer-family conformance or release gate |
| [`docs/architecture/maplibre.md`](../architecture/maplibre.md) | Declares MapLibre sole renderer and Cesium retired while this ADR remains proposed; references missing `docs/architecture/maplibre-3d.md` | **CONFLICTED documentation posture** requiring reconciliation, not silent promotion |

### 2.3 Current upstream snapshot

Current external research changes the baseline’s version framing:

- MapLibre GL JS **v6.0.0** remains the latest upstream release as of the 2026-08-13 review and was released on 2026-07-22.
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
| **Readiness outcome** | The v6 classifier’s finite `READY`, `HOLD`, or `ERROR` result for its declared inputs. It is validation evidence, not ADR acceptance, plugin admission, release approval, or publication authority. |

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

The current repository does not satisfy that burden. Its deterministic readiness classifier confirms ESM module posture and TypeScript `ES2022`, but the package scaffold has no dependency pin, the smoke harness still acquires v5.5.0 from a public CDN, and the six required v6 browser probes are `NOT_RUN`. The computed result is therefore `HOLD`, not `READY`. Neither a future `READY` classifier result nor an exact version pin would accept this ADR by itself.

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
- ADR-0029 alone is accepted and adopts Directory Rules v2 without selecting a renderer or MapLibre child-package name;
- a private MapLibre package scaffold exists;
- the scaffold and comment-only Explorer adapter have no renderer dependency or functional behavior;
- the root pnpm workspace, lockfile, and Explorer build/test toolchain now exist, while generic root lint/test/build remain explicit holds;
- the checked Cesium and `maplibre-runtime` package paths are absent;
- a root CDN harness uses MapLibre 5.5.0;
- an app-local import test mentions MapLibre and Cesium;
- a deterministic v6-readiness classifier, fixture pack, seven unit tests, and workflow lane exist;
- the current-tree readiness result is `HOLD` because MapLibre is unpinned and the six required browser probes are not recorded;
- eight MapLibre performance schemas remain identical accept-any-object placeholders;
- the latest applicable MapLibre workflow job passed bounded checks while explicitly holding browser-runtime and trust-object claims;
- the architecture lane currently overstates the renderer decision relative to the canonical ADR index.

No inspected repository artifact proves a complete renderer inventory, accepted version, admitted plugin set, functional package/adapter, browser execution, consumer migration, released runtime, or production sole-renderer behavior. A synthetic `READY` fixture proves classifier polarity only.

### 4.2 Attached doctrine and lineage

The supplied KFM corpus supports the governing posture that:

- renderers are downstream carriers, not truth authorities;
- public clients use governed APIs and released artifacts;
- 2D/2.5D/3D representations preserve evidence identity and reality-boundary labels;
- sensitive geometry is transformed upstream, not hidden by style;
- plugins and additional runtimes require policy, supply-chain, validation, review, release, correction, and rollback;
- the prior dual-renderer idea is lineage that may be superseded by a reviewed ADR rather than deleted.

For this revision, the directly reconciled supplied artifacts were:

| Supplied artifact | SHA-256 | Use in this ADR |
|---|---|---|
| `KFM_MapLibre_Operating_Architecture_Governed_UI_AI_Interaction_Manual_REVISED.pdf` | `77f56ec1ab632b76c7728cfb250330271b7dc8948db95c8c0594c92ad9ca6b36` | Renderer-as-downstream-carrier, governed UI/API boundary, dependency/plugin review, finite negative states, and runtime acceptance gates |
| `Master MapLibre Components-Functions-Features.pdf` | `309cf67311059c549e144ae9961b2f49eddf1caab8739a51b47ae88c2f5c1c90` | 2D-first and conditional 3D/globe lineage, renderer interoperability burden, evidence/proof/release separation |
| `maplibre3d.md` | `5148c85acaef7f299864df5b1804eb07498cb81ab4c4bcc39a9625287ee2817b` | Proposed sole-renderer recommendation, plugin/custom-layer admission, 2.5D/3D labels, and the `maplibre-runtime` naming proposal |
| `Unified Implementation Architecture Build Manual.md` | `e92500f9b40007e8b69d183ecaa6247c542ffec25857875ecd2dbd00709785b1` | Responsibility roots, trust membrane, lifecycle, review, and rollback boundaries |
| `Repository Structure Guiding Document.md` | `afe08af316d1f89779bab0d39888cdc65ee989907806a4126c331c50e4a0aa3a` | Placement, package-root, no-parallel-authority, scripts/tooling, and migration guidance |

These are design and lineage evidence. They do not prove current repository implementation, current upstream facts, ADR acceptance, runtime behavior, or release. In particular, the supplied `maplibre3d.md` proposes `packages/maplibre-runtime/`; accepted Directory Rules do not make that child name canonical.

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

The repository contains `packages/maplibre/`. Supplied architecture lineage proposes `packages/maplibre-runtime/`. Accepted Directory Rules establish `packages/` as the reusable-implementation root and explicitly leave renderer selection to architecture decisions; they do **not** choose either child name. The unresolved naming/API/consumer question MUST NOT be “fixed” by creating a second active package.

Resolution requires a reviewed migration or a later placement decision that:

- selects one canonical implementation home and public package/API identity;
- inventories consumers and backlinks;
- records compatibility treatment;
- prevents independent evolution;
- updates tests/workflows/docs atomically;
- preserves rollback.

Until that review, the current `packages/maplibre/` path is the only tracked implementation candidate, while `packages/maplibre-runtime/` remains design lineage and an absent proposed alternative—not a second authority.

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
| **J — Treat a future v6-readiness `READY` result as ADR acceptance** | Rejected | The classifier evaluates finite technical inputs; it cannot supply decision review, plugin admission, governed runtime proof, or an ADR/index status transition. |

[Back to top](#top)

---

<a id="8"></a>

## 8. Validation

### 8.1 Current enforcement snapshot

| Surface | Confirmed state | Boundary |
|---|---|---|
| ADR index validator | Canonical 34-record inventory and status normalization pass on the pinned tree; ADR-0029 alone is accepted | Does not accept or implement ADR-0007; ADR README counts remain stale adjacent documentation |
| ADR-0006 | Proposed import/acquisition seam with repository evidence | Does not establish a functional renderer or sole-renderer rule |
| Explorer Web boundary test | Scans app source and confines “maplibre”/“cesium” import lines to app-local adapters | Does not scan packages, scripts, workers, HTML/CDN, manifests, globals, or peer SDKs |
| v6 readiness classifier | Scans root/Explorer manifests, TS posture, Explorer and package sources, direct `maplibre-gl` imports, internal `map.transform`, and six finite browser-probe fields | Current result is `HOLD`; source scope and finite markers are not a complete peer-renderer or acquisition inventory |
| v6 readiness fixtures/tests | Five synthetic fixture cases and seven deterministic unit tests exercise `READY`, `HOLD`, `ERROR`, exact-version, direct-import, internal-API, probe, and authority-boundary polarity | Synthetic `READY` does not mean the repository or any browser is ready |
| Package manifests and lock | Workspace lock exists; MapLibre package is dependency-free; Explorer has tooling dependencies but no MapLibre dependency | No accepted or installed renderer dependency and no functional adapter |
| Smoke harness | Direct CDN acquisition of MapLibre 5.5.0 | Known version/acquisition divergence |
| MapLibre performance workflow | Latest applicable run `31759518767` succeeded; logs record dependency-free package, live-CDN smoke, eight permissive schemas, placeholder verifiers, unsigned attestation, skipped runtime/trust stages, and `WORKFLOW_HOLD` | No dependency install, browser/server run, screenshot, receipt, attestation, proof, release, correction, rollback, failure bundle, or upload was produced |
| Briefing campaign | Executes readiness unit tests/fixtures and asserts the current `HOLD` reasons and exit `3` | No live dependency upgrade or browser probe |
| Architecture lane | States sole renderer and Cesium retired | Conflicts with proposed ADR status and missing companion path |
| Checked alternative paths | `packages/cesium/`, `packages/maplibre-runtime/`, `docs/architecture/maplibre-3d.md`, and the v6 probe-results manifest are absent | Bounded absence is not a complete repository/branch/release inventory |

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

The implemented `tools/validators/maplibre/validate_v6_readiness.py` lane is the current finite version/readiness classifier. Reuse or deliberately extend it where its contract fits; do not relabel its bounded source scan as full renderer-family enforcement.

The following additional names are **PROPOSED** until an existing equivalent is found or the path is reviewed under Directory Rules:

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
python -m unittest discover \
  --start-directory tests/maplibre \
  --pattern 'test_validate_v6_readiness.py' \
  --verbose
python tools/validators/maplibre/validate_v6_readiness.py --fixtures
```

The current-tree readiness scan is expected to hold rather than pass:

```bash
set +e
output="$(python tools/validators/maplibre/validate_v6_readiness.py --scan-root .)"
code=$?
set -e
printf '%s\n' "$output"
test "$code" -eq 3
python -c 'import json,sys; value=json.loads(sys.argv[1]); assert value["outcome"] == "HOLD"; assert value["reasons"] == ["MAPLIBRE_DEPENDENCY_UNPINNED", "RUNTIME_PROBES_PENDING"]' "$output"
```

When the package and dependency strategy becomes real, use the pinned workspace manager and add repository-native locked install, package/consumer build, typecheck, unit, browser, CSP/worker, accessibility, and no-network commands. Root generic scripts currently fail closed with `WORKFLOW_HOLD`; do not report them as implemented aggregate checks.

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

`d1efbbec4b245037f884d2b614f6d6693d7162cb`

or revert the eventual documentation commit and its paired generated receipt. Blob `c753f09db18e12081f99405b42cd79ebb89d0ac3` remains earlier pre-v1.1 lineage, not the immediate rollback target. The ADR remains in history; do not delete it.

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

### OQ-A7-01 — Physical package home (`OPEN / LINEAGE CONFLICT`)

Which path and public package/API identity become the accepted adapter boundary: current `packages/maplibre/` or supplied-lineage `packages/maplibre-runtime/`? Accepted Directory Rules choose `packages/` as the responsibility root but do not answer this child-name question. Resolve through one reviewed migration; do not create both as independent authorities.

### OQ-A7-02 — Accepted MapLibre version (`NEEDS VERIFICATION`)

Upstream remains v6.0.0, the root harness loads v5.5.0, and the package scaffold pins nothing. The readiness classifier therefore returns `MAPLIBRE_DEPENDENCY_UNPINNED`. Decide an exact initial pin and update policy, ESM/CSP/worker strategy, browser/WebGL2 support, plugin compatibility, migration tests, and rollback.

### OQ-A7-03 — Complete renderer/dependency inventory (`NEEDS VERIFICATION`)

The v6 classifier scans bounded root/Explorer manifests and Explorer/package source files for `maplibre-gl` imports and internal transform access. It does not establish a recursive renderer-family inventory. Expand or pair it with reviewed scanning of all manifests, source files, workers, HTML templates, scripts, examples, test harnesses, generated assets, CDN references, globals, peer SDK identifiers, and release-relevant branches.

### OQ-A7-04 — Companion architecture document (`CONFLICTED`)

`docs/architecture/maplibre.md` references `docs/architecture/maplibre-3d.md`, but the checked path is absent and the lane entry point states the sole-renderer decision more strongly than the ADR index permits. Decide whether to create, consolidate, or redirect that companion in a separately authorized documentation packet.

### OQ-A7-05 — Plugin and custom-layer admission contract (`OPEN`)

Define the finite object and status vocabulary for plugin/integration admission, including source, exact version, license, role, capabilities, CSP/network/worker effects, policy effects, tests, review date, and removal path. The current eight `schemas/maplibre/` files are performance placeholders and do not provide this contract.

### OQ-A7-06 — Test-only runtime acquisition (`OPEN`)

Determine whether the root CDN smoke harness is migrated behind the adapter, replaced with a locked local package path, or retained as a tightly bounded test exception. The performance workflow currently guards this exact live-CDN posture and holds browser execution; that guard is not approval. The v5.5.0 global runtime must not be mistaken for the accepted package or current upstream.

### OQ-A7-07 — Peer-renderer classifier (`OPEN`)

Define how KFM distinguishes a plugin/overlay from a peer renderer. Camera ownership, map/scene lifecycle, source/layer model, event system, worker/runtime ownership, and direct public rendering authority are candidate dimensions.

### OQ-A7-08 — Existing Cesium lineage (`NEEDS VERIFICATION`)

No `packages/cesium/` path was found, but docs and tests still mention Cesium. Inventory any contracts, schemas, policy, examples, fixtures, generated artifacts, or historical release references before claiming retirement is complete.

### OQ-A7-09 — Mobile and native (`UNKNOWN`)

This ADR governs the browser. Decide separately whether MapLibre Native shares object contracts, manifests, plugin admission, evidence parity, and release controls without turning platform parity into an implied browser exception.

### OQ-A7-10 — Subsurface volumetric representation (`UNKNOWN`)

No production-quality KFM browser implementation is established. Keep reality-boundary labels and do not infer physical truth from 2.5D or scene reconstruction.

### OQ-A7-11 — Browser-probe evidence and transition (`HOLD`)

`configs/maplibre/v6-probe-results.json` is absent, so all six required probes are `NOT_RUN`. Define who may produce and review that record; how browser, OS/GPU, WebGL2-failure, CSP/worker, style-spec, GeoJSON, query, pixel-diff, artifact, and reproducibility context is bound; and which decision can transition a result from `HOLD` to implementation readiness. A classifier outcome must not accept this ADR or authorize release.

### OQ-A7-12 — Adjacent documentation drift (`OPEN`)

Reconcile the stale 30-record status in `docs/adr/README.md`, the pre-readiness snapshot in `tests/maplibre/README.md`, and the architecture lane’s accepted-sounding sole-renderer claim without coupling those independent corrections to ADR-0007 acceptance.

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
| 4 | Decide the accepted MapLibre version and package strategy | Exact initial pin, lock closure, ESM/worker/CSP/browser posture, build and rollback |
| 5 | Execute and review the six v6 browser probes | Bound probe-results record with reproducible environment and finite outcomes; no synthetic substitution |
| 6 | Define renderer/plugin vocabulary and admission record | Finite statuses and reason codes; no reuse of permissive performance placeholders |
| 7 | Classify current dependencies, scripts, examples, docs, and tests | Canonical, admitted, test-only exception, transitional, deprecated, conflicting |
| 8 | Implement or complete ADR-0006 adapter seam | KFM-owned port/types; no raw renderer leakage |
| 9 | Migrate at least one real consumer | Locked build/test through accepted adapter only |
| 10 | Expand structural validator and positive/negative tests | Deterministic repository-wide peer-renderer and acquisition enforcement |
| 11 | Reconcile architecture/package/schema/test/workflow docs | No proposed decision stated as accepted; no held lane described as operational |
| 12 | Prove a governed runtime slice | Released input, evidence lookup, finite policy state, correction, rollback |
| 13 | Review ADR-0007 for acceptance | ADR and index transition together with human evidence |

Every migration step is reversible, and no step treats generated output, successful rendering, or a passing import test as release or truth authority.

[Back to top](#top)

---

<a id="12"></a>

## 12. Truth-label summary

| Claim | Status |
|---|---|
| ADR-0007 number and exact path | **CONFIRMED** |
| Effective decision status | **CONFIRMED `proposed`; ADR-0029 alone is accepted among 34 numbered records** |
| Current `@kfm/maplibre` package scaffold | **CONFIRMED** |
| Functional package adapter or accepted consumer | **CONFIRMED absent from inspected package/Explorer surfaces; repository-wide operational state NOT ESTABLISHED** |
| Workspace manager and lockfile | **CONFIRMED pnpm 11.17.0 / Node 22 workspace; dependency state only** |
| `packages/cesium/` at checked path | **CONFIRMED absent at checked path** |
| Complete absence of Cesium or peer renderer references | **UNKNOWN** |
| Current upstream MapLibre release v6.0.0 on 2026-07-22 | **CONFIRMED external fact** |
| Accepted KFM MapLibre version | **UNKNOWN / NEEDS VERIFICATION** |
| Current harness acquisition of MapLibre 5.5.0 | **CONFIRMED repository evidence** |
| Executable v6-readiness classifier, fixtures, tests, and workflow lane | **CONFIRMED bounded implementation** |
| Current-tree v6-readiness outcome | **CONFIRMED `HOLD`: dependency unpinned; six browser probes pending** |
| Synthetic fixture `READY` outcome | **CONFIRMED classifier test only; not current readiness** |
| Latest applicable MapLibre performance job | **CONFIRMED `success` plus explicit `WORKFLOW_HOLD`; runtime/trust stages skipped** |
| Eight MapLibre performance schemas | **CONFIRMED identical accept-any-object placeholders** |
| Complete renderer-family enforcement | **NOT ESTABLISHED** |
| MapLibre capability families in upstream docs/examples | **CONFIRMED external capability evidence** |
| KFM plugin admission, performance fitness, accessibility, public safety, or release readiness | **PROPOSED / UNKNOWN** |
| Subsurface volumetric browser rendering | **UNKNOWN** |
| This revision accepts or publishes anything | **False** |

> [!CAUTION]
> **A sole-renderer policy and a readiness classifier are not proof of a renderer.** Until the package, dependency, adapter, consumer, browser probes, admission, policy, and release gates are real, ADR-0007 remains a proposed governance decision over a scaffolded and explicitly held implementation surface.

[Back to top](#top)

---

## References

### Repository evidence

- [Canonical ADR index](./INDEX.md)
- [ADR-0029 — Adopt Directory Governance Standard v2](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [ADR-0006 — MapLibre import/acquisition boundary](./ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md)
- [Directory Rules](../doctrine/directory-rules.md)
- [MapLibre architecture lane](../architecture/maplibre.md)
- [Map shell architecture](../architecture/map-shell.md)
- [Map runtime boundary](../architecture/ui/MAP_RUNTIME_BOUNDARY.md)
- [Packages root](../../packages/README.md)
- [MapLibre package boundary](../../packages/maplibre/README.md)
- [MapLibre package metadata](../../packages/maplibre/package.json)
- [MapLibre placeholder entry point](../../packages/maplibre/src/index.ts)
- [Explorer MapLibre adapter placeholder](../../apps/explorer-web/src/adapters/MapLibreAdapter.ts)
- [Explorer package metadata](../../apps/explorer-web/package.json)
- [Root package commands](../../package.json)
- [Workspace lockfile](../../pnpm-lock.yaml)
- [MapLibre smoke harness](../../scripts/maplibre-smoke-perf.mjs)
- [MapLibre performance-schema compatibility boundary](../../schemas/maplibre/README.md)
- [Explorer Web adapter-boundary test](../../tests/policy/test_explorer_web_adapter_boundary.py)
- [MapLibre performance-governance workflow](../../.github/workflows/maplibre-perf-governance.yml)
- [MapLibre v6 readiness validator](../../tools/validators/maplibre/validate_v6_readiness.py)
- [MapLibre v6 readiness fixtures](../../fixtures/maplibre/v6_readiness/cases.json)
- [MapLibre v6 readiness tests](../../tests/maplibre/test_validate_v6_readiness.py)
- [Briefing implementation campaign](../../.github/workflows/briefing-implementation-campaign.yml)
- [MapLibre test-lane README](../../tests/maplibre/README.md)

### Authoritative external sources

- [MapLibre GL JS releases](https://github.com/maplibre/maplibre-gl-js/releases)
- [MapLibre GL JS v5-to-v6 migration guide](https://github.com/maplibre/maplibre-gl-js/blob/v6.0.0/docs/guides/v5-to-v6-migration-guide.md)
- [MapLibre GL JS documentation](https://maplibre.org/maplibre-gl-js/docs/)
- [MapLibre GL JS examples](https://maplibre.org/maplibre-gl-js/docs/examples/)
- [MapLibre GL JS plugins catalog](https://maplibre.org/maplibre-gl-js/docs/plugins/)
- [Official 3D Tiles using three.js example](https://maplibre.org/maplibre-gl-js/docs/examples/add-3d-tiles-using-threejs/)

The external links document upstream capabilities and migration facts. They are not KFM dependency approval, plugin admission, or release evidence.

### Pinned repository evidence ledger

| Evidence | Identity | Bounded use |
|---|---|---|
| Default branch and tree | `59143eaeb7b92884b5f97621a15ef04a30a8da8e` / `4d278ccf65877884071495238d4e8de008f61c17` | Repository snapshot for this revision |
| Immediate prior ADR-0007 bytes | `d1efbbec4b245037f884d2b614f6d6693d7162cb` | No-loss baseline and document rollback target |
| Canonical ADR index | `938c5894c36b99e14810918e2c550ab0e92d53b1` | 34-record identity/status inventory |
| ADR README | `b497be1714b88550d2f1eb151bc20a6351e99dec` | Adjacent stale 30-record summary; not a competing index |
| ADR-0029 / adopted Directory Rules | `3ba5f902ffe20a65a259cb0a7dab07f1725d204b` / `fd49a0b83e55cef52c1124281f093e263526898d` | Accepted responsibility-root and placement authority |
| ADR-0006 | `2e40267d80a474dc53ceda81e5bbf9fce3939149` | Proposed import/acquisition-seam lineage |
| Packages root / MapLibre package docs | `7b672f4d834b648f4b30ce7e2e9a5e214efa2c71` / `3ba48e7d61b013a659ed51b9336eee788d06b8f2` | Current package-root posture and renderer-lane scaffold description |
| MapLibre manifest / entry | `b0582955feeb51016327113692fa5c98ecad8816` / `91664eb00583f9e3d0405eb7954fefa9a48f4ee9` | Dependency-free private package and placeholder export |
| Explorer adapter / package | `663ba0f7a05498948f67d644387c73ab19d5c16c` / `ddd201b74a06001d84a14bf54ac62a6cc3607a29` | Comment-only adapter and non-renderer app toolchain |
| Root package / workspace lock | `5cba790c88c40b885cc65fe2d585f3205aa1ef9d` / `69a45e6aaca1ea6521e01ff274e4f1b3e1bf3975` | Workspace/tooling dependency state; no MapLibre runtime pin |
| Smoke harness | `699dd4cf42d355dd2ed7620852b7fd1f3000bbe2` | Live-CDN MapLibre 5.5.0 acquisition evidence |
| Performance workflow / schema boundary | `306040e1c9283be5a95de76c09d205a58038f380` / `9560ed016077964b56988d7fb4c02fe34e42fb28` | Static/negative checks, eight placeholders, and explicit hold |
| Latest applicable MapLibre run / job | Head `9205823798b19f37ba7c4dc2761850584948b027`; run `31759518767`; job `94642665467` | Success plus explicit skip/hold on the PR #2753 head later merged to main; not a release receipt |
| v6 validator / tests / fixtures / campaign | `88bc8bcfb894eaa7871e53d130a93a2e0258be49` / `2e0b6a4b9fe237e13bde9a09f057bcdb6a03a066` / `1bf82ae6c8966be3b1baf01620bf8f4deb7be95b` / `7a73f5ad044a4e496d8e897b160e9b5c79e1dd94` | Bounded readiness classifier, polarity evidence, and current-hold assertion |
| MapLibre architecture lane | `ff4b4754e5dc7beae22620ee669d3fdc240c44d7` | Current accepted-sounding documentation conflict and missing companion link |

Counts, hashes, paths, run results, and absences are snapshot evidence. They do not establish acceptance, exhaustive repository history, browser behavior, or public release.

---

<a id="appendix-a--no-loss-modernization-ledger"></a>

<details>
<summary><strong>Appendix A — No-loss modernization ledger</strong></summary>

| v1.1 element | v1.2 disposition |
|---|---|
| ADR identity, H1, `ADR-0007`, and exact tracked filename | Preserved |
| `legacy-proposed` source status and effective `proposed` decision | Preserved; reconciled with the 34-record index and ADR-0029 as the sole accepted decision |
| Proposed sole-renderer decision | Preserved and made version-independent |
| Prior dual-renderer lineage / `KFM-P2-FEAT-0012` | Preserved as non-ADR lineage; no claim that repository register updates are complete |
| MapLibre capability matrix | Preserved, reorganized, and truth-bounded as upstream capability evidence rather than KFM admission |
| Plugin admission concept | Preserved and expanded into a finite evidence burden |
| Default-deny on peer renderers | Preserved and clarified |
| Exception-ADR path | Preserved and expanded |
| Directory Rules rationale | Preserved and corrected: adopted v2 governs the `packages/` responsibility root but does not select a MapLibre child-package name |
| Positive and negative consequences | Preserved and updated for v6/version drift |
| Alternatives A–I | Preserved in substance; expanded with the rejection of readiness-as-acceptance |
| Contract/schema/policy/validator/build test ideas | Preserved as proposed validation classes and paths |
| Additive exception and full-supersession rollback | Preserved |
| OQ-A7 numbering conflict | Closed using canonical ADR index evidence |
| Plugin licensing, pre-existing artifacts, subsurface, Category W, receipt-shape questions | Preserved and reorganized into current open questions |
| Migration plan | Preserved and expanded for the implemented readiness classifier, six browser probes, exact initial version pin, and held workflow posture |
| Truth-label summary | Preserved and made repository-specific |
| Badge strip | Reduced to four evidence-bearing orientation badges; no CI badge claim |
| Placeholder owner/spec hash | Replaced with visible `OWNER_TBD` and no invented hash |
| Missing `maplibre-3d.md` reference | Preserved as a documented conflict; the supplied same-topic Markdown is treated as design lineage, not a tracked repository file |
| v1.1 package/root command snapshot | Corrected for current pnpm workspace lock, fail-closed root commands, and real Explorer toolchain while retaining the dependency-free renderer package |
| v1.1 partial enforcement snapshot | Expanded with the executable v6-readiness validator, five fixture cases, seven unit tests, campaign wiring, bounded scan scope, and current `HOLD` result |
| v1.1 generic workflow hold | Reconciled with latest applicable hosted run `31759518767` / job `94642665467`: success plus explicit hold and no runtime/trust execution |
| Immediate document rollback | Corrected from pre-v1.1 blob `c753f09d…` to immediate prior v1.1 blob `d1efbbec…`; older lineage retained |
| Repository/source evidence basis | Repinned to `main@59143eae…`; added exact current blobs, adopted authority, supplied-reference hashes, and evidence limits |

</details>

<a id="appendix-b--beforeafter-upgrade-matrix"></a>

<details>
<summary><strong>Appendix B — Before/after upgrade matrix</strong></summary>

| Area | v1.1 | v1.2 |
|---|---|---|
| ADR/index status | Correctly proposed, but described a snapshot with no accepted numbered ADRs | Confirms 34 records, ADR-0029 alone accepted, and ADR-0007 still proposed; records stale adjacent README counts |
| Repository posture | Package scaffold, placeholder entry, CDN harness, app-local test, older readiness workflow | Adds comment-only app adapter, pnpm lock/toolchain, eight schema placeholders, current workflows, and exact held job evidence |
| v6 readiness | Migration pressure described as an acceptance requirement | Executable classifier, five fixtures, seven unit tests, workflow assertion, six probe fields, and current `HOLD` are distinguished from browser proof |
| Renderer implementation | Non-functional scaffold | Still non-functional; stronger tooling/readiness evidence is not laundered into implementation |
| Package placement | Stated that Directory Rules proposed `packages/maplibre-runtime/` | Corrects authority: accepted Rules choose `packages/`; supplied design lineage proposes `maplibre-runtime`; current candidate remains `maplibre` |
| Enforcement | App-local import test and workflow hold | Bounded v6 import/internal-API classifier plus explicit statement of what still lacks repository-wide coverage |
| Workflow evidence | Static workflow description | Exact applicable run/job conclusion and skipped-stage/hold boundary |
| Supplied references | Generic corpus statement | Five named, hash-bound design references with explicit non-proof boundary |
| Open work | Ten implementation questions | Twelve finite questions, including browser-probe governance and adjacent documentation drift |
| Rollback | Pointed to the pre-v1.1 blob | Points to immediate prior v1.1 bytes and keeps older lineage visible |

</details>

---

_Last updated 2026-08-13 · Document version: v1.2 · Source metadata: `legacy-proposed` · Effective decision status: `proposed` · Implementation maturity: renderer scaffold / bounded readiness controls / explicit hold · [Back to top](#top)_
