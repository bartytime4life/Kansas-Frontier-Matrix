<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-evidence-drawer-payload-readme
title: contracts/ui/evidence_drawer_payload — EvidenceDrawerPayload UI Object Folder README
type: readme
version: v0.1
status: draft; PROPOSED; object-folder-readme; ui-projection; evidence-dependent; path-needs-review
owners: OWNER_TBD — UI steward · Evidence steward · Contracts steward · Schema steward · Policy steward · Release steward · Accessibility steward · Docs steward
created: 2026-06-24
updated: 2026-06-24
policy_label: public; contracts; ui; evidence-drawer-payload; evidence-drawer; projection; trust-membrane; finite-outcomes; accessibility; release-gated; no-sovereign-truth
tags: [kfm, contracts, ui, evidence-drawer, evidence-drawer-payload, EvidenceDrawerPayload, EvidenceBundle, EvidenceRef, PolicyDecision, RuntimeResponseEnvelope, citation-validation, release-state, accessibility, projection]
related:
  - ../README.md
  - ../evidence_drawer_payload.md
  - ../../evidence/evidence_drawer_payload.md
  - ../../evidence/evidence_bundle.md
  - ../../evidence/evidence_ref.md
  - ../../evidence/citation_validation_report.md
  - ../../runtime/runtime_response_envelope.md
  - ../../runtime/decision_envelope.md
  - ../../policy/policy_decision.md
  - ../../release/release_manifest.md
  - ../../../docs/architecture/ui/EVIDENCE_DRAWER.md
  - ../../../docs/architecture/evidence-drawer.md
  - ../../../schemas/contracts/v1/ui/evidence_drawer_payload.schema.json
  - ../../../schemas/contracts/v1/evidence/evidence_drawer_payload.schema.json
  - ../../../policy/evidence/
  - ../../../policy/runtime/
  - ../../../release/
notes:
  - "This file replaces a blank placeholder at `contracts/ui/evidence_drawer_payload/README.md`."
  - "A flat UI-family scaffold exists at `contracts/ui/evidence_drawer_payload.md`."
  - "An expanded evidence-family contract exists at `contracts/evidence/evidence_drawer_payload.md`, but it is marked PATH-NEEDS-REVIEW because UI and evidence placement are unresolved."
  - "Evidence Drawer architecture identifies EvidenceDrawerPayload as a governed UI projection of EvidenceBundle and proposes a UI schema home."
  - "This folder README is a pointer/lane guide only; it is not EvidenceBundle closure, policy engine, release approval, proof storage, runtime proof, UI implementation, or AI answer authority."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/ui/evidence_drawer_payload

> Object-folder README for the UI-family `EvidenceDrawerPayload` contract path. `EvidenceDrawerPayload` is a governed UI projection over resolved evidence, citations, policy state, review state, release state, caveats, accessibility labels, and finite outcomes. It is not EvidenceBundle, not proof storage, not policy execution, not release approval, not UI component code, and not AI answer truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: ui" src="https://img.shields.io/badge/family-ui-0a7ea4">
  <img alt="Object: EvidenceDrawerPayload" src="https://img.shields.io/badge/object-EvidenceDrawerPayload-purple">
  <img alt="Boundary: projection only" src="https://img.shields.io/badge/boundary-projection__only-critical">
  <img alt="Truth: evidence dependent" src="https://img.shields.io/badge/truth-evidence__dependent-blue">
</p>

**Status:** draft / PROPOSED object-folder README  
**Path:** `contracts/ui/evidence_drawer_payload/README.md`  
**Flat UI contract path:** `contracts/ui/evidence_drawer_payload.md`  
**Related evidence-family contract:** `contracts/evidence/evidence_drawer_payload.md`  
**Schema home:** `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` — PROPOSED / NEEDS VERIFICATION  
**Evidence-family schema:** `schemas/contracts/v1/evidence/evidence_drawer_payload.schema.json` — known path from related contract; field shape remains NEEDS VERIFICATION  
**Truth posture:** CONFIRMED placeholder was blank · CONFIRMED flat UI scaffold exists · CONFIRMED expanded evidence-family contract exists and records path/home review risk · CONFIRMED UI architecture says EvidenceDrawerPayload is a governed projection of EvidenceBundle, not evidence itself · PROPOSED object-folder guide until UI/evidence home and schemas are resolved by stewards/ADR

## Quick jumps

[Purpose](#purpose) · [Authority split](#authority-split) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Projection rules](#projection-rules) · [Validation checklist](#validation-checklist) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This folder exists to organize or document the UI-facing `EvidenceDrawerPayload` object family if KFM keeps an object-folder layout under `contracts/ui/`.

The folder may point to:

- the flat semantic contract at `../evidence_drawer_payload.md`;
- the evidence-family projection contract at `../../evidence/evidence_drawer_payload.md`;
- schema, fixture, policy, accessibility, runtime, and release surfaces that remain outside this folder.

It must not become a second canonical payload contract unless the flat UI contract, evidence-family contract, and schema home are reconciled by steward review or ADR.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| UI-facing object-folder guide | `contracts/ui/evidence_drawer_payload/README.md` | This README; navigation and boundary only. |
| Flat UI semantic contract | `contracts/ui/evidence_drawer_payload.md` | Existing UI scaffold; may become canonical after review. |
| Evidence-facing projection contract | `contracts/evidence/evidence_drawer_payload.md` | Existing expanded contract; currently path-needs-review. |
| Evidence closure | `contracts/evidence/evidence_bundle.md` | EvidenceBundle is canonical evidence support, not this payload. |
| Evidence pointers | `contracts/evidence/evidence_ref.md` | EvidenceRef points to support; it is not drawer payload truth. |
| Citation validation | `contracts/evidence/citation_validation_report.md` | Citation validation stays upstream. |
| Runtime response | `contracts/runtime/runtime_response_envelope.md` | Runtime finite outcome envelope. |
| Decision/policy state | `contracts/runtime/decision_envelope.md`, `contracts/policy/policy_decision.md` | Policy/runtime decide; drawer renders safe state. |
| Machine shape | `schemas/contracts/v1/ui/` or `schemas/contracts/v1/evidence/` after steward decision | Schemas own fields and validation. |
| UI component code | UI/web/app roots | Component implementation stays outside contracts. |
| Release/correction/rollback | `release/` and release contract roots | Publication and rollback remain governed transitions. |

---

## Accepted contents

Only object-folder support material belongs here:

| Accepted item | Purpose |
|---|---|
| `README.md` | Defines folder boundary and points to canonical/related contracts. |
| `MIGRATION.md` | Optional plan if UI/evidence contract homes are consolidated. |
| `BACKLINKS.md` | Optional stale-reference audit for flat/folder/evidence paths. |
| `ADR_POINTER.md` | Optional pointer to accepted home-resolution ADR. |

No field semantics should be maintained here if `contracts/ui/evidence_drawer_payload.md` or `contracts/evidence/evidence_drawer_payload.md` is canonical.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| EvidenceBundle records or proof storage | evidence/proof roots | Drawer payload projects evidence; it is not evidence closure. |
| JSON Schema | `schemas/contracts/v1/ui/` or accepted schema home | Schemas own shape. |
| Policy rules | `policy/evidence/`, `policy/runtime/`, sensitivity/rights/release policy roots | Policy owns display/admissibility. |
| Runtime response implementation | runtime/API roots | Contracts do not implement API behavior. |
| UI component code, CSS, screenshots, design tokens | UI/web/design roots | Rendering implementation stays outside contracts. |
| RAW/WORK/QUARANTINE/canonical store access | data/internal lifecycle roots | Browser/UI must not read internal stores. |
| Release manifests, corrections, rollback cards | `release/` and release contracts | Release state is separate. |
| AI-generated answer text | governed AI/runtime/story surfaces with AIReceipt | AI output is downstream and evidence-bound. |

---

## Projection rules

PROPOSED semantic rules for any future folder-level material:

- The drawer payload must be produced by governed API/runtime surfaces, not assembled by direct browser reads from canonical stores.
- The payload must preserve finite states such as `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` where applicable.
- The payload must show limitations, caveats, source/citation posture, policy state, review state, release state, correction state, and rollback relevance when material.
- The payload must never upgrade unresolved, stale, denied, restricted, or uncited evidence into visible fact.
- The payload must not leak restricted geometry, living-person data, DNA/genomic inference, sensitive archaeology/cultural material, rare-species locations, infrastructure-sensitive details, source secrets, or internal proof-store contents.
- Accessibility text and trust badges are part of the public trust surface and must remain policy-safe.

---

## Validation checklist

- [ ] Verify whether canonical semantic home is `contracts/ui/evidence_drawer_payload.md`, `contracts/evidence/evidence_drawer_payload.md`, or a split.
- [ ] Verify whether canonical schema home is `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` or evidence-family schema.
- [ ] Verify no field semantics are duplicated between flat, folder, and evidence-family paths without ADR.
- [ ] Verify governed API/runtime creates drawer payloads after evidence, policy, citation, review, and release checks.
- [ ] Verify UI code does not read RAW, WORK, QUARANTINE, canonical/internal stores, proof stores, or direct model output.
- [ ] Verify accessibility and trust-visible states are tested for ANSWER, ABSTAIN, DENY, ERROR, stale, redacted, and corrected cases.

---

## Open questions

- Should the canonical semantic contract live in `contracts/ui/evidence_drawer_payload.md`, `contracts/evidence/evidence_drawer_payload.md`, or both with explicitly split responsibilities?
- Should this object-folder path remain after flat/family placement is resolved?
- Which schema path owns the field shape?
- Which fixtures prove negative states and redaction behavior?
- Which public UI surfaces are allowed to show drawer payload content beyond the drawer itself?

---

## Rollback

Rollback is required if this folder becomes a parallel payload contract, evidence closure, proof store, policy engine, runtime implementation, UI implementation, release approval, source truth, public API bypass, raw/canonical-store reader, or AI answer authority.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
