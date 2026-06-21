<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-specimen-record
title: Specimen Record Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Specimen steward · Herbarium/source steward · Taxonomy steward · Contract steward · Schema steward · Sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; specimen-record; voucher; herbarium; source-role-aware; locality-sensitive; evidence-bound; release-gated; no-current-occurrence-proof
tags: [kfm, contracts, flora, specimen-record, herbarium, voucher, catalog, accession, collector, determination, locality, plant-taxon, occurrence, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./plant_taxon.md
  - ./flora_taxon_crosswalk.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./flora_occurrence.md
  - ./occurrence_public.md
  - ./occurrence_restricted.md
  - ./rare_plant_record.md
  - ./phenology_observation.md
  - ./vegetation_community.md
  - ./invasive_plant_record.md
  - ./range_polygon.md
  - ./habitat_association.md
  - ./botanical_survey.md
  - ./redaction_receipt.md
  - ./domain_validation_report.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/specimen_record.schema.json
  - ../../../fixtures/domains/flora/specimen_record/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora specimen/voucher semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "SpecimenRecord captures herbaria-sourced vouchered specimen evidence, determinations, catalog/accession identity, collection event context, locality posture, and correction lineage."
  - "A specimen can support historical evidence and determinations, but it does not by itself prove current occurrence, public exact locality release, accepted taxonomy, or management action."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Specimen Record — Flora

> Semantic contract for Flora `SpecimenRecord`: the evidence-bound voucher object for herbarium, museum, institutional, collector, image, catalog, accession, determination, collection-event, locality, public-safe derivative, correction, and rollback support.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: voucher not current occurrence proof" src="https://img.shields.io/badge/boundary-voucher__not__current__occurrence__proof-critical">
</p>

`contracts/domains/flora/specimen_record.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Specimen classes](#specimen-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/specimen_record.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/specimen_record.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `SpecimenRecord` as the herbaria-sourced vouchered specimen object. Field-level schema shape, fixtures, validators, source registry terms, policy runtime, release workflow, API behavior, UI behavior, digitization/image handling, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `SpecimenRecord` is voucher evidence. It does **not** prove current occurrence by itself, does **not** replace `PlantTaxon`, `FloraOccurrence`, `OccurrenceRestricted`, `OccurrencePublic`, `RarePlantRecord`, or `PhenologyObservation`, and does **not** authorize public release of exact sensitive locality, collector notes, images, or institution-restricted metadata by itself.

---

## Meaning

`SpecimenRecord` is the Flora semantic object for a plant voucher, herbarium sheet, accession, catalog record, collection event, image-backed specimen, determination, re-determination, or institutional specimen record used as evidence in KFM.

It answers:

- Which voucher or specimen record is being referenced?
- Which institution, collection, catalog/accession identifier, collector, collection event, determination, image, and source record support it?
- Which source-native taxon label and KFM `PlantTaxon`/crosswalk state apply?
- What collection locality, date, locality precision, georeference, coordinate uncertainty, and public-safe geometry posture apply?
- Does the specimen support a historical occurrence, phenology phase, range evidence, rare-plant record, invasive record, or taxonomic correction?
- Which rights, source terms, sensitivity, review state, release state, correction state, and rollback target govern use?

A specimen record can be high-value evidence. It still remains source-role-bound, time-bound, locality-sensitive, and subordinate to evidence, policy, review, release, and correction controls.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Specimen/voucher meaning | `contracts/domains/flora/specimen_record.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/specimen_record.schema.json` | Linked only; currently scaffolded |
| Taxon identity | `plant_taxon.md`, `flora_taxon_crosswalk.md` | Determination, source name, synonym, and accepted/candidate identity support |
| Observation envelope | `domain_observation.md` | Source observation/collection-event support where modeled separately |
| Occurrence surfaces | `flora_occurrence.md`, `occurrence_restricted.md`, `occurrence_public.md` | Specimen may support occurrence derivatives; not replaced by voucher |
| Rare/sensitive support | `rare_plant_record.md`, `redaction_receipt.md` | Sensitive specimen locality and public-safe transform handling |
| Time/context users | `phenology_observation.md`, `range_polygon.md`, `habitat_association.md`, `vegetation_community.md` | Downstream users of specimen evidence/caveats |
| Survey context | `botanical_survey.md` | Survey/collection episode context when applicable |
| Validation report | `domain_validation_report.md` | Validates record, crosswalk, policy, fixtures, and release readiness |
| Source registry | `data/registry/sources/flora/` | Source identity, role, rights, cadence, attribution, access limits |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Admission/release and locality-sensitive decisions |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only after governed release |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/specimen_record.schema.json` |
| Schema title | `Specimen Record` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/specimen_record.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, source registry links, determination/crosswalk logic, sensitivity policy, public derivatives, correction flows, and rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `SpecimenRecord` should semantically assert:

1. **Specimen identity** — deterministic identity for the voucher, catalog/accession record, image record, or source specimen record.
2. **Institution/source support** — institution, collection, herbarium, portal, source descriptor, source record ID, rights, cadence, and attribution.
3. **Collection event** — collector, collector number, collection date, collection locality, habitat notes, associated taxa, and event context when supported.
4. **Determination support** — source-native name, determiner, determination date, current determination, prior determinations, uncertainty, and crosswalk state.
5. **Taxon support** — PlantTaxon and FloraTaxonCrosswalk refs, including candidate/synonym/unresolved caveats.
6. **Locality support** — exact, georeferenced, uncertain, generalized, obscured, withheld, restricted, or public-safe geometry support.
7. **Evidence support** — specimen image, label, catalog metadata, institution record, observation envelope, and EvidenceRef/EvidenceBundle links.
8. **Sensitivity posture** — rare/protected locality, private land, cultural plant context, source-restricted image/metadata, collector note sensitivity, or public-safe state.
9. **Derived-use posture** — occurrence, phenology, range, habitat, invasive, rare-plant, or taxonomic correction use with caveats.
10. **Governance state** — validation, policy, review, redaction, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating specimen as current occurrence proof | A collection event proves historical evidence at a time and support scale, not current presence. |
| Treating label text as accepted taxonomy | Determinations can change; source names must remain auditable. |
| Treating georeferenced locality as public-safe by default | Specimen localities can expose rare/protected plants, private land, or cultural context. |
| Publishing institution-restricted images or metadata | Source rights and access terms remain controlling. |
| Erasing prior determinations | Determination history is evidence and correction lineage. |
| Collapsing duplicate specimens without audit | Duplicates, isolectotypes, sheets, fragments, and images need explicit identity handling. |
| Treating a specimen image as public evidence without projection review | Images and labels can leak restricted localities or notes. |
| Direct public access to RAW/WORK/QUARANTINE specimen rows | Public clients consume governed released derivatives only. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM specimen record identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `record_class` | `voucher_specimen`, `herbarium_sheet`, `catalog_record`, `image_record`, `duplicate_specimen`, `fragment`, `type_specimen`, `sensitive_specimen`, `candidate_record`, or `synthetic`. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and authority limits. |
| `source_role` | Canonical source role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |
| `source_record_ref` | Source-native specimen/catalog/image record ID. |
| `institution_code` | Institution or herbarium code, if source provides it. |
| `collection_code` | Collection code or named collection. |
| `catalog_number` | Catalog/accession/barcode/sheet identifier. |
| `collector` | Collector or collecting team, with privacy/source caveats where needed. |
| `collector_number` | Collector number or source collection identifier. |
| `collection_event_ref` | Collection-event reference, if modeled separately. |
| `collection_time` | Collection date/time or range. |
| `collection_time_precision` | Exact date, month, year, range, label-derived, unknown, or source-native precision. |
| `source_taxon_name` | Source-native taxon name retained for audit. |
| `taxon_ref` | KFM PlantTaxon or reviewed candidate. |
| `taxon_crosswalk_ref` | Crosswalk support for source names, backbone IDs, synonyms, and status. |
| `determination_refs` | Current and prior determination records or summaries. |
| `determiner` | Determiner or reviewing authority, when source provides it. |
| `determination_time` | Determination or re-determination time, if known. |
| `determination_status` | Current, prior, tentative, disputed, unresolved, superseded, rejected, or unknown. |
| `type_status` | Type, holotype, isotype, paratype, voucher, non-type, unknown, or source-native type status. |
| `image_refs` | Specimen/label/image/media refs with rights/access posture. |
| `label_text_ref` | Label OCR/transcription ref, if available and rights/sensitivity allow. |
| `locality_text_ref` | Source locality text ref, access-controlled when sensitive. |
| `geometry_ref` | Exact/restricted/georeferenced geometry reference. |
| `public_geometry_ref` | Public-safe derivative geometry reference, if released. |
| `coordinate_uncertainty` | Source/native/georeferenced uncertainty. |
| `georeference_method` | Source-provided, georeferenced, label-derived, county centroid, generalized, withheld, or unknown. |
| `locality_precision` | Exact, high precision, county, grid, generalized, obscured, withheld, or unknown. |
| `occurrence_ref` | FloraOccurrence ref derived from or supported by the specimen, when applicable. |
| `occurrence_restricted_ref` | Restricted exact occurrence ref, if applicable. |
| `occurrence_public_ref` | Public-safe occurrence derivative, if released. |
| `rare_plant_record_ref` | Rare/protected record, if applicable. |
| `phenology_observation_ref` | Specimen-derived phenology ref, if applicable. |
| `range_polygon_ref` | Range/distribution support derived from specimen, if applicable. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, image terms, attribution, access, and source-term posture. |
| `sensitivity_state` | Rare-plant, exact-locality, private-land, cultural, source-restricted, public-safe, or unknown posture. |
| `policy_decision_ref` | Policy result when exposure, image use, locality projection, or release is material. |
| `validation_report_ref` | Validation report for this record or release candidate. |
| `review_record_ref` | Source, taxon, specimen, sensitivity, or release review. |
| `redaction_receipt_ref` | Required when locality, label text, image details, or source fields are transformed for public output. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, re-determination, source withdrawal, image takedown, locality correction, supersession, and rollback lineage. |
| `quality_flags` | Taxon-conflict, duplicate-candidate, locality-uncertain, label-ocr-risk, rights-unknown, sensitivity-unknown, stale-determination, source-role-conflict, or incomplete-evidence flags. |

---

## Specimen classes

| Class | Meaning | Default posture |
|---|---|---|
| `voucher_specimen` | Physical or institutional voucher supporting a collection event. | Strong evidence; still time-bound and locality-sensitive. |
| `herbarium_sheet` | Sheet-level record from herbarium or portal. | Preserve institution/catalog identity and rights. |
| `catalog_record` | Metadata-only catalog/accession record. | Evidence depends on source completeness and review. |
| `image_record` | Specimen, label, or media record. | Rights and sensitive-label projection required. |
| `duplicate_specimen` | Duplicate sheet/fragment/associated record. | Requires duplicate linkage and non-collapse proof. |
| `fragment` | Partial specimen or fragment record. | Requires context and source caveats. |
| `type_specimen` | Type or nomenclatural specimen. | Taxonomic significance; source authority limits remain. |
| `sensitive_specimen` | Locality, taxon, image, or notes are sensitive/restricted. | Restrict exact/public projection by default. |
| `candidate_record` | Unreviewed import or unresolved specimen row. | WORK/QUARANTINE only. |
| `synthetic` | Generated or hypothetical specimen note. | Reality-boundary disclosure; never voucher fact. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | SpecimenRecord posture |
|---|---|---|
| Vouchered specimen, collector label, herbarium sheet, verified catalog record | `observed` | Supports historical collection evidence when identity, date, locality, and source resolve. |
| Type status, protected-list linkage, institutional restriction, nomenclatural designation | `regulatory` | Supports status/context; not occurrence proof by itself. |
| Georeference model, inferred locality, predicted taxon match, OCR/transcription model | `modeled` | Must remain modeled/inferred with uncertainty. |
| Portal rollup, aggregate specimen count, checklist derived from collections | `aggregate` | Aggregate support only; not exact voucher detail. |
| Institution accession metadata, loan record, digitization workflow status | `administrative` | Operational/catalog context; not biological occurrence by itself. |
| Unreviewed import, unresolved OCR row, duplicate candidate, unmatched source record | `candidate` | Hold in WORK/QUARANTINE until reviewed. |
| AI-generated specimen description or reconstructed label | `synthetic` | Must not be treated as source voucher evidence. |

Source role must survive downstream projection. A specimen record can strengthen evidence; it cannot silently upgrade inferred taxonomy, locality, or current occurrence claims.

---

## Sensitivity and release

Specimen records often carry locality, collector, institution, label, image, and taxon information that can be sensitive even when the source is public.

Rules:

- Exact rare/protected plant localities, private-land context, culturally sensitive plant information, institution-restricted fields, and sensitive collector notes must fail closed unless policy/review allows public projection.
- Public derivatives should generalize locality, suppress label details, project only safe citations, or withhold media where exposure risk is material.
- Public payloads must preserve source role, collection time, locality uncertainty, determination state, rights, and caveats.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, source-restricted, duplicate-unresolved, or evidence-incomplete records must not enter public outputs as authoritative voucher facts.
- Specimen-derived phenology, range, occurrence, rare-plant, or taxon claims require separate downstream review and caveats.
- Public evidence/citation projections must avoid leaking exact restricted locality, label text, source-private notes, or image details.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native specimen rows, images, OCR text, labels, coordinates, catalog fields, and institution notes remain source-bound. |
| WORK / QUARANTINE | Candidate records are normalized, taxon-crosswalked, duplicate-checked, rights checked, sensitivity-screened, georeference-checked, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, catalog/source support, determination state, spatial/temporal support, evidence links, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Specimen claims may be cataloged or projected only with evidence, source role, locality precision, collection time, rights, and caveats preserved. |
| RELEASE CANDIDATE | Public specimen derivatives require validation report, policy decision, review record, redaction receipt when transformed, release manifest, and rollback target. |
| PUBLISHED | Only public-safe specimen summaries, occurrence derivatives, labels, or citations appear after governed release. |
| CORRECTION | Re-determination, duplicate merge/split, locality correction, source withdrawal, rights change, image takedown, sensitivity update, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/specimen_record.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for voucher specimen, herbarium sheet, catalog-only record, image-backed record, duplicate specimen, type specimen, sensitive specimen, candidate record, and public-safe derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing catalog/source identity, missing source role, accepted taxonomy from label text alone, current occurrence inferred from historical specimen, exact rare-plant locality public output, missing image rights, missing redaction receipt for transformed locality, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, catalog/accession fields, source role, taxon crosswalk, determination state, collection time precision, locality precision, evidence refs, rights state, sensitivity state, public derivative linkage, release linkage, and correction lineage.
- [ ] Add policy tests for rare-plant locality, private-land locality, institution-restricted media, source-restricted fields, candidate rows, OCR/model-derived data, and public citation projection.
- [ ] Add no-network fixtures so CI can validate this contract without live source access.
- [ ] Add non-regression tests for re-determination, duplicate merge/split, locality correction, source withdrawal, image takedown, redaction bug, and rollback of released derivatives.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, rights/sensitivity allow, review passes, release exists | `ANSWER` / public-safe specimen claim allowed |
| Evidence missing, source role ambiguous, determination/locality unresolved, rights unclear | `ABSTAIN` |
| Sensitive locality exposure, direct RAW/WORK/QUARANTINE access, rights denial, restricted media leak | `DENY` |
| Schema/validator/runtime/source-read failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Directory Rules / canonical path register | Confirms `contracts/` owns object meaning, schemas own machine shape, and `SpecimenRecord` is the Flora object-family contract for herbaria-sourced vouchered specimens. |
| Flora object-family register | Confirms `SpecimenRecord` is an expected Flora object family and that field-level shape remains outside the register. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM trust posture | Confirms evidence, source role, policy, review, release, correction, and rollback must outrank generated labels, maps, specimen summaries, or inferred occurrence claims. |

---

## Rollback

Specimen rollback is required when a released or review-authorized specimen claim weakens source integrity, leaks sensitive locality/media, misstates taxon determination, violates rights, misrepresents current occurrence, or depends on superseded evidence.

Rollback triggers include:

- re-determination or taxon crosswalk correction;
- duplicate merge/split or catalog identity correction;
- locality/georeference correction or precision downgrade;
- exact or inferable rare/protected plant locality exposure;
- private-land, cultural, collector-note, or source-restricted detail exposed;
- image/media rights change, takedown request, or source withdrawal;
- historical specimen published as current occurrence;
- label OCR/model inference published as reviewed fact;
- public derivative lacks redaction receipt, release manifest, or rollback target;
- release manifest points to RAW/WORK/QUARANTINE or restricted source instead of public-safe derivative.

Rollback artifacts should include affected SpecimenRecord IDs, institution/source IDs, catalog/accession IDs, taxon/crosswalk IDs, occurrence/rare/phenology/range derivative IDs, public derivative IDs, release IDs, layer/API/UI IDs, evidence refs, policy decisions, redaction receipts, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which herbarium/portal/source families are approved, and what rights/access limits apply? | NEEDS VERIFICATION | Source registry, specimen steward review, and policy tests. |
| Which fields define deterministic specimen identity across duplicate records and portals? | NEEDS VERIFICATION | Schema fixtures for institution/catalog/barcode/collector/source ID collisions. |
| How should re-determinations be modeled: nested history or separate determination objects? | PROPOSED / NEEDS VERIFICATION | Taxonomy/specimen schema review. |
| How should OCR label text be stored and public-projected safely? | NEEDS VERIFICATION | Evidence projection and redaction fixtures. |
| What rules distinguish specimen-supported occurrence from current occurrence? | NEEDS VERIFICATION | Fixtures spanning SpecimenRecord, FloraOccurrence, and OccurrencePublic. |
| Which media/image fields may be public when locality or label text is sensitive? | NEEDS VERIFICATION | Source rights + sensitivity policy review. |

---

## Related contracts

- `plant_taxon.md` and `flora_taxon_crosswalk.md` — taxon identity, determinations, source names, and synonyms.
- `domain_observation.md` — source observation/collection-event envelope.
- `flora_occurrence.md`, `occurrence_public.md`, and `occurrence_restricted.md` — occurrence surfaces that may be supported by specimens but remain distinct.
- `rare_plant_record.md` — rare/protected specimen locality and sensitivity handling.
- `phenology_observation.md` — specimen-derived flowering, fruiting, seed, or senescence evidence.
- `range_polygon.md` and `habitat_association.md` — downstream spatial/contextual claims that may use specimen support.
- `botanical_survey.md` — collection/survey episode context where applicable.
- `redaction_receipt.md` — public-safe locality/media/evidence transformation proof.
- `domain_validation_report.md` — validation reports for records, policy, fixtures, and releases.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any specimen-backed occurrence, phenology, range, taxon, or public citation depends on this contract.
- [ ] Add source profiles for approved herbarium/specimen/image portals before activation.
- [ ] Add policy tests for rare-plant locality, private-land locality, institution-restricted media, source-restricted labels, candidate records, and OCR/model-derived fields.
- [ ] Confirm public API/UI/map/AI surfaces do not treat specimens as current occurrence proof or leak restricted locality/media.
- [ ] Confirm every public derivative has release manifest, redaction receipt when transformed, correction path, and rollback target.
- [ ] Record any contract/schema/path/source/determination conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
