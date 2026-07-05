<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/ui/readme
title: Fauna UI Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — UI steward>
  - <PLACEHOLDER — Governed API steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, UI components, routes, validators, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - tests/domains/fauna/ui/drawer/README.md
  - tests/domains/fauna/a11y/README.md
  - tests/domains/fauna/focus/citation/README.md
  - tests/domains/fauna/focus/deny_sensitive/README.md
  - tests/domains/fauna/layers/README.md
  - tests/domains/fauna/tiles/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - docs/architecture/ui/EVIDENCE_DRAWER.md
  - apps/explorer-web/
  - apps/governed-api/
  - packages/ui/
  - packages/maplibre/
  - fixtures/domains/fauna/
  - schemas/contracts/v1/ui/
  - data/receipts/
  - data/proofs/fauna/
  - release/
tags:
  - kfm
  - tests
  - fauna
  - ui
  - map-ui
  - evidence-drawer
  - focus-mode
  - trust-state
  - governed-api
  - accessibility
  - finite-outcome
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna UI Tests

> Parent test-lane contract for proving Fauna UI surfaces are downstream of governed evidence, policy, release, and sensitivity controls, and never become truth, policy, source, or publication authority.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Fui-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Fui-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** parent UI test-lane README; not UI implementation, schema, policy bundle, layer registry, source registry, fixture inventory, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `ui/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed when evidence, policy, release, sensitivity, or UI payload validity is unresolved  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the parent Fauna test lane for **UI behavior**.

It exists to prove that Fauna UI surfaces render only governed, released, public-safe information and that every consequential interaction preserves the KFM trust membrane. Map views, popups, badges, drawers, layer catalog entries, Focus-adjacent controls, screenshots, and exports are downstream carriers. They do not create evidence, policy decisions, releases, or claims.

A mature parent lane should prove:

1. Fauna UI surfaces consume governed APIs and released manifests only.
2. Feature clicks resolve through the Evidence Drawer path or finite negative outcomes.
3. Focus-adjacent UI controls remain bounded by released evidence, citation validation, and sensitivity gates.
4. Trust states are visible, accessible, text-labelled, and not color-only.
5. Sensitive or unreleased Fauna material fails closed before rendering.
6. UI code does not read RAW, WORK, QUARANTINE, internal stores, model runtimes, graph stores, object stores, or direct source data.
7. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/ui/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna UI behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Parent UI lane | `ui/` |
| UI implementation homes | `apps/explorer-web/`, `packages/ui/`, and `packages/maplibre/` when present. |
| Governed API home | `apps/governed-api/` when present. |
| Schema home | `schemas/contracts/v1/ui/` when present. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/`. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second UI implementation home, schema home, evidence store, policy home, layer registry, fixture home, receipt home, proof home, release home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows evidence-resolution, governed API envelope, UI trust-state, accessibility, e2e, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive exact data, live network calls, trust-bearing receipts/proofs, and release decisions from `tests/` | CONFIRMED from current repo docs. |
| Fauna Map UI contract defines what features must satisfy before rendering, clicking, summarizing, exporting, or explaining | CONFIRMED from current repo docs. |
| Fauna Map UI contract says sensitivity is enforced upstream of style and trust-visible states are surfaced | CONFIRMED from current repo docs. |
| Fauna Map UI contract says renderer is downstream and public clients must not read internal lifecycle stores | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual UI components, route names, schemas, fixtures, validators, and CI jobs | NEEDS VERIFICATION. |

This README defines the parent UI test-lane contract. It does not claim that UI components, routes, schemas, fixtures, validators, or CI checks already exist.

---

## 4. Parent UI rule

**Rule:** A Fauna UI surface may render or explain a feature, layer, badge, drawer, Focus-adjacent answer, export, or screenshot only when the upstream governed evidence, policy, release, sensitivity, and manifest conditions are valid for the tested scope.

Tests should fail or require a finite negative outcome when:

- UI reads feature properties as claims;
- popup text, badge text, tile properties, screenshots, or generated summaries replace the Evidence Drawer;
- UI loads unreleased, withdrawn, candidate, work, quarantine, processed, catalog, or internal material as current public truth;
- sensitivity is enforced only through styling or hidden layers;
- trust badges are color-only or inaccessible;
- missing evidence, denied policy, stale source, withdrawn release, or invalid payload silently disappears;
- browser code reads lifecycle/internal stores or model/runtime backends directly;
- Focus-adjacent UI sends raw feature properties or restricted geometry; or
- tests store production evidence, receipts, proofs, releases, source data, or reusable fixture inventories under this path.

Tests may allow `ANSWER` or public rendering only when the fixture is public-safe, policy permits it, citations validate where needed, release state is current, manifests are valid, and the test remains inside its validation scope.

---

## 5. Child lanes

| Child lane | Responsibility | Status boundary |
|---|---|---|
| `drawer/` | Prove click-to-Evidence-Drawer resolution and finite outcomes. | README work may exist in an open PR; executable tests NEEDS VERIFICATION. |
| `layer-catalog/` | Prove layer listing, trust badges, and release state display. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `map-shell/` | Prove public map shell respects trust membrane and lifecycle boundaries. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `focus-panel/` | Prove Focus-adjacent UI sends bounded context and renders citations/denials. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `export/` | Prove exports/screenshots preserve policy, citation, and release constraints. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `trust-badges/` | Prove badges are text-labelled, accessible, and not proof substitutes. | PROPOSED / NEEDS VERIFICATION unless implemented. |

Additional child lanes may be added when they have a clear UI-test responsibility and do not duplicate another authority root.

---

## 6. Parent proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Governed API boundary | UI uses governed routes, not lifecycle/internal stores. | Boundary assertion. |
| Render gate | Feature/layer is released and manifest-backed before public render. | Validation assertion. |
| Click-to-drawer | Consequential click resolves through drawer or finite negative state. | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |
| Sensitive fail-closed | Policy-withheld material does not reach public UI. | `DENY` or non-render. |
| Style not protection | Styling alone cannot make unsafe data public. | Test failure. |
| Trust badges | Rights, sensitivity, review, freshness, release, correction, and source role are text-labelled. | Accessibility/trust-state assertion. |
| Focus context bound | Focus-adjacent UI sends bounded context only. | Context-envelope assertion. |
| Export/screenshot boundary | Exports preserve redaction, citation, and release state. | Export assertion. |
| Negative outcomes | Missing evidence, denied policy, stale support, invalid payload, and withdrawn release remain visible. | Finite outcome surface. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 7. What belongs here

This directory may contain:

- README and parent-lane contract material for Fauna UI tests.
- Tests that call canonical UI, governed API, evidence, policy, release, manifest, and validator code from owning roots.
- Negative tests for direct-store access, style-only sensitivity, popup substitution, missing evidence, denied policy, stale source, invalid payload, withdrawn release, and inaccessible trust states.
- Positive tests for public-safe UI fixtures with required governance references.
- Child-lane READMEs for focused Fauna UI concerns.
- Public-safe test-local examples when they are tiny, deterministic, and not reusable fixture inventory.

## 8. What does not belong here

This directory must not contain UI implementation, route implementation, schemas, production evidence, source records, reusable fixture inventories, receipts, proofs, release decisions, policy definitions, credentials, model prompts, model outputs, production screenshots, production tiles, or default tests that require live network access.

---

## 9. Fixture posture

Reusable fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model UI-governance states rather than include production source material or trust-bearing records.

Expected fixture families include valid public layer UI, valid drawer answer, missing evidence, policy denial, stale support, invalid payload, withdrawn release, hidden-by-style anti-pattern, direct-store anti-pattern, inaccessible trust badge, and bounded Focus context.

---

## 10. Suggested local commands

> [!NOTE]
> Command names, UI test runners, route names, validator names, markers, and CI jobs are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/fauna/ui
pytest tests/domains/fauna/ui/drawer
pytest tests/domains/fauna
npx playwright test --grep fauna
python tools/validate_all.py
```

---

## 11. Open questions

| Question | Status | Notes |
|---|---|---|
| Which UI test runner is canonical for Fauna UI tests? | NEEDS VERIFICATION | Must inspect UI app/package configuration. |
| Which governed routes own layer, drawer, Focus, and export interactions? | NEEDS VERIFICATION | Must inspect API/OpenAPI/router implementation. |
| Which UI schemas are canonical? | NEEDS VERIFICATION | Must inspect `schemas/contracts/v1/ui/`. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared UI trust-state tests live here or under a cross-domain UI test root? | OPEN | This lane should own Fauna-specific expectations only. |

---

## 12. Definition of done

This parent lane is mature when:

- [ ] Fauna UI tests run locally.
- [ ] Active child lanes have executable proof where implementation exists.
- [ ] Direct-store access, style-only sensitivity, popup substitution, missing evidence, denied policy, stale support, invalid payload, withdrawn release, inaccessible trust badge, and bounded Focus context cases are tested.
- [ ] Positive public-safe fixtures prove allowed UI behavior without becoming release approval.
- [ ] Tests call canonical UI/API/evidence/policy/release validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Fauna UI proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 13. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna UI parent test lane. |

---

## 14. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for evidence/API/UI/e2e/domain tests, and Fauna Map UI doctrine; executable tests, fixtures, UI components, routes, schemas, validators, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
