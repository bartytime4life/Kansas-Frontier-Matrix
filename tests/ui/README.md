# `tests/ui/` — Governed UI Trust-State Test Boundary

> Repository-grounded test boundary for proving that KFM user interfaces preserve governed evidence, policy, release, review, correction, rollback, time, sensitivity, and finite-outcome state without turning rendered pixels, browser state, component success, accessibility checks, or visual snapshots into truth or publication authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-ui-readme
title: tests/ui/README.md — Governed UI Trust-State Test Boundary
type: readme; directory-readme; ui-test-parent; trust-surface-enforceability-boundary
version: v0.2
status: draft; repository-grounded; readme-only-direct-lane; no-dedicated-ui-suite-established; static-boundary-guard-confirmed; explorer-and-shared-ui-placeholder-heavy; ui-and-accessibility-ci-stubs
owners: OWNER_TBD — QA steward · UI steward · Explorer Web steward · Shared UI package steward · Accessibility steward · Evidence steward · Policy steward · Sensitivity and rights stewards · Release steward · Map steward · Runtime steward · Security reviewer · CI steward · Docs steward
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1
policy_label: public-doctrine; tests; ui; trust-visible; map-first; governed-payloads-only; no-network-default; synthetic-only; accessibility-required; no-sensitive-leakage; correction-aware; rollback-aware; no-publication
current_path: tests/ui/README.md
truth_posture: CONFIRMED target README, Directory Rules, canonical tests root, UI semantic-contract README, packages/ui README and source README, Explorer Web README and source README, Explorer Web package metadata with TODO dev/build/test scripts, packages/ui package metadata without scripts, placeholder Evidence Drawer/Focus Panel/Trust Header feature entrypoints, placeholder packages/ui source entrypoint, tests/fixtures/ui README, checked absence of representative UI fixture payloads, executable Explorer Web adapter/internal-store policy guard, Makefile test collection limited to tests/schemas plus tests/contracts and TODO ui-build target, TODO-only ui-build and accessibility workflows, and checked absence of tests/ui/conftest.py, tests/ui/test_ui.py, and tests/ui/pytest.ini / PROPOSED shared UI trust-state case contract, component and app test routing, finite-outcome rendering matrix, evidence/citation display tests, release and temporal state tests, keyboard/focus/screen-reader/reduced-motion tests, sensitive-value leakage canaries, deterministic browser harness, network interception, snapshot governance, zero-collection failure, substantive CI, and promotion blocking / CONFLICTED centralized tests/ui ownership versus package-local and app-local component tests; tests/fixtures/ui proposed payload inventory versus checked absent representative files; UI architecture and README depth versus placeholder implementation and TODO scripts / UNKNOWN exhaustive UI source and test inventory, dynamic collection, accepted framework and runner, implemented component families, route inventory, browser harness, fixture consumers, accessibility baseline, visual-regression system, current pass rates, coverage, runtime, flake rate, deployment use, and promotion dependency / NEEDS VERIFICATION owners, lane-retention rule, package-local versus root test placement, accepted UI payload contracts and schemas, accessible-state vocabulary, screenshot/artifact retention, no-network mechanism, sensitive-fixture review, CI ownership, route and component graduation, correction propagation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: b902a5c34165ac55d2bb46b470f21e4002cf505f
  target_prior_blob: 4dbbea201819d91d95fc27dcdada0e2ff756d293
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    tests_root_readme: 5614de99433bca29d6a03d665fb4e00ec23eb5fb
    ui_contracts_readme: ddd14b5f86bc0273cf7d1b585908278cae9e1711
    packages_ui_readme: 832df71dbbf12e138ab5e4a7ea272e54cdc7b871
    packages_ui_source_readme: 55c1365c71a578f8a0b1e0d42e40896bedac083a
    packages_ui_package_json: 9e165aa0b09846cc6d242c1f777f67047ba146c1
    packages_ui_source_placeholder: 2c9ea341d61bf4d1733b9982fda8a9b869a3a720
    explorer_web_readme: 755dae3e175b103702caba573a5171d62ed710da
    explorer_web_source_readme: 770cace029d0b9016ec7bd1c2d879b1bb49c896a
    explorer_web_package_json: ce981192e725483c747affb45ca3de36a22ce9ce
    evidence_drawer_placeholder: 6438397db43b465a90fc9a33ac7c3d2f11406603
    focus_panel_placeholder: 73e8763e372009f8a537e596abc6755a90967c8f
    trust_header_placeholder: 2938d6ba019c0bebddd8c224d5a0decd2b7558eb
    ui_fixture_readme: 8d87d87b0d318e55518daba478962e092f523390
    explorer_web_boundary_test: 97d44069b0a5ab4a82b1e1fc48665e905c08a287
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
    ui_build_workflow: d73a43d72460b4105996615785bdf5aedba88a4c
    accessibility_workflow: 62ede945862baf6e9629a843d3c2a122b5912541
  direct_lane_files_confirmed:
    - tests/ui/README.md
  checked_absent_paths:
    - tests/ui/conftest.py
    - tests/ui/test_ui.py
    - tests/ui/pytest.ini
    - tests/fixtures/ui/evidence_drawer.valid.json
    - tests/fixtures/ui/focus_answer.valid.json
    - tests/fixtures/ui/policy_denied_banner.deny.json
    - apps/explorer-web/src/main.tsx
  bounded_inventory_note: repository search and representative path checks did not establish a dedicated executable suite under tests/ui or the proposed representative fixture payloads; this does not prove absence from history, ignored files, generated files, branch-local files, dynamically collected suites, package-local tests, app-local tests, external browser services, or uninspected paths
related:
  - ../README.md
  - ../policy/test_explorer_web_adapter_boundary.py
  - ../fixtures/ui/README.md
  - ../e2e/README.md
  - ../maplibre/README.md
  - ../api/README.md
  - ../release/README.md
  - ../../contracts/ui/README.md
  - ../../packages/ui/README.md
  - ../../packages/ui/src/README.md
  - ../../apps/explorer-web/README.md
  - ../../apps/explorer-web/src/README.md
  - ../../apps/governed-api/README.md
  - ../../schemas/contracts/v1/ui/
  - ../../policy/ui/
  - ../../release/
  - ../../docs/architecture/ui/README.md
  - ../../docs/architecture/ui/EVIDENCE_DRAWER.md
  - ../../docs/architecture/ui/FOCUS_FLOW.md
  - ../../docs/doctrine/directory-rules.md
  - ../../.github/workflows/ui-build.yml
  - ../../.github/workflows/accessibility.yml
  - ../../Makefile
notes:
  - "v0.2 replaces a planning-heavy proposed test tree with a commit-pinned current-state and routing boundary."
  - "The direct tests/ui lane is README-only at the bounded snapshot."
  - "Explorer Web and packages/ui metadata are scaffolded; representative UI feature and package entrypoints are placeholders."
  - "A static Explorer Web adapter/internal-store policy guard is confirmed, but it is not component, rendering, browser, accessibility, or non-vacuous source coverage."
  - "The current Makefile excludes tests/ui, and the UI-build and accessibility workflows execute TODO echo commands."
  - "This revision changes documentation only and creates no executable test, fixture, component, route, package export, schema, contract, policy, workflow behavior, data, receipt, proof, release object, screenshot, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<p>
  <img alt="Document status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Direct inventory: README only" src="https://img.shields.io/badge/direct__inventory-README__only-lightgrey">
  <img alt="UI suite: not established" src="https://img.shields.io/badge/UI__suite-not__established-orange">
  <img alt="Trust state: visible" src="https://img.shields.io/badge/trust__state-visible-blue">
  <img alt="Accessibility: required" src="https://img.shields.io/badge/accessibility-required-blueviolet">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Publication authority: denied" src="https://img.shields.io/badge/publication-DENIED-red">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Authority](#authority-boundary) · [Current state](#confirmed-current-state) · [Routing](#placement-and-routing-law) · [System under test](#ui-system-under-test) · [Case contract](#minimum-ui-test-case-contract) · [Governed payloads](#governed-payload-and-finite-outcome-contract) · [Evidence Drawer](#evidence-drawer-contract) · [Focus Mode](#focus-mode-contract) · [Map and time](#map-layer-time-and-selection-contract) · [Trust state](#trust-release-review-and-correction-state) · [Accessibility](#accessibility-and-inclusive-interaction-contract) · [Sensitive values](#sensitive-data-redaction-and-no-leak-contract) · [Loading and errors](#loading-empty-error-and-recovery-states) · [Determinism](#determinism-locale-time-and-replay) · [Security](#network-security-and-browser-side-effects) · [Fixtures](#fixtures-test-data-and-payload-boundary) · [Snapshots](#snapshots-visual-baselines-and-artifacts) · [Rollback](#correction-withdrawal-supersession-and-rollback) · [Outcomes](#test-results-ui-states-runtime-outcomes-and-policy-decisions) · [Runner](#runner-ci-and-promotion-boundary) · [Migration](#migration-deprecation-and-rollback-of-this-lane) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Evidence snapshot:** `main@b902a5c34165ac55d2bb46b470f21e4002cf505f`
> **Prior target blob:** `4dbbea201819d91d95fc27dcdada0e2ff756d293`
> **Direct lane:** `tests/ui/README.md` only at the bounded snapshot
> **Checked absent:** direct harness/test/config, representative fixture payloads, and `apps/explorer-web/src/main.tsx`
> **Makefile:** `make test` runs `tests/schemas` and `tests/contracts`, not this lane
> **Explorer scripts:** `dev`, `build`, and `test` all echo `TODO`
> **UI/accessibility workflows:** checkout plus TODO echo steps

`tests/ui/` is currently a documented UI-test boundary, not an established executable component, browser, accessibility, or visual-regression suite.

### Safe conclusions

- **CONFIRMED:** the direct README exists.
- **CONFIRMED:** the canonical tests root assigns UI trust-state component testing to this lane.
- **CONFIRMED:** UI semantic contracts exist as draft/proposed documentation and define a downstream trust surface.
- **CONFIRMED:** `packages/ui/` and `apps/explorer-web/` are the intended shared-component and deployable-shell homes.
- **CONFIRMED:** Explorer Web package scripts are TODO-only.
- **CONFIRMED:** the shared UI package manifest has no test, build, story, type-check, or accessibility scripts.
- **CONFIRMED:** sampled Evidence Drawer, Focus Panel, Trust Header, and shared UI entrypoints are explicit greenfield placeholders.
- **CONFIRMED:** representative UI fixture payloads named by the fixture README were not found at checked paths.
- **CONFIRMED:** a static policy test checks renderer-import placement and forbidden internal-store literals under Explorer Web source.
- **CONFIRMED:** that static test does not render components, launch a browser, exercise keyboard navigation, validate ARIA behavior, inspect screenshots, or prove non-vacuous source coverage.
- **CONFIRMED:** the Makefile default test target excludes `tests/ui`.
- **CONFIRMED:** `ui-build` and `accessibility` workflows are TODO-only scaffolds.
- **UNKNOWN:** complete source inventory, route implementation, dynamic tests, actual browser tooling, current pass rate, coverage, runtime, flake rate, visual baselines, accessibility baseline, deployment, and release-gate dependency.
- **NEEDS VERIFICATION:** the accepted split among this root lane, package-local tests, app-local tests, E2E tests, policy guards, and map-renderer tests.

### Maturity matrix

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Parent README | `CONFIRMED` | A UI-test boundary exists. |
| Direct executable test | `NOT ESTABLISHED` | No representative direct module was found. |
| Lane harness/config | `NOT FOUND AT CHECKED PATHS` | No independent collection contract is established. |
| UI fixtures | `README CONFIRMED; REPRESENTATIVE PAYLOADS ABSENT` | Fixture intent exists; payload coverage does not. |
| Shared UI implementation | `PLACEHOLDER-HEAVY` | Package/source READMEs exist; sampled entrypoint is a placeholder. |
| Explorer Web implementation | `PLACEHOLDER-HEAVY` | App/source READMEs exist; sampled features are placeholders. |
| Static UI boundary guard | `CONFIRMED EXECUTABLE` | Selected import and literal boundaries are checked. |
| Component rendering tests | `NOT ESTABLISHED` | No component harness or renderer was verified. |
| Browser/E2E UI tests | `NOT ESTABLISHED` | No browser runner was verified for this lane. |
| Accessibility tests | `NOT ESTABLISHED` | Workflow jobs echo TODO. |
| Visual regression | `NOT ESTABLISHED` | No accepted baseline tool or artifact policy was verified. |
| Default Makefile collection | `NOT ESTABLISHED` | Current target excludes this lane. |
| Dedicated substantive CI | `NOT ESTABLISHED` | UI workflows do not build or test. |
| Current metrics | `UNKNOWN` | No dedicated report was verified. |
| Promotion blocking | `UNKNOWN` | No verified promotion dependency targets this lane. |

### Truth labels

| Label | Meaning in this README |
|---|---|
| `CONFIRMED` | Verified from current repository files, executable code, workflows, or checked paths. |
| `PROPOSED` | A test contract, path, state, or procedure not established in implementation. |
| `CONFLICTED` | Current structure exposes competing ownership or naming choices. |
| `UNKNOWN` | Not established by inspected code, tests, CI, runtime, or release evidence. |
| `NEEDS VERIFICATION` | Checkable, but unresolved strongly enough to act as fact. |
| `DENY` | Disallowed because it bypasses governance, leaks protected state, or creates parallel authority. |

[Back to top](#top)

---

## Purpose

`tests/ui/` is the parent boundary for **shared, cross-cutting UI trust-state enforceability** when the assertion does not belong more precisely beside a package, app, policy, renderer, API, E2E flow, or domain.

A mature UI test proves that a governed payload is rendered without losing or inventing trust state:

```text
released or bounded-safe input
  -> governed API / accepted fixture envelope
  -> schema and semantic checks
  -> policy, evidence, citation, review, release, and time state
  -> UI component or route
  -> accessible trust-visible output
  -> protected values remain absent
  -> correction / withdrawal / rollback remains visible
  -> finite test result
```

A passing UI test may prove the scoped rendering or interaction behaved as expected. It does **not** prove:

- an upstream claim is true;
- an EvidenceBundle is complete merely because a drawer rendered;
- policy allowed a use merely because a component displayed it;
- material was released merely because a badge says “released”;
- a map feature is authoritative because it was selectable;
- a generated explanation is evidence;
- accessibility conformance beyond the exercised rules;
- browser behavior in untested engines or assistive technologies;
- deployment or production behavior;
- publication occurred.

The test target is the **trust-preserving presentation behavior**, not the truth itself.

[Back to top](#top)

---

## Authority boundary

### Directory Rules basis

KFM places files by primary responsibility:

```text
tests/                    authored enforceability proof
apps/explorer-web/        deployable map-first public/semi-public shell
packages/ui/              shared reusable UI implementation
contracts/ui/             UI payload and state meaning
schemas/contracts/v1/ui/  machine shape
policy/                    admissibility, rights, sensitivity, access
apps/governed-api/         normal public trust-membrane API
packages/maplibre/         browser map-renderer boundary
fixtures/                  reusable synthetic examples
tests/fixtures/            test-local synthetic examples
release/                   release, correction, withdrawal, rollback
data/                      governed lifecycle records and artifacts
```

| Responsibility | Authority home | This lane's role |
|---|---|---|
| Shared UI trust-state assertions | `tests/ui/` after placement review | May own genuinely cross-cutting authored tests. |
| Shared component implementation | `packages/ui/` | Tested, not implemented here. |
| Explorer shell/routes | `apps/explorer-web/` | Tested, not implemented here. |
| Governed API envelopes | `apps/governed-api/`, runtime/UI contracts | Consumed, not created here. |
| UI object meaning | `contracts/ui/` and accepted related contracts | Verified, not rewritten here. |
| UI machine shape | `schemas/contracts/v1/ui/` and accepted object homes | Validated, not defined here. |
| Policy and sensitivity | `policy/` | Exercised, not invented here. |
| Evidence and citations | evidence contracts and governed proof roots | Projected, not authored here. |
| Map rendering | `packages/maplibre/` and accepted adapter homes | Tested through adapters, not owned here. |
| Test-local UI fixtures | `tests/fixtures/ui/` | Referenced, not duplicated here. |
| Shared UI fixtures | `fixtures/` | Referenced, not duplicated here. |
| Browser E2E | `tests/e2e/` or accepted app-local harness | Composed behavior, not automatically this lane. |
| Release and rollback | `release/` | Displayed and tested, never approved here. |
| Screenshots and reports | ephemeral CI or accepted governed artifact lane | Generated output, never source truth. |

### Anti-collapse rules

This lane must not collapse:

```text
rendered text                  -> factual truth
visible citation               -> citation validity
visible EvidenceRef            -> EvidenceBundle closure
policy badge                   -> policy execution
release badge                  -> ReleaseManifest approval
map selection                  -> canonical feature identity
successful component render    -> route or app readiness
static grep                    -> complete UI safety
axe scan                        -> full accessibility conformance
snapshot match                 -> semantic correctness
visual similarity              -> trust-state correctness
green TODO workflow            -> UI coverage
zero collected tests           -> success
placeholder component          -> implementation
README test matrix             -> executable proof
```

[Back to top](#top)

---

## Confirmed current state

### Direct lane

The bounded direct inventory establishes:

```text
tests/ui/
└── README.md
```

Checked paths not found:

```text
tests/ui/conftest.py
tests/ui/test_ui.py
tests/ui/pytest.ini
```

This is a bounded result. It does not establish exhaustive absence from history, ignored files, generated workspaces, external services, dynamic collection, package-local tests, app-local tests, or uninspected branches.

### Fixture companion

`tests/fixtures/ui/README.md` exists and proposes UI fixture families. Representative proposed payloads were not found at the checked paths:

```text
tests/fixtures/ui/evidence_drawer.valid.json
tests/fixtures/ui/focus_answer.valid.json
tests/fixtures/ui/policy_denied_banner.deny.json
```

A fixture README is not fixture coverage.

### Explorer Web

The Explorer Web package manifest confirms a private `0.0.0` scaffold whose scripts are:

```json
{
  "dev": "echo TODO",
  "build": "echo TODO",
  "test": "echo TODO"
}
```

Sampled feature entrypoints are explicit placeholders:

```text
apps/explorer-web/src/features/evidence_drawer/index.tsx
apps/explorer-web/src/features/focus_panel/index.tsx
apps/explorer-web/src/features/trust_header/index.tsx
```

`apps/explorer-web/src/main.tsx` was not found at the checked path.

### Shared UI package

`packages/ui/package.json` identifies a private `@kfm/ui` `0.0.0` package but declares no scripts. `packages/ui/src/index.ts` is a greenfield placeholder.

### Confirmed static guard

`tests/policy/test_explorer_web_adapter_boundary.py` performs two static checks:

1. MapLibre/Cesium imports in inspected Explorer source files must remain inside the adapter directory.
2. Explorer source files must not contain configured internal-store path literals.

This is useful boundary evidence. It is not proof of:

- source-file existence;
- a nonempty inspected file set;
- runtime import behavior;
- network behavior;
- component rendering;
- governed API use;
- Evidence Drawer behavior;
- Focus Mode behavior;
- keyboard interaction;
- accessible names;
- focus management;
- screen-reader announcements;
- sensitive-value non-leakage;
- release/correction visibility;
- browser compatibility.

A future guard should explicitly assert a nonempty expected source inventory or target manifest before its result becomes trust-bearing.

### Workflow and runner state

- `make test` runs only schema and contract tests.
- `make ui-build` echoes a TODO command.
- `ui-build` workflow jobs echo TODO build/test commands.
- `accessibility` workflow jobs echo TODO axe/keyboard commands.

A green result from those jobs is workflow execution evidence, not UI or accessibility proof.

[Back to top](#top)

---

## Placement and routing law

Keep each test near the responsibility it primarily verifies.

| Primary assertion | Preferred home | Why |
|---|---|---|
| Shared component render behavior | Package-local tests beside `packages/ui/` | Package owns reusable component implementation. |
| Explorer route/shell behavior | App-local tests beside `apps/explorer-web/` | App owns route, shell, client, and page composition. |
| Neutral cross-cutting trust-state rendering | `tests/ui/` if accepted | Shared assertion spans more than one component/app. |
| Governed API envelope behavior | API tests or app-owned API tests | API owns the trust-membrane response. |
| Policy denial or internal-store boundary | `tests/policy/` | Policy/governance assertion owns the failure. |
| Map adapter and renderer behavior | MapLibre package/tests or accepted map lane | Renderer boundary owns camera/source/style behavior. |
| Full browser navigation | `tests/e2e/` | Composition across routes, API, map, and UI is end-to-end. |
| Accessibility of one component | Package/app test beside component | Failure is owned by the implementation. |
| Cross-app accessibility invariant | `tests/ui/` or dedicated accessibility lane after ADR | Shared invariant may justify neutral ownership. |
| Domain-specific display rule | `tests/domains/<domain>/` | Domain owns semantic/sensitivity context. |
| Snapshot/visual artifact generation | Test owner plus ephemeral CI artifact storage | Generated output stays out of authored-test authority. |
| Fixture payload | `tests/fixtures/ui/` or `fixtures/` | Fixtures are inputs, not tests. |

### Admission test for `tests/ui/`

A new executable file belongs directly here only when all are true:

1. the assertion is genuinely shared across more than one UI implementation owner;
2. no package, app, policy, renderer, E2E, or domain lane is more precise;
3. the UI object contract and system under test are named;
4. the runner and dependencies are accepted;
5. fixtures are synthetic and public-safe;
6. network and browser side effects are controlled;
7. positive and negative controls exist;
8. a responsible owner accepts maintenance;
9. CI collects the exact test;
10. migration and rollback are documented.

### Duplicate prohibition

Do not maintain the same assertion in multiple homes merely to increase apparent coverage. Choose one owner and make companion suites reference or compose it.

[Back to top](#top)

---

## UI system under test

Every test must identify the concrete system under test.

| System class | Examples | Required proof |
|---|---|---|
| Shared primitive | badge, banner, status label, caveat | Props-to-DOM behavior and accessibility. |
| Composite component | Evidence Drawer, layer card, correction panel | Governed payload rendering and interaction. |
| App route | Explore, Focus, Export, Diagnostics | Route loading, outcomes, policy, and release state. |
| Governed client adapter | API request/response validator | Invalid envelopes fail before render. |
| Map adapter | selection, viewport, layer state | Renderer remains subordinate and non-authoritative. |
| Browser flow | keyboard navigation, drawer focus, route change | User-observable composition. |
| Export/clipboard surface | citation copy, safe export | No protected or unreleased value escapes. |
| Static boundary guard | imports, path literals, forbidden APIs | Nonempty target inventory and explicit limitations. |

A test must not target only a README, proposed path, or placeholder export and then claim production UI behavior.

### Implementation maturity gate

Before a test is labeled as coverage for a component or route, verify:

- implementation file exists;
- export or route registration exists;
- package/app build resolves it;
- test imports the real implementation;
- fixture reaches the code path;
- assertions inspect user-visible and trust-bearing output;
- negative state is distinguishable;
- cleanup completes;
- CI runs it.

[Back to top](#top)

---

## Minimum UI test case contract

Every trust-bearing UI case should declare at least:

| Field | Required content |
|---|---|
| `case_id` | Stable deterministic identifier. |
| `owner` | Package, app, policy, E2E, map, or neutral UI owner. |
| `system_under_test` | Exact component, route, adapter, or flow. |
| `contract_ref` | Semantic contract or accepted behavior reference. |
| `schema_ref` | Payload shape when applicable. |
| `policy_ref` | Policy decision/obligation when material. |
| `release_ref` | Release/correction/rollback state when material. |
| `fixture_ref` | Synthetic input or local builder. |
| `audience` | Public, semi-public, steward, admin, or denied. |
| `runtime_outcome` | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` when applicable. |
| `ui_state` | Expected visible state and interaction posture. |
| `accessible_state` | Name, role, description, live-region, focus, keyboard expectations. |
| `must_render` | Required visible/semantic content. |
| `must_not_render` | Protected, unsupported, stale, or misleading content. |
| `network_posture` | Denied, mocked, or explicitly controlled. |
| `clock_locale` | Frozen time, timezone, locale, and formatting assumptions. |
| `side_effects` | Clipboard, storage, URL, download, focus, navigation, logging. |
| `cleanup` | DOM, mocks, timers, storage, downloads, and browser reset. |
| `rollback` | How the test or change is reverted. |

### Positive and negative controls

Every consequential denial, redaction, or abstention test should have a positive control proving the component is selective rather than permanently blocked.

Every positive trust-display test should have a negative companion proving missing or unsafe support does not silently render as normal truth.

### Required assertion layers

A complete case may need separate assertions for payload admission, semantic mapping, policy obligations, visible text, DOM semantics, accessible names, focus and keyboard behavior, protected-value absence, browser side effects, correction state, and deterministic cleanup.

[Back to top](#top)

---

## Governed payload and finite-outcome contract

Claim-bearing UI must consume an accepted governed envelope or a synthetic fixture that faithfully models one.

| Runtime outcome | UI obligation | Forbidden collapse |
|---|---|---|
| `ANSWER` | Render bounded answer plus evidence/citation/release context. | Do not imply more confidence or scope than the envelope. |
| `ABSTAIN` | Show insufficient-support state with safe next step. | Do not replace with generated filler or empty success. |
| `DENY` | Show safe denial without protected details. | Do not leak denied fields in DOM, labels, logs, or diagnostics. |
| `ERROR` | Show bounded failure and recovery posture. | Do not reinterpret as denial, abstention, or partial answer. |

The UI should fail closed when envelope versions or shapes are unsupported, outcomes are missing, required evidence refs are absent, policy obligations cannot be interpreted, release state is missing, time state is ambiguous, redaction metadata conflicts with values, or correction state conflicts with “current” labeling.

Direct model output must not be rendered as authoritative claim-bearing UI. It must enter through the governed runtime/API contract and remain subject to support, policy, and release controls.

[Back to top](#top)

---

## Evidence Drawer contract

Evidence Drawer tests should prove that support is inspectable without exposing internal or restricted material.

Required positive coverage includes bounded claim identity, allowed EvidenceRef/support summary, citation state, source roles, caveats, valid time/freshness, safe policy state, release/correction state, keyboard access, screen-reader access, and deterministic focus restoration.

Required negative coverage includes missing evidence, unresolved citations, restricted evidence metadata, stale support, withdrawn support, conflicting support, internal proof paths, and canonical identifiers.

The drawer is a governed projection. It does not become an EvidenceBundle, proof store, source registry, or correction authority.

[Back to top](#top)

---

## Focus Mode contract

Focus Mode tests should prove that a narrowed user question remains governed by map context, evidence, policy, time, release, and finite outcomes.

Required state includes bounded question/intent, explicit selection context, governed layer/feature refs, support for `ANSWER`, distinct `ABSTAIN`/`DENY`/`ERROR`, time caveats, preserved redaction, distinct loading/cancellation, correction state, and no hidden prompt or chain-of-thought exposure.

Negative cases should include no selection, unsupported selection type, missing evidence, denied detail, stale release, invalid context envelope, cancellation, timeout, conflicting evidence, unsupported locale/time, later correction, and release withdrawal.

Safe next steps must not encourage bypassing policy or accessing internal stores.

[Back to top](#top)

---

## Map, layer, time, and selection contract

The map is the interaction shell, not truth authority.

Tests should distinguish layer listed versus released, source configured versus admitted, tile loaded versus semantically valid, feature selected versus claim supported, style visible versus policy-allowed, viewport versus query scope, cache versus current release, and generalized versus exact geometry.

Where time matters, preserve valid time, observed time, issue time, source vintage, ingestion time, release time, correction time, stale state, timezone transitions, and unknown ranges. Do not collapse those into one generic date.

Selected objects must not expose exact sensitive locations, internal canonical IDs, private person/parcel joins, unreleased fields, credentials, hidden attributes, or restricted values through tooltips, accessible names, URLs, clipboard, exports, or diagnostics.

Renderer imports and calls remain inside accepted adapters. Static guards must assert a nonempty target inventory before becoming trust-bearing.

[Back to top](#top)

---

## Trust, release, review, and correction state

UI tests must make evidence, citation, policy, review, release, correction, source-role, freshness, and uncertainty state visible where material.

State must be expressed in text or semantic labels, not color alone. “Current” must not appear when release or correction state is unresolved. Withdrawn and superseded objects remain visibly non-current. Missing rollback support remains visible for consequential releases. Public audiences must not receive review-only details.

A badge is a projection of governed state. It does not create the state it labels.

[Back to top](#top)

---

## Accessibility and inclusive interaction contract

Accessibility is part of the trust membrane because hidden or inaccessible state can mislead users even when visible rendering looks correct.

Tests should verify semantic HTML, accessible names and descriptions, landmarks/headings, table relationships, meaningful control names, live-region behavior, error association, no inaccessible duplicate state, keyboard reachability, logical focus order, visible focus, drawer/modal focus restoration, safe Escape behavior, map keyboard escape, and understandable disabled/denied actions.

Evidence, policy, release, stale, corrected, withdrawn, and finite outcomes must never rely on color alone.

Reduced-motion preferences, announced loading, recoverable timeouts, and non-destructive auto-refresh should be tested where relevant.

Automated axe-style checks are useful but incomplete. Manual keyboard, focus, zoom, screen-reader, high-contrast, reduced-motion, and cognitive-clarity review remain necessary for consequential surfaces.

[Back to top](#top)

---

## Sensitive data, redaction, and no-leak contract

A correct denial can still fail if protected data remains in visible text, hidden DOM, ARIA labels, titles, data attributes, inputs, logs, request URLs/bodies, route state, browser history, storage, clipboard, downloads, screenshots, snapshots, source maps, telemetry, map properties, or caches.

Use synthetic, transformed, generalized, redacted, or denied fixtures for living-person data, DNA/genomic information, consent/revocation, archaeology, rare species, critical infrastructure, private land/person joins, restricted source detail, and emergency/security-sensitive state.

Sensitive tests should include unique synthetic canaries and assert their absence from every relevant leakage surface. Never use real sensitive values as canaries.

Public, semi-public, steward, admin, and restricted audiences require distinct assertions. CSS hiding is not access control.

[Back to top](#top)

---

## Loading, empty, error, and recovery states

Keep operational states distinct from governed outcomes:

| State | Meaning | Required display |
|---|---|---|
| loading | Work is pending. | Progress plus safe cancel/retry posture. |
| empty | Valid request returned no items. | Clear no-results state, not abstention. |
| `ABSTAIN` | Support is insufficient. | Support-limited explanation. |
| `DENY` | Policy/access blocks the request. | Safe denial without leak. |
| `ERROR` | The operation failed. | Bounded error and recovery. |
| offline | Network unavailable. | Offline posture; no stale truth upgrade. |
| stale cache | Cached state may be outdated. | Explicit stale label. |
| withdrawn | Previously released state is withdrawn. | Non-current warning and correction path. |

Retries must not duplicate side effects. Cancellation must not overwrite newer state. Stale responses must not replace current responses. Route changes must isolate pending work. Errors must not leak internals. Recovery must preserve focus and accessibility context.

[Back to top](#top)

---

## Determinism, locale, time, and replay

Default tests should control clock, timezone, locale, number/date formatting, random IDs, animation frames, timers, network responses, viewport, DPR, feature flags, storage, map camera, tile responses, reduced motion, and color scheme.

Given identical governed payload, audience, locale, time, viewport, and preferences, the UI should produce equivalent trust state and side effects.

Re-rendering unchanged state should not duplicate telemetry/downloads, refocus unexpectedly, reopen dismissed optional panels, reset map state, lose correction labels, or alter citation state.

[Back to top](#top)

---

## Network, security, and browser side effects

Default unit/component tests are no-network. Browser tests should intercept all requests and fail on undeclared destinations. Any allowed network behavior requires an explicit profile, local/mock allowlist, deterministic responses, no credentials, no production services, timeout/cancellation, redaction, cleanup, and rationale.

UI tests should fail on direct lifecycle/canonical/proof store access, local source files, secret-bearing configuration, unrestricted provider APIs, direct model endpoints, and unreleased object stores.

Each case must declare and clean URL/history, cookies, local/session storage, IndexedDB, service workers, caches, clipboard, downloads, permissions, analytics, window opening, and external navigation.

Security assertions should cover untrusted text, URL schemes/destinations, external link behavior, sanitized errors, audience-filtered diagnostics, safe exports, and fixture injection resistance.

[Back to top](#top)

---

## Fixtures, test data, and payload boundary

| Fixture class | Preferred home | Rule |
|---|---|---|
| Test-local UI payload | `tests/fixtures/ui/` | Small, synthetic, owned by specific tests. |
| Shared cross-suite payload | `fixtures/` | Reusable and explicitly governed. |
| Package-local builder | Package test support after approval | Must not become duplicate registry. |
| App-local route fixture | App test support after approval | Keep close to route owner. |
| Domain-sensitive UI fixture | Domain test/fixture lane | Preserve policy and sensitivity context. |

Consequential fixtures should identify object family/version, audience, outcome, evidence/citation, policy/sensitivity, release/review/correction, time state, redacted fields, expected visible state, forbidden canaries, consumers, owner, and review status.

Fixtures must not include real sensitive data, production exports, credentials, actual trust artifacts represented as authoritative, exact protected geometry, private model output, production logs, or hidden unsupported fields.

Shape and semantic intent must be validated separately. Schema-valid does not mean safe or admissible.

[Back to top](#top)

---

## Snapshots, visual baselines, and artifacts

Snapshots and screenshots are generated test artifacts, not authored truth.

Snapshot only stable semantic output, avoid whole-page snapshots when focused assertions are clearer, assert trust state explicitly, sanitize IDs/times/paths/URLs/canaries, review updates as behavior changes, pair snapshots with accessibility/no-leak assertions, and fail on empty collection.

Visual regression requires accepted browser/version, viewport/DPR, fonts, locale/timezone, motion settings, threshold, baseline owner, review process, storage/retention, sensitive-data scanning, correction, and rollback.

Generated reports, videos, traces, screenshots, and coverage should be ephemeral CI artifacts or use an accepted governed artifact lane. They do not belong under `tests/ui/` by default and do not establish release approval.

[Back to top](#top)

---

## Correction, withdrawal, supersession, and rollback

Tests should prove corrected claims replace display while preserving lineage, citations update with evidence, correction notices are accessible, exports use corrected state, and stale tabs discover invalidation.

Withdrawn material must not appear current; direct bookmarks and caches must fail safely; protected withdrawal reasons must not leak; allowed replacements should be linked.

After rollback, map, drawer, Focus Mode, export, and diagnostics should agree on the active release. Client caches/storage must invalidate, and rollback failure must fail closed.

Every new test framework, baseline system, fixture family, or shared harness needs a mechanical rollback plan that restores scripts, dependencies, CI, artifacts, and documentation without leaving duplicate ownership.

[Back to top](#top)

---

## Test results, UI states, runtime outcomes, and policy decisions

Do not reuse one vocabulary across layers.

Test results: `PASS`, `FAIL`, `SKIP`, `XFAIL`, `XPASS`, `ERROR`.

Proposed UI states: `LOADING`, `READY`, `EMPTY`, `BLOCKED`, `OFFLINE`, `STALE`, `WITHDRAWN`, `RECOVERING`.

Runtime outcomes: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`.

Policy decisions must use the accepted policy contract and remain distinct from UI rendering and test results.

Release states must preserve candidate, released, withdrawn, superseded, corrected, and rolled-back distinctions.

```text
pytest PASS        != runtime ANSWER
component READY    != release RELEASED
UI BLOCKED         != policy DENY unless policy says so
empty result       != ABSTAIN
network ERROR      != DENY
snapshot PASS      != accessibility conformance
axe PASS           != complete inclusive usability
```

[Back to top](#top)

---

## Runner, CI, and promotion boundary

No direct UI runner is established by the checked lane. Explorer scripts are TODO-only, the shared package has no scripts, the Makefile excludes `tests/ui`, and UI/accessibility workflows echo TODO commands.

A smallest sound activation sequence is: accept placement/owners; select one real component; ratify payload contract/schema; add synthetic positive and negative fixtures; select the owner-appropriate runner; add deterministic rendering and accessibility assertions; enforce no-network and cleanup; fail on zero collection; wire the exact suite into CI; retain only sanitized artifacts; document correction and rollback; repeat one component at a time.

Accepted commands must use locked dependencies, return nonzero on failure, fail on zero tests, avoid swallowed failures, deny live network, freeze time/locale, clean browser state, report counts/skips, and emit only declared sanitized artifacts.

Future substantive CI should prove installation, type/build success, real collection, component/app tests, policy guards, accessibility, no-network/no-leak controls, artifact sanitization, correction/rollback, thresholds, and branch-protection significance.

UI tests may block promotion when a public trust invariant is material. They cannot approve promotion or release. A green TODO job, empty source scan, empty browser suite, or zero-component accessibility scan is not enforcement.

[Back to top](#top)

---

## Migration, deprecation, and rollback of this lane

Retain `tests/ui/` only for shared assertions without a clearer implementation owner.

When ownership becomes specific, move the test to the package/app/policy/map/E2E/domain owner; preserve history; update fixtures and CI; remove duplicates; keep a pointer only when useful; compare behavior/collection; and record rollback.

Keep a shared test here only when it validates the same trust-state contract across multiple implementations and a neutral owner is explicitly accepted.

If every assertion gains a precise owner, this directory may remain a routing README or be retired through documented migration. Do not delete it while CI, docs, fixtures, or callers reference it.

Revert or correct this README if it claims nonexistent coverage, treats TODO workflows as enforcement, centralizes implementation-specific tests without review, permits direct store/model access, weakens accessibility/no-leak requirements, allows real sensitive fixtures, treats screenshots as release evidence, or creates parallel authority.

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Records the direct lane as README-only without claiming exhaustive absence.
- [x] Records checked-absent direct harness, test, and config paths.
- [x] Records representative fixture payload absence.
- [x] Separates app, package, contracts, schemas, policy, fixtures, tests, artifacts, and release authority.
- [x] Records TODO package scripts and workflows.
- [x] Records sampled placeholder component and package entrypoints.
- [x] Identifies the static Explorer boundary guard without inflating it into rendering/accessibility coverage.
- [x] Records Makefile exclusion.
- [x] Replaces schematic proposed test files with routing and admission rules.
- [x] Defines governed payload, finite outcome, Evidence Drawer, Focus Mode, map/time, accessibility, no-leak, browser side-effect, artifact, correction, and rollback requirements.
- [x] Separates test, UI, runtime, policy, and release vocabularies.
- [x] Changes documentation only.
- [ ] Record repository-native CI after PR creation.

### Future active UI test capability

The capability is not operationally complete until owners/placement are accepted; real components and routes exist; payload contracts/schemas are accepted; positive/negative fixtures exist; tests import real implementation; collection is nonzero; network/time/locale/viewport/storage are controlled; sensitive values cannot leak; accessibility and keyboard/focus checks are substantive; correction/rollback cases exist; artifacts are governed; exact suites run in CI; metrics are measured; promotion dependencies are explicit; and migration/rollback are documented.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `UI-TEST-001` | Should `tests/ui/` retain shared executable tests or remain a routing README? | `NEEDS VERIFICATION` |
| `UI-TEST-002` | Is the bounded direct inventory complete? | `NEEDS VERIFICATION` |
| `UI-TEST-003` | Are UI tests dynamically collected from another path or service? | `UNKNOWN` |
| `UI-TEST-004` | What is the accepted split among root, package-local, app-local, E2E, policy, and map tests? | `NEEDS VERIFICATION` |
| `UI-TEST-005` | Which Explorer Web feature entrypoints are functional rather than placeholders? | `NEEDS VERIFICATION` |
| `UI-TEST-006` | Which shared UI components and exports are functional? | `NEEDS VERIFICATION` |
| `UI-TEST-007` | What framework and component test runner are accepted? | `UNKNOWN` |
| `UI-TEST-008` | What browser/E2E runner is accepted? | `UNKNOWN` |
| `UI-TEST-009` | What is the canonical UI payload contract/schema set? | `NEEDS VERIFICATION` |
| `UI-TEST-010` | What UI render/interaction vocabulary is canonical? | `NEEDS VERIFICATION` |
| `UI-TEST-011` | How is zero collection made fatal? | `UNKNOWN` |
| `UI-TEST-012` | How is live network denied? | `UNKNOWN` |
| `UI-TEST-013` | How are clock, locale, timezone, viewport, and DPR fixed? | `UNKNOWN` |
| `UI-TEST-014` | What accessibility baseline and exception process are accepted? | `NEEDS VERIFICATION` |
| `UI-TEST-015` | Which screen readers/browsers require manual validation? | `NEEDS VERIFICATION` |
| `UI-TEST-016` | What keyboard and focus test matrix is required? | `NEEDS VERIFICATION` |
| `UI-TEST-017` | How are sensitive fixtures and screenshots reviewed? | `NEEDS VERIFICATION` |
| `UI-TEST-018` | What visual-regression tool, threshold, and baseline owner are accepted? | `UNKNOWN` |
| `UI-TEST-019` | What generated artifacts may CI retain, and for how long? | `NEEDS VERIFICATION` |
| `UI-TEST-020` | How are no-leak canaries scanned across DOM, storage, logs, URLs, clipboard, downloads, and artifacts? | `UNKNOWN` |
| `UI-TEST-021` | Which workflow owns substantive UI tests? | `UNKNOWN` |
| `UI-TEST-022` | Which workflow owns substantive accessibility tests? | `UNKNOWN` |
| `UI-TEST-023` | Which UI tests block promotion? | `UNKNOWN` |
| `UI-TEST-024` | What are current test count, scanned component/page count, pass rate, coverage, runtime, and flake rate? | `UNKNOWN` |
| `UI-TEST-025` | How do correction, withdrawal, supersession, and rollback invalidate browser caches and state? | `UNKNOWN` |
| `UI-TEST-026` | What is the deprecation trigger for this lane? | `NEEDS VERIFICATION` |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| prior target blob `4dbbea20…` | `CONFIRMED` | Existing v0.1 UI-test intent. | Direct executable suite. |
| Directory Rules `2affb080…` | `CONFIRMED DOCTRINE` | Responsibility placement and trust separation. | Current UI behavior. |
| tests root `5614de99…` | `CONFIRMED ROOT CONTRACT` | `tests/ui/` is the intended UI trust-state lane. | Collection or coverage. |
| UI contracts `ddd14b5f…` | `CONFIRMED DRAFT/PROPOSED` | UI trust-surface meaning and finite outcomes. | Accepted payload set or implementation. |
| packages/ui README `832df71d…` | `CONFIRMED DOCUMENTATION` | Shared component package boundary. | Functional components. |
| packages/ui source README `55c1365c…` | `CONFIRMED DOCUMENTATION` | Intended source and accessibility posture. | Exports, runner, or consumers. |
| packages/ui package JSON `9e165aa0…` | `CONFIRMED SCAFFOLD` | Package identity and version. | Build/test scripts. |
| packages/ui source entry `2c9ea341…` | `CONFIRMED PLACEHOLDER` | Entry file exists. | Shared UI implementation. |
| Explorer README `755dae3e…` | `CONFIRMED DOCUMENTATION` | Map-first shell and governed-API boundary. | Routes or deployment. |
| Explorer source README `770cace0…` | `CONFIRMED DOCUMENTATION` | Proposed source layout and TODO status. | Feature implementation. |
| Explorer package JSON `ce981192…` | `CONFIRMED TODO SCAFFOLD` | Scripts exist and echo TODO. | Build, test, or dev behavior. |
| Evidence Drawer entry `6438397d…` | `CONFIRMED PLACEHOLDER` | Named feature path exists. | Drawer behavior. |
| Focus Panel entry `73e8763e…` | `CONFIRMED PLACEHOLDER` | Named feature path exists. | Focus Mode behavior. |
| Trust Header entry `2938d6ba…` | `CONFIRMED PLACEHOLDER` | Named feature path exists. | Trust-header behavior. |
| UI fixture README `8d87d87b…` | `CONFIRMED PLANNING DOC` | Fixture intent and safety posture. | Payload inventory or consumers. |
| checked fixture paths | `NOT FOUND AT CHECKED PATHS` | Representative proposed payloads are not established. | Exhaustive fixture absence. |
| Explorer boundary test `97d44069…` | `CONFIRMED EXECUTABLE STATIC GUARD` | Adapter import and path-literal assertions. | Rendering, browser, accessibility, or non-vacuous source coverage. |
| Makefile `4dc8cf63…` | `CONFIRMED` | Default tests exclude UI; ui-build is TODO. | Dynamic/external UI collection. |
| ui-build workflow `d73a43d7…` | `CONFIRMED TODO SCAFFOLD` | Workflow exists. | UI build or test execution. |
| accessibility workflow `62ede945…` | `CONFIRMED TODO SCAFFOLD` | Workflow exists. | Axe or keyboard execution. |
| bounded search/path checks | `CONFIRMED BOUNDED RESULT` | README-only direct-lane conclusion and sampled scaffold state. | Exhaustive absence across history, branches, generators, ignored files, or external CI. |

For implementation claims, prefer real UI source and registration, direct test results, fixtures and accepted contracts/schemas, browser/accessibility traces, workflow commands/logs, sanitized reports, release records, repository documentation, then planning documents. README intent cannot outrank code, tests, logs, or generated evidence.

[Back to top](#top)

---

## Maintainer note

Keep UI assertions close to the implementation owner. Use this parent lane only for genuinely shared trust-state proof.

A rendered answer is not truth. A visible citation is not citation validation. A release badge is not release approval. A static grep is not complete UI safety. An axe scan is not complete accessibility. A screenshot is not semantic proof. A hidden value is still a leak if it remains in the DOM or client state. A placeholder export is not a component. A green workflow that echoes TODO or scans zero targets is not coverage.

Add one complete, reviewable UI case at a time with a real system under test, accepted payload contract, synthetic fixture, positive and negative controls, accessible semantics, deterministic browser state, no-network enforcement, no-leak canaries, correction/rollback handling, and substantive CI.

<p align="right"><a href="#top">Back to top</a></p>
