<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/ui/readme
title: UI Subsystem — Architecture README
type: standard
version: v3-draft
status: draft
owners:
  - "@bartytime4life"
created: 2026-05-08
updated: 2026-08-14
policy_label: public
owning_root: docs/
responsibility: "Provide the repository-grounded landing page for KFM UI architecture, trust boundaries, current implementation evidence, sibling documents, validation expectations, and open verification work without granting decision, release, deployment, or publication authority."
truth_posture: "CONFIRMED repository evidence / PROPOSED architecture / UNKNOWN deployed behavior; cite-or-abstain"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3974da9794fa11bd5355c49243c9193d22b9e81e
  target_prior_blob: 96a5dcc44ecb652c27e7f1e75e9634488d9aa9d0
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  explorer_readme_blob: 3d7944fcd31b7edeabca5b793eb7b88e12563f56
  explorer_package_blob: ddd201b74a06001d84a14bf54ac62a6cc3607a29
  explorer_main_blob: 9c95ae67333b7cbf6bc88051fa5c76e4cd97efa4
  explorer_shell_blob: 64c78c78820af33fb7a622094e4c0944ad9412f8
  evidence_drawer_blob: 7746843c259594568fe75e975155a67eb8372e8f
  maplibre_adapter_blob: 663ba0f7a05498948f67d644387c73ab19d5c16c
  packages_ui_entry_blob: 2c9ea341d61bf4d1733b9982fda8a9b869a3a720
  packages_maplibre_entry_blob: 91664eb00583f9e3d0405eb7954fefa9a48f4ee9
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
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
  - docs/architecture/ui/STORY_PLAYER.md
  - docs/architecture/ui/TELEMETRY.md
  - docs/architecture/ui/TRUST_BADGES.md
  - docs/architecture/ui/map-context-evidence-drawer-admission.md
  - docs/architecture/governed-ai/README.md
  - docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - docs/adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md
  - docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - apps/explorer-web/README.md
  - apps/governed-api/README.md
  - packages/ui/README.md
  - packages/maplibre/README.md
  - policy/ui/README.md
  - tests/policy/test_explorer_web_adapter_boundary.py
  - .github/workflows/ui-build.yml
tags: [kfm, ui, architecture, explorer-web, governed-api, maplibre, evidence-drawer, focus-mode, accessibility, finite-outcomes, trust-membrane]
notes:
  - "v3-draft is a same-path, documentation-only current-state reconciliation."
  - "ADR-0029 is accepted and provides placement authority; the UI, shell, MapLibre-boundary, sole-renderer, finite-envelope, abstention, and public-client ADRs remain proposed at the pinned evidence snapshot."
  - "The current Explorer entrypoint is a bounded fail-closed shell with a fixture-driven Evidence Drawer. It is not a functional map product, live governed-API client, released-layer flow, deployment, or publication surface."
  - "packages/ui/ and packages/maplibre/ are repository-present placeholder packages; packages/maplibre-runtime/ and docs/architecture/maplibre-3d.md are not treated as current authorities."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI Subsystem — Architecture README

> **Repository-grounded landing page.** KFM's user interface is a map-first, time-aware, evidence-bounded client surface. It may render governed finite outcomes and already released public-safe carriers; it does not own truth, evidence, policy, release, correction, rollback, source admission, or model execution.

> [!IMPORTANT]
> **Current evidence is bounded.** At `main@3974da9794fa11bd5355c49243c9193d22b9e81e`, the repository contains a buildable fixture-first Explorer shell, a strict Evidence Drawer projection, UI tests, architecture documents, and placeholder UI/MapLibre packages. The default entrypoint still renders a fixed fail-closed state; no functional browser map, live governed-API transport, accepted renderer dependency, released-layer flow, deployment, or public operation is established.

| Field | Current value |
|---|---|
| **Document status** | `draft` / architecture guidance |
| **Placement authority** | [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts Directory Rules v2 |
| **UI decision authority** | The relevant shell, renderer, finite-envelope, abstention, and public-client ADRs remain `proposed` at the evidence snapshot |
| **Repository review route** | `@bartytime4life` through CODEOWNERS; this is not proof of independent approval |
| **Current implementation** | Bounded static shell plus fixture-driven, keyboard-operable Evidence Drawer |
| **Map runtime** | `HOLD`: `packages/maplibre/` and `MapLibreAdapter.ts` are placeholders; Explorer has no renderer dependency |
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
- what is currently present in the repository;
- how the public shell, governed API, renderer seam, Evidence Drawer, Focus Mode, story, compare/export, telemetry, and accessibility surfaces relate;
- which claims are architectural targets rather than implemented behavior;
- which documents and ADRs carry the detailed decisions;
- what validation and review evidence is required before stronger maturity claims are made.

The UI is downstream of the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET
    -> governed release
    -> governed API or released public-safe carrier
    -> Explorer Web / Evidence Drawer / Focus Mode / export
```

The browser may help users inspect, navigate, compare, and request evidence. It must not turn a rendered feature, tile property, visual emphasis, generated summary, or model response into authoritative evidence.

[Back to top](#top)

---

## 2 · Authority level

This file is an **architecture landing page**, not an accepted decision record. Authority is resolved by the question being asked.

| Question | Controlling evidence |
|---|---|
| Where does this file belong? | Accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), adopted [`directory-rules.md`](../../doctrine/directory-rules.md), and the existing same-path `docs/architecture/ui/` lane |
| What exists now? | Pinned repository files, package manifests, tests, workflows, and emitted artifacts |
| What should the UI eventually do? | Proposed UI architecture, reviewed contracts/schemas/policy, and accepted ADRs |
| May a claim or detail be shown? | Resolved evidence, policy, review, release, sensitivity, rights, and correction state |
| Is something published? | A governed release decision and released artifact state, not this README, a build, a test, or a pull request |

At the current snapshot, [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) is the only accepted numbered ADR. The UI-related ADRs referenced below remain proposed and must not be written as settled architecture.

[Back to top](#top)

---

## 3 · Status

### Confirmed current repository evidence

| Surface | Verified state | Boundary |
|---|---|---|
| `docs/architecture/ui/` | This README and thirteen focused UI architecture documents are present | Presence does not prove freshness, acceptance, or implementation |
| [`apps/explorer-web/package.json`](../../../apps/explorer-web/package.json) | Vite, TypeScript, Vitest, and Playwright scripts are configured; no runtime renderer dependency is declared | Build tooling is not a functional map or deployment |
| [`apps/explorer-web/src/main.ts`](../../../apps/explorer-web/src/main.ts) | Mounts the baseline shell and Evidence Drawer | No route tree, map, API transport, authentication, or released data is composed |
| Baseline shell | Returns fixed `ABSTAIN / NO_GOVERNED_RESPONSE`; supplied input returns fixed `ERROR / UNSUPPORTED_BASELINE_INPUT`; both carry zero evidence references | A safe baseline, not a live response pipeline |
| Evidence Drawer | Strict fixture projection parser, finite states, fixed no-leak negative copy, evidence/citation/history display, keyboard open/close and focus return | No live API request, policy execution, or canonical payload adoption is established |
| [`MapLibreAdapter.ts`](../../../apps/explorer-web/src/adapters/MapLibreAdapter.ts) | One boundary comment and no implementation | No functioning renderer seam |
| [`packages/ui/`](../../../packages/ui/) | Private placeholder entrypoint | No shared component API is established |
| [`packages/maplibre/`](../../../packages/maplibre/) | Private placeholder entrypoint | No MapLibre dependency, adapter, plugin set, or runtime is established |
| UI review routing | `@bartytime4life` is the verified CODEOWNERS route | Review routing is not independent approval or release authority |

### Proposed architecture

The following remain architectural targets unless a current file, test, run, or accepted decision proves otherwise:

- a persistent map-first shell and route composition;
- a functioning renderer-neutral `MapRuntimePort` and accepted MapLibre adapter seam;
- live governed-API transport and canonical runtime envelopes;
- released layer loading and governed map-selection resolution;
- Focus Mode transport, story playback, compare/export, diagnostics, and steward-review composition;
- complete accessibility, security, telemetry, performance, correction, rollback, and deployment behavior.

### Unknown or not established

Deployment topology, authentication, authorization, CSP, CORS, cache behavior, service health, production telemetry, browser support, live data exposure, public operation, and runtime release state were not verified for this update.

[Back to top](#top)

---

## 4 · Repo fit

The existing path is placement-safe under the accepted Directory Rules:

- `docs/` owns human-facing explanation and architecture;
- `docs/architecture/` owns cross-system architecture descriptions;
- `docs/architecture/ui/` is the existing UI architecture lane;
- domain and product concerns stay inside their responsibility roots rather than becoming new root folders.

| Responsibility | Current or expected home | UI relationship |
|---|---|---|
| Deployable browser shell | [`apps/explorer-web/`](../../../apps/explorer-web/) | Current bounded implementation surface |
| Governed dynamic interface | [`apps/governed-api/`](../../../apps/governed-api/) | Normal trust-bearing network boundary; implementation maturity must be verified separately |
| Reusable UI code | [`packages/ui/`](../../../packages/ui/) | Current placeholder package |
| Renderer wrapper | [`packages/maplibre/`](../../../packages/maplibre/) | Current placeholder package and unresolved proposed boundary |
| Semantic meaning | [`contracts/`](../../../contracts/) | Defines object meaning; this README does not |
| Machine shape | [`schemas/`](../../../schemas/) | Defines validated payload shape; this README does not |
| Admissibility | [`policy/`](../../../policy/) | Decides allow, deny, restrict, abstain, and obligations |
| Executable proof | [`tests/`](../../../tests/) and [`fixtures/`](../../../fixtures/) | Positive and negative behavior evidence |
| Release/correction/rollback | [`release/`](../../../release/) and governed lifecycle records | Outside browser authority |
| Architecture explanation | `docs/architecture/ui/` | This lane |

> [!CAUTION]
> Do not create `packages/maplibre-runtime/`, a second UI package, a second public shell, or another architecture authority merely because older planning documents name one. The repository-present home and any migration require an accepted decision, compatibility treatment, tests, and rollback.

[Back to top](#top)

---

## 5 · What belongs here

This folder should contain bounded, human-facing UI architecture documentation:

- subsystem boundaries and responsibility maps;
- current-state evidence summaries;
- trust-visible UI rules;
- renderer and map-interaction boundaries;
- Evidence Drawer, Focus, story, compare/export, badge, telemetry, and accessibility architecture;
- validation expectations, negative states, migration notes, and rollback implications;
- links to the contracts, schemas, policy, code, tests, ADRs, and runbooks that actually carry executable behavior.

A document in this folder may explain a proposed contract or decision. It must label that proposal and point to the owning contract, schema, policy, code, or ADR rather than becoming a parallel authority.

[Back to top](#top)

---

## 6 · What does **not** belong here

| Artifact | Owning responsibility root |
|---|---|
| Executable browser or shared-package code | `apps/` or `packages/` |
| Semantic contracts | `contracts/` |
| JSON Schema or other machine shapes | `schemas/` |
| Allow/deny/restrict/abstain rules | `policy/` |
| Test fixtures and executable assertions | `fixtures/` and `tests/` |
| Source descriptors or lifecycle data | `data/registry/` and the governed data lifecycle |
| Receipts, proofs, release decisions, correction notices, rollback records | Their distinct data/release object families |
| Secrets, tokens, private prompts, exact restricted coordinates, raw evidence | Never in public documentation |
| Generated screenshots, build output, temporary reports | Governed generated-output homes; never as architecture authority |

This folder must not become a second schema, policy, source registry, release registry, proof store, or runtime package.

[Back to top](#top)

---

## 7 · Subsystem map

```text
source evidence + policy + review + release state
                         |
                         v
              governed API / released carriers
                         |
                         v
             browser validation and projection
                         |
          +--------------+----------------+
          |                               |
          v                               v
 bounded Explorer shell            candidate map context
          |                               |
          v                               v
 Evidence Drawer / Focus / story / compare / export
          |
          v
 finite, trust-visible UI state with correction lineage
```

**Current implemented composition is smaller:**

```text
apps/explorer-web/src/main.ts
    -> fixed fail-closed shell state
    -> fixture-driven Evidence Drawer
```

Map rendering, route composition, live transport, and released-layer selection remain outside the established default entrypoint.

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
├── STORY_PLAYER.md
├── TELEMETRY.md
├── TRUST_BADGES.md
└── map-context-evidence-drawer-admission.md
```

Some sibling documents retain old proposed filenames, placeholder owners, or pre-implementation assumptions. Their presence is confirmed; their currentness and authority must be evaluated independently.

[Back to top](#top)

---

## 9 · Sibling documents

| Document | Primary concern | Safe reading posture |
|---|---|---|
| [`ACCESSIBILITY.md`](./ACCESSIBILITY.md) | Keyboard, focus, semantics, alternatives, motion, and accessible trust states | Architecture target; app-wide conformance is not established |
| [`BOUNDARIES.md`](./BOUNDARIES.md) | Browser authority and forbidden operations | Trust-boundary guidance; reconcile with current code and ADRs |
| [`COMPARE_AND_EXPORT.md`](./COMPARE_AND_EXPORT.md) | Comparison and export behavior | Proposed surface; release/citation preservation remains mandatory |
| [`CONTINUITY_NOTES.md`](./CONTINUITY_NOTES.md) | Lineage, supersession, and redesign continuity | Historical/architecture aid, not decision authority |
| [`EVIDENCE_DRAWER.md`](./EVIDENCE_DRAWER.md) | Evidence inspection surface | Architecture guide; a bounded fixture implementation exists |
| [`FOCUS_FLOW.md`](./FOCUS_FLOW.md) | Governed Focus Mode user flow | Proposed composition; no direct model-client path |
| [`GOVERNED_SHELL.md`](./GOVERNED_SHELL.md) | Persistent shell composition | Proposed architecture; default entrypoint is much smaller |
| [`LAYERING.md`](./LAYERING.md) | Layer catalog, manifests, legends, and UI layering | Proposed architecture; released-layer runtime not established |
| [`MAP_RUNTIME_BOUNDARY.md`](./MAP_RUNTIME_BOUNDARY.md) | Renderer-neutral port and MapLibre adapter seam | Proposed decision surface; adapter remains comment-only |
| [`STORY_PLAYER.md`](./STORY_PLAYER.md) | Story playback and continuity | Proposed surface; stories remain downstream carriers |
| [`TELEMETRY.md`](./TELEMETRY.md) | Safe UI observability | Must exclude raw evidence, prompts, secrets, and restricted coordinates |
| [`TRUST_BADGES.md`](./TRUST_BADGES.md) | Trust-state projection | Badges summarize governed state; they do not create it |
| [`map-context-evidence-drawer-admission.md`](./map-context-evidence-drawer-admission.md) | Map-context admission to evidence inspection | Bounded seam note; verify against current implementation |

This README is the navigation and reconciliation surface. It does not silently promote any sibling from draft or proposal to accepted architecture.

[Back to top](#top)

---

## 10 · UI component families

| Component family | Intended responsibility | Current evidence |
|---|---|---|
| Shell | Persistent frame, headings, trust status, route/panel composition | Bounded static entrypoint with fixed fail-closed outcome |
| Evidence Drawer | Resolve governed projections into inspectable finite states | Implemented fixture parser/view model and keyboard-operable DOM projection |
| Governed client | Validate external payloads at the browser boundary | Strict app-local fixture projection parser exists; live transport is not wired |
| Map runtime | Render released layers and emit candidate selections through a KFM-owned seam | `MapLibreAdapter.ts` is comment-only; no renderer dependency |
| Layer catalog and badges | Project release, evidence, time, policy, review, correction, and representation state | Architecture documents exist; live composition is not established |
| Focus Mode | Send bounded requests through the governed AI/API boundary and render finite outcomes | Architecture and fixtures exist in the repository; live composition is not established here |
| Story player | Play released, cited narrative steps without becoming evidence authority | Architecture document exists; implementation maturity needs verification |
| Compare/export | Preserve scope, release identity, citation, and correction state in comparisons and exports | Architecture document exists; implementation maturity needs verification |
| Review surface | Show steward-oriented state without exposing privileged controls through the public shell | Separate app/feature lanes exist; authorization and deployment remain unverified |
| Telemetry/diagnostics | Report safe operational state without leaking protected content | Policy/docs exist; deployed telemetry behavior is unknown |

[Back to top](#top)

---

## 11 · Routes

No production route tree is confirmed by the current default Explorer entrypoint. This README therefore does not assign authoritative URL paths.

Any future route design must preserve these invariants:

1. the map-first shell remains a composition surface, not a truth store;
2. route changes do not silently discard time, selection, evidence, release, or correction context;
3. deep links carry safe public identifiers, not raw evidence or restricted geometry;
4. unavailable or denied state is rendered explicitly rather than replaced by guessed content;
5. privileged review or administration is separated from ordinary public navigation;
6. route names and ownership are verified in implementation and documented in one route authority before use.

Route families such as explore, evidence, focus, story, compare, export, settings, diagnostics, and read-only review remain descriptive architecture terms until implementation and tests establish exact paths.

[Back to top](#top)

---

## 12 · Finite outcomes

The public UI outcome vocabulary is:

| Outcome | UI meaning | Disclosure rule |
|---|---|---|
| `ANSWER` | Released, policy-safe, citation-capable support is available for the bounded request | Show evidence references, citations, limitations, and trust state |
| `ABSTAIN` | Support is missing, stale, unresolved, superseded, out of scope, or otherwise insufficient | Explain the bounded reason; do not manufacture a claim |
| `DENY` | Policy, rights, sensitivity, access, or safety blocks disclosure | Use fixed no-leak copy; do not expose protected reason details |
| `ERROR` | A validator, resolver, transport, policy engine, or runtime failed | Fail closed; do not downgrade the failure into an answer |

`HOLD`, `PASS`, and `FAIL` may describe review or validation state. They are not substitutes for the public response outcomes above.

The current shell establishes `ABSTAIN` and `ERROR` baseline states. The fixture-driven Evidence Drawer can project all four public outcomes from its strict local profile; that does not prove live governed transport.

[Back to top](#top)

---

## 13 · Trust membrane

The UI must preserve all of these boundaries:

- ordinary browser code reads governed interfaces or released public-safe carriers, not canonical/internal stores;
- `EvidenceRef` resolves to admissible `EvidenceBundle` support before a consequential claim is presented as authoritative;
- map pixels, tile properties, feature-state, camera state, and clicks are candidates or visual context, not evidence;
- policy, rights, sensitivity, review, and release decisions remain upstream;
- direct model-runtime calls from the browser are denied;
- negative outcomes use fixed, non-reflective copy and do not echo protected upstream content;
- corrections, supersessions, withdrawals, and release identity remain visible where material;
- UI telemetry excludes raw evidence, prompts, secrets, exact restricted locations, and protected policy reasons;
- exports preserve the evidence/release context needed to inspect what was shown.

Current enforcement is partial: the repository has strict fixture parsing, no-leak negative projections, an import/path boundary test, and app-local tests. Complete network, information-flow, CSP, deployment, renderer, and runtime-policy enforcement is not established.

[Back to top](#top)

---

## 14 · Layer trust badges

A trust badge is a projection of governed state, not proof by itself.

Where applicable, a layer or claim-bearing UI surface should expose:

- source role;
- observed, valid, source, retrieval, release, and correction time as applicable;
- freshness or stale state;
- policy/access outcome;
- review state;
- release state and release identifier;
- evidence resolution and citation state;
- correction, supersession, withdrawal, or rollback state;
- representation limits, including generalized or derived geometry where material.

The current Evidence Drawer view model already projects source role, policy, review, release, freshness, correction, evidence references, citations, limitations, and history labels. A map-layer badge system is not established by the default entrypoint.

Badges must never:

- imply an accepted ADR where none exists;
- turn a successful test into publication;
- expose restricted reason text;
- rely on color alone;
- hide stale, denied, corrected, or superseded state.

[Back to top](#top)

---

## 15 · Accessibility expectations

### Confirmed bounded behavior

The current Evidence Drawer implementation provides:

- a native button to open the drawer;
- labeled `main` and complementary landmarks in the tested shell;
- focus movement to the close control;
- Escape-to-close behavior;
- focus return to the opener;
- text labels for outcomes and trust state;
- fixed no-leak denied/error projections.

### Required architecture posture

A mature UI should also demonstrate, through representative automated and manual evidence:

- complete keyboard operation and visible focus;
- stable heading and landmark hierarchy;
- accessible names, descriptions, and status announcements;
- text/icon alternatives to color, shape, motion, and map-only encoding;
- reduced-motion and zoom/reflow support;
- screen-reader-accessible evidence, citations, tables, timelines, legends, and controls;
- non-map alternatives for consequential information;
- safe focus behavior during route, drawer, modal, error, and correction-state changes.

Repository tests prove only their bounded fixtures. They do not establish whole-app WCAG conformance, assistive-technology parity, or production accessibility.

[Back to top](#top)

---

## 16 · Validation

### Focused repository-native checks

A UI architecture or implementation change should run the smallest applicable set:

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  docs/architecture/ui/README.md \
  --repo-root . \
  --profile required

pnpm --dir apps/explorer-web build
pnpm --dir apps/explorer-web test:unit
pnpm --dir apps/explorer-web test:browser

python -m pytest -q tests/policy/test_explorer_web_adapter_boundary.py
```

Additional documentation link, anchor, metadata, staleness, and graph checks should run through the repository's configured docs workflows when the changed area participates in them.

### Acceptance matrix

| Change type | Minimum evidence |
|---|---|
| README-only reconciliation | Metadata, link/anchor, Markdown structure, stale-claim, and changed-file review |
| UI view-model change | Unit tests for `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, malformed input, and no-leak behavior |
| Browser interaction change | Playwright coverage for keyboard, focus, landmarks, and negative-state disclosure |
| Governed transport change | Contract/schema compatibility, fixture tests, no direct-store access, transport failure tests, and audit-safe telemetry |
| Map runtime change | Accepted package/seam decision, pinned dependency, import/acquisition enforcement, browser probes, performance budgets, and rollback |
| Export or public release change | Evidence, rights, sensitivity, release manifest, correction, cache invalidation, and rollback evidence |

A green workflow is validation evidence only. It is not review, release, deployment, or publication authority.

[Back to top](#top)

---

## 17 · Inputs

### Current implemented input boundary

- the baseline shell accepts no input;
- supplying input to the baseline shell produces fixed `ERROR / UNSUPPORTED_BASELINE_INPUT`;
- the Evidence Drawer accepts a strict app-local fixture projection;
- malformed projections fail to fixed `ERROR`;
- denied and error paths do not reflect protected upstream text.

### Intended governed inputs

Future UI composition may consume only validated, policy-safe forms such as:

- finite governed response envelopes;
- released layer/style/tile manifests and public-safe carriers;
- Evidence Drawer projections derived from resolved evidence;
- bounded Focus responses;
- release, freshness, review, correction, and representation state;
- safe public identifiers, viewport/time context, and candidate selections.

The UI must not accept raw source bytes, arbitrary model output, canonical store records, policy internals, secrets, or restricted exact geometry as ordinary client input.

[Back to top](#top)

---

## 18 · Outputs

Permitted UI outputs include:

- finite view states;
- accessible evidence and citation displays;
- map-selection candidates for governed resolution;
- safe filter, camera, layer, and time-state changes;
- bounded Focus requests and responses;
- comparisons and exports that preserve release/citation/correction context;
- privacy-safe operational telemetry;
- correction and stale-state notices.

The UI does not emit:

- source admission decisions;
- canonical evidence;
- policy approval;
- review approval;
- promotion or release decisions;
- publication state;
- proof closure;
- hidden reasoning as evidence;
- unreviewed sensitive-location transforms.

A screenshot, story, map state, badge, or export is a downstream carrier and must not be represented as sovereign truth.

[Back to top](#top)

---

## 19 · Review burden

| Concern | Required review perspective |
|---|---|
| Architecture and responsibility boundaries | Architecture/UI maintainer |
| Governed transport and runtime envelope | Governed API and contract/schema maintainer |
| Evidence and citation projection | Evidence maintainer |
| Rights, sensitivity, access, and negative-state copy | Policy/privacy/sensitivity reviewer |
| Renderer and dependency seam | Map/runtime and supply-chain reviewer |
| Keyboard, screen-reader, and non-map parity | Accessibility reviewer |
| Release, correction, export, and rollback | Release/correction reviewer |
| Documentation accuracy and links | Docs maintainer |

CODEOWNERS currently routes the repository and relevant roots to `@bartytime4life`. That is a confirmed GitHub review route, not proof that the independent roles above are assigned or that separation of duties is enforced.

Material changes to an ADR, contract, schema, policy, release rule, or responsibility boundary belong in their owning surface and may require a separate pull request. This README must not accept its own proposals.

[Back to top](#top)

---

## 20 · Related folders

| Path | Relationship |
|---|---|
| [`apps/explorer-web/`](../../../apps/explorer-web/) | Current deployable Explorer baseline |
| [`apps/governed-api/`](../../../apps/governed-api/) | Intended trust-bearing dynamic interface |
| [`apps/review-console/`](../../../apps/review-console/) | Separate steward/review application lane |
| [`packages/ui/`](../../../packages/ui/) | Current shared-UI placeholder package |
| [`packages/maplibre/`](../../../packages/maplibre/) | Current renderer placeholder package |
| [`contracts/`](../../../contracts/) | Semantic contracts |
| [`schemas/`](../../../schemas/) | Machine validation shapes |
| [`policy/ui/`](../../../policy/ui/) | UI policy orientation |
| [`tests/`](../../../tests/) | Cross-root executable tests |
| [`fixtures/`](../../../fixtures/) | Positive/negative fixture families |
| [`release/`](../../../release/) | Release, correction, and rollback control |
| [`docs/architecture/governed-ai/`](../governed-ai/) | Governed AI and Focus architecture |
| [`docs/architecture/story/`](../story/) | Story architecture |
| [`docs/architecture/review/`](../review/) | Review architecture |
| [`docs/runbooks/`](../../runbooks/) | Operational procedures |

Compatibility roots such as `ui/`, `web/`, `styles/`, and `viewer_templates/` must not become parallel canonical shell or architecture authorities without an accepted migration decision.

[Back to top](#top)

---

## 21 · ADRs that govern this folder

The table separates accepted placement authority from proposed UI decisions.

| ADR | Effective status at snapshot | Relevance |
|---|---|---|
| [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **accepted** | Adopts Directory Rules v2 and establishes responsibility-root placement law |
| [`ADR-0004`](../../adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md) | proposed | Governed API as the trust membrane |
| [`ADR-0005`](../../adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md) | proposed | Explorer Web as the canonical map-first shell |
| [`ADR-0006`](../../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) | proposed | One MapLibre acquisition/import seam |
| [`ADR-0007`](<../../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>) | proposed | Sole browser-renderer family and exception governance |
| [`ADR-0019`](../../adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md) | proposed | Governed AI adapter and finite envelopes |
| [`ADR-0020`](../../adr/ADR-0020-abstain-is-a-first-class-decision.md) | proposed | First-class abstention |
| [`ADR-0025`](../../adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md) | proposed | Public-client store boundary |

Until a decision is accepted, implementation and documentation may prepare, test, or describe the proposal but must not label it binding.

[Back to top](#top)

---

## 22 · FAQ

### Is this README canonical UI decision authority?

No. It is the architecture-lane landing page. Accepted ADRs, adopted Directory Rules, contracts, schemas, policy, and current implementation evidence control their respective questions.

### Is `apps/explorer-web/` implemented?

A bounded fail-closed baseline is implemented and testable. A functional governed map product, live transport, renderer, released-layer flow, deployment, and public operation are not established.

### Is MapLibre currently running in Explorer?

No current repository evidence establishes that. Explorer declares no MapLibre dependency, `packages/maplibre/` exports a placeholder, and `MapLibreAdapter.ts` is comment-only.

### Does the repository use `packages/maplibre-runtime/`?

Not at the checked snapshot. Older planning material proposed that name; the repository-present lane is `packages/maplibre/`. Do not create parallel active packages without a governed migration decision.

### May the UI read `data/published/` directly because the content is public-safe?

Not as an assumed normal path. Public clients use governed interfaces or released carriers with verified integrity and release context. Direct filesystem or canonical-store access is not a browser authority shortcut.

### Does a trust badge prove evidence or release?

No. It summarizes upstream governed state. The underlying evidence, policy, review, release, and correction records remain authoritative.

### Can a model answer be rendered when citations are unavailable?

No consequential answer should be shown as authoritative. The UI returns `ABSTAIN`, `DENY`, or `ERROR` according to the finite outcome and policy state.

### Does a passing UI workflow publish KFM?

No. Tests, workflows, commits, pull requests, merges, builds, and deployments are not publication decisions.

[Back to top](#top)

---

## 23 · Open questions and verification backlog

### Decision and authority

- **NEEDS VERIFICATION:** acceptance or supersession state of each proposed UI ADR after the pinned snapshot.
- **NEEDS VERIFICATION:** independently assigned UI, API, map-runtime, accessibility, policy, and release stewards.
- **NEEDS VERIFICATION:** whether any sibling architecture document should be superseded, narrowed, or corrected after current implementation review.

### Contracts and implementation

- **OPEN:** resolve the physical and semantic `MapRuntimePort` / `MapLibreAdapter` home without creating a second active package.
- **OPEN:** establish one accepted runtime response contract shared by Governed API and Explorer.
- **OPEN:** wire live governed transport while preserving strict finite outcomes and no-leak behavior.
- **OPEN:** compose a released-layer map-selection flow through evidence resolution.
- **OPEN:** define and test route/state continuity for map, time, selection, evidence, Focus, story, compare, export, settings, and diagnostics.
- **OPEN:** establish a real shared API for `packages/ui/` or keep it explicitly placeholder until needed.

### Security, accessibility, and operations

- **NEEDS VERIFICATION:** authentication, authorization, CSP, CORS, cache, worker, protocol, and supply-chain posture.
- **NEEDS VERIFICATION:** whole-app keyboard, screen-reader, reflow, reduced-motion, and non-map parity.
- **NEEDS VERIFICATION:** deployed telemetry redaction, retention, sampling, incident response, and no-raw-evidence guarantees.
- **NEEDS VERIFICATION:** exact-head hosted UI and documentation checks for the current change.
- **UNKNOWN:** production deployment, service health, browser matrix, public traffic, and operational release state.

Open items should be resolved in the owning ADR, contract, schema, policy, code, test, runbook, or register. This README may link to those decisions; it must not silently close them.

[Back to top](#top)

---

## Appendix A · No-loss modernization ledger

| Prior material | v3-draft treatment |
|---|---|
| Map-first, time-aware, evidence-bounded UI purpose | **Retained** |
| Cite-or-abstain, finite outcomes, no direct stores, no direct model client | **Retained and tied to current evidence** |
| Twenty-three numbered section anchors | **Retained** |
| UI sibling navigation | **Corrected to repository-present filenames** |
| Placeholder owners and dates | **Replaced with verified CODEOWNERS route and repository-history date** |
| Claim that this README is canonical decision authority | **Narrowed** to architecture landing-page authority |
| `docs/architecture/maplibre-3d.md` as upstream authority | **Removed** because the path is absent at the checked snapshot |
| `packages/maplibre-runtime/` as current implementation home | **Removed**; repository-present `packages/maplibre/` is documented as a placeholder |
| MapLibre GL JS `5.x` and named plugin set as implemented | **Removed**; renderer decision and dependency admission remain proposed/held |
| Cesium retirement as resolved | **Removed**; renderer-family choice remains proposed |
| Proposed exact route and schema trees | **Narrowed** to responsibility boundaries and open verification work |
| Accessibility, telemetry, export, correction, rollback, and review expectations | **Retained with explicit maturity limits** |
| Release, deployment, publication, or settings changes | **None** |

### Rollback

The documentation rollback target is prior blob `96a5dcc44ecb652c27e7f1e75e9634488d9aa9d0`. Reverting the update restores the previous README. No code, schema, contract, policy, fixture, workflow, receipt, proof, release, runtime, deployment, or public state requires rollback.

---

**Last reviewed:** `2026-08-14` against `main@3974da9794fa11bd5355c49243c9193d22b9e81e`
**Truth posture:** CONFIRMED repository evidence / PROPOSED architecture / UNKNOWN deployed behavior

[Back to top](#top)
