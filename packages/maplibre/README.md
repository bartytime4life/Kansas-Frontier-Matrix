<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-maplibre-readme
title: packages/maplibre/ — MapLibre Package, Adapter, Distribution, and Compatibility Boundary
type: readme
version: v1.3
status: draft
owners: OWNER_TBD — Package steward · MapLibre adapter steward · Map-runtime steward · UI steward · Governed API steward · Contract steward · Schema steward · Policy steward · Security steward · Privacy/sensitivity reviewer · Dependency steward · Supply-chain steward · Validation steward · Release steward · Migration steward · CI steward · Docs steward
created: 2026-08-23
updated: 2026-08-27
policy_label: "public-doctrine; package-boundary; maplibre; renderer-adapter; exact-dependency-candidate; concrete-adapter-initial-slice; null-runtime-implemented; browser-readiness-hold; private-npm-package; workspace-enrolled; distribution-not-authorized; accepted-single-importer; accepted-renderer-family; renderer-downstream; fail-closed; no-truth-authority; no-publication-authority; rollback-aware"
current_path: packages/maplibre/README.md
owning_root: packages/
responsibility: Document current package metadata, accepted renderer-boundary ownership, dependency and distribution posture, consumer compatibility, and held concrete-renderer work without becoming runtime, policy, release, or publication authority.
truth_posture: CONFIRMED accepted ADR-0006 package-owned seam, accepted ADR-0007 renderer family, renderer-neutral MapRuntimePort, deterministic NullMapRuntime, exact maplibre-gl 6.6.0 candidate and lock closure, minimal package-owned MapLibreAdapter lifecycle/camera slice, package-local positive and fail-closed tests, and raw-renderer acquisition confined to packages/maplibre / PROPOSED dependency admission pending review and merge / HOLD authenticated browser, CSP/worker, PMTiles, terrain, accessibility, performance, long-session, release, deployment, and publication evidence / CONFLICTED legacy CDN/global harness and stale packages/maplibre-runtime references / NEEDS VERIFICATION owners, license/provenance review, Node 22 exact-head validation, hosted checks, browser probes, correction, and rollback
evidence_snapshot:
  snapshot_role: prior_to_issue_3387_slice
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 6361e92b72deccef9fef4e7dea0d2cdcd635c2bd
  prior_blob: 334ed62b180273943ff23c010b90e2f351dfa9e6
  source_readme_blob: abf0041230ee591ae77888d613c92258c53f7730
  package_metadata_blob: c7e8e57445fcca8f8a7316b54043da0ea43968a6
  source_entry_blob: 08a48ac008665317833a9476b21cd35b1679c595
  map_runtime_port_blob: 01c3d17bfbb34aae310fe17cbf892a0516a1c852
  null_map_runtime_blob: f67d5f90fe58ce49b5e6496cd4398688e35b6399
  root_package_metadata_blob: 5cba790c88c40b885cc65fe2d585f3205aa1ef9d
  root_pnpm_lock_blob: 69a45e6aaca1ea6521e01ff274e4f1b3e1bf3975
  packages_root_blob: 7b672f4d834b648f4b30ce7e2e9a5e214efa2c71
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  maplibre_architecture_blob: a897b1b0a464bedeabdd8556d19be6e207038f6e
  adapter_adr_blob: 4bf4292dc05a85fd4cd829c491808b13894bc223
  sole_renderer_adr_blob: 2482eea382fd97e68544bb04bc2e2ea1e1cedebe
  config_readme_blob: 40bb91dd6b810b70f50bdba07b58d78fcb125ad2
  map_runtime_readme_blob: 4d3897eda64d11f84f4805cb9cc2bc30a2ee333c
  validator_readme_blob: 7d29f8e5b5c215a5848803d87fd9f4c7549be105
  perf_workflow_blob: aad6793dc416017f27d3da1d39af5f9a48c531e8
  perf_smoke_blob: 699dd4cf42d355dd2ed7620852b7fd1f3000bbe2
  perf_schema_blob: 511e7f34ca84390fd5d000326ab33c46c3050fc4
  perf_validator_blob: 1f9e0f785a701da2a2b8f52bf73f4e97866d951d
  maplibre_tests_readme_blob: b20a14eae605017b7d7f210f1c27768cacbd411a
  maplibre_fixtures_readme_blob: 3b6796d242157b22c8b6d2c1621c0b02178841f9
  bounded_path_checks:
    - packages/maplibre/README.md existed at version v1.1 before this correction
    - packages/maplibre/src/README.md exists at version v1.1 on the pinned base
    - packages/maplibre/package.json exists with name @kfm/maplibre, private true, version 0.0.0, module type, types, and root exports
    - packages/maplibre/src/index.ts exports map-runtime-port and null-map-runtime; their source modules define the accepted renderer-neutral consumer seam, closed local validators, and deterministic dependency-free behavior
    - repository root package.json includes workspaces apps/* and packages/*
    - repository root lint, test, and build scripts are TODO echo placeholders
    - repository root contains MapLibre performance/proof script entry points and Playwright/pixelmatch/pngjs development dependencies
    - root package.json pins pnpm 11.17.0 and Node >=22.13 <23; pnpm-lock.yaml exists
    - packages/maplibre package metadata has no scripts, dependencies, devDependencies, peerDependencies, engines, files, sideEffects, main, module, browser, or publishConfig fields
    - packages/maplibre/src/MapLibreAdapter.ts and renderer-bound source/layer/style/protocol modules were not found
    - packages/maplibre/tests/README.md and tests/packages/maplibre/README.md were not found
    - tests/maplibre/README.md and tests/fixtures/maplibre/README.md exist as draft documentation lanes
    - packages/maplibre-runtime/README.md was not found
    - Explorer Web source and tests import @kfm/maplibre through explicit TypeScript and Vite aliases
    - ADR-0006 and ADR-0007 are accepted architecture decisions with dependency and runtime readiness still held
    - scripts/maplibre-smoke-perf.mjs loads MapLibre GL JS and glyph assets from public external URLs
    - .github/workflows/maplibre-perf-governance.yml does not watch packages/maplibre/** and watches apps/web/** rather than apps/explorer-web/**
    - schemas/maplibre/perf-envelope.schema.json is an open object scaffold with additionalProperties true and no required fields
related:
  - src/README.md
  - src/index.ts
  - package.json
  - ../README.md
  - ../geo/README.md
  - ../hashing/README.md
  - ../../package.json
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/map-first.md
  - ../../docs/architecture/maplibre.md
  - ../../docs/architecture/map-master/README.md
  - ../../docs/architecture/maplibre-master.md
  - ../../docs/architecture/map-shell.md
  - ../../docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - ../../docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "../../docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - ../../configs/maplibre/README.md
  - ../../apps/explorer-web/src/features/map_runtime/README.md
  - ../../tools/validators/maplibre/README.md
  - ../../tools/validators/maplibre/validate_perf_envelope.py
  - ../../tests/maplibre/README.md
  - ../../tests/fixtures/maplibre/README.md
  - ../../.github/workflows/maplibre-perf-governance.yml
  - ../../scripts/maplibre-smoke-perf.mjs
  - ../../schemas/maplibre/perf-envelope.schema.json
  - ../../contracts/
  - ../../schemas/contracts/v1/
  - ../../policy/
  - ../../data/registry/
  - ../../data/catalog/
  - ../../data/published/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../release/
tags: [kfm, packages, maplibre, typescript, npm-workspace, renderer-adapter, map-runtime-port, source-descriptor, layer-descriptor, style-manifest, release-manifest, evidence-ref, negative-state, protocol-admission, plugin-admission, pmtiles, cog, performance, import-boundary, supply-chain, privacy, distribution, compatibility, migration, rollback]
notes:
  - "This v1.3 checkpoint accompanies issue #3387's proposed exact dependency-admission and minimal package-owned adapter slice."
  - "The branch selects maplibre-gl 6.6.0 only in packages/maplibre/package.json, records its pnpm lock closure, and adds a minimal lifecycle/camera MapLibreAdapter with deterministic mocked tests."
  - "Review or merge of this slice remains separate from #2906 browser readiness and does not admit plugins, protocols, sources, release, deployment, or publication."
  - "The renderer may consume only governed, released, public-safe artifacts. Descriptor validity, package installation, and successful visual rendering are not truth, evidence closure, policy approval, or release approval."
  - "Package release is a software-distribution event, not KFM map/data/claim publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapLibre Package, Adapter, Distribution, and Compatibility Boundary

`packages/maplibre/`

> Private npm workspace package at KFM's accepted renderer-adapter seam. This issue #3387 slice proposes exact `maplibre-gl@6.6.0` admission and implements the first package-owned lifecycle/camera adapter while browser readiness, source/layer admission, distribution, release, deployment, and publication remain on hold.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v1.3-informational)
![maturity](https://img.shields.io/badge/maturity-initial__adapter-blue)
![package](https://img.shields.io/badge/package-%40kfm%2Fmaplibre-blue)
![distribution](https://img.shields.io/badge/distribution-private__not__authorized-critical)
![adapter](https://img.shields.io/badge/adapter-lifecycle__slice-blue)
![renderer](https://img.shields.io/badge/renderer-downstream-blue)
![authority](https://img.shields.io/badge/truth__authority-none-red)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Responsibilities](#package-responsibilities) · [Conflicts](#compatibility-and-implementation-conflicts) · [Tree](#confirmed-package-tree) · [Invariants](#keystone-invariants) · [Metadata](#package-metadata-and-workspace-boundary) · [Dependencies](#dependency-and-supply-chain-boundary) · [Distribution](#distribution-and-publishing-posture) · [API](#public-api-and-export-boundary) · [Consumers](#consumer-and-import-boundary) · [Runtime](#renderer-runtime-and-source-boundary) · [Descriptors](#descriptor-manifest-and-release-boundary) · [Plugins](#plugin-protocol-and-network-boundary) · [Security](#security-rights-sensitivity-and-privacy) · [Performance](#performance-tooling-boundary) · [Testing](#testing-build-and-ci) · [Compatibility](#versioning-compatibility-and-consumer-migration) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Rollback](#rollback-correction-deprecation-and-package-release)

> [!IMPORTANT]
> **This README is not dependency approval, runtime readiness, a plugin or endpoint allowlist, distribution authorization, schema, policy, release, deployment, or publication authority.** The draft slice proposes exact dependency admission for review and implements only lifecycle/camera behavior; #2906 browser and long-session evidence remains `HOLD`.

> [!CAUTION]
> **MapLibre draws released artifacts; it does not decide what is true.** Package presence, installation, a valid descriptor, a successful render, a screenshot, a popup, a camera state, or a map feature property is never evidence closure, policy approval, review approval, release approval, or public truth by itself.

---

<a id="purpose"></a>

## Purpose

This README defines the package-level responsibility boundary for `packages/maplibre/`.

The package may eventually own the reusable software-distribution and adapter boundary that:

- exposes one KFM-shaped interface for browser-side map lifecycle and renderer operations;
- isolates approved MapLibre runtime imports behind an accepted adapter seam;
- packages deterministic descriptor compilation and explicitly bounded runtime effects;
- preserves manifest, evidence, policy, release, correction, withdrawal, and rollback references;
- prevents raw MapLibre handles, events, source objects, and style-runtime types from leaking into shared KFM contracts;
- centralizes approved plugin, protocol, worker, asset, and endpoint bindings;
- provides stable finite outcomes and reason codes for renderer admission and failure;
- offers a tested, versioned internal package for accepted consumers;
- makes dependency, build, browser, licensing, supply-chain, and rollback posture inspectable.

The package must not become:

- the source, layer, dataset, style, tile, plugin, endpoint, or rights registry;
- a lifecycle-data, catalog, published-artifact, receipt, proof, or release store;
- a schema, semantic contract, policy, evidence resolver, citation validator, or publication authority;
- a direct RAW, WORK, QUARANTINE, connector, canonical-store, database, object-store, graph-store, vector-store, or model-runtime client;
- an app shell, Evidence Drawer, Focus Mode, public API route, search surface, export surface, or AI answer surface;
- a client-side geoprivacy engine that substitutes style filters for upstream transformation;
- a general-purpose network or arbitrary URL loading library;
- a second renderer/runtime package parallel to an accepted adapter seam without an ADR and migration plan;
- a public npm distribution merely because it has a package name.

The merged [`src/README.md`](src/README.md) governs source placement, module decomposition, effect isolation, and adapter implementation rules. This package README governs package metadata, workspace enrollment, dependencies, build and export surfaces, consumers, versioning, distribution, compatibility, correction, deprecation, and software rollback.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| This README | **CONFIRMED v1.1 before correction** | The package boundary exists, but its implementation snapshot was stale after PR #3433. |
| `src/README.md` | **CONFIRMED v1.1 before paired correction** | The source envelope owns module-level status and placement. |
| `package.json` | **PROPOSED admission slice** | Private `0.0.0` package with exact `maplibre-gl@6.6.0`, a focused test script, and no publication authority. |
| Root workspace enrollment | **CONFIRMED** | Root `package.json` includes `packages/*`, so this folder is inside the npm workspace pattern. |
| Root generic commands | **CONFIRMED placeholders** | `lint`, `test`, and `build` only echo TODO messages; they do not prove package checks. |
| Root MapLibre commands | **CONFIRMED performance-tooling entry points** | Repository scripts invoke smoke/performance/proof tooling, not this package's adapter implementation. |
| Root package manager and lockfile | **CONFIRMED** | Root metadata pins `pnpm@11.17.0` and Node `>=22.13 <23`; `pnpm-lock.yaml` exists. This does not admit a renderer dependency. |
| Package exports | **IMPLEMENTED / SPLIT** | The root facade exports the renderer-neutral port/null runtime; `@kfm/maplibre/adapter` exports the package-owned adapter without raw renderer types. |
| Renderer-neutral source modules | **IMPLEMENTED / BOUNDED** | `MapRuntimePort`, `NullMapRuntime`, serializable values, strict validators, finite states, reason codes, listeners, and disposal behavior exist. |
| Concrete renderer modules | **IMPLEMENTED / INITIAL SLICE** | `MapLibreAdapter` owns inline empty-style construction, camera synchronization, finite errors, and teardown; source/layer/selection/plugin/protocol behavior remains absent. |
| Package dependencies | **EXACT CANDIDATE / REVIEW PENDING** | Only `packages/maplibre/package.json` declares `maplibre-gl@6.6.0`; `pnpm-lock.yaml` records the integrity-bound closure. |
| Package consumers | **CONFIRMED** | Explorer Web source and tests import the KFM facade through explicit TypeScript/Vite aliases. |
| Package-local tests | **IMPLEMENTED / FOCUSED** | Five deterministic mocked tests cover valid lifecycle/camera behavior plus invalid container, construction/error, and in-flight-disposal failures. |
| MapLibre test lane | **CONFIRMED draft documentation** | `tests/maplibre/README.md` documents proposed proof obligations; executable tests and placement acceptance remain unproved. |
| MapLibre fixture lane | **CONFIRMED draft documentation** | `tests/fixtures/maplibre/README.md` documents synthetic fixtures; payload coverage and consumers remain unproved. |
| ADR-0006 | **CONFIRMED accepted architecture** | The package-owned seam is followed; this draft requests exact dependency admission without creating another importer. |
| ADR-0007 | **CONFIRMED accepted architecture** | The selected renderer family is followed; plugins, protocols, browser readiness, and operations remain held. |
| Referenced runtime package | **NOT FOUND at named README path** | `packages/maplibre-runtime/README.md` remains unresolved architecture drift. |
| Performance harness | **CONFIRMED separate root tooling** | It loads MapLibre and glyph assets from public external URLs; it is not package implementation proof. |
| Performance workflow | **CONFIRMED present / path drift** | It omits `packages/maplibre/**` and watches legacy `apps/web/**`; it does not enforce package changes. |
| Performance schema | **CONFIRMED permissive scaffold** | It permits any object and proves no package API, descriptor, or admission contract. |
| Package publication | **NOT AUTHORIZED** | `private: true` blocks normal npm publication intent; no internal artifact-distribution process is established. |

### Truth posture

**CONFIRMED**

- `packages/maplibre/` is under the shared `packages/` responsibility root.
- The package is enrolled by the root `packages/*` workspace pattern.
- The package name is `@kfm/maplibre`, version `0.0.0`, and `private: true`.
- The package manifest declares exact `maplibre-gl@6.6.0`, a package-local test script, module/type exports, and no publishing configuration.
- The source facade exports a renderer-neutral `MapRuntimePort` and deterministic `NullMapRuntime`.
- The paired source README records the TypeScript source-envelope boundary.
- Root generic `lint`, `test`, and `build` scripts are placeholders.
- Root package metadata pins pnpm and Node, and the repository carries `pnpm-lock.yaml`.
- Root MapLibre scripts exercise performance/proof tooling outside the package.
- ADR-0006 and ADR-0007 are accepted architecture decisions.
- MapLibre remains downstream of governed evidence, policy, review, release, correction, and rollback.
- The package-owned adapter and focused mocked tests are implemented; Explorer boot wiring and authenticated browser runtime proof remain unestablished.

**PROPOSED**

- Package metadata completion and internal distribution rules.
- Human review and merge disposition for the exact dependency-admission candidate.
- An explicit export map and KFM-shaped API.
- Pure/effectful entry-point separation.
- Manifest-gated source/layer/style activation.
- Approved protocol/plugin registration.
- Dependency, license, vulnerability, provenance, and browser-compatibility gates.
- Package tests, import-boundary enforcement, consumer contract tests, and dedicated CI.
- Semantic versioning, consumer inventory, migration, deprecation, correction, and rollback.

**CONFLICTED**

- The prior helper-only blanket no-network wording versus the required effects of a browser renderer.
- Accepted `packages/maplibre/` ownership versus repeated references to absent `packages/maplibre-runtime/`.
- ADR-0006's accepted acquisition boundary versus repository-root smoke tooling loading MapLibre from a public CDN outside the package.
- ADR-0007's accepted renderer family versus still-unaccepted plugin admission, exact dependency, exception, and supply-chain mechanisms.
- Canonical `schemas/contracts/v1/maplibre/` doctrine versus permissive `schemas/maplibre/` performance scaffolding.
- `tests/maplibre/` versus `tests/packages/maplibre/` as the executable test home.
- `apps/explorer-web/` doctrine versus `apps/web/**` in the performance workflow filter.
- Performance proof artifacts under `artifacts/perf/` versus the Directory Rules limitation on trust-bearing content in `artifacts/`.
- Rich future-adapter documentation versus the current partial dependency-free implementation.

**UNKNOWN**

- Applicability of the root pnpm/lock profile to future renderer dependency admission and package-specific builds.
- Accepted MapLibre GL JS version and dependency range.
- Module format, TypeScript config, bundler, output directories, source maps, tree-shaking, and browser targets.
- Public export names and compatibility guarantees.
- Complete consumer inventory and deployment path beyond the bounded Explorer Web imports.
- Runtime ownership between package and app-local feature code.
- Protocol, plugin, worker, sprite, glyph, tile, and endpoint allowlists.
- Contract/schema/policy/release bindings.
- Build reproducibility, artifact provenance, SBOM, license review, vulnerability thresholds, and dependency update process.
- Test coverage, CI enforcement, release use, and operational health.

**NEEDS VERIFICATION**

- Named owners and reviewers.
- Accountable review and enforcement evidence for the accepted ADR-0006/0007 architecture.
- One canonical renderer/runtime package home.
- Package metadata, dependency, lockfile, export, build, and browser-support decisions.
- Import inventory and enforcement.
- Consumer inventory and migration plan.
- Contract, schema, policy, manifest, evidence, and release bindings.
- Hermetic tests and approved external-network test mode.
- Package-specific CI path filters and required checks.
- Internal distribution, deprecation, correction, and rollback automation.

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

`packages/maplibre/` is a sound package lane because `packages/` owns reusable implementation shared by apps, workers, pipelines, tools, and tests.

The responsibility split is:

| Concern | Owning home | Package relationship |
|---|---|---|
| Package metadata, dependencies, exports, versioning, distribution | `packages/maplibre/` | **This README's package-level boundary.** |
| Source layout and adapter implementation | `packages/maplibre/src/` | Governed by [`src/README.md`](src/README.md). |
| App-local map composition | `apps/explorer-web/` | Consumes the accepted adapter; does not own shared renderer dependency rules. |
| Shared UI components | `packages/ui/` | Renderer-agnostic unless an accepted interface requires otherwise. |
| Map architecture and ADRs | `docs/architecture/`, `docs/adr/` | Define intent and accepted decisions; docs do not prove implementation. |
| Semantic meaning | `contracts/` | Owns object semantics. |
| Machine shape | `schemas/contracts/v1/` | Owns accepted validation shape. |
| Policy and admission | `policy/` | Owns allow, deny, restrict, abstain, rights, sensitivity, and plugin decisions. |
| Source and layer registries | `data/registry/` | Owns authority metadata and declared source/layer identity. |
| Catalog records | `data/catalog/` | Owns governed discovery records. |
| Published artifacts | `data/published/` | Owns released public-safe map derivatives. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Owns auditable process/evidence artifacts. |
| Release, correction, withdrawal, rollback | `release/` | Owns governed publication state transitions. |
| Validators | `tools/validators/maplibre/` | Checks declared rules; does not implement the renderer. |
| Executable tests and fixtures | Accepted `tests/` and fixture lanes | Prove behavior with synthetic public-safe inputs. |

> [!WARNING]
> Package code must not become a second schema, policy, registry, release, evidence, artifact, or application authority. Package convenience never outranks root ownership.

### Compatibility-root restraint

The package may reference generated build artifacts during local or CI execution, but canonical trust artifacts must remain in their owning roots. `artifacts/` may hold temporary build, QA, or workflow outputs only under the repository's compatibility-root rules.

A performance report, screenshot, package tarball, source map, bundle, or CI artifact does not become:

- a ReleaseManifest;
- a PromotionDecision;
- a ProofPack;
- an EvidenceBundle;
- a correction or rollback record;
- a published map artifact;
- proof that the package is safe for production.

[Back to top](#top)

---

<a id="package-responsibilities"></a>

## Package responsibilities

A mature `@kfm/maplibre` package may own:

| Responsibility | Required behavior |
|---|---|
| Workspace package identity | Declare stable internal name, version, privacy, package-manager expectations, and ownership. |
| Dependency declaration | Pin or constrain approved renderer, protocol, plugin, and build dependencies through reviewed metadata and lockfile policy. |
| Export surface | Expose only KFM-shaped types and operations; do not export raw MapLibre runtime handles as the general interface. |
| Build surface | Produce deterministic, reviewable outputs for accepted module and browser targets. |
| Runtime seam | Isolate permitted effectful renderer operations behind accepted entry points. |
| Descriptor compilation | Convert already-governed inputs into bounded renderer commands or candidates without redefining contracts. |
| Manifest gating | Require declared release/integrity/policy/evidence support before activation. |
| Protocol/plugin registration | Centralize approved bindings and deny undeclared versions or arbitrary registration. |
| Negative states | Preserve deterministic denied, restricted, abstained, stale, invalid, unavailable, unsigned, and rollback states. |
| Consumer compatibility | Publish API/version change notes, migration instructions, and deprecation windows for known consumers. |
| Supply-chain posture | Record licenses, provenance, vulnerabilities, transitive dependencies, integrity, and artifact metadata. |
| Software rollback | Make prior known-good package/build versions restorable without rewriting map/data release history. |

The package must not own:

- truth or claim determination;
- evidence closure or citation acceptance;
- policy decisions;
- source/layer release;
- sensitive-geometry transformation approval;
- registry mutation;
- public API responses;
- UI shell composition;
- map-data storage;
- direct AI/model results;
- data-release rollback.

[Back to top](#top)

---

<a id="compatibility-and-implementation-conflicts"></a>

## Compatibility and implementation conflicts

These conflicts must remain visible until accepted decisions resolve them.

### 1. Package seam versus runtime-package references

ADR-0006 accepts `packages/maplibre/` as the single runtime importer. Other docs still reference `packages/maplibre-runtime/`, whose README was not found.

**Required resolution:**

- apply the accepted `packages/maplibre/` ownership decision;
- record migration/retirement of conflicting references without creating another package;
- inventory all references;
- migrate consumers and docs;
- freeze the losing path;
- define compatibility and removal dates;
- avoid creating both implementations.

### 2. Pure helper language versus renderer effects

The old package README described no-network helpers. A browser renderer necessarily performs bounded effects: DOM/WebGL setup, workers, resource requests, protocol handling, image/glyph/sprite loads, event subscriptions, and cleanup.

**Required resolution:**

- preserve pure descriptor modules where possible;
- isolate effects behind explicit adapter entry points;
- require admitted endpoints/protocols/plugins;
- forbid arbitrary URL loading;
- test cleanup, cancellation, timeouts, and denial;
- avoid pretending the entire package is pure or no-network.

### 3. Accepted single-importer boundary versus root smoke harness

The performance harness loads MapLibre through public CDN script tags outside `packages/maplibre/`.

**Required conformance resolution after ADR-0006 acceptance:**

- classify the harness as a temporary test exception or migrate it behind the package;
- record any exception scope;
- pin and integrity-check assets;
- use local/hermetic fixtures by default;
- add import/network enforcement;
- ensure examples and tests cannot become production bypass patterns.

### 4. Accepted renderer family versus plugin governance

ADR-0007 accepts MapLibre GL JS as the sole normal browser-renderer family, but plugin contracts, exact dependencies, policy decisions, pins, and supply-chain attestations remain unaccepted.

**Required resolution:**

- preserve ADR-0007 while separately admitting exact dependencies and plugins;
- define `PluginAdmission`;
- assign contract/schema/policy homes;
- pin versions and integrity;
- review licenses and vulnerabilities;
- define capability and fallback behavior;
- preserve explicit unsupported and denied states.

### 5. Schema-home drift

MapLibre doctrine points to `schemas/contracts/v1/maplibre/`; performance tooling validates against permissive `schemas/maplibre/perf-envelope.schema.json`.

**Required resolution:**

- decide whether the performance schema migrates, remains a bounded legacy scaffold, or becomes a declared compatibility surface;
- do not present the permissive scaffold as package API validation;
- avoid divergent definitions.

### 6. Test-home drift

`tests/maplibre/` exists as a proposed executable lane; package docs previously proposed `tests/packages/maplibre/`.

**Required resolution:**

- choose the accepted test home;
- document fixture separation;
- migrate or redirect the losing lane;
- update CI and CODEOWNERS;
- prevent duplicate, divergent suites.

### 7. App path and CI-filter drift

Architecture names `apps/explorer-web/`; the performance workflow watches `apps/web/**`.

**Required resolution:**

- align path filters with confirmed consumer homes;
- add `packages/maplibre/**`;
- prove the workflow triggers on package behavior changes;
- retain explicit compatibility filters only when documented.

### 8. Software release versus map/data release

An npm package version, bundle, CI artifact, or internal registry entry is not a MapReleaseManifest or data publication decision.

**Required resolution:**

- keep software distribution metadata separate;
- link software versions into release records only when required;
- never infer public map release from package build success.

[Back to top](#top)

---

<a id="confirmed-package-tree"></a>

## Confirmed package tree

Current bounded evidence supports:

```text
packages/maplibre/
├── README.md
├── package.json
├── tests/
│   └── maplibre-adapter.test.ts
└── src/
    ├── README.md
    ├── index.ts
    ├── maplibre-adapter.ts
    ├── map-runtime-port.ts
    └── null-map-runtime.ts
```

Confirmed details:

- `package.json` declares a private ESM package, exact `maplibre-gl@6.6.0`, and a focused Vitest script.
- `src/index.ts` retains the renderer-neutral port/null-runtime facade; the explicit `./adapter` subpath contains the effectful adapter export.
- `src/maplibre-adapter.ts` owns the raw renderer import, empty-style initialization, camera state, finite failures, and teardown.
- `src/map-runtime-port.ts` owns KFM-shaped values, strict validators, finite states, and the consumer interface.
- `src/null-map-runtime.ts` supplies deterministic no-network behavior for migration and tests.
- `tests/maplibre-adapter.test.ts` supplies deterministic positive and fail-closed adapter coverage through a renderer mock.
- No accepted build output directory was established.
- No package-local TypeScript configuration, bundler configuration, changelog, license file, or build output is established.
- No `packages/maplibre-runtime/README.md` was found.

### Proposed mature tree

The following tree is **PROPOSED** and must not be created wholesale without accepted ownership, contracts, dependencies, and tests:

```text
packages/maplibre/
├── README.md
├── package.json
├── tsconfig.json
├── CHANGELOG.md
├── src/
│   ├── README.md
│   ├── index.ts
│   ├── public-types.ts
│   ├── pure/
│   │   ├── descriptors.ts
│   │   ├── manifests.ts
│   │   ├── negative-states.ts
│   │   └── validation-results.ts
│   └── runtime/
│       ├── adapter.ts
│       ├── lifecycle.ts
│       ├── layers.ts
│       ├── events.ts
│       ├── protocols.ts
│       ├── plugins.ts
│       └── resource-policy.ts
└── tests/ or accepted repository test lane
```

Every new file requires:

- an owning responsibility;
- an accepted caller or implementation stage;
- contract/schema/policy references where applicable;
- tests, including negative paths;
- import and effect classification;
- rollback and migration consideration;
- no duplicate authority.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

1. **Renderer downstream.** MapLibre never becomes truth, source, evidence, policy, review, release, citation, or AI authority.
2. **Released public-safe artifacts only.** Public runtime activation requires governed release posture appropriate to the surface.
3. **Verify before activation.** Source, layer, style, protocol, and plugin binding must fail closed when required support is absent or mismatched.
4. **Raw renderer types stay inside the seam.** Shared KFM contracts use KFM-shaped values.
5. **Pure and effectful code remain distinguishable.** Descriptor compilation must not hide ambient runtime behavior.
6. **No arbitrary network access.** Effectful runtime access is endpoint-, protocol-, manifest-, and policy-bound.
7. **Sensitive geometry is transformed upstream.** Style filters and client-side omission are not geoprivacy controls.
8. **Negative states are first-class.** Denial, restriction, abstention, staleness, withdrawal, invalidity, and rollback mismatch must not disappear into visual behavior.
9. **Package identity is not release identity.** Software versioning is separate from map/data/claim release.
10. **Package build is not publication.** A successful bundle or install does not authorize public use.
11. **Plugins are not admitted by documentation mention.** Admission requires accepted policy and supply-chain evidence.
12. **One canonical runtime home.** Parallel package implementations require an ADR and migration plan.
13. **Consumer changes are reversible.** Breaking API changes require inventory, migration, compatibility, and rollback.
14. **No hidden credentials.** Secrets and source credentials never enter committed package code, examples, fixtures, logs, or bundles.
15. **Auditability over convenience.** Imports, dependencies, effects, endpoints, and release bindings must be inspectable.

[Back to top](#top)

---

<a id="package-metadata-and-workspace-boundary"></a>

## Package metadata and workspace boundary

### Confirmed manifest

The package manifest currently establishes only:

```json
{
  "name": "@kfm/maplibre",
  "private": true,
  "version": "0.0.0"
}
```

Safe interpretation:

- the package has an intended internal name;
- npm publication is not intended in the current state;
- version `0.0.0` signals scaffold maturity;
- workspace discovery is supplied by root `packages/*`;
- nothing else about installability, exports, runtime, build, or dependencies is established.

### Required metadata before implementation use

A mature manifest should explicitly decide and test:

| Field or concern | Required decision |
|---|---|
| `name` | Stable internal distribution identity. |
| `version` | Versioning policy and release provenance. |
| `private` | Whether publication remains denied. |
| `type` | ESM/CommonJS posture. |
| `exports` | Public entry points and type conditions. |
| `types` | Type declaration location. |
| `files` | Allowed packaged files. |
| `sideEffects` | Accurate tree-shaking/effect declaration. |
| `engines` | Supported Node tooling version. |
| browser targets | Supported browser/runtime matrix. |
| scripts | Build, typecheck, lint, test, package, and clean commands. |
| dependencies | Runtime dependencies with approved ranges. |
| peer dependencies | Consumer-supplied runtime expectations, if any. |
| dev dependencies | Build/test-only tooling. |
| publish configuration | Keep absent or explicitly deny unless distribution is approved. |
| license | Package/software licensing posture. |
| repository metadata | Traceable source and issue location where useful. |

### Root workspace limitations

Root workspace membership does not prove:

- successful workspace installation;
- a package manager choice;
- a lockfile;
- dependency hoisting behavior;
- build ordering;
- package exports;
- consumer imports;
- type resolution;
- browser bundling;
- CI coverage.

The current root `lint`, `test`, and `build` scripts are placeholders. Package maturity must not be inferred from their names.

[Back to top](#top)

---

<a id="dependency-and-supply-chain-boundary"></a>

## Dependency and supply-chain boundary

This draft slice declares exact `maplibre-gl@6.6.0` only in the accepted package manifest and records its lockfile integrity closure. Human dependency-admission review still requires:

1. accepted adapter/runtime ownership;
2. dependency purpose and import location;
3. exact or bounded version policy;
4. lockfile/package-manager decision;
5. license review;
6. source/provenance review;
7. vulnerability scanning;
8. transitive dependency inventory;
9. browser bundle impact;
10. worker/WASM/native asset handling;
11. CSP and endpoint implications;
12. plugin/protocol admission where applicable;
13. update and rollback procedure;
14. compatibility tests;
15. SBOM or equivalent software inventory for released builds where required.

### Dependency classes

| Class | Examples | Required posture |
|---|---|---|
| Core renderer | `maplibre-gl` | Single approved version/range; adapter-only import under accepted ADR-0006 after separate dependency admission. |
| Style/type support | style-spec packages | Keep renderer-specific types inside package boundary. |
| Protocols | PMTiles, COG, vector-text protocols | Explicit registration, endpoint controls, integrity, cleanup, and admission. |
| 3D/custom layers | three.js, 3D Tiles, glTF, lidar, deck.gl integrations | Per-version PluginAdmission, supply-chain review, capability tests, fallback state. |
| Build tooling | TypeScript, bundler, declarations | Reproducible and package-scoped; no undeclared global tooling. |
| Test tooling | DOM/WebGL mocks, browser harness | Hermetic by default; live-network mode explicit and isolated. |
| Validation helpers | schema or runtime validators | Do not duplicate semantic contract authority. |

### Lockfile posture

The root workspace pins `pnpm@11.17.0`, Node `>=22.13 <23`, and carries `pnpm-lock.yaml`. Until the proposed dependency receives review and the required Node 22 and hosted validation settles:

- do not claim reproducible installation;
- do not claim deterministic dependency resolution;
- do not publish or promote package artifacts;
- do not rely on undeclared transitive availability;
- do not treat a local install as repository-wide proof.

### Supply-chain outputs

Software supply-chain evidence may include:

- dependency inventory;
- license report;
- vulnerability report;
- source provenance;
- build provenance;
- package checksum;
- SBOM;
- signed internal package artifact;
- browser bundle inventory.

These are software integrity artifacts. They do not replace KFM evidence, policy, map release, or publication records.

[Back to top](#top)

---

<a id="distribution-and-publishing-posture"></a>

## Distribution and publishing posture

### Current posture

**Distribution is not authorized.**

Evidence:

- `private: true`;
- version `0.0.0`;
- only the renderer-neutral root facade is exported;
- no build;
- no files list;
- one exact renderer dependency candidate owned by the accepted package seam;
- focused mocked package tests but no authenticated browser probe packet;
- no consumer inventory;
- no package publication workflow;
- a bounded KFM-owned API with an initial lifecycle/camera adapter and no admitted source/layer/plugin/protocol API.

### Internal distribution, if later approved

An internal package artifact should require:

- accepted owners;
- accepted ADR and runtime home;
- completed manifest metadata;
- deterministic build;
- package contents inspection;
- declarations/typecheck;
- dependency and license review;
- vulnerability policy;
- test and compatibility evidence;
- package checksum/provenance;
- consumer inventory;
- changelog;
- rollback target;
- distribution location and retention policy;
- no secrets or environment-specific endpoints.

### Software distribution is not map publication

A package release:

- does not release a layer;
- does not publish PMTiles, COG, MVT, MLT, sprites, glyphs, styles, scenes, or screenshots;
- does not approve a plugin;
- does not satisfy map policy;
- does not create an EvidenceBundle;
- does not establish a public claim;
- does not supersede a MapReleaseManifest;
- does not authorize a public endpoint.

Any data/map release that depends on a package version should reference that version as implementation context while retaining independent release authority.

[Back to top](#top)

---

<a id="public-api-and-export-boundary"></a>

## Public API and export boundary

The package currently has no ratified API.

A future export surface should be:

- KFM-shaped;
- narrow;
- versioned;
- typed;
- renderer-agnostic above the adapter seam where practical;
- explicit about effects;
- explicit about finite outcomes;
- free of raw credentials and unrestricted URLs;
- covered by consumer contract tests.

### Proposed entry-point classes

| Entry point | Effect class | Possible responsibility |
|---|---:|---|
| package root | Mixed but controlled | Stable KFM-facing types and factory functions only. |
| `pure` entry point | Pure | Descriptor compilation, bounded validation results, negative-state values. |
| `runtime` entry point | Effectful | Adapter creation, lifecycle, source/layer binding, events, cleanup. |
| test helpers | Test-only | Synthetic factories and deterministic mocks; excluded from production export unless explicitly intended. |

### Raw renderer leakage denied

General consumers should not receive:

- `maplibregl.Map`;
- raw MapLibre event objects;
- arbitrary source/layer/style objects without KFM wrappers;
- raw WebGL contexts;
- internal workers;
- protocol registries;
- plugin instances;
- unrestricted URL callbacks.

Renderer-native escape hatches require:

- a named use case;
- accepted owner;
- bounded scope;
- security and compatibility review;
- tests;
- migration/rollback plan;
- documentation that they are not stable general API.

### Proposed finite package outcomes

These names are **PROPOSED**, not implemented:

- `READY`
- `ADDED`
- `REMOVED`
- `UPDATED`
- `DENIED`
- `RESTRICTED`
- `ABSTAINED`
- `UNRELEASED`
- `STALE`
- `WITHDRAWN`
- `INVALID_DESCRIPTOR`
- `INVALID_MANIFEST`
- `INTEGRITY_MISMATCH`
- `UNSIGNED`
- `ENDPOINT_DENIED`
- `UNSUPPORTED_SOURCE`
- `UNSUPPORTED_STYLE`
- `UNSUPPORTED_PLUGIN`
- `PROTOCOL_NOT_ADMITTED`
- `ROLLBACK_MISMATCH`
- `RESOURCE_LIMIT`
- `DEPENDENCY_UNAVAILABLE`
- `RUNTIME_ERROR`
- `DESTROYED`

Outcome names must align with accepted contracts and consumers before implementation.

[Back to top](#top)

---

<a id="consumer-and-import-boundary"></a>

## Consumer and import boundary

Explorer Web source and tests import the renderer-neutral `@kfm/maplibre` facade. That bounded consumer evidence does not prove a concrete renderer, deployment, or complete consumer inventory.

Before expanding consumer use, complete the consumer inventory with:

- repository path;
- owner;
- import entry point;
- runtime environment;
- browser/support requirements;
- capabilities used;
- expected finite outcomes;
- error/negative-state handling;
- policy/release dependencies;
- migration contact;
- rollback behavior.

### Accepted import law; enforcement remains partial

- only `@kfm/maplibre` implementation code may import approved MapLibre runtime packages;
- apps and shared UI import the KFM-shaped package surface;
- tests outside the package use test adapters or accepted exception boundaries;
- scripts/examples are included in enforcement or explicitly classified;
- direct CDN script loading is denied except for documented, isolated test exceptions.

### Import enforcement

Potential enforcement mechanisms include:

- ESLint `no-restricted-imports`;
- dependency-cruiser;
- custom repository validator;
- workspace dependency checks;
- code search in CI;
- bundler dependency inspection;
- consumer contract tests.

The selected mechanism must:

- cover TypeScript and JavaScript;
- cover apps, packages, scripts, examples, tests, and viewer templates as intended;
- distinguish accepted package-local imports from violations;
- emit deterministic failures;
- be required in CI;
- produce reviewable evidence.

### Consumer obligations

Consumers must:

- pass governed descriptors and release-aware inputs;
- handle denied, abstained, stale, unavailable, withdrawn, and rollback states;
- avoid treating feature properties or render success as evidence;
- preserve accessibility and non-map alternatives;
- avoid direct registry/store/model access;
- destroy adapters and unsubscribe listeners;
- avoid logging sensitive payloads;
- follow version and migration policy.

[Back to top](#top)

---

<a id="renderer-runtime-and-source-boundary"></a>

## Renderer runtime and source boundary

The source-level rules live in [`src/README.md`](src/README.md). Package-level decisions must support that boundary.

### Pure/effect split

| Concern | Preferred class | Rule |
|---|---:|---|
| Descriptor candidate construction | Pure | Explicit inputs, deterministic output, no network or ambient state. |
| Local shape/result validation | Pure | Contract/schema-aligned, finite outcomes, no authority inflation. |
| Negative-state values | Pure | Preserve reason, refs, and current posture. |
| Adapter creation | Effectful | DOM/WebGL/browser capability checks and explicit cleanup. |
| Source/layer activation | Effectful | Manifest, policy, release, endpoint, and integrity gated. |
| Protocol/plugin registration | Effectful | Central, idempotent, admitted, version-pinned, reversible. |
| Event subscription | Effectful | Translate to KFM-shaped candidates; no raw event leakage. |
| Resource loading | Effectful | Endpoint/manifest/CSP bounded; no arbitrary fetch. |
| Destruction | Effectful | Remove listeners, workers, protocols, controls, and map resources. |

### Package/source delegation

| Package root owns | Source envelope owns |
|---|---|
| Package name and version | Module placement |
| Dependencies and lockfile posture | Import direction |
| Build, exports, declarations | Pure/effect separation |
| Browser/module targets | Adapter implementation |
| Package test commands | Runtime lifecycle |
| Consumer compatibility | Descriptor compilation |
| Distribution and artifact provenance | Event translation |
| Deprecation and package rollback | Protocol/plugin implementation |

Neither surface owns contracts, schemas, policy, data release, or public truth.

[Back to top](#top)

---

<a id="descriptor-manifest-and-release-boundary"></a>

## Descriptor, manifest, and release boundary

The package may consume accepted, validated objects or references. It must not invent their meaning.

Potential governed inputs include:

- LayerDescriptor or LayerManifest;
- StyleManifest;
- TileArtifactManifest;
- KFMGeoManifest;
- MapReleaseManifest;
- ReleaseManifest or PromotionDecision refs;
- EvidenceRef and EvidenceBundle refs;
- PolicyDecision and obligations;
- rights and sensitivity posture;
- correction, supersession, withdrawal, and rollback refs;
- camera/time/view context;
- artifact hashes and integrity metadata.

### Verify-before-activation

Before an effectful operation adds or updates a source, layer, style, terrain, protocol, or plugin, the adapter should fail closed when required support is:

- missing;
- malformed;
- unsupported;
- unreleased;
- stale;
- withdrawn;
- correction-pending;
- rollback-mismatched;
- unsigned where signatures are required;
- integrity-mismatched;
- endpoint-denied;
- policy-denied;
- rights-incompatible;
- sensitivity-unsafe;
- incompatible with accepted browser/runtime capabilities.

### What local validation means

A locally valid descriptor means only that:

- required local fields and refs are present;
- values conform to an accepted profile;
- the package can safely proceed to the next governed check.

It does not mean:

- the source is authoritative;
- evidence is sufficient;
- the layer is public;
- rights are cleared;
- sensitivity is resolved;
- release is approved;
- the rendered representation is accurate for every use;
- the map is safe for operational action.

[Back to top](#top)

---

<a id="plugin-protocol-and-network-boundary"></a>

## Plugin, protocol, and network boundary

### Default posture

- No arbitrary URL acceptance.
- No implicit plugin discovery.
- No runtime registration from user-controlled strings.
- No unpinned CDN runtime dependencies in production.
- No credentials in source URLs, logs, bundles, or fixtures.
- No source activation without admitted endpoint and release posture.
- No silent fallback to a less-governed source.

### Plugin admission

A plugin's mention in ADR-0007 or architecture documentation is not admission.

Per-plugin admission should include:

- package and version;
- capability;
- license;
- source/provenance;
- vulnerability posture;
- transitive dependencies;
- bundle and performance impact;
- browser compatibility;
- worker/WASM/native assets;
- endpoint behavior;
- data/sensitivity impact;
- policy decision;
- manifest representation;
- tests and rollback.

### Protocol registration

PMTiles, COG, vector-text, custom URL, 3D tile, lidar, or other protocols require:

- one central registration point;
- idempotent setup;
- deterministic conflict handling;
- explicit cleanup where supported;
- admitted URL schemes;
- endpoint allowlists or resolver interfaces;
- request timeouts, cancellation, and limits;
- integrity and release checks;
- negative-state mapping;
- no credential leakage.

### Network classes

| Class | Default | Example |
|---|---:|---|
| Local pure tests | **DENY network** | Descriptor unit tests. |
| Hermetic browser tests | **Local fixture server only** | Synthetic tiles/styles/glyphs. |
| Review-only live integration | Explicit opt-in | Approved external compatibility check. |
| Production runtime | Governed allowlist/resolver | Released tiles, sprites, glyphs, APIs. |
| Arbitrary user URL | **DENY** | Unreviewed TileJSON or plugin endpoint. |
| RAW/WORK/QUARANTINE/internal store | **DENY public client** | Direct lifecycle/store access. |

### CSP and browser security

Before production use, verify:

- script, worker, image, font, and connect-src requirements;
- no `unsafe-eval` dependency without accepted exception;
- worker URL strategy;
- cross-origin and credential behavior;
- referrer policy;
- integrity/pinning for static assets;
- error redaction;
- denial of dangerous schemes;
- browser memory and resource limits.

[Back to top](#top)

---

<a id="security-rights-sensitivity-and-privacy"></a>

## Security, rights, sensitivity, and privacy

The package must fail closed when rendering could expose:

- living-person data;
- private property or ownership detail;
- DNA/genomic or kinship information;
- precise rare-species locations;
- archaeology or cultural-sensitive locations;
- critical infrastructure;
- protected ecological resources;
- source credentials or private endpoints;
- unreleased or embargoed data.

### Sensitive geometry rule

Sensitive geometry must be transformed upstream through governed:

- generalization;
- aggregation;
- jitter;
- omission;
- delayed release;
- staged access;
- denial.

Client-side style filters, opacity, hidden layers, zoom conditions, or disabled popups do not remove sensitive coordinates from delivered tiles or source data and therefore do not satisfy geoprivacy.

### Logging and diagnostics

Logs and telemetry must not record unrestricted:

- full feature payloads;
- exact sensitive coordinates;
- credentials;
- signed URLs;
- private endpoints;
- raw evidence objects;
- living-person identifiers;
- user-generated sensitive map context.

Prefer:

- stable reason codes;
- redacted IDs;
- bounded counters;
- coarse performance metrics;
- package/build version;
- capability state;
- release reference where public-safe;
- correlation IDs that are non-secret and policy-safe.

### Resource bounds

Define and test limits for:

- maximum sources and layers;
- style size and expression complexity;
- tile/cache memory;
- concurrent requests;
- request duration and retry count;
- event subscriber count;
- feature-query result size;
- plugin count;
- worker count;
- image/sprite/glyph sizes;
- 3D asset and point-cloud budgets;
- adapter initialization and cleanup time.

Resource exhaustion must produce explicit, recoverable outcomes rather than silent degradation or unsafe fallback.

[Back to top](#top)

---

<a id="performance-tooling-boundary"></a>

## Performance tooling boundary

Repository-root MapLibre performance tooling is **adjacent evidence**, not package implementation proof.

Confirmed tooling includes:

- root npm scripts;
- Playwright/pixelmatch/pngjs development dependencies;
- a smoke-performance script;
- a performance-envelope config;
- validators;
- render-diff and proof-building scripts;
- a dedicated workflow;
- temporary artifacts under `artifacts/perf/`.

### What performance tooling can prove

When successfully executed and reviewed, it may support claims about:

- scenario load and idle timing;
- frame-time distributions;
- render-diff behavior;
- threshold checks;
- fixture compatibility;
- workflow artifact production.

### What it does not prove

It does not by itself prove:

- `@kfm/maplibre` is imported;
- the package builds or installs;
- ADR-0006 is enforced;
- descriptors are contract/schema aligned;
- plugins are admitted;
- endpoints are production-safe;
- sensitive geometry is protected;
- evidence/policy/release gates are wired;
- package API compatibility;
- public runtime readiness.

### Current drift

- the workflow does not watch `packages/maplibre/**`;
- it watches `apps/web/**` rather than documented `apps/explorer-web/**`;
- the harness loads public CDN assets;
- the schema is permissive;
- trust-like outputs use `artifacts/perf/`;
- package use is not established.

The package README records these conflicts but does not repair them in this documentation-only change.

[Back to top](#top)

---

<a id="testing-build-and-ci"></a>

## Testing, build, and CI

### Required package test families

| Family | What it should prove |
|---|---|
| Manifest metadata | Package name, privacy, version, exports, files, engines, dependency classes, and side-effect declarations are intentional. |
| Build | Accepted module/browser outputs build reproducibly. |
| Typecheck | Public and internal types compile under supported toolchain versions. |
| Export map | Intended entry points resolve; internal modules do not leak. |
| Import safety | Importing pure entry points has no DOM, network, worker, timer, or global side effects. |
| Adapter lifecycle | Create, initialize, destroy, repeated destroy, cancellation, and cleanup are deterministic. |
| Single importer | Forbidden direct MapLibre imports fail outside accepted scope. |
| Descriptor compilation | Accepted synthetic descriptors produce deterministic candidates. |
| Negative states | Denied, restricted, abstained, stale, withdrawn, invalid, unsigned, and rollback paths remain visible. |
| Manifest gating | Missing/mismatched release and integrity support blocks activation. |
| Endpoint policy | Unapproved schemes/hosts/paths are denied. |
| Protocol registration | Registration is admitted, idempotent, bounded, and reversible. |
| Plugin admission | Unlisted/version-mismatched plugins fail closed. |
| Event translation | Raw renderer events become bounded KFM-shaped candidates. |
| Sensitive geometry | Unsafe exact detail never reaches public renderer fixtures. |
| Resource limits | Excess sources/layers/requests/assets produce deterministic limits. |
| Browser compatibility | Supported browsers/capabilities behave as declared. |
| Consumer contracts | Known consumers compile and pass expected interactions. |
| Bundle inspection | No secrets, undeclared endpoints, unexpected dependencies, or internal sources are bundled. |
| Rollback | Prior known-good package/build can be restored. |

### Fixture posture

Default fixtures should be:

- synthetic;
- public-safe;
- local;
- deterministic;
- small;
- versioned;
- free of source credentials and production URLs;
- explicit about expected outcomes.

Live external fixtures require an isolated opt-in mode and must not be required for ordinary unit or pull-request validation unless governance explicitly permits it.

### Required CI gates

Before production or internal distribution use, CI should include:

- package metadata validation;
- package-manager/lockfile verification;
- dependency and license scanning;
- vulnerability policy;
- typecheck;
- lint;
- unit tests;
- negative-path tests;
- import-boundary enforcement;
- build;
- bundle/content inspection;
- browser smoke tests;
- consumer contract tests;
- performance tests where material;
- documentation/link checks;
- rollback or prior-version compatibility checks;
- artifact provenance where required.

### Current CI limitation

The existing MapLibre performance workflow is not a package CI workflow. It does not watch this package and must not be cited as evidence that package changes are checked.

[Back to top](#top)

---

<a id="versioning-compatibility-and-consumer-migration"></a>

## Versioning, compatibility, and consumer migration

### Versioning posture

`0.0.0` remains a pre-release marker. Before a concrete renderer or broader consumer commitment:

- choose versioning policy;
- define which surfaces are public;
- define compatibility guarantees;
- define prerelease handling;
- define release notes and provenance;
- identify the package owner who approves versions.

### Breaking changes

Treat these as breaking unless an accepted compatibility policy says otherwise:

- removing or renaming exports;
- changing outcome names or reason codes;
- changing required manifest/policy inputs;
- exposing or withdrawing raw renderer types;
- changing lifecycle or cleanup behavior;
- changing endpoint/protocol/plugin requirements;
- changing supported browser/module targets;
- changing event payloads;
- changing error classification;
- changing side-effect behavior;
- changing dependency or peer-dependency expectations.

### Consumer migration sequence

1. Inventory consumers and owners.
2. Define old and new API contracts.
3. Add compatibility adapters only when necessary.
4. Test both paths against accepted fixtures.
5. Publish migration instructions.
6. Stage consumer updates.
7. Observe compatibility and negative states.
8. Preserve rollback to prior package and consumer versions.
9. Deprecate with a dated window.
10. Remove compatibility code only after evidence confirms migration.

Compatibility adapters must be:

- explicit;
- versioned;
- temporary;
- documented;
- tested;
- measurable;
- removable;
- unable to bypass policy, release, or sensitivity gates.

### Correction

When package behavior misrepresents release, policy, evidence, or map state:

- stop or constrain the affected software distribution;
- identify impacted versions and consumers;
- preserve evidence and logs safely;
- issue the appropriate software correction notice or changelog;
- coordinate with data/map release owners if public output was affected;
- provide a patched version or rollback;
- test the correction and prior-version recovery;
- do not rewrite historical release records.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Stage 0 — Apply accepted architecture and resolve remaining governance

Before expanding the initial renderer slice:

- assign owners;
- preserve accepted ADR-0006 and ADR-0007 boundaries;
- retire or migrate stale `packages/maplibre-runtime/` references without creating a parallel package;
- decide package manager and lockfile;
- approve dependency and plugin governance;
- choose contract/schema/policy bindings;
- choose test home and CI enforcement;
- define consumer and migration strategy.

**Stop condition:** unresolved parallel runtime ownership or absent dependency policy.

### Stage 1 — Complete package scaffold

Add only the minimum metadata and tooling needed to:

- install deterministically;
- typecheck;
- lint;
- build;
- test;
- inspect package contents;
- keep publication denied;
- preserve the dependency-free `NullMapRuntime` rollback path while the exact renderer dependency and initial adapter await review.

**Stop condition:** build metadata implies an API or runtime dependency not yet approved.

### Stage 2 — Pure descriptor core

Implement pure, profile-bound values and transformations for accepted contracts:

- no DOM;
- no MapLibre import;
- no network;
- finite outcomes;
- negative-state fixtures;
- contract/schema tests.

**Stop condition:** semantics are missing or conflict with owning contracts/schemas.

### Stage 3 — Minimal adapter lifecycle

Implement one bounded adapter seam:

- accepted MapLibre dependency;
- create/destroy;
- KFM-shaped view state;
- no public raw handle;
- cleanup tests;
- import enforcement.

**Stop condition:** direct imports remain uncontrolled or runtime ownership remains conflicted.

### Stage 4 — Manifest-gated layer binding

Add source/layer activation only after:

- accepted descriptor contracts;
- integrity/release refs;
- endpoint policy;
- negative states;
- rollback behavior;
- synthetic browser fixtures.

**Stop condition:** activation can bypass release, policy, rights, sensitivity, or integrity.

### Stage 5 — Events and map context

Translate clicks/camera/time into bounded KFM-shaped candidates:

- no feature property as claim;
- no raw event leakage;
- evidence resolution remains downstream;
- telemetry redaction;
- accessibility alternatives.

### Stage 6 — Protocols and plugins

Add one protocol/plugin at a time with:

- admission decision;
- pinned dependency;
- supply-chain evidence;
- endpoint/resource policy;
- capability and denial tests;
- fallback and rollback.

### Stage 7 — Consumer adoption

- onboard one named consumer;
- run contract tests;
- update CI path filters;
- measure performance;
- document version compatibility;
- retain rollback.

### Stage 8 — Internal distribution

Only after all prior gates:

- build deterministic package artifacts;
- inspect contents;
- attach software provenance/SBOM as required;
- publish to an approved internal channel;
- retain prior version;
- record consumer deployment;
- keep map/data release authority separate.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

The package may be described as implemented only when:

- [ ] Owners and required reviewers are assigned.
- [x] Renderer/runtime package ownership is accepted through ADR-0006.
- [x] ADR-0006 is accepted with dependency and concrete implementation still held.
- [x] ADR-0007 accepts the renderer family; plugin and dependency admission remain separate.
- [x] Current workspace package manager/version and root lockfile are declared; renderer dependency admission remains separate.
- [ ] Package metadata is complete and tested beyond the exact dependency and focused test-script slice.
- [x] Exact `maplibre-gl@6.6.0` is declared only in the accepted package as a review-pending admission candidate.
- [ ] License, provenance, vulnerability, and transitive dependency reviews exist.
- [ ] Build, typecheck, lint, and package commands are real; the focused package test command is implemented.
- [x] The explicit export map keeps the root facade renderer-neutral and exposes the initial package-owned adapter only through `@kfm/maplibre/adapter`, without raw renderer types.
- [ ] Pure and effectful entry points are explicit.
- [x] The current renderer-neutral facade exposes no raw renderer types; full acquisition enforcement remains open.
- [ ] Manifest, evidence, policy, release, correction, withdrawal, and rollback bindings are implemented as required.
- [ ] Endpoint, protocol, plugin, worker, and asset policies are explicit.
- [ ] Sensitive geometry is transformed upstream.
- [x] The bounded renderer-neutral port exposes deterministic finite states and reason codes.
- [x] Package tests cover bounded adapter success and fail-closed paths; authenticated browser coverage remains open.
- [ ] Import-boundary enforcement is required in CI.
- [ ] CI watches `packages/maplibre/**`.
- [x] Bounded Explorer Web consumers and contract-style tests exist; the complete inventory remains open.
- [ ] Browser and capability support are documented and tested.
- [ ] Build outputs are reproducible and inspected.
- [ ] No secrets or private endpoints enter artifacts.
- [ ] Internal distribution, deprecation, correction, and rollback are documented and tested.
- [ ] Package release remains distinct from map/data publication.
- [ ] Documentation reflects actual behavior.

Until review and browser gates close, describe the package as a **private package with an exact MapLibre dependency candidate and an initial package-owned lifecycle/camera adapter; operational runtime readiness remains on HOLD**.

[Back to top](#top)

---

<a id="verification-register"></a>

## Verification register

| ID | Verification item | Status |
|---|---|---:|
| MAPLIBRE-PKG-001 | Assign package owner. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-002 | Assign MapLibre adapter/runtime owner. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-003 | Assign dependency and supply-chain reviewer. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-004 | Confirm package root as canonical runtime home. | RESOLVED — ADR-0006 ACCEPTED |
| MAPLIBRE-PKG-005 | Resolve `packages/maplibre-runtime/` references. | CONFLICTED — migrate stale references without parallel implementation |
| MAPLIBRE-PKG-006 | Accept, supersede, or narrow ADR-0006. | RESOLVED — ACCEPTED |
| MAPLIBRE-PKG-007 | Accept, supersede, or narrow ADR-0007. | RESOLVED — ACCEPTED renderer family; dependency/plugin admission separate |
| MAPLIBRE-PKG-008 | Resolve plugin-admission contract/schema/policy. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-009 | Select package manager. | RESOLVED for current workspace — pnpm 11.17.0 |
| MAPLIBRE-PKG-010 | Establish lockfile policy. | PARTIAL — root pnpm lock exists; renderer admission not established |
| MAPLIBRE-PKG-011 | Confirm supported Node tooling version. | RESOLVED for current workspace — >=22.13 <23 |
| MAPLIBRE-PKG-012 | Confirm TypeScript configuration. | UNKNOWN |
| MAPLIBRE-PKG-013 | Confirm module format. | PARTIAL — package declares ESM |
| MAPLIBRE-PKG-014 | Confirm bundler/build tooling. | UNKNOWN |
| MAPLIBRE-PKG-015 | Confirm browser target matrix. | UNKNOWN |
| MAPLIBRE-PKG-016 | Confirm source-map posture. | UNKNOWN |
| MAPLIBRE-PKG-017 | Complete package export map. | PARTIAL — root renderer-neutral facade exported |
| MAPLIBRE-PKG-018 | Complete files/sideEffects metadata. | PROPOSED |
| MAPLIBRE-PKG-019 | Approve MapLibre GL JS dependency/version. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-020 | Approve style-spec dependency posture. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-021 | Approve PMTiles protocol dependency. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-022 | Approve COG protocol dependency. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-023 | Approve 3D/plugin dependency set. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-024 | Establish license review. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-025 | Establish vulnerability threshold and update process. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-026 | Establish SBOM/provenance requirements. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-027 | Ratify KFM-shaped public API. | PARTIAL — renderer-neutral port accepted and implemented |
| MAPLIBRE-PKG-028 | Ratify finite outcomes/reason codes. | PARTIAL — renderer-neutral states/reasons implemented |
| MAPLIBRE-PKG-029 | Enforce raw renderer type containment. | PARTIAL — current facade contains no raw types |
| MAPLIBRE-PKG-030 | Enforce single-importer boundary. | PROPOSED |
| MAPLIBRE-PKG-031 | Inventory direct MapLibre imports. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-032 | Classify or migrate external-CDN smoke harness. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-033 | Define production endpoint allowlist/resolver. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-034 | Define CSP/worker/asset posture. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-035 | Bind accepted layer/source/style contracts. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-036 | Bind accepted schemas. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-037 | Bind policy and release decisions. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-038 | Bind integrity and rollback references. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-039 | Prove sensitive geometry is transformed upstream. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-040 | Choose executable test home. | CONFLICTED |
| MAPLIBRE-PKG-041 | Populate synthetic fixtures. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-042 | Add pure import-safety tests. | PROPOSED |
| MAPLIBRE-PKG-043 | Add lifecycle/cleanup tests. | PROPOSED |
| MAPLIBRE-PKG-044 | Add denial/abstention/rollback tests. | PROPOSED |
| MAPLIBRE-PKG-045 | Add endpoint/protocol/plugin tests. | PROPOSED |
| MAPLIBRE-PKG-046 | Add resource-limit tests. | PROPOSED |
| MAPLIBRE-PKG-047 | Add browser compatibility tests. | PROPOSED |
| MAPLIBRE-PKG-048 | Add package build/content inspection. | PROPOSED |
| MAPLIBRE-PKG-049 | Add dependency/license/vulnerability CI. | PROPOSED |
| MAPLIBRE-PKG-050 | Update CI to watch `packages/maplibre/**`. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-051 | Resolve `apps/web/**` versus `apps/explorer-web/**`. | CONFLICTED |
| MAPLIBRE-PKG-052 | Resolve permissive performance schema posture. | CONFLICTED |
| MAPLIBRE-PKG-053 | Resolve `artifacts/perf/` trust-artifact placement. | CONFLICTED |
| MAPLIBRE-PKG-054 | Inventory consumers and owners. | PARTIAL — Explorer Web imports confirmed |
| MAPLIBRE-PKG-055 | Add consumer contract tests. | PARTIAL — bounded Explorer port/evidence/status tests exist |
| MAPLIBRE-PKG-056 | Define versioning and changelog policy. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-057 | Define internal distribution channel. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-058 | Define software correction process. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-059 | Define deprecation period. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-060 | Prove package rollback. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-061 | Prove package release is not map/data publication. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-062 | Verify operational health from real consumers and telemetry. | UNKNOWN |

[Back to top](#top)

---

<a id="rollback-correction-deprecation-and-package-release"></a>

## Rollback, correction, deprecation, and package release

### Documentation-only rollback

For this README change:

- revert the documentation commit; or
- restore the prior blob recorded in the evidence snapshot.

No package behavior changes because this revision changes documentation only.

### Future package rollback

A mature package rollback should preserve:

- prior package artifact and checksum;
- prior dependency lock state;
- prior export/API contract;
- known consumer compatibility;
- deployment/build references;
- reason and approver;
- correction and migration notes;
- test evidence for the restored version.

Rollback must not:

- delete historical package versions from audit records;
- rewrite map/data release meaning;
- silently retarget public map releases;
- erase affected consumer or incident evidence;
- bypass security or sensitivity remediation.

### Relationship to map/data rollback

Software rollback and map/data rollback are separate operations.

A package rollback may require:

- consumer redeployment;
- renderer cache invalidation;
- disabling a plugin or protocol;
- restoring a prior bundle.

A map/data rollback may require:

- ReleaseManifest changes;
- withdrawal/correction notices;
- published artifact alias changes;
- registry/catalog updates;
- public communication.

One operation must not silently imply the other.

### Deprecation

Deprecation requires:

- named surface;
- replacement;
- affected consumers;
- first warning version;
- removal version/date;
- migration guide;
- compatibility tests;
- rollback plan;
- owner.

### Status summary

| Concern | Current status |
|---|---:|
| Package path | CONFIRMED |
| npm workspace enrollment | CONFIRMED |
| Package name/privacy/version | CONFIRMED private `@kfm/maplibre` `0.0.0` |
| Source entry | CONFIRMED facade exports |
| Source boundary README | CONFIRMED v1.2 correction |
| Renderer-neutral port/null runtime | IMPLEMENTED / BOUNDED |
| Concrete `MapLibreAdapter` | IMPLEMENTED / INITIAL LIFECYCLE-CAMERA SLICE |
| Package dependencies | EXACT `maplibre-gl@6.6.0` CANDIDATE / REVIEW PENDING |
| Package build/export | PARTIAL — source export map; no build output |
| Package tests | IMPLEMENTED / FIVE FOCUSED MOCKED TESTS |
| Consumers | PARTIAL — Explorer Web bounded imports/tests |
| ADR-0006 | ACCEPTED architecture; proposed dependency and initial implementation conform |
| ADR-0007 | ACCEPTED renderer family; browser/runtime HOLD |
| Runtime package ownership | CONFLICTED |
| Performance tooling | CONFIRMED adjacent tooling |
| Package-specific CI | NOT ESTABLISHED |
| Package publication | NOT AUTHORIZED |
| Truth/policy/release authority | NONE |
| Operational health | UNKNOWN |

> **Current safe description:** `packages/maplibre/` is the private accepted MapLibre seam. This draft proposes exact `maplibre-gl@6.6.0` admission and implements only lifecycle, camera, finite error, and teardown behavior. #2906 browser readiness, source/layer/plugin/protocol admission, distribution, release, deployment, and publication remain held or unauthorized.

[Back to top](#top)
