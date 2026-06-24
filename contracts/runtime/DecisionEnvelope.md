<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-runtime-decision-envelope-compat
title: contracts/runtime/DecisionEnvelope.md — DecisionEnvelope Compatibility Pointer
type: contract-pointer
version: v0.1
status: draft; compatibility; legacy-case-alias; no-parallel-authority
owners: OWNER_TBD — Runtime steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Docs steward · Directory Rules reviewer
created: NEEDS VERIFICATION — file existed before compatibility rewrite
updated: 2026-06-24
policy_label: public; contracts; runtime; decision-envelope; compatibility; legacy-case-alias; no-parallel-authority; governed-runtime
tags: [kfm, contracts, runtime, DecisionEnvelope, decision-envelope, compatibility, pointer, legacy-case, schema-paired, finite-outcomes, no-parallel-authority]
related:
  - ./README.md
  - ./decision_envelope.md
  - ./decision_envelope/README.md
  - ../policy/policy_decision.md
  - ../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../policy/runtime/
  - ../../fixtures/contracts/v1/runtime/decision_envelope/
  - ../../tools/validators/validate_decision_envelope.py
notes:
  - "Compatibility pointer for the requested CamelCase `contracts/runtime/DecisionEnvelope.md` path."
  - "The canonical semantic contract is `contracts/runtime/decision_envelope.md`; the paired schema also points to that snake_case path."
  - "This file must not duplicate or supersede `decision_envelope.md`."
  - "This pointer does not create schema authority, executable runtime behavior, policy authority, public API/UI behavior, release approval, proof/receipt authority, or AI truth claims."
  - "Previous file was a scaffold from `docs/domains/archaeology/CONTINUITY_INVENTORY.md`; rollback target is blob SHA `19551286ed575c9e80748e48ea62c90ad537c637`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# DecisionEnvelope Compatibility Pointer

> Compatibility pointer for the legacy/CamelCase `DecisionEnvelope.md` path. The canonical runtime contract is [`decision_envelope.md`](./decision_envelope.md). Do not treat this file as a second `DecisionEnvelope` contract authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility" src="https://img.shields.io/badge/path-compatibility-lightgrey">
  <img alt="Canonical: decision_envelope.md" src="https://img.shields.io/badge/canonical-decision__envelope.md-blue">
  <img alt="Authority: pointer only" src="https://img.shields.io/badge/authority-pointer__only-lightgrey">
  <img alt="Schema: paired" src="https://img.shields.io/badge/schema-paired-green">
  <img alt="Posture: no parallel authority" src="https://img.shields.io/badge/posture-no__parallel__authority-critical">
</p>

**Status:** draft compatibility / legacy-case alias  
**Path:** `contracts/runtime/DecisionEnvelope.md`  
**Canonical semantic contract:** [`./decision_envelope.md`](./decision_envelope.md)  
**Object-folder pointer:** [`./decision_envelope/README.md`](./decision_envelope/README.md)  
**Paired schema:** `schemas/contracts/v1/runtime/decision_envelope.schema.json`  
**Policy authority:** `policy/runtime/`, not this file  
**Runtime/API authority:** implementation/API roots, not this file  
**Truth posture:** CONFIRMED scaffold replaced · CONFIRMED canonical snake_case contract exists · CONFIRMED paired schema points to `contracts/runtime/decision_envelope.md` · CONFIRMED schema has finite outcomes and closed additional properties · PROPOSED compatibility alias until ADR/steward review accepts or removes CamelCase paths

---

## Purpose

This file exists only to prevent ambiguity from older or inventory-derived references to:

```text
contracts/runtime/DecisionEnvelope.md
```

The canonical contract remains:

```text
contracts/runtime/decision_envelope.md
```

Any change to `DecisionEnvelope` meaning belongs in the canonical snake_case file, paired schema, fixtures, validators, policy, tests, and runtime implementation as appropriate.

---

## Why this is not canonical

The verified paired schema names the contract document as:

```text
contracts/runtime/decision_envelope.md
```

The verified schema also uses the object title:

```text
decision_envelope
```

That means this CamelCase path is a compatibility alias, not the schema-paired semantic home.

---

## Schema-confirmed surface

The paired schema confirms the runtime envelope uses:

| Field | Required | Schema-confirmed shape |
|---|---:|---|
| `decision_id` | yes | string matching `^[a-z][a-z0-9_:.-]*$` |
| `outcome` | yes | enum: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| `policy_family` | yes | enum: `promotion`, `access`, `render`, `capability`, `consent`, `sensitivity` |
| `reasons` | yes | array of strings |
| `obligations` | yes | array of strings |
| `evaluated_at` | yes | date-time string |
| `id` | no | string |
| `decision` | no | enum: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| `reason_code` | no | string |
| `evidence_refs` | no | array of strings |
| `spec_hash` | no | string |
| `version` | no | string |
| `issued_at` | no | date-time string |

The schema also confirms:

```text
additionalProperties: false
```

---

## Anti-collapse rules

Do not use this compatibility pointer as:

- the canonical semantic contract;
- a machine schema;
- runtime code;
- an API response contract;
- a policy rule;
- an evidence record;
- a release decision;
- a proof or receipt;
- an AI answer authority.

`DecisionEnvelope` is a governed runtime envelope. It remains distinct from `PolicyDecision`, `PromotionDecision`, `ReleaseManifest`, and downstream API/UI/AI rendering.

---

## Accepted changes here

Only conservative maintenance belongs here:

| Accepted change | Purpose |
|---|---|
| Update pointer links | Keep canonical path discoverable. |
| Add migration note | Explain any future path move or deletion. |
| Add backlink audit | Identify stale links to CamelCase path. |
| Add rollback note | Preserve reversible cleanup. |

Do not add field semantics here. Put those in [`decision_envelope.md`](./decision_envelope.md).

---

## Rollback

Rollback is required if this file is used to create a duplicate `DecisionEnvelope` contract, override the schema-paired snake_case contract, store runtime instances, claim executable behavior, or authorize public API/UI/map/AI exposure directly.

Rollback target for this compatibility rewrite: previous scaffold blob SHA `19551286ed575c9e80748e48ea62c90ad537c637`.

<p align="right"><a href="#top">Back to top</a></p>
