<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hazards-drought-declaration
title: DroughtDeclaration Contract — Hazards
type: semantic-contract
version: v0.1
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Legal/Administrative seam steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-08-03
updated: 2026-08-03
policy_label: public-with-gates; semantic-contract; hazards; drought; declaration; anti-collapse; source-role-aware; evidence-bound; release-gated; not-for-life-safety
related:
  - ./README.md
  - ./drought_observation.md
  - ../../../schemas/contracts/v1/domains/hazards/drought_declaration.schema.json
  - ../../../schemas/contracts/v1/domains/hazards/drought_observation.schema.json
  - ../../../schemas/contracts/v1/domains/hazards/drought_obs_decl_relationship.schema.json
  - ../../../fixtures/domains/hazards/drought_declaration/
  - ../../../tests/schemas/test_drought_separation_contracts.py
  - ../../../docs/domains/hazards/DROUGHT_ANTI_COLLAPSE.md
  - ../../../policy/domains/hazards/
tags: [kfm, contracts, hazards, drought, DroughtDeclaration, anti-collapse, kwo, watch, warning, emergency, source-role, evidence-bound, not-for-life-safety, release-gated]
notes:
  - "Implements the anti-collapse invariant: Kansas watch/warning/emergency legal stages must not be derived from USDM D0-D4 polygon categories."
  - "Missing or unresolved legal instrument evidence must abstain/hold rather than infer a stage."
  - "Synthetic fixtures only until source identity, rights, retrieval, and release gates are separately closed."
  - "Issue #1943 planning record. This contract itself does not activate a connector, assert a current county stage, create policy, release, deploy, or publish."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# DroughtDeclaration Contract — Hazards

> Semantic contract for `DroughtDeclaration`: a legal or administrative drought declaration or proclamation event that preserves issuing authority, legal instrument reference, effective time, county membership, and declaration-stage vocabulary — and that must never derive its stage from USDM D0–D4 polygon categories.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: Hazards" src="https://img.shields.io/badge/domain-Hazards-b71c1c">
  <img alt="Object: DroughtDeclaration" src="https://img.shields.io/badge/object-DroughtDeclaration-orange">
  <img alt="Boundary: NOT FOR LIFE SAFETY" src="https://img.shields.io/badge/boundary-NOT__FOR__LIFE__SAFETY-critical">
  <img alt="Anti-collapse: watch/warning/emergency ≠ D0-D4" src="https://img.shields.io/badge/anti--collapse-watch%2Fwarning%2Femergency%20%E2%89%A0%20D0--D4-red">
</p>

`contracts/domains/hazards/drought_declaration.md`

## Quick jumps

[Status](#status) · [Anti-collapse rule](#anti-collapse-rule) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Required fields](#required-fields) · [Forbidden fields](#forbidden-fields) · [Time semantics](#time-semantics) · [Legal instrument binding](#legal-instrument-binding) · [Stage vocabulary](#stage-vocabulary) · [County scope](#county-scope) · [Supersession and correction](#supersession-and-correction) · [Rollback](#rollback)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / PROPOSED semantic contract
> **Contract path:** `contracts/domains/hazards/drought_declaration.md`
> **Schema path:** `schemas/contracts/v1/domains/hazards/drought_declaration.schema.json`
> **Fixtures:** `fixtures/domains/hazards/drought_declaration/`
> **Tests:** `tests/schemas/test_drought_separation_contracts.py`
> **Issue:** #1943 planning record — no activation, stage assertion, policy, release, or deployment.

---

## Anti-collapse rule

> [!WARNING]
> **DroughtDeclaration and DroughtObservation are separate, non-substitutable object families.**
>
> Kansas watch/warning/emergency legal stages must never be derived from USDM D0–D4 polygon categories. Missing or unresolved legal instrument evidence must abstain/hold (`declaration_stage: "unknown"`) rather than infer a stage.

The hard invariants governing this separation are enumerated in [`docs/domains/hazards/DROUGHT_ANTI_COLLAPSE.md`](../../../docs/domains/hazards/DROUGHT_ANTI_COLLAPSE.md).

---

## Meaning

`DroughtDeclaration` is a legal or administrative drought declaration or proclamation event. It represents what an issuing authority proclaimed, not what a monitoring program observed.

A `DroughtDeclaration`:

- records the **issuing authority** and **legal instrument reference** for the proclamation;
- preserves the **legal effective time** and, when known, the **rescission/revision time**;
- records **county or governed-area membership** for the declaration;
- uses a **declaration-stage vocabulary** governed by the issuing authority;
- must **never carry a physical observation severity** (`source_native_severity`, `observation_stage`);
- must **never derive its stage from USDM polygon categories** (`usdm_derived` field is forbidden);
- must **abstain** (`declaration_stage: "unknown"`) when the legal instrument is unresolved or the evidence is insufficient;
- must use `successor_ref` to record supersession — **silent supersession is forbidden**.

---

## Repo fit

| Responsibility | Path |
|---|---|
| This semantic contract | `contracts/domains/hazards/drought_declaration.md` |
| Machine schema | `schemas/contracts/v1/domains/hazards/drought_declaration.schema.json` |
| Observation contract (counterpart) | `contracts/domains/hazards/drought_observation.md` |
| Relationship contract | `schemas/contracts/v1/domains/hazards/drought_obs_decl_relationship.schema.json` |
| Fixtures | `fixtures/domains/hazards/drought_declaration/` |
| Tests | `tests/schemas/test_drought_separation_contracts.py` |
| Anti-collapse documentation | `docs/domains/hazards/DROUGHT_ANTI_COLLAPSE.md` |
| Policy | `policy/domains/hazards/` |

---

## Required fields

| Field | Type | Notes |
|---|---|---|
| `object_type` | `"DroughtDeclaration"` | Const discriminator. Prevents substitution with DroughtObservation. |
| `schema_version` | `"v1"` | Schema version. |
| `declaration_id` | `string` (`decl:…`) | Stable identifier for this declaration record. |
| `issuing_authority` | `string` | Name of the issuing authority (e.g. "Kansas Water Office"). |
| `legal_instrument_ref` | `string` \| `null` | Legal instrument reference, or null if unresolved. |
| `legal_instrument_resolution_status` | `"bound"` \| `"unresolved"` \| `"abstain"` | Controls stage assertion. `unresolved` or `abstain` requires `declaration_stage: "unknown"`. |
| `effective_at` | `date-time` | Legal effective time. Distinct from retrieval time and observation time. |
| `rescinded_at` | `date-time` \| `null` | Rescission/revision time, or null if still in effect. |
| `retrieved_at` | `date-time` | Retrieval/ingestion time. Distinct from `effective_at` and `rescinded_at`. |
| `source_ref` | `string` | Governed source descriptor reference. |
| `source_resolution_status` | `"bound"` \| `"unresolved"` | Must be `bound` before downstream use. |
| `county_scope` | object | County or governed-area membership (see [County scope](#county-scope)). |
| `declaration_stage_vocabulary` | enum | Vocabulary governing stage values. |
| `declaration_stage` | enum | Legal stage: `watch`, `warning`, `emergency`, or `unknown`. Must be `unknown` when evidence is unresolved. |
| `review_state` | enum | Review posture. |
| `release_posture` | enum | Release state. Does not grant publication authority. |

---

## Forbidden fields

These fields must never appear on a `DroughtDeclaration`. The schema enforces this with `not: {}`:

| Forbidden field | Reason |
|---|---|
| `usdm_derived` | Stage must never be derived from USDM D0-D4 polygon categories. |
| `observation_stage` | Declarations must never carry a physical observation severity. |

Any undeclared field is also rejected (`additionalProperties: false`).

---

## Time semantics

A `DroughtDeclaration` preserves **three distinct time concepts**:

| Field | Meaning |
|---|---|
| `effective_at` | The legal effective time of the declaration. |
| `rescinded_at` | Time the declaration was rescinded or revised; null if still in effect. |
| `retrieved_at` | Time this record was retrieved or ingested by KFM. |

These are **not interchangeable**. A newer physical observation does not rescind a legal declaration. A later declaration does not rewrite historical observations.

---

## Legal instrument binding

`legal_instrument_ref` references the official proclamation or order document.

When `legal_instrument_resolution_status` is `"bound"`, `legal_instrument_ref` must be a non-null, non-empty string.

When `legal_instrument_resolution_status` is `"unresolved"` or `"abstain"`, `declaration_stage` must be `"unknown"`. **Missing or unresolved legal instrument evidence must abstain/hold rather than infer a stage.** Current legal stage remains `UNKNOWN` unless supported by an unsuperseded official declaration source.

---

## Stage vocabulary

`declaration_stage` uses the `kansas_kwo_2016` vocabulary by default:

| Stage | Meaning |
|---|---|
| `watch` | Drought watch as declared by the issuing authority. |
| `warning` | Drought warning as declared by the issuing authority. |
| `emergency` | Drought emergency as declared by the issuing authority. |
| `unknown` | Stage cannot be determined from available evidence. Required when evidence is unresolved. |

The stage vocabulary must **never include USDM D0–D4 values**. The schema enum explicitly excludes them.

---

## County scope

`county_scope` records county or governed-area membership:

- `all_105_counties: true` indicates all 105 Kansas counties are covered.
- `county_refs` is a list of specific county references, or null if `all_105_counties` is true.
- `county_scope_resolution_status` is `"bound"` or `"unresolved"`.

**Geometry overlap between a declared county and an observation extent is evidence of a relationship only** — not identity, authority transfer, or causal derivation.

---

## Supersession and correction

- `predecessor_ref`: reference to the prior `DroughtDeclaration` this record supersedes.
- `successor_ref`: reference to the `DroughtDeclaration` that supersedes this record (null if current).
- `correction_of`: reference to the declaration this record corrects.

**Silent supersession is forbidden.** When a declaration is known to be superseded, `successor_ref` must be set. A later declaration does not rewrite historical records.

---

## Rollback

Before merge: close the draft and abandon the scoped branch. After any separately authorized merge: use a focused reviewed revert of the contract/schema/fixture/validator packet; preserve historical source and correction identities.

<p align="right"><a href="#top">Back to top</a></p>
