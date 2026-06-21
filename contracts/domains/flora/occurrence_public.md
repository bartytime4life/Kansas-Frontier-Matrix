<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-occurrence-public
title: Public Occurrence Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Occurrence steward · Redaction steward · Contract steward · Source steward · Schema steward · Sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; public-occurrence; derivative; generalized; redaction-aware; source-role-aware; release-gated; no-canonical-exact-truth
tags: [kfm, contracts, flora, occurrence-public, public-safe-occurrence, generalized-occurrence, redaction, geoprivacy, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./flora_occurrence.md
  - ./occurrence_restricted.md
  - ./rare_plant_record.md
  - ./specimen_record.md
  - ./plant_taxon.md
  - ./flora_taxon_crosswalk.md
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
  - ../../../schemas/contracts/v1/domains/flora/occurrence_public.schema.json
  - ../../../fixtures/domains/flora/occurrence_public/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora public-safe occurrence semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "OccurrencePublic is a released or release-candidate derivative of Flora occurrence support; it is not the canonical exact occurrence, not a raw source row, and not a replacement for restricted/internal records."
  - "Public occurrence payloads must preserve source role, evidence, time, scale, uncertainty, redaction/generalization, release, correction, and rollback posture without exposing sensitive exact locations."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Occurrence Public — Flora

> Semantic contract for Flora `OccurrencePublic`: the public-safe occurrence derivative used for released map/API/UI surfaces after evidence, source role, sensitivity, redaction/generalization, review, release, correction, and rollback support resolve.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: public derivative not canonical exact" src="https://img.shields.io/badge/boundary-derivative__not__canonical__exact-critical">
</p>

`contracts/domains/flora/occurrence_public.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Public derivative classes](#public-derivative-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/occurrence_public.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/occurrence_public.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `OccurrencePublic` as the public-safe occurrence derivative: generalized, county-level, or grid-binned. Field-level schema shape, fixtures, validators, source registry terms, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `OccurrencePublic` is a public-safe derivative, not canonical exact truth. It must not expose restricted exact geometry, RAW/WORK/QUARANTINE content, steward-only notes, private-land joins, culturally sensitive plant knowledge, or source-restricted details. Public release still requires separate validation, policy, review, redaction receipt, release manifest, correction path, and rollback target.

---

## Meaning

`OccurrencePublic` is the Flora semantic object for an occurrence-class record that has been transformed, generalized, aggregated, binned, suppressed, or otherwise prepared for public or semi-public use.

It answers:

- Which internal occurrence, specimen, rare-plant record, survey record, invasive record, phenology observation, or aggregate support produced this public-safe derivative?
- What public geometry, label, scale, time, uncertainty, source role, evidence, and caveats are safe to expose?
- What was redacted, generalized, suppressed, binned, delayed, or withheld?
- Which policy, review, release, redaction receipt, correction, and rollback artifacts authorize this public representation?
- What must public clients know so they do not treat the derivative as canonical exact truth?

A public occurrence is a governed delivery object. It is not the source row, not the internal exact point, not the rare-plant restricted record, and not a shortcut around release controls.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Public derivative meaning | `contracts/domains/flora/occurrence_public.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/occurrence_public.schema.json` | Linked only; currently scaffolded |
| Umbrella occurrence meaning | `contracts/domains/flora/flora_occurrence.md` | Upstream occurrence-class support; not replaced |
| Restricted exact counterpart | `contracts/domains/flora/occurrence_restricted.md` | Internal exact geometry; never public source of truth |
| Rare/protected source | `contracts/domains/flora/rare_plant_record.md` | Sensitive upstream record; default-deny exact geometry |
| Voucher/source support | `specimen_record.md`, `domain_observation.md`, `botanical_survey.md` | Evidence and observation context |
| Taxon support | `plant_taxon.md`, `flora_taxon_crosswalk.md` | Public label and taxon caveat support |
| Redaction proof | `contracts/domains/flora/redaction_receipt.md` | Required when geometry/details are transformed |
| Validation report | `contracts/domains/flora/domain_validation_report.md` | Validates derivative/release candidate |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Admission/release and fail-closed decisions |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe artifacts only after release |
| Public clients | governed API/UI/map layers | Consume released derivatives, not internal exact stores |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/occurrence_public.schema.json` |
| Schema title | `Occurrence Public` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/occurrence_public.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, policy checks, public API payloads, map-layer properties, release manifests, correction flows, and rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `OccurrencePublic` should semantically assert:

1. **Public derivative identity** — deterministic public occurrence identity distinct from internal exact/canonical identity.
2. **Upstream support** — references to allowed upstream `FloraOccurrence`, `OccurrenceRestricted`, `RarePlantRecord`, `SpecimenRecord`, `BotanicalSurvey`, `InvasivePlantRecord`, `PhenologyObservation`, or aggregate support where policy allows.
3. **Public geometry** — generalized, binned, county-level, grid-level, buffered, delayed, suppressed, or otherwise public-safe spatial support.
4. **Transformation proof** — redaction/generalization/suppression/delay receipt with inputs, outputs, method, policy reason, and integrity hash where applicable.
5. **Source-role visibility** — observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic posture preserved in public-facing caveats.
6. **Evidence support** — EvidenceRef/EvidenceBundle links sufficient for cite-or-abstain behavior without exposing restricted content.
7. **Taxon support** — public-safe taxon label, original/source label caveat, accepted/candidate taxon posture, and crosswalk support.
8. **Temporal support** — observed/source/retrieval/release/correction/stale support visible at a safe level.
9. **Sensitivity posture** — proof that exact rare-plant, steward-only, private-land, cultural, or source-restricted details are not exposed.
10. **Governance state** — validation, policy, review, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating public derivative as canonical exact occurrence | Public derivative is intentionally transformed and may be generalized, binned, delayed, or suppressed. |
| Publishing exact restricted geometry | Exact sensitive locations belong in restricted/internal flows and fail closed for public clients. |
| Deriving public payload directly from RAW/WORK/QUARANTINE | Public clients use governed released artifacts only. |
| Omitting source role or uncertainty | Public users must see whether the support is observed, aggregate, modeled, regulatory, administrative, candidate, or synthetic. |
| Treating candidate records as public facts | Candidate/source-unresolved records cannot be authoritative public occurrences. |
| Exposing private-land or steward notes through labels/caveats | Public labels must be redacted and reviewed. |
| Treating redaction as irreversible truth | Redaction is a transformation receipt; upstream evidence and rollback remain auditable under governed access. |
| Publishing without rollback target | Public release requires correction and rollback path appropriate to consequence. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical public-derivative occurrence identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `public_record_class` | `generalized_point`, `county`, `grid_bin`, `hex_bin`, `range_cell`, `suppressed_geometry`, `delayed_release`, `aggregate_summary`, `public_label_only`, or `public_layer_feature`. |
| `upstream_occurrence_ref` | Internal FloraOccurrence or occurrence-family ref, access-controlled when sensitive. |
| `restricted_occurrence_ref` | Restricted counterpart, if allowed as an internal ref only. |
| `rare_plant_record_ref` | Rare/protected upstream record, if applicable and access-controlled. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and authority limits. |
| `source_role` | Canonical source role preserved in public caveats. |
| `taxon_ref` | Public-safe PlantTaxon or reviewed candidate taxon ref. |
| `taxon_label_public` | Public-safe display label. |
| `taxon_caveat_public` | Safe caveat for synonym, candidate, source-label, aggregate, or modeled support. |
| `public_geometry_ref` | Public-safe geometry object or layer feature reference. |
| `public_geometry_type` | County, grid, binned point, generalized point, polygon, suppressed, label-only, or other public-safe form. |
| `public_spatial_scale` | The minimum support scale visible to public clients. |
| `redaction_method` | Generalization, binning, suppression, delay, aggregation, precision reduction, masking, or withholding. |
| `redaction_receipt_ref` | Required transform receipt for sensitive or transformed data. |
| `location_uncertainty_public` | Public-safe uncertainty, scale, or caveat. |
| `observed_time_public` | Public-safe observed/event time or coarse time bucket. |
| `source_time` | Source-native assertion time, if safe. |
| `retrieval_time` | Time KFM retrieved source material. |
| `release_time` | Public release time. |
| `stale_state` | Current, stale, historical, superseded, withdrawn, or unknown. |
| `evidence_refs_public` | Public-safe evidence references or citations. |
| `evidence_refs_internal` | Internal evidence refs, access-controlled when sensitive. |
| `rights_state` | Public redistribution, attribution, and source-term posture. |
| `sensitivity_state` | Public-safe, generalized, suppressed, delayed, steward-only, restricted-source, rare-plant, private-land, or unknown. |
| `policy_decision_ref` | Release/admissibility decision. |
| `validation_report_ref` | Validation report for the derivative or release candidate. |
| `review_record_ref` | Steward/source/sensitivity/release review. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, supersession, withdrawal, stale-state, and rollback lineage. |
| `public_caveats` | Human-readable caveats safe for map/API/UI display. |
| `quality_flags_public` | Public-safe data quality flags. |

---

## Public derivative classes

| Class | Meaning | Default posture |
|---|---|---|
| `generalized_point` | Exact point moved/rounded/generalized to reduce exposure. | Requires redaction receipt and policy support. |
| `county` | Occurrence shown only at county support. | Good default for sensitive or coarse records. |
| `grid_bin` | Occurrence counted or shown in a grid cell. | Requires cell-size policy and suppression thresholds. |
| `hex_bin` | Occurrence represented in a hexagonal bin. | Same caveats as grid bins. |
| `range_cell` | Occurrence-like support projected to a range/distribution cell. | Must preserve aggregate/modeled caveats. |
| `suppressed_geometry` | No public geometry, only safe label/summary. | Required when even generalized geometry is unsafe. |
| `delayed_release` | Public output delayed to reduce exposure risk. | Requires release-time and source-time caveats. |
| `aggregate_summary` | Public occurrence support only as count/summary. | Must not imply exact presence. |
| `public_label_only` | Safe non-spatial public disclosure. | Useful for sensitive species or restricted sources. |
| `public_layer_feature` | Released map/API feature with approved public properties. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | Public derivative posture |
|---|---|---|
| Steward-reviewed field observation or specimen-backed record | `observed` | Can support public derivative if sensitivity/rights/release gates pass. |
| Rare/protected status, recovery list, agency restriction | `regulatory` | Supports public caveat/status only; not occurrence proof by itself. |
| Distribution model, habitat suitability model, inferred occurrence | `modeled` | Must remain model-labeled; not observed fact. |
| Atlas/county/grid/portal rollup | `aggregate` | Public output must remain aggregate-scale. |
| Management/project/site list | `administrative` | Public context only; not biological occurrence proof by itself. |
| Watcher/import/community-science unresolved row | `candidate` | No authoritative public occurrence until reviewed. |
| AI-generated/reconstructed scenario | `synthetic` | Reality-boundary disclosure; never public observed fact. |

Public transformation can reduce exposure, but it cannot upgrade source authority.

---

## Sensitivity and release

`OccurrencePublic` is a release-facing surface. Its safest default is to expose less detail than the internal record and more governance context than a plain map point.

Rules:

- Exact rare-plant, steward-controlled, private-land, culturally sensitive, and source-restricted geometry must fail closed unless a reviewed policy allows a transformed public representation.
- Public geometry must be no more precise than policy, source rights, review state, and sensitivity allow.
- Public evidence/citation refs must not leak restricted source rows, exact coordinates, internal reviewer notes, or private source context.
- Public payloads must carry source role, time support, uncertainty, scale, and caveats where material.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, evidence-incomplete, or unreviewed records must not be public authoritative occurrences.
- Public release requires validation report, policy decision, review state, release manifest, rollback target, and redaction receipt when transformed.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source occurrence data remains source-bound and never public through this contract. |
| WORK / QUARANTINE | Candidate public derivatives are prepared, sensitivity-screened, redacted/generalized, validated, and reviewed. Unsafe candidates remain quarantined or denied. |
| PROCESSED | Public derivative candidates receive deterministic identity, public geometry, evidence/citation posture, source-role caveats, redaction receipt refs, and correction posture. |
| CATALOG / TRIPLET | Public-safe claims may be cataloged or projected only at the approved support scale with caveats preserved. |
| RELEASE CANDIDATE | Release packages include validation report, policy decision, review record, redaction receipt, release manifest, and rollback target. |
| PUBLISHED | Public API/UI/map layers consume released public derivatives only. Internal exact stores remain outside public paths. |
| CORRECTION | Taxon change, geometry issue, source withdrawal, rights change, sensitivity update, stale-state update, or redaction failure triggers correction and possible rollback/suppression. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/occurrence_public.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for county-level derivative, grid-binned derivative, generalized point, suppressed-geometry record, delayed-release record, aggregate summary, and public-layer feature.
- [ ] Add invalid fixtures for exact rare-plant public geometry, missing redaction receipt, missing release manifest, missing rollback target, rights-unknown public output, candidate-as-public-fact, modeled-as-observed label, aggregate-as-exact label, and public evidence leaking restricted details.
- [ ] Add validator checks for upstream refs, source role, public geometry type, scale, redaction method, redaction receipt, evidence refs, public caveats, sensitivity state, policy decision, validation report, release ref, and correction lineage.
- [ ] Add policy tests for DENY / ABSTAIN / ERROR outcomes.
- [ ] Add no-network fixtures so CI can validate this contract without live source access.
- [ ] Add non-regression tests for rollback after source withdrawal, geometry leak, taxonomy correction, stale-state update, and redaction-method bug.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, policy allows, review passes, release exists, rollback target exists | `ANSWER` / public-safe payload allowed |
| Evidence missing, temporal support insufficient, source role ambiguous, redaction support incomplete | `ABSTAIN` |
| Sensitive exposure, direct RAW/WORK/QUARANTINE access, rights denial, restricted evidence leak | `DENY` |
| Schema/validator/runtime failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Directory Rules | Confirms `contracts/` owns object meaning, `schemas/` owns machine shape, and domain-specific files live as segments inside responsibility roots. |
| Flora canonical path register | Confirms `OccurrencePublic` is the public-safe Flora occurrence derivative and distinguishes it from restricted exact occurrence records. |
| Flora object-family register | Confirms Flora object-family scope and states that field-level shape remains outside the register. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM public-client rule | Confirms public clients should use governed APIs/released artifacts, not internal stores or direct model outputs. |

---

## Rollback

Public occurrence rollback is required when a released derivative weakens source integrity, leaks sensitive detail, misstates source role, misrepresents scale, loses evidence support, violates rights, or cannot support correction.

Rollback triggers include:

- exact or inferable rare-plant location leak;
- private-land, steward, cultural, or source-restricted detail exposed;
- redaction/generalization bug;
- missing or invalid redaction receipt;
- source withdrawal or changed source terms;
- taxon correction or crosswalk supersession;
- public derivative points to stale or superseded upstream record;
- public caveat omits modeled/aggregate/candidate source role;
- release manifest mismatch;
- rollback target missing or invalid.

Rollback artifacts should include affected public IDs, upstream occurrence IDs, restricted counterpart IDs if access allows, layer IDs, release IDs, evidence refs, policy decisions, redaction receipts, correction notices, rollback cards, replacement public derivatives, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which public geometry classes are approved for rare/protected taxa by default? | NEEDS VERIFICATION | Resolve in `policy/sensitivity/flora/` with fixtures. |
| What minimum grid/cell size or county-level threshold is required for sensitive Flora records? | NEEDS VERIFICATION | Define redaction policy and tests. |
| Should public derivatives carry internal upstream refs as hidden/admin-only fields or separate release metadata only? | NEEDS VERIFICATION | Decide with API/UI/release stewards. |
| How should public citation links avoid leaking restricted evidence refs? | NEEDS VERIFICATION | Define public EvidenceBundle projection rules. |
| Should `OccurrencePublic` be generated only during release packaging or earlier as a release candidate object? | PROPOSED / NEEDS VERIFICATION | Resolve with pipeline and release stewards. |
| Which stale-state thresholds force suppression, caveat, or re-release? | NEEDS VERIFICATION | Policy + validation steward decision. |

---

## Related contracts

- `flora_occurrence.md` — umbrella occurrence-class source support.
- `occurrence_restricted.md` — internal exact-geometry counterpart.
- `rare_plant_record.md` — rare/protected plant sensitivity source.
- `specimen_record.md` — voucher/specimen support.
- `domain_observation.md` — source observation envelope.
- `plant_taxon.md` and `flora_taxon_crosswalk.md` — taxon identity and public label support.
- `redaction_receipt.md` — public-safe transformation proof.
- `domain_validation_report.md` — validation reports for public derivative/release candidates.
- `range_polygon.md`, `habitat_association.md`, `vegetation_community.md`, `invasive_plant_record.md`, and `phenology_observation.md` — downstream or adjacent public-safe layer consumers.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any public Flora occurrence layer depends on this contract.
- [ ] Add policy tests for rare-plant, private-land, steward-only, source-restricted, candidate, modeled, aggregate, and stale-state cases.
- [ ] Confirm public API/UI surfaces consume released derivatives only and never read restricted exact records directly.
- [ ] Confirm every public derivative has release manifest, redaction receipt when transformed, and rollback target.
- [ ] Record any contract/schema/path conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
