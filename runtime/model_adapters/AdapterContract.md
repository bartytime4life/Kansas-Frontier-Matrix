# `runtime/model_adapters/AdapterContract.md` — Runtime Adapter Contract Note

Runtime-lane adapter contract note for the KFM model-adapter boundary: **FocusRequest in, DecisionEnvelope out, cite-or-abstain by default**.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-model-adapters-adapter-contract
title: runtime/model_adapters/AdapterContract.md — Runtime Adapter Contract Note
type: runtime-note; adapter-contract-note; interface-boundary; non-canonical-contract
version: v0.2
status: draft; expanded-stub; descriptive-contract-note; NEEDS VERIFICATION
owners: OWNER_TBD — Runtime steward · Governed-AI steward · API steward · Policy steward · Evidence steward · Docs steward
created: NEEDS VERIFICATION — short stub existed before v0.2 expansion
updated: 2026-07-05
policy_label: public; runtime; model-adapter; governed-ai; finite-outcome; cite-or-abstain
tags: [kfm, runtime, model-adapters, adapter-contract, focus-request, decision-envelope, cite-or-abstain, finite-outcomes, ai-receipt]
related:
  - ./README.md
  - ./mock/README.md
  - ../mock/README.md
  - ../AI/README.md
  - ../envelopes/README.md
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
  - ../../fixtures/
  - ../../tests/
  - ../../tools/validators/
  - ../../data/
  - ../../release/
notes:
  - "Expanded from the prior stub: FocusRequest in, DecisionEnvelope out. Cite-or-abstain."
  - "Current-session search did not confirm canonical FocusRequest, DecisionEnvelope, RuntimeResponseEnvelope, AIReceipt, or AdapterContract definitions elsewhere in the repo index."
  - "This file is a runtime-lane contract note, not canonical semantic contract authority. Canonical meaning belongs under contracts/ when accepted. Machine-checkable shape belongs under schemas/."
  - "This file does not prove adapter implementation, DTO implementation, schema validity, test coverage, policy enforcement, citation validation, AIReceipt emission, RuntimeResponseEnvelope behavior, or release readiness."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: runtime" src="https://img.shields.io/badge/root-runtime%2F-blue">
  <img alt="Lane: model adapters" src="https://img.shields.io/badge/lane-model__adapters-purple">
  <img alt="Posture: cite or abstain" src="https://img.shields.io/badge/posture-cite__or__abstain-green">
  <img alt="Boundary: not canonical contract" src="https://img.shields.io/badge/boundary-not__canonical__contract-critical">
</p>

**Status:** draft / descriptive runtime interface note
**Path:** `runtime/model_adapters/AdapterContract.md`
**Core rule:** `FocusRequest` in → `DecisionEnvelope` out → cite-or-abstain.
**Truth posture:** CONFIRMED this file existed as a short stub; CONFIRMED adjacent model-adapter, mock-runtime, governed-AI, and envelope README boundaries; NEEDS VERIFICATION for canonical contract, schema, DTO, test, validator, policy, receipt, and runtime implementation.

## Quick jumps

[Purpose](#purpose) · [Authority boundary](#authority-boundary) · [Contract summary](#contract-summary) · [Adapter flow](#adapter-flow) · [FocusRequest minimum](#focusrequest-minimum) · [DecisionEnvelope minimum](#decisionenvelope-minimum) · [Finite outcomes](#finite-outcomes) · [Adapter obligations](#adapter-obligations) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Validation](#validation) · [Open questions](#open-questions)

---

## Purpose

This file documents the runtime adapter boundary that model adapters must preserve.

It is intentionally small:

```text
FocusRequest in
  -> adapter evaluates only governed, allowed context
  -> DecisionEnvelope out
  -> cite-or-abstain by default
```

A model adapter may be mock, local, provider-backed, or future-provider-neutral. Regardless of runtime mode, it must stay downstream of evidence, policy, citation validation, finite outcomes, receipts, and release state.

## Authority boundary

This file is not the canonical semantic contract. It is a runtime-lane interface note.

| Authority area | Correct home | This file's role |
|---|---|---|
| Semantic meaning | `contracts/` | Describes intended runtime boundary only. |
| Machine-checkable shape | `schemas/` | Names expected fields, but does not define JSON Schema. |
| Runtime adapter implementation | `runtime/model_adapters/`, `runtime/ollama/`, local/provider lanes | Records adapter obligations; does not implement them. |
| Mock adapter behavior | `runtime/model_adapters/mock/` and `runtime/mock/` | Points to mock-first testing posture. |
| Runtime response envelope helpers | `runtime/envelopes/` | Aligns with finite-outcome envelope posture. |
| Policy rules | `policy/` | Requires policy decisions; does not define them. |
| Fixtures and tests | `fixtures/`, `tests/` | Requires evidence before behavior is claimed. |
| Receipts and proofs | accepted `data/` receipt/proof roots | Requires receipt pointers when applicable. |
| Release decisions | `release/` | Cannot publish, approve, correct, or roll back. |

## Contract summary

| Side | Object | Minimum meaning | Status |
|---|---|---|---|
| Input | `FocusRequest` | A bounded request for model-adapter interpretation over governed context. | PROPOSED / NEEDS VERIFICATION |
| Output | `DecisionEnvelope` | A finite-outcome response envelope carrying answer/abstain/deny/error posture plus support pointers. | PROPOSED / NEEDS VERIFICATION |
| Default truth posture | cite-or-abstain | The adapter must abstain when evidence, policy, citation, or release support is insufficient. | CONFIRMED doctrine posture / implementation NEEDS VERIFICATION |
| Publication posture | no direct publication | Adapter output cannot publish or approve public display. | CONFIRMED doctrine posture / implementation NEEDS VERIFICATION |

## Adapter flow

```text
FocusRequest
  -> scope check
  -> evidence support check
  -> policy check
  -> runtime adapter execution, if allowed
  -> citation/support validation, if answer-like output is produced
  -> finite DecisionEnvelope
  -> AIReceipt / RunReceipt pointer, when applicable
  -> governed caller decides next action
```

The adapter may return an answer only when the request is in scope, policy permits response, evidence support is sufficient, citation posture is valid where required, and the output is wrapped in a finite outcome.

## `FocusRequest` minimum

A canonical shape still needs a contract and schema. Until then, adapter notes should treat these as minimum expected fields:

| Field | Purpose | Status |
|---|---|---|
| `request_id` | Deterministic or traceable request identifier. | PROPOSED |
| `request_type` | Bounded request family, such as Focus Mode question, evidence summary, or review helper. | PROPOSED |
| `user_intent` | Short request intent after caller-side normalization. | PROPOSED |
| `scope` | Domain, geography, time, layer, feature, claim, or review scope. | PROPOSED |
| `evidence_refs` | EvidenceRef pointers or empty when unsupported. | PROPOSED |
| `policy_context` | Access role, sensitivity posture, rights posture, and other policy inputs. | PROPOSED |
| `release_context` | Release label, stale/correction state, publication state, or N/A. | PROPOSED |
| `allowed_tools` | Runtime tools or adapter capabilities permitted for this request. | PROPOSED |
| `citation_required` | Whether answer-like output must cite evidence. | PROPOSED |
| `receipt_context` | Run, trace, or receipt linkage expected by caller. | PROPOSED |

A `FocusRequest` must not carry RAW, WORK, QUARANTINE, unpublished candidate payloads, private secrets, provider credentials, private chain-of-thought, or direct canonical-store dumps as normal public-path input.

## `DecisionEnvelope` minimum

A canonical shape still needs a contract and schema. Until then, adapter notes should treat these as minimum expected fields:

| Field | Purpose | Status |
|---|---|---|
| `request_id` | Echoes or links the triggering `FocusRequest`. | PROPOSED |
| `outcome` | One of `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. | PROPOSED |
| `reason_codes` | Machine-readable reasons for finite outcome. | PROPOSED |
| `answer` | Optional answer text only when outcome is `ANSWER`. | PROPOSED |
| `citations` | Evidence/citation pointers when answer-like output cites support. | PROPOSED |
| `evidence_refs` | Evidence support actually used or checked. | PROPOSED |
| `policy_state` | Policy decision or policy posture used by runtime. | PROPOSED |
| `freshness_state` | Current/stale/unknown posture where material. | PROPOSED |
| `correction_state` | Superseded, corrected, withdrawn, or N/A posture where material. | PROPOSED |
| `adapter_ref` | Adapter family/name/version or mock reference. | PROPOSED |
| `receipt_ref` | AIReceipt, RunReceipt, validation receipt, or N/A. | PROPOSED |
| `debug_public` | Optional safe diagnostics; never private chain-of-thought. | PROPOSED |

A `DecisionEnvelope` must not present generated language as evidence, policy, review, release, correction, rollback, or publication authority.

## Finite outcomes

| Outcome | Use when | Required posture |
|---|---|---|
| `ANSWER` | The request is in scope, policy allows response, evidence support is sufficient, and citation posture is valid where required. | Include support pointers and receipt/envelope posture where applicable. |
| `ABSTAIN` | Evidence support, citation support, source authority, freshness, scope, or confidence is insufficient. | Explain the support gap without inventing an answer. |
| `DENY` | Policy, rights, sensitivity, release state, access role, or governance posture forbids response. | Return deny reason codes without exposing protected content. |
| `ERROR` | Runtime, adapter, validation, configuration, envelope, or dependency failure prevents completion. | Return safe diagnostics and preserve receipt/run linkage where possible. |

## Adapter obligations

| Obligation | Requirement |
|---|---|
| Stay provider-neutral | Mock, local, and provider-backed adapters should share the same boundary where practical. |
| Preserve evidence hierarchy | EvidenceBundle and source records outrank generated text. |
| Preserve policy hierarchy | Policy decisions and access posture outrank model capability. |
| Preserve citation posture | Cite-or-abstain is default for answer-like output. |
| Preserve finite outcomes | Never return unbounded free-text as the only result. |
| Preserve receipt posture | Emit or link AIReceipt, RunReceipt, validation receipt, or runtime envelope records when applicable. |
| Preserve privacy | Never store credentials, secrets, private config, private chain-of-thought, or private model internals here. |
| Preserve release boundary | Adapter output is not publication and does not approve map/API/UI exposure. |
| Preserve testability | Behavior claims require fixtures, tests, validators, or runtime evidence. |

## What belongs here

- This runtime adapter contract note.
- Descriptive interface boundary notes for `FocusRequest` and `DecisionEnvelope` until canonical contracts/schemas exist.
- Compatibility notes for mock, local, and provider-backed adapter behavior.
- Pointers to runtime adapter cards, runtime envelopes, mock adapter notes, fixtures, tests, policy, receipts, and validators.
- Open questions about DTO naming, schema pointers, and canonical contract placement.

## What does not belong here

| Do not put this in `AdapterContract.md` | Correct home |
|---|---|
| Canonical semantic contract authority | `contracts/` |
| JSON Schema definitions | `schemas/` |
| Policy rules or policy decisions | `policy/` and governed review roots |
| Adapter implementation code | accepted runtime/model-adapter implementation lane |
| Provider credentials, tokens, secrets, private `.env`, or private config | never in repo |
| Fixture payloads or golden outputs | `fixtures/` |
| Executable tests | `tests/` |
| Validator source code | `tools/validators/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | `data/` lifecycle roots |
| EvidenceBundles, SourceDescriptors, receipts, proofs, catalogs, or release manifests | accepted `data/`, source-registry, proof, receipt, catalog, or release roots |
| Release decisions, correction notices, or rollback records | `release/` |
| Generated text treated as truth, evidence, policy, review, or publication authority | nowhere |

## Validation

```bash
find runtime/model_adapters -maxdepth 4 -type f | sort
find runtime/envelopes runtime/mock -maxdepth 4 -type f 2>/dev/null | sort
find contracts schemas policy fixtures tests tools/validators -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/runtime tests/api tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once the accepted runtime adapter test commands are confirmed.

## Review checklist

- [ ] This note is not cited as canonical semantic contract authority.
- [ ] `FocusRequest` fields are backed by contract/schema before implementation claims are made.
- [ ] `DecisionEnvelope` fields are backed by contract/schema before implementation claims are made.
- [ ] Adapter output uses finite outcomes.
- [ ] `ANSWER` requires evidence/citation support where material.
- [ ] `ABSTAIN`, `DENY`, and `ERROR` preserve safe reason-code posture.
- [ ] Policy, rights, sensitivity, release, stale, and correction states are preserved where material.
- [ ] RuntimeResponseEnvelope and AIReceipt handoff are linked when applicable.
- [ ] Fixtures, tests, validators, or runtime evidence support any behavior claim.
- [ ] No generated text is treated as evidence, policy, review, release, or publication authority.

## Open questions

| Question | Status |
|---|---|
| Should the canonical semantic home be `contracts/runtime/AdapterContract.md`, `contracts/ai/`, or another accepted contract lane? | NEEDS VERIFICATION |
| Should the schema home be `schemas/contracts/v1/runtime/adapter_contract.schema.json` or another accepted schema path? | NEEDS VERIFICATION |
| Are `FocusRequest` and `DecisionEnvelope` the final object names, or compatibility names pending ADR? | NEEDS VERIFICATION |
| Should `DecisionEnvelope` be aligned with `RuntimeResponseEnvelope`, or should it remain a separate object family? | NEEDS VERIFICATION |
| Which fixtures and tests prove `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior? | NEEDS VERIFICATION |
| Which CI workflow, if any, currently validates runtime adapter behavior? | NEEDS VERIFICATION |
