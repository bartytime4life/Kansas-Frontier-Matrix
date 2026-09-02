<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/visual/readme
title: Fauna Visual Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — UI steward>
  - <PLACEHOLDER — Release steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, visual baselines, screenshot artifacts, test runners, validators, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - tests/domains/fauna/ui/README.md
  - tests/domains/fauna/a11y/README.md
  - tests/domains/fauna/layers/README.md
  - tests/domains/fauna/tiles/README.md
  - tests/domains/fauna/release/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - apps/explorer-web/
  - apps/governed-api/
  - packages/ui/
  - packages/maplibre/
  - fixtures/domains/fauna/
  - data/published/layers/fauna/
  - artifacts/
  - release/
tags:
  - kfm
  - tests
  - fauna
  - visual
  - visual-regression
  - map-ui
  - layer-rendering
  - trust-state
  - release-state
  - screenshot
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna Visual Tests

> Test-lane contract for proving public Fauna visual surfaces do not silently change after release, do not hide trust-state regressions, and do not treat screenshots or rendered maps as truth authority.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Fvisual-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Fvisual-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** visual test-lane README; not a screenshot archive, UI implementation, renderer implementation, layer registry, release manifest, fixture inventory, receipt, proof, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `visual/`  
**Default posture:** public-safe fixtures; no-network by default; deterministic viewport; finite outcomes; fail closed when visual state depends on unresolved evidence, policy, release, or sensitivity state  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Fauna domain test lane for **visual regression behavior**.

It exists to prove that public Fauna visual surfaces remain stable after release and that changes to maps, layers, legends, badges, drawers, time-state surfaces, and correction/rollback notices are deliberate, reviewable, and traceable. Visual tests verify downstream presentation; they do not create evidence, decide policy, approve release, or publish screenshots as truth.

A mature lane should prove:

1. Public Fauna layer visuals do not silently change after release.
2. Trust-state badges and negative states remain visible and text-supported.
3. Redacted/generalized public-safe renderings do not regress into policy-withheld detail.
4. Stale, withdrawn, superseded, denied, or restricted states remain visibly distinct.
5. Visual snapshots are tied to deterministic public-safe fixtures and viewport settings.
6. Screenshot artifacts are review aids only; they are not evidence, receipts, proofs, releases, or public data.
7. Default tests use no live tile services or source-network calls.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/visual/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna visual-regression behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Test lane | `visual/` |
| UI implementation homes | `apps/explorer-web/`, `packages/ui/`, and `packages/maplibre/` when present. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Published layer/artifact home | `data/published/layers/fauna/` when present. |
| Screenshot/artifact home | `artifacts/` when retained by CI or review tooling. |
| Release home | `release/`. |
| Documentation reference | `docs/domains/fauna/MAP_UI_CONTRACTS.md`. |

> [!WARNING]
> This directory must not become a second screenshot archive, UI implementation home, layer registry, tile store, fixture home, release home, artifact publication home, policy home, receipt home, proof home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows UI trust-state, e2e, accessibility, governed API envelope, release, lifecycle, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive exact data, live network calls, generated build artifacts, trust-bearing receipts/proofs, and release decisions from `tests/` | CONFIRMED from current repo docs. |
| Fauna Map UI contract names visual regression for public Fauna layers under `tests/domains/fauna/visual/` | CONFIRMED from current repo docs. |
| Fauna Map UI contract says renderer outputs, screenshots, dashboards, and layers are downstream carriers | CONFIRMED from current repo docs. |
| Fauna Map UI contract requires sensitivity/freshness gates and correction/rollback visibility | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual visual baseline location, screenshot retention policy, test runner, fixtures, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that visual tests, baselines, fixtures, screenshot artifacts, runners, or CI checks already exist.

---

## 4. Visual rule

**Rule:** A Fauna visual snapshot may pass only when the rendered public surface is derived from governed public-safe fixtures, displays required trust and release state, avoids policy-withheld detail, and remains traceable to the tested manifest/release context.

Tests should fail or require review when:

- visual output changes without an approved fixture, manifest, style, release, or expected-snapshot change;
- a visual surface hides, drops, or color-only encodes trust state;
- policy-withheld detail becomes visible through layer style, tile state, symbol density, labels, hover, popup, selection effect, or export;
- stale, withdrawn, superseded, denied, restricted, or generalized states are visually indistinguishable from current public truth;
- a screenshot is treated as evidence, a release artifact, or a proof;
- a baseline uses live source/network data or production-only services;
- candidate or unreleased layer state is rendered in the public visual path; or
- tests store production screenshots, released artifacts, receipts, proofs, or source data under this path.

Tests may allow a visual baseline only when the fixture is public-safe, deterministic, policy-permitted, release-aware, and scoped to the validation purpose.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Baseline determinism | Fixture, viewport, time window, and render options are stable. | Reproducible snapshot. |
| Public-safe rendering | Visual state does not expose policy-withheld detail. | Snapshot assertion or denial. |
| Trust-state visibility | Badges/notices are present and text-labelled. | Visual + accessibility assertion. |
| Release state | Withdrawn/superseded/corrected state is distinct from current truth. | Correction-aware visual state. |
| Stale state | Stale data is labelled and not silently current. | `SOURCE_STALE` visual state. |
| Redaction/generalization | Public-safe derivative remains visibly bounded. | Generalized-state assertion. |
| Popup/drawer continuity | Visual state links to drawer/trust detail and does not replace it. | UI assertion. |
| Screenshot boundary | Screenshot artifact is not evidence/release/proof. | Placement/metadata assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Fauna visual tests.
- Tests that call canonical UI, map, layer, tile, release, policy, accessibility, and fixture code from owning roots.
- Negative visual tests for hidden trust states, style-only sensitivity, stale-state disappearance, release-withdrawal disappearance, popup substitution, export leaks, and unreleased layer rendering.
- Positive visual tests for public-safe Fauna layer fixtures with required governance references.
- Small test-local expected-state declarations when they are documented and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain UI implementation, renderer implementation, production screenshots, production tiles, released artifacts, reusable fixture inventories, source records, receipts, proofs, release decisions, policy definitions, credentials, model prompts, model outputs, or default tests that require live network access.

---

## 8. Fixture and artifact posture

Reusable fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Visual test output, if retained by CI or review tooling, should normally live under the appropriate `artifacts/` path and should remain clearly marked as generated review material, not evidence or release authority.

Expected fixture families include valid public layer, generalized public layer, stale layer, withdrawn release, superseded release, denied layer, restricted/generalized notice, popup-to-drawer continuity, hidden-by-style anti-pattern, and export/screenshot boundary.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, visual test runners, browser engines, markers, artifact paths, and CI jobs are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/fauna/visual
pytest tests/domains/fauna/ui
npx playwright test --grep fauna
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| Which visual test runner is canonical? | NEEDS VERIFICATION | Must inspect UI app/package configuration. |
| Where are visual baselines stored, if any? | NEEDS VERIFICATION | Must inspect test and artifact conventions. |
| Which screenshot artifacts may CI retain? | NEEDS VERIFICATION | Must inspect workflow retention policy. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which public Fauna layer states need visual coverage first? | NEEDS VERIFICATION | Must inspect release/layer manifests. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared cross-domain visual tests live here or under a cross-domain UI/visual root? | OPEN | This lane should own Fauna-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Fauna visual tests run locally.
- [ ] Deterministic public-safe fixtures and viewport/time settings are declared.
- [ ] Valid public layer, generalized layer, stale layer, withdrawn/superseded release, denied/restricted state, popup-to-drawer continuity, and hidden-by-style anti-pattern cases are tested.
- [ ] Screenshots and baselines are stored only where repository policy allows and are labelled as generated review artifacts.
- [ ] Tests call canonical UI/map/release/policy fixtures rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Fauna visual proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna visual test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for UI/e2e/accessibility/release/domain tests, and Fauna Map UI visual-regression doctrine; executable tests, fixtures, visual baselines, screenshot artifacts, runners, validators, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
