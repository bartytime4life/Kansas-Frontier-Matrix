<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/ui/readme
title: UI Subsystem — Architecture README
type: architecture-landing-page
version: v4.0-draft
status: draft; repository-grounded; mixed-maturity; documentation-only; non-publisher
owners:
  - "@bartytime4life — verified CODEOWNERS review route"
  - "NEEDS VERIFICATION — independent UI, map-runtime, governed-API, evidence, policy, accessibility, security, review, release, correction, rollback, and operations stewardship"
created: 2026-05-08
updated: 2026-08-19
policy_label: public; architecture; ui; trust-membrane; no-release; no-publication
owning_root: docs/
responsibility: "Provide the repository-grounded landing page for KFM UI architecture, current bounded implementation, trust boundaries, sibling-document maturity, validation expectations, graduation gates, and rollback without becoming decision, contract, schema, policy, evidence, runtime, review, release, deployment, or publication authority."
truth_posture: "CONFIRMED repository evidence / PROPOSED architecture and integration / UNKNOWN deployment and public operation; cite-or-abstain"
current_path: docs/architecture/ui/README.md
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d639f9ff40288d12244cd7bc84af538652f6dfb1
  target_prior_blob: 36d975710d906a6c4146c550d40929b1822b667e
  ui_directory_tree_ref: d639f9ff40288d12244cd7bc84af538652f6dfb1
  explorer_readme_blob: f8f37ed6e396a19ca080ea29b41920afdf03a94b
  explorer_package_blob: ddd201b74a06001d84a14bf54ac62a6cc3607a29
  explorer_main_blob: 86c16e43e03601e65eb01b0b4949f7850089e877
  explorer_site_readme_blob: 3f2821cf221bb3b44e8e1236fe409edb34174787
  explorer_site_catalog_blob: 31824767e618e43308916534a57de76b9b1c212e
  explorer_site_catalog_test_blob: b00f4796f7d1a34ef36758c9df995f703350e740
  governed_shell_doc_blob: b0a203cbb5059d750c34a89c5f26ab02cedb6092
  layering_doc_blob: 2fc04fc39ac3cb74525644e186805730c5e287fe
  review_console_doc_blob: 9b036c731f26714785d0b63f588d0ddd9d300e4b
  story_player_doc_blob: 526d4e0500b686f18a05426059471d5f6cc65b69
  telemetry_doc_blob: 4d8038d933a5398313a362589ec1d7bc6a4c9586
  trust_badges_doc_blob: 18489f6d51da787dbaf6c292469997b2ca88e4e2
  map_context_admission_doc_blob: 4b85851b6f1d3e0f8bc4e305a6015b39ebd59235
  governed_api_main_blob: 4eb335c7c0b27f62c7419c478542e8fe40e1ff38
  governed_api_registry_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
  governed_api_stub_blob: 371e60d9f96c78e31c8a1e6109d19dee5da4213b
  ui_build_workflow_blob: 52382d796a8dd5ecafc39a801515aff0a8b013f8
  adr_index_ref: d639f9ff40288d12244cd7bc84af538652f6dfb1
  directory_rules_decision: ADR-0029 accepted
related:
  - docs/architecture/README.md
  - docs/architecture/map-shell.md
  - docs/architecture/ui/ACCESSIBILITY.md
  - docs/architecture/ui/BOUNDARIES.md
  - docs/architecture/ui/COMPARE_AND_EXPORT.md
  - docs/architecture/ui/CONTINUITY_NOTES.md
  - docs/architecture/ui/EVIDENCE_DRAWER.md
  - docs/architecture/ui/FOCUS_FLOW.md
  - docs/architecture/ui/GOVERNED_SHELL.md
  - docs/architecture/ui/LAYERING.md
  - docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - docs/architecture/ui/REVIEW_CONSOLE.md
  - docs/architecture/ui/STORY_PLAYER.md
  - docs/architecture/ui/TELEMETRY.md
  - docs/architecture/ui/TRUST_BADGES.md
  - docs/architecture/ui/map-context-evidence-drawer-admission.md
  - docs/architecture/governed-ai/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - docs/adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md
  - docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - docs/adr/ADR-0016-telemetry-redaction-posture.md
  - docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - apps/explorer-web/README.md
  - apps/explorer-web/src/main.ts
  - apps/explorer-web/src/site/README.md
  - apps/explorer-web/src/site/mountExplorerSite.ts
  - apps/explorer-web/src/site/catalog.ts
  - apps/explorer-web/tests/explorer-site-catalog.test.ts
  - apps/explorer-web/src/features/story_player/CURRENT_IMPLEMENTATION.md
  - apps/governed-api/src/governed_api/main.py
  - apps/governed-api/src/governed_api/routes/registry.py
  - apps/governed-api/src/governed_api/stub.py
  - packages/ui/README.md
  - packages/maplibre/README.md
  - policy/ui/README.md
  - tests/policy/test_explorer_web_adapter_boundary.py
  - .github/workflows/ui-build.yml
tags: [kfm, ui, architecture, explorer-web, governed-api, maplibre, evidence-drawer, focus-mode, story-player, review-console, accessibility, finite-outcomes, trust-membrane, correction, rollback]
notes:
  - "v4.0-draft reconciles the landing page with the repository-grounded Explorer composition introduced after the v3 evidence snapshot while preserving the document ID, path, H1, twenty-three numbered sections, and Appendix A anchor."
  - "The current Explorer entrypoint mounts a bounded map-first landing composition with a synthetic renderer-neutral map stage, deterministic selection-to-Evidence-Drawer laboratory, thirteen knowledge domains, thirty-eight feature catalog entries, and eight trust principles."
  - "The baseline shell still resolves to fixed fail-closed states, all claim-bearing demonstrations use local deterministic fixtures, and no live Governed API transport, released-layer loader, model call, MapLibre runtime, deployment, release, or publication is established."
  - "Sibling-document maturity is mixed: several pages are current repository-grounded references, while EVIDENCE_DRAWER.md, FOCUS_FLOW.md, and MAP_RUNTIME_BOUNDARY.md retain proposal-era metadata and require separate same-path reconciliation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI Subsystem — Architecture README

> **Repository-grounded landing page.** KFM's UI is a downstream, map-first, time-aware, evidence-bounded client surface. It may orient users, render finite governed projections, exercise deterministic synthetic interactions, and display already released public-safe carriers. It does not create truth, resolve evidence authority, decide policy, approve review or release, activate sources, call model runtimes directly, or publish by displaying something.

> [!IMPORTANT]
> **Current Explorer composition is real but bounded.** At `main@d639f9ff40288d12244cd7bc84af538652f6dfb1`, [`src/main.ts`](../../../apps/explorer-web/src/main.ts) mounts the repository-grounded [`mountExplorerSite`](../../../apps/explorer-web/src/site/mountExplorerSite.ts) composition. That composition includes a skip link, section navigation, trust posture, synthetic renderer-neutral map stage, deterministic map-selection-to-Evidence-Drawer laboratory, thirteen knowledge-domain entries, thirty-eight descriptive feature entries, and eight trust principles. It still uses local deterministic fixtures, preserves the baseline `ABSTAIN / NO_GOVERNED_RESPONSE` posture, imports no MapLibre runtime, and establishes no live Governed API claim path, released-layer loader, model call, deployment, release, or public operation.

| Field | Current evidence-backed value |
|---|---|
| **Document status** | `draft` / repository-grounded architecture landing page |
| **Placement authority** | [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts [`Directory Rules v2`](../../doctrine/directory-rules.md) |
| **UI decision authority** | The shell, governed-API, MapLibre-boundary, sole-renderer, finite-envelope, abstention, telemetry, and public-client ADRs remain `proposed` in the current [`ADR index`](../../adr/INDEX.md) |
| **Repository review route** | `@bartytime4life` through CODEOWNERS; routing is not independent approval or separation of duties |
| **Current composed UI** | Bounded Explorer landing composition plus deterministic synthetic map/evidence interaction and repository catalog |
| **Current isolated executable slices** | Fail-closed baseline shell, Evidence Drawer, map-evidence bridge, Story Player projection consumer, trust/header projections, and other fixture-first feature modules |
| **Governed API** | Three GET scaffold routes—`/bootstrap`, `/layers`, and `/evidence`—return `ABSTAIN / NOT_IMPLEMENTED`; unsupported operations fail safely |
| **Map runtime** | `HOLD`: Explorer has no `maplibre-gl` dependency; `packages/maplibre/` and `MapLibreAdapter.ts` remain placeholders |
| **Operational telemetry** | `HOLD`: bounded telemetry profiles exist, but no general UI event, emitter, governed route, sink, retention regime, or emitted telemetry receipt is established |
| **Release/publication effect** | None |

---

## Quick jump

- [1 · Scope](#1--scope)
- [2 · Authority level](#2--authority-level)
- [3 · Status](#3--status)
- [4 · Repo fit](#4--repo-fit)
- [5 · What belongs here](#5--what-belongs-here)
- [6 · What does **not** belong here](#6--what-does-not-belong-here)
- [7 · Subsystem map](#7--subsystem-map)
- [8 · Proposed directory tree](#8--proposed-directory-tree)
- [9 · Sibling documents](#9--sibling-documents)
- [10 · UI component families](#10--ui-component-families)
- [11 · Routes](#11--routes)
- [12 · Finite outcomes](#12--finite-outcomes)
- [13 · Trust membrane](#13--trust-membrane)
- [14 · Layer trust badges](#14--layer-trust-badges)
- [15 · Accessibility expectations](#15--accessibility-expectations)
- [16 · Validation](#16--validation)
- [17 · Inputs](#17--inputs)
- [18 · Outputs](#18--outputs)
- [19 · Review burden](#19--review-burden)
- [20 · Related folders](#20--related-folders)
- [21 · ADRs that govern this folder](#21--adrs-that-govern-this-folder)
- [22 · FAQ](#22--faq)
- [23 · Open questions and verification backlog](#23--open-questions-and-verification-backlog)
- [Appendix A · No-loss modernization ledger](#appendix-a--no-loss-modernization-ledger)

---

## 1 · Scope

This README is the entry point for the UI architecture lane under `docs/architecture/`. It explains:

- the UI subsystem's authority boundary;
- the current composed Explorer site and its narrower fail-closed baseline resolver;
- the difference between composed UI, independently tested fixture slices, documentation-only surfaces, placeholders, and held runtime capabilities;
- how the public shell, governed API, renderer seam, Evidence Drawer, Focus Mode, Story Player, Review Console, compare/export, telemetry, trust-badge, and accessibility surfaces relate;
- which sibling documents reflect current repository evidence and which retain proposal-era assumptions;
- which contracts, schemas, policies, tests, workflows, ADRs, receipts, and runbooks own the executable or governance questions;
- what must close before KFM can claim an integrated map product, live claim path, deployment, release, or public operation.

The UI remains downstream of the canonical lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET
    -> governed release
    -> governed API or released public-safe carrier
    -> Explorer Web / Evidence Drawer / Focus Mode / story / compare / export
```

The browser may help users inspect, navigate, compare, scope requests, and understand finite state. It must not turn a rendered feature, synthetic diagram, tile property, route fragment, visual emphasis, generated summary, telemetry event, screenshot, or model response into authoritative evidence.

[Back to top](#top)

---

## 2 · Authority level

This file is an **architecture landing page**, not an accepted decision record. Authority is resolved by the question being asked.

| Question | Controlling evidence |
|---|---|
| Where does this file belong? | Accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), adopted [`directory-rules.md`](../../doctrine/directory-rules.md), and the existing same-path `docs/architecture/ui/` lane |
| What files exist now? | Pinned repository tree, file blobs, package manifests, code, tests, workflows, and generated artifacts |
| What does current code do? | Exact code plus focused tests and hosted runs at the tested revision; prose is secondary when it conflicts |
| What should the UI eventually do? | Proposed UI architecture, reviewed contracts/schemas/policy, and accepted ADRs |
| May a claim or detail be shown? | Resolved evidence, policy, review, release, sensitivity, rights, purpose, audience, and correction state appropriate to consequence |
| Is something published? | A governed release decision and released artifact state, not this README, a fixture, test, workflow, commit, pull request, merge, build, or deployment |

The current [`ADR index`](../../adr/INDEX.md) records thirty-six numbered ADRs. [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) is the only accepted numbered ADR; the other thirty-five remain effectively proposed. This README may describe or prepare proposed decisions but cannot accept them by repetition.

[Back to top](#top)

---

## 3 · Status

### Confirmed current repository evidence

| Surface | Verified state | Authority limit |
|---|---|---|
| `docs/architecture/ui/` | This README plus fourteen sibling architecture documents are present | Presence does not prove freshness, acceptance, implementation, or consistency |
| [`apps/explorer-web/package.json`](../../../apps/explorer-web/package.json) | Real Vite, TypeScript, Vitest, and Playwright scripts under Node 22; no runtime renderer dependency is declared | Build tooling is not a map runtime, deployment, release, or publication |
| [`apps/explorer-web/src/main.ts`](../../../apps/explorer-web/src/main.ts) | Imports the site CSS bundle and mounts `mountExplorerSite(root)` | Composition is local and deterministic; it is not a live route or network claim path |
| [`apps/explorer-web/src/site/`](../../../apps/explorer-web/src/site/) | Map-first landing composition with skip link, section navigation, trust posture, synthetic map stage, deterministic evidence lab, domain matrix, feature catalog, and trust principles | Repository orientation and fixture proof only; no live data, source activation, policy execution, or public release |
| Repository catalog | Thirty-eight descriptive feature entries, thirteen knowledge domains, eight trust principles, and explicit maturity labels | Catalog labels describe bounded repository state; they are not release, review, policy, or publication states |
| Baseline shell resolver | No-input resolution returns `ABSTAIN / NO_GOVERNED_RESPONSE`; supplied input returns `ERROR / UNSUPPORTED_BASELINE_INPUT`; both carry zero evidence refs | Safe absence path only; not a live response pipeline |
| Map-evidence laboratory | Renderer-neutral synthetic selections exercise supported, missing, restricted, mismatched, and resolver-error cases through the local Evidence Drawer bridge | No MapLibre import, external fetch, EvidenceBundle resolver, policy engine, or released feature is involved |
| Evidence Drawer implementation | Strict app-local public-safe projection parsing, finite view-state resolution, fixed no-leak negative copy, evidence/citation/history display, and keyboard/focus behavior exist | Fixture-first projection; it does not prove authoritative evidence resolution or live transport |
| Story Player implementation | Pure 2D-only consumer of one already-governed public-safe StoryManifest projection with focused tests | No fetch, live route, StoryNode dereference, evidence resolution, map playback, release, or publication |
| Governed API scaffold | `/bootstrap`, `/layers`, and `/evidence` are registered as GET routes; each current route returns `ABSTAIN / NOT_IMPLEMENTED`; unsupported paths or methods return safe errors | Negative scaffold, not an evidence-backed ANSWER path |
| Review Console | Architecture/feature documentation, private placeholder package, and separate synthetic ReviewRecord validation proof are present | No operational queue, actor registry, decision recorder, audit ledger, API, deployment, release approval, or public path |
| Telemetry | Four bounded fixture-first profiles and focused validators/tests exist | No general UI event envelope, operational emitter, governed route, sink, retention, or receipt instances |
| [`packages/ui/`](../../../packages/ui/) | Private placeholder entrypoint | No stable shared component API is established |
| [`packages/maplibre/`](../../../packages/maplibre/) | Private placeholder package; Explorer has no `maplibre-gl` dependency | No functioning renderer seam or admitted runtime |
| UI build workflow | Read-only workflow checks locked readiness, build, unit tests, and browser tests | CI signal only; required-check coupling and current exact-head results must be evaluated separately |
| UI review routing | `@bartytime4life` is the verified CODEOWNERS route | Review routing is not independent approval, release authority, or separation of duties |

### Mixed documentation maturity

The architecture lane is not uniformly current:

- [`GOVERNED_SHELL.md`](./GOVERNED_SHELL.md), [`LAYERING.md`](./LAYERING.md), [`REVIEW_CONSOLE.md`](./REVIEW_CONSOLE.md), [`STORY_PLAYER.md`](./STORY_PLAYER.md), [`TELEMETRY.md`](./TELEMETRY.md), [`TRUST_BADGES.md`](./TRUST_BADGES.md), and [`map-context-evidence-drawer-admission.md`](./map-context-evidence-drawer-admission.md) contain recent repository-grounded boundaries.
- [`BOUNDARIES.md`](./BOUNDARIES.md), [`ACCESSIBILITY.md`](./ACCESSIBILITY.md), [`COMPARE_AND_EXPORT.md`](./COMPARE_AND_EXPORT.md), and [`CONTINUITY_NOTES.md`](./CONTINUITY_NOTES.md) are repository-grounded but predate the current site composition and must not be used for current entrypoint claims without checking code.
- [`EVIDENCE_DRAWER.md`](./EVIDENCE_DRAWER.md), [`FOCUS_FLOW.md`](./FOCUS_FLOW.md), and [`MAP_RUNTIME_BOUNDARY.md`](./MAP_RUNTIME_BOUNDARY.md) retain proposal-era metadata, placeholder ownership, stale path assumptions, or unmounted-repository disclaimers. Their doctrine may remain useful, but current behavior must come from code, current contracts/tests, and newer repository-grounded references until those pages are reconciled.

### Proposed architecture

The following remain architectural targets or held integrations unless a current file, test, run, or accepted decision proves otherwise:

- an accepted canonical Explorer-shell decision;
- a functioning renderer-neutral `MapRuntimePort` and admitted MapLibre adapter seam;
- live Explorer-to-Governed-API transport over an accepted runtime response contract;
- authoritative EvidenceRef-to-EvidenceBundle resolution in the claim path;
- operative UI/render/access/rights/sensitivity policy evaluation;
- active released-layer lookup, artifact integrity, correction/withdrawal propagation, and cache invalidation;
- integrated Focus, Story, Compare, Export, Review, Diagnostics, and Telemetry routes;
- complete accessibility, security, performance, observability, recovery, and deployment behavior.

### Unknown or not established

Production deployment topology, authentication, authorization, CSP, CORS, network isolation, cache behavior, service health, browser matrix, production telemetry, live source or artifact exposure, public traffic, operational release state, and public availability remain **UNKNOWN** unless separately proved by current deployment and runtime evidence.

[Back to top](#top)

---

## 4 · Repo fit

The existing path is placement-safe under the accepted Directory Rules:

- `docs/` owns human-facing explanation and architecture;
- `docs/architecture/` owns cross-system architecture descriptions;
- `docs/architecture/ui/` is the existing UI architecture lane;
- app behavior stays under `apps/`, reusable code under `packages/`, semantic meaning under `contracts/`, machine shape under `schemas/`, admissibility under `policy/`, executable proof under `tests/` and `fixtures/`, and release/correction/rollback authority under their owning roots;
- domain and product concerns remain lanes inside responsibility roots rather than new root folders.

| Responsibility | Current or expected home | UI relationship |
|---|---|---|
| Deployable browser composition | [`apps/explorer-web/`](../../../apps/explorer-web/) | Current bounded app workspace |
| Explorer site composition | [`apps/explorer-web/src/site/`](../../../apps/explorer-web/src/site/) | Current map-first landing composition and repository catalog |
| App-local features and adapters | [`apps/explorer-web/src/features/`](../../../apps/explorer-web/src/features/) and [`src/adapters/`](../../../apps/explorer-web/src/adapters/) | Defensive projections and view-model behavior |
| Governed dynamic interface | [`apps/governed-api/`](../../../apps/governed-api/) | Current negative scaffold and future trust-bearing transport boundary |
| Restricted steward application | [`apps/review-console/`](../../../apps/review-console/) | Documentation scaffold; runtime on HOLD |
| Reusable UI code | [`packages/ui/`](../../../packages/ui/) | Current placeholder package |
| Renderer wrapper | [`packages/maplibre/`](../../../packages/maplibre/) | Current placeholder package and held adapter/runtime boundary |
| Semantic meaning | [`contracts/`](../../../contracts/) | Defines object meaning; this README does not |
| Machine shape | [`schemas/`](../../../schemas/) | Defines validated payload shape; this README does not |
| Admissibility | [`policy/`](../../../policy/) | Owns allow, deny, restrict, abstain, obligations, and redaction decisions |
| Executable proof | [`tests/`](../../../tests/) and [`fixtures/`](../../../fixtures/) | Positive, negative, boundary, replay, and accessibility evidence |
| Authoring provenance | [`data/receipts/generated/`](../../../data/receipts/generated/) | Generated authoring receipts; not review or release authority |
| Release/correction/rollback | [`release/`](../../../release/) and governed lifecycle records | Outside browser and documentation authority |
| Architecture explanation | `docs/architecture/ui/` | This lane |

> [!CAUTION]
> Do not create `packages/maplibre-runtime/`, a second UI package, another public shell, a parallel Evidence Drawer contract, or another architecture authority merely because older planning documents name one. Repository-present homes and any migration require an accepted decision, compatibility treatment, validation, documentation, and rollback.

[Back to top](#top)

---

## 5 · What belongs here

This folder contains bounded, human-facing UI architecture documentation:

- subsystem boundaries and responsibility maps;
- current-state evidence summaries pinned to repository state;
- trust-visible UI rules and finite negative-state behavior;
- renderer and map-interaction boundaries;
- Evidence Drawer, Focus, Story, Compare/Export, Review Console, trust-badge, telemetry, continuity, and accessibility architecture;
- current maturity classifications and explicit HOLDs;
- validation expectations, negative cases, migration notes, correction implications, and rollback procedures;
- links to the contracts, schemas, policy, code, fixtures, tests, workflows, receipts, ADRs, and runbooks that actually carry executable or governance behavior.

A document in this folder may explain a proposed contract or decision. It must label that proposal and point to the owning contract, schema, policy, code, or ADR rather than becoming a parallel authority. When a sibling's prose conflicts with current code, this README should surface the drift and defer current behavior to pinned implementation evidence.

[Back to top](#top)

---

## 6 · What does **not** belong here

| Artifact | Owning responsibility root |
|---|---|
| Executable browser, API, worker, or shared-package code | `apps/` or `packages/` |
| Semantic contracts | `contracts/` |
| JSON Schema or other machine shapes | `schemas/` |
| Allow/deny/restrict/abstain rules | `policy/` |
| Test fixtures and executable assertions | `fixtures/` and `tests/` |
| Source descriptors or lifecycle data | `data/registry/` and the governed data lifecycle |
| Receipts, proofs, release decisions, correction notices, withdrawal records, rollback cards | Their distinct `data/` and `release/` object families |
| Secrets, tokens, private prompts, raw evidence, exact restricted coordinates, protected identities | Never in public documentation |
| Generated screenshots, build output, temporary reports | Governed generated-output homes; never architecture authority |
| Runtime configuration, deployment credentials, service secrets | `runtime/`, `configs/`, `infra/`, or platform settings as applicable |

This folder must not become a second schema, policy, source registry, release registry, proof store, review ledger, or runtime package.

[Back to top](#top)

---

## 7 · Subsystem map

### Target trust direction

```text
source evidence + policy + review + active release + correction state
                                |
                                v
                  governed API / released carriers
                                |
                                v
                    browser validation and projection
                                |
         +----------------------+-----------------------+
         |                      |                       |
         v                      v                       v
 map and layer views      Evidence / Focus        story / compare /
                         / trust inspection       export / read-only review
                                |
                                v
               finite, accessible, correction-aware UI state
```

### Current composed Explorer reality

```text
apps/explorer-web/src/main.ts
    -> apps/explorer-web/src/site/mountExplorerSite.ts
       -> resolveBaselineShell()
          -> ABSTAIN / NO_GOVERNED_RESPONSE
       -> repository-grounded site catalog
          -> 38 feature entries
          -> 13 knowledge domains
          -> 8 trust principles
       -> synthetic renderer-neutral map stage
          -> deterministic map_runtime fixture bridge
          -> local Evidence Drawer projection
             -> ANSWER / ABSTAIN / DENY / ERROR demonstrations
       -> in-page section navigation and repository links

No live fetch, router, MapLibre import, EvidenceBundle resolver, model call,
policy engine, active release lookup, source activation, or publication path.
```

The composed site is broader than the old minimal entrypoint, but its authority remains narrow. Its map is explicitly illustrative, its catalog is descriptive, and its finite demonstrations are synthetic.

[Back to top](#top)

---

## 8 · Proposed directory tree

The heading is retained for anchor compatibility. The tree below is the **confirmed current documentation lane**, not a request to create a speculative tree.

```text
docs/architecture/ui/
├── README.md
├── ACCESSIBILITY.md
├── BOUNDARIES.md
├── COMPARE_AND_EXPORT.md
├── CONTINUITY_NOTES.md
├── EVIDENCE_DRAWER.md
├── FOCUS_FLOW.md
├── GOVERNED_SHELL.md
├── LAYERING.md
├── MAP_RUNTIME_BOUNDARY.md
├── REVIEW_CONSOLE.md
├── STORY_PLAYER.md
├── TELEMETRY.md
├── TRUST_BADGES.md
└── map-context-evidence-drawer-admission.md
```

This is fifteen tracked Markdown files: this landing page plus fourteen siblings. Their presence is confirmed; their freshness, authority, and implementation maturity vary and must be evaluated independently.

[Back to top](#top)

---

## 9 · Sibling documents

| Document | Primary concern | Current safe reading posture |
|---|---|---|
| [`ACCESSIBILITY.md`](./ACCESSIBILITY.md) | Keyboard, focus, semantics, alternatives, motion, and accessible trust states | Repository-grounded bounded Evidence Drawer proof; app-wide accessibility workflow and WCAG conformance remain HOLD/UNKNOWN; predates current site composition |
| [`BOUNDARIES.md`](./BOUNDARIES.md) | Browser authority, governed API, and forbidden operations | Repository-grounded trust map with useful negative scaffold evidence; current entrypoint description predates the site composition |
| [`COMPARE_AND_EXPORT.md`](./COMPARE_AND_EXPORT.md) | Comparison and outbound artifact boundaries | Repository-grounded placeholder-only result; no launch wiring, route, policy, schema, receipt, or export runtime is established |
| [`CONTINUITY_NOTES.md`](./CONTINUITY_NOTES.md) | Context preservation across map, evidence, Focus, story, export, and correction | Repository-grounded bounded proof inventory; no live continuity runtime; current entrypoint detail predates site composition |
| [`EVIDENCE_DRAWER.md`](./EVIDENCE_DRAWER.md) | Evidence inspection doctrine and proposed UI panel | **NEEDS RECONCILIATION:** proposal-era metadata says implementation is unknown, while current code/tests establish a bounded fixture-first drawer; use current code, contract/schema, tests, and newer references for current behavior |
| [`FOCUS_FLOW.md`](./FOCUS_FLOW.md) | Client-side Focus Mode sequence | **NEEDS RECONCILIATION:** proposal-era path and sibling assumptions; isolated Focus fixtures may exist, but no live composed Focus transport or route is established |
| [`GOVERNED_SHELL.md`](./GOVERNED_SHELL.md) | Current Explorer composition and graduation boundary | Current repository-grounded architecture reference matching the composed synthetic site; no live transport or MapLibre runtime |
| [`LAYERING.md`](./LAYERING.md) | Layer contracts, schemas, fixtures, admission, policy, release, and map-shell use | Current repository-grounded mixed-maturity map; validator and admission evidence are fixture-only; layer-home drift and MapLibre HOLD remain explicit |
| [`MAP_RUNTIME_BOUNDARY.md`](./MAP_RUNTIME_BOUNDARY.md) | Proposed renderer-neutral port and MapLibre adapter seam | **NEEDS RECONCILIATION:** proposal-era metadata, placeholder owners, stale/nonexistent links, and unverified authority claims; renderer runtime remains HOLD |
| [`REVIEW_CONSOLE.md`](./REVIEW_CONSOLE.md) | Restricted human review support | Current repository-grounded architecture; application remains a documentation scaffold with separate synthetic ReviewRecord proof and no operational runtime |
| [`STORY_PLAYER.md`](./STORY_PLAYER.md) | StoryManifest projection and future playback | Current repository-grounded bounded 2D projection consumer; no fetch, route, node resolution, map playback, policy execution, or publication |
| [`TELEMETRY.md`](./TELEMETRY.md) | Safe UI observability and graduation requirements | Current repository-grounded fixture-first profile register; general operational telemetry remains HOLD |
| [`TRUST_BADGES.md`](./TRUST_BADGES.md) | Compact trust projections | Current repository-grounded anti-collapse map; multiple bounded surfaces exist, but no universal canonical badge state or live transport is established |
| [`map-context-evidence-drawer-admission.md`](./map-context-evidence-drawer-admission.md) | Cross-object MapContext-to-Drawer candidate admission | Current bounded executable/no-network helper and synthetic proof; inactive runtime, no evidence resolution, policy, active-release lookup, or app/API integration |

This README is the navigation and reconciliation surface. It does not silently promote any sibling from draft or proposal to accepted architecture, and it does not let a newer landing-page summary erase useful historical or detailed content in a sibling.

[Back to top](#top)

---

## 10 · UI component families

The current UI surface mixes composed elements, independently executable fixture slices, descriptive catalog entries, documentation-only areas, and explicit holds. Repository catalog maturity labels are useful orientation, not governance or release outcomes.

| Component family | Current repository evidence | Current maturity boundary |
|---|---|---|
| Explorer site composition | `main.ts` mounts `mountExplorerSite`; site CSS, catalog, and deterministic composition code exist | **BOUNDED COMPOSED SITE** — local/static orientation and synthetic interaction only |
| Baseline shell state | `resolveBaselineShell()` returns fixed fail-closed outcomes | **VERIFIED SLICE** — absence/error semantics, not live transport |
| Trust Header and trust posture | Bounded projections and catalog entries exist; current site exposes shell/renderer chips and trust language | **BOUNDED PROJECTION** — not universal trust authority |
| Evidence Drawer | Strict app-local projection parser/view model, DOM rendering, and focused tests | **VERIFIED FIXTURE SLICE** — no authoritative evidence resolution or network path |
| Map evidence bridge | Renderer-neutral selection parsing and injected resolver with finite local outcomes | **VERIFIED FIXTURE SLICE** — no actual renderer, released feature, or live resolver |
| Knowledge-domain matrix | Thirteen app-local domain catalog entries with public-safety safeguards | **DESCRIPTIVE CATALOG** — not proof of live domain data or routes |
| Feature catalog | Thirty-eight entries across six areas with local maturity labels and repository paths | **DESCRIPTIVE CATALOG** — not a runtime registry, product roadmap authority, or release register |
| Story Player | Pure 2D public-safe StoryManifest projection consumer with tests | **BOUNDED CONSUMER** — no live playback route or map continuity |
| Focus Mode | Fixture-first components and architecture exist | **FIXTURE-FIRST / NOT COMPOSED** — no live governed transport or model path |
| Layer catalog and lineage | Documents, contracts, schemas, and fixture-first admission surfaces exist | **MIXED / NOT LIVE** — no active released-layer loader |
| Trust badges / attestation | Several bounded projection surfaces exist | **MIXED / NON-UNIVERSAL** — no canonical cross-surface profile |
| Compare and Export | Feature folders and README contracts exist | **PLACEHOLDER / DOCUMENTED** — no governed outbound artifact flow |
| Review Console | Architecture/feature docs and private scaffold package exist | **IMPLEMENTATION HOLD** — no operational reviewer application |
| Telemetry and diagnostics | Four bounded telemetry profiles plus documentation exist | **OPERATIONAL HOLD** — no general UI emitter, route, sink, or retention |
| MapLibre runtime | Package scaffold, adapter boundary comment, readiness records, and issues exist | **HOLD** — no admitted dependency or functional browser renderer |

No local maturity label can substitute for accepted architecture, policy, authenticated review, release state, deployment evidence, or public operation.

[Back to top](#top)

---

## 11 · Routes

### Current browser navigation

The composed Explorer site uses in-page fragment navigation for its current sections:

- `#map`
- `#knowledge`
- `#features`
- `#trust`

These are document-section anchors inside one composition, not a production route contract, client-side router, permalink grammar, or public API.

### Current Governed API routes

The current route registry contains exactly three GET scaffold routes:

- `/bootstrap`
- `/layers`
- `/evidence`

Each delegates to the current negative scaffold and returns `ABSTAIN / NOT_IMPLEMENTED`. Unsupported paths return a safe `ERROR`; non-GET calls to registered paths return a safe method error. This is useful fail-closed infrastructure, not a live Explorer transport contract or evidence-backed answer path.

### Future route requirements

Any future route design must preserve these invariants:

1. the map-first shell remains a composition surface, not a truth store;
2. route changes do not silently discard time, selection, evidence, release, correction, sensitivity, or representation context;
3. deep links carry safe public identifiers, not raw evidence, internal store keys, protected policy reasons, or restricted geometry;
4. unavailable, stale, denied, superseded, or failed state is rendered explicitly rather than replaced by guessed content;
5. privileged review and administration remain separated from ordinary public navigation;
6. exact route names, DTOs, ownership, cache semantics, authentication, and rollback are verified in implementation and documented in one controlling route authority before use.

Route families such as explore, evidence, focus, story, compare, export, settings, diagnostics, and read-only review remain descriptive architecture terms until implementation and tests establish exact paths.

[Back to top](#top)

---

## 12 · Finite outcomes

The public claim-bearing UI outcome vocabulary is:

| Outcome | UI meaning | Disclosure rule |
|---|---|---|
| `ANSWER` | Released, policy-safe, citation-capable support is available for the bounded request | Show only the authorized public-safe claim, evidence references, citations, limitations, trust state, and correction context |
| `ABSTAIN` | Support is missing, stale, unresolved, superseded, conflicted, outside scope, or otherwise insufficient | Explain the bounded safe reason; do not manufacture or infer a claim |
| `DENY` | Policy, rights, sensitivity, access, purpose, audience, or safety blocks disclosure | Use fixed no-leak copy; do not expose protected details or reason internals |
| `ERROR` | A validator, resolver, transport, policy engine, parser, artifact check, or runtime failed | Fail closed; do not downgrade failure into an answer or stale cached success |

`PASS`, `FAIL`, `HOLD`, `READY`, and `BLOCKED` may describe validation, review, admission, or workflow state. They are not substitutes for the public response outcomes above.

Current code demonstrates all four outcomes through bounded local projections. The baseline shell itself proves the absence and unsupported-input paths. None of these demonstrations proves a live governed response, active release, or public claim.

[Back to top](#top)

---

## 13 · Trust membrane

The UI must preserve all of these boundaries:

- ordinary browser code reads governed interfaces or already released public-safe carriers, not RAW, WORK, QUARANTINE, PROCESSED, candidate, canonical, internal, graph, vector, object, proof, or model stores as normal truth paths;
- `EvidenceRef` resolves to an admissible `EvidenceBundle` before a consequential claim is presented as authoritative;
- map pixels, decorative geometry, tile properties, feature-state, camera state, clicks, route fragments, catalog labels, screenshots, and animations are candidates or context, not evidence;
- policy, rights, sensitivity, purpose, audience, review, and active release decisions remain upstream;
- direct model-provider or model-runtime calls from the browser are denied;
- negative outcomes use fixed, non-reflective copy and do not echo protected upstream content;
- corrections, supersessions, withdrawals, release identity, representation limits, and stale state remain visible where material;
- UI telemetry excludes raw evidence, prompts, secrets, identities, exact restricted locations, source payloads, and protected policy reasons;
- exports preserve the evidence/release/correction context needed to inspect what was shown and are blocked when rights or policy are unresolved;
- restricted review surfaces never become hidden administrative bypasses or ordinary public paths.

Current enforcement is partial. The repository contains strict app-local parsing, finite projection behavior, source-level boundary guards, read-only workflows, synthetic no-network profiles, and focused tests. Complete network, information-flow, authentication, authorization, CSP, deployment, renderer, artifact-integrity, evidence-resolution, and runtime-policy enforcement is not established.

[Back to top](#top)

---

## 14 · Layer trust badges

A trust badge, chip, header, score, icon, or label is a projection of governed state, not proof by itself.

Where applicable, a claim-bearing layer or UI surface should expose the public-safe subset of:

- source role and authority class;
- observed, valid, source, retrieval, release, correction, and freshness time as applicable;
- policy/access outcome and obligations;
- rights, sensitivity, consent, redaction, generalization, delay, or suppression state;
- review state;
- release state and release identifier;
- evidence resolution and citation state;
- correction, supersession, withdrawal, or rollback state;
- representation limits, including generalized, modeled, synthetic, or derived geometry where material;
- attestation or artifact-integrity state when it has been independently verified.

The repository currently contains multiple bounded trust projections rather than one universal canonical badge model. The site composition also uses simple posture chips. These surfaces must not be silently collapsed into a universal authority vocabulary.

Badges and chips must never:

- imply an accepted ADR where none exists;
- turn a successful test, attestation parse, or workflow into publication;
- expose restricted reason text or precise protected detail;
- rely on color alone;
- hide stale, denied, corrected, generalized, superseded, or unreleased state;
- allow users to infer that a descriptive catalog maturity label is a policy, review, or release decision.

[Back to top](#top)

---

## 15 · Accessibility expectations

### Confirmed bounded behavior

Current repository evidence includes:

- a skip link to the Explorer main content;
- labeled navigation and semantic `main`, section, header, and aside structures in the composed site;
- text labels for shell and renderer posture;
- a synthetic map SVG with an accessible title/description and an explicit statement that the geometry is illustrative, not factual data;
- native controls and text labels in bounded feature slices;
- Evidence Drawer focus movement to the close control, Escape-to-close behavior, focus restoration, and fixed no-leak negative copy;
- focused browser tests for bounded components.

### Required architecture posture

A mature UI must demonstrate, through representative automated and manual evidence:

- complete keyboard operation and visible focus across the composed route system;
- stable heading, landmark, list, table, status, dialog, and live-region semantics;
- accessible names, descriptions, state changes, and error/denial announcements;
- text/icon alternatives to color, shape, position, motion, map-only encoding, and visual hierarchy;
- reduced-motion, high-contrast, zoom, reflow, and responsive support;
- screen-reader-accessible evidence, citations, histories, legends, timelines, filters, and controls;
- non-map alternatives for consequential information;
- safe focus behavior during navigation, drawer, modal, correction, stale, denial, and transport-failure transitions;
- representative assistive-technology testing and documented limitations.

Repository tests prove only their bounded fixtures. The accessibility workflow remains a readiness HOLD and does not establish whole-app WCAG 2.2 AA conformance, browser/assistive-technology parity, deployment, release, or public accessibility.

[Back to top](#top)

---

## 16 · Validation

### Focused repository-native checks

A documentation-only update to this landing page should run the applicable metadata, Markdown, link/anchor, stale-claim, document-graph, and generated-receipt checks. UI behavior did not change in this slice, but the current claims should remain compatible with the repository's executable evidence.

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  docs/architecture/ui/README.md \
  --repo-root . \
  --profile required

pnpm --dir apps/explorer-web build
pnpm --dir apps/explorer-web test:unit
pnpm --dir apps/explorer-web test:browser

python -m pytest -q tests/policy/test_explorer_web_adapter_boundary.py

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/<current-ui-readme-receipt>.json \
  --repo-root .
```

The read-only [`ui-build` workflow](../../../.github/workflows/ui-build.yml) checks locked readiness, build, unit tests, and browser tests. Documentation workflows should supply repository-native metadata, link, graph, and stale-reference coverage according to their path triggers.

### Acceptance matrix

| Change type | Minimum evidence |
|---|---|
| README-only reconciliation | Complete target review, metadata, Markdown structure, links/fragments, sibling inventory, stale-claim review, changed-file closure, receipt binding, and hosted docs checks |
| Site catalog or composition change | TypeScript build, deterministic catalog tests, source/path uniqueness, sensitive-domain safeguards, and preservation of renderer HOLD |
| UI view-model change | Unit tests for `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, malformed input, evidence scoping, and no-leak behavior |
| Browser interaction change | Playwright coverage for keyboard, focus, landmarks, navigation, negative-state disclosure, and teardown |
| Governed transport change | Accepted contract/schema compatibility, positive and negative fixtures, no direct-store access, transport/auth failure tests, policy/release/correction context, and audit-safe telemetry |
| Map runtime change | Accepted package/seam decision, pinned dependency, acquisition/import enforcement, artifact and browser probes, accessibility/performance budgets, correction behavior, and rollback |
| Compare/export or public artifact change | Evidence, rights, sensitivity, release manifest, artifact integrity, citation preservation, correction/cache propagation, and rollback evidence |
| Restricted review surface change | Authenticated role/purpose checks, actor and duty separation, immutable audit reference, CSRF/XSS/IDOR controls, finite safe reasons, and no direct lifecycle mutation |

A green workflow is validation evidence only. It is not human review, policy approval, release, deployment, or publication authority.

[Back to top](#top)

---

## 17 · Inputs

### Current composed inputs

The current Explorer composition consumes repository-local, deterministic inputs:

- the fixed baseline shell resolver;
- the frozen repository snapshot and descriptive feature/domain/principle catalog;
- five synthetic renderer-neutral map-selection cases;
- injected in-memory resolver behavior;
- bounded public-safe Evidence Drawer projections;
- repository links pinned to the catalog snapshot.

No current site-composition code performs a fetch, calls a model, reads lifecycle stores, activates a source, or resolves a real release.

### Intended governed inputs

Future UI composition may consume only validated, policy-safe forms such as:

- finite governed response envelopes under an accepted contract;
- released layer/style/tile manifests and verified public-safe carriers;
- Evidence Drawer projections derived from resolved evidence;
- bounded Focus and Story projections;
- release, freshness, review, correction, representation, and integrity state;
- safe public identifiers, viewport/time context, and candidate selections;
- authenticated restricted-review projections through a separate role-gated application path.

The UI must not accept raw source bytes, arbitrary model output, canonical store records, policy internals, secrets, protected identities, or restricted exact geometry as ordinary client input.

[Back to top](#top)

---

## 18 · Outputs

### Current composed outputs

The current site produces:

- a repository-grounded orientation page;
- in-page navigation;
- descriptive domain and feature catalogs;
- a clearly labeled synthetic map illustration;
- deterministic local finite-outcome demonstrations;
- public-safe Evidence Drawer projections;
- links to repository boundaries and open governance work.

These outputs are documentation/orientation and synthetic proof. They are not KFM public claims, released map layers, active catalog records, review decisions, or publication artifacts.

### Permitted future UI outputs

Permitted UI outputs include:

- finite, accessible view states;
- evidence and citation displays derived from governed support;
- map-selection candidates for governed resolution;
- safe filter, camera, layer, and time-state changes;
- bounded Focus and Story requests/responses;
- comparisons and exports that preserve release/citation/correction context;
- privacy-safe operational telemetry when an operative contract/policy/runtime exists;
- correction, stale, supersession, withdrawal, and representation notices;
- read-only reviewer orientation separated from authority-bearing review submission.

The UI does not emit source admission decisions, canonical evidence, policy approval, authenticated review approval, promotion or release decisions, publication state, proof closure, hidden reasoning as evidence, or unreviewed sensitive-location transforms.

A screenshot, story, map state, badge, catalog label, synthetic diagram, or export remains a downstream carrier and must not be represented as sovereign truth.

[Back to top](#top)

---

## 19 · Review burden

| Concern | Required review perspective |
|---|---|
| Architecture and responsibility boundaries | Architecture/UI maintainer |
| Governed transport and runtime envelope | Governed API and contract/schema maintainer |
| Evidence and citation projection | Evidence maintainer |
| Rights, sensitivity, access, purpose, and negative-state copy | Policy/privacy/sensitivity reviewer |
| Renderer and dependency seam | Map/runtime and supply-chain reviewer |
| Keyboard, screen-reader, non-map, and cognitive accessibility | Accessibility reviewer |
| Review Console identity, authority, and audit | Review/security/governance reviewer |
| Telemetry minimization and retention | Observability/privacy/security reviewer |
| Release, correction, export, cache, and rollback | Release/correction reviewer |
| Documentation accuracy, links, anchors, and supersession | Docs maintainer |

CODEOWNERS currently routes the repository and relevant roots to `@bartytime4life`. That is a confirmed GitHub review route, not proof that the independent roles above are assigned, that specialist review occurred, or that separation of duties is enforced.

Material changes to an ADR, contract, schema, policy, release rule, object-family meaning, or responsibility boundary belong in their owning surface and may require a separate pull request. This README must not accept its own proposals.

[Back to top](#top)

---

## 20 · Related folders

| Path | Relationship |
|---|---|
| [`apps/explorer-web/`](../../../apps/explorer-web/) | Current deployable Explorer workspace |
| [`apps/explorer-web/src/site/`](../../../apps/explorer-web/src/site/) | Current map-first landing composition and descriptive repository catalog |
| [`apps/explorer-web/src/features/`](../../../apps/explorer-web/src/features/) | App-local bounded feature slices and placeholders |
| [`apps/explorer-web/src/adapters/`](../../../apps/explorer-web/src/adapters/) | Defensive app-local input boundaries |
| [`apps/governed-api/`](../../../apps/governed-api/) | Current negative scaffold and future trust-bearing dynamic interface |
| [`apps/review-console/`](../../../apps/review-console/) | Restricted steward/review application scaffold |
| [`packages/ui/`](../../../packages/ui/) | Current shared-UI placeholder package |
| [`packages/maplibre/`](../../../packages/maplibre/) | Current renderer placeholder package and held acquisition seam |
| [`contracts/ui/`](../../../contracts/ui/) | UI-facing semantic contracts |
| [`contracts/runtime/`](../../../contracts/runtime/) | Runtime envelope and admission semantics |
| [`schemas/contracts/v1/ui/`](../../../schemas/contracts/v1/ui/) | UI machine validation shapes |
| [`policy/ui/`](../../../policy/ui/) | UI policy orientation and proposed rules |
| [`tests/`](../../../tests/) | Cross-root executable tests |
| [`fixtures/`](../../../fixtures/) | Positive and negative fixture families |
| [`data/receipts/generated/`](../../../data/receipts/generated/) | AI authoring provenance; not approval or publication |
| [`release/`](../../../release/) | Release, correction, withdrawal, supersession, and rollback control |
| [`docs/architecture/governed-ai/`](../governed-ai/) | Governed AI and Focus architecture |
| [`docs/architecture/story/`](../story/) | Story architecture |
| [`docs/architecture/review/`](../review/) | Review architecture |
| [`docs/runbooks/`](../../runbooks/) | Operational procedures |

Compatibility roots such as `ui/`, `web/`, `styles/`, `viewer_templates/`, and `artifacts/` must not become parallel canonical shell, renderer, policy, release, or architecture authorities without an accepted migration decision.

[Back to top](#top)

---

## 21 · ADRs that govern this folder

The table separates accepted placement authority from proposed UI decisions. Effective status comes from the current [`ADR index`](../../adr/INDEX.md), not from repetition in architecture prose.

| ADR | Effective status | Relevance |
|---|---|---|
| [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **accepted** | Adopts Directory Rules v2 and establishes responsibility-root placement law |
| [`ADR-0004`](../../adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md) | proposed | Governed API as the trust membrane |
| [`ADR-0005`](../../adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md) | proposed | Explorer Web as the canonical map-first shell |
| [`ADR-0006`](../../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) | proposed | One MapLibre acquisition/import seam |
| [`ADR-0007`](<../../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>) | proposed | Sole browser-renderer family and exception governance |
| [`ADR-0016`](../../adr/ADR-0016-telemetry-redaction-posture.md) | proposed | Telemetry minimization and redaction posture |
| [`ADR-0019`](../../adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md) | proposed | Governed AI adapter and finite envelopes |
| [`ADR-0020`](../../adr/ADR-0020-abstain-is-a-first-class-decision.md) | proposed | First-class abstention |
| [`ADR-0025`](../../adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md) | proposed | Public-client store boundary |

Until a decision is accepted, implementation and documentation may prepare, test, or describe the proposal but must not label it binding. Repository presence and successful tests do not independently accept an ADR.

[Back to top](#top)

---

## 22 · FAQ

### Is this README canonical UI decision authority?

No. It is the architecture-lane landing page. Accepted ADRs, adopted Directory Rules, contracts, schemas, policy, current implementation evidence, review records, and release records control their respective questions.

### Is `apps/explorer-web/` implemented?

Yes, in a bounded sense. It has a real configured workspace, a map-first landing composition, a fail-closed baseline resolver, a descriptive repository catalog, deterministic synthetic map/evidence interaction, and independently tested feature slices. It does **not** establish a live map product, production router, governed transport, released-layer flow, authentication, deployment, or public operation.

### Is the current Explorer map real data?

No. The current map artwork is explicitly illustrative, and the interaction laboratory uses synthetic renderer-neutral selections and local projections. It scopes deterministic tests and demonstrations; it does not represent an observation, active layer, official advisory, or life-safety instruction.

### Is MapLibre currently running in Explorer?

No current repository evidence establishes that. Explorer declares no `maplibre-gl` dependency, `packages/maplibre/` remains a private placeholder, and `MapLibreAdapter.ts` is comment-only. The concrete renderer remains on HOLD.

### Are the thirty-eight feature catalog entries implemented routes?

No. They are descriptive repository entries with bounded local maturity labels. Some point to executable fixture slices, some to documentation, some to placeholders, and MapLibre is explicitly held. The catalog is not a route registry, product release register, or architecture decision.

### Does the Governed API currently answer evidence requests?

No evidence-backed answer path is established. The current `/bootstrap`, `/layers`, and `/evidence` routes return `ABSTAIN / NOT_IMPLEMENTED`; unsupported operations fail safely.

### Does Review Console work as an application?

No. The repository contains its architecture and feature documentation, a private placeholder package, and separate synthetic ReviewRecord validation proof. It does not contain an operational reviewer queue, authenticated actor/role system, decision recorder, audit ledger, policy engine, API composition, deployment, or release authority.

### Does a trust badge prove evidence, policy, or release?

No. It summarizes a bounded public-safe projection. The underlying evidence, policy, review, release, correction, and artifact-integrity records remain authoritative.

### Can a model answer be rendered when citations are unavailable?

No consequential answer should be presented as authoritative. The UI returns or displays `ABSTAIN`, `DENY`, or `ERROR` according to the finite outcome and policy state.

### May the UI read `data/published/` directly because the content is public-safe?

Not as an assumed normal browser path. Public clients use governed interfaces or released carriers with verified integrity and release context. Direct filesystem or canonical-store access is not a browser authority shortcut.

### Does a passing UI workflow publish KFM?

No. Tests, workflows, commits, pull requests, merges, builds, deployments, badges, and documentation updates are not publication decisions.

[Back to top](#top)

---

## 23 · Open questions and verification backlog

### P0 · Documentation convergence and authority clarity

- **NEEDS VERIFICATION:** reconcile [`EVIDENCE_DRAWER.md`](./EVIDENCE_DRAWER.md) with the current bounded implementation, contract/schema, tests, and map-evidence composition.
- **NEEDS VERIFICATION:** reconcile [`FOCUS_FLOW.md`](./FOCUS_FLOW.md) with current Focus fixtures, current contract homes, governed-AI boundaries, and the actual absence of a live composed route.
- **NEEDS VERIFICATION:** reconcile [`MAP_RUNTIME_BOUNDARY.md`](./MAP_RUNTIME_BOUNDARY.md) with accepted Directory Rules, current package homes, current ADR identities, acquisition enforcement, and MapLibre HOLD.
- **NEEDS VERIFICATION:** refresh entrypoint-specific claims in [`BOUNDARIES.md`](./BOUNDARIES.md), [`ACCESSIBILITY.md`](./ACCESSIBILITY.md), [`COMPARE_AND_EXPORT.md`](./COMPARE_AND_EXPORT.md), and [`CONTINUITY_NOTES.md`](./CONTINUITY_NOTES.md) against the composed site.
- **NEEDS VERIFICATION:** assign accountable UI, API, map-runtime, accessibility, evidence, policy, review, release, security, telemetry, and operations stewardship without confusing CODEOWNERS routing with substantive authority.

### P0 · Trust-bearing runtime closure

- **OPEN:** accept or revise the canonical Explorer shell, governed API, renderer, finite-envelope, abstention, telemetry, and public-client decisions.
- **OPEN:** establish one accepted runtime response contract shared by Governed API and Explorer.
- **OPEN:** implement authenticated, bounded live transport while preserving strict finite outcomes, no-leak behavior, request budgets, and safe error handling.
- **OPEN:** resolve `EvidenceRef -> EvidenceBundle` through an admitted repository/runtime abstraction before consequential answers.
- **OPEN:** compose operative rights, sensitivity, access, purpose, audience, review, active release, correction, and withdrawal checks.
- **OPEN:** implement released artifact verification, loader isolation, cache invalidation, correction propagation, and rollback behavior.

### P1 · Map, navigation, and user workflow closure

- **OPEN:** resolve the physical and semantic `MapRuntimePort` / `MapLibreAdapter` home without creating a second active package.
- **OPEN:** admit the concrete renderer dependency only after version, integrity, import/acquisition, browser, accessibility, performance, security, and rollback evidence closes.
- **OPEN:** define and test route/deep-link continuity for map, time, selection, evidence, Focus, story, compare, export, settings, diagnostics, and read-only review.
- **OPEN:** connect released-layer map selection to governed evidence resolution without exposing renderer-native or internal-store state.
- **OPEN:** decide whether the descriptive site catalog is generated, manually curated, or replaced by a governed registry projection; add drift detection accordingly.
- **OPEN:** graduate Story Player, Focus, Compare/Export, and read-only review from isolated/documented surfaces to bounded governed composition.

### P1 · Security, accessibility, telemetry, and operations

- **NEEDS VERIFICATION:** authentication, authorization, CSP, CORS, CSRF, XSS, IDOR, cache, worker, protocol, dependency, artifact-integrity, and deployment posture.
- **NEEDS VERIFICATION:** whole-app keyboard, screen-reader, reflow, reduced-motion, high-contrast, cognitive accessibility, and non-map parity.
- **NEEDS VERIFICATION:** operational telemetry contract, fail-closed policy, emitter, governed route, sink, retention, deletion, incident response, correction, and no-raw-evidence guarantees.
- **NEEDS VERIFICATION:** performance and memory budgets for catalog growth, map runtime, evidence interaction, story playback, and constrained devices.
- **UNKNOWN:** production deployment, service health, browser matrix, public traffic, incident history, recovery objectives, and operational release state.

Open items should be resolved in the owning ADR, contract, schema, policy, code, test, workflow, runbook, or register. This README may link to those decisions; it must not silently close them.

[Back to top](#top)

---

## Appendix A · No-loss modernization ledger

| Prior material or identity | v4.0-draft treatment |
|---|---|
| Document path, `doc_id`, title, H1, `top` anchor, twenty-three numbered sections, and Appendix A | **Retained** |
| Map-first, time-aware, evidence-bounded UI purpose | **Retained and tied to current composition evidence** |
| Cite-or-abstain, finite outcomes, no direct stores, no direct model client | **Retained and strengthened with current trust-boundary evidence** |
| Prior claim that `main.ts` mounts only the baseline shell and Evidence Drawer | **Corrected** — current entrypoint mounts `mountExplorerSite` |
| Current fail-closed baseline resolver | **Retained** as a nested safety primitive rather than the whole composed app |
| Current Explorer composition | **Added** — synthetic map stage, evidence lab, thirteen domains, thirty-eight feature entries, and eight principles |
| Current Governed API route state | **Added** — three GET ABSTAIN scaffolds plus safe unsupported-operation errors |
| UI sibling inventory | **Corrected** — `REVIEW_CONSOLE.md` added; current lane is fifteen files total |
| Sibling document currentness | **Classified** — current repository-grounded references separated from proposal-era pages needing reconciliation |
| Story Player bounded executable slice | **Added** without implying live playback or publication |
| Review Console and operational telemetry maturity | **Narrowed** to explicit implementation HOLDs |
| MapLibre GL JS implementation or package admission | **Not claimed**; renderer remains HOLD |
| Exact production route tree, authentication, deployment, and public operation | **Not claimed** |
| Accessibility, telemetry, export, correction, rollback, and review expectations | **Retained with explicit maturity limits** |
| Contract, schema, policy, fixture, validator, code, workflow, source, release, deployment, publication, or settings changes | **None in this documentation slice** |

### Rollback

The documentation rollback target is prior blob `36d975710d906a6c4146c550d40929b1822b667e`. Reverting this documentation change restores the previous README. Remove only the companion generated authoring receipt introduced by the same change. No app code, contract, schema, policy, fixture, validator, workflow, source, evidence, lifecycle state, release, deployment, cache, or public state requires rollback.

---

**Last reviewed:** `2026-08-19` against `main@d639f9ff40288d12244cd7bc84af538652f6dfb1`  
**Truth posture:** CONFIRMED repository evidence / PROPOSED architecture and integration / UNKNOWN deployment and public operation

[Back to top](#top)
