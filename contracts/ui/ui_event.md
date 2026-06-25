<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-ui-event
title: contracts/ui/ui_event.md — UIEvent Contract
type: semantic-contract
version: v0.2
status: draft; PROPOSED; schema-stub-confirmed; ui-family; interaction-event; telemetry-adjacent; evidence-dependent
owners: OWNER_TBD — UI steward · Runtime steward · Evidence steward · Telemetry steward · Policy steward · Schema steward · Accessibility steward · Docs steward
created: NEEDS VERIFICATION — greenfield scaffold existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; ui; ui-event; interaction-event; projection; telemetry-adjacent; no-sovereign-truth
tags: [kfm, contracts, ui, ui-event, UIEvent, interaction, EvidenceDrawerPayload, FocusRequest, FocusResponse, TrustBadgeState, RuntimeResponseEnvelope, PolicyDecision, EvidenceRef, telemetry]
related:
  - ./README.md
  - ./focus_request.md
  - ./focus_response.md
  - ./evidence_drawer_payload.md
  - ./citation_validation_report.md
  - ./trust_badge_state.md
  - ./story_manifest.md
  - ./story_node.md
  - ../runtime/runtime_response_envelope.md
  - ../runtime/decision_envelope.md
  - ../policy/policy_decision.md
  - ../evidence/evidence_ref.md
  - ../evidence/evidence_bundle.md
  - ../../schemas/contracts/v1/ui/ui_event.schema.json
  - ../../policy/ui/
  - ../../fixtures/ui/ui_event/
  - ../../docs/architecture/ui/README.md
  - ../../docs/standards/TELEMETRY_MINIMUMS.md
notes:
  - "Expanded from a PROPOSED greenfield scaffold at `contracts/ui/ui_event.md`."
  - "A paired UI schema stub exists at `schemas/contracts/v1/ui/ui_event.schema.json`; it requires only `id`, allows additional properties, and names this contract doc."
  - "UI contracts are semantic meaning only and must stay downstream of governed API/runtime/evidence/policy/release surfaces."
  - "Telemetry minimums say telemetry carries evidence and does not create truth; UIEvent follows the same carrier-not-truth boundary."
  - "Rollback target for this expansion is previous scaffold blob SHA `ff2739d4e0da5d73226336b9bc03cfa0d51acfcb`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UIEvent Contract

> `UIEvent` is the UI-facing event envelope for meaningful user-interface interactions and trust-surface state changes. It records or carries interaction context for governed UI/runtime flows; it is not evidence, not telemetry truth, not policy execution, not release approval, not proof storage, and not UI implementation.

<p>
  <img alt="Status: PROPOSED" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Family: UI" src="https://img.shields.io/badge/family-ui-0a7ea4">
  <img alt="Object: UIEvent" src="https://img.shields.io/badge/object-UIEvent-purple">
  <img alt="Schema: stub confirmed" src="https://img.shields.io/badge/schema-stub__confirmed-orange">
  <img alt="Boundary: event not truth" src="https://img.shields.io/badge/boundary-event__not__truth-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/ui/ui_event.md`  
**Paired schema:** `schemas/contracts/v1/ui/ui_event.schema.json`  
**Schema posture:** PROPOSED stub; required field `id` only; `additionalProperties: true`  
**Telemetry posture:** telemetry-adjacent carrier, not truth  
**Truth posture:** CONFIRMED target was a greenfield scaffold · CONFIRMED paired UI schema stub exists and names this contract doc · CONFIRMED UI lane excludes implementation, schemas, policy, evidence stores, raw/internal access, and release authority · NEEDS VERIFICATION for final schema, fixtures, validator, UI implementation, runtime integration, policy handling, and telemetry wiring

**Quick jumps:** [Purpose](#purpose) · [Repo fit](#repo-fit) · [Meaning](#meaning) · [Authority split](#authority-split) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended UI fields](#recommended-ui-fields) · [Event families](#event-families) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This contract defines how KFM UI events are described when they cross a governed boundary, feed a runtime action, support audit/debug review, or connect UI surfaces to evidence and policy context.

It answers:

- which UI interaction happened;
- which surface, object, layer, feature, story node, drawer payload, focus request, or trust badge the event involved;
- which evidence, policy, release, runtime, or telemetry refs frame the event;
- what the event must not imply.

It does not answer whether a claim is true, whether evidence is complete, whether policy admits display, whether release is approved, or whether UI code is implemented.

## Repo fit

| Relationship | Path | Status |
|---|---|---|
| This semantic contract | `contracts/ui/ui_event.md` | PROPOSED / current file |
| UI contract lane | `contracts/ui/README.md` | CONFIRMED adjacent lane guide |
| Paired UI schema | `schemas/contracts/v1/ui/ui_event.schema.json` | CONFIRMED permissive stub |
| Runtime response | `contracts/runtime/runtime_response_envelope.md` | Related finite outcome boundary |
| UI policy home | `policy/ui/` | Referenced by schema; implementation depth NEEDS VERIFICATION |
| UI fixtures | `fixtures/ui/ui_event/` | Referenced by schema; existence/coverage NEEDS VERIFICATION |
| Telemetry standard | `docs/standards/TELEMETRY_MINIMUMS.md` | CONFIRMED carrier-not-truth boundary |

## Meaning

A `UIEvent` is a bounded interaction or state-transition record for UI flows.

```text
user interaction / UI state change
  -> UIEvent
  -> governed runtime, telemetry carrier, or audit trail
  -> policy/evidence/release-aware downstream handling
```

The event can describe what happened in the UI. It must not become evidence, proof, release approval, or policy authority.

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| UI event meaning | `contracts/ui/ui_event.md` | This file. |
| UI object meaning | `contracts/ui/` | UI semantic contracts. |
| Runtime outcome | `contracts/runtime/` | Runtime owns finite outcome envelopes. |
| Evidence support | `contracts/evidence/` | EvidenceBundle and EvidenceRef support claims. |
| Policy/admissibility | `policy/ui/`, `policy/runtime/`, `policy/evidence/` | Policy owns allow/restrict/deny/abstain decisions. |
| Telemetry requirements | `docs/standards/TELEMETRY_MINIMUMS.md` and telemetry roots | Telemetry carries evidence; it does not create truth. |
| Machine shape | `schemas/contracts/v1/ui/ui_event.schema.json` | Current stub only. |
| UI implementation | UI/web/app roots | Component code and state management stay outside contracts. |
| Release/correction/rollback | `release/` and release contracts | Publication state remains separate. |

## Schema posture

The paired UI schema currently confirms:

| Field | Required | Shape |
|---|---:|---|
| `id` | yes | string |
| `version` | no | string |
| `spec_hash` | no | string |

The schema allows additional properties, so the rest of this contract is semantic guidance until schema expansion is verified.

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Recording a meaningful UI interaction | Yes | Must avoid sensitive payload leakage. |
| Triggering a governed runtime request | Conditional | Must preserve request/admission boundaries. |
| Connecting a UI action to evidence or policy refs | Conditional | Use refs, not raw proof/source payloads. |
| Supporting telemetry or audit review | Conditional | Carrier only; not truth. |
| Treating event as evidence | No | EvidenceBundle/EvidenceRef own evidence support. |
| Treating event as policy decision | No | Policy roots own decisions. |
| Treating event as release approval | No | Release roots own publication state. |

## Exclusions

| Do not use this contract as | Correct home or behavior |
|---|---|
| Evidence or proof | Use EvidenceBundle, EvidenceRef, receipts, and proof roots. |
| Policy authority | Use PolicyDecision and policy roots. |
| Runtime response authority | Use runtime contracts. |
| Telemetry standard | Use telemetry standards and observability roots. |
| UI component implementation | Use UI/web/app roots. |
| Raw clickstream dump | Use governed telemetry with redaction and policy controls. |
| Internal-store access path | Use governed API/released projections only. |

## Recommended UI fields

PROPOSED until schema expansion:

| Field | Meaning |
|---|---|
| `id` | UI event identifier. |
| `version` | Event contract/object version. |
| `spec_hash` | Deterministic baseline hash. |
| `event_type` | focus_request_submitted, drawer_opened, badge_clicked, story_node_selected, export_requested, or accepted type. |
| `surface` | Map, Evidence Drawer, Focus panel, Story player, Layer Catalog, export flow, or accepted surface. |
| `subject_ref` | Feature, layer, claim, story node, badge, payload, or runtime response involved. |
| `request_ref` | Related FocusRequest or runtime request ref. |
| `runtime_response_ref` | Related RuntimeResponseEnvelope ref, if applicable. |
| `evidence_refs` | Optional public-safe EvidenceRef pointers. |
| `policy_decision_refs` | Related policy decision refs. |
| `release_refs` | Related release state refs. |
| `caller_role` | Public/steward/internal role context. |
| `occurred_at` | Event time. |
| `session_ref` | Redacted/public-safe session or interaction reference. |
| `redaction_state` | Public-safe redaction posture for event payload. |
| `caveats` | Any caveats needed for interpreting the event. |

## Event families

| Family | Examples | Required boundary |
|---|---|---|
| `navigation` | map pan, selected feature, story node selection | Do not imply evidence support. |
| `trust_surface` | badge clicked, drawer opened, citation report viewed | Must point to governed details. |
| `focus_mode` | focus request submitted, response viewed | Runtime owns outcome. |
| `export` | export requested, screenshot generated | Must preserve release/citation/caveat posture. |
| `diagnostic` | error state shown, stale state shown | Diagnostic is not evidence. |

## Validation expectations

NEEDS VERIFICATION:

- schema expansion beyond `id`, `version`, and `spec_hash`;
- final event vocabulary;
- validator path and CI wiring;
- fixtures for navigation, trust-surface, focus, export, and diagnostic events;
- telemetry/redaction behavior;
- runtime request/response linkage;
- policy and release linkage;
- accessibility/event-label handling.

## Open questions

- Should `UIEvent` remain a UI contract or move under telemetry/runtime if it becomes operational logging?
- Which events are stored, emitted transiently, or dropped after runtime processing?
- Which event fields are public-safe versus steward/internal only?
- What is the final event vocabulary?

## Rollback

Rollback is required if this contract becomes evidence authority, telemetry truth, policy authority, release approval, runtime response authority, UI implementation, internal-store access, or a raw clickstream capture path.

Rollback target for this expansion: previous scaffold blob SHA `ff2739d4e0da5d73226336b9bc03cfa0d51acfcb`.

<p align="right"><a href="#top">Back to top</a></p>
