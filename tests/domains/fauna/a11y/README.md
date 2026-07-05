<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/a11y/readme
title: Fauna Accessibility Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Accessibility steward>
  - <PLACEHOLDER — UI steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Governance reviewer>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, UI components, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/SENSITIVITY.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - fixtures/domains/fauna/
  - schemas/contracts/v1/domains/fauna/
  - schemas/contracts/v1/ui/
  - packages/ui/
  - packages/maplibre/
  - apps/explorer-web/
  - apps/governed-api/
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
] -->

<a id="top"></a>

# Fauna Accessibility Tests

> Test-lane contract for proving Fauna UI and map surfaces remain accessible while preserving KFM's Fauna sensitivity, geoprivacy, evidence, and finite-outcome boundaries.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Fa11y-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Fa11y-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: public--safe](https://img.shields.io/badge/posture-public--safe-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** accessibility test-lane README; not a UI implementation, schema, policy bundle, fixture inventory, source registry, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `a11y/`  
**Default posture:** accessibility without sensitivity downgrade; deterministic public-safe fixtures; no-network by default  
**Last reviewed:** 2026-07-05

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Status and evidence boundary](#3-status-and-evidence-boundary)
4. [Accessibility rule](#4-accessibility-rule)
5. [What belongs here](#5-what-belongs-here)
6. [What does not belong here](#6-what-does-not-belong-here)
7. [Accessibility proof matrix](#7-accessibility-proof-matrix)
8. [Fixture posture](#8-fixture-posture)
9. [Expected outcomes](#9-expected-outcomes)
10. [Lifecycle and publication boundaries](#10-lifecycle-and-publication-boundaries)
11. [No-network default](#11-no-network-default)
12. [Suggested local commands](#12-suggested-local-commands)
13. [Review burden](#13-review-burden)
14. [Related folders and files](#14-related-folders-and-files)
15. [Open questions](#15-open-questions)
16. [Definition of done](#16-definition-of-done)
17. [Changelog](#17-changelog)
18. [Last reviewed](#18-last-reviewed)

---

## 1. Purpose

This directory is the Fauna domain test lane for **accessibility** behavior.

It exists to prove that Fauna-facing UI surfaces can be navigated, understood, and checked by users who rely on keyboard navigation, screen readers, visible focus, text alternatives, readable status messages, and non-visual trust cues.

A mature lane should support these claims:

1. **Accessible does not mean over-disclosed.** Accessibility labels, alt text, titles, tables, focus states, tooltips, popups, and evidence drawers must not expose details that policy withholds.
2. **Trust state is perceivable.** Generalized, restricted, denied, stale, abstained, and error states are visible and non-visually available.
3. **Keyboard paths work.** Fauna map controls, layer toggles, feature lists, evidence drawers, and Focus Mode controls can be reached and exited without a pointing device.
4. **Finite outcomes are announced.** `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` states have clear accessible names or descriptions.
5. **Fixtures are public-safe.** Accessibility tests use generalized, synthetic, or approved public-safe fixture records.
6. **Tests remain tests.** This lane verifies UI/accessibility behavior; it does not implement UI components or decide release policy.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/a11y/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna accessibility behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Test lane | `a11y/` |
| UI implementation homes | `packages/ui/`, `packages/maplibre/`, `apps/explorer-web/` as applicable. |
| Governed API home | `apps/governed-api/` as applicable. |
| Domain doctrine home | `docs/domains/fauna/` |
| Policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/` |
| Schema homes | `schemas/contracts/v1/domains/fauna/` and `schemas/contracts/v1/ui/` when present. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Release/proof homes | `release/`, `data/receipts/`, and `data/proofs/` |

> [!WARNING]
> This directory must not become a second UI, policy, fixture, proof, release, or source-data home. It verifies accessibility behavior against governed Fauna UI and policy boundaries.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows e2e, UI trust-state, and accessibility paths | CONFIRMED from current repo docs. |
| `tests/README.md` says sensitive Fauna coordinates are excluded from test trees | CONFIRMED from current repo docs. |
| Fauna sensitivity doc explains deny-by-default and geoprivacy posture | CONFIRMED from current repo docs. |
| Fauna map UI contracts describe map, Evidence Drawer, Focus Mode, sensitivity gates, trust states, and tests | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual UI component names and route names | NEEDS VERIFICATION. |
| Actual fixtures and fixture manifests | NEEDS VERIFICATION. |
| Actual accessibility tooling and CI job names | NEEDS VERIFICATION. |

This README defines the accessibility test-lane contract. It does not claim that components, routes, fixtures, test runners, or CI checks already exist.

---

## 4. Accessibility rule

**Rule:** Fauna accessibility tests must make trust state perceivable without making withheld Fauna details discoverable.

Accessibility support must not:

- expose policy-withheld details in labels, alt text, descriptions, hidden text, DOM attributes, snapshots, logs, fixtures, screenshots, traces, or test reports;
- make a generalized map feature sound like exact feature truth;
- hide policy denial or abstention from assistive technology;
- rely on color alone for sensitivity, review, freshness, or evidence status;
- use style-only hiding as a protection mechanism; or
- treat a passing accessibility test as publication approval.

Accessibility support should:

- provide accessible names and descriptions for layer toggles, trust badges, denial states, evidence drawers, feature lists, filters, legends, and Focus Mode controls;
- preserve keyboard access and visible focus order;
- announce finite outcomes clearly;
- provide non-color trust indicators; and
- use public-safe fixture records.

---

## 5. What belongs here

This directory may contain:

- README and lane contract material for Fauna accessibility tests.
- Keyboard-navigation tests for Fauna layer controls, legends, feature lists, evidence drawers, and Focus Mode paths.
- Accessibility-tree tests for Fauna trust states and finite outcomes.
- Tests that ensure denial, abstention, generalized status, restricted access, stale source, and evidence-missing states are perceivable.
- Tests that ensure accessibility text does not expose policy-withheld details.
- Tests that verify UI controls do not rely on color alone for policy or evidence state.
- Tests that use public-safe Fauna fixtures from the fixture root or documented tiny local examples.
- Tests that call UI, MapLibre, and governed API code from their owning roots.

---

## 6. What does not belong here

This directory must not contain:

- UI implementation code.
- Production map styles, tile artifacts, layer manifests, or public UI payloads.
- Raw Fauna source records, sensitive geometry, private steward records, or unreleased candidate data.
- Policy definitions, schema definitions, source registry records, receipts, proofs, release decisions, or rollback decisions.
- Reusable fixture inventories that belong under `fixtures/domains/fauna/`.
- Accessibility snapshots or reports that include policy-withheld details.
- Tests that require live network access by default.

[↑ Back to top](#top)

---

## 7. Accessibility proof matrix

| Test concern | Required proof | Preferred lane behavior |
|---|---|---|
| Keyboard navigation | User can reach and exit Fauna controls, drawers, lists, and Focus Mode paths. | Deterministic local UI test. |
| Visible focus | Focus is visible and ordered through Fauna controls. | UI/a11y assertion. |
| Accessible names | Layer toggles, buttons, badges, and drawers have meaningful names. | DOM/a11y-tree assertion. |
| Trust states are perceivable | Generalized, denied, restricted, stale, and evidence-missing states are not color-only. | UI trust-state assertion. |
| Finite outcomes announced | `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` are exposed to assistive technology. | Runtime/envelope UI assertion. |
| Evidence Drawer access | Evidence controls are reachable when allowed. | Keyboard and a11y assertion. |
| Denial reason access | Denial/abstention reasons are accessible without withheld detail. | Negative-state UI assertion. |
| Sensitive detail withheld | Labels, DOM attributes, logs, and snapshots do not include withheld details. | Fixture/snapshot guard. |
| Map interaction parity | Non-pointer users can inspect public-safe Fauna records through list/table or equivalent governed surface. | UI/e2e assertion. |
| No-network default | Tests use local fixtures and do not fetch live sources. | Test harness guard. |

---

## 8. Fixture posture

Reusable Fauna accessibility fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Fixture requirements:

- public-safe by construction;
- no policy-withheld location detail;
- no private steward identifiers;
- no unreleased source payloads;
- deterministic and no-network;
- clear expected trust state; and
- clear expected finite outcome.

Expected fixture families include public-safe, generalized, denied, restricted, evidence-missing, stale-source, and map-list parity examples.

Tiny local examples may be used only when they are not reusable fixture records and are documented as test-local.

---

## 9. Expected outcomes

Fauna accessibility tests should prefer finite, inspectable outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

| Condition | Preferred outcome |
|---|---|
| Public-safe feature with evidence | `ANSWER` with accessible evidence controls. |
| Evidence missing | `ABSTAIN` or accessible evidence-missing state. |
| Policy denies detail | `DENY` with accessible reason and no withheld detail. |
| UI/accessibility wiring failure | Test failure. |
| Fixture includes withheld detail | Test setup failure or quarantine of fixture. |
| Live fetch attempted in default test | Test failure. |

---

## 10. Lifecycle and publication boundaries

This lane supports KFM verification but does not move records through the lifecycle:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Boundary | Rule |
|---|---|
| RAW | Do not store raw Fauna records here. |
| WORK / QUARANTINE | Do not store candidate or quarantined records here. |
| PROCESSED | Do not store processed Fauna products here. |
| CATALOG / TRIPLET | Do not treat test fixtures or snapshots as catalog truth. |
| PUBLISHED | Accessibility tests never publish. |
| RECEIPTS / PROOFS | Do not store trust-bearing receipts or proofs here. |
| RELEASE | Release decisions remain under `release/`. |

A passing accessibility test proves UI behavior for the tested scenario. It is not release approval or proof that a Fauna record is safe to publish.

---

## 11. No-network default

Default Fauna accessibility tests must avoid:

- live source services;
- internet access;
- live map tiles or geocoding;
- local credential files;
- developer machine caches;
- mutable upstream API responses; and
- direct source-system side effects.

Live or integration checks, if ever needed, should be explicitly marked and excluded from the default suite.

---

## 12. Suggested local commands

> [!NOTE]
> Command names, accessibility tools, browser runners, markers, and CI jobs are **NEEDS VERIFICATION** until checked against the actual repository configuration.

Likely lane check:

```bash
pytest tests/domains/fauna/a11y
```

Possible broader Fauna domain check:

```bash
pytest tests/domains/fauna
```

Possible UI/e2e checks if configured:

```bash
npm test -- --grep fauna
npx playwright test --grep fauna
```

Possible repo-wide validation command if implemented:

```bash
python tools/validate_all.py
```

---

## 13. Review burden

Reviewers should be able to answer:

- Does the test verify accessibility behavior without becoming UI implementation?
- Are accessible names, descriptions, focus order, and trust states tested?
- Are denial, abstention, restriction, and error states accessible without withheld detail?
- Do labels, hidden text, snapshots, logs, and fixtures avoid withheld details?
- Are fixtures deterministic, public-safe, and no-network?
- Are policy, schema, source registry, receipts, proofs, release decisions, and production code kept in their canonical roots?
- Are route/component/tooling/CI gaps marked **NEEDS VERIFICATION** rather than claimed?

---

## 14. Related folders and files

| Path | Relationship | Status from current evidence |
|---|---|---|
| `tests/README.md` | Root test contract and accessibility/e2e allowance. | CONFIRMED. |
| `docs/doctrine/directory-rules.md` | Domain segment rule for `tests/domains/<domain>/`. | CONFIRMED. |
| `docs/domains/fauna/SENSITIVITY.md` | Fauna sensitivity and geoprivacy posture. | CONFIRMED. |
| `docs/domains/fauna/MAP_UI_CONTRACTS.md` | Fauna map UI, Evidence Drawer, Focus Mode, trust states, and tests. | CONFIRMED. |
| `fixtures/domains/fauna/` | Reusable public-safe fixture home. | Inventory NEEDS VERIFICATION. |
| `policy/sensitivity/fauna/` | Binding sensitivity policy home. | Behavior NEEDS VERIFICATION. |
| `policy/domains/fauna/` | Domain policy home. | Behavior NEEDS VERIFICATION. |
| `schemas/contracts/v1/ui/` | UI payload schema home when present. | NEEDS VERIFICATION. |
| `packages/ui/`, `packages/maplibre/`, `apps/explorer-web/` | UI implementation homes when present. | NEEDS VERIFICATION. |
| `apps/governed-api/` | Governed API envelope home when present. | NEEDS VERIFICATION. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| Which accessibility runner is canonical? | NEEDS VERIFICATION | Playwright, axe, pytest, or another configured tool must be verified. |
| Which UI routes/components are canonical for Fauna map, Evidence Drawer, and Focus Mode? | NEEDS VERIFICATION | Do not invent route or component names. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which CI job runs Fauna accessibility tests? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should cross-domain accessibility tests live here or in a UI/e2e root? | OPEN | This lane should own Fauna-specific assertions; shared UI assertions may belong elsewhere. |
| Which WCAG version/level is the project standard? | NEEDS VERIFICATION | Do not declare conformance level without repo evidence. |

---

## 16. Definition of done

This lane is mature when:

- [ ] Fauna accessibility tests run locally.
- [ ] Keyboard navigation and visible focus are tested for Fauna surfaces.
- [ ] Accessible names/descriptions exist for Fauna layer, feature, evidence, and Focus Mode controls.
- [ ] Trust states are perceivable without color-only cues.
- [ ] Denial, abstention, restriction, and error states are accessible without withheld detail.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] Tests call canonical UI/API components rather than redefining behavior locally.
- [ ] CI exposes the Fauna accessibility proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna accessibility test lane. |

---

## 18. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for accessibility/e2e paths, Fauna sensitivity posture, and Fauna map UI contracts; executable tests, fixtures, UI route/component names, accessibility tooling, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
