<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-geophysical-observation
title: GeophysicalObservation Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Geophysics steward
  - OWNER_TBD — Spatial steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; geology; geophysical-observation; survey-product; source-role-aware; modeled-surface-caveat; release-gated
tags: [kfm, contracts, geology, GeophysicalObservation, geophysics, gravity, magnetic, seismic, survey, footprint, instrument-class, modeled-surface, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./CrossSection.md
  - ./GeologicUnit.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../docs/domains/geology/sublanes/README.md
  - ../../../schemas/contracts/v1/domains/geology/GeophysicalObservation.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology GeophysicalObservation semantic contract."
  - "The exact paired schema path schemas/contracts/v1/domains/geology/GeophysicalObservation.schema.json was not found in this session; schema shape and casing remain NEEDS VERIFICATION."
  - "GeophysicalObservation is a field or remote-sensed geophysical measurement/survey-product reference. Derived surfaces may be modeled and must not be relabeled as observed."
  - "A GeophysicalObservation does not replace GeologicUnit, CrossSection, StructureFeature, HydrostratigraphicUnit, Hydrology measurement, Hazards risk, resource estimate, public layer, or AI/UI truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GeophysicalObservation — Geology

> Semantic contract for Geology `GeophysicalObservation`: the evidence-bound object for geophysical survey products, footprints, instrument classes, observed measurements, modeled/derived surfaces, public-safe derivatives, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: GeophysicalObservation" src="https://img.shields.io/badge/object-GeophysicalObservation-blue">
  <img alt="Schema: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Boundary: observation not risk or model truth" src="https://img.shields.io/badge/boundary-observation__not__risk__or__model__truth-critical">
</p>

`contracts/domains/geology/GeophysicalObservation.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Observation classes](#observation-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/GeophysicalObservation.md`  
> **Schema posture:** exact paired schema path `schemas/contracts/v1/domains/geology/GeophysicalObservation.schema.json` was **not found** in this session  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Geophysical Observation` as an owned object family for field or remote-sensed geophysical measurements and survey products. Field-level schema shape, fixtures, validators, source registry records, policy runtime, release workflow, API behavior, UI behavior, instrument vocabulary, method vocabulary, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `GeophysicalObservation` is observation or survey-product evidence. It does **not** prove a `GeologicUnit`, `CrossSection`, `StructureFeature`, `HydrostratigraphicUnit`, Hydrology measurement, Hazards risk, mineral occurrence, resource estimate, reserve claim, public layer, or AI/UI statement by itself.

---

## Meaning

`GeophysicalObservation` is the Geology semantic object for a geophysical survey product, measurement series, footprint, profile, line, grid, raster, interpreted horizon, or modeled/derived surface admitted as evidence in KFM.

It answers:

- Which survey, observation, product, line, grid, raster, or derived surface is being referenced?
- Which source, source role, instrument class, method, geometry footprint, time, units, processing state, uncertainty, and evidence support apply?
- Which GeologicUnit, StructureFeature, CrossSection, HydrostratigraphicUnit, resource context, or public derivative may cite the observation without collapsing identity?
- Is the object observed, processed, interpreted, modeled, aggregate, candidate, synthetic, or public-safe?
- What public-safe footprint, summary, or derivative may be shown?
- Which policy decision, review record, representation/redaction receipt, release manifest, correction notice, and rollback target govern downstream use?

A geophysical observation can support interpretation. It is not itself an interpretation authority, a risk claim, a hydrology measurement, a public alert, or a release decision.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Geophysical observation meaning | `contracts/domains/geology/GeophysicalObservation.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/GeophysicalObservation.schema.json` or accepted variant | NEEDS VERIFICATION; exact path not found |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms owned family and adjacent-lane exclusions |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms purpose, key fields, source roles, and sensitivity posture |
| Cross-section contract | `contracts/domains/geology/CrossSection.md` | May cite geophysical evidence; does not replace it |
| Geologic-unit contract | `contracts/domains/geology/GeologicUnit.md` | May cite survey products; unit identity stays separate |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, modeled, restricted, and public-safe proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

No exact paired schema was confirmed for this casing/path in this session.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/GeophysicalObservation.md` |
| Exact schema tried | `schemas/contracts/v1/domains/geology/GeophysicalObservation.schema.json` |
| Exact schema result | Not found in this session |
| Naming posture | `GeophysicalObservation` preserved because the user requested this path and Geology docs use the human-readable `Geophysical Observation` owned-family spelling |
| Roster posture | §B-only owned family; not present in the §E main object-family table verbatim |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema is created or located under an accepted name, this contract is semantic guidance only.

---

## Assertions

A reviewed `GeophysicalObservation` should semantically assert:

1. **Observation identity** — deterministic identity for the survey/product/line/grid/raster/horizon/surface, source, role, temporal scope, and normalized digest.
2. **Source identity** — SourceDescriptor, source record ID, survey ID, source role, source time, rights, cadence, and attribution.
3. **Instrument/method support** — gravity, magnetic, seismic, electrical, electromagnetic, remote-sensed, derived, or source-native instrument/method class.
4. **Geometry support** — footprint, line geometry, grid/raster extent, profile corridor, resolution, CRS, geometry fingerprint, and public-safe derivative geometry where released.
5. **Observed vs derived posture** — observed measurements, processed products, interpreted horizons, modeled surfaces, aggregate summaries, and synthetic reconstructions remain explicitly labeled.
6. **Units and processing state** — units, processing level, filter/transform, datum, calibration, normalization, and uncertainty/caveats where source-supported.
7. **Temporal discipline** — source time, observed/acquisition time, valid time, retrieval time, release time, correction time, and stale/supersession state remain distinct.
8. **Evidence linkage** — survey reports, data products, rasters, linework, metadata, interpretation reports, EvidenceRefs, and EvidenceBundles.
9. **Derived-use posture** — cross-section, unit, structure, hydrostratigraphic, resource-context, or public-map uses with caveats.
10. **Governance state** — validation, review, representation/redaction, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating a geophysical observation as mapped unit truth | It can support GeologicUnit interpretation, but it is not the unit identity. |
| Treating a derived surface as observed measurement | Modeled/processed/derived products must retain method and source-role labels. |
| Treating a survey product as hazards risk | Hazards owns risk. Geology supplies structural/geophysical context only. |
| Treating geophysics as Hydrology measurement | Hydrology owns measurements; Geology may provide context or geologic interpretation only. |
| Treating interpreted horizons as direct observations | Interpretation version, method, and uncertainty must be explicit. |
| Treating a raster tile or image as authority | Delivery artifacts are downstream carriers; source/evidence/release state carries authority. |
| Treating public generalized footprint as exact footprint | Public-safe geometry is a derivative with caveats. |
| Treating scaffold presence as release approval | Publication requires release manifest, policy outcome where material, correction path, and rollback target. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by any verified schema in this session.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM geophysical-observation identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `GeophysicalObservation` or accepted canonical spelling after naming reconciliation. |
| `observation_class` | Gravity, magnetic, seismic, electrical, electromagnetic, remote-sensing, raster product, line profile, interpreted horizon, modeled surface, candidate, synthetic, or public derivative. |
| `survey_id` | Source-native or KFM survey/product identifier. |
| `instrument_class` | Instrument or method family. |
| `method_ref` | Method, processing workflow, survey type, or source-native method ref. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, modeled, aggregate, administrative, regulatory, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native survey, product, line, grid, raster, plate, report, or dataset record. |
| `geometry_ref` | Internal footprint, line, profile, grid, raster, or corridor geometry reference. |
| `public_geometry_ref` | Public-safe generalized footprint/extent, if released. |
| `geometry_fingerprint` | Stable geometry fingerprint for identity and drift detection. |
| `crs` | Coordinate reference system / projection metadata. |
| `spatial_resolution` | Grid cell size, line spacing, sample spacing, footprint resolution, or source-native resolution. |
| `extent_precision` | Source precision, generalized, aggregate, withheld, or unknown. |
| `units_ref` | Unit vocabulary/ref for observed or derived values. |
| `datum_ref` | Vertical, magnetic, gravity, time/depth, or source-native datum as applicable. |
| `processing_level` | Raw, corrected, filtered, gridded, interpreted, modeled, generalized, or source-native level. |
| `processing_summary` | Public-safe processing/method caveat. |
| `uncertainty_summary` | Measurement uncertainty, processing caveat, spatial uncertainty, or interpretation confidence. |
| `observed_time` | Acquisition/measurement time, if known. |
| `source_time` | Source publication/assertion time. |
| `valid_time` | Time interval the product/interpretation claims to represent, where material. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `stale_state` | Current, historical, stale, superseded, withdrawn, or unknown. |
| `geologic_unit_refs` | Linked GeologicUnit or SurficialUnit refs supported by interpretation. |
| `structure_feature_refs` | Linked StructureFeature / FaultStructure refs where supported. |
| `cross_section_refs` | Linked CrossSection refs that cite the observation. |
| `hydrostratigraphic_refs` | Hydrostratigraphic context refs, not Hydrology measurement ownership. |
| `resource_context_refs` | Mineral/resource/extraction refs only where evidence supports relationship and anti-collapse rules hold. |
| `representation_receipt_ref` | Required when a modeled, rendered, reconstructed, or synthetic surface/visualization is used as a carrier. |
| `redaction_receipt_ref` | Required when footprint/detail is generalized or withheld for public output. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Public-safe, generalized, rights-limited, restricted, proprietary, source-limited, withheld, or unknown. |
| `policy_decision_ref` | Policy result governing use or release where material. |
| `review_record_ref` | Source, geology, geophysics, sensitivity, interpretation, or release review. |
| `validation_report_ref` | Validation report for schema, geometry, source-role, processing state, uncertainty, sensitivity, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, processing correction, geometry correction, rights update, supersession, and rollback lineage. |
| `quality_flags` | Source-role conflict, method missing, unit missing, geometry missing, resolution unknown, rights unknown, sensitivity unknown, derived-as-observed, stale source, or incomplete evidence. |

---

## Observation classes

| Class | Meaning | Default posture |
|---|---|---|
| `gravity_survey` | Gravity measurements, grids, anomaly maps, or related products. | Public-safe/generalized when rights allow; method and units required. |
| `magnetic_survey` | Magnetic measurements, grids, anomaly maps, or related products. | Public-safe/generalized when rights allow; datum and processing caveats required. |
| `seismic_profile` | Seismic line/profile/product or interpreted horizon source. | Rights and interpretation review required; derived surfaces labeled. |
| `electrical_or_em` | Electrical, electromagnetic, resistivity, conductivity, or related survey product. | Method, units, footprint, and caveats required. |
| `remote_sensed_geophysics` | Remote-sensed geophysical proxy/product. | Source-role and method caveats required. |
| `interpreted_horizon` | Interpreted horizon/contact/surface derived from observations. | Modeled/interpreted; not observed unless tied to direct evidence. |
| `model_derived_surface` | Interpolated or modeled geophysical surface. | Modeled, not observed; representation receipt may be required. |
| `candidate_record` | Unreviewed import or unresolved source product. | WORK/QUARANTINE until reviewed. |
| `public_derivative` | Released generalized footprint, summary, or display product. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | GeophysicalObservation posture |
|---|---|---|
| Field/airborne/remote survey measurements | `observed` | Evidence-bearing measurement/product; preserve acquisition time, method, units, geometry, and uncertainty. |
| Processed grid, filtered raster, gridded anomaly product | `observed` with processing caveat or `aggregate` | Preserve processing level and method; do not hide derived nature. |
| Interpreted horizon, interpolated surface, inversion product | `modeled` | Interpretation/model output; never label as observed measurement. |
| Regional compilation, map plate, atlas product | `aggregate` | Compiled support with source scale/version caveats. |
| Source catalog or inventory row | `administrative` | Identifies product/status context; not observation truth by itself. |
| Unreviewed import, missing method, unresolved source row | `candidate` | Quarantine until identity, method, units, geometry, and rights resolve. |
| AI-generated or hypothetical geophysical feature | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`GeophysicalObservation` is evidence or a survey product, not the downstream claim.

```text
GeophysicalObservation != GeologicUnit
GeophysicalObservation != StructureFeature
GeophysicalObservation != CrossSection
GeophysicalObservation != HydrostratigraphicUnit
GeophysicalObservation != Hydrology measurement
GeophysicalObservation != Hazards risk
GeophysicalObservation != MineralOccurrence
GeophysicalObservation != ResourceEstimate
GeophysicalObservation != public tile/layer release
GeophysicalObservation != AI summary
```

Any linkage must preserve object identity, source role, method, uncertainty, processing level, rights, evidence, validation, release, and correction state.

---

## Sensitivity and release

Geophysical observations are often public-safe at generalized footprint scale when rights allow, but source rights, proprietary survey detail, infrastructure-adjacent context, high-resolution linework, modeled surfaces, and derived interpretation can require review or generalization.

Rules:

- A survey product is not automatically a released KFM public layer.
- Public derivatives require validation, source rights, policy/review where material, release manifest, correction path, and rollback target.
- Footprints may be coarsened or summarized when rights or sensitivity require it.
- Modeled, interpreted, rendered, or reconstructed products must carry source role, method, uncertainty, and reality-boundary caveats.
- Public outputs must preserve instrument class, method, units, source time, observed time where known, processing level, footprint precision, and caveats.
- Candidate, synthetic, rights-unknown, method-unknown, unit-missing, geometry-missing, or evidence-incomplete records must not enter public outputs as authoritative observation facts.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native survey files, rasters, linework, grids, profiles, metadata, units, methods, and reports remain source-bound. |
| WORK / QUARANTINE | Candidate products are normalized, method/unit checked, source-role checked, rights/sensitivity-screened, geometry/CRS checked, processing-level labeled, and evidence-linked. |
| PROCESSED | Reviewed observations receive deterministic identity, survey/product ID, geometry fingerprint, method/units, processing state, evidence refs, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, acquisition/source/retrieval times, method, units, processing level, evidence, geometry precision, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy/review where material, representation/redaction receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only released public-safe observation summaries, footprints, products, layers, or API/UI payloads appear in public clients. |
| CORRECTION | Source update, method correction, unit correction, geometry correction, reprocessing, interpretation supersession, rights change, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Create or locate the accepted paired schema path.
- [ ] Add valid fixtures for gravity survey, magnetic survey, seismic profile, electrical/EM survey, processed grid, interpreted horizon, model-derived surface, candidate import, and public generalized derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing survey ID, missing instrument class, missing geometry fingerprint, missing units, missing method, derived surface labeled observed, source/observed time collapse, rights unknown, footprint released without review, missing representation/redaction receipt where required, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, survey ID, geometry fingerprint, CRS, instrument class, method refs, units, processing level, observed/source time separation, source role, evidence refs, release refs, and correction refs.
- [ ] Add policy/access tests proving public clients consume released derivatives only.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source revision, unit correction, method correction, geometry repair, reprocessing, modeled-surface relabeling, rights update, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, method/units/geometry validate, source role is clear, derivative is released | `ANSWER` / public-safe observation derivative may be shown |
| Evidence, rights, source role, method, units, geometry, or processing support is incomplete | `ABSTAIN` |
| Restricted detail would be exposed, rights deny use, release is absent, or derived content is mislabeled as observed | `DENY` |
| Schema, validator, source-read, transform, rendering, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Geology scope doc | Confirms Geology owns Geophysical Observation and excludes hydrology, hazards, title, and UI/AI truth. | Records broader naming drift and field realization remains PROPOSED. |
| Geology object-family doc | Confirms GeophysicalObservation purpose, proposed key fields, material times, sensitivity posture, and observed/modeled source-role distinction. | Does not prove schema or validator enforcement. |
| Object-family sensitivity table | Confirms T0/T1 generalized-footprint posture. | Tier mapping remains NEEDS VERIFICATION under ADR-S-05. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized GeophysicalObservation weakens source integrity, misstates source role, hides method/uncertainty, labels derived content as observed, exposes restricted detail, or depends on superseded source, geometry, rights, processing, or release evidence.

Rollback triggers include:

- schema/name/casing is superseded by ADR or schema decision;
- source survey/product corrected, withdrawn, reprocessed, or superseded;
- method, units, datum, processing level, or geometry corrected;
- observed/source/retrieval/release times were collapsed or corrected;
- interpreted/model-derived surface was published as observed measurement;
- public derivative exposes restricted footprint/detail or lacks a representation/redaction receipt where required;
- release manifest lacks policy decision where material, correction path, or rollback target;
- public API/UI/AI reads RAW/WORK/QUARANTINE or candidate records as public truth.

Rollback artifacts should include affected GeophysicalObservation IDs, source record IDs, survey IDs, geometry refs, product/raster/profile refs, method/unit refs, linked unit/structure/cross-section/hydrostratigraphic/resource refs, public derivative refs, release IDs, evidence refs, policy decisions, receipts, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| What is the accepted paired schema path and casing for `GeophysicalObservation`? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which instrument/method vocabulary is canonical for KFM? | NEEDS VERIFICATION | Geophysics steward, schema, and source review. |
| What footprint generalization thresholds are acceptable by source family and product type? | NEEDS VERIFICATION | Policy and release fixture review. |
| When does a processed grid remain `observed` with caveats versus become `modeled`? | NEEDS VERIFICATION | Source-role matrix and fixture review. |
| Which receipt family applies to modeled/rendered geophysical surfaces? | NEEDS VERIFICATION | RepresentationReceipt / RedactionReceipt / release review. |
| How should geophysical products support CrossSection without becoming CrossSection truth? | NEEDS VERIFICATION | Cross-contract schema and validation review. |

---

## Related contracts and docs

- `contracts/domains/geology/CrossSection.md` — interpretive section panels that may cite geophysical evidence.
- `contracts/domains/geology/GeologicUnit.md` — mapped unit claims that may cite geophysical evidence.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — Geology object-family reference and observation semantics.
- `schemas/contracts/v1/domains/geology/` — expected machine-shape home, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Create or verify paired schema and fixtures.
- [ ] Add validation for survey ID, instrument class, method, units, geometry fingerprint, processing level, source role, and evidence refs.
- [ ] Add anti-collapse tests for observation/model/unit/structure/cross-section/hydrology/hazards/resource/UI-summary distinctions.
- [ ] Add source profiles or SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released public-safe observation derivatives and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved path/schema/source-role drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
