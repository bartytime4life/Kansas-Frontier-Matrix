<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-domain-observation
title: Domain Observation Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Contract steward · Source steward · Schema steward · Sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; domain-observation; source-role-aware; sensitivity-aware; evidence-bound; no-publication-authority
tags: [kfm, contracts, domains, flora, domain-observation, observation-envelope, evidence, source-role, geoprivacy, rare-plant, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./domain_feature_identity.md
  - ./plant_taxon.md
  - ./flora_taxon_crosswalk.md
  - ./specimen_record.md
  - ./flora_occurrence.md
  - ./rare_plant_record.md
  - ./vegetation_community.md
  - ./invasive_plant_record.md
  - ./phenology_observation.md
  - ./range_polygon.md
  - ./habitat_association.md
  - ./botanical_survey.md
  - ./restoration_planting.md
  - ./redaction_receipt.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/domain_observation.schema.json
  - ../../../data/registry/sources/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../fixtures/domains/flora/domain_observation/
  - ../../../tests/domains/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a greenfield scaffold into a Flora semantic contract."
  - "The paired schema is a PROPOSED scaffold with id/version/spec_hash only and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "DomainObservation is an observation envelope and normalization contract. It is not occurrence proof, taxonomic authority, rare-plant publication permission, source registry authority, or release approval."
  - "Exact rare-plant, steward-controlled, private-land, and culturally sensitive plant-location exposure remains deny-by-default until policy, review, redaction, release, and rollback support are proven."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Observation — Flora

> Semantic contract for a Flora `DomainObservation`: a source-role-aware, evidence-bound observation envelope used to normalize plant-related observations before they become specific Flora records, public-safe map features, catalog records, claims, or release artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: observation envelope not release authority" src="https://img.shields.io/badge/boundary-observation__not__release__authority-critical">
</p>

`contracts/domains/flora/domain_observation.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/domain_observation.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/domain_observation.schema.json`  
> **Truth posture:** the path, paired schema pointer, and current scaffold state are confirmed from current repo evidence. The complete field model, validators, fixtures, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `DomainObservation` is an observation envelope. It does **not** prove a public plant occurrence by itself, does **not** publish rare-plant exact geometry, does **not** replace specialized Flora contracts, and does **not** bypass EvidenceBundle, policy, review, release, correction, or rollback controls.

---

## Meaning

`DomainObservation` is the Flora lane's generic semantic envelope for a bounded plant-related observation candidate, observation record, or normalized observation unit before that unit is specialized into one or more domain objects.

It can carry source-provided or normalized observation context for:

- a plant taxon sighting, specimen-backed record, survey finding, phenology event, invasive-plant report, vegetation-community observation, restoration monitoring observation, or range/distribution support;
- a field-survey, herbarium, agency, community-science, steward, aggregate, modeled, or synthetic observation carrier;
- a restricted internal observation that may later yield a public-safe derivative;
- a public-safe observation derivative that has already passed redaction, policy, review, and release gates.

A `DomainObservation` answers:

- What was observed, reported, modeled, aggregated, administered, or proposed?
- Which source supplied it, under which source role, rights posture, cadence, and attribution rules?
- What spatial, temporal, taxonomic, evidentiary, uncertainty, and sensitivity support does it carry?
- Which more specific Flora object family should own downstream meaning?
- Which EvidenceBundle, PolicyDecision, ReviewRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, and rollback references must resolve before the observation contributes to public claims?

It is a normalization and routing contract, not a sovereign truth object.

---

## Repo fit

The Flora lane follows the KFM responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Observation envelope meaning | `contracts/domains/flora/domain_observation.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/domain_observation.schema.json` | Linked only; currently scaffolded |
| Feature identity | `contracts/domains/flora/domain_feature_identity.md` | Identity companion; not replaced |
| Taxon authority | `contracts/domains/flora/plant_taxon.md`, `flora_taxon_crosswalk.md` | Referenced; not replaced |
| Occurrence result | `contracts/domains/flora/flora_occurrence.md` | Downstream specialization |
| Rare-plant record | `contracts/domains/flora/rare_plant_record.md` | Sensitive specialization |
| Specimen record | `contracts/domains/flora/specimen_record.md` | Voucher specialization |
| Survey effort | `contracts/domains/flora/botanical_survey.md` | Survey context; not replaced |
| Redaction proof | `contracts/domains/flora/redaction_receipt.md` | Required for public-safe derivatives when location/sensitivity is transformed |
| Source registry | `data/registry/sources/flora/` | Source identity, rights, role, cadence, activation |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Admission/release decisions |
| Fixtures/tests | `fixtures/domains/flora/domain_observation/`, `tests/domains/flora/` | Validation and non-regression proof |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/domain_observation.schema.json` |
| Schema title | `domain_observation` |
| Declared properties | `spec_hash`, `id`, `version` |
| Required fields | `id` |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Contract document | `contracts/domains/flora/domain_observation.md` |
| Fixtures root | `fixtures/domains/flora/domain_observation/` |
| Validator | `tools/validators/domains/flora/validate_domain_observation.py` |
| Policy root | `policy/domains/flora/` |

Because the schema is permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, policy tests, sensitivity checks, source registry links, release checks, API payloads, and UI use. It does not claim current machine enforcement.

---

## Assertions

A reviewed `DomainObservation` should semantically assert:

1. **Observation identity** — a deterministic identity or source-bound candidate identity for one bounded observation unit.
2. **Observation class** — whether the observation is taxonomic, occurrence-like, specimen-derived, survey-derived, phenological, invasive, vegetation-community, restoration, distribution/range, or another reviewed Flora type.
3. **Source and role** — the SourceDescriptor, source role, rights posture, retrieval/cadence information, and attribution basis.
4. **Subject support** — observed or reported taxon, community, site, project area, survey event, specimen, habitat relation, or restoration context.
5. **Spatial support** — geometry, geometry reference, uncertainty, geoprivacy state, generalization state, restricted/public split, and scale limits.
6. **Temporal support** — observed, valid, source, retrieval, release, correction, and stale-state times where material.
7. **Evidence support** — EvidenceRef/EvidenceBundle linkage sufficient for cite-or-abstain behavior.
8. **Sensitivity posture** — rare-plant, steward-controlled, private-land, culturally sensitive, source-restricted, or public-safe classification.
9. **Downstream ownership** — the specialized Flora object family that must own claim meaning before release or public interpretation.
10. **Governance state** — review, policy, redaction, release, correction, rollback, and supersession references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating observation as public occurrence proof | Public occurrence claims require resolved evidence, source role, policy, review, and an appropriate specialized object such as `FloraOccurrence`, `SpecimenRecord`, or `RarePlantRecord`. |
| Treating source taxon text as accepted taxonomy | Taxonomic authority belongs to `PlantTaxon` and `FloraTaxon Crosswalk`. |
| Publishing exact rare-plant geometry | Exact sensitive flora locations are deny-by-default without steward review, redaction/generalization, release, and rollback support. |
| Treating aggregate/model output as observed fact | `aggregate`, `modeled`, and `synthetic` source roles must remain visible and cannot be upgraded by downstream promotion. |
| Treating survey effort as occurrence truth | Survey meaning belongs to `BotanicalSurvey`; non-detection and completeness require method/effort support. |
| Treating the envelope as release approval | Release authority belongs to PolicyDecision, ReviewRecord, ReleaseManifest, PromotionDecision, and rollback artifacts. |
| Direct public use of RAW/WORK/QUARANTINE observations | Public clients must use governed interfaces and released/public-safe derivatives only. |
| AI-generated observation creation | AI may interpret and route evidence-bound observations; it must not create root truth or publish unsupported claims. |

---

## Recommended semantics

The following field semantics are **PROPOSED** targets for future schema work. They are not fully enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical observation identity or candidate identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `observation_type` | Controlled value such as `occurrence`, `specimen`, `survey_result`, `phenology`, `invasive`, `vegetation_community`, `range_support`, `restoration_monitoring`, `candidate`, or `public_derivative`. |
| `observation_basis` | Whether the record is source-observed, source-reported, voucher-backed, aggregated, modeled, administrative, candidate, or synthetic. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and activation reference. |
| `source_role` | Canonical source role. Recommended enum: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, `synthetic`. |
| `source_record_ref` | Stable source-native identifier, row identifier, occurrence ID, specimen ID, survey ID, event ID, or run record reference. |
| `taxon_ref` | Link to `PlantTaxon` or source-native taxon candidate. |
| `taxon_string_original` | Original source taxon text when retained for audit/correction. |
| `feature_identity_ref` | Link to `DomainFeatureIdentity` when feature identity has been resolved. |
| `related_record_refs` | Links to specimen, occurrence, survey, rare-plant, phenology, vegetation, invasive, range, restoration, or habitat-association records. |
| `geometry_ref` | Reference to geometry or geometry-bearing source material; may be restricted. |
| `geometry_precision` | Precision/uncertainty/scale class. |
| `geoprivacy_state` | Exact, generalized, suppressed, steward-only, private, public-safe, or unknown state. |
| `location_uncertainty` | Numeric, categorical, or source-native uncertainty. |
| `observed_time` | Time the observation event occurred, when known. |
| `valid_time` | Time period the observation is intended to support. |
| `source_time` | Time asserted by the source. |
| `retrieval_time` | Time KFM retrieved the source material. |
| `release_time` | Time a released derivative became public, when applicable. |
| `correction_time` | Time a correction or supersession applies, when applicable. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, terms, redistribution, attribution, and access posture summary. |
| `sensitivity_state` | Rare plant, steward, cultural, private-land, source-restricted, or public-safe posture. |
| `policy_decision_ref` | Policy result when observation data affects exposure or release. |
| `review_record_ref` | Steward/source/sensitivity/release review record. |
| `redaction_receipt_ref` | Generalization, aggregation, suppression, or withholding receipt when public output is derived. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, supersession, withdrawal, and rollback lineage. |
| `quality_flags` | Duplicate, stale, taxon-conflict, geometry-conflict, temporal-conflict, source-role-conflict, rights-unknown, sensitivity-unknown, or incomplete-evidence flags. |
| `notes_public` | Public-safe caveat text only. |
| `notes_internal` | Restricted steward notes; never exposed through public payloads without policy review. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | Contract posture |
|---|---|---|
| Herbarium specimen, field survey observation, steward-reviewed source observation | `observed` | May support observation meaning when evidence, taxonomy, time, geometry, and rights resolve. |
| Federal/state listed-plant status, regulatory review, legal designation, permit condition | `regulatory` | Supports status or requirement context; does not prove occurrence by itself. |
| Species distribution model, habitat suitability model, vegetation index inference | `modeled` | Requires model identity, input evidence, uncertainty, and review; not observed fact. |
| Atlas grid, county rollup, biodiversity portal aggregation, public-safe density surface | `aggregate` | Supports aggregate claims only at the published support scale. |
| Source program roster, survey schedule, administrative site table, restoration project registry | `administrative` | Supports administrative context; not occurrence truth by itself. |
| Watcher/import result, unresolved community-science submission, unreviewed source row | `candidate` | Hold in WORK/QUARANTINE until reviewed; public edge forbidden. |
| AI-generated, reconstructed, interpolated, or synthetic scenario observation | `synthetic` | Requires reality-boundary disclosure; never observed fact by itself. |

Source role is set at admission or normalization and should not be silently upgraded by promotion. Promotion can approve a derivative release, not rewrite the source's authority.

---

## Sensitivity and release

Flora observations can reveal exact rare-plant locations, steward-controlled records, private-land context, culturally sensitive plant knowledge, source-restricted material, or high-risk habitat associations.

Rules:

- Exact rare-plant and sensitive-plant geometry is deny-by-default for public release.
- Public derivatives must prove redaction, generalization, aggregation, suppression, or withholding with a `RedactionReceipt` or equivalent release proof.
- Public outputs must retain source-role, uncertainty, scale, time, and caveat visibility.
- `candidate`, `synthetic`, sensitivity-unknown, rights-unknown, and evidence-incomplete observations must not enter public outputs.
- Community-science observations require source-rights and geoprivacy checks before reuse.
- Steward-only and private-land notes must stay outside public payloads unless a release decision explicitly approves a transformed public representation.
- AI and search surfaces must abstain or deny when evidence, policy, source role, or sensitivity cannot be resolved.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source exports, specimen dumps, survey notes, community-science rows, stewardship tables, model outputs, and raster/vector extracts remain source-bound. |
| WORK / QUARANTINE | Observations are normalized, deduplicated, taxon-crosswalked, source-role checked, rights checked, sensitivity reviewed, and linked to evidence. Unresolved or risky material remains quarantined. |
| PROCESSED | Reviewed observations receive deterministic identity, evidence links, source-role posture, temporal support, geometry/sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Observation-derived claims may be cataloged or projected only with evidence, source role, time, policy, scale, and caveats preserved. |
| PUBLISHED | Only public-safe derivatives appear in public API/UI/map layers, and only after review, policy, release manifest, redaction proof where needed, and rollback target exist. |
| CORRECTION | Taxon correction, geometry correction, duplicate merge, source withdrawal, rights change, stale-state update, sensitivity update, or evidence correction requires correction and rollback consideration. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/domain_observation.schema.json` beyond the scaffold fields.
- [ ] Add valid fixtures for non-sensitive observed, specimen-derived, phenology, aggregate public-safe, and steward-only restricted observations.
- [ ] Add invalid fixtures for missing `id`, missing `source_descriptor_ref`, unresolved `evidence_refs`, rights-unknown public release, rare-plant exact public geometry, candidate public exposure, synthetic-as-observed mislabeling, and source-role mismatch.
- [ ] Add validator checks for deterministic identity, source role, evidence closure, temporal support, geometry validity, sensitivity class, redaction receipt linkage, release linkage, and correction lineage.
- [ ] Add policy tests for DENY / ABSTAIN / ERROR outcomes.
- [ ] Add no-network fixtures so CI can validate the contract without live source access.
- [ ] Add non-regression tests for stale-state handling, source withdrawal, and correction/rollback paths.

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
| Directory and placement doctrine | Confirms responsibility-root pattern and the split between Markdown contracts and machine schemas. |
| Current repo evidence | Confirms the existing scaffold contract path and paired schema pointer. |
| Flora domain doctrine | Confirms Flora ownership of plant taxa, specimens, occurrences, rare plants, vegetation communities, invasives, phenology, range/habitat associations, surveys, restoration planting, and redaction receipts. |
| Flora sensitivity posture | Confirms rare plants and exact sensitive flora locations require fail-closed, redaction/generalization, review, or denial before public release. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with promotion as a governed state transition. |

---

## Rollback

A released observation derivative must have a rollback path before public exposure.

Rollback triggers include:

- taxon misidentification;
- duplicate observation merge or split;
- geometry correction or geoprivacy failure;
- source withdrawal or changed source terms;
- rare-plant sensitivity update;
- steward review reversal;
- stale data or superseded source version;
- mistaken source-role upgrade;
- invalid redaction/generalization receipt;
- release manifest or catalog integrity failure.

Rollback artifacts should include the affected observation IDs, release IDs, layer IDs, evidence refs, policy decisions, redaction receipts, correction notice, rollback card, and replacement/suppression plan.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is `DomainObservation` intended to remain a generic envelope or become a concrete public DTO? | NEEDS VERIFICATION | Confirm with Flora steward, API steward, and schema steward before schema expansion. |
| Which observation subtypes become required enum values? | NEEDS VERIFICATION | Resolve in schema PR with fixtures. |
| Which geometry precision classes are allowed for public Flora layers? | NEEDS VERIFICATION | Resolve with `policy/sensitivity/flora/` and redaction fixtures. |
| How should community-science source geoprivacy flags map into KFM sensitivity states? | NEEDS VERIFICATION | Source registry + policy tests. |
| When does an aggregate observation become a `RangePolygon`, `DistributionSurface`, or public layer feature instead of `DomainObservation`? | NEEDS VERIFICATION | Contract crosswalk + layer manifest review. |
| Should this contract define an abstract base used by other Flora schemas? | PROPOSED | ADR or schema design note if multiple schemas inherit these fields. |

---

## Related contracts

- `domain_feature_identity.md` — deterministic Flora feature identity and cross-source identity posture.
- `plant_taxon.md` and `flora_taxon_crosswalk.md` — taxonomic meaning and crosswalk authority.
- `flora_occurrence.md` — occurrence claim specialization.
- `rare_plant_record.md` — rare/protected plant record specialization.
- `specimen_record.md` — voucher/specimen-backed specialization.
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
- [ ] Record any contract/schema conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
