<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-ui-readme
title: UI Tests README
type: test-readme
version: v0.1
status: draft; greenfield-stub-replaced; ui-test-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Test steward
  - OWNER_TBD - UI steward
  - OWNER_TBD - Accessibility steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public-doc; tests; ui; trust-state; accessibility; finite-outcomes; no-network; synthetic-only; evidence-aware; policy-aware; release-gated
tags: [kfm, tests, ui, trust-state, EvidenceDrawerPayload, FocusMode, MapContextEnvelope, RuntimeResponseEnvelope, accessibility, finite-outcomes, release-state, rollback, correction, ANSWER, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../fixtures/README.md
  - ../fixtures/ui/README.md
  - ../../contracts/ui/README.md
  - ../../packages/ui/README.md
  - ../../apps/explorer-web/README.md
  - ../../apps/governed-api/README.md
  - ../../docs/architecture/ui/README.md
  - ../../docs/architecture/ui/EVIDENCE_DRAWER.md
  - ../../docs/architecture/ui/FOCUS_FLOW.md
  - ../../schemas/contracts/v1/ui/
  - ../../policy/ui/
  - ../../release/
notes:
  - "This README replaces the greenfield stub at tests/ui/README.md."
  - "This lane documents executable UI trust-state tests. It is not UI implementation, fixture storage, contract authority, schema authority, policy authority, release approval, evidence storage, or public app routing."
  - "UI tests should prove trust-visible rendering, finite outcomes, no-leak posture, accessibility behavior, and correction/rollback visibility from governed payloads."
  - "Executable test inventory, actual runner/framework, fixture consumption, schema bindings, app/component wiring, accessibility tooling, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI tests

> Test-lane README for UI trust-state, component, accessibility, and negative-behavior checks under `tests/ui/`. This lane proves that UI surfaces render governed state faithfully without becoming UI implementation, source truth, evidence closure, policy approval, release approval, or public artifact authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: UI tests" src="https://img.shields.io/badge/lane-ui__tests-purple">
  <img alt="Posture: trust visible" src="https://img.shields.io/badge/posture-trust__visible-0a7ea4">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/ui/README.md`  
**Status:** draft / greenfield stub replaced / UI test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `ui`  
**Fixture companion:** `tests/fixtures/ui/`  
**Default posture:** deterministic, synthetic, no-network, public-safe UI tests only  
**Truth posture:** CONFIRMED target file existed as a greenfield stub before replacement; CONFIRMED `tests/README.md` lists `tests/ui/` as UI trust-state component tests; CONFIRMED UI semantic contracts and `packages/ui/` preserve the boundary that UI renders governed state and is not truth, policy, schema, release, or source authority; CONFIRMED `tests/fixtures/ui/` exists as a fixture companion lane; NEEDS VERIFICATION for executable tests, runner/framework, fixture consumption, schema bindings, component/app wiring, accessibility tooling, CI coverage, and pass rates.

---

## Scope

Use `tests/ui/` for executable checks that verify UI trust-state behavior.

In scope:

- Evidence Drawer rendering tests;
- Focus Mode and governed answer-state UI tests;
- finite outcome display tests for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
- trust badge, caveat, stale, corrected, withdrawn, superseded, review-required, release-state, and rollback-visibility tests;
- accessibility tests proving trust state is not color-only and is available to assistive technologies;
- no-leak tests for redacted, generalized, denied, restricted, or withheld values;
- tests that verify UI components consume governed payloads and do not read RAW, WORK, QUARANTINE, unpublished candidate, canonical/internal, direct source, or direct model state.

Out of scope:

- UI component source code, design tokens, CSS, app routing, state management, or deployable app code;
- fixture payload collections;
- contract, schema, or policy definitions;
- real EvidenceBundles, receipts, proofs, release records, source payloads, public screenshots, tiles, styles, exports, dashboards, or generated model output.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| UI trust-state executable tests | `tests/ui/` | This lane. |
| UI unit-test fixtures | `tests/fixtures/ui/` | Synthetic inputs; not executable tests. |
| Shared UI components | `packages/ui/` | Implementation/package source; not owned here. |
| Deployable UI app | `apps/explorer-web/` or accepted app roots | App shell and routing; tests may consume. |
| Governed API payloads | `apps/governed-api/` and runtime contracts | Upstream governed state; not owned here. |
| UI semantic contracts | `contracts/ui/` | Object meaning; tests verify. |
| UI machine schemas | `schemas/contracts/v1/ui/` or accepted schema homes | Shape authority; tests reference. |
| UI and runtime policy | `policy/ui/`, `policy/runtime/`, `policy/evidence/`, sensitivity/release roots | Admissibility authority; tests assert behavior. |
| Release/correction/rollback | `release/` | Publication authority; tests verify visibility, not decisions. |
| Cross-cutting fixtures | `fixtures/` | Shared examples; not owned here. |

> [!IMPORTANT]
> `tests/ui/` must not become UI implementation, fixture storage, contract authority, schema authority, policy authority, release approval, evidence/proof storage, screenshot archive, public artifact storage, app routing, or direct model-output transport.

---

## UI-test rule

UI tests prove that downstream UI surfaces render governed state without weakening it.

Core expectations:

| Expectation | Required posture |
|---|---|
| Governed input | UI tests use governed payloads or synthetic stand-ins shaped like governed payloads. |
| Trust visibility | Evidence, policy, release, review, correction, rollback, caveat, stale, and finite-outcome states remain visible where material. |
| Finite outcomes | `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` render distinctly and do not collapse into blank panels, loading states, or generic errors. |
| Accessibility | Trust state is text/label/ARIA-visible and not color-only. |
| No-leak posture | Redacted, generalized, denied, restricted, or withheld values do not appear in rendered output or test snapshots. |
| No direct store access | UI tests fail if a public/component path reads lifecycle/canonical/internal stores, source APIs, or direct model output. |
| Release awareness | Unreleased, withdrawn, superseded, or rollback-missing states do not render as public-current truth. |

---

## Expected test families

| Family | What it proves | Expected outcome |
|---|---|---|
| `evidence_drawer_answer` | Evidence Drawer renders cited, released, policy-allowed support. | `PASS`. |
| `evidence_drawer_abstain` | Missing or stale evidence renders visible abstain state, not filler text. | `PASS` / `ABSTAIN`. |
| `policy_denied_banner` | Denied content displays safe denial posture without leaking restricted details. | `PASS` / `DENY`. |
| `finite_outcomes_render` | `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` have distinct user-visible states. | `PASS`. |
| `trust_badges_accessible` | Trust badges and status labels are accessible and not color-only. | `PASS`. |
| `stale_corrected_withdrawn` | Stale, corrected, withdrawn, and superseded states stay visible. | `PASS`. |
| `rollback_visible` | Rollback/correction path is shown where material. | `PASS`. |
| `redacted_value_hidden` | Redacted/generalized/withheld details are not rendered or snapshot-leaked. | `PASS` / `DENY`. |
| `direct_store_access_forbidden` | UI path cannot fetch RAW/WORK/QUARANTINE/candidate/canonical/internal stores. | validation failure / `DENY`. |
| `direct_model_output_forbidden` | UI/Focus surface cannot render direct model output as truth without governed envelope. | validation failure / `ABSTAIN`. |

---

## Accepted inputs

Accepted material is limited to executable UI tests, lane-local notes, and tiny synthetic inline values when they are too small to justify fixture files.

Preferred input sources:

- `tests/fixtures/ui/` for unit-test-scoped UI fixtures;
- `fixtures/` for shared synthetic examples when accepted;
- `contracts/ui/` for UI payload meaning;
- `schemas/contracts/v1/ui/` for UI payload shape;
- `policy/ui/` and related policy roots for admissibility behavior;
- `release/` for release/correction/rollback references;
- `packages/ui/` and `apps/explorer-web/` only as implementation under test after wiring is verified.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| UI component implementation, CSS, design tokens, app state, stories | `packages/ui/`, `apps/explorer-web/`, or accepted UI roots |
| deployable app routing or shell implementation | `apps/explorer-web/` or accepted app roots |
| fixture payload collections | `tests/fixtures/ui/`, `tests/fixtures/`, or `fixtures/` |
| UI contracts | `contracts/ui/` |
| UI schemas | `schemas/contracts/v1/ui/` |
| UI/runtime/evidence/sensitivity/release policy | `policy/` roots |
| EvidenceBundles, receipts, proofs, source records, lifecycle data | governed `data/` roots |
| release manifests, correction notices, rollback cards | `release/` roots |
| screenshots, visual baselines, public exports, dashboards, tiles, styles, generated artifacts | governed artifact/release roots only when accepted |
| secrets, production logs, real sensitive details, direct model output | not allowed in UI tests |

---

## Suggested layout

```text
tests/ui/
|-- README.md
|-- evidence_drawer_answer.test.PROPOSED
|-- evidence_drawer_abstain.test.PROPOSED
|-- policy_denied_banner.test.PROPOSED
|-- finite_outcomes_render.test.PROPOSED
|-- trust_badges_accessible.test.PROPOSED
|-- stale_corrected_withdrawn.test.PROPOSED
|-- rollback_visible.test.PROPOSED
|-- redacted_value_hidden.test.PROPOSED
|-- direct_store_access_forbidden.test.PROPOSED
`-- direct_model_output_forbidden.test.PROPOSED
```

The layout is schematic. Actual test filenames, extensions, package manager, runner, framework, and accessibility tooling remain NEEDS VERIFICATION.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/ui
```

If the UI stack uses JavaScript or TypeScript tooling, replace this with the repo-confirmed command after package metadata, test runner, and CI ownership are verified.

Default runs should be deterministic, local, no-network, public-safe, finite-outcome-aware, and accessibility-aware.

---

## Maintenance checklist

- [ ] Keep UI implementation in `packages/ui/`, `apps/explorer-web/`, or accepted app roots, not this test lane.
- [ ] Keep fixtures in `tests/fixtures/ui/`, `tests/fixtures/`, or `fixtures/` and reference them from tests.
- [ ] Assert UI never reads RAW, WORK, QUARANTINE, unpublished candidates, canonical/internal stores, source APIs, or direct model output.
- [ ] Assert finite outcomes render distinctly and accessibly.
- [ ] Assert evidence, policy, review, release, correction, rollback, caveat, stale, withdrawn, and superseded states remain visible where material.
- [ ] Assert denied/redacted/generalized/withheld sensitive values do not leak through snapshots, labels, titles, logs, or fallback text.
- [ ] Link tests to fixtures, contracts, schemas, policies, release gates, app/component entrypoints, and accessibility tooling after verification.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; greenfield stub replaced. |
| `tests/ui/` placement | CONFIRMED in `tests/README.md` as UI trust-state component tests. |
| UI contract boundary | CONFIRMED in `contracts/ui/README.md`. |
| UI package boundary | CONFIRMED in `packages/ui/README.md`; implementation depth remains UNKNOWN/NEEDS VERIFICATION. |
| UI fixture companion lane | CONFIRMED at `tests/fixtures/ui/README.md`. |
| Executable test inventory | NEEDS VERIFICATION. |
| Actual runner/framework | NEEDS VERIFICATION. |
| Fixture consumption | NEEDS VERIFICATION. |
| Schema/policy bindings | NEEDS VERIFICATION. |
| App/component wiring | NEEDS VERIFICATION. |
| Accessibility tooling | NEEDS VERIFICATION. |
| CI wiring and pass rates | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
