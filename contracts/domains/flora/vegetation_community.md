<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-vegetation-community
title: Vegetation Community Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Vegetation/community steward · Spatial steward · Contract steward · Source steward · Schema steward · Sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; vegetation-community; polygonal-classification; source-role-aware; sensitivity-aware; release-gated; no-canonical-habitat-truth
tags: [kfm, contracts, flora, vegetation-community, community-classification, polygon, floristic-composition, habitat, plant-taxon, survey, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./plant_taxon.md
  - ./flora_taxon_crosswalk.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./specimen_record.md
  - ./flora_occurrence.md
  - ./occurrence_public.md
  - ./occurrence_restricted.md
  - ./rare_plant_record.md
  - ./phenology_observation.md
  - ./invasive_plant_record.md
  - ./range_polygon.md
  - ./habitat_association.md
  - ./botanical_survey.md
  - ./restoration_planting.md
  - ./redaction_receipt.md
  - ./domain_validation_report.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/vegetation_community.schema.json
  - ../../../fixtures/domains/flora/vegetation_community/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora vegetation-community semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "VegetationCommunity captures polygonal or plot/community classification, floristic composition, source scale, method, and review context; it does not replace HabitatAssociation, RangePolygon, BotanicalSurvey, or occurrence records."
  - "Community polygons can expose rare habitats, rare-plant search areas, private-land stewardship, or sensitive cultural/ecological context; public use requires evidence, rights, sensitivity, policy, review, release, correction, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Vegetation Community — Flora

> Semantic contract for Flora `VegetationCommunity`: the evidence-bound object for polygonal, plot-based, survey-derived, modeled, aggregate, or reviewed vegetation-community classification and floristic composition support.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: community classification not canonical habitat truth" src="https://img.shields.io/badge/boundary-community__not__canonical__habitat__truth-critical">
</p>

`contracts/domains/flora/vegetation_community.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Community classes](#community-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/vegetation_community.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/vegetation_community.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `VegetationCommunity` as the polygonal community-classification object. Field-level schema shape, fixtures, validators, source registry terms, policy runtime, release workflow, API behavior, UI behavior, topology checks, classification vocabulary, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `VegetationCommunity` records vegetation-community classification support at a stated scale, method, source role, and uncertainty. It does **not** prove exact species occurrence by itself, does **not** replace `HabitatAssociation`, `RangePolygon`, `BotanicalSurvey`, `FloraOccurrence`, or `PlantTaxon`, and does **not** authorize public exposure of sensitive community patches, rare habitats, private stewardship sites, or rare-plant search clues by itself.

---

## Meaning

`VegetationCommunity` is the Flora semantic object for a vegetation community, plant association, ecological community, floristic assemblage, plant-cover type, mapped community polygon, survey plot classification, modeled community, aggregate community summary, or candidate community label.

It answers:

- Which vegetation community or community-classification claim is being represented?
- Which source vocabulary, survey method, mapped polygon, plot, model, community description, or review supports the classification?
- Which plant taxa, dominant species, indicator species, composition summaries, structure notes, or condition attributes support the claim?
- What spatial support, scale, topology, temporal scope, uncertainty, and source-role posture apply?
- Does the community classification expose rare habitat, rare/protected plant context, private-land stewardship, source-restricted detail, or culturally sensitive plant knowledge?
- Which validation, policy, review, redaction, release, correction, and rollback objects govern downstream use?

A vegetation community can support map layers, Focus Mode context, restoration interpretation, habitat association, range context, and AI explanations. It remains evidence-subordinate and cannot stand in for occurrence proof, habitat truth, or release approval.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Vegetation-community meaning | `contracts/domains/flora/vegetation_community.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/vegetation_community.schema.json` | Linked only; currently scaffolded |
| Taxon identity | `plant_taxon.md`, `flora_taxon_crosswalk.md` | Dominant/indicator/composition taxon support |
| Survey support | `botanical_survey.md`, `domain_observation.md`, `specimen_record.md` | Method, plots, observations, and vouchers that may support classification |
| Occurrence support | `flora_occurrence.md`, `occurrence_public.md`, `occurrence_restricted.md` | May support composition; not replaced by community polygon |
| Sensitive flora support | `rare_plant_record.md`, `redaction_receipt.md` | Rare/sensitive plant or habitat exposure handling |
| Habitat and range context | `habitat_association.md`, `range_polygon.md` | Adjacent spatial/context claims; not collapsed into community truth |
| Invasive/restoration users | `invasive_plant_record.md`, `restoration_planting.md` | Community condition, treatment, or project context with caveats |
| Validation report | `domain_validation_report.md` | Validates topology, vocabulary, source-role, policy, fixtures, and release readiness |
| Source registry | `data/registry/sources/flora/` | Source identity, rights, cadence, attribution, access limits |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Admission/release and sensitive-context decisions |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only after governed release |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/vegetation_community.schema.json` |
| Schema title | `Vegetation Community` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/vegetation_community.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, source registry links, classification vocabulary, topology checks, sensitivity policy, public derivatives, correction flows, and rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `VegetationCommunity` should semantically assert:

1. **Community identity** — deterministic identity for the community classification record, polygon, plot, or candidate record.
2. **Classification support** — source-native community label, normalized community label, classification system, version, method, and review state.
3. **Spatial support** — polygon, multipolygon, plot, transect, grid, remote-sensing pixel, generalized public geometry, or withheld geometry.
4. **Floristic support** — dominant taxa, indicator taxa, composition summaries, cover estimates, structure notes, or source-native species lists where available.
5. **Source and role** — SourceDescriptor, source role, source record ID, source authority limits, rights, cadence, and attribution.
6. **Temporal support** — observed, mapped, modeled, source, retrieval, release, stale-state, supersession, and correction times where material.
7. **Uncertainty and scale** — support scale, mapping precision, classification confidence, topology state, method limitations, and absence caveats.
8. **Sensitivity posture** — rare habitat, rare/protected plant inference, private land, cultural plant knowledge, source-restricted field notes, or public-safe state.
9. **Derived-use posture** — habitat association, restoration, invasive, range, occurrence, public map, or AI-answer use with caveats.
10. **Governance state** — validation, policy, review, redaction, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating community polygon as exact species occurrence proof | Community classification can imply composition, but occurrence still needs occurrence/survey/specimen support. |
| Treating modeled community as observed survey truth | `modeled` source role and uncertainty must remain visible. |
| Treating desired restoration target as observed community | Restoration target and observed vegetation community are separate claims. |
| Treating habitat association as owned here | Flora may link to Habitat, but this contract does not replace the Habitat lane. |
| Publishing rare habitat patches without policy review | Community polygons can reveal rare/protected plant search areas. |
| Hiding classification vocabulary/version | Community labels are source- and version-dependent and must be auditable. |
| Simplifying/altering geometry without a receipt | Generalization, masking, clipping, dissolving, or suppression requires transform proof where release-significant. |
| Direct public access to RAW/WORK/QUARANTINE community rows | Public clients consume governed released derivatives only. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical vegetation community identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `record_class` | `mapped_polygon`, `survey_plot`, `transect_classification`, `floristic_summary`, `remote_sensing_class`, `modeled_community`, `aggregate_community`, `restoration_target`, `candidate_record`, or `synthetic`. |
| `community_label` | KFM normalized community label, when reviewed. |
| `source_community_label` | Source-native community/cover/association label retained for audit. |
| `classification_system_ref` | Source/classification system or vocabulary ref. |
| `classification_version` | Classification version, date, or source edition. |
| `classification_confidence` | Qualitative or quantitative classification confidence. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and authority limits. |
| `source_role` | Canonical source role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |
| `source_record_refs` | Source-native polygon, plot, survey, model, atlas, map, or classification records. |
| `geometry_ref` | Internal geometry reference. |
| `public_geometry_ref` | Public-safe derivative geometry reference, if released. |
| `geometry_type` | Polygon, multipolygon, plot, transect, grid, raster cell, ecoregion, county, generalized geometry, or withheld. |
| `crs` | Coordinate reference system / projection metadata. |
| `topology_state` | Valid, repaired, simplified, clipped, dissolved, masked, invalid, or NEEDS VERIFICATION. |
| `spatial_support_scale` | Plot, transect, polygon, grid, county, ecoregion, mapped unit, model cell, aggregate, or unknown. |
| `dominant_taxon_refs` | Dominant PlantTaxon refs, where supported. |
| `indicator_taxon_refs` | Indicator PlantTaxon refs, where supported. |
| `composition_summary` | Public-safe composition or cover summary. |
| `cover_method` | Source-native or normalized cover/abundance method. |
| `structure_summary` | Canopy/understory/strata/height/cover structure, if available. |
| `condition_summary` | Disturbance, quality, intactness, restoration state, invasive pressure, or source-native condition summary. |
| `botanical_survey_refs` | Survey method/effort/completeness refs, when applicable. |
| `domain_observation_refs` | Observation-envelope refs, when applicable. |
| `specimen_record_refs` | Voucher support, when applicable. |
| `flora_occurrence_refs` | Occurrence support, when applicable. |
| `habitat_association_refs` | HabitatAssociation refs, when this community informs cross-lane context. |
| `range_polygon_refs` | Range/distribution context refs, when applicable. |
| `restoration_planting_refs` | Restoration target/project refs, when applicable. |
| `observed_time` | Survey/observation/classification time, if known. |
| `effective_time` | Time range this classification supports. |
| `source_time` | Time asserted by source. |
| `retrieval_time` | Time KFM retrieved source material. |
| `release_time` | Time a public derivative was released. |
| `stale_state` | Current, historical, stale, superseded, withdrawn, model-superseded, or unknown. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Rare-habitat, rare-plant-inference, private-land, cultural, source-restricted, public-safe, or unknown posture. |
| `policy_decision_ref` | Policy result when exposure or release is material. |
| `validation_report_ref` | Validation report for topology, vocabulary, support, policy, fixtures, or release candidate. |
| `review_record_ref` | Source, vegetation, spatial, sensitivity, domain, or release review. |
| `redaction_receipt_ref` | Required when geometry, label, composition, or evidence is generalized/suppressed for public output. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, classification update, geometry correction, source withdrawal, stale-state, and rollback lineage. |
| `quality_flags` | Classification-conflict, taxon-conflict, topology-invalid, model-uncertainty, source-version-stale, rights-unknown, sensitivity-unknown, aggregate-not-exact, or incomplete-evidence flags. |

---

## Community classes

| Class | Meaning | Default posture |
|---|---|---|
| `mapped_polygon` | Source/community map polygon or mapped vegetation unit. | Requires source scale, topology, and classification caveats. |
| `survey_plot` | Plot-level community classification. | Requires method, date, effort, and plot context. |
| `transect_classification` | Transect/route-level community classification. | Requires route sensitivity and method caveats. |
| `floristic_summary` | Community described by species composition/cover summary. | Composition support only; not exact occurrence proof. |
| `remote_sensing_class` | Image/raster/model-derived vegetation class. | Must retain model/inference uncertainty. |
| `modeled_community` | Predicted or suitability-based community. | Modeled, not observed. |
| `aggregate_community` | County/grid/ecoregion/atlas/community summary. | Aggregate scale only. |
| `restoration_target` | Desired/planned target community. | Planned target, not observed community. |
| `candidate_record` | Unreviewed import or unresolved community label. | WORK/QUARANTINE only. |
| `synthetic` | Generated/hypothetical community description. | Reality-boundary disclosure; not observed fact. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | VegetationCommunity posture |
|---|---|---|
| Surveyed plot, field-mapped community, reviewed vegetation polygon | `observed` | Can support observed community claim when method, time, geometry, and evidence resolve. |
| Protected community type, conservation status, legal boundary, agency classification rule | `regulatory` | Supports status/context, not occurrence proof by itself. |
| Remote-sensing classification, suitability model, predicted community | `modeled` | Requires model identity, version, uncertainty, and caveats. |
| Atlas/community summary, county rollup, literature vegetation region | `aggregate` | Aggregate context only. |
| Management unit, restoration target, administrative map, project area | `administrative` | Supports management/project context, not biological community truth by itself. |
| Unreviewed import, unresolved source polygon, watcher row | `candidate` | Hold in WORK/QUARANTINE until reviewed. |
| AI-generated or hypothetical community description | `synthetic` | Must not be treated as observed community. |

Source role must survive public projection. A modeled, aggregate, or administrative community cannot be worded into observed field truth.

---

## Sensitivity and release

Vegetation-community records can expose sensitive ecological information even when they do not include exact plant occurrences. Small polygons, high-quality habitat labels, rare community types, species composition, and overlays with range or rare-plant records can reveal search areas.

Rules:

- Public outputs must not expose exact rare-habitat, rare-plant inference, private-land stewardship, culturally sensitive plant context, or source-restricted field notes without policy/review approval.
- Public derivatives should generalize geometry, suppress sensitive labels, aggregate composition, delay release, or withhold records when exposure risk is material.
- Public payloads must preserve source role, classification vocabulary/version, spatial support scale, topology state, uncertainty, temporal scope, and caveats.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, source-restricted, stale, or evidence-incomplete records must not enter public outputs as authoritative community facts.
- Community records must not be used as management/restoration recommendations without reviewed policy and domain expertise.
- Public evidence/citation projections must avoid leaking restricted plots, exact rare-plant context, private source records, or steward notes.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native polygons, rasters, plot rows, species lists, cover data, classification labels, and notes remain source-bound. |
| WORK / QUARANTINE | Candidate records are normalized, classification-mapped, taxon-crosswalked, topology-checked, source-role checked, rights checked, sensitivity-screened, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, community label, classification source/version, geometry support, spatial/temporal support, evidence links, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Community claims may be cataloged or projected only with evidence, source role, classification vocabulary, scale, uncertainty, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy decision, review record, redaction receipt when transformed, release manifest, and rollback target. |
| PUBLISHED | Only public-safe community layers, summaries, or API/UI payloads appear after governed release. |
| CORRECTION | Classification update, geometry repair, source withdrawal, model supersession, taxon correction, sensitivity update, topology issue, or stale-state change triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/vegetation_community.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for mapped polygon, survey plot, transect classification, floristic summary, remote-sensing class, modeled community, aggregate community, restoration target, sensitive community, and public-safe derivative.
- [ ] Add invalid fixtures for missing source role, missing classification label/source, invalid topology, modeled community labeled observed, restoration target treated as observed community, community polygon treated as occurrence proof, sensitive habitat public release without policy, missing redaction receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, classification system/version, source role, geometry ref, CRS/topology state, spatial support scale, taxon/composition refs, temporal support, evidence refs, sensitivity state, policy decision, release linkage, and correction lineage.
- [ ] Add policy tests for rare habitat exposure, rare-plant inference, private-land stewardship, source-restricted field notes, model uncertainty, and public map filtering.
- [ ] Add no-network fixtures so CI can validate this contract without live source access.
- [ ] Add non-regression tests for classification vocabulary update, topology repair, model supersession, source withdrawal, redaction bug, and rollback of released derivatives.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, topology validates, policy allows, review passes, release exists | `ANSWER` / public-safe community claim allowed |
| Evidence missing, topology invalid, source role ambiguous, classification unresolved, uncertainty too high | `ABSTAIN` |
| Sensitive community exposure, direct RAW/WORK/QUARANTINE access, rights denial, restricted evidence leak | `DENY` |
| Schema/validator/runtime/spatial-processing failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Directory Rules / canonical path register | Confirms `contracts/` owns object meaning, schemas own machine shape, and `VegetationCommunity` is the Flora object-family contract for polygonal community classification. |
| Flora object-family register | Confirms `VegetationCommunity` is an expected Flora object family and that field-level shape remains outside the register. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM trust posture | Confirms evidence, source role, policy, review, release, correction, and rollback must outrank generated summaries, map layers, models, or community labels. |

---

## Rollback

Vegetation-community rollback is required when a released or review-authorized community claim weakens source integrity, leaks sensitive ecological context, misstates classification, violates rights, misrepresents source role, or depends on superseded spatial/classification evidence.

Rollback triggers include:

- classification vocabulary correction or source-version supersession;
- topology error, geometry repair, projection issue, simplification bug, or clipping mistake;
- modeled/aggregate/administrative community published as observed field truth;
- restoration target published as observed community;
- community polygon used as species occurrence proof;
- rare habitat, rare-plant inference, private-land, cultural, or steward-only detail exposed;
- source withdrawal, changed source terms, or rights denial;
- redaction/generalization receipt is missing or invalid;
- downstream release depends on stale, superseded, or invalid community geometry.

Rollback artifacts should include affected VegetationCommunity IDs, source records, classification system/version refs, geometry refs, taxon/composition refs, occurrence/survey/habitat/range/restoration refs, public derivative IDs, release IDs, layer/API/UI IDs, evidence refs, policy decisions, redaction receipts, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which vegetation classification vocabulary should be canonical for KFM public labels? | NEEDS VERIFICATION | Resolve with Flora, Habitat, schema, and source stewards. |
| Should community composition live inside this object or in linked observation/survey composition objects? | PROPOSED / NEEDS VERIFICATION | Schema fixtures across BotanicalSurvey, DomainObservation, and VegetationCommunity. |
| What topology and minimum mapping-unit checks are required before public release? | NEEDS VERIFICATION | Spatial validator and fixture design. |
| Which community labels or polygons are sensitive enough to require suppression/generalization? | NEEDS VERIFICATION | Sensitivity policy and redaction fixtures. |
| How should modeled/remote-sensing communities be labeled in public UI? | NEEDS VERIFICATION | API/UI projection rules and model receipt alignment. |
| How should vegetation communities cross-lane into Habitat without creating parallel authority? | NEEDS VERIFICATION | HabitatAssociation and lane-boundary review. |

---

## Related contracts

- `plant_taxon.md` and `flora_taxon_crosswalk.md` — plant identity and composition taxon support.
- `domain_observation.md` and `botanical_survey.md` — observations, surveys, plots, and method support.
- `specimen_record.md` — voucher support for floristic composition or determinations.
- `flora_occurrence.md`, `occurrence_public.md`, and `occurrence_restricted.md` — occurrence surfaces that may support composition but remain separate.
- `rare_plant_record.md` — rare/protected plant context that can constrain community release.
- `habitat_association.md` — cross-lane relationship to Habitat; this contract does not replace Habitat truth.
- `range_polygon.md` — range/distribution context that may be informed by community support.
- `restoration_planting.md` — target/restored community context, distinct from observed community.
- `redaction_receipt.md` — public-safe geometry/label/composition transformation proof.
- `domain_validation_report.md` — validation reports for topology, vocabulary, policy, fixtures, and releases.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any vegetation community layer depends on this contract.
- [ ] Add source profiles for approved vegetation/community classification sources before activation.
- [ ] Add policy tests for rare habitat exposure, rare-plant inference, private-land stewardship, source-restricted notes, and public map filtering.
- [ ] Confirm public API/UI/map/AI surfaces label observed, modeled, aggregate, administrative, candidate, synthetic, and restoration-target community records clearly.
- [ ] Confirm every public derivative has release manifest, redaction receipt when transformed, correction path, and rollback target.
- [ ] Record any contract/schema/path/classification/source-role conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
