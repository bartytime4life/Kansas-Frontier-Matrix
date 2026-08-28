<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/a11y/readme
title: Fauna Accessibility Test Lane README
type: test-lane-readme
version: v0.2
status: draft; repository-grounded; readme-only lane at evidence snapshot
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Accessibility steward>
  - <PLACEHOLDER — UI steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Sensitivity reviewer>
created: 2026-07-05
updated: 2026-07-17
policy_label: public; tests; fauna; accessibility; no-network; fail-closed
implementation_status: README contract present; executable Fauna accessibility tests and canonical lane command not established by bounded repository inspection
truth_posture: cite-or-abstain; current behavior claims are limited to the pinned evidence snapshot
responsibility_root: tests/
domain_lane: fauna
sub_lane: a11y
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: dc30140567828b45d54426b0e55055ef8d83b5a7
  target_prior_blob: 27779ceb75e90646d80fe4b3d0e116feb84fe609
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - docs/architecture/directory-rules.md
  - docs/doctrine/directory-rules.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/architecture/ui/ACCESSIBILITY.md
  - docs/domains/fauna/SENSITIVITY.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - fixtures/domains/fauna/README.md
  - .github/workflows/accessibility.yml
  - .github/workflows/domain-fauna.yml
  - .github/workflows/README.md
  - Makefile
  - pyproject.toml
  - package.json
  - apps/explorer-web/package.json
  - schemas/contracts/v1/receipts/generated_receipt.schema.json
tags:
  - kfm
  - tests
  - fauna
  - a11y
  - accessibility
  - ui
  - map
  - evidence-drawer
  - focus-mode
  - sensitivity
  - geoprivacy
  - no-network
  - fail-closed
notes:
  - "v0.2 preserves the v0.1 lane contract and replaces blanket implementation uncertainty with a pinned repository-grounded maturity statement."
  - "Bounded code-index searches surfaced this README but no executable module under tests/domains/fauna/a11y; absence is not claimed beyond that inspection boundary."
  - "The root workspace declares Playwright, but no Fauna accessibility command, axe dependency, or non-placeholder explorer-web test implementation was established."
  - "Both accessibility.yml and domain-fauna.yml exist as broad-trigger PROPOSED greenfield stubs whose jobs currently echo TODO commands."
  - "Directory Rules have duplicate live authority surfaces; both agree that this test lane belongs under tests/domains/fauna/a11y. The authority-path conflict remains visible and unresolved."
] -->

<a id="top"></a>

# Fauna Accessibility Tests

> **Purpose.** Define the test contract for proving that Fauna map, drawer, list, Focus Mode, and trust-state surfaces remain perceivable, operable, understandable, and robust without disclosing policy-withheld Fauna information or weakening KFM's governed public path.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![authority: tests only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![maturity: README only](https://img.shields.io/badge/maturity-README--only-yellow)
![network: denied by default](https://img.shields.io/badge/network-denied--by--default-critical)
![sensitivity: fail closed](https://img.shields.io/badge/sensitivity-fail--closed-blue)
![WCAG target: proposed](https://img.shields.io/badge/WCAG%202.2%20AA-target%20PROPOSED-informational)

**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `a11y/`  
**Current maturity:** repository-grounded README contract; executable lane tests are not established  
**Default posture:** public-safe deterministic fixtures; no network; no secrets; no exact sensitive locations; finite outcomes remain accessible  
**Last reviewed:** 2026-07-17

> [!IMPORTANT]
> Accessibility does not authorize disclosure. Labels, descriptions, hidden text, DOM attributes, screenshots, traces, logs, tables, and non-map alternatives must obey the same Fauna rights, sensitivity, geoprivacy, evidence, review, and release gates as the visible map.

> [!CAUTION]
> This README does not claim WCAG conformance, executable Fauna accessibility coverage, a canonical axe setup, a working explorer-web test suite, or CI enforcement. Those claims require observed tests, tooling, runs, and review evidence.

## Quick navigation

[Purpose](#purpose-and-audience) · [Authority](#authority-directory-fit-and-conflicts) · [Status](#repository-grounded-status) · [Scope](#scope-and-non-scope) · [Case contract](#minimum-test-case-contract) · [Scenarios](#required-scenario-families) · [Proof matrix](#accessibility-proof-matrix) · [Fixtures](#fixtures-and-test-data) · [Network](#determinism-network-and-live-test-tiers) · [Execution](#current-execution-and-ci-surface) · [Validation](#validation-layers-and-expected-outcomes) · [Failures](#failure-interpretation) · [Limits](#what-a-passing-suite-does-not-prove) · [Review](#review-burden) · [Maintenance](#maintenance-and-fixture-updates) · [Done](#definition-of-done) · [Evidence](#evidence-ledger) · [Open](#open-verification-register) · [Rollback](#changelog-and-rollback)

---

## Purpose and audience

This directory is the Fauna domain test lane for **accessibility behavior**. It exists to prove that governed Fauna UI states can be used by people who rely on keyboard navigation, visible focus, screen readers, text alternatives, non-map views, reduced motion, zoom or reflow, and non-color trust cues.

The lane is for:

- Fauna, UI, accessibility, test, sensitivity, and governance reviewers;
- maintainers implementing or revising Fauna map controls, feature lists, Evidence Drawer content, trust badges, and Focus Mode states;
- CI maintainers deciding when an accessibility scaffold is mature enough to become an enforceable check; and
- reviewers interpreting what a passing or failing result actually supports.

A mature lane should prove all of the following:

1. **Accessible does not mean over-disclosed.** Assistive content never reveals fields or geometry that policy withholds.
2. **Trust state is perceivable.** Released, generalized, restricted, stale, conflicted, denied, abstained, withdrawn, and error states are available in text and are not color-only.
3. **Keyboard paths are complete.** Users can enter, traverse, activate, dismiss, and leave Fauna controls without a pointer.
4. **Finite outcomes are announced.** `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` are distinguishable to assistive technology.
5. **A non-map path exists.** Public-safe Fauna information that can be selected on the map can also be reached through an equivalent governed list, table, or detail path when the map itself is not operable.
6. **Fixtures are public-safe.** Tests use synthetic, generalized, or explicitly approved public-safe inputs.
7. **Tests remain tests.** This lane proves behavior; it does not define UI implementation, policy, evidence, schemas, release state, or publication authority.

[Back to top](#top)

---

## Authority, directory fit, and conflicts

The path is correct under the KFM responsibility-root rule:

```text
tests/domains/fauna/a11y/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna-specific accessibility and trust-state behavior. |
| Owning root | `tests/` — enforceability and regression proof. |
| Domain segment | `domains/fauna/` — Fauna remains a lane, not a repository root. |
| Sub-lane | `a11y/` — accessibility assertions that are specifically Fauna-aware. |
| Reusable fixture home | `fixtures/domains/fauna/`, subject to its own runtime-fixture boundary and consumer review. |
| UI implementation homes | `packages/ui/`, `packages/maplibre/`, and `apps/explorer-web/` when implemented. |
| Governed API home | `apps/governed-api/` when the tested flow crosses the public trust membrane. |
| Domain doctrine home | `docs/domains/fauna/`. |
| Accessibility doctrine home | `docs/architecture/ui/ACCESSIBILITY.md`. |
| Policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/`. |
| Schema homes | `schemas/contracts/v1/domains/fauna/` and applicable UI/runtime schema families. |
| Receipts, proofs, and release decisions | Their owning `data/` and `release/` lanes; never this test directory. |

### Directory Rules authority conflict

Repository evidence contains multiple Directory Rules artifacts, including:

- `docs/architecture/directory-rules.md`, which identifies itself as the live v1.3.1 placement-refresh artifact; and
- `docs/doctrine/directory-rules.md`, which is a later-numbered presentation edition at a different path.

`CONTRIBUTING.md` directs contributors to use the architecture-path artifact while the placement question remains ADR-class and unresolved. This README does not resolve that conflict. Both inspected artifacts agree on the rule that domain-specific enforceability work belongs under `tests/` with the domain as a path segment, so the target placement is not blocked.

> [!WARNING]
> This directory must not become a second UI, fixture, schema, policy, source-registry, receipt, proof, release, catalog, or lifecycle-data home.

[Back to top](#top)

---

## Repository-grounded status

**Evidence snapshot:** `main@dc30140567828b45d54426b0e55055ef8d83b5a7`  
**Prior target blob:** `27779ceb75e90646d80fe4b3d0e116feb84fe609`

| Surface | Observed state | Truth posture |
|---|---|---:|
| Target README | Existing v0.1 README fetched and preserved as the revision baseline. | `CONFIRMED` |
| Target path placement | Existing path under `tests/domains/fauna/a11y/`; both inspected Directory Rules copies support the responsibility-root pattern. | `CONFIRMED` path / authority-copy conflict visible |
| Path-scoped instructions | No `AGENTS.md` was found at repository root, `tests/`, `tests/domains/`, `tests/domains/fauna/`, or this lane in the bounded preflight. | `CONFIRMED` for checked paths |
| Overlapping open work | No open PR naming the target path and no matching Fauna-a11y task branch surfaced in the connector searches. | `CONFIRMED` within search boundary |
| Executable files in this lane | Code-index searches for the exact lane surfaced this README but no test module. This is not a complete recursive absence proof. | `NEEDS VERIFICATION` / not established |
| Root Python test command | `make test` runs only `tests/schemas` and `tests/contracts`; it does not exercise this lane. | `CONFIRMED` |
| Root validator command | `make schemas` runs the shared schema validator aggregate; it is not a Fauna accessibility check. | `CONFIRMED` |
| Root JavaScript tooling | Root `package.json` declares Playwright, pixelmatch, and pngjs. No axe dependency or Fauna accessibility script surfaced. | `CONFIRMED` / bounded search |
| Explorer-web test script | `apps/explorer-web/package.json` defines `test` as `echo TODO`. | `CONFIRMED` placeholder |
| Accessibility workflow | `.github/workflows/accessibility.yml` exists, triggers broadly, and currently runs `echo TODO axe` and `echo TODO keyboard-navigation`. | `CONFIRMED` stub; no enforcement claim |
| Fauna workflow | `.github/workflows/domain-fauna.yml` exists, triggers broadly, and all observed jobs currently echo TODO commands. | `CONFIRMED` stub; no enforcement claim |
| Fauna fixture root | `fixtures/domains/fauna/README.md` records draft valid, invalid, layers, sensitive-deny, stale-source, synthetic, and golden lanes. Payload-to-consumer alignment remains incomplete. | `CONFIRMED` README inventory / `NEEDS VERIFICATION` consumers |
| Accessibility standard | UI doctrine names WCAG 2.2 AA as a proposed target, not measured conformance. | `PROPOSED` target |
| Recent test or workflow results | No run, log, coverage report, accessibility report, or branch-protection requirement was inspected for this revision. | `UNKNOWN` / `NOT RUN` |

### Safe current conclusion

`tests/domains/fauna/a11y/` is a valid, documented test responsibility lane. At this snapshot it must be treated as **README-only until executable tests, a non-placeholder command, and observed CI evidence prove otherwise**.

[Back to top](#top)

---

## Scope and non-scope

### In scope

This lane may contain Fauna-specific tests for:

- keyboard navigation, focus order, focus visibility, focus restoration, and escape behavior;
- accessible names, descriptions, headings, landmarks, dialog semantics, and status announcements;
- trust badges and finite outcomes that do not rely on color alone;
- Fauna layer controls, legends, feature lists, map alternatives, Evidence Drawer content, and Focus Mode result states;
- generalized, restricted, stale, conflicted, denied, abstained, withdrawn, and error presentations;
- prevention of sensitive-data leaks through hidden text, accessible names, DOM attributes, snapshots, traces, logs, screenshots, or exported accessibility trees;
- reduced-motion behavior for map transitions or Story/Focus interactions when those surfaces exist;
- zoom, reflow, narrow viewport, and touch behavior where a Fauna-specific failure mode exists;
- non-map parity for public-safe feature inspection; and
- integration with canonical UI and governed-API code from their owning roots.

### Out of scope

This lane does not own:

- production UI, MapLibre, API, runtime, model-adapter, or application code;
- binding policy, geoprivacy parameters, source descriptors, rights decisions, or sensitivity classifications;
- canonical schemas, semantic contracts, layer manifests, release manifests, receipts, proofs, catalogs, correction notices, or rollback cards;
- raw, work, quarantined, processed, or published Fauna data;
- reusable fixture corpora that belong in the verified fixture responsibility root;
- exact sensitive locations, real observer identities, restricted agency records, private stewardship details, or reconstruction-enabling metadata;
- general WCAG conformance certification for the entire KFM product; or
- live-network source checks in the default suite.

[Back to top](#top)

---

## Minimum test-case contract

Every executable case added to this lane should make its governance and accessibility claim explicit.

| Field | Required content |
|---|---|
| `case_id` | Stable, descriptive identifier. |
| Concern | Keyboard, focus, naming, status, non-map parity, reduced motion, leakage guard, or another bounded concern. |
| Fixture reference | Exact synthetic or public-safe input path and version/hash where available. |
| Rights and sensitivity posture | Public-safe, generalized, denied, restricted, stale, or another declared test state. |
| Expected finite outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or an explicit test/setup failure. |
| Expected accessible surface | Name, description, role, status announcement, focus target, or non-map equivalent. |
| Forbidden disclosure | Fields, coordinates, identifiers, hidden text, or metadata that must not appear. |
| Deterministic setup | Local state, viewport, locale, time, seed, and mock/fixture assumptions. |
| Network posture | `denied` by default; any live tier must be separately marked and excluded from default CI. |
| Validation layer | DOM/a11y tree, keyboard/e2e, schema/envelope, policy boundary, snapshot/leak scan, or another named layer. |
| Cleanup | No retained credentials, mutable cache dependence, source side effects, or sensitive artifacts. |

A test with no assertion about observable behavior is not proof. A skipped case, zero-test collection, placeholder command, or TODO workflow is not a pass.

[Back to top](#top)

---

## Required scenario families

The tests profile requires positive, negative, denied, abstained, quarantined, and error cases. In this lane those states mean:

| Scenario family | Example condition | Expected behavior | Authority boundary |
|---|---|---|---|
| Valid public-safe | Released generalized Fauna feature with resolvable evidence. | `ANSWER`; controls and evidence path are keyboard reachable and correctly named. | Test proves only the asserted UI behavior. |
| Invalid | Missing accessible name, malformed envelope, invalid role/state pairing, or inaccessible focus path. | Deterministic test failure; do not coerce into `ANSWER`. | Schema/contract meaning remains in owning roots. |
| Denied | Request or selection would expose policy-withheld detail, unknown rights, or unreleased material. | Accessible `DENY` state and reason category without withheld detail. | Policy decides denial; test verifies presentation and non-disclosure. |
| Abstained | Evidence is missing, stale beyond allowed use, conflicted, or not released for the requested claim. | Accessible `ABSTAIN` state with bounded explanation and correction/evidence path when permitted. | Evidence resolution and release state remain upstream. |
| Quarantined | A fixture or candidate is marked unsafe, malformed, or pre-public and must not reach the public UI. | No public rendering; test reports inadmissible setup or asserts the governed boundary. | This lane does not create or move lifecycle quarantine records. |
| Error | Runtime, transport, parser, schema, or component failure prevents a safe response. | Accessible `ERROR`; no silent fallback, stale truth claim, or sensitive-data exposure. | Operational error is distinct from policy `DENY` and evidence `ABSTAIN`. |
| Restricted/generalized | Public derivative is allowed but exact detail is withheld. | Public-safe representation plus text that exact detail is not disclosed; no reconstructive clues. | Transform and review authority remain upstream. |
| Withdrawn/superseded | Previously released view has correction or supersession state. | Accessible withdrawn/superseded notice and current-release path when available. | Test does not issue the correction or release. |

[Back to top](#top)

---

## Accessibility proof matrix

| Test concern | Required proof | Negative assertion |
|---|---|---|
| Keyboard entry and exit | User can enter, traverse, activate, dismiss, and leave Fauna controls and drawers. | No keyboard trap or pointer-only action. |
| Focus visibility and order | Focus remains visible, logical, and restored after dialogs/drawers close. | No focus loss behind overlays or into hidden content. |
| Accessible names | Layers, filters, badges, buttons, lists, drawers, and Focus actions have meaningful names. | No policy-withheld detail embedded in labels or descriptions. |
| Dialog and drawer semantics | Evidence Drawer and modal surfaces expose correct roles, names, focus containment, and escape behavior. | Popup content is not represented as equivalent to evidence authority. |
| Status announcements | Loading, result, stale, denial, abstention, withdrawal, and error changes are announced without excessive repetition. | No silent negative state. |
| Trust state not color-only | Icon, text, pattern, or programmatic state accompanies color. | No color-only distinction between released, stale, denied, or redacted. |
| Finite outcomes | `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` are programmatically distinguishable. | No generic success message for a negative outcome. |
| Evidence access | Allowed evidence controls are reachable and identify evidence state. | No inaccessible evidence path and no evidence claims from raw feature properties. |
| Sensitive-detail withholding | Accessible tree, DOM, logs, traces, snapshots, and exports omit withheld fields and exact details. | No hidden-but-discoverable sensitive content. |
| Non-map parity | Public-safe feature information is available through an equivalent governed list/table/detail route. | No essential information available only by pointer interaction. |
| Reduced motion | Motion-heavy map or Story/Focus behavior honors reduced-motion settings when implemented. | No forced camera or transition sequence that blocks use. |
| Zoom and reflow | Text, controls, and trust state remain usable at supported zoom/reflow conditions. | No clipped reason or hidden status that changes meaning. |
| Narrow viewport and touch | Critical controls remain reachable and operable when the supported surface narrows. | No inaccessible hover-only state. |
| No-network default | Test succeeds entirely from pinned local fixtures and mocks. | Any unexpected source, tile, geocoder, or external call fails the harness. |

[Back to top](#top)

---

## Fixtures and test data

The currently documented reusable Fauna fixture root is:

```text
fixtures/domains/fauna/
```

Its README records draft lanes for `valid/`, `invalid/`, `golden/`, `layers/`, `sensitive_deny/`, `stale_source/`, and `synthetic/`. This README does not upgrade placeholder payloads or unverified consumer links into executable coverage.

### Required fixture posture

Fixtures used by this lane must be:

- synthetic or explicitly public-safe;
- compact, deterministic, reviewable, and no-network;
- free of exact sensitive locations, real observer identities, private stewardship details, production source exports, and reconstructive clues;
- explicit about source role, evidence state, rights, sensitivity, review, release, correction, freshness, and expected finite outcome when material;
- paired with stable expected outputs when they become regression anchors; and
- linked to an actual test consumer before being counted as covered.

### Test-local examples

Tiny test-local values may live beside a test only when they are not a reusable corpus, are clearly synthetic, and are easier to understand inline. Reusable scenario families belong in the verified fixture root rather than being duplicated under `tests/`.

### Rights and sensitivity review

A fixture that contains or plausibly reconstructs real protected Fauna detail is not a test convenience. Stop use, prevent logs or artifacts from spreading it, route the material through the appropriate private/security and sensitivity-review path, and replace it with a synthetic or governed public-safe fixture.

[Back to top](#top)

---

## Determinism, network, and live-test tiers

### Default tier: deterministic and no-network

Default tests must not depend on:

- live source services, map tiles, geocoders, model providers, or mutable upstream APIs;
- credentials, local secret files, developer caches, browser profiles, or production storage;
- current clock time without a fixed clock;
- uncontrolled locale, timezone, viewport, random seed, or animation timing; or
- direct source-system side effects.

Unexpected network access is a test-harness failure, not a skip.

### Separate live or integration tier

A future live tier may exist only when it is:

- explicitly named and separately triggered;
- excluded from the default no-network suite;
- read-only unless a separately governed write is authorized;
- bounded by source terms, rate limits, credentials, and sensitivity rules;
- safe for fork pull requests and logs; and
- documented with timeout, retry, outage, stale-state, and cleanup behavior.

No such Fauna accessibility live tier was established in the inspected repository evidence.

[Back to top](#top)

---

## Current execution and CI surface

### Repository-native commands observed

| Surface | Observed command or behavior | Coverage of this lane |
|---|---|---|
| `make test` | `python -m pytest tests/schemas tests/contracts -q` | **None established.** The target lane is not included. |
| `make schemas` | `python tools/validators/_common/run_all.py` | Schema validation only; not accessibility behavior. |
| Root `npm test` | Echoes a repository TODO message. | Placeholder; no test execution claim. |
| Explorer-web `test` script | Echoes `TODO`. | Placeholder; no UI/a11y execution claim. |
| Root Playwright dependency | Playwright is declared in root dev dependencies. | Tool availability signal only; no Fauna a11y suite or script established. |
| Axe integration | No axe dependency or executable integration surfaced in bounded searches. | `NEEDS VERIFICATION` / not established. |

### Workflow status

| Workflow | Trigger observed | Current job behavior | Interpretation |
|---|---|---|---|
| `.github/workflows/accessibility.yml` | Broad `pull_request` and push to `main` | `echo TODO axe`; `echo TODO keyboard-navigation` | Named scaffold, not accessibility enforcement. |
| `.github/workflows/domain-fauna.yml` | Broad `pull_request` and push to `main` | TODO validate, proof, and publish-dry-run echoes | Named scaffold, not Fauna-domain proof or publication. |

The workflow inventory also records broad documentation, schema, contract, API, and validator triggers. Reviewers must inspect actual steps and conclusions; job names do not expand coverage.

### Proposed future lane command

Once executable modules exist and the repository accepts the lane runner, a targeted command may take the form:

```bash
python -m pytest tests/domains/fauna/a11y -q
```

This is **PROPOSED**, not current repository behavior. Before adoption, the command must collect at least one intended test, fail on unexpected skips or zero collection as defined by the accepted harness, and be wired to deterministic public-safe fixtures.

[Back to top](#top)

---

## Validation layers and expected outcomes

A mature suite should exercise separate layers rather than treating one green check as universal proof.

| Validation layer | What it proves for the tested case | Expected output |
|---|---|---|
| Static structure | Required names, roles, labels, landmarks, and state attributes exist. | Pass/fail assertion. |
| Keyboard and focus | Operable path, logical order, visible focus, dismissal, and restoration. | Pass/fail trace. |
| Accessibility tree | Assistive representation contains intended public-safe meaning. | Pass/fail tree assertion. |
| Status and live-region behavior | Finite and changing states are announced appropriately. | Pass/fail announcement assertion. |
| Non-map parity | Equivalent governed path exists for map-selected information. | Pass/fail parity assertion. |
| Envelope/schema boundary | UI consumes valid finite-outcome payloads and rejects malformed payloads. | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or test failure as declared. |
| Policy-leak guard | Withheld detail is absent from all rendered and test-artifact channels. | Pass/fail disclosure scan. |
| Fixture admission | Fixture is synthetic/public-safe and has a declared expected state. | Accepted test setup or explicit setup failure. |
| Visual support | Focus, contrast, status, and non-color cues remain visible where image comparison is appropriate. | Reviewable diff; not sufficient alone. |
| No-network guard | No unexpected external request occurs. | Pass or harness failure. |

### Acceptance vocabulary

Task- and suite-level reporting should use explicit outcomes such as:

```text
PASS | FAIL | PARTIAL | NOT RUN | NOT APPLICABLE | UNKNOWN
```

Runtime fixtures may additionally expect:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

Do not conflate the two vocabularies. A correctly rendered `DENY` can make a test `PASS`; an unexpected `ANSWER` can make it `FAIL`.

[Back to top](#top)

---

## Failure interpretation

| Observed result | Interpretation | Required response |
|---|---|---|
| Accessibility assertion fails | Regression or unmet contract for the exact tested scope. | Fix implementation or revise the test only with evidence that the contract changed. |
| Sensitive detail appears in DOM, a11y tree, snapshot, log, trace, screenshot, or artifact | Security/sensitivity failure, not a cosmetic defect. | Stop dissemination, contain artifacts, use the private review path, and replace unsafe data. |
| Expected `DENY` or `ABSTAIN` becomes `ANSWER` | Trust-membrane or policy/evidence boundary failure. | Fail closed and investigate upstream decision inputs. |
| Expected public-safe `ANSWER` becomes negative | Possible regression, stale fixture, missing evidence, or policy change. | Preserve the negative state; investigate rather than bypass it. |
| Zero tests collected | No proof was executed. | Treat as failure or invalid run under the accepted harness. |
| Test skipped | Coverage gap. | Report `SKIPPED`/`NOT RUN`; do not count as pass. |
| Runner, browser, component, or fixture missing | Infrastructure or implementation gap. | Report the gap; do not replace it with a TODO success. |
| Unexpected network request | Hermeticity failure. | Fail the default tier and identify the caller. |
| Flaky timing or focus result | Determinism defect until resolved. | Quarantine the test from authority claims, fix the harness, and retain failure evidence. |
| Workflow job echoes TODO and succeeds | Scaffold executed, not validation. | Report as placeholder only. |

[Back to top](#top)

---

## What a passing suite does not prove

Even a substantive passing Fauna accessibility suite would not, by itself, prove:

- complete WCAG 2.2 AA conformance for KFM;
- accessibility across every browser, assistive technology, device, locale, viewport, zoom level, or user workflow;
- correctness, completeness, authority, or freshness of Fauna evidence;
- validity of rights, sensitivity, source-role, policy, review, release, correction, or rollback decisions;
- that generalized data cannot be re-identified through untested cross-domain joins;
- that a map, popup, screenshot, tile, badge, or AI answer is sovereign truth;
- release readiness, publication approval, or branch-protection enforcement; or
- absence of defects outside the exact fixtures and paths exercised.

A green accessibility check is one review signal. It does not publish, approve, or certify the underlying Fauna claim.

[Back to top](#top)

---

## Review burden

Reviewers should be able to answer:

- Does each test have a bounded accessibility claim and a deterministic expected result?
- Are `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` states distinguishable without color alone?
- Can a keyboard-only user complete and exit the tested path?
- Does the non-map alternative preserve the same governed, public-safe meaning?
- Do labels, hidden text, DOM attributes, logs, traces, snapshots, screenshots, and test artifacts avoid withheld detail?
- Are fixtures synthetic/public-safe, no-network, rights-aware, and linked to actual consumers?
- Are policy, schema, source, evidence, receipt, proof, release, and UI authorities kept in their owning roots?
- Are skips, TODOs, zero collection, missing tools, and workflow stubs reported as gaps rather than passes?
- Are proposed WCAG targets distinguished from measured conformance?
- Does the PR identify workflow-trigger, sensitivity, generated-receipt, validation, and rollback posture?

Fauna accessibility changes require Fauna and accessibility review. Changes that alter sensitivity, public-safe transformation, rights, or release behavior require the corresponding policy/sensitivity/release reviewers; this test lane cannot approve those changes.

[Back to top](#top)

---

## Maintenance and fixture updates

Update this README when any of the following changes:

- executable tests are added, removed, renamed, or moved;
- the canonical runner, command, browser harness, or accessibility library changes;
- fixture lanes or stable expected outputs change;
- finite-outcome vocabulary or trust-state presentation changes;
- the non-map alternative or Evidence Drawer/Focus Mode interaction model changes;
- workflow stubs become command-bearing or their trigger/permission posture changes;
- WCAG target, measurement method, supported browser/assistive-technology matrix, or release gate changes; or
- the Directory Rules authority-path conflict is resolved.

For each fixture update:

1. identify the consuming test and expected state;
2. verify synthetic/public-safe provenance and sensitivity posture;
3. preserve deterministic identifiers, time, locale, viewport, and seed assumptions;
4. update expected outputs intentionally;
5. run the targeted lane and any affected broader UI/Fauna checks when they exist;
6. inspect generated screenshots, traces, logs, and reports for disclosure; and
7. record why the change is a correction, new scenario, or expected-behavior change.

Do not silently refresh snapshots to make a failure disappear.

[Back to top](#top)

---

## Definition of done

This lane is mature only when all applicable criteria are supported by repository evidence:

- [ ] At least one executable test module exists and the targeted command collects the intended cases.
- [ ] The canonical lane command is documented in repository tooling and is not a TODO.
- [ ] Keyboard entry, traversal, activation, dismissal, visible focus, and restoration are tested.
- [ ] Accessible names, descriptions, roles, landmarks, and status announcements are tested.
- [ ] `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` states are programmatically distinguishable.
- [ ] Generalized, restricted, stale, conflicted, withdrawn, and error states do not rely on color alone.
- [ ] Non-map parity is tested for public-safe Fauna feature inspection.
- [ ] Sensitive-detail leak guards cover DOM, accessibility tree, logs, traces, snapshots, screenshots, and artifacts as applicable.
- [ ] Fixtures are synthetic/public-safe, deterministic, rights-aware, and no-network.
- [ ] Valid, invalid, denied, abstained, quarantined-boundary, and error scenarios are executable.
- [ ] Zero collection, unexpected skips, unexpected network access, and TODO-only jobs cannot be misreported as proof.
- [ ] CI runs substantive repository-native commands with reviewed triggers and permissions.
- [ ] Coverage gaps, supported environments, and WCAG measurement limits are documented.
- [ ] Human Fauna, accessibility, and sensitivity review is recorded where required.

At the current evidence snapshot, these criteria remain **open** unless a separate executable artifact proves them.

[Back to top](#top)

---

## Evidence ledger

| Evidence location at pinned base | Observation supported |
|---|---|
| `tests/domains/fauna/a11y/README.md` | Existing v0.1 baseline and lane purpose. |
| `tests/README.md` | Canonical test-root authority, mixed maturity, narrow `make test`, TODO-only accessibility workflows, and no-network posture. |
| `tests/domains/fauna/README.md` | Parent Fauna test responsibilities and child-lane boundary. |
| `docs/architecture/directory-rules.md` | Live Directory Rules placement-refresh artifact and unresolved authority-path question. |
| `docs/doctrine/directory-rules.md` | Duplicate/later-numbered Directory Rules presentation artifact; same test-root placement rule. |
| `CONTRIBUTING.md` | Draft-PR default, preservation rules, Directory Rules conflict notice, AI-receipt and validation expectations. |
| `docs/registers/DRIFT_REGISTER.md` | Existing drift register; no target-specific entry was present in the fetched file. |
| `docs/architecture/ui/ACCESSIBILITY.md` | Accessibility as trust-visible governance; WCAG 2.2 AA proposed target; non-map, keyboard, motion, and state requirements. |
| `docs/domains/fauna/MAP_UI_CONTRACTS.md` | Fauna finite outcomes, trust states, badge accessibility, renderer boundary, and geoprivacy requirements. |
| `docs/domains/fauna/SENSITIVITY.md` | Deny-by-default sensitivity and no exact-detail posture. |
| `fixtures/domains/fauna/README.md` | Current documented fixture families and unresolved consumer alignment. |
| `Makefile` | Exact narrow test and validator targets; no Fauna a11y target. |
| `pyproject.toml` | Root pytest configuration and dependency boundary. |
| `package.json` | Root Playwright declaration and placeholder generic test script. |
| `apps/explorer-web/package.json` | Placeholder explorer-web test script. |
| `.github/workflows/accessibility.yml` | Broad-trigger TODO accessibility jobs. |
| `.github/workflows/domain-fauna.yml` | Broad-trigger TODO Fauna jobs. |
| `.github/workflows/README.md` | Workflow inventory, trigger/threat posture, and stub-versus-command-bearing distinction. |

[Back to top](#top)

---

## Open verification register

| Question | Status | Evidence needed |
|---|---|---|
| Are there unindexed or branch-local executable tests for this lane? | `NEEDS VERIFICATION` | Complete tree/read at resulting branch and test collection. |
| Which runner and accessibility library are canonical? | `NEEDS VERIFICATION` | Accepted package scripts, lockfile, executable tests, and CI command. |
| Is axe intended, and where should it be configured? | `NEEDS VERIFICATION` | Dependency and executable integration; the workflow name alone is not proof. |
| Which Fauna UI routes and components are canonical? | `NEEDS VERIFICATION` | Implemented explorer-web/UI code and route/component tests. |
| Which fixture payloads are stable regression anchors? | `NEEDS VERIFICATION` | Exact files, hashes, expected outputs, and consuming tests. |
| Which browser, assistive-technology, viewport, zoom, locale, and motion matrix is supported? | `UNKNOWN` | Accepted accessibility test plan and observed runs. |
| Is WCAG 2.2 AA adopted as a release requirement or only a design target? | `NEEDS VERIFICATION` | Accepted decision, measurement method, and release-gate evidence. |
| Which CI checks are required by branch protection? | `UNKNOWN` | Repository ruleset/branch-protection evidence. |
| When will accessibility.yml and domain-fauna.yml graduate from stubs? | `PROPOSED` work | Owners, commands, fixtures, permissions, negative cases, and rollback plan. |
| Which Directory Rules copy becomes canonical? | `CONFLICTED` / `NEEDS VERIFICATION` | Accepted ADR and synchronized supersession/migration update. |

[Back to top](#top)

---

## Changelog and rollback

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README scaffold for the Fauna accessibility test lane. |
| 2026-07-17 | v0.2 | Repository-grounded maturity refresh; added test-case and scenario profiles, exact command/workflow limits, fixture and sensitivity rules, failure interpretation, passing-suite limits, maintenance rules, evidence ledger, and explicit Directory Rules conflict. |

### Rollback

This is a documentation-only revision. Restore v0.1 by reverting the implementation commit or replacing this file with blob `27779ceb75e90646d80fe4b3d0e116feb84fe609`. A revert changes documentation only; it does not alter tests, fixtures, workflows, policy, UI, data, release state, or publication.

### Re-review triggers

Re-review on the first executable test, runner/dependency change, workflow graduation, fixture-family change, UI trust-state change, WCAG decision, sensitivity-policy change, or Directory Rules authority resolution.

[Back to top](#top)
