<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-focus-request
title: contracts/ui/focus_request.md — UI FocusRequest Contract
type: semantic-contract; ui-request-profile
version: v0.2
status: draft; PROPOSED; schema-stub-confirmed; ui-family; focus-mode-request; runtime-admission; evidence-dependent; not-response-payload
owners: OWNER_TBD — UI steward · Focus Mode steward · Runtime steward · Evidence steward · Policy steward · Release steward · Schema steward · Accessibility steward · Docs steward
created: NEEDS VERIFICATION — greenfield scaffold existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; ui; focus-request; FocusRequest; focus-mode; runtime-admission; map-context; evidence-dependent; finite-outcomes; no-direct-model-client; no-sovereign-truth
tags: [kfm, contracts, ui, focus-request, FocusRequest, FocusModePayload, MapContextEnvelope, EvidenceBundle, EvidenceRef, PolicyDecision, RuntimeResponseEnvelope, AIReceipt, citation-validation, trust-membrane]
related:
  - ./README.md
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
  - ../../schemas/contracts/v1/ui/focus_request.schema.json
  - ../../schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json
  - ../../policy/ui/
  - ../../policy/focus/
  - ../../policy/runtime/
  - ../../policy/evidence/
  - ../../fixtures/ui/focus_request/
  - ../../tools/validators/ui/validate_focus_request.py
  - ../../docs/architecture/ui/README.md
  - ../../docs/architecture/ui/FOCUS_FLOW.md
  - ../../docs/focus-mode/state/map-context-state.md
notes:
  - "Expanded from a PROPOSED greenfield scaffold at `contracts/ui/focus_request.md`."
  - "A paired UI schema stub exists at `schemas/contracts/v1/ui/focus_request.schema.json`; it requires only `id`, allows additional properties, and names this contract doc."
  - "FocusModePayload is already a governed downstream payload contract under `contracts/focus_mode/`; this UI contract defines the request profile that asks for focus processing and must not duplicate payload/response authority."
  - "UI contracts are semantic meaning only; UI code, schemas, policy, fixtures, tests, validators, runtime routes, release artifacts, and proof stores remain in separate roots."
  - "Rollback target for this expansion is previous scaffold blob SHA `311305688c34d61b38976b073641725048423594`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI FocusRequest Contract

> `FocusRequest` is the UI-facing request profile for asking a governed Focus Mode/runtime surface to evaluate a bounded question against released map context, evidence, policy, and release state. It is a request envelope, not a FocusModePayload, not a RuntimeResponseEnvelope, not an AI prompt authority, not evidence closure, and not release approval.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts/ui" src="https://img.shields.io/badge/root-contracts%2Fui-blue">
  <img alt="Object: FocusRequest" src="https://img.shields.io/badge/object-FocusRequest-purple">
  <img alt="Schema: stub confirmed" src="https://img.shields.io/badge/schema-stub__confirmed-orange">
  <img alt="Boundary: request not response" src="https://img.shields.io/badge/boundary-request__not__response-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/ui/focus_request.md`  
**Paired UI schema:** `schemas/contracts/v1/ui/focus_request.schema.json`  
**Schema posture:** PROPOSED stub; required field `id` only; `additionalProperties: true`  
**Downstream payload contract:** `contracts/focus_mode/focus_mode_payload.md`  
**Owning root:** `contracts/ui/` — UI-facing semantic meaning only  
**Truth posture:** CONFIRMED target was a greenfield scaffold · CONFIRMED paired UI schema stub exists and names this contract doc · CONFIRMED FocusModePayload exists as a separate governed downstream payload contract · CONFIRMED UI README says UI contracts are semantic meaning only and not implementation · NEEDS VERIFICATION for final request schema, validator, fixtures, runtime/API route behavior, map-context envelope binding, policy gates, AIReceipt linkage, accessibility behavior, and release behavior

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Authority split](#authority-split) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Request rules](#request-rules) · [Recommended UI fields](#recommended-ui-fields) · [Outcome relationship](#outcome-relationship) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This contract defines the UI-facing meaning of `FocusRequest`.

It answers:

- what the UI is asking a governed Focus Mode/runtime surface to evaluate;
- which map context, area scope, question text, selected features, evidence refs, caller role, and release context frame the request;
- which upstream objects must be present before runtime processing can safely proceed;
- what the UI must not infer from submitting a request.

It does not answer:

- whether the request will produce an answer;
- whether evidence is sufficient;
- whether policy permits display;
- whether release is approved;
- whether AI may answer without EvidenceBundle support;
- whether the FocusModePayload is valid;
- whether raw/canonical/internal data can be read by UI or model code.

---

## Meaning

A `FocusRequest` is a user-facing or steward-facing request envelope. It carries enough bounded context for a governed runtime to decide whether it can evaluate a focus query.

A mature governed flow should look like:

```text
UI focus interaction
  -> FocusRequest
  -> MapContextEnvelope / area / caller-role admission
  -> policy + evidence + citation + release checks
  -> runtime / AI process if allowed
  -> RuntimeResponseEnvelope with ANSWER / ABSTAIN / DENY / ERROR
  -> FocusModePayload or EvidenceDrawerPayload projection when applicable
```

The request starts the governed flow. It does not guarantee a successful answer and must not bypass evidence, policy, citation, release, or AI receipt requirements.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| UI request meaning | `contracts/ui/focus_request.md` | This file; request semantics only. |
| Map context | `contracts/ui/map_context_envelope/README.md` or accepted flat contract | MapContextEnvelope bounds the map state; not query text. |
| Focus payload meaning | `contracts/focus_mode/focus_mode_payload.md` | Downstream governed payload, not request. |
| Runtime response | `contracts/runtime/runtime_response_envelope.md`, `contracts/runtime/decision_envelope.md` | Runtime/API owns finite outcome response. |
| AI audit | `contracts/runtime/ai_receipt.md` | AIReceipt records AI execution; request is not AI proof. |
| Evidence support | `contracts/evidence/evidence_bundle.md`, `contracts/evidence/evidence_ref.md` | EvidenceBundle/EvidenceRef support claims. |
| Citation checking | `contracts/evidence/citation_validation_report.md`, `contracts/ui/citation_validation_report.md` | Citation validation gates display. |
| Policy/admissibility | `policy/ui/`, `policy/focus/`, `policy/runtime/`, `policy/evidence/` | Policy owns allow/deny/restrict/abstain. |
| Machine shape | `schemas/contracts/v1/ui/focus_request.schema.json` | Current stub only; field realization remains proposed. |
| UI implementation | UI/web/app roots | Component code and state management stay outside contracts. |
| Release/correction/rollback | `release/` and release contracts | Release state and rollback remain separate. |

---

## Schema posture

The paired UI schema currently declares:

| Field | Required | Schema-confirmed shape | Meaning |
|---|---:|---|---|
| `id` | yes | string | Canonical identifier for this focus request. |
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
| Submitting a bounded focus query to governed runtime | Yes | Must include/map to admissible context and caller role. |
| Carrying question text | Conditional | Query text must be bounded by map/evidence/release context and policy. |
| Referencing MapContextEnvelope | Yes | Runtime should admit envelope before evidence/AI work. |
| Referencing EvidenceRefs or selected features | Conditional | References must resolve or lead to ABSTAIN/ERROR/DENY as appropriate. |
| Triggering AI Focus Mode | Conditional | AI must remain downstream of evidence/policy and emit/resolve AIReceipt. |
| Treating request as an answer | No | RuntimeResponseEnvelope owns response. |
| Treating request as FocusModePayload | No | FocusModePayload is downstream projection. |
| Treating request as release approval | No | Release manifests and promotion decisions remain separate. |

---

## Exclusions

This contract must not be used as:

| Misuse | Required home/outcome |
|---|---|
| FocusModePayload | Use `contracts/focus_mode/focus_mode_payload.md`. |
| RuntimeResponseEnvelope | Use runtime contracts. |
| EvidenceBundle closure | Use EvidenceBundle. |
| PolicyDecision | Use policy/runtime/evidence policy outputs. |
| AIReceipt | Use AI/runtime receipt contract. |
| ReleaseManifest or publication approval | Use release roots. |
| UI component implementation | Use UI/web/app roots. |
| Raw prompt/model chain-of-thought storage | Do not store in public contracts. |
| RAW/WORK/QUARANTINE/canonical data access | Deny; use governed API projections. |

---

## Request rules

PROPOSED UI rules:

- A request must be bounded to an area, map context, release context, caller role, and finite surface type.
- A request should carry query text separately from `MapContextEnvelope` when the accepted request model keeps map state and question text separate.
- A request must not include raw evidence payloads, protected source data, credentials, secrets, direct model context dumps, or canonical store paths.
- A request that references stale, missing, unresolved, denied, or restricted context must produce governed `ABSTAIN`, `DENY`, or `ERROR`, not a best-effort answer.
- A request may trigger AI interpretation only after evidence/policy/release context is admitted and receipt/audit rules are satisfied.
- Public clients must submit requests through governed API/runtime surfaces, never direct model clients.

---

## Recommended UI fields

PROPOSED until schema expansion:

| Field | Meaning |
|---|---|
| `id` | Request identifier. |
| `version` | Request contract/object version. |
| `spec_hash` | Deterministic schema/request spec hash. |
| `request_id` | Idempotency/audit id, if different from `id`. |
| `surface` | Focus panel, Evidence Drawer launch, map popover, export, steward review, or accepted surface. |
| `area_scope` | County/region/corridor/domain scope. |
| `map_context_envelope_ref` | Reference to admitted map context envelope, or inline envelope if schema accepts. |
| `query_text` | User/steward question text, bounded and policy-safe. |
| `caller_role` | public, internal, validator, steward, or accepted role. |
| `selected_feature_refs` | Selected features from map context, if safe. |
| `evidence_refs` | Optional user-selected evidence refs. |
| `release_refs` | Release context for visible layers/data. |
| `requested_output_mode` | answer, summary, compare, export, diagnostic, or accepted mode. |
| `policy_context_refs` | Applicable policy refs/decisions. |
| `locale` | User-visible language/locale, if needed. |
| `accessibility_context` | Accessibility settings that affect output rendering. |
| `client_context` | Public-safe client/browser context. |
| `submitted_at` | Timestamp the request was submitted. |

---

## Outcome relationship

`FocusRequest` does not own the outcome. The governed runtime response does.

| Runtime outcome | Meaning for request |
|---|---|
| `ANSWER` | Request was admitted and sufficient evidence/policy/release context permitted an answer. |
| `ABSTAIN` | Request was admitted but evidence was missing, stale, unresolved, conflicted, or insufficient. |
| `DENY` | Policy, rights, sensitivity, release, or role gates denied evaluation/display. |
| `ERROR` | Request/envelope/schema/runtime failure prevented evaluation. |

---

## Validation expectations

NEEDS VERIFICATION:

- schema expansion beyond `id`, `version`, and `spec_hash`;
- validator path and CI wiring;
- fixtures for valid public request, steward request, stale map context, denied caller role, missing release ref, unresolved evidence ref, sensitive context, malformed query, and AI-triggered request;
- runtime/API route behavior;
- MapContextEnvelope resolution/admission;
- policy/focus and policy/ui integration;
- AIReceipt creation or reference behavior;
- accessibility-state handling;
- public UI refusal/deny/abstain copy.

---

## Open questions

- Should `FocusRequest` live under `contracts/ui/`, `contracts/focus_mode/`, or both with split responsibilities?
- Should query text be part of FocusRequest while map state remains in MapContextEnvelope?
- Which caller roles are accepted and how do they map to policy?
- Should FocusRequest be persisted, logged, redacted, or treated as transient runtime input?
- What is the final request/response object boundary between FocusRequest, FocusModePayload, and RuntimeResponseEnvelope?

---

## Rollback

Rollback is required if this contract becomes FocusModePayload authority, runtime response authority, EvidenceBundle closure, PolicyDecision, ReleaseManifest, AIReceipt, direct model client permission, raw/canonical-store access, UI implementation, schema authority, or proof storage.

Rollback target for this expansion: previous scaffold blob SHA `311305688c34d61b38976b073641725048423594`.

<p align="right"><a href="#top">Back to top</a></p>
