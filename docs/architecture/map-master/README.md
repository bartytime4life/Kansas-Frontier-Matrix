<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture-map-master-readme
title: Map Master Architecture
type: architecture-index
version: v2.0-draft
status: draft; repository-grounded; mixed-maturity; concrete-runtime-hold; non-authoritative; non-publication
owners:
  - "@bartytime4life — current CODEOWNERS review route"
  - "NEEDS VERIFICATION — independent map/runtime, evidence, policy, release, accessibility, security, and operations stewardship"
created: 2026-05-24
updated: 2026-08-20
policy_label: public; architecture; map-master; trust-membrane; evidence-bound; fail-closed; non-publication
owning_root: docs/
current_path: docs/architecture/map-master/README.md
responsibility: >-
  Serve as the compact, repository-grounded entry point for KFM's Map Master
  architecture lane; identify each direct child, reconcile current bounded
  implementation evidence, preserve the renderer-downstream trust membrane,
  and keep dependency admission, runtime behavior, release, deployment, and
  publication claims on explicit HOLD until their owning authorities and proof
  close.
truth_posture: >-
  CONFIRMED current tracked path, accepted Directory Rules placement, eight-file
  direct-child inventory, repository-grounded sibling set, renderer-neutral
  map-selection-to-Evidence-Drawer bridge, fixture-only layer-admission and
  release-scoped PMTiles-cache decisions, bounded 3D and performance profiles,
  structural MapLibre acquisition inventory, exact 6.6.0 readiness classifier,
  dependency-free MapLibre package scaffold, comment-only Explorer adapter, and
  absent committed browser-probe packet / PROPOSED ADR-0006 adapter boundary,
  ADR-0007 renderer-family decision, concrete MapLibre runtime, plugin and
  protocol admission, released-layer loader, production thresholds, operational
  correction, and rollback execution / UNKNOWN deployed renderer, public layer
  serving, production policy and EvidenceBundle resolution, telemetry, cache
  invalidation, and public parity / NEEDS VERIFICATION independent reviewers,
  complete hosted exact-head validation, accepted ownership, authenticated
  browser probes, release coupling, and operational recovery.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 1fbb35ccf3f4d9166c815ded78bfd851e3825ece
  target_prior_blob: e26f81e3452b812b70ef25b4b7f791be72e88154
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  adr_0006_blob: 3b789a623a07d27eb538ffaed10b0487ffc43d95
  adr_0007_blob: 6bfd66b1169728d7fad08f0bb2d7e2a56e3577b2
  maplibre_package_manifest_blob: b0582955feeb51016327113692fa5c98ecad8816
  maplibre_package_entry_blob: 91664eb00583f9e3d0405eb7954fefa9a48f4ee9
  explorer_manifest_blob: ddd201b74a06001d84a14bf54ac62a6cc3607a29
  explorer_adapter_blob: 663ba0f7a05498948f67d644387c73ab19d5c16c
  map_selection_bridge_blob: 18d61ea0ef2fbe2fc2f3cc9d42291c101003037f
  layer_admission_blob: 895100728c9eb676b9e2aef84680073142694b27
  pmtiles_cache_blob: 9e52c7c186ce72d56e2728c8c1a35737fe5f1540
  acquisition_inventory_blob: 2d5b9f0cf494ebb6f3cfc6e4f12acb497572edcf
  readiness_validator_blob: d9f189fd6f726ff6085371f7d69f2b035474e3fc
  two_d_three_d_parity_blob: 0c56d7a27a1d26d34779b4a40f576e06d79a6c6a
  evidence_drawer_blob: d9991838883d9eeb618a880025f658fb710c92a1
  layer_lifecycle_blob: 630557b79421e70033a9a2d906c3c472be714ecb
  performance_budgets_blob: c800cdd8d622ca2a4596cf80e9951f241fc70187
  renderer_boundary_blob: 628872aa58f9f86e31337924025a8590405385b5
  tile_artifacts_blob: f68bf295761711e1cec6046c2ea0f54564a0d4a4
  viewer_verification_blob: 3e1f7bfe7599bc658452468308d04b1eba24b2db
inspection_boundary: >-
  Current-session GitHub reads covered the complete prior target in bounded
  chunks; the direct-child inventory; accepted ADR-0029 and the adopted
  Directory Rules bytes; proposed ADR-0006 and ADR-0007; the current root,
  Explorer, and MapLibre package manifests; the placeholder package and adapter;
  renderer-neutral map selection; fixture-only layer admission and PMTiles cache
  decisions; the acquisition and 6.6.0 readiness validators; the absent committed
  probe-results path; recent sibling modernization pull requests; and open pull
  request overlap. No mounted checkout, dependency installation, repository-native
  test run, live source, authenticated browser probe, deployed runtime, public
  endpoint, release application, correction propagation, or operational rollback
  was exercised.
related:
  - ../map-shell.md
  - ../maplibre-master.md
  - ../planetary-3d.md
  - ../ui/MAP_RUNTIME_BOUNDARY.md
  - ../../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "../../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../../../packages/maplibre/README.md
  - ../../../packages/maplibre/package.json
  - ../../../packages/maplibre/src/index.ts
  - ../../../apps/explorer-web/package.json
  - ../../../apps/explorer-web/src/adapters/MapLibreAdapter.ts
  - ../../../apps/explorer-web/src/features/map_runtime/index.tsx
  - ../../../apps/explorer-web/src/features/map_runtime/layer_manifest_admission.ts
  - ../../../apps/explorer-web/src/features/map_runtime/pmtiles_release_cache.ts
  - ../../../tools/validators/maplibre/assess_acquisition_inventory.py
  - ../../../tools/validators/maplibre/validate_v6_readiness.py
tags: [kfm, architecture, map-master, maplibre, renderer, evidence-drawer, layer-lifecycle, tile-artifacts, viewer-verification, performance, 2d-3d-parity, trust-membrane, runtime-hold]
notes:
  - "v2.0-draft is a same-path repository-grounded refresh; placement outcome PLACE."
  - "All seven direct-child architecture pages are now repository-grounded mixed-maturity references; none establishes an admitted MapLibre runtime or public map release."
  - "ADR-0006 and ADR-0007 remain proposed; their embedded August 13 readiness snapshots predate the current 6.6.0, twelve-probe classifier and are lineage for exact current readiness facts."
  - "The parent records child boundaries and current evidence but does not duplicate their normative contracts, schemas, policy, validators, receipts, or release objects."
  - "This document changes no dependency, lockfile, adapter, runtime, source, registry, lifecycle state, release, deployment, publication, or repository setting."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Map Master Architecture

> **Operating rule.** The renderer is downstream of trust. KFM may use a browser map to present released, public-safe carriers and to collect bounded interaction context, but the renderer does not create evidence, source authority, policy, review, release, publication, or AI authority.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-d4a72c?style=flat-square)](#status-and-authority)
[![Directory: confirmed](https://img.shields.io/badge/directory-confirmed-2da44e?style=flat-square)](#directory-rules-basis)
[![Sibling set: reconciled](https://img.shields.io/badge/sibling%20set-reconciled-0969da?style=flat-square)](#5-direct-child-map)
[![Concrete MapLibre: held](https://img.shields.io/badge/concrete%20MapLibre-HOLD-b42318?style=flat-square)](#2-current-repository-evidence)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#4-boundary-contract)

> [!IMPORTANT]
> **This page is an architecture index, not a renderer, manifest, policy, evidence, or release authority.** It records where the deeper Map Master boundaries live and what current repository evidence supports. The owning contract, schema, policy, validator, receipt, proof, release, runtime, correction, and rollback families remain separate.

> [!CAUTION]
> **The lane has meaningful bounded implementation but no concrete MapLibre runtime.** Explorer Web contains renderer-neutral map-selection, Evidence Drawer, layer-admission, and release-scoped PMTiles-cache profiles. The repository also contains fixture-first 3D and performance profiles plus structural acquisition/readiness validators. None of those surfaces installs MapLibre, creates a source, mutates a registry or cache, contacts a live governed service, applies a release transition, or publishes a map.

> [!WARNING]
> **ADR-0006 and ADR-0007 remain proposed.** The current `@kfm/maplibre` `0.0.0` package is dependency-free, its export is a placeholder, `MapLibreAdapter.ts` is comment-only, `maplibre-gl` is absent from the inspected manifests, and `configs/maplibre/v6-probe-results.json` is absent. The exact `6.6.0` readiness lane therefore cannot be represented as `READY` from current evidence.

**Quick navigation:** [Status](#status-and-authority) · [Directory Rules](#directory-rules-basis) · [Purpose](#1-purpose-and-authority) · [Current evidence](#2-current-repository-evidence) · [Trust boundary](#3-renderer-boundary-and-seven-negative-authorities) · [Boundary contract](#4-boundary-contract) · [Children](#5-direct-child-map) · [Current implementation](#6-current-implementation-surfaces) · [Click-to-truth](#7-click-to-truth-and-governed-interaction) · [Artifacts and parity](#8-artifacts-lifecycle-performance-and-parity) · [Validation](#9-validation-and-finite-outcomes) · [Gates](#10-decision-and-graduation-gates) · [Change rules](#11-change-review-and-maintenance-rules) · [Open work](#12-open-verification-register) · [Rollback](#13-rollback-and-correction) · [Related](#14-related-repository-evidence) · [Ledger](#15-no-loss-change-ledger)

---

<a id="status-and-authority"></a>

## Status and authority

| Field | Current bounded result |
|---|---|
| **Tracked path** | `docs/architecture/map-master/README.md` |
| **Document identity** | `kfm://doc/architecture-map-master-readme` |
| **Owning root** | `docs/` — human-readable architecture orientation and cross-root boundary explanation |
| **Placement** | **CONFIRMED / PLACE** under accepted ADR-0029 and Directory Rules v2 |
| **Repository evidence base** | `main@1fbb35ccf3f4d9166c815ded78bfd851e3825ece` |
| **Prior target blob** | `e26f81e3452b812b70ef25b4b7f791be72e88154` |
| **Direct-child inventory** | **CONFIRMED** — this README plus seven sibling Markdown files |
| **Sibling-document posture** | **CONFIRMED / repository-grounded / mixed maturity** |
| **Review route** | `@bartytime4life` through current CODEOWNERS |
| **Independent specialist review** | **NEEDS VERIFICATION** |
| **ADR-0006 adapter/acquisition decision** | **PROPOSED** |
| **ADR-0007 renderer-family decision** | **PROPOSED** |
| **Renderer-neutral Explorer slices** | **CONFIRMED / bounded / fixture or injected-transport only** |
| **Concrete MapLibre dependency and adapter** | **HOLD / absent or placeholder** |
| **Authenticated browser probe packet** | **NOT PRESENT** at the inspected path |
| **Deployed public behavior** | **UNKNOWN / not established here** |
| **Release, deployment, publication effect** | None |

### Truth labels

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Verified from current repository bytes, accepted decisions, tests, workflows, artifacts, or current-session inspection |
| **PROPOSED** | A decision, dependency, seam, behavior, field family, threshold, or future state not accepted and verified as current behavior |
| **UNKNOWN** | Available repository or operational evidence does not establish the claim |
| **NEEDS VERIFICATION** | A concrete review, run, artifact, or platform check remains before relying on the claim |

Finite workflow or runtime terms such as `PASS`, `READY`, `HOLD`, `DENY`, `ABSTAIN`, `FAIL`, `ERROR`, and `PUBLISHED` do not replace the four evidence labels.

[Back to top](#top)

---

<a id="directory-rules-basis"></a>

## Directory Rules basis

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact bytes of [Directory Rules v2](../../doctrine/directory-rules.md) and makes that doctrine path the single writable human placement authority. This target already exists under `docs/architecture/map-master/` and explains a cross-root architecture boundary to humans. The same-path update therefore receives **PLACE**.

The update does not create or move a root, child lane, semantic contract, machine schema, policy family, source registry, evidence store, receipt family, proof family, release record, runtime package, published carrier, or compatibility mirror.

### Responsibility split

| Responsibility | Owning surface | This README may do |
|---|---|---|
| Human architecture orientation | `docs/architecture/` | Reconcile and link current evidence |
| Renderer-family or adapter decision | Accepted ADR | Report current status and open gates |
| Reusable renderer implementation | `packages/` after reviewed ownership and admission | Link and report maturity |
| Explorer composition | `apps/explorer-web/` | Explain browser-facing boundaries |
| Semantic object meaning | `contracts/` | Reference accepted semantics |
| Machine validation shape | `schemas/` | Reference validated profiles |
| Admissibility and restrictions | `policy/` plus accountable decisions | State obligations; never decide them here |
| Fixtures, validators, tests, workflows | Their responsibility roots | Report bounded evidence and non-effects |
| Evidence, receipts, proofs, catalogs | Their distinct data/accountability families | Require closure without collapsing object families |
| Release, correction, withdrawal, rollback | `release/` and governed operators | Explain state effects; never apply them |
| Released public-safe carriers | `data/published/` | Treat as downstream carriers, not canonical truth |
| Deployed runtime and operations | app/package/runtime/config/log evidence | Report only what was exercised |

[Back to top](#top)

---

<a id="1-scope"></a>
<a id="1-purpose-and-authority"></a>

## 1. Purpose and authority

This README is the compact landing page for KFM's Map Master architecture lane. It answers five questions:

1. What trust boundary every browser renderer must obey.
2. Which direct child owns each detailed map concern.
3. Which bounded implementation surfaces are present now.
4. Which renderer, dependency, release, correction, and operational claims remain held.
5. Which evidence would be required before the lane can graduate.

### 1.1 What this lane owns

- renderer-downstream architecture and negative-authority boundaries;
- click-to-truth and Evidence Drawer architecture;
- explanatory relationships among layer, style, tile, release, and representation objects;
- viewer-side fail-closed admission concepts;
- map artifact, performance, and 2D/3D trust-parity guidance;
- current maturity, validation entry points, review triggers, and rollback notes.

### 1.2 What this lane does not own

- canonical records or EvidenceBundle contents;
- source admission, rights, sensitivity, or policy decisions;
- semantic contracts or machine schemas;
- release, promotion, correction, withdrawal, or rollback decisions;
- dependency installation, package ownership, or renderer selection without accepted ADRs;
- runtime secrets, infrastructure configuration, deployed services, or public publication;
- generated receipts, proofs, catalog records, or published carriers merely because they concern maps.

### 1.3 Authority order for claims on this page

1. KFM trust, lifecycle, public-boundary, correction, and rollback invariants.
2. Accepted ADRs, especially ADR-0029 within its placement scope.
3. Adopted Directory Rules and current machine projections.
4. Current repository implementation, tests, validators, workflows, and emitted artifacts.
5. Proposed ADR-0006 and ADR-0007 for intended future decisions only.
6. Sibling architecture pages as repository-grounded explanatory references.
7. Supplied manuals and older plans as design lineage, not current implementation proof.

[Back to top](#top)

---

<a id="2-repo-fit--open-dr-12-family"></a>
<a id="2-current-repository-evidence"></a>

## 2. Current repository evidence

The prior v1.0 landing page correctly recorded a scaffold and readiness HOLD, but it predated the repository-grounded rewrite of every sibling page and the current `6.6.0`, twelve-probe readiness profile. This edition reconciles those changes without upgrading bounded fixtures into runtime or publication proof.

### 2.1 Direct evidence snapshot

| Surface | Current repository evidence | Safe conclusion |
|---|---|---|
| Directory authority | ADR-0029 is accepted and adopts Directory Rules v2 | The existing `docs/architecture/map-master/` lane has confirmed explanatory placement |
| Renderer ADRs | ADR-0006 and ADR-0007 remain effectively proposed | No adapter seam or renderer-family decision is binding yet |
| Root workspace | Node/pnpm workspace scripts exist; no `maplibre-gl` dependency is declared | Workspace presence does not admit a renderer |
| Explorer Web | Vite, TypeScript, Vitest, and Playwright scripts are present; no `maplibre-gl` dependency is declared | A build/test shell exists, not a MapLibre runtime |
| `@kfm/maplibre` package | Private `0.0.0` manifest with no dependencies | Package home is a scaffold candidate only |
| Package entry | `export const placeholder = true` | No functional KFM renderer adapter is exported |
| Explorer adapter | One comment naming the intended import boundary | No concrete adapter behavior exists |
| Map selection | Strict renderer-neutral `MapFeatureSelection` parser and injected resolver bridge | Bounded click-scope and no-leak behavior exist without renderer or transport ownership |
| Evidence Drawer | Strict public-safe projection parser, finite view model, keyboard-operable fixture surface | Bounded UI behavior exists; live evidence/policy/release composition remains held |
| Layer admission | Fixture-only evaluator with `PASS / HOLD / DENY / ERROR`; all authority and effect flags remain false | `PASS` means later registration eligibility only |
| PMTiles cache | Fixture-only release-scoped decision; no fetch and no CacheStorage call | Cache planning exists; mutation and network behavior do not |
| 3D/parity | Inactive candidate decisions, Reality Boundary guidance, representation receipts, and zero-effect fixtures | Trust-parity logic exists; no renderer, scene, or public 3D runtime exists |
| Performance | Synthetic mobile, resource-envelope, service-SLO, and telemetry profiles | Fixture measurements and arithmetic exist; production budgets and telemetry do not |
| Acquisition inventory | Bounded no-network scan for manifests, imports, globals, CDN URLs, workers, and protocols | Structural inventory exists; it creates no dependency or renderer authority |
| Readiness classifier | Exact `6.6.0` profile with twelve required probes and finite `READY / HOLD / ERROR` outcomes | `READY` is human-review eligibility only; current inspected inputs cannot satisfy it |
| Probe record | `configs/maplibre/v6-probe-results.json` is absent | All required browser/runtime probes are unrecorded in the committed profile |
| Direct-child docs | All seven siblings have repository-grounded mixed-maturity rewrites | The parent can treat them as current lane references, not stale proposal-only pages |

### 2.2 Current maturity model

| Capability | Status | What is actually proven |
|---|---|---|
| Architecture lane and child routing | **CONFIRMED** | Current paths, responsibilities, and boundaries are documented |
| Renderer-neutral click bridge | **CONFIRMED / bounded** | Strict input validation, injected resolver, evidence-subset enforcement, finite local failures |
| Evidence Drawer fixture behavior | **CONFIRMED / bounded** | Public-safe projection parsing and keyboard-operable local behavior |
| Layer admission decision | **CONFIRMED / fixture-only** | Deterministic eligibility classification with explicit zero effects |
| Release-scoped PMTiles cache decision | **CONFIRMED / fixture-only** | Deterministic cache action classification with no fetch or mutation |
| 3D admission and representation support | **CONFIRMED / inactive fixture-first** | Candidate classification and truth-parity obligations; no renderer execution |
| Performance and SLO support | **CONFIRMED / synthetic** | Declared fixture measurements and arithmetic, not production observations |
| Complete renderer acquisition enforcement | **NEEDS VERIFICATION** | Inventory tool exists; representative full-tree execution and policy coupling remain separate evidence |
| Exact MapLibre dependency selection | **HOLD** | No exact dependency is declared in inspected manifests |
| Functional KFM adapter | **UNKNOWN / not implemented in inspected files** | Package export and app adapter remain placeholders |
| Browser and device behavior | **UNKNOWN** | No committed twelve-probe packet was found |
| Released layer loader and `addSource` path | **UNKNOWN / not established** | Fixture eligibility does not execute registration |
| Production evidence, policy, review, correction, release, rollback | **UNKNOWN / held** | No end-to-end operational proof is claimed |
| Deployment and publication | **UNKNOWN / none established here** | Documentation and fixtures do not create public state |

### 2.3 Current contradictions and stale embedded snapshots

ADR-0006 and ADR-0007 remain the correct decision records for the proposed adapter and renderer-family choices. Their embedded August 13 repository snapshots, however, describe an earlier six-probe readiness profile and earlier version context. The current executable validator at the evidence snapshot targets exact `6.6.0` and requires twelve probes. This README therefore uses the ADRs for **decision status** and the current validator for **current readiness behavior**.

That difference is documentation drift, not authority to accept either ADR or silently rewrite its decision.

[Back to top](#top)

---

<a id="3-the-canonical-posture--renderer-is-downstream-of-trust"></a>
<a id="4-the-seven-negative-authorities"></a>
<a id="3-renderer-boundary-and-seven-negative-authorities"></a>

## 3. Renderer boundary and seven negative authorities

A KFM browser renderer may consume released public-safe carrier descriptions, maintain view and interaction state, display trust-visible UI, and emit bounded selection context. It must remain downstream of seven authorities.

| Authority the renderer does **not** own | Canonical responsibility | Fail-closed consequence |
|---|---|---|
| Canonical truth store | Governed records and evidence families | A rendered pixel or feature property is never evidence by itself |
| Source registry | Source admission and descriptor authorities | The browser cannot activate or reclassify a source |
| Policy engine | Policy rules and accountable decisions | Missing or denied policy never falls back to allow |
| Citation authority | EvidenceRef-to-EvidenceBundle and citation validation | Unsupported claims abstain or fail safely |
| Review authority | Authenticated accountable review records | UI interaction and fixture `PASS` cannot approve a candidate |
| Publication authority | Promotion and release objects | Rendering, a green check, or a PR does not publish |
| AI authority | Governed AI over resolved released evidence | Generated language cannot replace evidence or policy |

### 3.1 Direction of trust

```text
source admission
  -> evidence resolution
  -> policy / sensitivity / review
  -> validation / proof / release
  -> governed API or released public-safe carrier
  -> renderer-neutral KFM runtime boundary
  -> concrete renderer adapter, only after admission
  -> map, Evidence Drawer, Focus Mode, export, or story projection
```

Trust does not flow backward from the browser. A visible layer does not legalize its source, validate its evidence, approve its policy, release itself, or authorize a model answer.

### 3.2 Public clients

Normal public clients use governed APIs and released public-safe artifacts. They do not read RAW, WORK, QUARANTINE, candidate registries, unrestricted canonical stores, model runtimes, or sensitive decision reasons as their ordinary path.

[Back to top](#top)

---

<a id="13-anti-patterns"></a>
<a id="11-what-lives-here--what-does-not-live-here"></a>
<a id="4-boundary-contract"></a>

## 4. Boundary contract

### 4.1 Permitted responsibilities

A future admitted map runtime may:

- accept a released layer or scene projection through KFM-owned interfaces;
- create renderer sources and layers only after governed admission succeeds;
- preserve release, correction, sensitivity, and evidence context in visible UI;
- translate renderer click events into the strict renderer-neutral selection profile;
- maintain camera, viewport, selection, hover, timeline, and accessibility state;
- expose deterministic diagnostics and bounded performance observations;
- propose safe map actions to governed AI without granting execution authority.

### 4.2 Prohibited responsibilities

The browser runtime must not:

- read internal stores or unreviewed source endpoints as its normal path;
- infer evidence from feature properties, style metadata, tile bytes, or visual appearance;
- evaluate rights, sensitivity, review, or release as an unreviewed local substitute;
- treat `PASS`, cache hit, successful decode, or successful draw as publication authority;
- expose restricted geometry or reasons merely because the browser received them;
- let plugins, protocols, workers, CDN scripts, or custom layers bypass the one reviewed acquisition seam;
- let AI call a renderer, source, or model outside governed interfaces;
- conceal stale, denied, withdrawn, superseded, corrected, or error states.

### 4.3 Required failure posture

| Condition | Required public-safe posture |
|---|---|
| Missing evidence | `ABSTAIN` or equivalent no-claim state |
| Policy denial or harmful precision | `DENY`, with public-safe wording |
| Stale or unresolved release support | `HOLD` or visible stale state |
| Withdrawn release | Deny load or remove through governed correction behavior |
| Resolver, validator, or runtime failure | `ERROR`, without unsafe fallback |
| Unsupported renderer capability | Visible fallback, reduced feature set, or alternate 2D representation |
| Performance pressure | Degrade presentation without dropping trust, accessibility, or correction context |

### 4.4 Anti-patterns

- Importing or acquiring a renderer outside the reviewed seam.
- Loading a layer because a URL exists.
- Treating `data/published/` as the canonical truth store.
- Treating a manifest as a release decision or a receipt as proof.
- Treating renderer-neutral fixture `PASS` as browser registration.
- Treating a cache decision as CacheStorage mutation.
- Treating a 3D candidate as a released scene.
- Treating synthetic timings as production service-level objectives.
- Treating documentation, badges, screenshots, tests, or PR state as publication.
- Copying contract, schema, policy, or release authority into this README.

[Back to top](#top)

---

<a id="12-directory-tree-proposed"></a>
<a id="5-direct-child-map"></a>

## 5. Direct-child map

The current tracked lane contains exactly eight files:

```text
docs/architecture/map-master/
├── README.md
├── 2D_3D_PARITY.md
├── EVIDENCE_DRAWER.md
├── LAYER_LIFECYCLE.md
├── PERFORMANCE_BUDGETS.md
├── RENDERER_BOUNDARY.md
├── TILE_ARTIFACTS.md
└── VIEWER_VERIFICATION.md
```

The tree is a current direct-child inventory, not a proposed future implementation tree.

### 5.1 Child responsibility and maturity

| Document | Owns | Current bounded posture |
|---|---|---|
| [`README.md`](README.md) | Lane entry point, child routing, aggregate maturity, gates, and open work | This repository-grounded v2.0 draft |
| [`RENDERER_BOUNDARY.md`](RENDERER_BOUNDARY.md) | Seven negative authorities and renderer-downstream enforcement | Repository-grounded; renderer-neutral and fixture evidence present; concrete MapLibre held |
| [`EVIDENCE_DRAWER.md`](EVIDENCE_DRAWER.md) | Map selection to inspectable public-safe evidence projection | Strict local parsing, injected resolver, evidence-subset checks, finite outcomes, keyboard drawer; live governed composition held |
| [`LAYER_LIFECYCLE.md`](LAYER_LIFECYCLE.md) | Candidate manifests, admission, map release, correction, withdrawal, and rollback relationships | Mixed maturity; LayerManifest and MapReleaseManifest fixture families exist; no transition application or source registration |
| [`TILE_ARTIFACTS.md`](TILE_ARTIFACTS.md) | Tile, raster, array, sidecar, integrity, transport, and release distinctions | Mixed repository profiles; structural and metadata checks exist; trusted public carrier delivery held |
| [`VIEWER_VERIFICATION.md`](VIEWER_VERIFICATION.md) | Verify-before-registration boundary and zero-effect admission outcomes | Fixture-only evaluator with finite outcomes and explicit `registryMutated: false` / `maplibreSourceCreated: false` |
| [`PERFORMANCE_BUDGETS.md`](PERFORMANCE_BUDGETS.md) | Measurement evidence levels, degradation, synthetic budgets/SLOs, and telemetry boundary | Synthetic and fixture-backed profiles exist; production thresholds and operational telemetry held |
| [`2D_3D_PARITY.md`](2D_3D_PARITY.md) | Trust parity among 2D, 2.5D, globe, and true-3D candidates | Repository-grounded renderer-neutral parity; inactive 3D candidate families exist; no renderer or released scene |

### 5.2 Sibling authority rule

Each child is authoritative only for its human-readable architecture responsibility. It may point to contracts, schemas, policy, validators, fixtures, tests, workflows, receipts, proofs, and release objects, but it does not replace them.

The siblings carry their own pinned evidence snapshots. This parent records their current blobs and roles; it does not rewrite their historical evidence bases or imply that one child proves another's runtime behavior.

[Back to top](#top)

---

<a id="6-the-click-to-truth-flow"></a>
<a id="7-map-object-families"></a>
<a id="6-current-implementation-surfaces"></a>

## 6. Current implementation surfaces

### 6.1 Package and adapter boundary

| Path | Current evidence | Authority limit |
|---|---|---|
| [`packages/maplibre/package.json`](../../../packages/maplibre/package.json) | Private `@kfm/maplibre` `0.0.0`; no dependencies | Scaffold identity only |
| [`packages/maplibre/src/index.ts`](../../../packages/maplibre/src/index.ts) | Exports `placeholder = true` | No renderer API or adapter |
| [`apps/explorer-web/package.json`](../../../apps/explorer-web/package.json) | Vite/TypeScript/Vitest/Playwright shell; no `maplibre-gl` | Browser toolchain, not renderer admission |
| [`MapLibreAdapter.ts`](../../../apps/explorer-web/src/adapters/MapLibreAdapter.ts) | Comment naming the intended import boundary | No functioning adapter |

### 6.2 Renderer-neutral map selection

[`apps/explorer-web/src/features/map_runtime/index.tsx`](../../../apps/explorer-web/src/features/map_runtime/index.tsx) currently provides:

- exact-field parsing for `kfm.explorer.map-feature-selection.v1`;
- bounded identifiers and a maximum of sixteen unique evidence references;
- local abstention when the selection has no evidence references;
- an injected resolver whose caller owns transport;
- strict Evidence Drawer parsing;
- denial of returned evidence outside the clicked selection's declared reference set;
- finite invalid-selection, missing-evidence, scope-mismatch, resolver-error, and drawer outcomes;
- a deterministic button-based browser fixture that proves keyboard/focus behavior before a renderer dependency is admitted.

It performs no source, policy, evidence-store, lifecycle, renderer, model, or owned network access.

### 6.3 Fixture-only layer admission

[`layer_manifest_admission.ts`](../../../apps/explorer-web/src/features/map_runtime/layer_manifest_admission.ts) evaluates one closed synthetic projection. Every result carries:

```text
authority: "NONE"
registryMutated: false
maplibreSourceCreated: false
holds: ["RUNTIME_REGISTRATION_NOT_EXECUTED"]
```

A `PASS / LAYER_MANIFEST_REGISTER_ELIGIBLE` result means only that a later governed loader could consider registration. It does not mutate a registry, create a source, approve a release, authorize public use, or prove browser behavior.

### 6.4 Fixture-only release-scoped PMTiles cache decision

[`pmtiles_release_cache.ts`](../../../apps/explorer-web/src/features/map_runtime/pmtiles_release_cache.ts) classifies a future cache hit, online fetch requirement, offline miss, partial entry, mismatch, withdrawal, denied source class, authority overclaim, or invalid input. It performs no fetch and does not call CacheStorage.

Even `PASS` retains:

```text
authority: "NONE"
cacheMutated: false
networkRequested: false
```

### 6.5 Structural acquisition and exact readiness

| Validator | Scope | Finite outcomes | Non-effect |
|---|---|---|---|
| [`assess_acquisition_inventory.py`](../../../tools/validators/maplibre/assess_acquisition_inventory.py) | Bounded manifests and source roots for renderer packages, imports, CDN URLs, globals, protocols, and workers | `PASS / HOLD / FAIL / ERROR` | Does not admit a dependency or select a renderer |
| [`validate_v6_readiness.py`](../../../tools/validators/maplibre/validate_v6_readiness.py) | Exact `6.6.0` dependency, ESM/ES2022, boundary hygiene, internal API scan, and twelve named probes | `READY / HOLD / ERROR` | `READY` is eligibility evidence for human review only |

The current inspected manifests have no exact MapLibre dependency and the committed probe-results file is absent. Those facts are sufficient to preserve a readiness HOLD without claiming that the complete repository scan was freshly executed in this documentation task.

[Back to top](#top)

---

<a id="7-click-to-truth-and-governed-interaction"></a>

## 7. Click-to-truth and governed interaction

### 7.1 Current bounded flow

```text
synthetic or future renderer selection
  -> strict MapFeatureSelection parse
  -> local missing-evidence abstention, or injected resolver call
  -> strict EvidenceDrawerPayload parse
  -> returned-evidence subset check
  -> finite Evidence Drawer view model
  -> keyboard-operable drawer fixture
```

This is **CONFIRMED** as renderer-neutral, injected-transport browser behavior. It is not a live MapLibre flow and does not prove an EvidenceRef-to-EvidenceBundle service, policy execution, authenticated review, release application, correction propagation, or public deployment.

### 7.2 Proposed production flow

A future admitted production path should be able to prove:

```text
released layer / carrier
  -> admitted KFM renderer adapter
  -> bounded feature selection
  -> governed API request
  -> authenticated EvidenceRef -> EvidenceBundle resolution
  -> policy / sensitivity / review / release checks
  -> citation-valid public-safe projection
  -> Evidence Drawer
  -> optional bounded Focus Mode answer or abstention
```

Every arrow requires an owning contract, implementation, negative case, and reviewable receipt or runtime evidence appropriate to consequence.

### 7.3 Required visible states

The eventual map shell must keep at least these classes visible where applicable:

- evidence missing or unresolved;
- policy denied or precision generalized;
- review pending or not applicable;
- release unreleased, stale, superseded, withdrawn, or corrected;
- citation failure;
- runtime or resolver error;
- offline cache miss or partial bundle;
- unsupported renderer capability;
- representation or 2D/3D parity limitation.

The exact production contract names and visual implementation remain **NEEDS VERIFICATION** beyond the bounded profiles documented by the child pages.

[Back to top](#top)

---

<a id="8-2d-default--3d-conditional--tile-artifact-discipline"></a>
<a id="10-reality-boundary-note--synthetic-vs-observed"></a>
<a id="8-artifacts-lifecycle-performance-and-parity"></a>

## 8. Artifacts, lifecycle, performance, and parity

### 8.1 Carrier and authority separation

| Family | Role | Must not be mistaken for |
|---|---|---|
| Layer/style manifest | Describes a candidate or released presentation | Evidence, policy, or release decision |
| PMTiles/MVT/COG/Zarr/MBTiles/MLT carrier | Delivers encoded spatial content | Canonical truth or rights clearance |
| Integrity sidecar or geo manifest | Binds metadata and digests within its profile | Promotion or public-use authority |
| RunReceipt / generated receipt | Records process execution or authorship | Proof, review, or release |
| ProofPack | Assembles declared proof evidence | Policy or promotion decision |
| MapReleaseManifest | Binds released map artifacts within its accepted profile | A substitute for underlying release authority |
| Viewer admission result | Classifies eligibility for a later step | Registry mutation or `addSource` execution |
| Cache result | Classifies a future cache action | Network or CacheStorage mutation |
| RepresentationReceipt | Records representation process memory | Observation or reality truth |
| Reality Boundary Note | Discloses observed, modeled, inferred, reconstructed, or synthetic status | Evidence resolution by itself |

### 8.2 Lifecycle posture

Map-related carriers still follow KFM's governed lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

Promotion is a governed state transition. A file move, successful validator, browser load, cache hit, screenshot, commit, or pull request is not promotion.

### 8.3 Performance evidence levels

The performance child distinguishes declared fixture data, synthetic execution, representative browser/device measurements, operational telemetry, and release-gating evidence. KFM must not convert one level into another by prose.

Current bounded profiles support synthetic mobile PMTiles verification, declared rendering-resource assessment, service-SLO arithmetic, and telemetry architecture fixtures. Production thresholds, workload/device classes, authenticated telemetry, operational dashboards, and automatic release effects remain held.

### 8.4 2D / 3D trust parity

2D remains the calm baseline. A 2.5D, globe, or true-3D candidate may differ visually, but it must not weaken:

- evidence and citation visibility;
- rights, sensitivity, and public-safe geometry;
- review and release state;
- correction, withdrawal, and rollback behavior;
- accessibility and reduced-motion alternatives;
- representation truthfulness and Reality Boundary disclosure;
- deterministic identity and finite outcomes.

Current 3D admission fixtures may return `ALLOW_RENDER_CANDIDATE`, `ABSTAIN`, `DENY`, or `ERROR`, but all effect flags remain false. Candidate allowance is not render, review, release, deployment, public use, or publication permission.

[Back to top](#top)

---

<a id="9-viewer-side-verification-fails-closed--ui-negative-states"></a>
<a id="9-validation-and-finite-outcomes"></a>

## 9. Validation and finite outcomes

### 9.1 Evidence classes

| Evidence class | What it can establish | What it cannot establish |
|---|---|---|
| Markdown structure and links | Documentation integrity | Runtime behavior or publication |
| Contract/schema fixtures | Shape and declared semantic conformance | Source truth or operational policy |
| Deterministic validators | Bounded classification for inspected inputs | Uninspected environment behavior |
| Browser fixture tests | Local DOM, focus, finite-state, and no-leak behavior | Live renderer, network, evidence, or release closure |
| Structural acquisition scan | Located declared acquisition mechanisms in bounded roots | Supply-chain approval or complete dynamic behavior |
| Readiness probe record | Named behavior for an exact dependency/build when genuinely run | Admission, release, deployment, or publication |
| Representative integration test | One governed end-to-end slice | Universal production behavior |
| Runtime logs and telemetry | Observed deployed behavior within scope | Canonical truth or rights authority |
| Release/correction/rollback rehearsal | Governed transition behavior for a release candidate | Automatic public authority outside its record |

### 9.2 Repository-owned focused entry points

```bash
python tools/validators/maplibre/assess_acquisition_inventory.py --repo-root . --summary
python tools/validators/maplibre/validate_v6_readiness.py --scan-root .
python tools/validators/maplibre/validate_v6_readiness.py --fixtures
python -m unittest tests.maplibre.test_validate_v6_readiness
pnpm --dir apps/explorer-web test:unit
pnpm --dir apps/explorer-web test:browser
```

These commands are current repository entry points or package scripts. They are documented here; they were **not** represented as freshly executed by this connector-only documentation update.

### 9.3 Finite outcomes remain profile-specific

| Profile | Outcomes | Critical interpretation |
|---|---|---|
| Acquisition inventory | `PASS / HOLD / FAIL / ERROR` | `PASS` means no detected acquisition in the bounded scan, not renderer approval |
| Exact readiness | `READY / HOLD / ERROR` | `READY` means eligibility for human review only |
| Layer admission | `PASS / HOLD / DENY / ERROR` | `PASS` means later registration eligibility with zero effects |
| PMTiles cache | `PASS / HOLD / DENY / ERROR` | `PASS` may allow a future action; no action is performed |
| Evidence Drawer | `ANSWER / ABSTAIN / DENY / ERROR` plus local bridge codes | Outcome is a public-safe view state, not release authority |
| 3D admission | Candidate allow, abstain, deny, or error | Candidate allow has no render/public effect |
| Documentation QA | Pass/fail for declared checks | Green docs checks prove docs only |

Do not silently normalize these vocabularies into one global state machine. Cross-profile mappings require an accepted contract or ADR when they affect authority.

[Back to top](#top)

---

<a id="10-decision-and-graduation-gates"></a>

## 10. Decision and graduation gates

A concrete MapLibre browser path remains held until equivalent evidence closes all applicable gates.

| Gate | Required closure evidence | Current state |
|---|---|---|
| Effective decisions | Reviewed status transition and index parity for ADR-0006/0007 or accepted successors | **OPEN** |
| Physical ownership | One accepted package/adapter home and no parallel acquisition seam | **OPEN** |
| Exact dependency | Exact version in manifest and lockfile with compatibility, license, security, update, and rollback review | **OPEN** |
| Complete acquisition inventory | Representative recursive scan of manifests, imports, dynamic acquisition, workers, protocols, globals, and examples | **PARTIAL** — validator exists |
| Functional adapter | KFM-owned interface with no raw renderer leakage and focused consumer tests | **OPEN** |
| Twelve-probe packet | Authenticated results tied to exact dependency, build, browser matrix, and revision | **OPEN** |
| Released-layer loader | Evidence/policy/review/release-bound loader with negative cases and no internal-store bypass | **OPEN** |
| Evidence Drawer integration | Real renderer selection through governed transport and authenticated EvidenceBundle closure | **PARTIAL** — renderer-neutral fixture exists |
| Artifact verification | Trusted carrier bytes, integrity, source class, host headers, failure, correction, and withdrawal behavior | **PARTIAL / HELD** |
| Performance and accessibility | Representative device/browser/network budgets, visible degradation, reduced motion, keyboard, and alternate representation | **PARTIAL / HELD** |
| 2D/3D parity | Integrated candidate proving evidence, policy, release, correction, sensitivity, and reality-boundary parity | **PARTIAL / HELD** |
| Correction and rollback | Rehearsed release invalidation, cache purge/rebuild, UI update, and rollback with auditable records | **OPEN** |
| Operations | Telemetry, alerting, incident ownership, recovery, and runbooks for deployed behavior | **OPEN** |
| Independent review | Named accountable reviewers with separation appropriate to consequence | **OPEN** |

No documentation rewrite, package scaffold, fixture `PASS`, green workflow, screenshot, or performance number substitutes for these gates.

[Back to top](#top)

---

<a id="11-change-review-and-maintenance-rules"></a>

## 11. Change, review, and maintenance rules

### 11.1 Ordinary same-path documentation changes

A bounded edit may:

- correct stale repository evidence;
- update child routing and maturity;
- repair links, anchors, navigation, metadata, or examples;
- clarify non-effects, validation limits, and rollback;
- reconcile accepted doctrine without changing authority.

It must not accept an ADR, admit a dependency, invent runtime behavior, duplicate normative object families, or represent a fixture as release/publication proof.

### 11.2 ADR-class changes

Open or amend an ADR when work would:

- accept, replace, or create an exception to the renderer-family decision;
- select or move the one renderer package/adapter authority;
- create a peer renderer or a second acquisition seam;
- create or relocate a normative contract, schema, policy, registry, release, or proof family;
- change public trust boundaries, lifecycle phases, promotion semantics, sensitivity posture, correction, or rollback authority.

### 11.3 Propagation review

When map runtime behavior changes materially, inspect at least:

- this README and the owning sibling page;
- ADR-0006, ADR-0007, and any accepted successor;
- `packages/maplibre/` metadata and implementation;
- Explorer adapter/runtime docs and tests;
- acquisition and readiness validators, fixtures, and workflows;
- layer, tile, evidence, performance, parity, release, correction, and rollback references actually affected;
- generated receipts and current bindings required by repository controls.

### 11.4 Maintenance triggers

Refresh this page when any of the following changes:

- a direct child is added, moved, renamed, retired, or materially reclassified;
- ADR-0006 or ADR-0007 changes effective status;
- the selected MapLibre version, probe set, package home, or adapter seam changes;
- a real released-layer loader or MapLibre source-registration path appears;
- production Evidence Drawer, performance, telemetry, correction, or rollback proof lands;
- a public deployment or publication decision is recorded;
- current claims conflict with repository evidence.

[Back to top](#top)

---

<a id="14-open-questions-and-adr-triggers"></a>
<a id="12-open-verification-register"></a>

## 12. Open verification register

| Item | Status | Closure evidence |
|---|---|---|
| Effective adapter/acquisition decision | **PROPOSED** | Accepted ADR-0006 or successor plus synchronized index |
| Effective renderer-family decision | **PROPOSED** | Accepted ADR-0007 or successor plus synchronized index |
| One physical package/adapter authority | **NEEDS VERIFICATION** | Reviewed ownership decision, one active home, migration and rollback |
| Exact MapLibre dependency and update policy | **UNKNOWN** | Manifest and lockfile pin, dependency/security/license review, rollback |
| Complete acquisition inventory | **NEEDS VERIFICATION** | Representative full-tree execution and reviewed findings |
| Functional KFM renderer adapter | **UNKNOWN** | Implementation, interface contract, focused tests, and consumer proof |
| Committed twelve-probe packet | **NOT PRESENT** | Authenticated probe record tied to exact revision and environment |
| Plugin/protocol/custom-layer allowlist | **UNKNOWN** | Admission contract, version pins, supply-chain and failure evidence |
| Released-layer loader and source registration | **UNKNOWN** | Governed integration with negative, correction, and withdrawal tests |
| Production Evidence Drawer composition | **PARTIAL / HOLD** | Real renderer selection, governed transport, authenticated evidence/policy/review/release closure |
| Trusted public-safe artifact hosting | **UNKNOWN** | Rights, host headers, byte verification, integrity, release, correction, and rollback proof |
| Production performance budgets | **UNKNOWN** | Accepted workloads, devices, browsers, networks, thresholds, and measured evidence |
| Operational telemetry and incident path | **UNKNOWN** | Emission, ingestion, retention, dashboard, alerting, ownership, and recovery proof |
| Integrated 2D/3D candidate | **HOLD** | Scene/note/admission/receipt/UI dependency closure with no-leak and fallback proof |
| Correction, cache invalidation, withdrawal, rollback | **UNKNOWN** | Rehearsal and auditable transition records |
| Independent specialist stewardship | **NEEDS VERIFICATION** | Named accountable reviewers and separation-of-duties route |
| ADR embedded readiness snapshot drift | **NEEDS VERIFICATION** | Same-path ADR refresh without changing proposed decisions |
| Hosted exact-head validation for this revision | **PENDING / NEEDS VERIFICATION** | Completed workflow conclusions for the final PR head |

Until these close, the safe posture is a repository-grounded architecture lane with bounded fixture evidence and an explicit concrete-runtime HOLD.

[Back to top](#top)

---

<a id="13-rollback-and-correction"></a>

## 13. Rollback and correction

This revision changes documentation and its required authoring provenance only.

- **Before merge:** close the draft pull request and abandon the feature branch.
- **After an authorized merge:** revert the documentation and receipt commits or apply a transparent forward correction through normal review.
- **Prior README blob:** `e26f81e3452b812b70ef25b4b7f791be72e88154`.
- **Caution:** restoring the prior blob also restores the stale six-probe readiness description and the now-invalid classification of `2D_3D_PARITY.md` and the other siblings as unreconciled draft lineage.
- **Runtime effect:** none. No dependency, lockfile, adapter, plugin, source, registry, cache, lifecycle record, release, deployment, or public endpoint changes.
- **Correction preference:** use a forward correction when only evidence or wording changes; preserve historical receipts as immutable lineage.

[Back to top](#top)

---

<a id="5-relationship-to-other-architecture-lanes"></a>
<a id="15-related-docs"></a>
<a id="14-related-repository-evidence"></a>

## 14. Related repository evidence

### 14.1 Decisions and doctrine

| Reference | Role | Current status |
|---|---|---|
| [Directory Rules v2](../../doctrine/directory-rules.md) | Canonical human placement authority | Adopted exact bytes through ADR-0029 |
| [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Directory Rules adoption record | **Accepted** |
| [ADR-0006](../../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) | Proposed one-adapter/acquisition seam | **Proposed** |
| [ADR-0007](<../../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>) | Proposed renderer-family decision | **Proposed** |
| [`map-shell.md`](../map-shell.md) | Governed map shell and trust-visible interaction architecture | Repository-present reference |
| [`maplibre-master.md`](../maplibre-master.md) | Broader MapLibre design and verification lineage | Repository-present; current claims require evidence-by-section |
| [`planetary-3d.md`](../planetary-3d.md) | Planetary/3D carrier and admission boundary | Repository-grounded mixed-maturity reference |
| [`MAP_RUNTIME_BOUNDARY.md`](../ui/MAP_RUNTIME_BOUNDARY.md) | UI/runtime boundary | Repository-present reference |

### 14.2 Implementation and validation

| Reference | Current bounded role |
|---|---|
| [`packages/maplibre/README.md`](../../../packages/maplibre/README.md) | Package boundary and scaffold documentation |
| [`packages/maplibre/package.json`](../../../packages/maplibre/package.json) | Private `0.0.0` package identity; no dependency |
| [`packages/maplibre/src/index.ts`](../../../packages/maplibre/src/index.ts) | Placeholder export |
| [`apps/explorer-web/package.json`](../../../apps/explorer-web/package.json) | Explorer toolchain and scripts; no `maplibre-gl` |
| [`MapLibreAdapter.ts`](../../../apps/explorer-web/src/adapters/MapLibreAdapter.ts) | Comment-only intended import seam |
| [`map_runtime/index.tsx`](../../../apps/explorer-web/src/features/map_runtime/index.tsx) | Renderer-neutral selection-to-Evidence-Drawer bridge |
| [`layer_manifest_admission.ts`](../../../apps/explorer-web/src/features/map_runtime/layer_manifest_admission.ts) | Fixture-only zero-effect admission decision |
| [`pmtiles_release_cache.ts`](../../../apps/explorer-web/src/features/map_runtime/pmtiles_release_cache.ts) | Fixture-only zero-effect cache decision |
| [`assess_acquisition_inventory.py`](../../../tools/validators/maplibre/assess_acquisition_inventory.py) | Bounded structural acquisition inventory |
| [`validate_v6_readiness.py`](../../../tools/validators/maplibre/validate_v6_readiness.py) | Exact `6.6.0`, twelve-probe readiness classifier |
| [MapLibre acquisition workflow](../../../.github/workflows/maplibre-acquisition-inventory.yml) | Read-only hosted orchestration for the inventory profile |
| [MapLibre performance workflow](../../../.github/workflows/maplibre-perf-governance.yml) | Bounded performance-governance orchestration; green may still mean explicit HOLD |

[Back to top](#top)

---

<a id="16-appendix--glossary-and-reference"></a>
<a id="15-no-loss-change-ledger"></a>

## 15. No-loss change ledger

| Prior material | v2.0 disposition |
|---|---|
| Renderer downstream of trust | **Retained as the primary operating law** |
| Seven negative authorities | **Retained** |
| Click-to-truth concept | **Retained and split into current bounded flow versus proposed production flow** |
| Evidence Drawer, layer lifecycle, tile artifacts, viewer verification, performance, and parity children | **Retained and updated to current repository-grounded maturity** |
| 2D calm baseline and conditional 3D | **Retained with current renderer-neutral trust-parity evidence** |
| Reality Boundary discipline | **Retained; implementation authority remains with owning families** |
| Fail-closed finite outcomes and negative states | **Retained with profile-specific vocabulary** |
| Directory Rules `PLACE` basis | **Retained and grounded in accepted ADR-0029** |
| Eight-file direct-child tree | **Retained and reverified** |
| `@kfm/maplibre` scaffold, placeholder export, comment-only adapter | **Retained as current evidence** |
| Old exact-readiness description | **Corrected from the prior six-probe snapshot to current `6.4.0`, twelve-probe behavior** |
| `2D_3D_PARITY.md` marked stale/conflicted | **Corrected; the child is now repository-grounded mixed-maturity guidance** |
| Remaining siblings described generically as retained drafts | **Corrected with current bounded implementation summaries** |
| Proposed click-to-truth represented as current runtime | **Denied; current bridge remains renderer-neutral and injected-transport only** |
| Production performance and telemetry assumptions | **Narrowed to synthetic profiles and explicit HOLDs** |
| Renderer/plugin/version claims from older external-source snapshots | **Removed from the landing page; current primary-source verification belongs in decision/admission work** |
| Rollback to v0.1 blob | **Replaced with the exact current prior README blob** |

### Changelog

| Version | Date | Change |
|---|---|---|
| **v2.0-draft** | 2026-08-20 | Reconciled all seven repository-grounded siblings, current renderer-neutral and fixture-only implementation, exact `6.4.0` twelve-probe readiness, decision/status drift, graduation gates, validation limits, and rollback |
| **v1.0** | 2026-08-14 | First repository-grounded same-path rewrite against current scaffold/HOLD evidence and accepted Directory Rules |
| **v0.2** | 2026-05-24 | Document-only renderer-oriented revision with proposed path and runtime assumptions |
| **v0.1** | 2026-05-24 | Initial draft |

[Back to top](#top)
