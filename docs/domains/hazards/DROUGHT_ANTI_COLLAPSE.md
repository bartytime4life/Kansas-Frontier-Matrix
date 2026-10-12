# DROUGHT_ANTI_COLLAPSE — Hazards Domain

> Anti-collapse rule: DroughtObservation and DroughtDeclaration are separate, non-substitutable object families. USDM D0–D4 physical classifications must never be treated as a legal-stage derivation rule.

**Document path:** `docs/domains/hazards/DROUGHT_ANTI_COLLAPSE.md`  
**Status:** draft / PROPOSED  
**Issue:** #1943 planning and implementation record — no connector activation, stage assertion, policy, release, deployment, or publication.

---

## Quick jumps

[Purpose](#purpose) · [Current evidence](#current-evidence) · [Object families](#object-families) · [Hard invariants](#hard-invariants) · [Anti-collapse rule](#anti-collapse-rule) · [Validator outcomes](#validator-outcomes) · [Crosswalk candidates](#crosswalk-candidates) · [Rollback](#rollback)

---

## Purpose

This document names the anti-collapse rule and rollback posture for the drought observation and legal declaration object families in the KFM Hazards domain.

The drought anti-collapse rule exists because:

1. **Two different authorities** describe related but non-identical state:
   - **USDM** (National Drought Mitigation Center / USDA / NOAA) publishes weekly D0–D4 physical drought classifications based on expert synthesis of meteorological, hydrological, and soil-moisture observations.
   - **Kansas Water Office (KWO)** issues legal drought declarations (watch/warning/emergency) based on state law and its own assessment, which may use USDM and additional information.

2. **USDM geometry is not a derivation rule** for Kansas legal stages. The KWO proclamation of April 30, 2026 placed all 105 counties under watch, warning, or emergency status. That legal stage is a separate authority determination — not a mechanical mapping from D0–D4 polygon coverage.

3. **Collapsing the two** — treating physical severity as legal stage, or overwriting historical observations with later declarations — violates source-role integrity, creates false authority, and may cause harm if stale or misattributed state is presented as current official status.

---

## Current evidence

| Source | What it describes | What it does not describe |
|---|---|---|
| [Drought.gov / USDM Kansas](https://www.drought.gov/states/kansas) | Current USDM D0–D4 physical classifications for Kansas. Notes states may use additional information for declarations and actions. | Kansas legal watch/warning/emergency stages. |
| [Kansas Water Office — April 30, 2026 Proclamation](https://www.kwo.ks.gov/Home/Components/News/News/68/75) | Proclamation placing all 105 counties in watch, warning, or emergency status; effective until rescinded or revised. | USDM physical classification or physical drought severity. |

These sources describe related but non-identical state. They are preserved in separate `DroughtObservation` and `DroughtDeclaration` records, not merged.

---

## Object families

### DroughtObservation

A `DroughtObservation` is a time-bounded physical drought observation or classification.

**Preserves independently:**

| Concept | Field |
|---|---|
| Stable observation identity | `observation_id`, `profile_version` |
| Source descriptor / evidence reference | `source_ref`, `source_resolution_status` |
| Observed or valid time | `observed_at`, `observed_interval_end` |
| Retrieval time | `retrieved_at` |
| Publication time | `publication_time` |
| Geometry identity and version | `geometry_ref`, `geometry_resolution_status`, `geometry_version` |
| Classification vocabulary | `classification_vocabulary` |
| Source-native severity | `source_native_severity` |
| Method / product identity | `method_ref` |
| Correction and supersession links | `correction_of`, `superseded_by` |
| Rights, sensitivity, release posture | `rights_status`, `sensitivity`, `release_posture` |

**Forbidden on DroughtObservation:**

- `legal_stage` — observations must never carry a legal or administrative stage.
- `declaration_derived` — observations must never be derived from declarations.

**Schema:** `schemas/contracts/v1/domains/hazards/drought_observation.schema.json`

---

### DroughtDeclaration

A `DroughtDeclaration` is a legal or administrative drought declaration or proclamation event.

**Preserves independently:**

| Concept | Field |
|---|---|
| Declaration / proclamation identity | `declaration_id` |
| Issuing authority | `issuing_authority` |
| Legal instrument reference | `legal_instrument_ref`, `legal_instrument_resolution_status` |
| Legal effective time | `effective_at` |
| Rescission / revision time | `rescinded_at` |
| Retrieval time | `retrieved_at` |
| County or governed-area membership | `county_scope` |
| Declaration-stage vocabulary | `declaration_stage_vocabulary`, `declaration_stage` |
| Predecessor / successor and correction lineage | `predecessor_ref`, `successor_ref`, `correction_of` |
| Source descriptor / evidence reference | `source_ref`, `source_resolution_status` |
| Review and release posture | `review_state`, `release_posture` |

**Forbidden on DroughtDeclaration:**

- `usdm_derived` — stage must never be derived from USDM D0–D4 polygon categories.
- `observation_stage` — declarations must never carry a physical observation severity.

**Schema:** `schemas/contracts/v1/domains/hazards/drought_declaration.schema.json`

---

## Hard invariants

These invariants are enforced by schemas, fixtures, and validators. None may be relaxed without a separately reviewed change.

| # | Invariant |
|---|---|
| 1 | No direct or implicit mapping from D0–D4 polygons to Kansas watch/warning/emergency status. |
| 2 | Observation time, publication time, legal effective time, retrieval time, and supersession time remain distinct typed fields. |
| 3 | A newer physical observation does not rescind a legal declaration. |
| 4 | A later declaration does not rewrite historical observations. |
| 5 | Missing or unresolved legal instrument evidence must abstain/hold (`declaration_stage: "unknown"`) rather than infer a stage. |
| 6 | Geometry overlap is evidence of relationship only — not identity or authority equivalence. |
| 7 | Synthetic fixtures only until source identity, rights, retrieval, and release gates are separately closed. |
| 8 | `DroughtObservation` and `DroughtDeclaration` schemas cannot be substituted for one another (`object_type` const discriminator enforced). |
| 9 | Silent supersession is forbidden — `successor_ref` must be set when a declaration is known to be superseded. |
| 10 | `additionalProperties: false` on both schemas — undeclared fields are rejected. |

---

## Anti-collapse rule

> **The anti-collapse rule:** Physical drought severity (D0–D4) and legal drought stage (watch/warning/emergency) are properties of separate object families with separate authorities, separate time semantics, and separate evidence requirements. Collapsing them — by mapping one to the other, treating one as a derivation of the other, or merging their records — is a schema violation and a governance failure.

### Consequences of collapse

- **False authority:** Presenting USDM classifications as Kansas legal status, or vice versa, misrepresents the source's role.
- **Stale state harm:** USDM releases weekly; KWO declarations are effective until rescinded. Collapse can present outdated physical observations as current legal status, or vice versa.
- **Unmaintainable lineage:** Merging records destroys correction, supersession, and rollback traceability.
- **Downstream risk:** Maps, APIs, and AI summaries that receive collapsed records may produce legally incorrect or life-safety-relevant errors.

### What the schemas enforce

| Schema rule | What it prevents |
|---|---|
| `object_type: const: "DroughtObservation"` | A declaration document cannot pass the observation schema. |
| `object_type: const: "DroughtDeclaration"` | An observation document cannot pass the declaration schema. |
| `legal_stage: not: {}` on observation | Observation cannot carry a legal stage. |
| `usdm_derived: not: {}` on declaration | Declaration cannot record a USDM-derived field. |
| `observation_stage: not: {}` on declaration | Declaration cannot carry physical severity. |
| `allOf` constraint on declaration | `declaration_stage` must be `"unknown"` when `legal_instrument_resolution_status` is `"unresolved"` or `"abstain"`. |
| `declaration_stage` enum excludes D0–D4 | Stage vocabulary cannot include USDM category codes. |

---

## Validator outcomes

The deterministic validator for this object family emits one of these outcomes per fixture:

| Outcome | Meaning |
|---|---|
| `PASS` | Document conforms to schema and all anti-collapse invariants. |
| `ABSTAIN` | Evidence is insufficient; stage or binding cannot be determined. No downstream use authorized. |
| `DENY` | Document violates an invariant. Not admissible. |
| `ERROR` | Unexpected failure during validation. Treated as deny. |

No `APPROVE`, `PUBLISH`, `ACTIVATE`, or `RELEASE` outcome is emitted. These validators do not grant publication or release authority.

---

## Crosswalk candidates

The following crosswalk entries are **candidates only** — they name the relationship between the two families without asserting derivation or authority equivalence.

| Observation family | Declaration family | Relationship kind | Derivation claimed |
|---|---|---|---|
| `DroughtObservation` (USDM weekly) | `DroughtDeclaration` (KWO 2026-04-30) | `temporal_overlap` | `false` |

**Geometry overlap and temporal proximity are evidence of a relationship only.** A crosswalk record of kind `temporal_overlap` or `geographic_overlap` does not assert that the observation caused, justified, or is equivalent to the declaration, or vice versa.

Use the `DroughtObsDeclarationRelationship` schema (`schemas/contracts/v1/domains/hazards/drought_obs_decl_relationship.schema.json`) to record crosswalk candidates. The `derivation_claimed` field must always be `false`.

---

## Rollback

This document and the implementation slice it describes may be rolled back by a focused reviewed revert of:

- `schemas/contracts/v1/domains/hazards/drought_observation.schema.json`
- `schemas/contracts/v1/domains/hazards/drought_declaration.schema.json`
- `schemas/contracts/v1/domains/hazards/drought_obs_decl_relationship.schema.json`
- `contracts/domains/hazards/drought_observation.md`
- `contracts/domains/hazards/drought_declaration.md`
- `docs/domains/hazards/DROUGHT_ANTI_COLLAPSE.md`
- `fixtures/domains/hazards/drought_observation/`
- `fixtures/domains/hazards/drought_declaration/`
- `fixtures/domains/hazards/drought_obs_decl_relationship/`
- `tests/schemas/test_drought_separation_contracts.py`
- `fixtures/generated_receipt/drought_anti_collapse_receipt.json`

Preserve historical source and correction identities. Do not rewrite observation or declaration history as part of rollback.

Before merge: close the draft and abandon the scoped branch. After any separately authorized merge: use a focused reviewed revert; no source activation, policy approval, promotion, release, deployment, or publication occurs as part of rollback.
