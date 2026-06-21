<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-phenology-observation
title: Phenology Observation Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Phenology steward · Time steward · Contract steward · Source steward · Schema steward · Sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; phenology; time-series; seasonal-observation; source-role-aware; sensitivity-aware; release-gated; no-publication-authority
tags: [kfm, contracts, flora, phenology-observation, flowering, leaf-out, fruiting, senescence, time-series, plant-taxon, occurrence, evidence, source-role, sensitivity, policy, release, correction, rollback]
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
  - ./specimen_record.md
  - ./vegetation_community.md
  - ./habitat_association.md
  - ./range_polygon.md
  - ./botanical_survey.md
  - ./restoration_planting.md
  - ./redaction_receipt.md
  - ./domain_validation_report.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/phenology_observation.schema.json
  - ../../../fixtures/domains/flora/phenology_observation/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora phenology-observation semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "PhenologyObservation captures time-bound plant seasonal state such as flowering, leaf-out, fruiting, senescence, dormancy, or derived/aggregate/model phenology; it does not replace occurrence, survey, taxon, or release authority."
  - "Phenology records can expose sensitive species timing, exact rare-plant locations, harvest/collection windows, or private-land context; public use requires evidence, policy, review, redaction, release, correction, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Phenology Observation — Flora

> Semantic contract for Flora `PhenologyObservation`: the evidence-bound, time-aware record of plant seasonal state, including flowering, leaf-out, fruiting, senescence, dormancy, survey snapshots, specimen-derived phenology, aggregate summaries, and modeled seasonal timing.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: seasonal observation not occurrence proof" src="https://img.shields.io/badge/boundary-seasonal__not__occurrence__proof-critical">
</p>

`contracts/domains/flora/phenology_observation.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Phenology classes](#phenology-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/phenology_observation.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/phenology_observation.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `PhenologyObservation` as the time-series flowering / leaf-out / senescence object. Field-level schema shape, fixtures, validators, source registry terms, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `PhenologyObservation` records seasonal-state support. It does **not** prove current occurrence by itself, does **not** replace `FloraOccurrence`, `BotanicalSurvey`, `SpecimenRecord`, `PlantTaxon`, or `RangePolygon`, and does **not** authorize public release of exact sensitive plant timing or location details.

---

## Meaning

`PhenologyObservation` is the Flora semantic object for a bounded claim that a plant taxon, occurrence, specimen, survey subject, vegetation-community subject, restoration planting, or modeled/aggregate flora subject was in a seasonal state at a stated time, place, and support scale.

It answers:

- Which plant subject was observed, inferred, modeled, aggregated, or reported?
- Which phenological phase was recorded: bud, leaf-out, flowering, fruiting, seed, senescence, dormancy, absence of phase, or other source-native state?
- What time support, date precision, season, duration, uncertainty, and source timestamp apply?
- What place or public-safe spatial support applies?
- Is the source observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic?
- Which evidence, taxon support, occurrence/survey support, sensitivity review, release state, correction path, and rollback target control downstream use?

A phenology observation can support seasonal interpretation, time-series views, climate-change analysis, restoration timing, survey planning, and public caveats. It is not a substitute for occurrence proof or policy-reviewed release.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Phenology meaning | `contracts/domains/flora/phenology_observation.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/phenology_observation.schema.json` | Linked only; currently scaffolded |
| Taxon identity | `contracts/domains/flora/plant_taxon.md`, `flora_taxon_crosswalk.md` | Plant identity and source-name support |
| Occurrence support | `flora_occurrence.md`, `occurrence_public.md`, `occurrence_restricted.md` | Presence/geoprivacy context; not replaced |
| Rare/protected support | `rare_plant_record.md` | Sensitive plant timing/location context |
| Voucher support | `specimen_record.md` | Specimen-derived flowering/fruiting state support |
| Survey support | `botanical_survey.md`, `domain_observation.md` | Method, effort, observation envelope, completeness |
| Community/restoration support | `vegetation_community.md`, `restoration_planting.md` | Community/project seasonal state context |
| Public-safe transform | `redaction_receipt.md`, `occurrence_public.md` | Required when timing/location detail is transformed for release |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Admission/release and sensitive-context decisions |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/phenology_observation.schema.json` |
| Schema title | `Phenology Observation` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/phenology_observation.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, policy checks, public time-series payloads, release manifests, correction flows, and rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `PhenologyObservation` should semantically assert:

1. **Observation identity** — deterministic identity for the phenology record or series member.
2. **Plant subject** — PlantTaxon, source taxon, occurrence, specimen, survey subject, community, restoration planting, or candidate subject.
3. **Phenophase** — source-native and normalized phase/state with clear vocabulary and uncertainty.
4. **Phase evidence** — observed, specimen-derived, image-derived, survey-derived, modeled, aggregate, administrative, candidate, or synthetic basis.
5. **Time support** — date/time, date precision, season, duration/window, source time, retrieval time, release time, and stale state.
6. **Spatial support** — exact, restricted, public-safe, plot, survey route, grid, county, range, or suppressed geometry support.
7. **Source and role** — SourceDescriptor, source role, source record ID, source authority limits, rights, cadence, and attribution.
8. **Taxon support** — taxon/crosswalk state and original source label retained for audit.
9. **Sensitivity posture** — sensitive species timing, exact rare-plant location, private land, cultural plant knowledge, harvest/collection risk, or public-safe state.
10. **Governance state** — validation, policy, review, redaction, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating phenology as occurrence proof | Seasonal state does not prove current presence without occurrence/specimen/survey support. |
| Treating modeled bloom timing as observed bloom | `modeled` source role and uncertainty must remain visible. |
| Treating one date as a full seasonal window | Date precision, duration, and sampling effort must be explicit. |
| Publishing exact rare-plant bloom/fruit timing with location | This can expose sensitive locations or collection windows and must fail closed. |
| Hiding source-native phenophase terms | Source vocabulary must remain auditable for correction and crosswalk. |
| Turning seasonal patterns into management advice | Restoration or treatment recommendations require reviewed policy/operations context. |
| Collapsing community-science candidate records into authoritative facts | Candidate records require review before authoritative use. |
| Direct public access to RAW/WORK/QUARANTINE phenology rows | Public clients consume governed released derivatives only. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical phenology observation identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `record_class` | `observed_phase`, `specimen_derived`, `survey_snapshot`, `time_series_point`, `aggregate_summary`, `modeled_phase`, `administrative_window`, `candidate_report`, or `synthetic`. |
| `flora_subject_type` | `plant_taxon`, `flora_occurrence`, `specimen_record`, `rare_plant_record`, `botanical_survey`, `vegetation_community`, `restoration_planting`, or candidate. |
| `flora_subject_ref` | Flora subject reference. |
| `taxon_ref` | KFM PlantTaxon or reviewed candidate. |
| `taxon_crosswalk_ref` | Taxon-crosswalk support. |
| `source_taxon_name` | Source-native taxon name retained for audit. |
| `phenophase_source` | Source-native phenophase/state text or code. |
| `phenophase_normalized` | Normalized phase such as bud, leaf-out, flowering, fruiting, seed, senescence, dormancy, no-phase-detected, or unknown. |
| `phenophase_intensity` | Count, percentage, categorical intensity, abundance, or source-native scale where supported. |
| `phenophase_certainty` | Certainty or confidence for the phase/state. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and authority limits. |
| `source_role` | Canonical source role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |
| `source_record_ref` | Source-native observation, specimen, survey, image, model, or event ID. |
| `domain_observation_ref` | Upstream observation-envelope reference, when applicable. |
| `flora_occurrence_ref` | Occurrence support, when applicable. |
| `specimen_record_ref` | Voucher/specimen support, when applicable. |
| `botanical_survey_ref` | Survey method/effort/completeness context, when applicable. |
| `geometry_ref` | Exact, restricted, generalized, plot, route, grid, county, range, or public-safe geometry reference. |
| `public_geometry_ref` | Public-safe derivative geometry, when released. |
| `spatial_support_scale` | Exact, plot, transect, grid, county, ecoregion, range, statewide, aggregate, modeled, or unknown. |
| `observed_time` | Time/date of phenology observation. |
| `observed_time_precision` | Exact date, month, season, year, range, specimen label, source approximate, or unknown. |
| `phenology_window_start` | Start of phase window, if known. |
| `phenology_window_end` | End of phase window, if known. |
| `source_time` | Time asserted by source. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `stale_state` | Current, historical, stale, superseded, withdrawn, or unknown. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, and access posture. |
| `sensitivity_state` | Sensitive timing, rare-plant, exact-location, private-land, cultural, source-restricted, or public-safe posture. |
| `policy_decision_ref` | Policy result when exposure, recommendation, or release is material. |
| `validation_report_ref` | Validation report for this observation or release candidate. |
| `review_record_ref` | Source, taxon, sensitivity, domain, or release review. |
| `redaction_receipt_ref` | Required if location, timing, or details are generalized, delayed, suppressed, or transformed. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, supersession, withdrawal, stale-state, and rollback lineage. |
| `quality_flags` | Taxon-conflict, phase-conflict, date-precision-gap, stale-record, modeled-not-observed, aggregate-not-exact, rights-unknown, sensitivity-unknown, or incomplete-evidence flags. |

---

## Phenology classes

| Class | Meaning | Default posture |
|---|---|---|
| `observed_phase` | Field/community-science/steward observation of a phase at place/time. | Can support claims when evidence, taxon, time, geometry, and rights resolve. |
| `specimen_derived` | Phenology inferred from specimen label/image/determination. | Retain specimen context and collection-date precision. |
| `survey_snapshot` | Phase observed during a bounded survey episode. | Requires survey method/effort and absence limitations. |
| `time_series_point` | One point in a repeated observation series. | Requires series identity and temporal consistency checks. |
| `aggregate_summary` | County/grid/range/portal/literature seasonal summary. | Aggregate scale only; not exact observation. |
| `modeled_phase` | Predicted bloom/leaf/fruit/senescence window. | Must remain modeled with uncertainty. |
| `administrative_window` | Management/restoration/survey calendar or planned window. | Administrative context, not biological observation. |
| `candidate_report` | Unreviewed import or unresolved community-science row. | WORK/QUARANTINE only; no public authoritative use. |
| `synthetic` | Generated/reconstructed/hypothetical seasonal state. | Reality-boundary disclosure; never observed fact by itself. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | Phenology posture |
|---|---|---|
| Field observation, steward note, verified community-science record, specimen image/label, survey detection | `observed` | Can support phenology when evidence, taxon, time, geometry, and rights resolve. |
| Agency seasonal restriction, harvest/collection window, recovery-plan timing rule | `regulatory` | Supports policy/status context, not phase observation proof. |
| Bloom model, growing-degree-day prediction, remote-sensing inference, climate projection | `modeled` | Requires model identity, uncertainty, version, and caveats. |
| Atlas summary, county/month rollup, literature seasonal range | `aggregate` | Supports aggregate claims only. |
| Restoration schedule, survey plan, management calendar | `administrative` | Planning context, not biological observation. |
| Unreviewed import, watcher result, unresolved community-science report | `candidate` | Hold in WORK/QUARANTINE until reviewed. |
| AI-generated seasonal note or reconstructed phase | `synthetic` | Requires reality-boundary disclosure; never observed fact by itself. |

---

## Sensitivity and release

Phenology records can expose more than dates. A precise flowering or fruiting record joined to exact location may reveal rare-plant sites, collection/harvest windows, private-land context, or culturally sensitive plant knowledge.

Rules:

- Exact rare-plant phenology tied to precise location is deny-by-default for public release.
- Public outputs should generalize, delay, aggregate, suppress, or withhold timing/location detail when exposure risk is material.
- Public payloads must preserve source role, date precision, uncertainty, support scale, and caveats.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, source-restricted, stale, or evidence-incomplete records must not enter public outputs as authoritative observations.
- Restoration or management timing must not be presented as advice without reviewed policy and operational context.
- Public evidence/citation projections must not leak restricted exact geometry, internal steward notes, private source details, or sensitive plant-use context.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native phenology labels, dates, coordinates, specimen labels, survey rows, images, model outputs, and notes remain source-bound. |
| WORK / QUARANTINE | Candidate records are normalized, taxon-crosswalked, source-role checked, rights checked, sensitivity-screened, date-precision evaluated, deduplicated, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, normalized phase, source/version support, spatial/temporal support, sensitivity state, evidence links, and correction posture. |
| CATALOG / TRIPLET | Phenology claims may be cataloged or projected only with evidence, source role, time precision, spatial scale, uncertainty, and caveats preserved. |
| RELEASE CANDIDATE | Public phenology derivatives require validation report, policy decision, review record, redaction/delay/suppression receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only public-safe derivatives appear in public API/UI/map/time-series layers after release. |
| CORRECTION | Taxon correction, phase correction, date correction, source withdrawal, sensitivity update, model supersession, or stale-state change triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/phenology_observation.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for observed flowering, observed leaf-out, observed fruiting, observed senescence, specimen-derived flowering, survey snapshot, aggregate month summary, modeled bloom window, and public-safe generalized derivative.
- [ ] Add invalid fixtures for missing source role, missing taxon support, missing date precision, modeled-as-observed label, aggregate-as-exact overclaim, candidate-as-public-fact, exact rare-plant bloom location in public payload, missing redaction receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, taxon crosswalk, phenophase vocabulary, source role, observed time/date precision, spatial support scale, evidence refs, sensitivity state, policy decision, redaction receipt linkage, release linkage, and correction lineage.
- [ ] Add policy tests for sensitive timing/location, rare-plant release, source-restricted records, candidate rows, modeled outputs, and management-advice prevention.
- [ ] Add no-network fixtures so CI can validate this contract without live source access.
- [ ] Add non-regression tests for taxonomy correction, date correction, phase-vocabulary update, source withdrawal, model supersession, and sensitive timing leak.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, policy allows, review passes, release exists | `ANSWER` / public-safe phenology claim allowed |
| Evidence missing, time precision insufficient, source role ambiguous, taxon unresolved | `ABSTAIN` |
| Sensitive timing/location exposure, direct RAW/WORK/QUARANTINE access, rights denial, unsafe recommendation | `DENY` |
| Schema/validator/runtime failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Directory Rules | Confirms `contracts/` owns object meaning, `schemas/` owns machine shape, and domain-specific files live as segments inside responsibility roots. |
| Flora canonical path register | Confirms `PhenologyObservation` is a Flora object-family contract for time-series flowering, leaf-out, and senescence. |
| Flora object-family register | Confirms `PhenologyObservation` is an expected Flora object family and that field-level shape remains outside the register. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM trust posture | Confirms evidence, source role, policy, review, release, correction, and rollback must outrank generated summaries, time-series charts, or map displays. |

---

## Rollback

Phenology rollback is required when a released or review-authorized phenology record changes plant timing, public seasonal labels, survey planning context, restoration timing, map/time-series output, AI answers, or published layers.

Rollback triggers include:

- taxon correction or crosswalk supersession;
- phenophase vocabulary correction;
- date/time correction or date-precision downgrade;
- source withdrawal or rights change;
- modeled/aggregate record published as observed exact record;
- exact rare-plant timing/location exposed;
- private-land, steward, cultural, or source-restricted details exposed;
- restoration/management timing presented as advice without review;
- redaction/delay/generalization receipt is missing or invalid;
- downstream release depends on a stale or superseded record.

Rollback artifacts should include affected phenology IDs, taxon IDs, occurrence/specimen/survey IDs, source records, public derivative IDs, release IDs, layer/time-series IDs, evidence refs, policy decisions, redaction receipts, correction notices, rollback cards, replacement derivatives, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which normalized phenophase vocabulary should KFM use? | NEEDS VERIFICATION | Resolve in schema/fixtures with Flora and data stewards. |
| How should specimen-derived phenology preserve uncertainty from labels and images? | NEEDS VERIFICATION | Define specimen fixtures and validation rules. |
| Which rare-plant phenology combinations require delayed or suppressed public release? | NEEDS VERIFICATION | Define policy/sensitivity fixtures. |
| Should repeated observations form a separate time-series parent object? | PROPOSED / NEEDS VERIFICATION | Review with temporal and schema stewards. |
| How should modeled bloom windows be versioned and rolled back? | NEEDS VERIFICATION | Align with model receipt and validation report contracts. |
| Which public date granularity is safe for sensitive taxa? | NEEDS VERIFICATION | Policy + release steward decision. |

---

## Related contracts

- `plant_taxon.md` and `flora_taxon_crosswalk.md` — plant identity and taxon mapping support.
- `domain_observation.md` — source observation envelope.
- `flora_occurrence.md` — occurrence-class support.
- `occurrence_public.md` and `occurrence_restricted.md` — public-safe and restricted occurrence surfaces.
- `rare_plant_record.md` — sensitive rare/protected plant context.
- `specimen_record.md` — voucher/specimen support for derived phenology.
- `botanical_survey.md` — survey method, effort, and completeness context.
- `restoration_planting.md` — project/restoration timing context.
- `redaction_receipt.md` — public-safe timing/location transformation proof.
- `domain_validation_report.md` — validation reports for records, policy, fixtures, and releases.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any phenology layer or time-series endpoint depends on this contract.
- [ ] Add source profiles for approved phenology sources before activation.
- [ ] Add policy tests for rare-plant timing, private-land, source-restricted, candidate, modeled, aggregate, and management-advice cases.
- [ ] Confirm public API/UI/map/time-series surfaces do not expose sensitive timing/location details or turn seasonal records into unreviewed recommendations.
- [ ] Record any contract/schema/path conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
