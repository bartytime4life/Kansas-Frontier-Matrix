<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-readme
title: contracts/ui — UI Contract Semantics README
type: readme
version: v0.2
status: draft; PROPOSED; semantic-contract-lane; map-first; evidence-bounded; trust-membrane; no-implementation-authority
owners: OWNER_TBD — UI steward · Map steward · Evidence steward · Runtime steward · Policy steward · Release steward · Accessibility steward · Contracts steward · Schema steward · Docs steward
created: NEEDS VERIFICATION — stub existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; ui; semantic-contracts; map-first; evidence-bounded; finite-outcomes; accessibility; release-gated; no-sovereign-truth; no-direct-store-access
tags: [kfm, contracts, ui, README, semantic-contracts, map-first, maplibre, evidence-drawer, map-context-envelope, focus-mode, finite-outcomes, trust-membrane, accessibility, policy-filtered, release-state]
related:
  - ../README.md
  - ./evidence_drawer_payload.md
  - ./evidence_drawer_payload/README.md
  - ./map_context_envelope/README.md
  - ../evidence/evidence_drawer_payload.md
  - ../evidence/evidence_bundle.md
  - ../evidence/evidence_ref.md
  - ../runtime/runtime_response_envelope.md
  - ../runtime/decision_envelope.md
  - ../policy/policy_decision.md
  - ../release/release_manifest.md
  - ../../docs/architecture/ui/README.md
  - ../../docs/architecture/ui/EVIDENCE_DRAWER.md
  - ../../docs/architecture/ui/FOCUS_FLOW.md
  - ../../docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - ../../docs/focus-mode/state/map-context-state.md
  - ../../schemas/contracts/v1/ui/
  - ../../policy/ui/
  - ../../policy/runtime/
  - ../../policy/evidence/
  - ../../release/
notes:
  - "Expanded from the short stub at `contracts/ui/README.md`."
  - "UI architecture doctrine describes KFM UI as a map-first, time-aware, evidence-bounded shell that renders released, policy-checked, citation-capable state and is not a sovereign truth surface."
  - "Current session evidence verified a flat UI scaffold for `evidence_drawer_payload.md` and object-folder READMEs for `evidence_drawer_payload/` and `map_context_envelope/`."
  - "This README defines UI semantic-contract boundaries only; UI component code, schemas, policy, fixtures, tests, runtime routes, map rendering, release artifacts, and data lifecycle stores remain in separate roots."
  - "Rollback target for this expansion is previous stub blob SHA `12c0efbe2521663a73c4e0f534dc38f493b59207`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/ui

> Semantic-contract lane for UI-facing KFM object meanings. UI contracts describe what governed UI payloads and envelopes mean at the trust surface. They do not implement components, read canonical stores, validate schemas, execute policy, approve releases, or turn rendered text/maps into sovereign truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts/ui" src="https://img.shields.io/badge/root-contracts%2Fui-blue">
  <img alt="Purpose: semantic meaning" src="https://img.shields.io/badge/purpose-semantic__meaning-blueviolet">
  <img alt="Posture: evidence bounded" src="https://img.shields.io/badge/posture-evidence__bounded-0a7ea4">
  <img alt="Boundary: not implementation" src="https://img.shields.io/badge/boundary-not__implementation-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/ui/README.md`  
**Owning root:** `contracts/` — semantic meaning only  
**Architecture doctrine:** `docs/architecture/ui/README.md` and related UI docs  
**Schema home:** `schemas/contracts/v1/ui/` — NEEDS VERIFICATION per object  
**Policy homes:** `policy/ui/`, `policy/runtime/`, `policy/evidence/`, `policy/sensitivity/`, `policy/release/` or accepted successors  
**Truth posture:** CONFIRMED target was a short stub · CONFIRMED UI architecture doctrine exists · CONFIRMED UI architecture describes the UI as map-first, time-aware, evidence-bounded, released/policy-checked/citation-capable, and not sovereign truth · CONFIRMED UI object-folder guides now exist for EvidenceDrawerPayload and MapContextEnvelope · NEEDS VERIFICATION for canonical UI schema home, validators, fixtures, app/component implementation, runtime/API routes, accessibility tests, policy wiring, and release behavior

## Quick jumps

[Purpose](#purpose) · [UI contract meaning](#ui-contract-meaning) · [Authority split](#authority-split) · [Observed/proposed object families](#observedproposed-object-families) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Trust-surface rules](#trust-surface-rules) · [Validation checklist](#validation-checklist) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`contracts/ui/` is the semantic-contract lane for UI-facing object families that cross the trust membrane or shape public/steward-facing presentation.

It answers:

- what a UI payload, envelope, badge, drawer, focus surface, map-state projection, or trust-visible state means;
- which upstream evidence, runtime, policy, release, review, correction, and accessibility states it must preserve;
- which downstream UI or map surfaces may consume it;
- what it must not assert or expose.

It does not answer:

- how React/Svelte/Vue/plain JavaScript components are implemented;
- how MapLibre renders layers;
- whether source/evidence claims are true;
- whether policy admits display;
- whether release is approved;
- whether schema validation passes;
- whether AI output is correct.

---

## UI contract meaning

A UI contract defines the semantics of payloads and envelopes that UI code receives or emits. It is not UI code.

A mature UI trust flow should look like:

```text
released feature / user selection / governed request
  -> governed API or runtime admission
  -> policy + evidence + citation + review + release checks
  -> finite outcome envelope / UI payload
  -> UI renders trust-visible state
  -> correction / rollback / caveat path remains visible
```

UI contracts must preserve that the renderer is downstream of trust, never upstream of it.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| UI object meaning | `contracts/ui/` | This lane; Markdown semantic contracts only. |
| UI architecture doctrine | `docs/architecture/ui/` | Human-facing architecture and boundary docs. |
| Evidence closure | `contracts/evidence/`, evidence stores/proofs | EvidenceBundle and related contracts own support semantics. |
| Runtime finite outcomes | `contracts/runtime/` | RuntimeResponseEnvelope and DecisionEnvelope own runtime response semantics. |
| Machine shape | `schemas/contracts/v1/ui/` or accepted object-specific schema homes | Schemas own field shape and validation. |
| Policy/admissibility | `policy/ui/`, `policy/runtime/`, `policy/evidence/`, sensitivity/rights/release policy roots | Policy owns allow/deny/restrict/abstain. |
| UI implementation | apps/web/UI/package roots | Component code, CSS, accessibility implementation, and state management live outside contracts. |
| Map rendering | MapLibre/map runtime roots | Renderer implementation stays outside contracts. |
| Fixtures/tests/validators | `fixtures/`, `tests/`, `tools/validators/` | Enforceability stays outside contracts. |
| Release/correction/rollback | `release/` and release contracts | Publication state and rollback are separate. |

---

## Observed/proposed object families

| Object family | Current evidence | Posture |
|---|---|---|
| `EvidenceDrawerPayload` | Flat UI scaffold exists at `contracts/ui/evidence_drawer_payload.md`; object-folder README exists; evidence-family contract also exists and notes placement review. | PROPOSED / PATH NEEDS REVIEW |
| `MapContextEnvelope` | Object-folder README exists; doctrine anchor verified in Focus Mode state docs; flat contract/schema not verified in this session. | PROPOSED / NEEDS VERIFICATION |
| Focus Mode UI payloads | Related to `contracts/focus_mode/` and UI/focus docs. | Boundary must be checked per object. |
| Trust badges / caveats / accessibility labels | UI architecture doctrine names trust badges/accessibility expectations. | PROPOSED unless contract/schema exists. |
| Layer catalog / legends / diagnostics surfaces | UI architecture doctrine names these surfaces. | PROPOSED unless contract/schema exists. |

Do not treat this table as a complete object inventory. It reflects current-session evidence and recent files created/verified.

---

## Accepted contents

| Accepted content | Purpose | Guardrail |
|---|---|---|
| `README.md` | Defines UI contract-lane boundary. | Must preserve trust membrane and no-implementation posture. |
| UI semantic contract Markdown | Defines meaning of UI payload/envelope objects. | Must identify upstream evidence/runtime/policy/release dependencies. |
| Object-folder READMEs | Folder-level guards/pointers for object families. | Must not duplicate canonical field semantics unless accepted. |
| `INDEX.md` | Optional inventory after object homes are resolved. | Must label proposed/verified status accurately. |
| `MIGRATION.md` / `BACKLINKS.md` | Optional path/home migration support. | Must include rollback/backlink plan. |

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| UI component implementation, app state, CSS, design tokens | UI/web/app/package roots | Contracts define meaning, not rendering code. |
| MapLibre adapter code or plugin code | map runtime/package roots | Renderer behavior is implementation. |
| JSON Schema | `schemas/contracts/v1/ui/` or accepted schema homes | Schemas own shape. |
| Policy rules | `policy/` roots | Policy owns admissibility. |
| Fixtures/tests/validators | `fixtures/`, `tests/`, `tools/validators/` | Proof and enforcement stay separate. |
| EvidenceBundle records, proof stores, source records | evidence/source/proof/data roots | UI consumes governed projections. |
| RAW/WORK/QUARANTINE/internal/canonical store access | data/internal lifecycle roots | UI must not read these directly. |
| Release manifests, correction notices, rollback cards | `release/` and release contracts | UI displays release state; it does not approve it. |
| AI prompts, chain-of-thought, direct model output | governed AI/runtime roots | AI output is downstream and receipt-bound. |

---

## Trust-surface rules

PROPOSED semantic rules for UI contracts:

- UI payloads must be downstream of governed API/runtime outputs.
- UI surfaces must not read RAW, WORK, QUARANTINE, canonical/internal stores, proof stores, or direct model output.
- UI contracts must preserve finite outcomes: `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` where applicable.
- UI contracts must preserve caveats, limitations, evidence refs, citation posture, sensitivity/redaction state, review state, release state, correction state, and rollback state when material.
- UI contracts must not upgrade missing, stale, unresolved, denied, restricted, uncited, or conflicted evidence into visible fact.
- Accessibility labels, trust badges, tooltips, drawers, popovers, diagnostics, and export copy are trust surfaces and must remain policy-safe.
- Public UI clients must use released/governed projections, not canonical truth stores.

---

## Validation checklist

- [ ] Verify canonical schema home for each UI contract.
- [ ] Verify validators and fixtures exist before claiming enforceability.
- [ ] Verify component/app implementation consumes governed API/runtime payloads only.
- [ ] Verify negative states are tested: ABSTAIN, DENY, ERROR, stale, redacted, corrected, withdrawn, and no-data.
- [ ] Verify accessibility labels do not leak restricted values and communicate trust state.
- [ ] Verify UI export/share/screenshot paths preserve release, citation, caveat, and rollback posture.
- [ ] Verify no contract in this lane becomes schema/policy/code/data/release authority.

---

## Open questions

- Which UI object families should be canonical in `contracts/ui/` versus `contracts/evidence/`, `contracts/focus_mode/`, `contracts/runtime/`, or `contracts/map/`?
- Should object folders or flat files be the canonical UI contract layout?
- Which schema homes are accepted for UI object families?
- Which policy package owns UI-specific redaction/display decisions?
- Which UI trust states are mandatory for public versus steward/internal surfaces?

---

## Rollback

Rollback is required if this lane is used as UI implementation, schema authority, policy authority, evidence closure, source truth, proof storage, release approval, raw/canonical-store access, direct model-output transport, or a way to bypass governed APIs.

Rollback target for this expansion: previous stub blob SHA `12c0efbe2521663a73c4e0f534dc38f493b59207`.

<p align="right"><a href="#top">Back to top</a></p>
