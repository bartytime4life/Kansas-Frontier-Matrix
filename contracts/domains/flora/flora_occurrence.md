<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-flora-occurrence
title: Flora Occurrence Contract
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Occurrence steward · Contract steward · Source steward · Schema steward · Sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; occurrence; source-role-aware; sensitivity-aware; geoprivacy-aware; no-publication-authority
tags: [kfm, contracts, flora, flora-occurrence, occurrence, plant-occurrence, rare-plant, specimen, observation, evidence, source-role, geoprivacy, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./plant_taxon.md
  - ./flora_taxon_crosswalk.md
  - ./specimen_record.md
  - ./rare_plant_record.md
  - ./occurrence_public.md
  - ./occurrence_restricted.md
  - ./phenology_observation.md
  - ./vegetation_community.md
  - ./invasive_plant_record.md
  - ./range_polygon.md
  - ./habitat_association.md
  - ./botanical_survey.md
  - ./restoration_planting.md
  - ./redaction_receipt.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/flora_occurrence.schema.json
  - ../../../fixtures/domains/flora/flora_occurrence/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora occurrence semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "FloraOccurrence is an umbrella occurrence-class contract. Public-safe and restricted exact-geometry occurrence records remain separate object-family responsibilities."
  - "Rare-plant exact geometry, steward-controlled records, private-land joins, and culturally sensitive plant knowledge remain fail-closed unless evidence, policy, review, redaction, release, and rollback support all resolve."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Occurrence

> Semantic contract for `FloraOccurrence`: the Flora lane's umbrella occurrence-class object for plant presence claims, source-role posture, evidence closure, geoprivacy, sensitivity, public-safe derivatives, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: occurrence not publication authority" src="https://img.shields.io/badge/boundary-occurrence__not__publication__authority-critical">
</p>

`contracts/domains/flora/flora_occurrence.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Occurrence classes](#occurrence-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/flora_occurrence.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/flora_occurrence.schema.json`  
> **Truth posture:** the contract path is present, the paired schema path is present, and the Flora canonical path register identifies `FloraOccurrence` as an umbrella occurrence-class object. Field-level schema shape, fixtures, validators, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `FloraOccurrence` can support a plant presence claim only when evidence, source role, taxonomic support, spatial/temporal support, rights, sensitivity, review, and correction posture resolve. It does **not** publish exact rare-plant geometry, does **not** replace `RarePlantRecord`, `SpecimenRecord`, `PlantTaxon`, `BotanicalSurvey`, or `RedactionReceipt`, and does **not** approve public release by itself.

---

## Meaning

`FloraOccurrence` is the Flora lane's umbrella semantic object for a plant occurrence-class record: a bounded assertion that a plant taxon, plant group, or vegetation-relevant plant observation was present, reported, collected, surveyed, aggregated, modeled, or otherwise asserted at a place and time under a known source role.

It answers:

- What plant taxon or taxon candidate is involved?
- What source supplied the occurrence and under which source role?
- What evidence supports the observation or assertion?
- What spatial and temporal support applies, and at what precision?
- Is the record exact, restricted, generalized, aggregated, suppressed, or public-safe?
- Does the occurrence derive from a specimen, survey, community-science record, steward record, model, aggregate atlas, or administrative source?
- Which specialized Flora record owns the downstream claim, restriction, redaction, release, correction, or rollback path?

A `FloraOccurrence` is not necessarily public, exact, verified, vouchered, rare-plant-safe, or publishable. Those states must be proven through separate evidence, validation, policy, review, redaction, release, and rollback objects.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Occurrence meaning | `contracts/domains/flora/flora_occurrence.md` | Owned here as the umbrella occurrence contract |
| Machine schema shape | `schemas/contracts/v1/domains/flora/flora_occurrence.schema.json` | Linked only; currently scaffolded |
| Raw/normalized observation envelope | `contracts/domains/flora/domain_observation.md` | Upstream observation envelope; not replaced |
| Feature identity | `contracts/domains/flora/domain_feature_identity.md` | Deterministic identity companion |
| Taxon authority | `contracts/domains/flora/plant_taxon.md`, `flora_taxon_crosswalk.md` | Required for taxon support |
| Voucher support | `contracts/domains/flora/specimen_record.md` | Specimen-backed occurrence evidence |
| Rare/protected occurrence | `contracts/domains/flora/rare_plant_record.md` | Sensitive specialization |
| Public-safe occurrence | `contracts/domains/flora/occurrence_public.md` | Generalized / county / grid-binned derivative |
| Restricted occurrence | `contracts/domains/flora/occurrence_restricted.md` | Internal exact geometry; steward-only access |
| Survey context | `contracts/domains/flora/botanical_survey.md` | Method/effort/completeness context |
| Redaction proof | `contracts/domains/flora/redaction_receipt.md` | Required for transformed public outputs |
| Source registry | `data/registry/sources/flora/` | Source identity, role, rights, cadence, attribution |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Admission and release decisions |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/flora_occurrence.schema.json` |
| Schema title | `Flora Occurrence` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/flora_occurrence.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, policy tests, sensitivity checks, source registry links, release checks, public-safe derivatives, API payloads, and UI use. It does not claim current machine enforcement.

---

## Assertions

A reviewed `FloraOccurrence` should semantically assert:

1. **Occurrence identity** — a canonical identity or candidate identity for one occurrence-class record.
2. **Taxonomic subject** — a taxon, source taxon string, crosswalked taxon, or reviewed taxon candidate.
3. **Occurrence basis** — observed, specimen-backed, survey-derived, aggregate, modeled, administrative, candidate, or synthetic support.
4. **Source and role** — SourceDescriptor, source role, source record ID, rights posture, attribution, cadence, and source authority limits.
5. **Spatial support** — exact geometry, geometry reference, generalized geometry, administrative area, grid/cell, range polygon, uncertainty, and geoprivacy state.
6. **Temporal support** — observed time, event date, valid time, source time, retrieval time, release time, stale-state, and correction time where material.
7. **Evidence support** — EvidenceRef/EvidenceBundle links sufficient for cite-or-abstain behavior.
8. **Sensitivity posture** — rare-plant, steward-controlled, private-land, culturally sensitive, source-restricted, or public-safe classification.
9. **Specialization path** — whether the occurrence requires `RarePlantRecord`, `SpecimenRecord`, `OccurrenceRestricted`, `OccurrencePublic`, or another specialized contract.
10. **Governance state** — validation, policy, review, redaction, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating any occurrence row as verified presence | Evidence, source role, taxon, time, geometry, and review support must resolve. |
| Treating a public-safe derivative as canonical exact truth | Public derivatives are carriers; exact/internal support and source evidence remain separate. |
| Publishing exact rare-plant geometry | Rare/protected and steward-controlled records are deny-by-default without policy/review/redaction/release support. |
| Treating source taxon text as accepted taxonomy | Taxonomic authority belongs to `PlantTaxon` and `FloraTaxon Crosswalk`. |
| Treating a model or aggregate as observed fact | `modeled` and `aggregate` source roles remain visible and cannot be silently upgraded. |
| Treating non-detection as absence | Absence/non-detection requires survey method, effort, target scope, season, and limitations. |
| Treating `FloraOccurrence` as release approval | PolicyDecision, ReviewRecord, RedactionReceipt, ReleaseManifest, PromotionDecision, and rollback remain separate. |
| Direct public use of RAW/WORK/QUARANTINE occurrences | Public clients use governed interfaces and released/public-safe derivatives only. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical occurrence identity or candidate identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `occurrence_class` | `observed`, `specimen_backed`, `survey_derived`, `aggregate`, `modeled`, `administrative`, `candidate`, `synthetic`, `restricted`, or `public_derivative`. |
| `occurrence_basis` | Source-native or normalized basis of record. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and activation reference. |
| `source_role` | Canonical source role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |
| `source_record_ref` | Source-native occurrence/specimen/survey/event ID. |
| `domain_observation_ref` | Upstream observation-envelope reference, when applicable. |
| `feature_identity_ref` | Domain feature identity reference, when resolved. |
| `taxon_ref` | Link to `PlantTaxon` or reviewed taxon candidate. |
| `taxon_string_original` | Original source taxon text retained for audit and correction. |
| `specimen_record_ref` | Voucher/specimen support, when applicable. |
| `botanical_survey_ref` | Survey effort/method context, when applicable. |
| `rare_plant_record_ref` | Rare/protected specialization, when applicable. |
| `geometry_ref` | Geometry or geometry-bearing source reference; may be restricted. |
| `public_geometry_ref` | Public-safe geometry derivative, when released. |
| `geometry_precision` | Precision, uncertainty, scale, or support class. |
| `geoprivacy_state` | `exact`, `restricted`, `generalized`, `suppressed`, `steward_only`, `private`, `public_safe`, or `unknown`. |
| `location_uncertainty` | Numeric, categorical, or source-native uncertainty. |
| `observed_time` | Time the occurrence event occurred, when known. |
| `valid_time` | Time span the occurrence is intended to support. |
| `source_time` | Time asserted by the source. |
| `retrieval_time` | Time KFM retrieved the source material. |
| `release_time` | Time a released derivative became public, when applicable. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Rare-plant, steward, cultural, private-land, source-restricted, or public-safe posture. |
| `validation_report_ref` | Validation report for this occurrence or release candidate. |
| `policy_decision_ref` | Policy result when occurrence data affects exposure or release. |
| `review_record_ref` | Steward/source/sensitivity/release review record. |
| `redaction_receipt_ref` | Generalization, aggregation, suppression, or withholding receipt when public output is derived. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, supersession, withdrawal, stale-state, and rollback lineage. |
| `quality_flags` | Duplicate, stale, taxon-conflict, geometry-conflict, temporal-conflict, source-role-conflict, rights-unknown, sensitivity-unknown, or incomplete-evidence flags. |

---

## Occurrence classes

| Class | Meaning | Public posture |
|---|---|---|
| `observed` | Source asserts a direct observation event. | Public only after evidence, rights, sensitivity, review, and release gates. |
| `specimen_backed` | Occurrence is supported by a voucher or herbarium specimen. | Public-safe derivative may be allowed; exact geometry still needs sensitivity review. |
| `survey_derived` | Occurrence was produced from a botanical survey. | Requires method/effort context and review. |
| `aggregate` | County/grid/atlas/portal rollup or summary. | Public only at aggregate support scale with caveats. |
| `modeled` | Model-inferred distribution or likelihood. | Must remain model-labeled; not observed fact. |
| `administrative` | Program, list, site, project, or management record. | Supports administrative context, not occurrence truth by itself. |
| `candidate` | Unreviewed import, watcher, community-science, or unresolved row. | No public path until reviewed. |
| `synthetic` | Generated/reconstructed/interpolated occurrence-like statement. | Requires reality-boundary disclosure; never observed fact. |
| `restricted` | Internal exact or sensitive occurrence. | Steward-only; not a source for `data/published/`. |
| `public_derivative` | Redacted/generalized/suppressed/aggregated public occurrence. | Requires redaction receipt, release manifest, and rollback target. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | Contract posture |
|---|---|---|
| Herbarium specimen, field observation, steward-reviewed occurrence | `observed` | Can support occurrence meaning when evidence, taxonomy, time, geometry, and rights resolve. |
| Listed-plant status, regulatory survey requirement, permit condition | `regulatory` | Supports legal/status context; not occurrence proof by itself. |
| Species distribution model, habitat suitability model, interpolation | `modeled` | Requires model identity, uncertainty, and review; not observed fact. |
| Atlas grid, county rollup, portal summary, public-safe density surface | `aggregate` | Supports aggregate claims only at stated support scale. |
| Project registry, management area list, survey schedule, administrative site table | `administrative` | Supports administrative context, not presence truth by itself. |
| Watcher/import result, unresolved community-science submission, unreviewed row | `candidate` | Hold in WORK/QUARANTINE until reviewed; public edge forbidden. |
| AI-generated, reconstructed, interpolated, or synthetic scenario occurrence | `synthetic` | Requires reality-boundary disclosure; never observed fact by itself. |

Source role is set at admission or normalization and should not be silently upgraded by promotion. Promotion can approve a derivative release, not rewrite the source's authority.

---

## Sensitivity and release

Flora occurrences are high-risk when they reveal exact rare-plant locations, steward-controlled records, private-land context, culturally sensitive plant knowledge, source-restricted material, or precise habitat associations.

Rules:

- Exact rare-plant and sensitive occurrence geometry is deny-by-default for public release.
- Public derivatives must prove redaction, generalization, aggregation, suppression, or withholding with a `RedactionReceipt` or equivalent release proof.
- Public outputs must retain source-role, uncertainty, scale, time, and caveat visibility.
- `candidate`, `synthetic`, sensitivity-unknown, rights-unknown, and evidence-incomplete occurrences must not enter public outputs.
- Community-science observations require source-rights and geoprivacy checks before reuse.
- Steward-only and private-land notes must stay outside public payloads unless a release decision explicitly approves a transformed public representation.
- AI and search surfaces must abstain or deny when evidence, policy, source role, or sensitivity cannot be resolved.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source occurrence exports, specimen records, survey-derived records, community-science rows, stewardship tables, and model outputs remain source-bound. |
| WORK / QUARANTINE | Occurrences are normalized, deduplicated, taxon-crosswalked, source-role checked, rights checked, sensitivity reviewed, and linked to evidence. Unresolved or risky material remains quarantined. |
| PROCESSED | Reviewed occurrences receive deterministic identity, evidence links, source-role posture, temporal support, geometry/sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Occurrence-derived claims may be cataloged or projected only with evidence, source role, time, policy, scale, and caveats preserved. |
| PUBLISHED | Only public-safe derivatives appear in public API/UI/map layers, and only after review, policy, release manifest, redaction proof where needed, and rollback target exist. |
| CORRECTION | Taxon correction, geometry correction, duplicate merge/split, source withdrawal, rights change, stale-state update, sensitivity update, or evidence correction requires correction and rollback consideration. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/flora_occurrence.schema.json` beyond the scaffold fields.
- [ ] Add valid fixtures for non-sensitive observed occurrence, specimen-backed occurrence, survey-derived occurrence, aggregate public-safe occurrence, modeled occurrence, restricted exact occurrence, and public derivative occurrence.
- [ ] Add invalid fixtures for unresolved evidence, missing source role, rare-plant exact public geometry, rights-unknown public release, synthetic-as-observed mislabeling, missing taxon support, missing redaction receipt, and missing rollback target.
- [ ] Add validator checks for deterministic identity, source role, evidence closure, temporal support, taxon crosswalk, geometry validity, geoprivacy state, sensitivity class, redaction receipt linkage, release linkage, and correction lineage.
- [ ] Add policy tests for DENY / ABSTAIN / ERROR outcomes.
- [ ] Add no-network fixtures so CI can validate the contract without live source access.
- [ ] Add non-regression tests for stale-state handling, source withdrawal, correction, and rollback paths.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, policy allows, review passes, release exists | `ANSWER` / public-safe payload allowed |
| Evidence missing, temporal support insufficient, source role ambiguous | `ABSTAIN` |
| Sensitive location exposure, direct RAW/WORK/QUARANTINE access, rights denial | `DENY` |
| Schema/validator/runtime failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Flora canonical path register | Confirms `FloraOccurrence` is the umbrella occurrence-class record and distinguishes public-safe and restricted occurrence records. |
| Flora object-family register | Confirms `FloraOccurrence` is one of the expected Flora object families and that field-level shape is not covered by the register. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM sensitivity posture | Confirms sensitive ecological location details require fail-closed, review, redaction/generalization, or denial before public exposure. |

---

## Rollback

A released occurrence derivative must have a rollback path before public exposure.

Rollback triggers include:

- taxon misidentification;
- duplicate occurrence merge or split;
- geometry correction or geoprivacy failure;
- source withdrawal or changed source terms;
- rare-plant sensitivity update;
- steward review reversal;
- stale source version or stale taxonomy;
- mistaken source-role upgrade;
- invalid redaction/generalization receipt;
- public layer contains restricted exact geometry;
- release manifest or catalog integrity failure.

Rollback artifacts should include affected occurrence IDs, release IDs, layer IDs, evidence refs, policy decisions, redaction receipts, correction notice, rollback card, and replacement/suppression plan.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Should `FloraOccurrence` become an abstract base contract for `occurrence_public.md` and `occurrence_restricted.md`? | PROPOSED / NEEDS VERIFICATION | Confirm with Flora steward, contract steward, and schema steward before schema expansion. |
| Which occurrence classes become required enum values? | NEEDS VERIFICATION | Resolve in schema PR with fixtures. |
| Which geometry precision classes are allowed for public Flora layers? | NEEDS VERIFICATION | Resolve with `policy/sensitivity/flora/` and redaction fixtures. |
| How should community-science source geoprivacy flags map into KFM sensitivity states? | NEEDS VERIFICATION | Source registry + policy tests. |
| When does aggregate occurrence support become a `RangePolygon` rather than a `FloraOccurrence`? | NEEDS VERIFICATION | Contract crosswalk + layer manifest review. |
| Should non-detection records be represented here or under `BotanicalSurvey` only? | NEEDS VERIFICATION | Decide with survey steward and validation steward. |

---

## Related contracts

- `domain_observation.md` — upstream observation-envelope record.
- `domain_feature_identity.md` — deterministic Flora feature identity and cross-source identity posture.
- `plant_taxon.md` and `flora_taxon_crosswalk.md` — taxonomic meaning and crosswalk authority.
- `specimen_record.md` — voucher/specimen-backed occurrence support.
- `rare_plant_record.md` — rare/protected plant occurrence specialization.
- `occurrence_public.md` — public-safe occurrence derivative.
- `occurrence_restricted.md` — internal exact-geometry occurrence.
- `botanical_survey.md` — survey effort, method, and completeness context.
- `phenology_observation.md` — phenological event specialization.
- `vegetation_community.md` — community/polygon classification specialization.
- `redaction_receipt.md` — public-safe transformation proof.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any release candidate uses this contract.
- [ ] Add policy tests for exact rare-plant and source-restricted geometry.
- [ ] Confirm API/UI payload use goes through governed interfaces only.
- [ ] Confirm `occurrence_public.md` and `occurrence_restricted.md` remain separate authority surfaces and do not duplicate this contract.
- [ ] Record any contract/schema/path conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
