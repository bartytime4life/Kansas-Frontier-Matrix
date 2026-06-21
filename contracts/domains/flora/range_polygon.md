<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-range-polygon
title: Range Polygon Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Range/distribution steward · Spatial steward · Contract steward · Source steward · Schema steward · Sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; range-polygon; distribution; modeled-or-compiled; source-role-aware; sensitivity-aware; release-gated; no-occurrence-proof
tags: [kfm, contracts, flora, range-polygon, distribution, species-range, modeled-range, compiled-range, plant-taxon, occurrence, evidence, source-role, spatial-support, sensitivity, policy, release, correction, rollback]
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
  - ./phenology_observation.md
  - ./vegetation_community.md
  - ./invasive_plant_record.md
  - ./habitat_association.md
  - ./botanical_survey.md
  - ./restoration_planting.md
  - ./redaction_receipt.md
  - ./domain_validation_report.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/range_polygon.schema.json
  - ../../../fixtures/domains/flora/range_polygon/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora range/distribution semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "RangePolygon captures modeled, compiled, aggregate, administrative, or reviewed distribution support; it does not prove exact occurrence and does not replace OccurrencePublic, OccurrenceRestricted, FloraOccurrence, or HabitatAssociation."
  - "Range polygons can amplify sensitive species exposure when joined with taxa, habitat, or rare-plant records; public use requires evidence, policy, review, redaction/generalization where needed, release, correction, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Range Polygon — Flora

> Semantic contract for Flora `RangePolygon`: the evidence-bound spatial object for plant range, distribution, modeled suitability, compiled extent, administrative distribution, aggregate support, and released public-safe range layers.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: range not occurrence proof" src="https://img.shields.io/badge/boundary-range__not__occurrence__proof-critical">
</p>

`contracts/domains/flora/range_polygon.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Range classes](#range-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/range_polygon.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/range_polygon.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `RangePolygon` as a modeled or compiled range/distribution polygon. Field-level schema shape, fixtures, validators, source registry terms, policy runtime, release workflow, API behavior, UI behavior, spatial topology checks, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `RangePolygon` records range or distribution support at a stated scale and source-role posture. It does **not** prove current exact occurrence, does **not** replace `FloraOccurrence`, `OccurrencePublic`, `OccurrenceRestricted`, `RarePlantRecord`, or `HabitatAssociation`, and does **not** authorize public release of sensitive taxa, precise habitat clues, or derived map layers by itself.

---

## Meaning

`RangePolygon` is the Flora semantic object for a bounded spatial representation of where a plant taxon, source taxon, vegetation subject, invasive plant, rare plant, restoration species, or modeled/candidate subject is believed, compiled, modeled, administratively listed, or reviewed to occur or potentially occur.

It answers:

- Which plant subject does the polygon describe?
- Is the polygon observed-supported, compiled, modeled, regulatory, aggregate, administrative, candidate, or synthetic?
- What geometry, support scale, uncertainty, source version, temporal scope, and caveats apply?
- Which source records, occurrences, specimens, surveys, models, habitat associations, or status lists support the range?
- Does the polygon expose rare/protected plant range, private-land context, sensitive habitat association, or source-restricted detail?
- Which validation, policy, review, redaction, release, correction, and rollback objects govern downstream use?

A range polygon is a spatial claim carrier. It may be useful for map layers, search filters, Focus Mode context, habitat association, restoration planning, invasive-risk context, and AI explanations, but it remains evidence-subordinate and source-role-bound.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Range/distribution meaning | `contracts/domains/flora/range_polygon.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/range_polygon.schema.json` | Linked only; currently scaffolded |
| Taxon identity | `plant_taxon.md`, `flora_taxon_crosswalk.md` | Defines plant subject and public labels/caveats |
| Occurrence support | `flora_occurrence.md`, `occurrence_public.md`, `occurrence_restricted.md` | May support range; not replaced by range |
| Rare/protected support | `rare_plant_record.md` | Can force generalized/suppressed release posture |
| Survey/specimen support | `botanical_survey.md`, `specimen_record.md`, `domain_observation.md` | Evidence and source-observation context |
| Habitat/context support | `habitat_association.md`, `vegetation_community.md` | Contextual support; not collapsed into range truth |
| Invasive/restoration users | `invasive_plant_record.md`, `restoration_planting.md` | Downstream or adjacent uses with caveats |
| Redaction proof | `redaction_receipt.md` | Required when geometry is generalized, suppressed, delayed, or transformed |
| Validation report | `domain_validation_report.md` | Validates polygon topology, support, policy, and release readiness |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Admission/release and sensitive-context decisions |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only after governed release |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/range_polygon.schema.json` |
| Schema title | `Range Polygon` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/range_polygon.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, spatial topology checks, source-role handling, policy checks, public range layers, correction flows, and rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `RangePolygon` should semantically assert:

1. **Polygon identity** — deterministic identity for the range/distribution polygon or candidate polygon.
2. **Plant subject** — PlantTaxon, source taxon, invasive plant subject, rare-plant subject, vegetation subject, restoration species, or candidate subject.
3. **Range class** — observed-supported, compiled, modeled, regulatory, administrative, aggregate, candidate, synthetic, public derivative, or historical range.
4. **Geometry support** — polygon geometry, geometry source, precision, topology posture, CRS/projection, simplification, and public-safe derivative state where applicable.
5. **Evidence support** — source records, observations, specimens, surveys, models, atlases, literature, or review records sufficient for cite-or-abstain behavior.
6. **Source-role posture** — observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic support preserved without silent upgrade.
7. **Temporal support** — effective, observed, modeled, source, retrieval, release, stale-state, supersession, and correction times where material.
8. **Uncertainty and scale** — confidence, resolution, support scale, absence limitations, model uncertainty, and aggregate caveats.
9. **Sensitivity posture** — rare/protected species, exact sensitive edges, private-land inference, habitat exposure, source restrictions, or public-safe state.
10. **Governance state** — validation, policy, review, redaction, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating range as occurrence proof | Range/distribution support does not prove current exact presence at a point. |
| Treating modeled range as observed range | `modeled` source role and uncertainty must remain visible. |
| Treating administrative/state lists as biological distribution | Administrative scope is not occurrence proof. |
| Publishing sensitive rare-plant range detail without review | Range polygons can expose search areas or habitat clues. |
| Hiding source scale and age | Historical/stale/aggregate ranges require date and scale caveats. |
| Replacing habitat or vegetation contracts | Range can reference habitat/community support but does not own those meanings. |
| Direct public use of RAW/WORK/QUARANTINE polygons | Public clients consume governed released derivatives only. |
| Simplifying geometry without a receipt | Generalization, simplification, clipping, binning, or suppression needs transform proof. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical range polygon identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `range_class` | `observed_supported`, `compiled_range`, `modeled_range`, `regulatory_range`, `administrative_extent`, `aggregate_distribution`, `historical_range`, `candidate_range`, `synthetic_range`, or `public_derivative`. |
| `flora_subject_type` | `plant_taxon`, `source_taxon`, `rare_plant_record`, `invasive_plant_record`, `vegetation_community`, `restoration_species`, or candidate. |
| `flora_subject_ref` | Flora subject reference. |
| `taxon_ref` | KFM PlantTaxon or reviewed candidate. |
| `taxon_crosswalk_ref` | Taxon-crosswalk support. |
| `source_taxon_name` | Source-native taxon name retained for audit. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and authority limits. |
| `source_role` | Canonical source role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |
| `source_record_refs` | Source-native range, atlas, occurrence, specimen, survey, model, or status records. |
| `support_refs` | Occurrence, specimen, survey, habitat, community, model, or review support refs. |
| `geometry_ref` | Canonical internal polygon geometry reference. |
| `public_geometry_ref` | Public-safe derivative geometry reference, when released. |
| `geometry_type` | Polygon, multipolygon, grid, hexbin, county set, ecoregion, range cell, masked polygon, or suppressed geometry. |
| `crs` | Coordinate reference system / projection metadata. |
| `geometry_precision` | Exact source polygon, compiled coarse, generalized, modeled grid, county, ecoregion, public-safe, or unknown precision. |
| `spatial_support_scale` | Exact polygon, grid, county, ecoregion, statewide, watershed, habitat patch, literature-general, or unknown. |
| `topology_state` | Valid, repaired, simplified, clipped, dissolved, unioned, masked, invalid, or NEEDS VERIFICATION. |
| `range_confidence` | Qualitative or quantitative confidence where supported. |
| `uncertainty_summary` | Source/model/geometry uncertainty and limitations. |
| `absence_caveat` | Statement that absence outside the polygon is or is not supported. |
| `effective_time` | Time range the range claim supports. |
| `source_time` | Time asserted by source. |
| `retrieval_time` | Time KFM retrieved source material. |
| `release_time` | Time a public-safe derivative was released. |
| `stale_state` | Current, historical, stale, superseded, withdrawn, model-superseded, or unknown. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, and access posture. |
| `sensitivity_state` | Rare-plant, exact-sensitive, private-land inference, habitat-sensitive, cultural, source-restricted, public-safe, or unknown. |
| `policy_decision_ref` | Policy result when exposure or release is material. |
| `validation_report_ref` | Validation report for topology, support, policy, fixtures, or release candidate. |
| `review_record_ref` | Source, taxon, spatial, sensitivity, domain, or release review. |
| `redaction_receipt_ref` | Required if geometry was generalized, simplified, clipped, masked, suppressed, or delayed for public output. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, supersession, withdrawal, stale-state, model supersession, and rollback lineage. |
| `quality_flags` | Taxon-conflict, stale-source, model-uncertainty, topology-invalid, rights-unknown, sensitivity-unknown, aggregate-not-exact, modeled-not-observed, or incomplete-evidence flags. |

---

## Range classes

| Class | Meaning | Default posture |
|---|---|---|
| `observed_supported` | Polygon compiled from reviewed occurrences/specimens/surveys. | Stronger support, but still not exact occurrence proof. |
| `compiled_range` | Range digitized or compiled from atlas, literature, agency, or source polygon. | Preserve source scale and date. |
| `modeled_range` | Species distribution/suitability/prediction model output. | Must remain modeled with uncertainty and version. |
| `regulatory_range` | Legal/status/recovery/program boundary. | Regulatory context, not biological occurrence proof. |
| `administrative_extent` | County/program/management extent. | Administrative scope only. |
| `aggregate_distribution` | County/grid/portal/literature summary polygon. | Aggregate scale only. |
| `historical_range` | Historical distribution or prior extent. | Requires date/stale caveat. |
| `candidate_range` | Unreviewed import or provisional polygon. | WORK/QUARANTINE until reviewed. |
| `synthetic_range` | Generated/reconstructed/hypothetical polygon. | Reality-boundary disclosure; not observed fact. |
| `public_derivative` | Released public-safe range geometry. | Requires release, caveats, and rollback target. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | Range posture |
|---|---|---|
| Range compiled from reviewed occurrences, specimens, surveys, or steward review | `observed` | Can support observed-backed range when evidence and scale are clear. |
| Rare/protected recovery map, legal boundary, status-list extent | `regulatory` | Supports policy/status context, not occurrence proof. |
| Species distribution model, habitat suitability model, climate projection, risk model | `modeled` | Requires model identity, version, uncertainty, and caveats. |
| Atlas, checklist, county grid, portal rollup, literature summary | `aggregate` | Supports aggregate distribution only. |
| Management area, administrative program boundary, project extent | `administrative` | Supports management scope, not biological range by itself. |
| Unreviewed import, watcher result, unresolved digitized polygon | `candidate` | Hold in WORK/QUARANTINE until reviewed. |
| AI-generated or reconstructed polygon | `synthetic` | Requires reality-boundary disclosure; never observed fact by itself. |

---

## Sensitivity and release

Range polygons can create sensitive inferences even when they are not exact occurrence points. A range edge, small polygon, habitat overlay, taxon label, or rare-plant association can expose likely search areas or steward-controlled knowledge.

Rules:

- Rare/protected plant ranges are deny-by-default when geometry is precise enough to guide collection, disturbance, or location inference.
- Public range layers must preserve source role, scale, uncertainty, date, and absence limitations.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, source-restricted, stale, or evidence-incomplete polygons must not enter public outputs as authoritative current ranges.
- Public evidence/citation projections must not leak restricted occurrence, exact rare-plant geometry, private-land context, or steward notes.
- Generalization, simplification, clipping, dissolving, binning, masking, or suppression must be traceable through a `RedactionReceipt` or transform receipt where release consequences matter.
- Range polygons must not be used as restoration or management recommendations without reviewed policy and operations context.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native polygons, model outputs, range tables, atlas grids, occurrence-derived geometries, and notes remain source-bound. |
| WORK / QUARANTINE | Candidate polygons are normalized, taxon-crosswalked, source-role checked, rights checked, topology-screened, sensitivity-screened, and evidence-linked. |
| PROCESSED | Reviewed polygons receive deterministic identity, taxon support, geometry support, topology state, source/version support, spatial/temporal support, sensitivity state, evidence links, and correction posture. |
| CATALOG / TRIPLET | Range claims may be cataloged or projected only with evidence, source role, geometry scale, temporal scope, uncertainty, and caveats preserved. |
| RELEASE CANDIDATE | Public range derivatives require validation report, policy decision, review record, transform/redaction receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only public-safe range layers or API/UI payloads appear after governed release. |
| CORRECTION | Taxon correction, geometry repair, source withdrawal, source-version update, model supersession, sensitivity update, topology issue, or stale-state change triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/range_polygon.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for observed-supported range, compiled atlas range, modeled distribution, regulatory extent, aggregate county/grid range, historical range, candidate range, and public-safe derivative.
- [ ] Add invalid fixtures for missing source role, missing taxon support, invalid geometry/topology, modeled range labeled observed, aggregate range labeled exact, regulatory boundary used as biological occurrence proof, exact rare-plant range public release, missing transform receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, taxon crosswalk, range class, source role, geometry ref, CRS, topology state, spatial support scale, temporal support, evidence refs, sensitivity state, policy decision, redaction receipt linkage, release linkage, and correction lineage.
- [ ] Add policy tests for sensitive range exposure, source-restricted polygons, stale/historical ranges, model uncertainty, and public map filter behavior.
- [ ] Add no-network fixtures so CI can validate this contract without live source access.
- [ ] Add non-regression tests for taxon split/merge, topology repair, model supersession, source withdrawal, range generalization bug, and sensitive geometry leak.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, topology validates, policy allows, review passes, release exists | `ANSWER` / public-safe range claim allowed |
| Evidence missing, topology invalid, source role ambiguous, taxon unresolved, uncertainty too high | `ABSTAIN` |
| Sensitive geometry exposure, direct RAW/WORK/QUARANTINE access, rights denial, restricted evidence leak | `DENY` |
| Schema/validator/runtime/spatial-processing failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Directory Rules | Confirms `contracts/` owns object meaning, `schemas/` owns machine shape, and domain-specific files live as segments inside responsibility roots. |
| Flora canonical path register | Confirms `RangePolygon` is a Flora object-family contract for modeled or compiled range/distribution polygons. |
| Flora object-family register | Confirms `RangePolygon` is an expected Flora object family and that field-level shape remains outside the register. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM trust posture | Confirms evidence, source role, policy, review, release, correction, and rollback must outrank generated summaries, map layers, or spatial projections. |

---

## Rollback

Range-polygon rollback is required when a released or review-authorized polygon changes taxon distribution, public map labels, search filters, habitat associations, rare-plant exposure, invasive-risk context, restoration planning, AI answers, or published layers.

Rollback triggers include:

- taxon correction or crosswalk supersession;
- source polygon withdrawal or source-rights change;
- model version supersession;
- stale/historical range published as current;
- topology error, geometry repair, projection issue, or simplification bug;
- modeled/aggregate/regulatory polygon published as observed exact distribution;
- exact or inferable rare-plant range exposure;
- private-land, steward, cultural, habitat-sensitive, or source-restricted detail exposed;
- redaction/generalization receipt is missing or invalid;
- downstream release depends on a superseded polygon.

Rollback artifacts should include affected range polygon IDs, taxon IDs, crosswalk IDs, occurrence/specimen/survey/model/support refs, public derivative IDs, release IDs, layer IDs, evidence refs, policy decisions, redaction receipts, correction notices, rollback cards, replacement polygons, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which range classes should be exposed as public map layers by default? | NEEDS VERIFICATION | Resolve in policy and release fixtures. |
| What topology requirements should be mandatory before promotion? | NEEDS VERIFICATION | Define schema/validator rules for valid, repaired, simplified, clipped, and dissolved geometries. |
| How should modeled suitability polygons differ from range polygons in schema and UI labels? | NEEDS VERIFICATION | Align with model receipt, habitat association, and validation-report contracts. |
| Which generalization thresholds are safe for rare/protected taxa? | NEEDS VERIFICATION | Define in sensitivity policy and redaction fixtures. |
| Should absence outside a range polygon ever be asserted? | PROPOSED / NEEDS VERIFICATION | Requires source-specific and model-specific support rules. |
| How should historical range be versioned and displayed without implying current presence? | NEEDS VERIFICATION | Add stale-state and public-label fixtures. |

---

## Related contracts

- `plant_taxon.md` and `flora_taxon_crosswalk.md` — plant identity and taxon mapping support.
- `flora_occurrence.md` — occurrence-class support that may inform range but is not replaced by range.
- `occurrence_public.md` and `occurrence_restricted.md` — public-safe and restricted occurrence surfaces.
- `rare_plant_record.md` — sensitive rare/protected plant context that can constrain range release.
- `specimen_record.md` and `botanical_survey.md` — voucher and survey support for compiled ranges.
- `habitat_association.md` and `vegetation_community.md` — contextual spatial support, not collapsed into range truth.
- `invasive_plant_record.md` — invasive distribution and risk context.
- `redaction_receipt.md` — public-safe geometry transformation proof.
- `domain_validation_report.md` — validation reports for topology, policy, fixtures, and releases.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add spatial fixtures and validator coverage before any range layer depends on this contract.
- [ ] Add source profiles for approved range/distribution sources before activation.
- [ ] Add policy tests for rare-plant range, source-restricted geometry, stale ranges, modeled ranges, aggregate ranges, and public map filters.
- [ ] Confirm public API/UI/map surfaces label modeled, aggregate, historical, candidate, and synthetic ranges clearly.
- [ ] Confirm public range layers have release manifest, transform/redaction receipt where needed, and rollback target.
- [ ] Record any contract/schema/path/source-role conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
