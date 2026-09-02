<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-focus-response
title: contracts/ui/focus_response.md — UI FocusResponse Contract
type: semantic-contract; ui-response-projection-profile
version: v0.2
status: draft; PROPOSED; schema-stub-confirmed; ui-family; focus-mode-response-projection; runtime-envelope-dependent; not-runtime-authority
owners: OWNER_TBD — UI steward · Focus Mode steward · Runtime steward · Evidence steward · Policy steward · Release steward · Schema steward · Accessibility steward · Docs steward
created: NEEDS VERIFICATION — greenfield scaffold existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; ui; focus-response; FocusResponse; focus-mode; runtime-response-projection; finite-outcomes; evidence-dependent; citation-capable; no-sovereign-truth
tags: [kfm, contracts, ui, focus-response, FocusResponse, FocusRequest, FocusModePayload, RuntimeResponseEnvelope, DecisionEnvelope, EvidenceBundle, EvidenceRef, PolicyDecision, CitationValidationReport, AIReceipt, accessibility]
related:
  - ./README.md
  - ./focus_request.md
  - ./map_context_envelope/README.md
  - ./evidence_drawer_payload.md
  - ./citation_validation_report.md
  - ../focus_mode/focus_mode_payload.md
  - ../runtime/runtime_response_envelope.md
  - ../runtime/decision_envelope.md
  - ../runtime/ai_receipt.md
  - ../evidence/evidence_bundle.md
  - ../evidence/evidence_ref.md
  - ../evidence/citation_validation_report.md
  - ../policy/policy_decision.md
  - ../release/release_manifest.md
  - ../../schemas/contracts/v1/ui/focus_response.schema.json
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../policy/ui/
  - ../../policy/focus/
  - ../../policy/runtime/
  - ../../policy/evidence/
  - ../../fixtures/ui/focus_response/
  - ../../tools/validators/ui/validate_focus_response.py
  - ../../docs/architecture/ui/README.md
  - ../../docs/architecture/ui/FOCUS_FLOW.md
  - ../../docs/focus-mode/state/map-context-state.md
notes:
  - "Expanded from a PROPOSED greenfield scaffold at `contracts/ui/focus_response.md`."
  - "A paired UI schema stub exists at `schemas/contracts/v1/ui/focus_response.schema.json`; it requires only `id`, allows additional properties, and names this contract doc."
  - "RuntimeResponseEnvelope is the runtime/client trust membrane object with the finite outcome enum ANSWER, ABSTAIN, DENY, ERROR; this UI contract is a response projection/profile, not runtime authority."
  - "FocusModePayload is a downstream governed payload contract under `contracts/focus_mode/`; this UI response may reference it but must not replace it."
  - "Rollback target for this expansion is previous scaffold blob SHA `e4b066b3b26fa45e60e65d8b2ceaa78ec72b787d`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI FocusResponse Contract

> `FocusResponse` is the UI-facing response projection shown after a governed Focus Mode/runtime request resolves to a finite outcome. It renders or references the result of a `RuntimeResponseEnvelope` and any related `FocusModePayload`, evidence, policy, citation, review, release, correction, and AI receipt state. It is not the runtime authority, not the payload store, not EvidenceBundle closure, not policy execution, not release approval, and not AI truth.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts/ui" src="https://img.shields.io/badge/root-contracts%2Fui-blue">
  <img alt="Object: FocusResponse" src="https://img.shields.io/badge/object-FocusResponse-purple">
  <img alt="Schema: stub confirmed" src="https://img.shields.io/badge/schema-stub__confirmed-orange">
  <img alt="Boundary: projection not runtime" src="https://img.shields.io/badge/boundary-projection__not__runtime-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/ui/focus_response.md`  
**Paired UI schema:** `schemas/contracts/v1/ui/focus_response.schema.json`  
**Schema posture:** PROPOSED stub; required field `id` only; `additionalProperties: true`  
**Runtime authority:** `contracts/runtime/runtime_response_envelope.md`  
**Downstream/related payload contract:** `contracts/focus_mode/focus_mode_payload.md`  
**Owning root:** `contracts/ui/` — UI-facing semantic meaning only  
**Truth posture:** CONFIRMED target was a greenfield scaffold · CONFIRMED paired UI schema stub exists and names this contract doc · CONFIRMED RuntimeResponseEnvelope is the client-facing runtime envelope with finite outcomes · CONFIRMED FocusModePayload is a separate governed payload contract · CONFIRMED UI README says UI contracts are semantic meaning only and not implementation · NEEDS VERIFICATION for final response schema, validator, fixtures, runtime/API route behavior, FocusModePayload linkage, policy gates, citation validation, AIReceipt linkage, accessibility behavior, and release behavior

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Authority split](#authority-split) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Projection rules](#projection-rules) · [Recommended UI fields](#recommended-ui-fields) · [Outcome relationship](#outcome-relationship) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This contract defines the UI-facing meaning of `FocusResponse`.

It answers:

- what the UI may render after a FocusRequest resolves;
- which finite outcome was produced by the governed runtime;
- what public-safe answer, abstention, denial, or diagnostic text may be shown;
- which evidence, citations, policy decisions, release state, AI receipt, caveats, and correction/rollback refs must remain visible when material;
- what the UI must not infer or hide from the response.

It does not answer:

- whether the runtime decision was correct;
- whether evidence is sufficient beyond the runtime/evidence closure refs;
- whether policy permits more detail than the envelope provides;
- whether release is approved;
- whether AI text is true;
- whether raw/canonical/internal stores can be read;
- whether the response may be cached or exported without release/citation/caveat checks.

---

## Meaning

A `FocusResponse` is a presentation projection of a governed runtime result.

A mature governed flow should look like:

```text
FocusRequest
  -> MapContextEnvelope / caller-role admission
  -> evidence + policy + citation + release checks
  -> RuntimeResponseEnvelope with ANSWER / ABSTAIN / DENY / ERROR
  -> optional FocusModePayload / EvidenceDrawerPayload / AIReceipt refs
  -> FocusResponse UI projection
  -> UI renders trust-visible state with caveats and correction/rollback posture
```

The response shown in the UI must stay downstream of runtime, evidence, policy, citation, review, release, and correction state.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| UI response meaning | `contracts/ui/focus_response.md` | This file; UI projection/profile only. |
| UI request meaning | `contracts/ui/focus_request.md` | Request semantics; not response. |
| Runtime response authority | `contracts/runtime/runtime_response_envelope.md` | Owns runtime finite outcome envelope. |
| Runtime decision detail | `contracts/runtime/decision_envelope.md` | Decision context, not UI text authority by itself. |
| Focus payload meaning | `contracts/focus_mode/focus_mode_payload.md` | Governed payload/projection for focus-mode slices. |
| AI audit | `contracts/runtime/ai_receipt.md` | AIReceipt records AI execution; response is not proof. |
| Evidence support | `contracts/evidence/evidence_bundle.md`, `contracts/evidence/evidence_ref.md` | EvidenceBundle/EvidenceRef support claims. |
| Citation checking | `contracts/evidence/citation_validation_report.md`, `contracts/ui/citation_validation_report.md` | Citation validation gates display. |
| Policy/admissibility | `policy/ui/`, `policy/focus/`, `policy/runtime/`, `policy/evidence/` | Policy owns allow/deny/restrict/abstain. |
| Machine shape | `schemas/contracts/v1/ui/focus_response.schema.json` | Current stub only; field realization remains proposed. |
| UI implementation | UI/web/app roots | Component rendering and state management stay outside contracts. |
| Release/correction/rollback | `release/` and release contracts | Release state and rollback remain separate. |

---

## Schema posture

The paired UI schema currently declares:

| Field | Required | Schema-confirmed shape | Meaning |
|---|---:|---|---|
| `id` | yes | string | Canonical identifier for this focus response projection. |
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
| Rendering a runtime finite outcome to the Focus Mode panel | Yes | Must preserve ANSWER/ABSTAIN/DENY/ERROR semantics. |
| Showing answer text | Conditional | Only if runtime/evidence/policy/release context permits. |
| Showing abstain/deny/error reasons | Yes | Must be public-safe and not leak restricted details. |
| Showing citations/evidence/source summaries | Conditional | Only if policy/release permits. |
| Showing AI receipt/audit state | Conditional | Must be safe for caller role. |
| Linking to EvidenceDrawerPayload | Yes | Drawer may inspect supporting evidence if allowed. |
| Treating response as RuntimeResponseEnvelope authority | No | Runtime contract owns the envelope. |
| Treating response as FocusModePayload | No | FocusModePayload is separate. |
| Treating response as release approval | No | Release manifests and promotion decisions remain separate. |

---

## Exclusions

This contract must not be used as:

| Misuse | Required home/outcome |
|---|---|
| RuntimeResponseEnvelope | Use runtime contract. |
| FocusRequest | Use `contracts/ui/focus_request.md`. |
| FocusModePayload | Use `contracts/focus_mode/focus_mode_payload.md`. |
| EvidenceBundle closure | Use EvidenceBundle. |
| PolicyDecision | Use policy/runtime/evidence policy outputs. |
| AIReceipt | Use AI/runtime receipt contract. |
| ReleaseManifest or publication approval | Use release roots. |
| UI component implementation | Use UI/web/app roots. |
| Raw prompt/model chain-of-thought storage | Do not store in public contracts. |
| RAW/WORK/QUARANTINE/canonical data access | Deny; use governed API projections. |

---

## Projection rules

PROPOSED UI rules:

- A FocusResponse must derive from a governed RuntimeResponseEnvelope or equivalent accepted runtime response object.
- A FocusResponse must preserve finite outcome state and not normalize negative states into answer text.
- `ANSWER` responses must preserve evidence, citation, policy, release, caveat, and correction/rollback posture when material.
- `ABSTAIN` responses must explain evidence gaps without inventing missing support.
- `DENY` responses must not leak the restricted fact, exact geometry, protected source details, or policy-sensitive internals.
- `ERROR` responses must be diagnostic and must not be confused with evidentiary abstention.
- If AI generated or transformed text appears, an AIReceipt or equivalent audit reference must be available to the permitted audience.
- Public clients must consume governed API/runtime projections, not direct model clients or internal stores.

---

## Recommended UI fields

PROPOSED until schema expansion:

| Field | Meaning |
|---|---|
| `id` | UI response projection identifier. |
| `version` | Response contract/object version. |
| `spec_hash` | Deterministic schema/rendering baseline. |
| `request_ref` | FocusRequest id/ref. |
| `runtime_response_ref` | RuntimeResponseEnvelope id/ref. |
| `outcome` | ANSWER, ABSTAIN, DENY, ERROR. |
| `reason_code` | Public-safe primary reason. |
| `display_text` | Public-safe answer/abstain/deny/error text. |
| `evidence_refs` | EvidenceRef pointers surfaced or used. |
| `evidence_bundle_refs` | EvidenceBundle refs supporting answer, if permitted. |
| `citation_validation_ref` | Citation validation report/projection ref. |
| `policy_decision_refs` | Policy decisions affecting display. |
| `release_refs` | Release manifest/state refs. |
| `ai_receipt_ref` | AIReceipt ref if AI participated and caller may see it. |
| `drawer_payload_ref` | EvidenceDrawerPayload ref for inspection. |
| `caveats` | Limitations, uncertainty, redaction, no-data, stale-source notes. |
| `correction_refs` | Correction/withdrawal/supersession refs. |
| `rollback_ref` | Rollback card/target if material. |
| `accessibility_label` | Assistive-tech trust-state label. |
| `issued_at` | UI projection issue time or runtime issue time. |

---

## Outcome relationship

| Outcome | UI obligation |
|---|---|
| `ANSWER` | Render answer only with permitted citations/caveats/trust state. |
| `ABSTAIN` | Render why the system cannot answer from current evidence. |
| `DENY` | Render safe denial without leaking restricted details. |
| `ERROR` | Render diagnostic failure and recovery guidance where safe. |

---

## Validation expectations

NEEDS VERIFICATION:

- schema expansion beyond `id`, `version`, and `spec_hash`;
- validator path and CI wiring;
- fixtures for ANSWER, ABSTAIN, DENY, ERROR, redacted answer, AI-generated answer, stale evidence, missing release ref, and correction/withdrawal cases;
- runtime/API response projection behavior;
- FocusRequest and MapContextEnvelope linkage;
- FocusModePayload and EvidenceDrawerPayload linkage;
- policy/focus, policy/ui, and policy/runtime integration;
- accessibility-state tests;
- export/share/copy behavior and trust-state preservation.

---

## Open questions

- Should FocusResponse be a separate UI object or only a view over RuntimeResponseEnvelope?
- Which fields should be duplicated versus referenced from RuntimeResponseEnvelope?
- Should AIReceipt refs be visible to public callers or only steward/internal callers?
- Should FocusResponse be persisted, cached, exported, or generated per request only?
- Which finite outcome reason-code vocabulary is final across runtime, focus, and UI?

---

## Rollback

Rollback is required if this contract becomes runtime response authority, FocusModePayload authority, EvidenceBundle closure, PolicyDecision, ReleaseManifest, AIReceipt, direct model client permission, raw/canonical-store access, UI implementation, schema authority, or proof storage.

Rollback target for this expansion: previous scaffold blob SHA `e4b066b3b26fa45e60e65d8b2ceaa78ec72b787d`.

<p align="right"><a href="#top">Back to top</a></p>
