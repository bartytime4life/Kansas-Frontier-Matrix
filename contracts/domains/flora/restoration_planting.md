<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-restoration-planting
title: Restoration Planting Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Restoration steward · Land-stewardship steward · Contract steward · Source steward · Schema steward · Sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; restoration-planting; project-record; seed-stock-provenance; source-role-aware; sensitivity-aware; release-gated; no-management-advice
tags: [kfm, contracts, flora, restoration-planting, restoration, planting, seed-mix, provenance, project-record, plant-taxon, habitat, evidence, source-role, sensitivity, policy, release, correction, rollback]
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
  - ../../../schemas/contracts/v1/domains/flora/restoration_planting.schema.json
  - ../../../fixtures/domains/flora/restoration_planting/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora restoration-planting semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "RestorationPlanting captures planting/project/species-mix/provenance/monitoring context; it does not prove wild occurrence, prescribe management, approve seed sourcing, or authorize public release by itself."
  - "Restoration records can expose private land, steward sites, rare plant introductions, culturally sensitive plant use, or vulnerable habitat context; public use requires evidence, rights, sensitivity, policy, review, release, correction, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Restoration Planting — Flora

> Semantic contract for Flora `RestorationPlanting`: the evidence-bound project record for planted/restored flora, seed or stock provenance, planting design, site context, monitoring posture, public-safe exposure, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: project record not management advice" src="https://img.shields.io/badge/boundary-project__record__not__management__advice-critical">
</p>

`contracts/domains/flora/restoration_planting.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Restoration classes](#restoration-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/restoration_planting.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/restoration_planting.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `RestorationPlanting` as the Flora object-family contract for restoration project records. Field-level schema shape, fixtures, validators, source registry terms, policy runtime, release workflow, API behavior, UI behavior, land-stewardship integration, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `RestorationPlanting` records planting or restoration context. It does **not** prove a wild occurrence, does **not** replace `FloraOccurrence`, `PlantTaxon`, `HabitatAssociation`, `VegetationCommunity`, or `BotanicalSurvey`, and does **not** authorize treatment, seed sourcing, public site disclosure, or management recommendations by itself.

---

## Meaning

`RestorationPlanting` is the Flora semantic object for a project, site, planting event, seed mix, stock planting, revegetation action, monitoring record, or planned/restored flora intervention. It can represent what was planted, where and when planting occurred, which taxa or source labels were used, what seed or stock provenance was recorded, which site/habitat/community context applies, how success is monitored, and what public-safe release posture is allowed.

It answers:

- Which restoration project, planting event, site, plot, mix, species list, or monitoring record is being described?
- Which plant taxa, source taxon labels, seed lots, stock lots, cultivars, ecotypes, or provenance notes are involved?
- Was the record observed, administrative, regulatory, aggregate, modeled, candidate, or synthetic?
- What spatial support, temporal support, project phase, site context, monitoring method, and evidence support apply?
- Which rights, landowner, steward, cultural, rare-plant, seed-source, habitat, or source-restricted sensitivity checks apply?
- Which public-safe derivative, validation report, policy decision, review record, release manifest, correction path, and rollback target govern downstream use?

A restoration planting record can support project history, stewardship review, seed-mix audit, monitoring summaries, public-safe maps, and AI explanations. It must not be treated as wild occurrence evidence unless separately supported by occurrence/survey evidence.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Restoration planting meaning | `contracts/domains/flora/restoration_planting.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/restoration_planting.schema.json` | Linked only; currently scaffolded |
| Taxon identity | `plant_taxon.md`, `flora_taxon_crosswalk.md` | Plant identity, seed/stock label, and provenance support |
| Observation/survey support | `domain_observation.md`, `botanical_survey.md` | Field checks, monitoring visits, and completeness context |
| Occurrence surfaces | `flora_occurrence.md`, `occurrence_public.md`, `occurrence_restricted.md` | Wild/observed occurrence support; not replaced by planting record |
| Sensitive taxa | `rare_plant_record.md`, `redaction_receipt.md` | Rare/protected/culturally sensitive planting or site protection |
| Community/habitat context | `vegetation_community.md`, `habitat_association.md`, `range_polygon.md` | Site context and suitability support; not collapsed into project truth |
| Invasive context | `invasive_plant_record.md` | Invasive risk, contamination, or management caveats |
| Validation report | `domain_validation_report.md` | Validates project record, fixtures, policy, and release readiness |
| Source registry | `data/registry/sources/flora/` | Source identity, rights, cadence, attribution, access limits |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Admission/release, sensitive site, and public-advice decisions |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only after governed release |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/restoration_planting.schema.json` |
| Schema title | `Restoration Planting` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/restoration_planting.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, source registry links, policy checks, monitoring linkage, public derivatives, correction flows, and rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `RestorationPlanting` should semantically assert:

1. **Project identity** — deterministic identity for the restoration project, planting event, project phase, or monitored planting unit.
2. **Planting subject** — plant taxon, source taxon label, seed mix, stock lot, cultivar/ecotype, restoration community target, or candidate subject.
3. **Project context** — project name, phase, purpose, site, sponsor/steward, landowner/access posture, treatment area, and public-safe label.
4. **Source and role** — SourceDescriptor, source role, source record ID, source authority limits, rights, cadence, and attribution.
5. **Spatial support** — site polygon, plot, management area, transect, planting area, public-safe geometry, withheld geometry, or generalized support.
6. **Temporal support** — planning, planting, seed collection, treatment, monitoring, source, retrieval, release, stale-state, and correction times.
7. **Seed/stock provenance** — source region, seed lot, nursery/stock source, ecotype, cultivar/native status, collection area, or provenance uncertainty where available.
8. **Evidence support** — project documents, observations, invoices, seed-mix sheets, monitoring surveys, steward records, photos, or evidence bundles.
9. **Sensitivity posture** — private-land, rare/protected planting, culturally significant plant use, source-restricted records, vulnerable habitat, or public-safe state.
10. **Governance state** — validation, policy, review, public derivative, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating planted taxa as wild occurrence proof | Planted/restored presence is project evidence, not wild occurrence evidence unless separately observed and classified. |
| Treating the contract as management advice | Operational recommendations require reviewed policy, expertise, and context outside this contract. |
| Treating a seed mix list as confirmed establishment | Planting intent does not prove germination, survival, or community outcome. |
| Treating a project polygon as public-safe by default | Sites can expose private land, steward projects, rare plant introductions, or sensitive habitat. |
| Erasing seed/stock provenance uncertainty | Provenance, cultivar/ecotype, and source-region uncertainty can matter for interpretation. |
| Publishing private landowner or steward details | Public derivatives must remove or generalize sensitive site/context fields. |
| Collapsing restoration target community into observed vegetation community | Desired target and observed community are different claims. |
| Direct public access to RAW/WORK/QUARANTINE project records | Public clients consume governed released derivatives only. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical restoration planting identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `record_class` | `project`, `planting_event`, `seed_mix`, `stock_planting`, `site_preparation`, `monitoring_visit`, `restoration_phase`, `administrative_plan`, `candidate_record`, or `synthetic`. |
| `project_ref` | Parent project or restoration program reference, if modeled separately. |
| `planting_event_ref` | Specific planting/seeding event reference. |
| `flora_subject_type` | `plant_taxon`, `seed_mix`, `stock_lot`, `vegetation_community`, `habitat_association`, `range_polygon`, or candidate. |
| `flora_subject_ref` | Flora subject reference. |
| `taxon_refs` | PlantTaxon refs included in planting or monitoring context. |
| `taxon_crosswalk_refs` | Source name/ID mapping support. |
| `source_taxon_names` | Source-native names retained for audit. |
| `seed_mix_ref` | Seed mix or species list reference. |
| `seed_or_stock_provenance` | Source region, collection zone, ecotype, cultivar, nursery, seed lot, or provenance uncertainty summary. |
| `native_status_claim` | Native, introduced, cultivar, local ecotype, nonlocal, unknown, or source-native status. |
| `project_goal` | Prairie restoration, riparian restoration, wetland restoration, pollinator planting, erosion control, mitigation, reclamation, monitoring, or other project goal. |
| `site_ref` | Site, management area, project area, or plot reference. |
| `geometry_ref` | Internal site/plot/project geometry. |
| `public_geometry_ref` | Public-safe geometry derivative, when released. |
| `geometry_precision` | Exact, parcel/site, plot, management area, county, grid, generalized, suppressed, or unknown. |
| `site_context_refs` | HabitatAssociation, VegetationCommunity, RangePolygon, hydrology/soil/context refs as applicable. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and authority limits. |
| `source_role` | Canonical source role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |
| `source_record_refs` | Source-native project, planting, monitoring, seed, stock, or plan records. |
| `domain_observation_refs` | Observation-envelope refs, when monitoring/field observation applies. |
| `botanical_survey_refs` | Survey/monitoring method and effort context. |
| `occurrence_refs` | Separate occurrence support, if a planted/wild observation has been independently recorded. |
| `rare_plant_refs` | Rare/protected planting or sensitive context, if applicable. |
| `invasive_plant_refs` | Invasive contamination, treatment, or risk context, if applicable. |
| `planned_time` | Planning/design time. |
| `planting_time` | Planting/seeding/staking time. |
| `monitoring_time` | Monitoring visit or evaluation time. |
| `source_time` | Time asserted by source. |
| `retrieval_time` | Time KFM retrieved source material. |
| `release_time` | Public release time, if a public derivative exists. |
| `stale_state` | Current, historical, stale, superseded, withdrawn, completed, failed, ongoing, or unknown. |
| `establishment_state` | Planned, planted, observed-establishing, established, failed, mixed, unknown, or not-assessed. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Private-land, steward-only, rare-plant, cultural, source-restricted, public-safe, or unknown posture. |
| `policy_decision_ref` | Policy result when exposure, advice, or release is material. |
| `validation_report_ref` | Validation report for this record or release candidate. |
| `review_record_ref` | Source, restoration, sensitivity, land-stewardship, or release review. |
| `redaction_receipt_ref` | Required when site, landowner, rare plant, or sensitive context is generalized/suppressed for public output. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source withdrawal, seed-mix correction, monitoring update, supersession, and rollback lineage. |
| `quality_flags` | Taxon-conflict, provenance-unknown, planting-not-established, rights-unknown, sensitivity-unknown, public-advice-risk, source-role-conflict, stale-record, or incomplete-evidence flags. |

---

## Restoration classes

| Class | Meaning | Default posture |
|---|---|---|
| `project` | Restoration project/program record. | Administrative/project context; not biological outcome proof. |
| `planting_event` | Seeding/planting/staking event at place/time. | Supports project action, not establishment unless monitored. |
| `seed_mix` | Species/mix list or seed-lot composition. | Preserve source labels and provenance uncertainty. |
| `stock_planting` | Plugs, nursery stock, transplants, or live material. | Requires stock/provenance caveats. |
| `site_preparation` | Burn, mowing, herbicide, soil prep, invasive removal, or other prep. | Management context only; no recommendation by itself. |
| `monitoring_visit` | Follow-up observation or survey. | Requires method/effort and occurrence/survey separation. |
| `restoration_phase` | Phase, milestone, treatment period, or contract unit. | Administrative context; may be public-safe after review. |
| `administrative_plan` | Planned/speculative planting design. | Planned, not observed action. |
| `candidate_record` | Unreviewed import or unresolved project row. | WORK/QUARANTINE only. |
| `synthetic` | Generated or hypothetical restoration scenario. | Reality-boundary disclosure; not project fact. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | RestorationPlanting posture |
|---|---|---|
| Field monitoring, verified planting observation, photo-supported project inspection | `observed` | Can support observed project/monitoring claim when evidence, time, site, and rights resolve. |
| Permit, mitigation requirement, conservation program rule, planting specification | `regulatory` | Supports obligation/status context; not biological outcome proof. |
| Restoration suitability model, seed-zone model, predicted establishment model | `modeled` | Must remain modeled with uncertainty and version. |
| Program summary, county rollup, public report, grant dashboard | `aggregate` | Supports aggregate reporting only. |
| Project plan, contract, invoice, seed order, management schedule | `administrative` | Supports project intent/action context; not wild occurrence proof by itself. |
| Unreviewed import, watcher row, unresolved project spreadsheet | `candidate` | Hold in WORK/QUARANTINE until reviewed. |
| AI-generated planting plan or hypothetical scenario | `synthetic` | Must not be treated as observed project or recommendation. |

Source role must survive public projection. A planting record cannot be upgraded into occurrence proof or advice by wording.

---

## Sensitivity and release

Restoration records can seem harmless, but they may expose private land, steward work sites, rare plant introductions, culturally significant plant use, vulnerable habitat restoration, seed-source locations, or operational plans.

Rules:

- Public outputs must not expose private landowner details, precise steward-only sites, sensitive rare/protected planting locations, culturally sensitive plant-use context, or source-restricted project data.
- Public derivatives should generalize site geometry, suppress sensitive labels, aggregate by project area, delay release, or withhold records when exposure risk is material.
- Planting records must preserve source role, project phase, time support, establishment uncertainty, provenance uncertainty, and caveats.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, source-restricted, or evidence-incomplete records must not enter public outputs as authoritative project facts.
- Restoration planting records must not become operational advice or recommendations without reviewed policy and domain expertise.
- Public evidence/citation projections must avoid leaking exact restricted sites, private source records, landowner details, or sensitive habitat/rare-plant context.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native project records, seed sheets, invoices, plans, maps, photos, monitoring rows, and steward notes remain source-bound. |
| WORK / QUARANTINE | Candidate records are normalized, taxon-crosswalked, source-role checked, rights checked, sensitivity-screened, deduplicated, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, project/site/planting support, taxon/provenance support, spatial/temporal support, sensitivity state, evidence links, and correction posture. |
| CATALOG / TRIPLET | Restoration claims may be cataloged or projected only with source role, time, establishment/provenance caveats, evidence, and sensitivity preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy decision, review record, redaction receipt when transformed, release manifest, and rollback target. |
| PUBLISHED | Only public-safe project summaries, planting layers, or API/UI payloads appear after governed release. |
| CORRECTION | Taxon correction, seed-mix correction, project update, monitoring update, source withdrawal, rights change, sensitivity update, or public-advice issue triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/restoration_planting.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for project record, planting event, seed mix, stock planting, site-prep record, monitoring visit, administrative plan, public-safe derivative, and suppressed sensitive project.
- [ ] Add invalid fixtures for missing source role, missing taxon support, missing project/site identity, seed mix treated as establishment proof, planting record treated as wild occurrence, management plan treated as recommendation, private-land exact public geometry, missing redaction receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, source role, project/site refs, taxon crosswalk, provenance fields, establishment state, spatial/temporal support, evidence refs, rights state, sensitivity state, policy decision, release linkage, and correction lineage.
- [ ] Add policy tests for private-land exposure, rare/protected planting, culturally sensitive plant use, source-restricted records, public advice prevention, and public map filtering.
- [ ] Add no-network fixtures so CI can validate this contract without live source access.
- [ ] Add non-regression tests for seed-mix correction, taxon split/merge, project withdrawal, monitoring update, redaction bug, and rollback of released derivatives.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, rights/sensitivity allow, review passes, release exists | `ANSWER` / public-safe restoration record allowed |
| Evidence missing, source role ambiguous, provenance unresolved, establishment unsupported | `ABSTAIN` |
| Sensitive site exposure, direct RAW/WORK/QUARANTINE access, rights denial, unsafe recommendation | `DENY` |
| Schema/validator/runtime/source-read failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Directory Rules / canonical path register | Confirms `contracts/` owns object meaning, schemas own machine shape, and `RestorationPlanting` is the Flora object-family contract for restoration project records. |
| Flora object-family register | Confirms `RestorationPlanting` is an expected Flora object family and that field-level shape remains outside the register. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM trust posture | Confirms evidence, source role, policy, review, release, correction, and rollback must outrank generated recommendations, project summaries, or map layers. |

---

## Rollback

Restoration-planting rollback is required when a released or review-authorized record weakens source integrity, exposes sensitive site context, misstates project status, misstates establishment, violates rights, creates unsafe advice, or depends on superseded project/taxon/provenance evidence.

Rollback triggers include:

- private-land, steward-only, rare-plant, cultural, or source-restricted site detail exposed;
- seed mix or planting plan published as established vegetation or wild occurrence;
- management/treatment record presented as recommendation without review;
- taxon correction, seed-lot correction, or provenance correction;
- project withdrawal, source withdrawal, rights change, or steward correction;
- monitoring update invalidates establishment or survival claim;
- public derivative lacks redaction receipt, release manifest, or rollback target;
- public evidence projection leaks restricted project records or site notes;
- release manifest points to RAW/WORK/QUARANTINE or restricted source instead of public derivative.

Rollback artifacts should include affected restoration IDs, project IDs, planting event IDs, seed mix refs, taxon/crosswalk IDs, site/geometry refs, occurrence/survey/monitoring refs, public derivative IDs, release IDs, layer/API/UI IDs, evidence refs, policy decisions, redaction receipts, correction notices, rollback cards, replacement derivatives, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which restoration/project source families are approved, and what rights/access limits apply? | NEEDS VERIFICATION | Source registry, restoration steward review, and policy tests. |
| Should seed mixes/stock lots become separate contracts or remain nested under RestorationPlanting? | PROPOSED / NEEDS VERIFICATION | Resolve with schema, flora, and restoration stewards. |
| How should KFM distinguish planted occurrence, wild occurrence, and monitored establishment? | NEEDS VERIFICATION | Add fixtures spanning RestorationPlanting, FloraOccurrence, and BotanicalSurvey. |
| Which public site geometry classes are acceptable for private or steward-controlled projects? | NEEDS VERIFICATION | Sensitivity policy and redaction fixtures. |
| How should provenance/ecotype/cultivar status be represented without overclaiming local adaptation? | NEEDS VERIFICATION | Source profiles, schema enum review, and validation tests. |
| Which project records require landowner/steward review before public release? | NEEDS VERIFICATION | Policy + release steward decision. |

---

## Related contracts

- `plant_taxon.md` and `flora_taxon_crosswalk.md` — plant identity and seed/stock label mapping support.
- `domain_observation.md` — source observation envelope.
- `botanical_survey.md` — monitoring method, effort, and completeness context.
- `flora_occurrence.md`, `occurrence_public.md`, and `occurrence_restricted.md` — occurrence surfaces that must remain separate from planting intent.
- `rare_plant_record.md` — rare/protected planting and sensitive site context.
- `vegetation_community.md` and `habitat_association.md` — target/observed community and habitat context.
- `invasive_plant_record.md` — invasive risk, contamination, or treatment context.
- `redaction_receipt.md` — public-safe transformation proof.
- `domain_validation_report.md` — validation reports for records, policy, fixtures, and releases.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any restoration layer or public project summary depends on this contract.
- [ ] Add source profiles for approved restoration/project/seed/stock sources before activation.
- [ ] Add policy tests for private-land exposure, rare/protected planting, culturally sensitive plant use, source-restricted records, and public-advice prevention.
- [ ] Confirm public API/UI/map/AI surfaces label planned, planted, monitored, established, failed, candidate, and synthetic records clearly.
- [ ] Confirm every public derivative has release manifest, redaction receipt when transformed, correction path, and rollback target.
- [ ] Record any contract/schema/path/source/provenance conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
