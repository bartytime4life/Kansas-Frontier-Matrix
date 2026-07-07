<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-ui-readme
title: UI Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - UI steward
  - OWNER_TBD - Accessibility steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; ui; synthetic-only; no-network; trust-visible; evidence-bounded; release-gated; accessibility-aware
tags: [kfm, tests, fixtures, ui, evidence-drawer, focus-mode, trust-badges, accessibility, finite-outcomes, no-network, ANSWER, ABSTAIN, DENY, ERROR, rollback]
related:
  - ../README.md
  - ../../README.md
  - ../../../contracts/ui/README.md
  - ../../../packages/ui/README.md
  - ../../../apps/explorer-web/src/features/evidence_drawer/README.md
  - ../../../apps/explorer-web/src/features/focus_panel/README.md
  - ../../../apps/explorer-web/src/features/trust_header/README.md
  - ../../../docs/architecture/ui/EVIDENCE_DRAWER.md
  - ../../../docs/architecture/ui/FOCUS_FLOW.md
  - ../../../docs/architecture/ui/TRUST_BADGES.md
  - ../../../schemas/contracts/v1/ui/
  - ../../../policy/ui/
  - ../../../release/
notes:
  - "This README replaces placeholder content at tests/fixtures/ui/README.md."
  - "This lane documents unit-test-scoped UI fixtures. It is not UI implementation, component source, contract authority, schema authority, policy authority, evidence storage, release approval, or public UI routing."
  - "UI fixtures must preserve trust-visible state, finite outcomes, evidence/citation posture, policy posture, release state, correction lineage, rollback posture, and accessibility expectations."
  - "Executable tests, payload inventory, schema bindings, app/component wiring, accessibility checks, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI test fixtures

> Unit-test-scoped fixture lane for synthetic UI payload, trust-state, accessibility, and finite-outcome examples under `tests/fixtures/ui/`. These fixtures help test how UI surfaces preserve governed state without becoming UI implementation, source truth, evidence closure, policy approval, release approval, or public-routing authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: UI fixtures" src="https://img.shields.io/badge/lane-ui__fixtures-purple">
  <img alt="Posture: trust visible" src="https://img.shields.io/badge/posture-trust__visible-0a7ea4">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/ui/README.md`  
**Status:** draft / placeholder replaced / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/ui`  
**Default posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED `tests/fixtures/` is unit-test-scoped by repo doctrine; CONFIRMED UI contracts and package docs preserve the boundary that UI consumes governed state and is not truth, policy, schema, release, or implementation authority; NEEDS VERIFICATION for fixture payload inventory, executable tests, schemas, app/component wiring, accessibility checks, CI coverage, and pass rates.

---

## Scope

Use `tests/fixtures/ui/` for small synthetic fixtures that exercise UI-facing trust behavior.

In scope:

- Evidence Drawer payload examples;
- Focus request/response and finite-outcome examples;
- trust badge, caveat, stale, corrected, withdrawn, rollback, and no-data display states;
- accessibility label and non-color-state canaries;
- policy-denied, abstention, error, redacted, generalized, and review-required examples;
- test-local manifests that explain expected UI outcomes without carrying real source, evidence, release, or policy records.

Out of scope:

- UI component source code;
- app routing, state management, CSS, design tokens, or build configuration;
- contract meaning, schema definitions, or policy rules;
- real EvidenceBundles, proofs, receipts, release records, or source payloads;
- public screenshots, exports, tiles, styles, or rendered-map artifacts.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Unit-test-scoped UI fixtures | `tests/fixtures/ui/` | This lane. |
| UI semantic contracts | `contracts/ui/` | Defines meaning; not owned here. |
| UI schemas | `schemas/contracts/v1/ui/` or accepted schema homes | Defines machine shape; not owned here. |
| UI policy | `policy/ui/` and related policy roots | Admissibility authority; not owned here. |
| Shared component implementation | `packages/ui/` | Implementation/package source; not owned here. |
| Deployable UI app | `apps/explorer-web/` or accepted app roots | Consumer surface; not owned here. |
| Release/correction/rollback authority | `release/` and release contracts | Publication control; not owned here. |
| Cross-cutting reusable fixtures | `fixtures/` root if accepted | Shared fixture home; this lane remains test-local. |

> [!IMPORTANT]
> This fixture lane must not become a UI implementation home, schema home, policy home, contract home, evidence/proof store, release store, screenshot archive, public app route, or direct model-output transport.

---

## Fixture rule

UI fixtures are downstream test carriers. They should prove that UI-facing payloads preserve governed state and fail closed when support is missing.

Core expectations:

| Expectation | Required posture |
|---|---|
| Synthetic only | Use toy IDs, toy refs, toy labels, toy timestamps, and review-safe values. |
| No-network default | No live API, source, tile, style, glyph, sprite, model, or public-service calls. |
| Governed payload boundary | UI fixtures model governed API/runtime payloads, not direct lifecycle-store reads. |
| Finite outcomes | Expected outcomes remain explicit: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or validation failure. |
| Trust visibility | Evidence, policy, release, review, correction, rollback, caveat, and stale states stay visible where material. |
| Accessibility | Trust state must not be color-only; labels and assistive-state expectations are explicit where UI-facing. |
| Sensitive fail-closed | Redacted, generalized, denied, restricted, or withheld examples do not expose the protected value. |

---

## Expected fixture families

| Family | Purpose | Expected posture |
|---|---|---|
| `evidence_drawer_valid` | Evidence Drawer state with refs, caveats, and citation posture. | `ANSWER` / `PASS`. |
| `evidence_drawer_missing_support` | Drawer lacks evidence or citation support. | `ABSTAIN`. |
| `focus_answer_valid` | Focus response can render evidence-backed answer state. | `ANSWER`. |
| `focus_uncited_abstain` | Focus response blocks unsupported answer. | `ABSTAIN`. |
| `policy_denied_banner` | UI shows denial state without leaking restricted detail. | `DENY`. |
| `stale_or_withdrawn_label` | UI marks stale, corrected, withdrawn, or superseded state. | `PASS`. |
| `rollback_visible` | UI exposes rollback/correction path where material. | `PASS`. |
| `trust_badges_accessible` | Trust badges include text/assistive labels, not color-only state. | `PASS`. |
| `redacted_value_hidden` | Redacted/generalized state is safe and labelled. | `DENY` / `PASS`. |
| `direct_store_access_forbidden` | Browser/client fixture attempts forbidden direct internal read. | validation failure / `DENY`. |

---

## Accepted inputs

Accepted material is limited to compact, synthetic, reviewable examples, such as:

- small `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` fixture notes;
- toy `EvidenceDrawerPayload`, Focus response, RuntimeResponseEnvelope, PolicyDecision, ReleaseManifest, CorrectionNotice, and RollbackCard refs;
- toy accessibility labels, trust badges, caveats, and status text;
- expected outcome and reason-code notes for `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or validation failure;
- links to consumer tests once those tests are verified.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| UI component source, CSS, state management, design tokens, or stories | `packages/ui/`, `apps/explorer-web/`, or accepted UI roots |
| semantic contract definitions | `contracts/ui/` |
| schema definitions | `schemas/contracts/v1/ui/` or accepted schema homes |
| policy rules | `policy/` roots |
| EvidenceBundle records, proofs, receipts, or source records | governed evidence/proof/data roots |
| release manifests, correction notices, rollback cards | `release/` and release contract roots |
| screenshots, retained CI outputs, public exports, tiles, styles, or map artifacts | governed artifact/release roots only after release |
| secrets, production logs, private endpoints, raw/canonical-store values, or direct model output | not allowed in repository fixtures |

---

## Suggested layout

```text
tests/fixtures/ui/
|-- README.md
|-- evidence_drawer.valid.json
|-- evidence_drawer_missing_support.abstain.json
|-- focus_answer.valid.json
|-- focus_uncited.abstain.json
|-- policy_denied_banner.deny.json
|-- stale_or_withdrawn_label.valid.json
|-- rollback_visible.valid.json
|-- trust_badges_accessible.valid.json
|-- redacted_value_hidden.deny.json
`-- direct_store_access_forbidden.invalid.json
```

The layout is PROPOSED until payload files and consumers exist.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/ui tests/fixtures/ui
```

Default runs should be deterministic, local, no-network, public-safe, and finite-outcome only.

---

## Maintenance checklist

- [ ] Keep examples synthetic, public-safe, compact, and reviewable.
- [ ] Make evidence, policy, release, review, correction, rollback, caveat, and accessibility posture explicit where material.
- [ ] Use `ABSTAIN`, `DENY`, or `ERROR` for missing evidence, denied policy, restricted detail, stale/withdrawn state, invalid payloads, or forbidden direct-store access.
- [ ] Do not store UI implementation, schemas, contracts, policies, release records, evidence records, screenshots, public artifacts, secrets, raw/canonical-store values, or direct model output here.
- [ ] Link to consumer tests only after verification.
- [ ] Update this README when payloads, schemas, tests, app/component wiring, or accessibility checks are verified.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; placeholder replaced. |
| UI contract boundary | CONFIRMED as semantic-contract lane, not implementation authority. |
| UI package boundary | CONFIRMED as shared component package, not truth source. |
| Fixture payload inventory | NEEDS VERIFICATION. |
| Consumer tests | NEEDS VERIFICATION. |
| Schema bindings | NEEDS VERIFICATION. |
| App/component wiring | NEEDS VERIFICATION. |
| Accessibility checks | NEEDS VERIFICATION. |
| Runner and CI wiring | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
