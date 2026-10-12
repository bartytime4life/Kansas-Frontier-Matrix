<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hazards-drought-observation
title: DroughtObservation Contract — Hazards
type: semantic-contract
version: v0.1
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Drought/Hydrology seam steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-08-03
updated: 2026-08-03
policy_label: public-with-gates; semantic-contract; hazards; drought; observation; anti-collapse; source-role-aware; evidence-bound; release-gated; not-for-life-safety
related:
  - ./README.md
  - ./drought_declaration.md
  - ../../../schemas/contracts/v1/domains/hazards/drought_observation.schema.json
  - ../../../schemas/contracts/v1/domains/hazards/drought_declaration.schema.json
  - ../../../schemas/contracts/v1/domains/hazards/drought_obs_decl_relationship.schema.json
  - ../../../fixtures/domains/hazards/drought_observation/
  - ../../../tests/schemas/test_drought_separation_contracts.py
  - ../../../docs/domains/hazards/DROUGHT_ANTI_COLLAPSE.md
  - ../../../policy/domains/hazards/
tags: [kfm, contracts, hazards, drought, DroughtObservation, anti-collapse, usdm, d0-d4, source-role, evidence-bound, not-for-life-safety, release-gated]
notes:
  - "Implements the anti-collapse invariant: D0-D4 USDM polygon categories must never be mapped to Kansas watch/warning/emergency legal stages."
  - "Synthetic fixtures only until source identity, rights, retrieval, and release gates are separately closed."
  - "Issue #1943 planning record. This contract itself does not activate a connector, assert a current county stage, create policy, release, deploy, or publish."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# DroughtObservation Contract — Hazards

> Semantic contract for `DroughtObservation`: a time-bounded physical drought observation or classification record that preserves source identity, geometry reference, source-native severity, and evidence bindings — and that must never carry a legal or administrative stage.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: Hazards" src="https://img.shields.io/badge/domain-Hazards-b71c1c">
  <img alt="Object: DroughtObservation" src="https://img.shields.io/badge/object-DroughtObservation-blue">
  <img alt="Boundary: NOT FOR LIFE SAFETY" src="https://img.shields.io/badge/boundary-NOT__FOR__LIFE__SAFETY-critical">
  <img alt="Anti-collapse: D0-D4 ≠ watch/warning/emergency" src="https://img.shields.io/badge/anti--collapse-D0--D4%20%E2%89%A0%20watch%2Fwarning%2Femergency-red">
</p>

`contracts/domains/hazards/drought_observation.md`

## Quick jumps

[Status](#status) · [Anti-collapse rule](#anti-collapse-rule) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Required fields](#required-fields) · [Forbidden fields](#forbidden-fields) · [Time semantics](#time-semantics) · [Source and evidence binding](#source-and-evidence-binding) · [Geometry binding](#geometry-binding) · [Severity vocabulary](#severity-vocabulary) · [Supersession and correction](#supersession-and-correction) · [Rollback](#rollback)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / PROPOSED semantic contract
> **Contract path:** `contracts/domains/hazards/drought_observation.md`
> **Schema path:** `schemas/contracts/v1/domains/hazards/drought_observation.schema.json`
> **Fixtures:** `fixtures/domains/hazards/drought_observation/`
> **Tests:** `tests/schemas/test_drought_separation_contracts.py`
> **Issue:** #1943 planning record — no activation, stage assertion, policy, release, or deployment.

---

## Anti-collapse rule

> [!WARNING]
> **DroughtObservation and DroughtDeclaration are separate, non-substitutable object families.**
>
> USDM D0–D4 polygon classifications must never be mapped to Kansas watch/warning/emergency legal stages. Geometry overlap between an observation extent and a declared county is evidence of relationship only — not identity or authority equivalence.

The hard invariants governing this separation are enumerated in [`docs/domains/hazards/DROUGHT_ANTI_COLLAPSE.md`](../../../docs/domains/hazards/DROUGHT_ANTI_COLLAPSE.md).

---

## Meaning

`DroughtObservation` is a time-bounded physical drought observation or classification record. It represents what a monitoring program observed or classified, not what a legal or administrative authority declared.

A `DroughtObservation`:

- preserves the **source-native severity** exactly as emitted (D0–D4 or equivalent) without silent recoding;
- binds a **source descriptor reference** to the monitoring program that produced the classification;
- binds a **geometry reference** to the spatial extent of the classification;
- records **distinct time fields** for observed/valid time, retrieval time, and publication time;
- may record **supersession and correction links** without rewriting historical records;
- must **never carry a legal or administrative stage** (`legal_stage`, `declaration_stage`);
- must **never be derived from a DroughtDeclaration** (`declaration_derived` field is forbidden).

---

## Repo fit

| Responsibility | Path |
|---|---|
| This semantic contract | `contracts/domains/hazards/drought_observation.md` |
| Machine schema | `schemas/contracts/v1/domains/hazards/drought_observation.schema.json` |
| Declaration contract (counterpart) | `contracts/domains/hazards/drought_declaration.md` |
| Relationship contract | `schemas/contracts/v1/domains/hazards/drought_obs_decl_relationship.schema.json` |
| Fixtures | `fixtures/domains/hazards/drought_observation/` |
| Tests | `tests/schemas/test_drought_separation_contracts.py` |
| Anti-collapse documentation | `docs/domains/hazards/DROUGHT_ANTI_COLLAPSE.md` |
| Policy | `policy/domains/hazards/` |

---

## Required fields

| Field | Type | Notes |
|---|---|---|
| `object_type` | `"DroughtObservation"` | Const discriminator. Prevents substitution with DroughtDeclaration. |
| `schema_version` | `"v1"` | Schema version. |
| `observation_id` | `string` (`obs:…`) | Stable identifier for this observation record. |
| `profile_version` | `string` (semver) | Source descriptor profile version at capture time. |
| `source_ref` | `string` | Governed source descriptor reference. Required; must be bound. |
| `source_resolution_status` | `"bound"` \| `"unresolved"` | Must be `bound` before downstream use. |
| `observed_at` | `date-time` | Observed or valid time. Distinct from `retrieved_at` and `publication_time`. |
| `retrieved_at` | `date-time` | Ingestion/retrieval time. Distinct from `observed_at` and `publication_time`. |
| `geometry_ref` | `string` \| `null` | Governed geometry reference, or null if unresolved. |
| `geometry_resolution_status` | `"bound"` \| `"unresolved"` | `bound` requires non-null `geometry_ref`. |
| `classification_vocabulary` | enum | Source-native vocabulary (e.g. `usdm_d0_d4`). |
| `source_native_severity` | `"None"` \| `"D0"`–`"D4"` | Source-native code preserved exactly. Never mapped to legal stages. |
| `rights_status` | enum | Rights posture for this record. |
| `sensitivity` | enum | Sensitivity classification. |
| `release_posture` | enum | Release state. Does not grant publication authority. |

---

## Forbidden fields

These fields must never appear on a `DroughtObservation`. The schema enforces this with `not: {}`:

| Forbidden field | Reason |
|---|---|
| `legal_stage` | Observations must never carry a legal or administrative stage. |
| `declaration_derived` | Observations must never be derived from a declaration. |

Any undeclared field is also rejected (`additionalProperties: false`).

---

## Time semantics

A `DroughtObservation` preserves **four distinct time concepts**:

| Field | Meaning |
|---|---|
| `observed_at` | The time the physical phenomenon was observed or classified (valid time). |
| `observed_interval_end` | End of the observed interval; null for point-in-time observations. |
| `publication_time` | Time the source published or released the classification. |
| `retrieved_at` | Time this record was retrieved or ingested by KFM. |

These are **not interchangeable**. A later publication or retrieval time does not change the observed time. A newer observation does not rescind a legal declaration.

---

## Source and evidence binding

`source_ref` must reference a governed `SourceDescriptor` record. When `source_resolution_status` is `bound`, `source_ref` must be a non-null non-empty string.

Unbound source evidence must fail closed — `source_resolution_status: unresolved` signals that downstream use is not authorized.

---

## Geometry binding

`geometry_ref` references a governed geometry authority record. When `geometry_resolution_status` is `bound`, `geometry_ref` must be non-null.

Geometry overlap between an observation extent and a declared county area is **evidence of a relationship only** — it does not establish identity, authority transfer, or causal derivation between `DroughtObservation` and `DroughtDeclaration`.

---

## Severity vocabulary

`source_native_severity` preserves the source-native classification exactly as emitted:

- For USDM: `None`, `D0`, `D1`, `D2`, `D3`, `D4`.
- For other vocabularies: governed by the `classification_vocabulary` enum.

**Native classifications must never be silently recoded** into KFM domain truth, and must never be mapped to Kansas legal stages (watch/warning/emergency).

---

## Supersession and correction

- `superseded_by`: reference to the `observation_id` that supersedes this record (null = not superseded).
- `correction_of`: reference to the `observation_id` this record corrects.

A later declaration does not rewrite historical observation records.

---

## Rollback

Before merge: close the draft and abandon the scoped branch. After any separately authorized merge: use a focused reviewed revert of the contract/schema/fixture/validator packet; preserve historical source and correction identities.

<p align="right"><a href="#top">Back to top</a></p>
