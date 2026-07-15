<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-maplibre-readme
title: packages/maplibre/ — MapLibre Package, Adapter, Distribution, and Compatibility Boundary
type: readme
version: v1.1
status: draft
owners: OWNER_TBD — Package steward · MapLibre adapter steward · Map-runtime steward · UI steward · Governed API steward · Contract steward · Schema steward · Policy steward · Security steward · Privacy/sensitivity reviewer · Dependency steward · Supply-chain steward · Validation steward · Release steward · Migration steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target existed before the current evidence-grounded revision
updated: 2026-07-15
policy_label: "public-doctrine; package-boundary; maplibre; renderer-adapter; implementation-placeholder; private-npm-package; workspace-enrolled; distribution-not-authorized; api-unratified; single-importer-proposed; sole-renderer-proposed; runtime-split-conflicted; renderer-downstream; released-artifacts-only; effect-boundary-explicit; network-posture-conflicted; sensitive-geometry-upstream; supply-chain-aware; fail-closed; no-truth-authority; no-publication-authority; migration-required; rollback-aware"
current_path: packages/maplibre/README.md
truth_posture: CONFIRMED target README v1, merged source-envelope README v1.1, private npm package metadata @kfm/maplibre version 0.0.0, source index.ts greenfield placeholder export, root npm workspace enrollment and placeholder generic lint/test/build scripts, MapLibre-specific root performance scripts, package/root placement, proposed ADR-0006 single-importer boundary, proposed ADR-0007 sole-browser-renderer decision, MapLibre architecture lane, app-local map-runtime README, MapLibre config/performance workflow and scripts, permissive legacy performance schema, executable performance-envelope validator wrapper, MapLibre validator/test/fixture README lanes, and bounded absence of package dependencies, exports, scripts, engines, build configuration, common root lockfiles, functional adapter modules, package-local tests, tests/packages/maplibre README, packages/maplibre-runtime README, package consumers, and package-watching CI / PROPOSED package metadata contract, accepted adapter ownership, dependency and supply-chain controls, export map, browser/runtime support matrix, KFM-shaped public API, manifest-gated renderer activation, plugin/protocol admission, package test matrix, import-boundary enforcement, consumer inventory, semantic versioning, internal distribution, correction, migration, deprecation, and rollback / CONFLICTED helper-only no-network wording versus an effectful renderer adapter, ADR-0006 package seam versus external CDN-based smoke harness outside the package, packages/maplibre versus referenced packages/maplibre-runtime ownership, ADR-0007 sole-renderer proposal versus unaccepted exception and plugin governance, canonical schema family versus permissive schemas/maplibre scaffold, tests/maplibre versus tests/packages/maplibre placement, apps/explorer-web versus workflow apps/web filter, repository-root performance tooling versus package-specific proof, and artifacts/perf trust-like outputs versus artifacts compatibility-root limits / UNKNOWN accepted adapter API, package manager and lockfile strategy, MapLibre dependency/version, plugin dependency set, build tooling, module format, TypeScript configuration, source maps, browser targets, package exports, actual consumers, runtime import inventory beyond bounded search, plugin/protocol allowlist, manifest resolver bindings, endpoint policy, CSP posture, contract/schema bindings, test pass rates, CI enforcement, internal release use, deployment use, and operational health / NEEDS VERIFICATION owners, ADR acceptance or supersession, renderer-runtime ownership decision, package metadata completion, dependency approval, lockfile policy, import allowlist, public API, contract/schema pairing, policy and release bindings, local hermetic fixtures, consumer migration, CI path filters, software distribution policy, correction path, deprecation window, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 96ae9619f3d38daeb7a2881c0ae691e31314177c
  prior_blob: 7aff988e18d5b113d8fb049f2ffd8c9e49bcf422
  source_readme_blob: eccacaa37463e222febaa9f0659d98d3a80486bf
  package_metadata_blob: b0582955feeb51016327113692fa5c98ecad8816
  source_entry_blob: 91664eb00583f9e3d0405eb7954fefa9a48f4ee9
  root_package_metadata_blob: 62f45306aef7376a2d68042b0c9e7f556edf0e78
  packages_root_blob: fc18fb3334fefe992a551fe12aa98c812232cd17
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  maplibre_architecture_blob: ff4b4754e5dc7beae22620ee669d3fdc240c44d7
  adapter_adr_blob: fba9562322a263876bb5b1096b8093746dd43990
  sole_renderer_adr_blob: c753f09db18e12081f99405b42cd79ebb89d0ac3
  config_readme_blob: a216d1b1f2203f781846512ea2cca7ac163adc4b
  map_runtime_readme_blob: 4d3897eda64d11f84f4805cb9cc2bc30a2ee333c
  validator_readme_blob: 7d29f8e5b5c215a5848803d87fd9f4c7549be105
  perf_workflow_blob: ad9dffbddc455411fef1eb35c83b513fa96eb3e0
  perf_smoke_blob: 699dd4cf42d355dd2ed7620852b7fd1f3000bbe2
  perf_schema_blob: 511e7f34ca84390fd5d000326ab33c46c3050fc4
  perf_validator_blob: 1f9e0f785a701da2a2b8f52bf73f4e97866d951d
  maplibre_tests_readme_blob: 4c5d24be322fcbff1a98aa255adc1be26b168ba6
  maplibre_fixtures_readme_blob: 3b6796d242157b22c8b6d2c1621c0b02178841f9
  bounded_path_checks:
    - packages/maplibre/README.md existed at version v1 before this revision
    - packages/maplibre/src/README.md exists at version v1.1
    - packages/maplibre/package.json exists with name @kfm/maplibre, private true, and version 0.0.0
    - packages/maplibre/src/index.ts exists and exports only placeholder = true
    - repository root package.json includes workspaces apps/* and packages/*
    - repository root lint, test, and build scripts are TODO echo placeholders
    - repository root contains MapLibre performance/proof script entry points and Playwright/pixelmatch/pngjs development dependencies
    - package-lock.json, pnpm-lock.yaml, and yarn.lock were not found as repository-root lockfiles at checked paths
    - packages/maplibre package metadata has no scripts, exports, dependencies, devDependencies, peerDependencies, engines, files, sideEffects, type, main, module, types, browser, or publishConfig fields
    - packages/maplibre/src/MapLibreAdapter.ts and functional source/layer/style/manifest/context/validation modules were not found
    - packages/maplibre/tests/README.md and tests/packages/maplibre/README.md were not found
    - tests/maplibre/README.md and tests/fixtures/maplibre/README.md exist as draft documentation lanes
    - packages/maplibre-runtime/README.md was not found
    - bounded code search found no @kfm/maplibre consumer import
    - ADR-0006 and ADR-0007 remain PROPOSED
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
  - ../../docs/architecture/map-master.md
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
  - "This revision changes only packages/maplibre/README.md."
  - "The package currently contains documentation, a private 0.0.0 npm manifest, and a placeholder TypeScript export; no functioning adapter or package consumer is established."
  - "This README does not accept ADR-0006 or ADR-0007, create a MapLibreAdapter, approve dependencies, admit plugins/protocols/endpoints, authorize package publication, or prove runtime consumers."
  - "The renderer may consume only governed, released, public-safe artifacts. Descriptor validity, package installation, and successful visual rendering are not truth, evidence closure, policy approval, or release approval."
  - "Package release is a software-distribution event, not KFM map/data/claim publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapLibre Package, Adapter, Distribution, and Compatibility Boundary

`packages/maplibre/`

> Repository-present private npm workspace package intended to become KFM's governed MapLibre renderer-adapter seam. Current evidence establishes documentation, a `0.0.0` package manifest, and a one-line placeholder export—not a functioning adapter, declared dependency set, buildable package, tested API, published distribution, or enforced single-importer boundary.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v1.1-informational)
![maturity](https://img.shields.io/badge/maturity-package__scaffold-lightgrey)
![package](https://img.shields.io/badge/package-%40kfm%2Fmaplibre-blue)
![distribution](https://img.shields.io/badge/distribution-private__not__authorized-critical)
![adapter](https://img.shields.io/badge/adapter-unratified-orange)
![renderer](https://img.shields.io/badge/renderer-downstream-blue)
![authority](https://img.shields.io/badge/truth__authority-none-red)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Responsibilities](#package-responsibilities) · [Conflicts](#compatibility-and-implementation-conflicts) · [Tree](#confirmed-package-tree) · [Invariants](#keystone-invariants) · [Metadata](#package-metadata-and-workspace-boundary) · [Dependencies](#dependency-and-supply-chain-boundary) · [Distribution](#distribution-and-publishing-posture) · [API](#public-api-and-export-boundary) · [Consumers](#consumer-and-import-boundary) · [Runtime](#renderer-runtime-and-source-boundary) · [Descriptors](#descriptor-manifest-and-release-boundary) · [Plugins](#plugin-protocol-and-network-boundary) · [Security](#security-rights-sensitivity-and-privacy) · [Performance](#performance-tooling-boundary) · [Testing](#testing-build-and-ci) · [Compatibility](#versioning-compatibility-and-consumer-migration) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Rollback](#rollback-correction-deprecation-and-package-release)

> [!IMPORTANT]
> **This README is not an implemented adapter, accepted ADR, dependency approval, export contract, plugin allowlist, endpoint allowlist, distribution authorization, schema, policy, release, or publication decision.** It does not establish the accepted MapLibre version, package manager, lockfile, build output, browser matrix, public API, consumer bindings, network policy, protocol registration, CI enforcement, or operational health.

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
| This README | **CONFIRMED v1 before revision** | A package-boundary document exists, but its Python-shaped layout was inconsistent with repository evidence. |
| `src/README.md` | **CONFIRMED v1.1** | The source envelope now documents the TypeScript placeholder state and proposed adapter boundary. |
| `package.json` | **CONFIRMED private `0.0.0` scaffold** | Distribution name is `@kfm/maplibre`; no scripts, exports, dependencies, engines, entry points, or build configuration are declared. |
| Root workspace enrollment | **CONFIRMED** | Root `package.json` includes `packages/*`, so this folder is inside the npm workspace pattern. |
| Root generic commands | **CONFIRMED placeholders** | `lint`, `test`, and `build` only echo TODO messages; they do not prove package checks. |
| Root MapLibre commands | **CONFIRMED performance-tooling entry points** | Repository scripts invoke smoke/performance/proof tooling, not this package's adapter implementation. |
| Root JavaScript lockfiles | **NOT FOUND at checked paths** | `package-lock.json`, `pnpm-lock.yaml`, and `yarn.lock` were absent at checked paths; dependency reproducibility is not established. |
| `src/index.ts` | **CONFIRMED placeholder** | It exports only `placeholder = true`; no public adapter behavior exists. |
| Functional adapter modules | **NOT ESTABLISHED** | No lifecycle adapter, descriptor compiler, protocol registrar, event bridge, or package validation implementation was found. |
| Package dependencies | **NONE DECLARED** | `maplibre-gl`, style-spec, PMTiles, COG, plugin, and runtime dependencies are not declared in the package manifest. |
| Package consumers | **NOT ESTABLISHED by bounded search** | No `@kfm/maplibre` consumer import was found. |
| Package-local tests | **NOT FOUND at checked paths** | No package test README or accepted package-local test suite is established. |
| MapLibre test lane | **CONFIRMED draft documentation** | `tests/maplibre/README.md` documents proposed proof obligations; executable tests and placement acceptance remain unproved. |
| MapLibre fixture lane | **CONFIRMED draft documentation** | `tests/fixtures/maplibre/README.md` documents synthetic fixtures; payload coverage and consumers remain unproved. |
| ADR-0006 | **CONFIRMED `proposed`** | The single-importer `MapLibreAdapter` seam is architectural intent, not accepted or enforced behavior. |
| ADR-0007 | **CONFIRMED `PROPOSED`** | Sole-browser-renderer and plugin-admission commitments are not accepted runtime authority. |
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
- The package manifest does not declare an adapter runtime, build, exports, dependencies, engines, files list, side-effect metadata, or publishing configuration.
- The source entry is a greenfield placeholder.
- The merged source README records the TypeScript source-envelope boundary.
- Root generic `lint`, `test`, and `build` scripts are placeholders.
- Root MapLibre scripts exercise performance/proof tooling outside the package.
- ADR-0006 and ADR-0007 remain proposed.
- MapLibre remains downstream of governed evidence, policy, review, release, correction, and rollback.
- No package consumer, package-local tests, package-specific build, or accepted runtime API was established by bounded inspection.

**PROPOSED**

- Package metadata completion and internal distribution rules.
- Accepted adapter/runtime ownership.
- Declared and pinned dependencies.
- An explicit export map and KFM-shaped API.
- Pure/effectful entry-point separation.
- Manifest-gated source/layer/style activation.
- Approved protocol/plugin registration.
- Dependency, license, vulnerability, provenance, and browser-compatibility gates.
- Package tests, import-boundary enforcement, consumer contract tests, and dedicated CI.
- Semantic versioning, consumer inventory, migration, deprecation, correction, and rollback.

**CONFLICTED**

- The prior helper-only blanket no-network wording versus the required effects of a browser renderer.
- `packages/maplibre/` as the proposed adapter seam versus repeated references to absent `packages/maplibre-runtime/`.
- ADR-0006's single-importer proposal versus repository-root smoke tooling loading MapLibre from a public CDN outside the package.
- ADR-0007's sole-renderer proposal versus unaccepted plugin-admission, exception-ADR, and supply-chain mechanisms.
- Canonical `schemas/contracts/v1/maplibre/` doctrine versus permissive `schemas/maplibre/` performance scaffolding.
- `tests/maplibre/` versus `tests/packages/maplibre/` as the executable test home.
- `apps/explorer-web/` doctrine versus `apps/web/**` in the performance workflow filter.
- Performance proof artifacts under `artifacts/perf/` versus the Directory Rules limitation on trust-bearing content in `artifacts/`.
- Rich package/source documentation versus a placeholder implementation.

**UNKNOWN**

- Accepted package manager and lockfile.
- Accepted MapLibre GL JS version and dependency range.
- Module format, TypeScript config, bundler, output directories, source maps, tree-shaking, and browser targets.
- Public export names and compatibility guarantees.
- Accepted consumers and deployment path.
- Runtime ownership between package and app-local feature code.
- Protocol, plugin, worker, sprite, glyph, tile, and endpoint allowlists.
- Contract/schema/policy/release bindings.
- Build reproducibility, artifact provenance, SBOM, license review, vulnerability thresholds, and dependency update process.
- Test coverage, CI enforcement, release use, and operational health.

**NEEDS VERIFICATION**

- Named owners and reviewers.
- ADR acceptance or supersession.
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

ADR-0006 proposes `packages/maplibre/` as the single runtime importer. Other docs reference `packages/maplibre-runtime/`, whose README was not found.

**Required resolution:**

- select one canonical package home;
- record the decision in an accepted ADR or migration note;
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

### 3. Single-importer proposal versus root smoke harness

The performance harness loads MapLibre through public CDN script tags outside `packages/maplibre/`.

**Required resolution before ADR-0006 acceptance:**

- classify the harness as a temporary test exception or migrate it behind the package;
- record any exception scope;
- pin and integrity-check assets;
- use local/hermetic fixtures by default;
- add import/network enforcement;
- ensure examples and tests cannot become production bypass patterns.

### 4. Sole-renderer proposal versus plugin governance

ADR-0007 proposes MapLibre GL JS plus an admitted plugin set as the sole browser renderer, but plugin contracts, policy decisions, pins, and supply-chain attestations remain proposed.

**Required resolution:**

- accept or supersede ADR-0007;
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
└── src/
    ├── README.md
    └── index.ts
```

Confirmed details:

- `package.json` contains only `name`, `private`, and `version`.
- `src/index.ts` contains only a placeholder export.
- No package-specific test directory was established.
- No accepted build output directory was established.
- No package-local TypeScript configuration, bundler configuration, changelog, license file, export map, or dependency declarations were established.
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

No package dependencies are currently declared. Before adding `maplibre-gl` or any runtime/plugin dependency, require:

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
| Core renderer | `maplibre-gl` | Single approved version/range; adapter-only import if ADR-0006 is accepted. |
| Style/type support | style-spec packages | Keep renderer-specific types inside package boundary. |
| Protocols | PMTiles, COG, vector-text protocols | Explicit registration, endpoint controls, integrity, cleanup, and admission. |
| 3D/custom layers | three.js, 3D Tiles, glTF, lidar, deck.gl integrations | Per-version PluginAdmission, supply-chain review, capability tests, fallback state. |
| Build tooling | TypeScript, bundler, declarations | Reproducible and package-scoped; no undeclared global tooling. |
| Test tooling | DOM/WebGL mocks, browser harness | Hermetic by default; live-network mode explicit and isolated. |
| Validation helpers | schema or runtime validators | Do not duplicate semantic contract authority. |

### Lockfile posture

Common root lockfiles were not found at checked paths. Until a package-manager and lockfile strategy is accepted:

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
- no exports;
- no build;
- no files list;
- no dependencies;
- no package tests;
- no consumer inventory;
- no package publication workflow;
- no accepted API.

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

No executable consumer import was established.

Before consumers depend on `@kfm/maplibre`, create a consumer inventory containing:

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

### Proposed import law

If ADR-0006 is accepted:

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

`0.0.0` is a scaffold marker. Before the first consumer:

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

### Stage 0 — Resolve governance

Before functional code:

- assign owners;
- accept or supersede ADR-0006;
- accept, supersede, or narrow ADR-0007;
- choose `packages/maplibre/` versus `packages/maplibre-runtime/`;
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
- preserve placeholder behavior until the API is accepted.

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
- [ ] Renderer/runtime package ownership is accepted.
- [ ] ADR-0006 is accepted, superseded, or explicitly deferred with bounded behavior.
- [ ] ADR-0007 and plugin admission posture are accepted, superseded, or narrowed.
- [ ] Package manager and lockfile policy are accepted.
- [ ] Package metadata is complete and tested.
- [ ] Approved dependencies and exact/range policy are declared.
- [ ] License, provenance, vulnerability, and transitive dependency reviews exist.
- [ ] Build, typecheck, lint, test, and package commands are real.
- [ ] Export map and public types are ratified.
- [ ] Pure and effectful entry points are explicit.
- [ ] Raw renderer types do not leak across the accepted boundary.
- [ ] Manifest, evidence, policy, release, correction, withdrawal, and rollback bindings are implemented as required.
- [ ] Endpoint, protocol, plugin, worker, and asset policies are explicit.
- [ ] Sensitive geometry is transformed upstream.
- [ ] Negative states are deterministic and visible.
- [ ] Package-local or accepted repository tests cover success and failure paths.
- [ ] Import-boundary enforcement is required in CI.
- [ ] CI watches `packages/maplibre/**`.
- [ ] Consumer inventory and contract tests exist.
- [ ] Browser and capability support are documented and tested.
- [ ] Build outputs are reproducible and inspected.
- [ ] No secrets or private endpoints enter artifacts.
- [ ] Internal distribution, deprecation, correction, and rollback are documented and tested.
- [ ] Package release remains distinct from map/data publication.
- [ ] Documentation reflects actual behavior.

Until then, describe the package as a **private workspace scaffold with proposed adapter responsibilities**.

[Back to top](#top)

---

<a id="verification-register"></a>

## Verification register

| ID | Verification item | Status |
|---|---|---:|
| MAPLIBRE-PKG-001 | Assign package owner. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-002 | Assign MapLibre adapter/runtime owner. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-003 | Assign dependency and supply-chain reviewer. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-004 | Confirm package root as canonical runtime home. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-005 | Resolve `packages/maplibre-runtime/` references. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-006 | Accept, supersede, or narrow ADR-0006. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-007 | Accept, supersede, or narrow ADR-0007. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-008 | Resolve plugin-admission contract/schema/policy. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-009 | Select package manager. | UNKNOWN |
| MAPLIBRE-PKG-010 | Establish lockfile policy. | UNKNOWN |
| MAPLIBRE-PKG-011 | Confirm supported Node tooling version. | UNKNOWN |
| MAPLIBRE-PKG-012 | Confirm TypeScript configuration. | UNKNOWN |
| MAPLIBRE-PKG-013 | Confirm module format. | UNKNOWN |
| MAPLIBRE-PKG-014 | Confirm bundler/build tooling. | UNKNOWN |
| MAPLIBRE-PKG-015 | Confirm browser target matrix. | UNKNOWN |
| MAPLIBRE-PKG-016 | Confirm source-map posture. | UNKNOWN |
| MAPLIBRE-PKG-017 | Complete package export map. | PROPOSED |
| MAPLIBRE-PKG-018 | Complete files/sideEffects metadata. | PROPOSED |
| MAPLIBRE-PKG-019 | Approve MapLibre GL JS dependency/version. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-020 | Approve style-spec dependency posture. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-021 | Approve PMTiles protocol dependency. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-022 | Approve COG protocol dependency. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-023 | Approve 3D/plugin dependency set. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-024 | Establish license review. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-025 | Establish vulnerability threshold and update process. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-026 | Establish SBOM/provenance requirements. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-027 | Ratify KFM-shaped public API. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-028 | Ratify finite outcomes/reason codes. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-029 | Enforce raw renderer type containment. | PROPOSED |
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
| MAPLIBRE-PKG-054 | Inventory consumers and owners. | NEEDS VERIFICATION |
| MAPLIBRE-PKG-055 | Add consumer contract tests. | PROPOSED |
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
| Source entry | CONFIRMED placeholder |
| Source boundary README | CONFIRMED v1.1 |
| Functional adapter | NOT ESTABLISHED |
| Package dependencies | NONE DECLARED |
| Package build/export | NOT ESTABLISHED |
| Package tests | NOT ESTABLISHED |
| Consumers | NOT ESTABLISHED |
| ADR-0006 | PROPOSED |
| ADR-0007 | PROPOSED |
| Runtime package ownership | CONFLICTED |
| Performance tooling | CONFIRMED adjacent tooling |
| Package-specific CI | NOT ESTABLISHED |
| Package publication | NOT AUTHORIZED |
| Truth/policy/release authority | NONE |
| Operational health | UNKNOWN |

> **Current safe description:** `packages/maplibre/` is a private npm workspace scaffold and documentation boundary for a proposed governed MapLibre adapter. It is not yet a functioning, installable, consumer-proven, CI-enforced, or distribution-authorized renderer package.

[Back to top](#top)
