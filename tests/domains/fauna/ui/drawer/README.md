<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/ui/drawer/readme
title: Fauna UI Drawer Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — UI steward>
  - <PLACEHOLDER — Evidence steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, drawer payload schema, routes, validators, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - tests/domains/fauna/a11y/README.md
  - tests/domains/fauna/focus/citation/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - docs/architecture/ui/EVIDENCE_DRAWER.md
  - fixtures/domains/fauna/
  - schemas/contracts/v1/ui/
  - apps/governed-api/
  - apps/explorer-web/
  - data/receipts/
  - data/proofs/fauna/
  - release/
tags:
  - kfm
  - tests
  - fauna
  - ui
  - drawer
  - evidence-drawer
  - evidence-bundle
  - runtime-response-envelope
  - finite-outcome
  - trust-state
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna UI Drawer Tests

> Test-lane contract for proving Fauna feature clicks resolve through the governed Evidence Drawer path, preserve evidence and policy state, render finite outcomes, and never treat map properties or popups as truth.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Fui%2Fdrawer-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Fui%2Fdrawer-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** UI drawer test-lane README; not UI implementation, drawer schema, evidence store, policy engine, source registry, fixture inventory, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `ui/drawer/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed when evidence, policy, release, or payload validity is unresolved  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Fauna domain test lane for **Evidence Drawer behavior**.

It exists to prove that a clicked Fauna feature, badge, or consequential map claim becomes inspectable only through a governed claim-resolution request. Feature properties, popups, screenshots, layer styles, tiles, and generated text are downstream carriers; they are not evidence and do not replace the drawer.

A mature lane should prove:

1. A click routes through governed claim resolution before the drawer renders.
2. `EvidenceDrawerPayload` preserves evidence, citation, source-role, policy, review, release, correction, transform, and limitation state.
3. `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` are rendered as first-class outcomes.
4. Missing, stale, conflicted, denied, invalid, or withdrawn support does not silently degrade to an answer.
5. Popups and badges may launch the drawer but never replace it.
6. Browser-side code does not read RAW, WORK, QUARANTINE, internal stores, model runtimes, graph stores, object stores, or raw evidence directly.
7. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/ui/drawer/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna Evidence Drawer behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| UI lane | `ui/drawer/` |
| UI implementation homes | `apps/explorer-web/` and shared UI packages when present. |
| Governed API home | `apps/governed-api/` when present. |
| Schema home | `schemas/contracts/v1/ui/` when present. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/`. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second UI implementation home, schema home, evidence store, policy home, fixture home, receipt home, proof home, release home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows evidence-resolution, governed API envelope, UI trust-state, accessibility, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive exact data, live network calls, trust-bearing receipts/proofs, and release decisions from `tests/` | CONFIRMED from current repo docs. |
| Fauna Map UI contract says clicked feature properties are not claims | CONFIRMED from current repo docs. |
| Fauna Map UI contract requires `RuntimeResponseEnvelope` plus `EvidenceDrawerPayload` or typed negative state | CONFIRMED from current repo docs. |
| Evidence Drawer architecture says the drawer is a projection, not a source | CONFIRMED from current repo docs. |
| Evidence Drawer architecture requires finite outcomes and color-independent trust badges | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual drawer payload schema, route names, components, fixtures, validators, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that drawer components, routes, schemas, fixtures, validators, or CI checks already exist.

---

## 4. Drawer rule

**Rule:** A Fauna drawer may render an evidence-bearing answer only when governed claim resolution returns a valid payload whose evidence, policy, review, release, correction, and citation state are complete for the tested scope.

Tests should fail or require a finite negative outcome when:

- a click reads feature properties as a claim;
- a popup, badge, tooltip, screenshot, tile, or generated summary substitutes for the drawer;
- payload schema validation fails;
- evidence references are missing, unresolved, stale, conflicted, unreleased, or withdrawn;
- policy, rights, sensitivity, review, release, correction, or transform state is missing where required;
- the browser reads lifecycle/internal stores or model/runtime backends directly;
- trust badges are color-only or unavailable to keyboard/screen-reader paths;
- a negative state is hidden by closing the drawer or showing a generic empty panel; or
- tests store production evidence, receipts, proofs, release decisions, or source material under this path.

Tests may allow `ANSWER` only when the fixture is public-safe, policy permits it, citations validate, evidence support resolves, release state is current, and the test remains inside its validation scope.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Click boundary | Click produces governed request, not direct claim from feature fields. | API/UI boundary assertion. |
| Payload shape | Drawer payload validates against canonical schema where present. | Schema/validator assertion. |
| Evidence support | Evidence refs resolve or drawer abstains. | `ANSWER` or `ABSTAIN`. |
| Policy gate | Denied policy state renders denial reason. | `DENY`. |
| Invalid payload | Bad shape never renders as answer. | `ERROR`. |
| Release state | Withdrawn/superseded/unreleased support is not current truth. | `ABSTAIN`, `DENY`, `ERROR`, or correction notice. |
| Source role | Drawer preserves source-role and knowledge-character separation. | Projection assertion. |
| Trust badges | Rights, sensitivity, review, freshness, release, correction, and source role are text-labelled. | Accessibility/trust-state assertion. |
| Popup/badge boundary | Popup or badge launches drawer but does not replace it. | UI assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Fauna drawer tests.
- Tests that call canonical drawer, governed API, evidence, policy, release, and validator code from owning roots.
- Negative tests for missing evidence, stale evidence, conflict, denied policy, invalid payload, withdrawn release, popup substitution, and direct-store access.
- Positive tests for public-safe drawer fixtures with required governance references.
- Accessibility checks specific to drawer trust states when they are not already covered by a broader a11y lane.
- Public-safe test-local examples when they are tiny, deterministic, and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain UI implementation, route implementation, schemas, production evidence, source records, reusable fixture inventories, receipts, proofs, release decisions, policy definitions, credentials, model prompts, model outputs, or default tests that require live network access.

---

## 8. Fixture posture

Reusable fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model drawer-governance states rather than include production source material or trust-bearing records.

Expected fixture families include valid answer payload, missing evidence, policy denial, stale support, conflicted support, invalid payload, withdrawn release, popup-only anti-pattern, badge-to-drawer behavior, and color-independent trust badges.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, drawer component names, route names, validator names, markers, and CI jobs are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/fauna/ui/drawer
pytest tests/domains/fauna/ui
pytest tests/domains/fauna
npx playwright test --grep fauna
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the canonical EvidenceDrawerPayload schema/path? | NEEDS VERIFICATION | Must inspect UI schema roots. |
| Which governed route owns click-to-evidence resolution? | NEEDS VERIFICATION | Must inspect API/OpenAPI/router implementation. |
| Which drawer component/test runner exists? | NEEDS VERIFICATION | Must inspect UI app/packages. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared drawer behavior live here or under a cross-domain UI drawer test root? | OPEN | This lane should own Fauna-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Fauna drawer tests run locally.
- [ ] Positive `ANSWER` fixtures prove valid drawer projection behavior.
- [ ] Missing evidence, denied policy, stale support, conflicted support, invalid payload, withdrawn release, popup substitution, direct-store access, and inaccessible trust badges are tested.
- [ ] Tests call canonical drawer/API/evidence/policy/release validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Fauna drawer proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna UI drawer test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for evidence/API/UI/domain tests, and Fauna Evidence Drawer doctrine; executable tests, fixtures, drawer schema, UI components, routes, validators, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
