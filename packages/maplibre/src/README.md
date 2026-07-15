<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-maplibre-src-readme
title: packages/maplibre/src/ — MapLibre Source Envelope and Renderer-Adapter Placement Boundary
type: readme
version: v1.1
status: draft
owners: OWNER_TBD — Package steward · MapLibre adapter steward · Map-runtime steward · UI steward · Governed API steward · Contract steward · Schema steward · Policy steward · Security steward · Privacy/sensitivity reviewer · Dependency steward · Validation steward · Release steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target existed before the current evidence-grounded revision
updated: 2026-07-15
policy_label: "public-doctrine; package-source-boundary; maplibre; renderer-adapter; implementation-placeholder; private-npm-package; api-unratified; single-importer-proposed; runtime-split-conflicted; renderer-downstream; released-artifacts-only; effect-boundary-explicit; network-posture-conflicted; sensitive-geometry-upstream; fail-closed; no-truth-authority; no-publication-authority; migration-required; rollback-aware"
current_path: packages/maplibre/src/README.md
truth_posture: CONFIRMED target README v1, packages/maplibre private package metadata @kfm/maplibre version 0.0.0, source index.ts greenfield placeholder export, package/root placement, proposed ADR-0006 single-importer boundary, MapLibre architecture lane, app-local map-runtime README, MapLibre config/performance workflow and scripts, permissive legacy performance schema, executable performance-envelope validator wrapper, MapLibre validator/test/fixture README lanes, and bounded absence of a source namespace directory, functional adapter modules, package-local tests, tests/packages/maplibre README, and packages/maplibre-runtime README / PROPOSED TypeScript source envelope, KFM-shaped renderer port, adapter lifecycle, manifest-gated source/layer/style binding, event translation, protocol/plugin admission, finite negative states, pure/effectful module separation, import-boundary enforcement, local fixtures, package tests, CI gates, correction, migration, deprecation, and rollback / CONFLICTED helper-only no-network wording versus an effectful renderer adapter, ADR-0006 package seam versus external CDN-based smoke harness outside the package, package/maplibre versus referenced package/maplibre-runtime ownership, canonical schema family versus permissive schemas/maplibre scaffold, tests/maplibre versus tests/packages/maplibre placement, apps/explorer-web versus workflow apps/web filter, and artifacts/perf trust-like outputs versus artifacts compatibility-root limits / UNKNOWN accepted adapter API, package build tooling, dependency declarations, source-map and browser targets, actual consumers, runtime import inventory beyond bounded search, plugin/protocol allowlist, manifest resolver bindings, network endpoint policy, source/layer/style contract bindings, test pass rates, CI enforcement, release use, and operational health / NEEDS VERIFICATION owners, ADR acceptance or supersession, renderer-runtime ownership decision, package metadata, dependency approval, import allowlist, public API, contract/schema pairing, policy and release bindings, local hermetic fixtures, consumer migration, CI path filters, correction path, deprecation window, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 3bf8b1440669bd77bb2ad35d047b290bb3f9c5ca
  prior_blob: f92eb9de4e19ac3083e3e5eca91cba425af545ea
  package_readme_blob: 7aff988e18d5b113d8fb049f2ffd8c9e49bcf422
  package_metadata_blob: b0582955feeb51016327113692fa5c98ecad8816
  source_entry_blob: 91664eb00583f9e3d0405eb7954fefa9a48f4ee9
  packages_root_blob: fc18fb3334fefe992a551fe12aa98c812232cd17
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  maplibre_architecture_blob: ff4b4754e5dc7beae22620ee669d3fdc240c44d7
  adapter_adr_blob: fba9562322a263876bb5b1096b8093746dd43990
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
    - packages/maplibre/src/README.md existed at version v1 before this revision
    - packages/maplibre/package.json exists with name @kfm/maplibre, private true, and version 0.0.0
    - packages/maplibre/src/index.ts exists and exports only placeholder = true
    - packages/maplibre/pyproject.toml was not found
    - packages/maplibre/src/maplibre/README.md was not found
    - packages/maplibre/src/MapLibreAdapter.ts was not found
    - package source search exposed no functional source/layer/style/manifest/context/validation modules
    - packages/maplibre/tests/README.md and tests/packages/maplibre/README.md were not found
    - tests/maplibre/README.md and tests/fixtures/maplibre/README.md exist as draft documentation lanes
    - packages/maplibre-runtime/README.md was not found
    - bounded code search found no @kfm/maplibre consumer import
    - scripts/maplibre-smoke-perf.mjs loads MapLibre GL JS and glyph assets from public external URLs
    - .github/workflows/maplibre-perf-governance.yml exists but does not watch packages/maplibre/** and watches apps/web/** rather than apps/explorer-web/**
    - schemas/maplibre/perf-envelope.schema.json is an open object scaffold with additionalProperties true and no required fields
related:
  - ../README.md
  - index.ts
  - ../package.json
  - ../../README.md
  - ../../geo/README.md
  - ../../hashing/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/map-first.md
  - ../../../docs/architecture/maplibre.md
  - ../../../docs/architecture/map-master.md
  - ../../../docs/architecture/maplibre-master.md
  - ../../../docs/architecture/map-shell.md
  - ../../../docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - ../../../docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - ../../../configs/maplibre/README.md
  - ../../../apps/explorer-web/src/features/map_runtime/README.md
  - ../../../tools/validators/maplibre/README.md
  - ../../../tools/validators/maplibre/validate_perf_envelope.py
  - ../../../tests/maplibre/README.md
  - ../../../tests/fixtures/maplibre/README.md
  - ../../../.github/workflows/maplibre-perf-governance.yml
  - ../../../scripts/maplibre-smoke-perf.mjs
  - ../../../schemas/maplibre/perf-envelope.schema.json
  - ../../../contracts/
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../data/registry/
  - ../../../data/catalog/
  - ../../../data/published/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../release/
tags: [kfm, packages, maplibre, src, typescript, renderer-adapter, map-runtime-port, source-descriptor, layer-descriptor, style-manifest, release-manifest, evidence-ref, negative-state, protocol-admission, pmtiles, cog, performance, import-boundary, privacy, migration, rollback]
notes:
  - "This revision changes only packages/maplibre/src/README.md."
  - "The source envelope currently contains this README and index.ts; index.ts exports only a greenfield placeholder."
  - "This README does not accept ADR-0006, create a MapLibreAdapter, approve package dependencies, admit plugins/protocols/endpoints, authorize package publication, or prove runtime consumers."
  - "The renderer may consume only governed, released, public-safe artifacts. Descriptor validity and visual rendering are not truth, evidence closure, policy approval, or release approval."
  - "Effectful renderer operations must be isolated from pure descriptor compilation; a blanket no-network claim is not credible for an implemented browser renderer and must be replaced by explicit admitted-effect rules."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapLibre Source Envelope and Renderer-Adapter Placement Boundary

`packages/maplibre/src/`

> Repository-present TypeScript source envelope for the future KFM MapLibre adapter seam. Current evidence establishes this README and a one-line greenfield placeholder export—not a functioning renderer adapter, descriptor compiler, protocol registrar, tested package, or enforced single-importer boundary.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v1.1-informational)
![maturity](https://img.shields.io/badge/maturity-placeholder__source-lightgrey)
![runtime](https://img.shields.io/badge/runtime-adapter__unratified-orange)
![renderer](https://img.shields.io/badge/renderer-downstream-blue)
![effects](https://img.shields.io/badge/effects-explicit__only-critical)
![release](https://img.shields.io/badge/released__artifacts-only-critical)
![authority](https://img.shields.io/badge/truth__authority-none-red)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Responsibilities](#source-envelope-responsibilities) · [Conflicts](#compatibility-and-implementation-conflicts) · [Tree](#confirmed-and-proposed-source-tree) · [Invariants](#keystone-invariants) · [Imports](#import-and-dependency-direction) · [Pure/effect split](#pure-and-effectful-module-boundary) · [Adapter](#renderer-adapter-contract) · [Descriptors](#descriptor-and-manifest-boundary) · [Events](#map-context-and-event-boundary) · [Protocols](#protocol-plugin-and-network-boundary) · [Negative states](#negative-state-contract) · [Security](#security-rights-sensitivity-and-privacy) · [Performance](#performance-tooling-boundary) · [Testing](#testing-fixtures-and-ci) · [Migration](#compatibility-and-migration) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Rollback](#rollback-correction-and-deprecation)

> [!IMPORTANT]
> **This README is not an implemented adapter, accepted ADR, runtime contract, dependency approval, plugin allowlist, endpoint allowlist, schema, policy, release, or publication decision.** It does not establish the exported API, accepted MapLibre version, consumer bindings, network policy, release-manifest resolver, protocol registration, browser support, CI enforcement, or operational health.

> [!CAUTION]
> **MapLibre draws released artifacts; it does not decide what is true.** A source, layer, style, tile, popup, screenshot, camera state, feature property, or successful render is never evidence closure, policy approval, review approval, release approval, or public truth by itself.

---

<a id="purpose"></a>

## Purpose

This README defines the source-code responsibility boundary under `packages/maplibre/src/`.

The source envelope may eventually contain the reusable implementation seam that:

- isolates approved `maplibre-gl` runtime imports behind one KFM-shaped adapter;
- translates governed layer, source, style, release, evidence, policy, and rollback inputs into bounded renderer operations;
- prevents raw MapLibre objects and event types from leaking into apps, shared UI, domain packages, or governed API contracts;
- separates deterministic descriptor compilation from effectful browser/runtime behavior;
- verifies required manifest and release support before source or layer activation;
- translates renderer events into bounded KFM map-context and claim-resolution candidates;
- registers approved protocols and plugins in one auditable location;
- exposes explicit negative states instead of hiding denial, abstention, staleness, or rollback in style behavior;
- supports deterministic local tests and import-boundary enforcement.

It must not become:

- a source registry, layer registry, catalog, tile store, style registry, release store, receipt store, proof store, or lifecycle-data home;
- a schema, semantic contract, policy, evidence resolver, citation validator, or publication authority;
- a direct RAW, WORK, QUARANTINE, connector, canonical-store, database, object-store, graph-store, vector-store, or model-runtime client;
- an app shell, Evidence Drawer, Focus Mode, public API route, search surface, export surface, or AI answer surface;
- a geoprivacy transform engine that merely hides precise data through client-side style filters;
- a general network client or arbitrary URL loader;
- a second renderer package parallel to an accepted adapter seam without an ADR;
- a place where raw renderer types become shared KFM contracts.

The package root governs package metadata and distribution. This `src/` README governs source placement, module decomposition, import direction, side effects, adapter isolation, and the evidence required before source files are added.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| This README | **CONFIRMED v1 before revision** | A source-boundary document exists. |
| `src/index.ts` | **CONFIRMED placeholder** | It exports only `placeholder = true`; no adapter behavior is established. |
| `package.json` | **CONFIRMED private `0.0.0` scaffold** | Distribution name is `@kfm/maplibre`; build scripts, exports, dependencies, engines, and entry points are absent. |
| Python package layout | **NOT APPLICABLE / prior proposal contradicted** | `pyproject.toml` and `src/maplibre/` were not found; current evidence is a JavaScript/TypeScript package. |
| Functional source modules | **NOT ESTABLISHED** | No `MapLibreAdapter.ts`, source/layer/style compiler, protocol registrar, event bridge, or validation module was found. |
| Package consumers | **NOT ESTABLISHED by bounded search** | No `@kfm/maplibre` consumer import was found. |
| Package-local tests | **NOT FOUND at checked paths** | Neither `packages/maplibre/tests/README.md` nor `tests/packages/maplibre/README.md` was found. |
| MapLibre test lane | **CONFIRMED README / execution unknown** | `tests/maplibre/README.md` documents a proposed executable lane; test inventory and runner remain unproved. |
| MapLibre fixtures | **CONFIRMED README lanes / payload use unknown** | Tiny, baseline, invalid, and bad-baseline documentation lanes exist. |
| Adapter ADR | **CONFIRMED proposed ADR** | ADR-0006 proposes a single importer and KFM-shaped adapter; acceptance and enforcement are not established. |
| Architecture lane | **CONFIRMED documentation** | Renderer-downstream and released-artifact rules are documented. |
| App-local map runtime | **CONFIRMED README / runtime unknown** | Explorer Web documents a `MapRuntimePort`/adapter handoff but does not prove code or wiring. |
| Referenced `packages/maplibre-runtime/` | **NOT FOUND at checked README path** | Ownership between helper and runtime package remains unresolved. |
| Performance workflow | **CONFIRMED executable workflow** | It runs validators and a browser smoke harness, but does not watch this package path. |
| Performance smoke harness | **CONFIRMED executable script** | It launches Playwright and loads MapLibre/glyph assets from external URLs. |
| Performance schema | **CONFIRMED permissive scaffold** | It accepts any JSON object and does not prove field-level governance. |
| General MapLibre validator lane | **CONFIRMED README-led routing** | Broad validation is documented; executable general adapter validation is not established. |

### Truth posture

**CONFIRMED**

- The current package is an npm-style private package named `@kfm/maplibre`.
- The source envelope contains a placeholder TypeScript entry point.
- There is no verified functional adapter implementation in this package.
- MapLibre is doctrinally downstream of governed evidence, policy, review, release, correction, and rollback.
- The current performance lane is real but separate from this package's unimplemented adapter source.
- The current performance harness is not hermetic because it loads public CDN assets.
- The dedicated performance workflow does not include `packages/maplibre/**` in its path filters.
- The legacy performance schema is intentionally or effectively non-restrictive.
- Test and fixture README lanes exist, but executable package behavior is not proved.

**PROPOSED**

- One TypeScript adapter seam for approved MapLibre imports.
- A pure/effectful module split.
- Typed KFM-facing ports and immutable input/result types.
- Manifest-gated source, layer, style, protocol, and plugin activation.
- Renderer event translation into KFM-shaped candidates.
- Explicit capability and negative-state models.
- Import-boundary linting and dependency checks.
- Local, deterministic browser fixtures and adapter contract tests.
- A migration from external CDN smoke loading to pinned, reviewed dependencies or hermetic fixtures.

**CONFLICTED**

- The prior README's Python-shaped module proposal versus the actual npm/TypeScript scaffold.
- “Helper-only, no-network” wording versus ADR-0006's effectful runtime-adapter responsibilities.
- `packages/maplibre/` as the proposed adapter seam versus architecture references to absent `packages/maplibre-runtime/`.
- ADR-0006's single-importer intent versus a standalone smoke harness that loads the MapLibre runtime outside the package.
- `schemas/contracts/v1/maplibre/` as the proposed governed schema family versus the current permissive `schemas/maplibre/` performance schema.
- `tests/maplibre/` versus `tests/packages/maplibre/` as package test placement.
- `apps/explorer-web/` as the documented app shell versus the workflow's `apps/web/**` filter.
- Trust-like performance proof/release/rollback outputs under `artifacts/perf/` versus Directory Rules limits on `artifacts/`.
- Synthetic/no-network test doctrine versus current external CDN use.

**UNKNOWN**

- Accepted MapLibre GL JS and style-spec versions.
- Whether root workspace tooling builds this package.
- TypeScript compiler/bundler settings and browser targets.
- The future public export surface.
- The actual runtime consumer and deployment path.
- The complete renderer-import inventory.
- Source, layer, style, event, protocol, and plugin contract bindings.
- Network allowlist and CSP posture.
- Release-manifest lookup and verification behavior.
- Package test pass rates and CI enforcement.
- Operational performance, accessibility, error, and rollback behavior.

**NEEDS VERIFICATION**

- Owners and review duties.
- ADR-0006 acceptance, revision, or supersession.
- Whether `packages/maplibre/` owns both pure helpers and the effectful runtime adapter.
- Whether `packages/maplibre-runtime/` should be created, removed from doctrine, or treated as a compatibility proposal.
- Package scripts, exports, dependencies, engines, and build output.
- Exact public API and raw renderer type restrictions.
- Accepted contracts, schemas, policy bundles, manifest types, and reason codes.
- Protocol/plugin/endpoint admission.
- Consumer migration and import allowlist.
- Test-home decision and fixture payload inventory.
- Workflow path filters and hermeticity.
- Correction, deprecation, and rollback automation.

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

`packages/maplibre/src/` is inside the `packages/` responsibility root for shared reusable implementation.

The placement is appropriate **only** when the source remains a reusable renderer-adapter or renderer-helper library. It does not inherit authority over adjacent roots.

| Responsibility | Owning home | Source-envelope rule |
|---|---|---|
| MapLibre adapter implementation | `packages/maplibre/src/` if ADR-approved | May implement the renderer seam; must stay subordinate to governed inputs. |
| Package metadata and publishing | `packages/maplibre/package.json` and workspace tooling | `src/` must not silently define package distribution. |
| App-local map orchestration | `apps/explorer-web/` | Consumes the adapter through a stable port; does not import raw renderer APIs. |
| Shared UI | `packages/ui/` | Uses KFM-shaped props/events, not MapLibre types or handles. |
| Map doctrine | `docs/architecture/`, `docs/doctrine/` | Explains renderer and trust rules; code conforms but does not redefine them. |
| Object meaning | `contracts/` | Layer, style, release, context, evidence, and receipt meaning stay outside source. |
| Machine shape | `schemas/contracts/v1/` after accepted reconciliation | Source validates or consumes schemas; it does not become schema authority. |
| Policy and sensitivity | `policy/` | Source consumes finite decisions and obligations; it does not make policy. |
| Source/layer registries | `data/registry/`, `data/catalog/` | Source may consume released refs; it must not mutate registry authority. |
| Released artifacts | `data/published/` and release-approved homes | Renderer consumes public-safe released derivatives only. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Adapter may return receipt-ready facts; storage and authority remain separate. |
| Release/correction/rollback | `release/` | Adapter enforces supplied state; it never approves release. |
| Validators | `tools/validators/maplibre/` | Validator orchestration remains outside package runtime code. |
| Tests and fixtures | accepted `tests/` and fixture lanes | Prove behavior without becoming implementation or trust stores. |
| Performance scripts | `scripts/` until graduated | External tooling; not evidence of package implementation. |

### Public-path rule

Normal public UI surfaces must not use package internals to bypass governed APIs, released artifacts, manifest checks, policy, evidence resolution, review state, correction state, or rollback state.

The adapter may receive approved URLs and handles through explicit typed inputs. It must not discover, infer, or manufacture trust from a URL, filename, renderer response, style object, or successful network load.

[Back to top](#top)

---

<a id="source-envelope-responsibilities"></a>

## Source-envelope responsibilities

This source envelope owns, once accepted and implemented:

1. **Source placement** — where adapter and pure renderer-binding code lives.
2. **Dependency direction** — renderer dependencies point inward to the adapter; KFM contracts remain renderer-agnostic.
3. **Runtime isolation** — raw MapLibre APIs and event objects do not leak across the seam.
4. **Effect isolation** — network, DOM, WebGL, protocol, worker, and renderer lifecycle effects remain explicit.
5. **Manifest gating** — no source/layer/style/protocol activation without required supplied support.
6. **Negative-state fidelity** — denial, abstention, invalidity, staleness, withdrawal, and rollback are first-class.
7. **Event translation** — clicks and camera changes become bounded candidates, not claims.
8. **Capability reporting** — callers can inspect admitted renderer capabilities without probing hidden globals.
9. **Deterministic pure helpers** — descriptor compilation and validation can run without browser or network effects.
10. **Reversibility** — consumers depend on a stable port so renderer upgrades or replacement remain bounded.

This source envelope does **not** own:

- source acquisition or admission;
- descriptor semantic meaning;
- evidence resolution;
- policy evaluation;
- sensitive-geometry transformation;
- release approval;
- artifact storage;
- public API assembly;
- UI composition;
- screenshot truth or visual proof;
- AI interpretation.

[Back to top](#top)

---

<a id="compatibility-and-implementation-conflicts"></a>

## Compatibility and implementation conflicts

### 1. Language and layout

The existing package metadata is JavaScript/npm-oriented and the source entry is `index.ts`. The prior README proposed a Python package namespace with `__init__.py` and `py.typed`.

**Disposition:** treat the Python tree as superseded planning prose. Do not create `src/maplibre/` or Python files unless a separate language ADR changes the package.

### 2. Helper package versus runtime adapter

The package README describes descriptor helpers. ADR-0006 proposes that this package be the sole importer and effectful MapLibre adapter.

**Disposition:** this needs an explicit ownership decision. The smallest coherent design is one package with a strict internal split between:

- pure descriptor and type modules; and
- one effectful runtime adapter sublane.

A separate `packages/maplibre-runtime/` must not be created in parallel without an ADR or migration plan.

### 3. Blanket no-network versus renderer effects

Pure helper functions should be no-network. A browser renderer adapter necessarily causes network, worker, DOM, and WebGL effects when loading admitted artifacts.

**Disposition:** replace blanket “no network” with:

- no hidden or arbitrary network access;
- no source discovery;
- no direct connector/internal-store access;
- only caller-supplied, policy- and release-admitted URLs/protocols;
- effectful methods isolated behind the adapter;
- deterministic local/no-network unit and contract tests;
- separately labeled integration/performance tests where network is intentionally enabled.

### 4. Single-importer proposal versus smoke harness

ADR-0006 proposes that only the adapter package access MapLibre runtime dependencies. The current smoke harness loads MapLibre GL JS from `unpkg.com` and glyphs from `demotiles.maplibre.org`.

**Disposition:** until ADR acceptance, classify this as a tooling exception requiring review. Before accepting the single-importer rule, either:

- move the smoke harness behind the package adapter;
- document a narrow test-only exception with enforcement and expiry; or
- revise the ADR to distinguish imports, browser injection, and test harnesses.

### 5. Package versus absent runtime package

Architecture/config/app docs reference `packages/maplibre-runtime/`, but the named README is absent.

**Disposition:** do not create both homes. Choose one responsibility owner and update docs through an ADR/migration note.

### 6. Schema authority

The performance validator reads `schemas/maplibre/perf-envelope.schema.json`, which accepts any object. Architecture proposes governed shapes under `schemas/contracts/v1/maplibre/`.

**Disposition:** do not use the permissive performance schema as evidence that source/layer/style/manifest contracts are enforced. Reconcile schema authority before adapter DTOs stabilize.

### 7. CI path coverage

The MapLibre performance workflow watches scripts, configs, validators, fixtures, `schemas/maplibre/**`, and `apps/web/**`, but not `packages/maplibre/**` and not the documented `apps/explorer-web/**`.

**Disposition:** source changes require package-specific build/test/import-boundary checks. The performance workflow is not sufficient proof for this package.

### 8. Test-home ambiguity

`tests/maplibre/` exists as a proposed lane, while older package docs point to `tests/packages/maplibre/`.

**Disposition:** select one canonical executable test home and make the other a documented compatibility pointer or remove it.

### 9. Trust artifacts under `artifacts/perf/`

The performance workflow builds proof-pack, release-manifest, correction, rollback, and failure-bundle-like outputs under `artifacts/perf/`.

**Disposition:** these are CI artifacts unless governed promotion moves accepted trust records to their canonical homes. Their names do not make them release or proof authority.

[Back to top](#top)

---

<a id="confirmed-and-proposed-source-tree"></a>

## Confirmed and proposed source tree

### Confirmed

```text
packages/maplibre/
├── README.md
├── package.json                  # @kfm/maplibre; private; 0.0.0
└── src/
    ├── README.md                 # this file
    └── index.ts                  # greenfield placeholder export only
```

### Proposed after ownership and API decisions

```text
packages/maplibre/src/
├── README.md
├── index.ts                      # intentional public exports only
├── core/
│   ├── types.ts                  # KFM-shaped immutable input/result types
│   ├── source-candidate.ts       # pure descriptor compilation
│   ├── layer-candidate.ts        # pure descriptor compilation
│   ├── style-candidate.ts        # pure style binding checks
│   ├── manifest-refs.ts          # immutable ref carriers
│   ├── capabilities.ts           # admitted capability model
│   ├── negative-states.ts        # finite renderer states/reasons
│   └── validation.ts             # local structural checks, not policy
├── runtime/
│   ├── maplibre-adapter.ts       # sole approved runtime seam
│   ├── lifecycle.ts              # create/destroy and state transitions
│   ├── sources.ts                # gated add/remove source effects
│   ├── layers.ts                 # gated add/remove layer effects
│   ├── styles.ts                 # bounded style application
│   ├── events.ts                 # renderer event -> KFM candidate translation
│   ├── protocols.ts              # admitted protocol registration
│   ├── plugins.ts                # admitted plugin binding
│   └── network.ts                # explicit URL/protocol enforcement
└── internal/
    ├── errors.ts                 # stable internal error mapping
    └── assertions.ts             # invariant checks
```

Every proposed file requires a confirmed responsibility, accepted contract/profile, tests, consumer need, and rollback plan. Do not create the entire tree merely because it is documented.

### Stop conditions

Do not add functional modules until:

- adapter ownership is decided;
- package metadata/build tooling is accepted;
- raw renderer type leakage rules are defined;
- contract/schema/policy/release dependencies are identified;
- import-boundary enforcement is selected;
- local test fixtures are available;
- effects and network posture are approved.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

1. **Renderer downstream.** MapLibre never creates canonical truth, evidence closure, policy, review, or release state.
2. **Released artifacts only.** Public rendering cannot activate RAW, WORK, QUARANTINE, unpublished, internal, or direct-model paths.
3. **Verify before activation.** Required descriptors, manifests, integrity refs, policy decisions, and release state are checked before `addSource`, `addLayer`, style replacement, protocol registration, or plugin activation.
4. **Sensitive geometry upstream.** Generalization, aggregation, omission, delay, redaction, or denial occurs before public rendering—not through client-side hiding.
5. **One renderer seam.** If ADR-0006 is accepted, all runtime imports and raw renderer types remain inside the adapter package.
6. **No raw event authority.** Feature properties and renderer events are candidates for governed resolution, not claims.
7. **Negative states visible.** Denied, restricted, abstained, stale, withdrawn, invalid, unavailable, unsigned, and rollback-mismatched states remain explicit.
8. **Effects explicit.** DOM, WebGL, worker, protocol, network, and runtime mutations occur only in effectful adapter modules.
9. **Pure core deterministic.** Descriptor compilation and local validation have explicit inputs, no ambient globals, and stable outputs.
10. **No URL-as-trust.** A reachable URL or successful load is not admission, integrity, evidence, or release.
11. **No style-as-policy.** Visibility, filters, opacity, clipping, and source-layer selection cannot substitute for policy or sensitive transforms.
12. **No visual-proof collapse.** Screenshots, render diffs, maps, legends, and scenes are review carriers, not sovereign proof.
13. **Correction and rollback preserved.** Supersession, withdrawal, correction, and rollback context remain visible through renderer state.
14. **Public clients use governed interfaces.** Package internals do not become a shortcut around the trust membrane.
15. **Reversible change.** API, dependency, renderer-version, plugin, protocol, and network changes have migration and rollback paths.

[Back to top](#top)

---

<a id="import-and-dependency-direction"></a>

## Import and dependency direction

### Allowed direction

```text
contracts / schemas / policy / release records
                   ↓
governed API and app-owned resolvers
                   ↓
KFM-shaped adapter inputs
                   ↓
packages/maplibre core
                   ↓
packages/maplibre runtime adapter
                   ↓
approved MapLibre runtime / protocols / plugins
```

### Required rules

- Package source may import approved renderer dependencies only inside the effectful runtime seam.
- Apps and shared UI import the adapter's KFM-shaped public surface, not `maplibre-gl`.
- Contracts and schemas must not import package code.
- Domain packages must not depend on MapLibre types.
- `packages/ui/` must not receive raw `Map`, `MapMouseEvent`, `LngLat`, source, layer, or style-spec runtime objects.
- Validation tools may import pure package functions only when that dependency does not make package code semantic authority.
- Runtime adapter code must not import data stores, connector clients, model clients, policy engines, or release writers.
- Package source must not dynamically import unapproved renderer plugins from caller-controlled names or URLs.
- Test-only imports and runtime injection exceptions must be explicit, linted, documented, and bounded.

### Public entry point

`src/index.ts` should eventually export only stable KFM-shaped interfaces and functions. It must not export:

- raw MapLibre map handles;
- raw renderer event types;
- internal protocol registries;
- arbitrary fetch helpers;
- unbounded plugin loaders;
- secret-bearing endpoint types;
- registry, policy, evidence, or release writers.

[Back to top](#top)

---

<a id="pure-and-effectful-module-boundary"></a>

## Pure and effectful module boundary

### Pure core

Pure modules may:

- validate locally supplied descriptor fields;
- normalize only where an accepted profile explicitly permits it;
- compile immutable source/layer/style candidates;
- compare declared IDs and refs;
- map finite decision inputs to finite renderer states;
- produce stable reason codes;
- calculate deterministic cache keys through approved hashing helpers;
- serialize receipt-ready facts without writing receipts.

Pure modules must not:

- access `window`, `document`, WebGL, workers, network, filesystem, environment variables, clocks, random values, or hidden global registries;
- infer missing release, policy, evidence, rights, attribution, or sensitivity facts;
- fetch TileJSON, PMTiles, styles, glyphs, sprites, or manifests;
- mutate caller inputs.

### Effectful runtime

Effectful adapter modules may, after accepted gating:

- create and destroy the MapLibre runtime;
- bind an approved container;
- add or remove admitted sources and layers;
- apply admitted styles and view state;
- register approved protocols/plugins once;
- subscribe to renderer events;
- translate events into KFM-shaped candidates;
- expose bounded health and capability state.

Effectful modules must:

- receive all approved refs, URLs, constraints, and finite decisions explicitly;
- enforce endpoint/protocol/plugin admission;
- reject unresolved or contradictory state;
- clean up listeners, workers, protocols, and map instances;
- avoid hidden retries that change policy or release semantics;
- return stable results rather than leak renderer exceptions directly.

[Back to top](#top)

---

<a id="renderer-adapter-contract"></a>

## Renderer-adapter contract

A future adapter surface should remain small and KFM-shaped. Illustrative names below are **PROPOSED**, not implemented exports.

```ts
export interface MapRuntimePort {
  create(input: CreateMapInput): Promise<AdapterResult<RuntimeState>>;
  destroy(): Promise<AdapterResult<void>>;
  bindSource(input: ReleasedSourceBinding): Promise<AdapterResult<SourceBinding>>;
  bindLayer(input: ReleasedLayerBinding): Promise<AdapterResult<LayerBinding>>;
  removeLayer(layerId: string): Promise<AdapterResult<void>>;
  removeSource(sourceId: string): Promise<AdapterResult<void>>;
  setView(view: GovernedViewState): AdapterResult<void>;
  setTime(context: ReleasedTimeContext): AdapterResult<void>;
  queryClick(point: ScreenPoint): Promise<AdapterResult<ClickCandidate[]>>;
  capabilities(): RendererCapabilities;
  health(): RuntimeHealth;
}
```

### Adapter inputs

Inputs should carry, where material:

- stable layer/source/style identifiers;
- contract/schema/profile versions;
- source role and attribution;
- CRS, bounds, zoom, tiling scheme, and tile format;
- artifact and manifest refs;
- evidence and citation-validation refs;
- finite policy decision and obligations;
- audience/sensitivity posture;
- release, correction, supersession, withdrawal, and rollback refs;
- approved endpoint/protocol/plugin identifiers;
- time context and freshness state.

### Adapter results

Results should include:

- finite status;
- stable reason codes;
- candidate/binding identifiers;
- capability or health changes;
- receipt-ready operation facts;
- safe diagnostics;
- no sensitive payload echo;
- no raw renderer object leakage.

[Back to top](#top)

---

<a id="descriptor-and-manifest-boundary"></a>

## Descriptor and manifest boundary

The package may compile or bind renderer candidates. It does not own descriptor or manifest meaning.

### Before source activation

A source binding should fail closed when required support is absent or contradictory, including:

- source/layer/style identity;
- source role and attribution;
- public-safe released artifact ref;
- tile/COG/PMTiles/GeoParquet/TileJSON integrity support;
- declared format and tiling scheme;
- bounds, zoom, CRS, and temporal scope;
- policy decision and obligations;
- rights and sensitivity posture;
- release state and rollback target;
- correction, withdrawal, or supersession state;
- endpoint/protocol admission.

### Before layer activation

A layer binding should additionally check:

- source binding exists and matches;
- style-layer ID is unique in the declared scope;
- source-layer reference is valid;
- required expressions/capabilities are supported;
- legend and Evidence Drawer projection refs are present where required;
- stale, denied, unreleased, or withdrawn state cannot appear as current;
- sensitive detail was transformed upstream.

### Style handling

Style JSON and expression fragments are renderer instructions, not policy.

The package must not:

- use a hidden filter to conceal unredacted sensitive features;
- convert denied state into zero opacity;
- remove attribution or provenance because a style omits it;
- allow arbitrary expression or image/plugin execution without admission;
- treat style equality or visual similarity as semantic equivalence.

[Back to top](#top)

---

<a id="map-context-and-event-boundary"></a>

## Map context and event boundary

Renderer events must be translated before they cross the adapter seam.

### Allowed outward event families

- camera settled;
- bounded view state changed;
- time context changed;
- layer visibility requested;
- click candidate selected;
- runtime capability changed;
- source/layer load state changed;
- finite negative state changed;
- runtime health degraded or recovered.

### Click handling

A click may return a bounded candidate containing:

- released layer ID;
- public-safe feature reference;
- screen point and generalized query geometry;
- time context;
- candidate evidence/claim-resolution reference;
- source role;
- release/correction state;
- safe display hints.

It must not return:

- raw private feature properties;
- raw sensitive geometry;
- source credentials;
- internal URLs or storage handles;
- unvalidated model output;
- a claim that the clicked feature is true;
- a raw MapLibre event object as a public contract.

### Map context

Camera, selection, bbox, time, and visible layers are interaction context. They may guide a governed API or Focus Mode request, but they are not evidence.

[Back to top](#top)

---

<a id="protocol-plugin-and-network-boundary"></a>

## Protocol, plugin, and network boundary

### Default posture

- Pure package modules: **no network**.
- Runtime adapter: **effects permitted only through explicit admitted operations**.
- Tests: **local and no-network by default**.
- Performance/integration jobs: network use must be declared, pinned, reviewable, and separable from default tests.
- Public runtime: endpoint, protocol, CSP, and plugin posture must be policy- and release-bound.

### Protocol registration

PMTiles, COG, custom protocols, workers, and plugin adapters must:

- be registered once through the adapter;
- use pinned reviewed dependencies;
- have explicit capability identifiers;
- reject unknown schemes;
- validate supplied artifact/manifest support;
- expose failure as finite negative state;
- clean up when the adapter is destroyed;
- avoid global registration races.

### Endpoint admission

The adapter must not accept arbitrary caller URLs merely because MapLibre supports them.

An admitted endpoint should be:

- derived from a governed released artifact or approved service reference;
- compatible with the declared audience and policy decision;
- free of embedded credentials;
- HTTPS or approved local-test transport;
- constrained by host/scheme/path rules;
- observable without logging secrets or sensitive query values;
- revocable and rollback-aware.

### Current performance exception

The existing smoke harness loads:

- `maplibre-gl@5.5.0` from `unpkg.com`;
- CSS from `unpkg.com`;
- glyphs from `demotiles.maplibre.org`.

That is confirmed performance-tool behavior, not the approved package runtime contract. It must not be copied into package source or public production configuration without dependency, rights, endpoint, CSP, integrity, availability, privacy, and rollback review.

[Back to top](#top)

---

<a id="negative-state-contract"></a>

## Negative-state contract

A renderer adapter should never turn unresolved trust state into a normal-looking map.

| State | Meaning | Required posture |
|---|---|---|
| `INVALID_INPUT` | Local shape or invariant failed. | Do not mutate runtime. |
| `SCHEMA_UNRESOLVED` | Required machine shape/version is absent or unsupported. | `ERROR` or review-required. |
| `POLICY_DENIED` | Supplied policy decision denies display. | `DENY`; preserve safe reason code. |
| `POLICY_RESTRICTED` | Display requires obligations or generalized form. | Apply only pre-approved derivative; otherwise deny/abstain. |
| `EVIDENCE_UNRESOLVED` | Required evidence support cannot resolve. | `ABSTAIN`; no authoritative popup. |
| `UNRELEASED` | Artifact/layer/style is not public-ready. | Block activation. |
| `UNSIGNED_OR_UNVERIFIED` | Required integrity/signature support is absent. | Block activation. |
| `STALE` | Candidate is outside accepted freshness posture. | Display only with explicit stale state if policy allows. |
| `WITHDRAWN` | Release was withdrawn. | Remove or disable; expose withdrawal state. |
| `CORRECTION_PENDING` | Supersession/correction is unresolved. | Do not present as current. |
| `ROLLBACK_MISMATCH` | Candidate does not match active rollback root/state. | Block mutation and require review. |
| `UNSUPPORTED_CAPABILITY` | Renderer/plugin cannot support declared behavior safely. | `ABSTAIN` or `ERROR`; no silent degradation. |
| `ENDPOINT_DENIED` | URL/protocol/host is not admitted. | Block network operation. |
| `RUNTIME_DEGRADED` | Renderer is unhealthy or partially unavailable. | Preserve safe degraded UI state. |
| `DISPOSED` | Operation targeted a destroyed adapter. | Deterministic error; no recreation side effect. |

Reason codes should be stable, documented, tested, and safe to expose. Internal exceptions and sensitive values must not cross the public boundary.

[Back to top](#top)

---

<a id="security-rights-sensitivity-and-privacy"></a>

## Security, rights, sensitivity, and privacy

### Sensitive geometry

The package may render only the public-safe derivative supplied by governed upstream processes.

It must not:

- receive precise restricted geometry and rely on style hiding;
- expose hidden source layers through devtools, queries, or click events;
- include redaction parameters that permit reconstruction;
- enable public joins that re-identify protected sites, people, parcels, infrastructure, archaeology, rare species, or cultural resources;
- log coordinates or feature properties beyond approved diagnostics.

### Credentials and secrets

Do not embed or export:

- API keys;
- bearer tokens;
- signed private URLs beyond their bounded runtime handling;
- source credentials;
- cloud storage secrets;
- internal hostnames;
- private layer IDs when restricted;
- authorization decisions as mutable client state.

Credentialed access belongs behind governed services. A browser adapter should receive only public-safe or audience-authorized delivery references.

### Diagnostics

Diagnostics should prefer:

- stable operation ID;
- adapter/package version;
- capability ID;
- safe layer/source identifier;
- release and manifest references;
- finite status and reason code;
- duration buckets;
- redacted endpoint class.

Diagnostics should avoid:

- exact protected coordinates;
- full feature properties;
- credentials or query strings;
- user identity unless separately governed;
- raw renderer exceptions containing URLs or payload fragments.

### Resource bounds

Accepted implementation should define limits for:

- source and layer counts;
- style size and expression depth;
- feature-query result count;
- click-candidate count;
- bounds and coordinate validity;
- cache budgets;
- worker count;
- protocol/plugin registrations;
- event-listener count;
- request timeouts and retries;
- screenshot/export dimensions where delegated;
- teardown time.

Limit breaches return explicit negative states rather than uncontrolled renderer behavior.

[Back to top](#top)

---

<a id="performance-tooling-boundary"></a>

## Performance tooling boundary

The repository contains a real MapLibre performance-governance lane. That lane is useful evidence about tooling, but it is not proof that this package implements the adapter.

### Confirmed performance surfaces

- `configs/maplibre/perf-envelope.v1.json`;
- `.github/workflows/maplibre-perf-governance.yml`;
- `scripts/maplibre-smoke-perf.mjs`;
- render-diff, attestation, release-manifest, proof-pack, correction/rollback, and failure-bundle scripts;
- MapLibre performance validators;
- `schemas/maplibre/perf-envelope.schema.json`;
- `artifacts/perf/` CI outputs.

### Boundaries

- Performance thresholds do not define package API semantics.
- A successful browser render does not prove manifest, policy, evidence, release, or privacy correctness.
- The permissive performance schema does not validate adapter contracts.
- Performance scripts should not become package runtime dependencies.
- CI artifact names do not promote outputs into canonical receipt/proof/release homes.
- Package changes need build, type, import-boundary, unit, adapter-contract, and browser tests in addition to performance jobs.
- The performance workflow's stale path filters must be corrected before it can be treated as coverage for the canonical app/package paths.

[Back to top](#top)

---

<a id="testing-fixtures-and-ci"></a>

## Testing, fixtures, and CI

### Required test families

| Test family | Purpose |
|---|---|
| Package metadata | Parse manifest, verify private/publish posture, engines, exports, scripts, and dependency pinning. |
| Type/build | Compile all public and internal TypeScript under supported targets. |
| Import boundary | Fail when non-adapter modules import `maplibre-gl` or style-spec runtime types. |
| Public API | Prove raw renderer handles/types are not exported. |
| Pure descriptor unit | Deterministic source/layer/style candidate results with no globals or network. |
| Manifest gating | Missing or mismatched refs block activation. |
| Policy finite states | Allow/restrict/deny/abstain/error inputs map to explicit renderer states. |
| Sensitive geometry | Unsafe precise input is denied; style hiding cannot satisfy policy. |
| Endpoint/protocol | Unknown schemes, hosts, plugins, and protocols fail closed. |
| Lifecycle | Create/destroy, listener cleanup, source/layer teardown, repeated calls, and disposed-state behavior. |
| Event translation | Raw events become bounded KFM candidates without sensitive leakage. |
| Rollback/correction | Withdrawn, superseded, stale, and rollback-mismatched layers cannot appear current. |
| Capability degradation | Unsupported behavior returns explicit state without silent fallback. |
| Local browser integration | Use local synthetic assets and fixture server; no public CDN required. |
| Visual regression | Baselines are review aids only and include bad-baseline canaries. |
| Performance | Threshold and render-diff jobs remain separate from semantic/admission tests. |
| Consumer contract | Explorer Web uses only the accepted adapter port. |
| Security/privacy | Logs, errors, URLs, click payloads, and telemetry remain public-safe. |

### Fixture posture

Use synthetic, public-safe fixtures. Keep valid, invalid, denied, unreleased, stale, withdrawn, sensitive, rollback-mismatch, unsupported, and endpoint-denied cases.

External services must not be required for default package tests.

### CI requirements

A package-aware workflow should watch at least:

```text
packages/maplibre/**
apps/explorer-web/**
docs/adr/ADR-0006*
docs/architecture/maplibre*
docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
contracts/**/*layer*
contracts/**/*style*
contracts/**/*map*
schemas/contracts/v1/maplibre/**
policy/**/*map*
policy/**/*layer*
tests/maplibre/**
tests/fixtures/maplibre/**
```

The current performance workflow does not satisfy this requirement because it does not watch the package and uses the legacy `apps/web/**` path.

### CI claims

A green docs, schema, performance, or generic validator workflow must not be described as proof that:

- the adapter API exists;
- the package builds;
- the single-importer rule is enforced;
- released-artifact checks run before source activation;
- sensitive geometry is safe;
- package consumers use the adapter;
- public runtime behavior is correct.

[Back to top](#top)

---

<a id="compatibility-and-migration"></a>

## Compatibility and migration

Changes are compatibility-significant when they affect:

- package name or entry point;
- public exports;
- renderer dependency/version;
- MapLibre style-spec version;
- adapter port methods or result types;
- finite states or reason codes;
- source/layer/style candidate shape;
- event candidate shape;
- protocol/plugin IDs;
- network endpoint admission;
- capability behavior;
- manifest, policy, evidence, release, correction, or rollback bindings;
- browser/runtime support;
- test-home or schema-home decisions.

A migration should include:

1. prior and new contract/API versions;
2. consumer inventory;
3. compile-time and runtime compatibility tests;
4. import-boundary validation;
5. fixture/golden-vector updates;
6. release and rollback impact;
7. network/CSP/dependency review;
8. deprecation window;
9. correction path for emitted or cached state;
10. rollback target and verification.

### No silent compatibility

Do not silently:

- rename layer/source IDs;
- retarget URLs;
- change tiling scheme or tile format;
- change event coordinate semantics;
- unwrap or reinterpret manifest refs;
- downgrade denied/restricted state;
- enable a plugin or protocol fallback;
- switch CDN/dependency source;
- change cache or retry semantics in a way that affects freshness or policy;
- convert renderer errors into normal empty maps.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Gate 0 — decide ownership

- Review ADR-0006.
- Decide `packages/maplibre/` versus `packages/maplibre-runtime/`.
- Define test-only runtime exceptions.
- Record the decision and migration path.

### Gate 1 — establish package mechanics

- Add accepted TypeScript/build tooling.
- Pin runtime and style-spec dependencies.
- Define engines/browser targets.
- Define private or publishable posture.
- Configure intentional exports.
- Add type/build/import-boundary CI.

### Gate 2 — define KFM-shaped port contracts

- Identify authoritative semantic contracts and schemas.
- Define immutable adapter inputs/results.
- Define finite states and reason codes.
- Prohibit raw renderer types from public exports.
- Add compile-time consumer fixtures.

### Gate 3 — implement pure core

- Source/layer/style candidate compilation.
- Local invariant checks.
- Capability and negative-state mapping.
- Safe diagnostics.
- Unit tests with no DOM/network.

### Gate 4 — implement minimal adapter lifecycle

- Create/destroy.
- Local synthetic style.
- One admitted source and layer.
- Event translation.
- Listener/resource cleanup.
- Fake/runtime contract tests.

### Gate 5 — add governed activation

- Manifest/integrity bindings.
- Policy and release inputs.
- Endpoint/protocol admission.
- Correction/rollback handling.
- Sensitive-geometry denial.

### Gate 6 — migrate consumers

- Inventory renderer imports and injections.
- Move Explorer Web to the adapter port.
- Decide treatment of smoke/performance harnesses.
- Enforce no-restricted-imports or equivalent.
- Remove temporary exceptions after migration.

### Gate 7 — make tests hermetic

- Replace public CDN dependence in default tests.
- Use pinned local runtime assets and synthetic fixtures.
- Keep optional external performance checks separately labeled.
- Prove negative and rollback cases.

### Gate 8 — reconcile schemas and CI

- Migrate or explicitly classify the legacy performance schema.
- Add package/app path filters.
- Run package, consumer, security, privacy, browser, and performance gates.
- Store trust artifacts only in governed homes.

Stop after any gate whose contract, policy, evidence, dependency, ownership, or rollback prerequisite is unresolved.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This source envelope is implementation-ready only when all applicable items are verified:

- [ ] Adapter ownership is accepted by ADR or documented decision.
- [ ] `packages/maplibre-runtime/` references are reconciled.
- [ ] Package metadata defines build, type, engines, exports, dependencies, and scripts.
- [ ] MapLibre and style-spec versions are pinned and reviewed.
- [ ] Public API is KFM-shaped and excludes raw renderer handles/types.
- [ ] Pure and effectful source modules are separated.
- [ ] Single-importer enforcement exists or the ADR is revised.
- [ ] Source/layer/style activation is manifest-, policy-, evidence-, and release-aware.
- [ ] Sensitive geometry is transformed upstream.
- [ ] Arbitrary endpoint/protocol/plugin loading is denied.
- [ ] Click and camera events translate into bounded KFM candidates.
- [ ] Negative states and stable reason codes are implemented.
- [ ] Correction, withdrawal, supersession, and rollback are visible.
- [ ] Resources and listeners clean up deterministically.
- [ ] Package unit and adapter-contract tests exist.
- [ ] Local browser tests are hermetic by default.
- [ ] Test-home and fixture-home decisions are documented.
- [ ] Explorer Web consumes the accepted port.
- [ ] Dedicated CI watches package and canonical app paths.
- [ ] Performance checks remain separate from semantic/admission proof.
- [ ] Schema authority is reconciled.
- [ ] Diagnostics and telemetry are privacy-safe.
- [ ] Dependency, endpoint, CSP, and supply-chain checks pass.
- [ ] Migration, deprecation, correction, and rollback paths are tested.
- [ ] Documentation reflects actual behavior.
- [ ] No claim of truth, policy, evidence, release, or publication authority is introduced.

[Back to top](#top)

---

<a id="verification-register"></a>

## Verification register

| ID | Verification item | Status |
|---|---|---:|
| ML-SRC-001 | Assign package and adapter owners. | NEEDS VERIFICATION |
| ML-SRC-002 | Accept, revise, or supersede ADR-0006. | NEEDS VERIFICATION |
| ML-SRC-003 | Decide `packages/maplibre/` versus `packages/maplibre-runtime/`. | CONFLICTED |
| ML-SRC-004 | Confirm package remains private or define publication policy. | NEEDS VERIFICATION |
| ML-SRC-005 | Add/confirm package build tooling. | UNKNOWN |
| ML-SRC-006 | Confirm TypeScript configuration and targets. | UNKNOWN |
| ML-SRC-007 | Pin MapLibre GL JS version. | NEEDS VERIFICATION |
| ML-SRC-008 | Pin style-spec/runtime companion dependencies. | NEEDS VERIFICATION |
| ML-SRC-009 | Define package engines/browser support. | NEEDS VERIFICATION |
| ML-SRC-010 | Define intentional public exports. | NEEDS VERIFICATION |
| ML-SRC-011 | Prohibit raw renderer types in public API. | NEEDS VERIFICATION |
| ML-SRC-012 | Inventory all runtime imports/injections. | NEEDS VERIFICATION |
| ML-SRC-013 | Decide test-only import/injection exceptions. | NEEDS VERIFICATION |
| ML-SRC-014 | Enforce single-importer rule or revised boundary. | UNKNOWN |
| ML-SRC-015 | Define MapRuntimePort semantic owner. | NEEDS VERIFICATION |
| ML-SRC-016 | Bind source/layer/style contract versions. | NEEDS VERIFICATION |
| ML-SRC-017 | Reconcile MapLibre schema authority. | CONFLICTED |
| ML-SRC-018 | Define finite adapter states and reason codes. | PROPOSED |
| ML-SRC-019 | Define source activation prerequisites. | PROPOSED |
| ML-SRC-020 | Define layer activation prerequisites. | PROPOSED |
| ML-SRC-021 | Define style admission rules. | PROPOSED |
| ML-SRC-022 | Define protocol/plugin allowlist. | NEEDS VERIFICATION |
| ML-SRC-023 | Define endpoint and CSP policy. | NEEDS VERIFICATION |
| ML-SRC-024 | Define manifest/integrity verification handoff. | NEEDS VERIFICATION |
| ML-SRC-025 | Define policy decision input contract. | NEEDS VERIFICATION |
| ML-SRC-026 | Define release/correction/rollback input contract. | NEEDS VERIFICATION |
| ML-SRC-027 | Define evidence/click-candidate handoff. | NEEDS VERIFICATION |
| ML-SRC-028 | Define camera/time context semantics. | NEEDS VERIFICATION |
| ML-SRC-029 | Prove sensitive geometry is upstream-transformed. | NEEDS VERIFICATION |
| ML-SRC-030 | Define safe diagnostics and telemetry. | NEEDS VERIFICATION |
| ML-SRC-031 | Define resource limits. | NEEDS VERIFICATION |
| ML-SRC-032 | Implement pure/effectful source separation. | PROPOSED |
| ML-SRC-033 | Replace placeholder entry point. | PROPOSED |
| ML-SRC-034 | Select canonical package test home. | CONFLICTED |
| ML-SRC-035 | Verify fixture payload inventory. | UNKNOWN |
| ML-SRC-036 | Add deterministic pure-core tests. | PROPOSED |
| ML-SRC-037 | Add adapter lifecycle/cleanup tests. | PROPOSED |
| ML-SRC-038 | Add manifest/policy/release negative tests. | PROPOSED |
| ML-SRC-039 | Add sensitive-geometry denial tests. | PROPOSED |
| ML-SRC-040 | Add endpoint/protocol/plugin denial tests. | PROPOSED |
| ML-SRC-041 | Add correction/withdrawal/rollback tests. | PROPOSED |
| ML-SRC-042 | Make default browser tests hermetic. | NEEDS VERIFICATION |
| ML-SRC-043 | Decide external CDN performance-test posture. | CONFLICTED |
| ML-SRC-044 | Correct workflow `apps/web/**` path drift. | NEEDS VERIFICATION |
| ML-SRC-045 | Add `packages/maplibre/**` workflow coverage. | NEEDS VERIFICATION |
| ML-SRC-046 | Add Explorer Web consumer contract tests. | PROPOSED |
| ML-SRC-047 | Reconcile `artifacts/perf/` trust-artifact naming/homes. | CONFLICTED |
| ML-SRC-048 | Confirm package build/test workflow pass rates. | UNKNOWN |
| ML-SRC-049 | Define dependency update and rollback policy. | NEEDS VERIFICATION |
| ML-SRC-050 | Define API deprecation window. | NEEDS VERIFICATION |
| ML-SRC-051 | Define consumer migration receipts/checks. | PROPOSED |
| ML-SRC-052 | Define adapter correction and runtime rollback procedure. | PROPOSED |
| ML-SRC-053 | Verify production runtime and operational health. | UNKNOWN |
| ML-SRC-054 | Update package/source/app docs after implementation. | PROPOSED |

[Back to top](#top)

---

<a id="rollback-correction-and-deprecation"></a>

## Rollback, correction, and deprecation

### Documentation rollback

If this README misstates the verified repository boundary:

1. revert the README commit;
2. restore the prior blob recorded in the metadata block;
3. preserve review discussion as audit evidence;
4. correct the evidence snapshot;
5. avoid changing runtime code merely to make documentation appear correct.

### Source rollback

A functional adapter change should define:

- previous package and API version;
- previous MapLibre/dependency lock state;
- previous consumer binding;
- previous protocol/plugin/endpoint admission state;
- previous manifest/schema/profile support;
- cache/service-worker invalidation needs;
- release/correction/rollback interactions;
- deterministic verification after revert.

### Runtime correction

When a renderer defect causes unsafe or misleading display:

- stop or disable the affected binding;
- preserve the affected release/layer/source/style identifiers;
- emit or route receipt-ready failure facts;
- link correction, withdrawal, or rollback state through the owning release process;
- do not rewrite evidence or source records to hide the renderer defect;
- ensure public surfaces show a safe negative state;
- verify stale caches and workers no longer serve the affected state.

### Deprecation

Deprecating an adapter method, state, capability, protocol, plugin, or event shape requires:

- consumer inventory;
- replacement and migration guidance;
- compatibility tests;
- sunset date or release condition;
- warning behavior that does not expose sensitive data;
- removal gate;
- rollback target.

### Authority reminder

Reverting the adapter or package does not by itself roll back a KFM data release. Software rollback and governed publication rollback are separate operations and must remain auditable.

[Back to top](#top)
