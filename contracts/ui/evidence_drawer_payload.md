<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-evidence-drawer-payload
title: contracts/ui/evidence_drawer_payload.md — UI EvidenceDrawerPayload Contract
type: semantic-contract; ui-projection-profile
version: v0.2
status: draft; PROPOSED; schema-stub-confirmed; ui-family; evidence-drawer-projection; evidence-dependent; path-needs-review
owners: OWNER_TBD — UI steward · Evidence steward · Contracts steward · Schema steward · Policy steward · Release steward · Accessibility steward · Runtime steward · Docs steward
created: NEEDS VERIFICATION — greenfield scaffold existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; ui; evidence-drawer-payload; EvidenceDrawerPayload; evidence-drawer; projection; finite-outcomes; citation-capable; policy-filtered; release-gated; accessibility; no-sovereign-truth
tags: [kfm, contracts, ui, evidence-drawer-payload, EvidenceDrawerPayload, evidence-drawer, EvidenceBundle, EvidenceRef, CitationValidationReport, PolicyDecision, RuntimeResponseEnvelope, ReleaseManifest, RollbackCard, accessibility, trust-badges]
related:
  - ./README.md
  - ./evidence_drawer_payload/README.md
  - ./citation_validation_report.md
  - ../evidence/evidence_drawer_payload.md
  - ../evidence/evidence_bundle.md
  - ../evidence/evidence_ref.md
  - ../evidence/citation_validation_report.md
  - ../runtime/runtime_response_envelope.md
  - ../runtime/decision_envelope.md
  - ../policy/policy_decision.md
  - ../release/release_manifest.md
  - ../../schemas/contracts/v1/ui/evidence_drawer_payload.schema.json
  - ../../schemas/contracts/v1/evidence/evidence_drawer_payload.schema.json
  - ../../policy/ui/
  - ../../policy/evidence/
  - ../../policy/runtime/
  - ../../fixtures/ui/evidence_drawer_payload/
  - ../../tools/validators/ui/validate_evidence_drawer_payload.py
  - ../../docs/architecture/ui/README.md
  - ../../docs/architecture/ui/EVIDENCE_DRAWER.md
notes:
  - "Expanded from a PROPOSED greenfield scaffold at `contracts/ui/evidence_drawer_payload.md`."
  - "A paired UI schema stub exists at `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json`; it requires only `id`, allows additional properties, and names this contract doc."
  - "An expanded evidence-family contract exists at `contracts/evidence/evidence_drawer_payload.md`; it marks drawer-payload placement as PATH-NEEDS-REVIEW until UI/evidence home is resolved."
  - "This UI contract is the UI-facing projection profile; it must not duplicate EvidenceBundle closure or evidence-family authority."
  - "Rollback target for this expansion is previous scaffold blob SHA `aca4e52be4bef7b48fdf8301feb00ba6a9b376ea`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI EvidenceDrawerPayload Contract

> `EvidenceDrawerPayload` is the UI-facing governed projection that carries resolved, cited, policy-filtered evidence context to the Evidence Drawer for a clicked feature, layer assertion, popover, export, Focus Mode reference, or AI-answer reference. It makes trust state visible; it does not create evidence, close an EvidenceBundle, execute policy, approve release, read proof stores, or authorize AI answers.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts/ui" src="https://img.shields.io/badge/root-contracts%2Fui-blue">
  <img alt="Object: EvidenceDrawerPayload" src="https://img.shields.io/badge/object-EvidenceDrawerPayload-purple">
  <img alt="Schema: stub confirmed" src="https://img.shields.io/badge/schema-stub__confirmed-orange">
  <img alt="Boundary: projection only" src="https://img.shields.io/badge/boundary-projection__only-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/ui/evidence_drawer_payload.md`  
**Object-folder guide:** `contracts/ui/evidence_drawer_payload/README.md`  
**Paired UI schema:** `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json`  
**Schema posture:** PROPOSED stub; required field `id` only; `additionalProperties: true`  
**Related evidence-family contract:** `contracts/evidence/evidence_drawer_payload.md` — PATH-NEEDS-REVIEW for final home split  
**Truth posture:** CONFIRMED target was a greenfield scaffold · CONFIRMED paired UI schema stub exists and names this contract doc · CONFIRMED evidence-family contract exists and treats EvidenceDrawerPayload as a projection, not evidence/policy/release/proof/AI authority · CONFIRMED UI README states UI contracts are semantic meaning only · NEEDS VERIFICATION for final canonical home, schema expansion, validators, fixtures, governed API/runtime behavior, policy filtering, UI rendering, accessibility implementation, release behavior, and AI/runtime integration

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Authority split](#authority-split) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Projection rules](#projection-rules) · [Recommended UI fields](#recommended-ui-fields) · [Outcome and trust states](#outcome-and-trust-states) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This contract defines the UI-facing meaning of `EvidenceDrawerPayload`.

It answers:

- what evidence/trust context the Evidence Drawer may render;
- which clicked feature, layer, claim, focus answer, export, or AI-answer reference the payload explains;
- which evidence refs, bundle refs, citations, source summaries, policy state, review state, release state, caveats, and rollback/correction refs are safe to show;
- whether the UI should render `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`-style trust state;
- what the UI must never infer from the payload.

It does not answer:

- whether a claim is true;
- whether an EvidenceBundle is closed;
- whether policy permits display;
- whether release is approved;
- whether proof records exist;
- whether raw source/canonical data can be shown;
- whether AI text is correct.

---

## Meaning

`EvidenceDrawerPayload` is a governed projection envelope for the UI trust panel.

A mature governed flow should look like:

```text
clicked released feature / badge / consequential map claim
  -> governed claim-resolution request
  -> policy + evidence + citation + review + release checks
  -> RuntimeResponseEnvelope / DecisionEnvelope
  -> EvidenceDrawerPayload projection
  -> UI renders trust-visible state with caveats and refs
```

The payload renders what the governed API/runtime has resolved. It does not compute new evidence, infer new policy, promote a release, or upgrade an abstention into an answer.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| UI-facing payload meaning | `contracts/ui/evidence_drawer_payload.md` | This file; UI projection/profile. |
| Object-folder boundary | `contracts/ui/evidence_drawer_payload/README.md` | Folder guide; not field authority. |
| Evidence-facing payload meaning | `contracts/evidence/evidence_drawer_payload.md` | Existing expanded contract; final home still needs steward review. |
| Evidence closure | `contracts/evidence/evidence_bundle.md` | EvidenceBundle is canonical evidence support. |
| Evidence pointer | `contracts/evidence/evidence_ref.md` | EvidenceRef points to evidence; payload may carry refs. |
| Citation checking | `contracts/evidence/citation_validation_report.md`, `contracts/ui/citation_validation_report.md` | Validation/report objects remain separate. |
| Runtime finite outcome | `contracts/runtime/runtime_response_envelope.md`, `contracts/runtime/decision_envelope.md` | Runtime/API owns finite outcome and decision envelope. |
| Policy/admissibility | `policy/ui/`, `policy/evidence/`, `policy/runtime/`, sensitivity/rights/release policy roots | Policy owns display decisions. |
| Machine shape | `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` or evidence-family schema after decision | Current UI schema is a permissive stub. |
| UI implementation | UI/web/app roots | Drawer component code and state machine stay outside contracts. |
| Release/correction/rollback | `release/` and release contracts | Release and rollback remain separate. |

---

## Schema posture

The paired UI schema currently declares:

| Field | Required | Schema-confirmed shape | Meaning |
|---|---:|---|---|
| `id` | yes | string | Canonical identifier for the UI payload/projection. |
| `version` | no | string | Contract or object version. |
| `spec_hash` | no | string | Deterministic content/spec hash. |

The schema also confirms:

```text
additionalProperties: true
```

Because the schema is permissive, most fields in this contract are PROPOSED semantic guidance until schemas, fixtures, validators, policy tests, and UI/runtime behavior are verified.

---

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Rendering evidence context for a clicked feature/layer/claim | Yes | Must be governed API/runtime projection. |
| Showing finite outcome state | Yes | Preserve answer/abstain/deny/error semantics. |
| Showing citations and source summaries | Conditional | Only if policy/release permits. |
| Showing sensitivity, redaction, review, and release state | Conditional | Must avoid leaking restricted details. |
| Showing stale/no-data/failed-verification states | Yes | Trust-visible negative states must not be hidden. |
| Supporting AI-answer trust display | Conditional | AI answer must remain evidence-bound and receipt-aware. |
| Treating payload as EvidenceBundle closure | No | EvidenceBundle owns closure. |
| Treating payload as PolicyDecision or ReleaseManifest | No | Policy/release roots own decisions. |
| Reading RAW/WORK/QUARANTINE/canonical stores from the drawer | No | UI must consume governed projections only. |

---

## Exclusions

This contract must not be used as:

| Misuse | Required home/outcome |
|---|---|
| EvidenceBundle closure | Use EvidenceBundle. |
| EvidenceRef pointer authority | Use EvidenceRef. |
| CitationValidationReport | Use citation validation contracts. |
| PolicyDecision | Use policy/runtime/evidence policy outputs. |
| ReleaseManifest or publication approval | Use release roots. |
| Proof storage | Use governed proof/data roots. |
| UI component implementation | Use UI/web/app roots. |
| Direct source/canonical data access | Deny; use governed API projections. |
| AI answer authority | Use governed AI/runtime/evidence flow with cite-or-abstain. |

---

## Projection rules

PROPOSED UI rules:

- The payload must be produced by governed API/runtime code after evidence, policy, citation, review, and release checks.
- The payload must preserve finite outcome state and negative states; it must not convert unresolved or denied evidence into a supported claim.
- The payload must identify the inspected feature/layer/claim context without exposing restricted internals.
- The payload must carry public-safe evidence/citation/source summaries, not raw proof or source payloads.
- The payload must preserve limitations, caveats, stale/no-data states, correction refs, and rollback refs when material.
- The payload must not leak restricted coordinates, living-person data, DNA/genomic inference, cultural-sensitive material, infrastructure-sensitive details, source secrets, or internal proof-store contents.
- Accessibility labels and trust badges are part of the trust surface and must reflect the same state as visible UI.

---

## Recommended UI fields

PROPOSED until schema expansion:

| Field | Meaning |
|---|---|
| `id` | UI payload/projection identifier. |
| `version` | Payload contract/object version. |
| `spec_hash` | Deterministic schema/rendering baseline. |
| `outcome` | ANSWER, ABSTAIN, DENY, ERROR, or accepted equivalent. |
| `reason_codes` | Public-safe finite outcome reasons. |
| `feature_ref` | Inspected feature reference. |
| `layer_ref` | Inspected layer/release reference. |
| `claim_ref` | Claim or assertion being inspected. |
| `time_window` | Time context shown to user. |
| `evidence_bundle_refs` | EvidenceBundle refs supporting visible claim. |
| `evidence_refs` | EvidenceRef pointers, if safe. |
| `citation_validation_ref` | Citation validation report/projection ref. |
| `source_summary` | Public-safe source summary. |
| `policy_decision_ref` | Policy decision driving visible state. |
| `sensitivity_state` | Public-safe sensitivity/redaction posture. |
| `review_state` | Review state. |
| `release_state` | Release state / manifest ref. |
| `caveats` | Limitations and uncertainty text. |
| `correction_refs` | Correction/withdrawal refs if material. |
| `rollback_ref` | Rollback target/card if material. |
| `trust_badges` | Public-safe trust-state badges. |
| `accessibility_label` | Assistive-tech label for trust state. |

---

## Outcome and trust states

| State | UI meaning | Required posture |
|---|---|---|
| `ANSWER` | Resolved evidence/policy/release state permits a supported display. | Show citations, caveats, release/review state. |
| `ABSTAIN` | Evidence is missing, stale, unresolved, conflicted, or insufficient. | Do not render claim as fact; explain why. |
| `DENY` | Policy/release/sensitivity/rights denies display. | Do not leak restricted details. |
| `ERROR` | Envelope, runtime, validation, or system failure prevents evaluation. | Diagnostic state, not evidentiary state. |

---

## Validation expectations

NEEDS VERIFICATION:

- final canonical UI/evidence home split;
- schema expansion beyond `id`, `version`, and `spec_hash`;
- validator path and CI wiring;
- fixtures for ANSWER, ABSTAIN, DENY, ERROR, stale, missing, no-data, redacted, corrected, withdrawn, and AI-reference cases;
- UI behavior in Evidence Drawer, Focus Mode, export/share, diagnostics, and map popover flows;
- policy filtering of sensitive details;
- accessibility-state tests;
- release-gate behavior for public surfaces.

---

## Open questions

- Should `EvidenceDrawerPayload` be canonical under `contracts/ui/`, `contracts/evidence/`, or split by UI projection versus evidence projection?
- Should the UI schema reference the evidence-family schema or become the canonical field shape?
- Which finite outcome vocabulary is final across runtime, evidence, and UI?
- Which source/citation details may public users see versus steward/internal users?
- Should drawer payloads be persisted, cached, or generated per governed API request only?

---

## Rollback

Rollback is required if this contract becomes evidence closure, policy authority, release approval, proof storage, UI component implementation, source truth, public API authority, raw/canonical-store access, or AI answer truth.

Rollback target for this expansion: previous scaffold blob SHA `aca4e52be4bef7b48fdf8301feb00ba6a9b376ea`.

<p align="right"><a href="#top">Back to top</a></p>
