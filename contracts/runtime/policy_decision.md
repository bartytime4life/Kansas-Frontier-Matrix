<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-runtime-policy-decision-compat
title: contracts/runtime/policy_decision.md — Runtime PolicyDecision Compatibility Pointer
type: contract-pointer
version: v0.1
status: draft; compatibility; scaffold-replaced; no-parallel-authority; schema-missing
owners: OWNER_TBD — Runtime steward · Policy steward · Contracts steward · Schema steward · Policy-runtime steward · Evidence steward · Release steward · Docs steward · Directory Rules reviewer
created: NEEDS VERIFICATION — file existed before compatibility rewrite
updated: 2026-06-24
policy_label: public; contracts; runtime; policy-decision; compatibility; no-parallel-authority; governed-runtime; policy-boundary
tags: [kfm, contracts, runtime, policy-decision, compatibility, pointer, canonical-policy-decision, decision-envelope, policy-runtime, no-parallel-authority]
related:
  - ./README.md
  - ./decision_envelope.md
  - ./runtime_response_envelope.md
  - ./ai_receipt.md
  - ../policy/README.md
  - ../policy/policy_decision.md
  - ../policy/policy_input_bundle.md
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../schemas/contracts/v1/runtime/policy_decision.schema.json
  - ../../policy/runtime/
  - ../../policy/
  - ../../packages/policy-runtime/README.md
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "Compatibility pointer for the requested runtime `policy_decision.md` path."
  - "The inspected canonical `PolicyDecision` semantic contract lives at `contracts/policy/policy_decision.md`."
  - "The runtime decision transport object is `contracts/runtime/decision_envelope.md`."
  - "No `schemas/contracts/v1/runtime/policy_decision.schema.json` was verified in this session; runtime policy-decision schema placement remains NEEDS VERIFICATION."
  - "This file must not become a second PolicyDecision authority, a policy rule, a runtime transport envelope, or executable policy behavior."
  - "Rollback target for this compatibility rewrite is previous scaffold blob SHA `96504ea65bc18ad4281d578924b61c1eb4195c56`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Runtime PolicyDecision Compatibility Pointer

> Compatibility pointer for `contracts/runtime/policy_decision.md`. The inspected canonical `PolicyDecision` semantic contract is [`../policy/policy_decision.md`](../policy/policy_decision.md). Runtime decision transport belongs to [`./decision_envelope.md`](./decision_envelope.md). This runtime path must not become a duplicate policy-decision authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility" src="https://img.shields.io/badge/path-compatibility-lightgrey">
  <img alt="Canonical: policy PolicyDecision" src="https://img.shields.io/badge/canonical-policy__PolicyDecision-blue">
  <img alt="Runtime: DecisionEnvelope" src="https://img.shields.io/badge/runtime-DecisionEnvelope-0a7ea4">
  <img alt="Schema: missing" src="https://img.shields.io/badge/runtime__schema-missing-orange">
  <img alt="Posture: no parallel authority" src="https://img.shields.io/badge/posture-no__parallel__authority-critical">
</p>

**Status:** draft compatibility / scaffold replacement  
**Path:** `contracts/runtime/policy_decision.md`  
**Canonical inspected PolicyDecision contract:** [`../policy/policy_decision.md`](../policy/policy_decision.md)  
**Runtime decision envelope:** [`./decision_envelope.md`](./decision_envelope.md)  
**Canonical policy schema:** `schemas/contracts/v1/policy/policy_decision.schema.json`  
**Runtime policy-decision schema:** `schemas/contracts/v1/runtime/policy_decision.schema.json` — not verified / not found in this session  
**Policy authority:** `policy/`, `policy/runtime/`, and policy-runtime packages, not this file  
**Runtime/API authority:** implementation/API roots, not this file  
**Truth posture:** CONFIRMED runtime target scaffold replaced · CONFIRMED canonical PolicyDecision exists under `contracts/policy/` · CONFIRMED DecisionEnvelope is the runtime decision object · CONFIRMED no runtime policy-decision schema was verified · PROPOSED compatibility alias until ADR/steward review accepts or removes this runtime path

## Quick jumps

[Purpose](#purpose) · [Why this is compatibility only](#why-this-is-compatibility-only) · [Repo fit](#repo-fit) · [Accepted changes here](#accepted-changes-here) · [Exclusions](#exclusions) · [Runtime boundary](#runtime-boundary) · [Validation checklist](#validation-checklist) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This file exists to make the runtime `policy_decision.md` path safe and unambiguous after it appeared as a planned/inventory-derived scaffold.

It points maintainers to the accepted authority split:

```text
contracts/policy/policy_decision.md     # canonical inspected PolicyDecision semantic contract
contracts/runtime/decision_envelope.md  # runtime finite decision envelope
contracts/runtime/policy_decision.md    # this compatibility pointer
```

Any change to `PolicyDecision` meaning belongs in the policy contract. Any change to runtime decision transport belongs in `DecisionEnvelope` or `RuntimeResponseEnvelope`, with corresponding schema, fixture, policy, validator, runtime, and test changes.

---

## Why this is compatibility only

The runtime file started as a scaffold from a domain API-contract inventory. Current evidence shows:

- the policy lane already defines `PolicyDecision` as the canonical semantic object for a single policy evaluation result;
- the runtime lane already defines `DecisionEnvelope` as the runtime-facing finite decision object;
- no runtime-specific `policy_decision` schema was verified in this session.

Therefore this runtime file should not claim policy-decision authority. It should remain a compatibility pointer unless an accepted ADR or migration explicitly creates a distinct runtime policy-decision object.

---

## Repo fit

| Responsibility | Correct home | Relationship to this file |
|---|---|---|
| Canonical PolicyDecision semantic meaning | `contracts/policy/policy_decision.md` | Inspected canonical policy-decision contract. |
| Runtime finite decision transport | `contracts/runtime/decision_envelope.md` | Runtime-facing decision envelope. |
| Runtime response envelope | `contracts/runtime/runtime_response_envelope.md` | Client/API-facing response envelope. |
| AI run receipt | `contracts/runtime/ai_receipt.md` | AI accountability receipt that may reference policy decision. |
| Runtime policy-decision compatibility path | `contracts/runtime/policy_decision.md` | This pointer; not canonical. |
| PolicyDecision schema | `schemas/contracts/v1/policy/policy_decision.schema.json` | Shape authority for canonical policy decision. |
| Runtime policy rules | `policy/runtime/` | Runtime rule/admissibility behavior. |
| Policy rules | `policy/` and policy-family roots | Policy rule authority. |
| Policy runtime implementation | `packages/policy-runtime/` or accepted runtime roots | Executable policy helpers. |
| Runtime/API implementation | accepted app/package/API roots | Execution/transport behavior. |

---

## Accepted changes here

Only conservative compatibility maintenance belongs here:

| Accepted change | Purpose |
|---|---|
| Update links to canonical policy/runtime contracts | Keep stale runtime references navigable. |
| Add migration note | Explain future move, deletion, or canonicalization. |
| Add backlink audit | Find stale links to runtime policy-decision path. |
| Add validation note | Track schema/migration drift without defining a new schema. |

Do not add `PolicyDecision` field semantics here. Put policy-decision meaning in [`../policy/policy_decision.md`](../policy/policy_decision.md) unless an accepted ADR changes the canonical home.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| Canonical PolicyDecision fields | `contracts/policy/policy_decision.md` | Avoids duplicate policy-decision authority. |
| Runtime decision-envelope fields | `contracts/runtime/decision_envelope.md` | Runtime transport already has a contract. |
| JSON Schema | `schemas/contracts/v1/policy/` or accepted runtime schema home | Schemas own shape. |
| Policy rules | `policy/`, `policy/runtime/`, policy-family roots | Policy owns admissibility. |
| Policy runtime code | `packages/policy-runtime/` or accepted runtime roots | Execution belongs outside contracts. |
| Runtime/API behavior | apps/packages/API roots | Runtime implementation is not contract prose. |
| Receipts/proofs/logs | accepted receipt/proof/log homes | Audit artifacts remain separately inspectable. |
| Release manifests or promotion decisions | `contracts/release/` and `release/` | Release state is distinct from policy-decision meaning. |

---

## Runtime boundary

Runtime systems may carry policy-decision refs, policy-family context, reasons, obligations, and outcomes. They should not redefine the canonical `PolicyDecision` object.

A safe runtime path is:

```text
PolicyDecision (policy)
  -> DecisionEnvelope (runtime decision transport)
  -> RuntimeResponseEnvelope / AIReceipt as needed
  -> governed API/UI/map/AI client surface
```

Public clients must not treat this compatibility pointer as proof of policy evaluation, runtime permission, release approval, or evidence truth.

---

## Validation checklist

- [ ] Decide whether the runtime `policy_decision` path should stay as compatibility, be deleted, or be formalized by ADR.
- [ ] If formalized, define why runtime needs a distinct policy-decision object beyond `contracts/policy/policy_decision.md` and `contracts/runtime/decision_envelope.md`.
- [ ] Verify no schema, fixture, validator, or runtime code depends on this path as canonical without migration notes.
- [ ] Ensure canonical policy-decision links remain valid.
- [ ] Verify `DecisionEnvelope` remains the runtime decision transport object.
- [ ] Verify no public client uses this file as runtime permission or policy truth.

---

## Open questions

- Should `contracts/runtime/policy_decision.md` remain as a compatibility pointer only?
- Should any stale references be migrated to `contracts/policy/policy_decision.md`?
- Should runtime envelopes reference `PolicyDecision` directly, or use `DecisionEnvelope.policy_family` plus a separate `policy_decision_ref` in response/receipt contracts?
- Should a runtime-specific policy-decision schema ever exist, or would that create avoidable drift?

---

## Rollback

Rollback is required if this file is used as canonical policy-decision meaning, policy rule authority, executable policy behavior, runtime transport authority, release approval, evidence authority, public API/UI/map/AI permission, or a replacement for `DecisionEnvelope`.

Rollback target for this compatibility rewrite: previous scaffold blob SHA `96504ea65bc18ad4281d578924b61c1eb4195c56`.

<p align="right"><a href="#top">Back to top</a></p>
