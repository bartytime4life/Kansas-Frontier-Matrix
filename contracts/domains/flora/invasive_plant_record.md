<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-invasive-plant-record
title: Invasive Plant Record Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Invasive-species steward · Contract steward · Source steward · Schema steward · Sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; invasive-plant; occurrence-aware; source-role-aware; sensitivity-aware; management-context; no-publication-authority
tags: [kfm, contracts, flora, invasive-plant-record, invasive-species, plant-occurrence, management, source-role, evidence, policy, sensitivity, release, correction, rollback]
related:
  - ./README.md
  - ./plant_taxon.md
  - ./flora_taxon_crosswalk.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./flora_occurrence.md
  - ./occurrence_public.md
  - ./occurrence_restricted.md
  - ./habitat_association.md
  - ./range_polygon.md
  - ./botanical_survey.md
  - ./restoration_planting.md
  - ./redaction_receipt.md
  - ./domain_validation_report.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/invasive_plant_record.schema.json
  - ../../../fixtures/domains/flora/invasive_plant_record/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora invasive-plant semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "InvasivePlantRecord captures invasive plant observation, status, spread, management, and source-role posture; it does not replace FloraOccurrence, PlantTaxon, management policy, release approval, or source authority."
  - "Public invasive-plant records may be appropriate when rights, sensitivity, source role, evidence, review, release, and rollback support resolve; private-land, steward-controlled, threatened-species-adjacent, or culturally sensitive context remains fail-closed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Invasive Plant Record — Flora

> Semantic contract for Flora `InvasivePlantRecord`: the evidence-bound record for invasive plant observations, source status, spread context, management posture, cross-lane interactions, public-safe exposure, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: record not management order" src="https://img.shields.io/badge/boundary-record__not__management__order-critical">
</p>

`contracts/domains/flora/invasive_plant_record.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Invasive record classes](#invasive-record-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/invasive_plant_record.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/invasive_plant_record.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `InvasivePlantRecord` as an EDDMapS-class observation surface that can cross-reference fauna for invasive interactions. Field-level schema shape, fixtures, validators, source registry terms, policy runtime, release workflow, API behavior, UI behavior, cross-domain interaction contracts, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `InvasivePlantRecord` can support an invasive plant observation or status claim only within its evidence, source-role, taxonomic, spatial, temporal, rights, sensitivity, review, and release scope. It does **not** create a management order, does **not** replace `FloraOccurrence`, does **not** prove current infestation by itself, and does **not** authorize public release or treatment recommendations.

---

## Meaning

`InvasivePlantRecord` is the Flora semantic object for invasive or potentially invasive plant records. It may describe a reported invasive plant occurrence, infestation, survey result, management observation, treatment record, risk note, spread context, source status, or cross-domain interaction where the Flora lane owns the plant-side meaning.

It answers:

- Which plant taxon, source taxon label, or reviewed taxon candidate is involved?
- Which source identified the plant as invasive, noxious, watch-list, regulated, managed, or otherwise concern-worthy?
- Was the record observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic?
- What place, time, scale, uncertainty, survey method, infestation extent, abundance, treatment, or management context applies?
- Which evidence, source-role, rights, sensitivity, validation, review, release, correction, and rollback objects must resolve before use?
- Which downstream public-safe map layers, restoration decisions, habitat associations, or cross-domain invasive-interaction claims are allowed or blocked?

An invasive plant record may be high-value for public awareness and land management, but it still follows KFM cite-or-abstain, source-role, rights, sensitivity, and release controls.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Invasive record meaning | `contracts/domains/flora/invasive_plant_record.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/invasive_plant_record.schema.json` | Linked only; currently scaffolded |
| Taxon identity | `contracts/domains/flora/plant_taxon.md`, `flora_taxon_crosswalk.md` | Required for plant identity and status mapping |
| Occurrence support | `contracts/domains/flora/flora_occurrence.md` | Occurrence-class support; not replaced |
| Observation envelope | `contracts/domains/flora/domain_observation.md` | Upstream observation/source normalization |
| Habitat/spread context | `contracts/domains/flora/habitat_association.md`, `range_polygon.md` | Associated habitat/range context; not replaced |
| Survey context | `contracts/domains/flora/botanical_survey.md` | Method, effort, completeness, and detection context |
| Restoration/management context | `contracts/domains/flora/restoration_planting.md` | Management/restoration linkage; not a treatment order |
| Public-safe transform | `contracts/domains/flora/redaction_receipt.md` | Redaction/generalization proof when required |
| Source registry | `data/registry/sources/flora/` | Source identity, role, rights, cadence, attribution |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Admission/release and sensitive-context decisions |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/invasive_plant_record.schema.json` |
| Schema title | `Invasive Plant Record` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/invasive_plant_record.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, policy checks, source registry links, public layers, management-context disclaimers, cross-domain interactions, correction flows, and rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `InvasivePlantRecord` should semantically assert:

1. **Record identity** — deterministic identity for the invasive plant record or candidate.
2. **Taxon identity** — source taxon label, source ID, KFM `PlantTaxon` target, and crosswalk state.
3. **Invasive status** — invasive, noxious, watch-list, regulated, managed, introduced, nuisance, uncertain, or candidate status, with source authority and date.
4. **Occurrence or context basis** — observed occurrence, survey result, infestation polygon, management treatment, regulatory record, aggregate report, modeled risk, or candidate report.
5. **Source and role** — SourceDescriptor, source role, source record ID, source authority limits, cadence, rights, and attribution.
6. **Spatial support** — exact location, generalized location, infestation polygon, survey route, grid, county, management area, range polygon, or public-safe derivative.
7. **Temporal support** — observed, treatment, report, valid, source, retrieval, release, stale-state, and correction times where material.
8. **Evidence support** — EvidenceRef/EvidenceBundle links sufficient for cite-or-abstain behavior.
9. **Sensitivity posture** — private-land, steward-controlled, rare-species-adjacent, culturally sensitive, source-restricted, or public-safe classification.
10. **Governance state** — validation, policy, review, redaction, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating a status-list row as an observed infestation | Regulatory/list status supports concern context, not occurrence proof. |
| Treating a model/risk layer as an observation | Modeled risk must remain modeled and uncertainty-bearing. |
| Treating an old occurrence as current infestation | Temporal support and stale-state must be visible. |
| Treating an invasive record as treatment advice | Management action requires reviewed policy/operations context outside this contract. |
| Publishing private-land or steward-controlled details without release gates | Public exposure can create landowner, conservation, or source-rights risk. |
| Collapsing plant identity and invasive status | Taxon identity and invasive/legal/management status are separate claims. |
| Treating public-safe derivative as canonical exact truth | Public layers are released carriers, not source truth. |
| Direct public access to RAW/WORK/QUARANTINE invasive records | Public clients use governed interfaces and released derivatives only. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical invasive plant record identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `record_class` | `observed_occurrence`, `infestation`, `survey_detection`, `survey_non_detection`, `treatment_record`, `regulatory_status`, `aggregate_report`, `modeled_risk`, `candidate_report`, or `synthetic`. |
| `taxon_ref` | KFM `PlantTaxon` or reviewed taxon candidate. |
| `taxon_crosswalk_ref` | FloraTaxonCrosswalk support. |
| `source_taxon_name` | Source-native plant name retained for audit. |
| `invasive_status` | Source/KFM-normalized status such as invasive, noxious, watch-list, regulated, managed, introduced, uncertain, or candidate. |
| `status_authority_ref` | Source or authority behind the invasive/status classification. |
| `status_effective_time` | Time the status is valid or sourced. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and authority limits. |
| `source_role` | Canonical source role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |
| `source_record_ref` | Source-native record, observation, survey, treatment, polygon, or status-list ID. |
| `domain_observation_ref` | Upstream observation-envelope reference, when applicable. |
| `flora_occurrence_ref` | Occurrence-class support, when applicable. |
| `botanical_survey_ref` | Survey method/effort context, when applicable. |
| `habitat_association_ref` | Habitat/spread/suitability context, when applicable. |
| `range_polygon_ref` | Distribution/risk range context, when applicable. |
| `geometry_ref` | Exact, restricted, generalized, polygon, route, grid, county, or management-area geometry reference. |
| `public_geometry_ref` | Public-safe geometry derivative, when released. |
| `geometry_precision` | Exact, parcel, point-radius, polygon, grid, county, watershed, ecoregion, or unknown support. |
| `abundance_or_extent` | Source-supported count, percent cover, infestation area, density, severity, or qualitative extent. |
| `management_state` | Reported, verified, monitored, treated, eradicated, recurring, unresolved, or unknown. |
| `treatment_refs` | Treatment/management records, if represented elsewhere. |
| `observed_time` | Time of observation/detection. |
| `valid_time` | Time span the record supports. |
| `source_time` | Time asserted by source. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, and access posture. |
| `sensitivity_state` | Private-land, steward, cultural, threatened-species-adjacent, source-restricted, or public-safe posture. |
| `validation_report_ref` | Validation report for this record or release candidate. |
| `policy_decision_ref` | Policy result when exposure, management use, or release is material. |
| `review_record_ref` | Source, steward, sensitivity, domain, or release review. |
| `redaction_receipt_ref` | Generalization, aggregation, suppression, or withholding receipt when public output is derived. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, supersession, withdrawal, stale-state, and rollback lineage. |
| `quality_flags` | Taxon-conflict, status-conflict, stale-record, geometry-conflict, rights-unknown, sensitivity-unknown, source-role-conflict, modeled-not-observed, aggregate-not-exact, or incomplete-evidence flags. |

---

## Invasive record classes

| Class | Meaning | Default posture |
|---|---|---|
| `observed_occurrence` | Source reports a plant detection at a place/time. | Can support occurrence when evidence, taxon, time, geometry, and rights resolve. |
| `infestation` | Source describes a population, patch, polygon, spread area, or density. | Requires extent/scale and date caveats. |
| `survey_detection` | Detection from a survey, route, transect, or inspection. | Requires survey method and effort context. |
| `survey_non_detection` | Source reports no detection in a bounded survey. | Not absence unless method/scope/season support it. |
| `treatment_record` | Report of management action, treatment, removal, or monitoring. | Management context only; not public advice by itself. |
| `regulatory_status` | Noxious/listed/regulated/status record. | Status context, not occurrence proof. |
| `aggregate_report` | County/grid/portal/literature summary. | Aggregate support scale only. |
| `modeled_risk` | Risk, spread, or suitability model. | Must remain modeled with uncertainty. |
| `candidate_report` | Unreviewed import or watcher/community-science row. | Work/quarantine only; no public authoritative use. |
| `synthetic` | Generated/reconstructed/hypothetical record. | Reality-boundary disclosure; never observed fact. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | Record posture |
|---|---|---|
| Field observation, verified EDDMapS-class record, survey detection, treatment observation | `observed` | Can support observed record when evidence, taxonomy, geometry, and time resolve. |
| Noxious weed list, regulatory program list, quarantine status, agency status table | `regulatory` | Supports status/legal context, not occurrence proof. |
| Spread model, risk map, suitability layer, predictive alert | `modeled` | Requires model identity, uncertainty, version, and caveats. |
| County rollup, portal summary, grid count, literature summary | `aggregate` | Supports aggregate claims only. |
| Management program record, project table, treatment schedule | `administrative` | Supports management context, not biological truth by itself. |
| Unreviewed import, watcher result, unresolved community-science observation | `candidate` | Hold in WORK/QUARANTINE until reviewed. |
| AI-generated scenario, reconstructed infestation, hypothetical spread | `synthetic` | Requires reality-boundary disclosure; never observed fact by itself. |

---

## Sensitivity and release

Invasive plant data is often public-benefit information, but it can still carry sensitivity and rights risk.

Rules:

- Public outputs must preserve source role, date, scale, uncertainty, and caveat visibility.
- Private-land, steward-controlled, culturally sensitive, source-restricted, or threatened-species-adjacent details must fail closed unless policy/review/release allows a transformed public representation.
- Candidate, synthetic, rights-unknown, source-restricted, stale, and evidence-incomplete records must not enter public outputs as authoritative current infestations.
- Treatment or management records must not be turned into recommendations without reviewed policy and operational context.
- Records that imply nearby rare species, protected habitat, archaeological/cultural context, or vulnerable landowner information require sensitivity review before public map release.
- Public layers should use generalized or aggregate support when exact detail creates avoidable exposure risk.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source observations, reports, status lists, treatment logs, model outputs, and portal exports remain source-bound. |
| WORK / QUARANTINE | Candidate records are normalized, taxon-crosswalked, source-role checked, rights checked, sensitivity-screened, deduplicated, and evidence-linked. Risky or unresolved material remains quarantined. |
| PROCESSED | Reviewed records receive deterministic identity, taxon support, status support, source/version support, spatial/temporal support, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Invasive-plant claims may be cataloged or projected only with evidence, source role, time, support scale, and caveats preserved. |
| PUBLISHED | Only public-safe derivatives appear in public API/UI/map layers after validation, policy, review, release manifest, redaction proof where needed, and rollback target. |
| CORRECTION | Taxon correction, status-list update, source withdrawal, treatment update, stale-state change, geometry correction, or sensitivity update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/invasive_plant_record.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for observed occurrence, infestation polygon, survey detection, survey non-detection, regulatory status, modeled risk, aggregate report, treatment record, and public-safe derivative.
- [ ] Add invalid fixtures for missing source role, missing taxon support, regulatory status treated as occurrence proof, modeled risk treated as observed, aggregate report treated as exact, stale record without caveat, rights-unknown public release, private-land exact exposure, missing redaction receipt, and missing rollback target.
- [ ] Add validator checks for deterministic identity, source role, taxon crosswalk, invasive status authority, evidence refs, spatial support scale, temporal support, management-state caveats, sensitivity state, redaction receipt linkage, release linkage, and correction lineage.
- [ ] Add policy tests for public-benefit release, private-land protection, source-restricted rows, stale data, and management-advice prevention.
- [ ] Add cross-domain tests for invasive interactions that touch fauna, habitat, restoration, and public map filters.
- [ ] Add no-network fixtures so CI can validate the contract without live source access.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, policy allows, review passes, release exists | `ANSWER` / public-safe record allowed |
| Evidence missing, temporal support insufficient, source role ambiguous, status authority unresolved | `ABSTAIN` |
| Sensitive exposure, direct RAW/WORK/QUARANTINE access, rights denial, unsafe management recommendation | `DENY` |
| Schema/validator/runtime failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Directory Rules | Confirms `contracts/` owns object meaning, `schemas/` owns machine shape, and domain-specific files live as segments inside responsibility roots. |
| Flora canonical path register | Confirms `InvasivePlantRecord` is a Flora object-family contract and describes it as an EDDMapS-class observation surface with possible fauna cross-references for invasive interactions. |
| Flora object-family register | Confirms `InvasivePlantRecord` is an expected Flora object family and that field-level shape remains outside the register. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM trust posture | Confirms evidence, source role, policy, review, release, correction, and rollback must outrank generated summaries or map displays. |

---

## Rollback

Invasive-plant rollback is required when a released or review-authorized record changes public awareness, management interpretation, map filters, restoration planning, invasive-interaction claims, AI answers, or published layers.

Rollback triggers include:

- taxon correction or crosswalk supersession;
- invasive/noxious/status-list update;
- source withdrawal or rights change;
- stale observation treated as current infestation;
- modeled/aggregate record published as observed exact location;
- private-land, steward, or source-restricted details exposed;
- mistaken management/treatment implication;
- redaction/generalization receipt is missing or invalid;
- downstream release depends on a superseded record;
- correction notice invalidates the record basis.

Rollback artifacts should include affected invasive record IDs, taxon IDs, occurrence IDs, source records, treatment/management refs, release IDs, layer IDs, evidence refs, policy decisions, redaction receipts, correction notices, rollback cards, and replacement/suppression plan.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which source families are approved for invasive plant records, and what are their rights/redistribution limits? | NEEDS VERIFICATION | Source registry and source steward review. |
| Should treatment records remain in Flora or move to a management/restoration contract family? | PROPOSED / NEEDS VERIFICATION | Review with restoration, policy, and release stewards. |
| Which invasive statuses are canonical enum values? | NEEDS VERIFICATION | Resolve with schema, fixtures, and source registry examples. |
| How should EDDMapS-class source data map into source roles, geoprivacy, and public layers? | NEEDS VERIFICATION | Source-specific profile and validation fixtures. |
| How should invasive plant/fauna interactions be modeled without creating cross-domain authority drift? | NEEDS VERIFICATION | Define cross-domain interaction contract or ADR if needed. |
| Which stale-date thresholds should trigger warnings, abstention, or rollback? | NEEDS VERIFICATION | Policy + validation steward decision. |

---

## Related contracts

- `plant_taxon.md` and `flora_taxon_crosswalk.md` — plant identity and status mapping support.
- `domain_observation.md` — source observation envelope.
- `flora_occurrence.md` — occurrence-class record support.
- `occurrence_public.md` and `occurrence_restricted.md` — public-safe and restricted occurrence derivatives.
- `habitat_association.md` — habitat/spread/suitability context.
- `range_polygon.md` — distribution/risk/range context.
- `botanical_survey.md` — survey method, effort, and completeness context.
- `restoration_planting.md` — restoration/management context.
- `redaction_receipt.md` — public-safe transformation proof.
- `domain_validation_report.md` — validation reports for records, policy, sensitivity, fixtures, and releases.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any public invasive layer depends on this contract.
- [ ] Add source profiles for approved invasive plant sources before activation.
- [ ] Add policy tests for private-land, source-restricted, stale, modeled, aggregate, and management-advice cases.
- [ ] Confirm public API/UI surfaces do not expose unreviewed candidate records or turn records into treatment recommendations.
- [ ] Record any contract/schema/path conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
