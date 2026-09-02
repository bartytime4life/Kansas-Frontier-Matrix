<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-botanical-survey
title: Botanical Survey Contract
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Survey steward · Contract steward · Source steward · Schema steward · Sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; botanical-survey; survey-effort; source-role-aware; sensitivity-aware; no-publication-authority
tags: [kfm, contracts, flora, botanical-survey, survey, effort, completeness, plant-occurrence, rare-plant, sensitivity, evidence, policy, release, correction, rollback]
related:
  - ./README.md
  - ./flora_occurrence.md
  - ./rare_plant_record.md
  - ./specimen_record.md
  - ./plant_taxon.md
  - ./phenology_observation.md
  - ./vegetation_community.md
  - ./redaction_receipt.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/botanical_survey.schema.json
  - ../../../data/registry/sources/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../fixtures/domains/flora/botanical_survey/
  - ../../../tests/domains/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a planned-path scaffold into a Flora botanical-survey semantic contract."
  - "The paired schema is a PROPOSED scaffold with empty properties and additionalProperties=true; field-level realization remains NEEDS VERIFICATION."
  - "The repository also contains contracts/domains/flora/BotanicalSurvey.md; that mixed-case path is treated as a compatibility/drift surface because the Flora register and schema point to botanical_survey.md."
  - "BotanicalSurvey is survey effort and completeness metadata; it is not occurrence proof, specimen proof, rare-plant release permission, vegetation-community classification, or public layer release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Botanical Survey

> Semantic contract for Flora survey events: what a botanical survey episode means, how it records effort and completeness, and which evidence, source-role, sensitivity, policy, release, correction, and rollback controls must remain visible before survey-derived claims are trusted or published.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: survey effort not occurrence proof" src="https://img.shields.io/badge/boundary-effort__not__proof-critical">
</p>

`contracts/domains/flora/botanical_survey.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/botanical_survey.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/botanical_survey.schema.json`  
> **Truth posture:** lowercase contract path, paired schema path, Flora lane pattern, object-family inventory, source-role enum, lifecycle posture, and rare-plant sensitivity posture are CONFIRMED from current repo evidence. Field-level schema shape, fixtures, validators, source registry records, policy runtime behavior, public-release workflow, API behavior, UI behavior, and test coverage remain NEEDS VERIFICATION.

> [!CAUTION]
> `BotanicalSurvey` records survey effort and completeness context. It does **not** prove a plant occurrence by itself, does not publish rare-plant exact geometry, and does not replace `FloraOccurrence`, `RarePlantRecord`, `SpecimenRecord`, `VegetationCommunity`, or release records.

---

## Meaning

`BotanicalSurvey` is a Flora semantic object for a **survey episode, survey visit, field inventory, transect, plot visit, quadrat sample, checklist effort, vegetation walkover, targeted rare-plant search, restoration monitoring pass, or other bounded botanical survey activity**.

It answers questions like:

- Who or what source performed the survey, and under what source role?
- What plant taxon, community, site, plot, transect, route, project area, or administrative area was surveyed?
- What method, effort, timing, season, search intensity, completeness, and limitations apply?
- Which downstream records may have been produced: FloraOccurrence, RarePlantRecord, SpecimenRecord, PhenologyObservation, VegetationCommunity, InvasivePlantRecord, or RestorationPlanting?
- Which EvidenceBundle, SourceDescriptor, ReviewRecord, PolicyDecision, RedactionReceipt, ReleaseManifest, CorrectionNotice, and rollback references must resolve before survey-derived claims are trusted?

A survey can support confidence about search effort and completeness, but it does not automatically prove presence, absence, abundance, trend, or public-safe release.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Survey meaning | `contracts/domains/flora/botanical_survey.md` | Owned here |
| Compatibility/drift alias | `contracts/domains/flora/BotanicalSurvey.md` | Should not become parallel authority |
| Machine schema shape | `schemas/contracts/v1/domains/flora/botanical_survey.schema.json` | Linked only |
| Occurrence result | `contracts/domains/flora/flora_occurrence.md` | Downstream result; not replaced |
| Rare-plant record | `contracts/domains/flora/rare_plant_record.md` | Sensitive result; not replaced |
| Specimen record | `contracts/domains/flora/specimen_record.md` | Voucher/collection result; not replaced |
| Source registry | `data/registry/sources/flora/` | Source identity, rights, cadence, role |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Admission/release decisions |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current evidence |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/botanical_survey.schema.json` |
| Schema title | `Botanical Survey` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/botanical_survey.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema, fixtures, validators, policy tests, sensitivity checks, source registry links, release checks, and API/UI use. It does not claim current machine enforcement.

---

## Assertions

A reviewed `BotanicalSurvey` should semantically assert:

1. **Survey identity** — a bounded survey episode, visit, plot, transect, route, checklist, project-area survey, or restoration-monitoring pass.
2. **Survey purpose** — inventory, targeted rare-plant search, vegetation classification support, specimen collection support, phenology monitoring, invasive-plant survey, restoration monitoring, or other reviewed purpose.
3. **Source and role** — SourceDescriptor, collector/observer/team/source system, source role, rights, cadence, and attribution posture.
4. **Effort and method** — method, protocol, duration, search area, completeness, limitations, detection confidence, and uncertainty.
5. **Spatial/temporal support** — plot/transect/route/area reference, observed/valid/source/retrieval/release time, season, and correction time posture.
6. **Derived-object posture** — links to occurrence, rare-plant, specimen, phenology, community, invasive, restoration, or validation records produced from the survey.
7. **Sensitivity posture** — whether exact survey location, rare-plant target, steward-controlled site, culturally sensitive plant knowledge, or private-land join requires restriction or redaction.

---

## Exclusions

| Misuse | Why it is denied |
|---|---|
| Occurrence proof by itself | Occurrence claims require occurrence/specimen/rare-plant evidence objects. |
| Absence proof by default | Non-detection requires explicit method, effort, target scope, season, and limitations. |
| Rare-plant public release | Rare-plant exact geometry remains deny-by-default unless policy/review/redaction/release support exists. |
| Vegetation-community classification | Community polygons/classes require `VegetationCommunity` or related classification evidence. |
| Specimen/voucher proof | Vouchered specimen meaning belongs to `SpecimenRecord`. |
| Restoration success proof | Restoration outcomes require restoration and monitoring evidence, not survey effort alone. |
| Source descriptor | Rights, cadence, source role, and activation state belong in source registry records. |
| Release approval | PolicyDecision, ReviewRecord, ReleaseManifest, and rollback remain separate object families. |

---

## Recommended semantics

| Field | Meaning |
|---|---|
| `id` | Canonical botanical survey identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `survey_type` | Inventory, transect, plot, checklist, rare-plant search, vegetation survey, restoration monitoring, etc. |
| `survey_purpose` | Intended claim support or monitoring purpose. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and source role. |
| `source_role` | Canonical source role for the survey assertion. |
| `survey_method` | Protocol/method reference or source-native method label. |
| `effort` | Duration, distance, area, observer count, plot/quadrat count, search intensity, or completeness indicator. |
| `target_taxon_refs` | Plant taxa or groups targeted, if any. |
| `site_or_area_ref` | Plot, transect, route, project area, administrative unit, or restricted geometry reference. |
| `observed_time` | When the survey occurred. |
| `temporal_scope` | Observed, valid, source, retrieval, release, and correction time posture. |
| `derived_record_refs` | Occurrence, rare-plant, specimen, phenology, vegetation, invasive, or restoration records derived from the survey. |
| `sensitivity_state` | Rare-plant/steward/private-land/cultural sensitivity posture. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `policy_decision_ref` | Policy result when survey data affects release. |
| `review_record_ref` | Steward/source/sensitivity/release review record. |
| `redaction_receipt_ref` | Generalization, aggregation, suppression, or withholding receipt if public output is derived. |
| `release_ref` | Release or candidate release linkage. |
| `correction_refs` | Correction/supersession/rollback lineage. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | Contract posture |
|---|---|---|
| Field survey, plot visit, transect, quadrat, collector checklist | `observed` | Supports survey effort and derived records, not occurrence truth by itself. |
| Agency/steward survey roster or program table | `administrative` | Supports survey context, schedule, or program history; not direct plant observation by itself. |
| Published survey summary or atlas rollup | `aggregate` | Supports summarized effort/completeness only at aggregate support. |
| Regulatory survey requirement or official monitoring protocol | `regulatory` | Supports requirement/protocol context; not observed results. |
| Unreviewed watcher/import/survey candidate | `candidate` | Hold until reviewed; public edge forbidden. |
| Modeled or inferred survey completeness | `modeled` | Requires model identity, uncertainty, and review; not observed effort. |
| Generated/reconstructed historical survey statement | `synthetic` | Requires reality-boundary disclosure; never observed survey fact by itself. |

---

## Sensitivity and release

Flora doctrine identifies rare plants, exact sensitive occurrence geometry, steward-controlled records, and culturally sensitive plant knowledge as fail-closed or redaction/generalization candidates before public release.

Rules:

- Exact survey geometry can be sensitive when it reveals rare plants, steward-controlled sites, private-land details, or culturally sensitive plant knowledge.
- Targeted rare-plant survey metadata may itself reveal sensitive locations even without occurrence results.
- Public survey summaries must use public-safe geometry, time, taxon labels, and caveats.
- Non-detection or completeness claims require explicit method and effort support.
- Public clients receive only released, policy-safe representations through governed interfaces.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Field notes, survey forms, source exports, GPS tracks, plot sheets, and photos remain source-bound. |
| WORK / QUARANTINE | Survey records are normalized, source-role checked, rights checked, sensitivity reviewed, and linked to evidence. |
| PROCESSED | Reviewed surveys receive deterministic identity, method/effort fields, evidence links, sensitivity posture, and correction posture. |
| CATALOG / TRIPLET | Survey events can support inspectable effort/completeness claims only with method, source, time, evidence, and caveats preserved. |
| PUBLISHED | Only public-safe summaries or derived released records appear in public surfaces. |
| CORRECTION | Method correction, geometry correction, taxon correction, duplicate survey, source withdrawal, or sensitivity update requires correction and rollback consideration. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Define and review the paired schema fields in `schemas/contracts/v1/domains/flora/botanical_survey.schema.json`.
- [ ] Resolve or remove the mixed-case compatibility path `contracts/domains/flora/BotanicalSurvey.md`.
- [ ] Add fixtures for plot survey, transect survey, checklist survey, targeted rare-plant survey, restoration-monitoring survey, aggregate summary, administrative roster, candidate import, and modeled completeness case.
- [ ] Add negative tests proving survey effort cannot be used as occurrence proof, absence proof, rare-plant release permission, community classification, or restoration success proof by itself.
- [ ] Add sensitivity tests proving targeted rare-plant survey geometry and private/steward/cultural joins are withheld or generalized before public output.
- [ ] Confirm source descriptors, rights, cadence, attribution, and source role for admitted Flora survey sources.
- [ ] Confirm correction and rollback behavior for method, geometry, taxon, source, duplicate, sensitivity, and release changes.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/flora/botanical_survey.md` prior version | CONFIRMED repo evidence | Lowercase canonical target existed as a planned-path scaffold. | Did not define authoritative semantics. |
| `contracts/domains/flora/BotanicalSurvey.md` prior version | CONFIRMED repo evidence | Mixed-case requested path exists as a separate scaffold. | Conflicts with lowercase register/schema path and should not become parallel authority. |
| `schemas/contracts/v1/domains/flora/botanical_survey.schema.json` | CONFIRMED repo evidence | Paired schema exists, points to lowercase contract path, and is PROPOSED. | Schema has empty properties and does not validate field-level semantics yet. |
| `docs/domains/flora/CANONICAL_PATHS.md` | CONFIRMED repo evidence | Confirms Flora lane pattern, object families, lifecycle invariant, source-role enum, and lowercase botanical-survey contract/schema path. | Many concrete paths are still labeled PROPOSED until repo verification. |
| `contracts/domains/flora/README.md` | CONFIRMED repo evidence | Confirms this root is the Flora contracts home and should not duplicate generic/cross-domain materials. | README is itself a greenfield scaffold. |
| User-provided Markdown Authoring Agent v2 prompt | CONFIRMED user-provided guidance | Authoring guidance for grounded, repo-aware Markdown. | It is not repository implementation evidence and was not pasted into this contract. |

---

## Rollback

Rollback if this file is used to claim implemented schema validation, treat survey effort as occurrence proof, publish rare-plant or sensitive survey geometry, hide the mixed-case path conflict, or publish survey-derived claims without evidence, method, source-role, rights, sensitivity, policy, review, release, correction, and rollback support.

Rollback target: prior scaffold blob SHA `eeecf58a515b50caff20382fee8299795a1b5ded`.

<p align="right"><a href="#top">Back to top</a></p>
