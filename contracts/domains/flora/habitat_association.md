<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-habitat-association
title: Habitat Association Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Habitat steward · Association steward · Contract steward · Source steward · Schema steward · Sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; habitat-association; cross-lane; evidence-bound; source-role-aware; sensitivity-aware; no-publication-authority
tags: [kfm, contracts, flora, habitat-association, habitat, plant-taxon, flora-occurrence, rare-plant, vegetation-community, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./plant_taxon.md
  - ./flora_taxon_crosswalk.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./flora_occurrence.md
  - ./rare_plant_record.md
  - ./vegetation_community.md
  - ./range_polygon.md
  - ./botanical_survey.md
  - ./restoration_planting.md
  - ./redaction_receipt.md
  - ./domain_validation_report.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/habitat_association.schema.json
  - ../../../fixtures/domains/flora/habitat_association/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora habitat-association semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "HabitatAssociation is a cross-lane link owned by Flora when the claim is about a plant/taxon/community association with habitat; it does not replace the Habitat domain's HabitatPatch, EcologicalSystem, quality, suitability, or connectivity records."
  - "Rare-plant habitat association can amplify sensitive-location risk and remains fail-closed unless evidence, policy, review, redaction, release, and rollback support all resolve."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Association — Flora

> Semantic contract for Flora `HabitatAssociation`: the evidence-bound, cross-lane relationship between a plant taxon, occurrence, rare-plant record, vegetation community, range, survey, or restoration record and a habitat, ecological system, land-cover, site condition, or suitability context.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: association not habitat ownership" src="https://img.shields.io/badge/boundary-association__not__habitat__ownership-critical">
</p>

`contracts/domains/flora/habitat_association.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Association types](#association-types) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/habitat_association.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/habitat_association.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `HabitatAssociation` as a cross-lane object to Habitat that Flora owns as an association object. Field-level schema shape, fixtures, validators, source registry terms, policy runtime, release workflow, API behavior, UI behavior, habitat-domain counterpart contracts, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `HabitatAssociation` records the meaning and support for a plant ↔ habitat relationship. It does **not** create Habitat-domain canonical truth, does **not** prove a plant occurrence by itself, does **not** publish sensitive habitat for rare plants, and does **not** substitute for EvidenceBundle, PolicyDecision, ReviewRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, or RollbackCard.

---

## Meaning

`HabitatAssociation` is the Flora semantic object for a bounded relationship between a Flora subject and a habitat context.

The Flora subject may be:

- `PlantTaxon`;
- `FloraOccurrence`;
- `RarePlantRecord`;
- `VegetationCommunity`;
- `RangePolygon`;
- `BotanicalSurvey`;
- `RestorationPlanting`;
- a reviewed taxon candidate or occurrence candidate with clear caveats.

The habitat context may be a Habitat-domain object, ecological-system label, land-cover class, vegetation structure, soil/moisture condition, hydrologic context, slope/aspect class, restoration site condition, modeled suitability surface, or source-native habitat description.

It answers:

- Which plant or plant-community subject is associated with which habitat context?
- Is the relationship observed, inferred, modeled, regulatory, aggregate, candidate, or synthetic?
- What evidence, source role, time period, spatial support, taxonomic support, and caveats apply?
- Does the association expose sensitive rare-plant habitat, private-land context, or steward-controlled knowledge?
- Can the relationship be used for public maps, search filters, suitability analysis, restoration planning, or AI explanation?
- Which review, policy, release, correction, and rollback objects must resolve before publication?

An association can support interpretation. It is not, by itself, habitat ownership, occurrence proof, suitability proof, or publication approval.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Association meaning | `contracts/domains/flora/habitat_association.md` | Owned here as the Flora-side association contract |
| Machine schema shape | `schemas/contracts/v1/domains/flora/habitat_association.schema.json` | Linked only; currently scaffolded |
| Taxon identity | `contracts/domains/flora/plant_taxon.md`, `flora_taxon_crosswalk.md` | Plant-side identity support |
| Occurrence support | `contracts/domains/flora/flora_occurrence.md`, `rare_plant_record.md` | Plant presence/sensitivity context; not replaced |
| Community support | `contracts/domains/flora/vegetation_community.md` | Community/polygon subject context |
| Range/suitability support | `contracts/domains/flora/range_polygon.md` | Distribution context; not replaced |
| Survey/restoration support | `botanical_survey.md`, `restoration_planting.md` | Method, effort, project, and monitoring context |
| Habitat-domain truth | `contracts/domains/habitat/` | HabitatPatch/EcologicalSystem/etc. remain Habitat-owned; path NEEDS VERIFICATION |
| Source registry | `data/registry/sources/flora/` | Source identity, role, rights, cadence, and attribution |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Admission/release decisions and sensitive association controls |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/habitat_association.schema.json` |
| Schema title | `Habitat Association` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/habitat_association.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, policy checks, cross-lane references, public-safe derivatives, release review, and correction/rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `HabitatAssociation` should semantically assert:

1. **Association identity** — a deterministic relationship identity, not just a note field.
2. **Flora subject** — the plant taxon, occurrence, rare-plant record, vegetation community, range, survey, or restoration record involved.
3. **Habitat target** — the habitat object, ecological system, land-cover class, habitat descriptor, site condition, or modeled suitability context involved.
4. **Relationship type** — observed occupancy, habitat preference, host/substrate relation, community membership, restoration suitability, modeled suitability, regulatory habitat, aggregate association, candidate relation, or synthetic relation.
5. **Evidence support** — EvidenceRef/EvidenceBundle links sufficient for cite-or-abstain behavior.
6. **Source-role posture** — whether the association came from observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic source context.
7. **Spatial support** — geometry, range, patch, polygon, grid, county, site, route, transect, or generalized support scale.
8. **Temporal support** — observed, valid, source, retrieval, release, correction, and stale-state support.
9. **Sensitivity posture** — whether the association reveals rare-plant habitat, steward-controlled knowledge, private-land context, cultural plant knowledge, or source-restricted information.
10. **Governance state** — validation, policy, review, redaction, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating association as occurrence proof | Habitat relation does not prove presence without occurrence/specimen/survey evidence. |
| Treating association as Habitat-domain ownership | Flora owns the association object; Habitat owns habitat patches, systems, quality, suitability, and connectivity truth. |
| Publishing rare-plant habitat clues | Exact or overly specific association can expose sensitive plant locations and must fail closed. |
| Treating modeled suitability as observed habitat use | `modeled` source role and uncertainty must remain visible. |
| Treating broad literature as site-specific evidence | Literature associations require support scale and caveats; they do not prove local occupancy. |
| Ignoring time | Historical habitat association may not support current occurrence or restoration planning. |
| Collapsing habitat, soil, hydrology, and land-cover authority | Cross-lane references must preserve owning domains and source roles. |
| Using association as release approval | Review, policy, redaction, release manifest, and rollback objects remain separate. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical association identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `flora_subject_type` | `plant_taxon`, `flora_occurrence`, `rare_plant_record`, `vegetation_community`, `range_polygon`, `botanical_survey`, `restoration_planting`, or candidate. |
| `flora_subject_ref` | Flora object reference. |
| `habitat_target_type` | `habitat_patch`, `ecological_system`, `land_cover_class`, `site_condition`, `soil_context`, `hydrologic_context`, `suitability_surface`, `source_habitat_text`, or candidate. |
| `habitat_target_ref` | Habitat or cross-lane object reference; may be unresolved/candidate. |
| `association_type` | Relationship category. |
| `association_strength` | Qualitative or quantitative strength where evidence supports it. |
| `association_basis` | Observation, specimen label, survey method, vegetation plot, literature, model, source list, expert review, or restoration plan basis. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and authority limits. |
| `source_role` | Canonical source role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |
| `source_record_ref` | Source-native record, plot, survey, model, or literature reference. |
| `taxon_ref` | PlantTaxon or reviewed taxon candidate, when applicable. |
| `occurrence_ref` | FloraOccurrence/RarePlantRecord/SpecimenRecord support, when applicable. |
| `spatial_support_ref` | Geometry, habitat patch, range polygon, survey area, transect, grid, county, or generalized geometry. |
| `spatial_support_scale` | Exact, patch, polygon, grid, county, ecoregion, statewide, literature-general, or unknown. |
| `temporal_support` | Observed/valid/source/retrieval/release/correction time support. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `sensitivity_state` | Sensitive habitat, rare-plant, steward, private-land, cultural, source-restricted, or public-safe posture. |
| `policy_decision_ref` | Policy result when association affects exposure or release. |
| `validation_report_ref` | Validation report for this association or release candidate. |
| `review_record_ref` | Steward, source, sensitivity, habitat, or release review record. |
| `redaction_receipt_ref` | Required when association is generalized, suppressed, binned, or transformed for public output. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, supersession, withdrawal, stale-state, and rollback lineage. |
| `quality_flags` | Evidence-gap, source-role-conflict, temporal-gap, spatial-overprecision, habitat-owner-conflict, rare-plant-risk, stale-state, or taxonomy-conflict flags. |

---

## Association types

| Type | Meaning | Default posture |
|---|---|---|
| `observed_occupancy` | Plant subject was observed in a habitat context. | Stronger when tied to occurrence/specimen/survey evidence. |
| `habitat_preference` | Source asserts the taxon tends to use or prefer the habitat. | Requires support scale and caveats. |
| `community_membership` | Plant is part of or diagnostic for a vegetation community. | Must not replace VegetationCommunity classification. |
| `rare_plant_habitat` | Association supports rare/protected plant habitat context. | Sensitive by default; public exact detail denied unless policy allows transformed output. |
| `invasive_habitat` | Association supports invasive plant spread, risk, or management context. | Public possible after evidence/source/sensitivity checks. |
| `restoration_suitability` | Association informs restoration planting or site suitability. | Requires project/source/method support and time caveats. |
| `model_suitability` | Association derived from model or suitability surface. | Must remain modeled; uncertainty required. |
| `regulatory_habitat` | Habitat relation from rule/list/permit/recovery context. | Regulatory context, not occurrence proof. |
| `aggregate_association` | Association from atlas/rollup/literature summary. | Aggregate scale only; no exact claims. |
| `candidate_association` | Unreviewed import, watcher result, or unresolved relation. | Work/quarantine only; no public authoritative use. |
| `synthetic_association` | Generated or reconstructed association. | Reality-boundary disclosure; never observed fact. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | Association posture |
|---|---|---|
| Field survey, specimen label, vegetation plot, steward-reviewed occurrence | `observed` | Can support site/polygon association when evidence, taxonomy, geometry, and time resolve. |
| Recovery plan, rare-plant status list, permit condition, agency habitat definition | `regulatory` | Supports legal/status context; not occurrence proof. |
| Suitability model, species distribution model, vegetation-index model | `modeled` | Must carry model identity, uncertainty, time, and review caveats. |
| Atlas summary, literature review, county checklist, public portal rollup | `aggregate` | Supports aggregate claims only at stated support scale. |
| Restoration project, management area table, administrative habitat category | `administrative` | Supports management context, not biological truth by itself. |
| Watcher/imported unresolved row, unreviewed community-science note | `candidate` | Hold in WORK/QUARANTINE until reviewed. |
| AI-generated habitat note, reconstructed relation, hypothetical restoration scenario | `synthetic` | Requires reality-boundary disclosure; never observed fact by itself. |

---

## Sensitivity and release

Habitat associations can amplify ecological sensitivity. A public-safe plant occurrence may become sensitive when joined with a precise habitat clue, private-land context, restoration site, or rare-plant habitat model.

Rules:

- Rare-plant habitat associations are deny-by-default when they expose exact or highly inferable location detail.
- Public outputs should generalize, suppress, aggregate, or withhold sensitive association details when exposure could reveal protected locations.
- Public labels must preserve source role, scale, uncertainty, and caveat when association support is modeled, aggregate, regulatory, candidate, or stale.
- A habitat association used for public map filters, AI answers, or restoration recommendations must resolve evidence, source rights, sensitivity, review, release, and rollback support.
- Candidate, synthetic, rights-unknown, source-restricted, and evidence-incomplete associations must not enter public outputs as authoritative statements.
- Cross-domain joins must not leak Habitat-domain restricted fields through Flora public payloads.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native habitat notes, plot records, survey context, specimen labels, model outputs, or literature associations remain source-bound. |
| WORK / QUARANTINE | Candidate associations are normalized, source-role checked, taxon-linked, habitat-linked, evidence-linked, sensitivity-screened, and reviewed. Risky joins remain quarantined. |
| PROCESSED | Reviewed associations receive deterministic identity, relationship type, source/version support, evidence links, spatial/temporal support, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Association triples may be generated only with evidence, source role, time, scale, caveats, and sensitivity posture preserved. |
| PUBLISHED | Only public-safe association summaries or generalized derivatives may appear in public API/UI/map layers after policy/review/release gates. |
| CORRECTION | Taxon change, habitat classification update, source withdrawal, model supersession, sensitivity update, or release issue triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/habitat_association.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for observed occupancy, rare-plant restricted association, public-safe generalized association, model suitability association, aggregate association, restoration suitability association, and rejected candidate association.
- [ ] Add invalid fixtures for missing Flora subject, missing habitat target, unresolved evidence, unsupported exact public rare-plant habitat, modeled-as-observed mislabeling, aggregate-as-exact overclaim, stale habitat classification, missing source role, missing redaction receipt, and missing rollback target.
- [ ] Add validator checks for deterministic identity, source role, Flora subject refs, Habitat target refs, evidence refs, relationship type, spatial support scale, temporal support, sensitivity flags, redaction receipt linkage, release linkage, and correction lineage.
- [ ] Add policy tests proving sensitive association joins fail closed.
- [ ] Add cross-lane tests proving Flora association payloads do not become Habitat-domain canonical truth.
- [ ] Add no-network fixtures so CI can validate the contract without live source access.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, policy allows, review passes, release exists | `ANSWER` / public-safe association allowed |
| Evidence missing, temporal support insufficient, source role ambiguous, habitat target unresolved | `ABSTAIN` |
| Sensitive association exposure, direct RAW/WORK/QUARANTINE access, rights denial | `DENY` |
| Schema/validator/runtime failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Directory Rules | Confirms `contracts/` owns object meaning, `schemas/` owns machine shape, and domain-specific files live as segments inside responsibility roots. |
| Flora canonical path register | Confirms `HabitatAssociation` is the Flora-owned association object and is cross-lane to Habitat. |
| Flora object-family register | Confirms `HabitatAssociation` is an expected Flora object family and that field-level shape remains outside the register. |
| Flora doctrine | Confirms Flora owns habitat associations while linking to habitat, and that exact rare-plant locations fail closed. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |

---

## Rollback

Habitat-association rollback is required when a released or review-authorized association changes plant interpretation, habitat interpretation, sensitivity posture, public labels, map filters, suitability analysis, restoration recommendations, AI answers, or released layers.

Rollback triggers include:

- taxon correction or crosswalk supersession;
- habitat classification update;
- rare-plant sensitivity update;
- model version supersession;
- source withdrawal or rights change;
- mistaken site-specific association from aggregate/literature support;
- public payload leaks restricted Habitat-domain or Flora-domain fields;
- redaction/generalization receipt is missing or invalid;
- downstream release depends on a stale association;
- correction notice invalidates the association basis.

Rollback artifacts should include affected association IDs, Flora subject IDs, Habitat target IDs, source records, release IDs, layer IDs, evidence refs, policy decisions, redaction receipts, correction notices, rollback cards, and replacement/suppression plan.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which Habitat-domain contract path should be treated as the canonical target for HabitatPatch/EcologicalSystem references? | NEEDS VERIFICATION | Inspect Habitat lane contracts/schemas and record any path conflict in the drift register. |
| Should `HabitatAssociation` remain Flora-owned, or should some association classes move to a cross-domain contract root? | PROPOSED / NEEDS VERIFICATION | Review with Flora steward, Habitat steward, and contract steward. |
| Which association types are safe for public map filtering? | NEEDS VERIFICATION | Define policy fixtures and redaction tests. |
| How should modeled suitability confidence be represented? | NEEDS VERIFICATION | Align with model receipt, validation report, and uncertainty-surface contracts. |
| When does an association become a `RangePolygon`, `VegetationCommunity`, or Habitat-domain suitability object instead? | NEEDS VERIFICATION | Add contract crosswalk examples and invalid fixtures. |
| How should restoration planning associations avoid becoming recommendations without review? | NEEDS VERIFICATION | Define policy and UI copy constraints before public release. |

---

## Related contracts

- `plant_taxon.md` and `flora_taxon_crosswalk.md` — plant identity and taxon mapping support.
- `flora_occurrence.md` — occurrence context that may support observed association.
- `rare_plant_record.md` — sensitive plant context requiring fail-closed association handling.
- `vegetation_community.md` — community context that may define or imply habitat association.
- `range_polygon.md` — range/distribution context that must not be confused with site-specific association.
- `botanical_survey.md` — survey method, effort, and completeness context.
- `restoration_planting.md` — project and site suitability context.
- `redaction_receipt.md` — proof of public-safe transformation.
- `domain_validation_report.md` — validation reports for association, policy, sensitivity, and release checks.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Inspect Habitat-domain contracts/schemas and link the correct canonical Habitat target contracts.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any public association layer depends on this contract.
- [ ] Add policy tests for rare-plant habitat, source-restricted fields, modeled suitability, aggregate support, and public-safe map filters.
- [ ] Confirm public API/UI surfaces do not expose sensitive association details or make unreviewed restoration recommendations.
- [ ] Record any contract/schema/path conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
