<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-land-cover-observation-top-level
title: Land Cover Observation Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; COMPATIBILITY_ALIAS; CONFLICTED duplicate semantic home; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Observation steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-22
updated: 2026-06-22
policy_label: public-with-gates; semantic-contract; habitat; land-cover; LandCoverObservation; compatibility-alias; source-role-aware; source-vintage-aware; valid-pixel-aware; evidence-bound; release-gated
tags: [kfm, contracts, habitat, land-cover, land_cover_observation, LandCoverObservation, observation, class-scheme, valid-pixel-footprint, categorical-raster, continuous-raster, source-role, source-vintage, evidence, policy, release, correction, rollback, compatibility-alias]
related:
  - ./README.md
  - ./land_cover/observation.md
  - ./land_cover/class_scheme.md
  - ./land_cover/crosswalk.md
  - ./land_cover/change_summary.md
  - ./land_cover/model_run_receipt.md
  - ./land_cover/uncertainty.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./domain_validation_report.md
  - ./habitat_patch.md
  - ./ecological_system.md
  - ./SuitabilityModel.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../schemas/contracts/v1/domains/habitat/land_cover_observation.schema.json
  - ../../../schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json
  - ../../../policy/domains/habitat/land_cover/
  - ../../../policy/sensitivity/habitat/
  - ../../../fixtures/domains/habitat/land_cover/observation/
  - ../../../tests/domains/habitat/land_cover/observation/
  - ../../../data/registry/sources/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a top-level scaffold at contracts/domains/habitat/land_cover_observation.md."
  - "This top-level path is currently referenced by schemas/contracts/v1/domains/habitat/land_cover_observation.schema.json."
  - "A fuller nested semantic contract already exists at contracts/domains/habitat/land_cover/observation.md. This file treats the top-level path as a compatibility/schema-aligned contract until schema-home/path migration is resolved. Do not treat both files as independent competing authorities."
  - "Both observed schema homes remain PROPOSED scaffolds with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "LandCoverObservation is a governed land-cover evidence object, not a HabitatPatch, not a suitability score, not species occurrence truth, not regulatory critical habitat, not a public layer by itself, and not release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Land Cover Observation Contract — Habitat

> Compatibility semantic contract for `LandCoverObservation`: the Habitat land-cover evidence object that records a governed categorical or continuous land-cover classification over declared spatial and temporal scope, with source role, class scheme, CRS/resolution, valid-pixel support, evidence, policy, release, correction, and rollback boundaries visible.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: LandCoverObservation" src="https://img.shields.io/badge/object-LandCoverObservation-blue">
  <img alt="Schema: top-level scaffold" src="https://img.shields.io/badge/schema-top--level_scaffold-orange">
  <img alt="Path: compatibility alias" src="https://img.shields.io/badge/path-compatibility__alias-lightgrey">
  <img alt="Boundary: observation not release" src="https://img.shields.io/badge/boundary-observation__not__release-critical">
</p>

`contracts/domains/habitat/land_cover_observation.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Path and schema posture](#path-and-schema-posture) · [Observation vs nearby objects](#observation-vs-nearby-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Source-role rules](#source-role-rules) · [Raster and geometry rules](#raster-and-geometry-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract / compatibility alias  
> **Requested contract path:** `contracts/domains/habitat/land_cover_observation.md`  
> **Top-level schema path:** `schemas/contracts/v1/domains/habitat/land_cover_observation.schema.json`  
> **Nested semantic contract already present:** `contracts/domains/habitat/land_cover/observation.md`  
> **Nested schema path:** `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json`  
> **Truth posture:** Habitat doctrine confirms `LandCoverObservation` as a Habitat land-cover object family. The top-level and nested schema homes are both scaffolds, and the duplicate path split is **CONFLICTED / NEEDS VERIFICATION** before either path is promoted as stable authority.

> [!CAUTION]
> This file exists because the top-level schema scaffold points here. It must not create a competing semantic authority against `contracts/domains/habitat/land_cover/observation.md`. Resolve by ADR, migration note, schema-pointer update, compatibility policy, or deprecation plan before promotion.

---

## Meaning

`LandCoverObservation` records a governed land-cover classification or measurement over a declared spatial and temporal scope. It may be categorical, continuous, fractional, wetland-class, vegetation-type, raster-backed, vector-backed, source-native, or reviewed derivative, but it remains an **observation/evidence object** until downstream evidence closure, review, policy, and release state permit use.

It answers:

- Which source family, source descriptor, source artifact, source vintage, rights posture, and source role support the observation?
- Which `ClassSchemeProfile` encodes the source class values or continuous value semantics?
- Which spatial support applies: extent, footprint, CRS, resolution, valid-pixel mask, nodata handling, analysis unit, or delivery derivative?
- Which temporal scopes remain distinct: source time, observed/acquisition time, valid time, retrieval time, release time, and correction time?
- Which downstream objects may cite it without replacing it: crosswalks, change summaries, uncertainty surfaces, model receipts, ecological systems, habitat patches, suitability models, or public layers?

A land-cover observation may support Habitat reasoning, but it does not itself assert habitat quality, species presence, plant occurrence, regulatory critical habitat, land-title status, management instruction, or public release.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Top-level semantic contract | `contracts/domains/habitat/land_cover_observation.md` | Compatibility/schema-aligned contract requested here |
| Nested semantic contract | `contracts/domains/habitat/land_cover/observation.md` | Expanded land-cover-specific semantic contract already present |
| Top-level schema | `schemas/contracts/v1/domains/habitat/land_cover_observation.schema.json` | CONFIRMED scaffold pointing to this file |
| Nested schema | `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json` | CONFIRMED scaffold for nested land-cover contract |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Defines object family, source roles, identity, lifecycle, raster discipline, and public boundaries |
| Class scheme | `contracts/domains/habitat/land_cover/class_scheme.md` | Observation must cite a reviewed class scheme; it does not define it |
| Crosswalk | `contracts/domains/habitat/land_cover/crosswalk.md` | Crosswalks map between class schemes; observations do not silently recode |
| Change summary | `contracts/domains/habitat/land_cover/change_summary.md` | Summaries compare observations; they do not replace them |
| Model run receipt | `contracts/domains/habitat/land_cover/model_run_receipt.md` | Receipts record model/derived runs; observations remain separate input facts |
| Uncertainty | `contracts/domains/habitat/land_cover/uncertainty.md` | Accuracy/footprint/vintage/crosswalk uncertainty support |
| Source registry | `data/registry/sources/habitat/` | Source identity, source role, rights, cadence, activation |
| Policy | `policy/domains/habitat/land_cover/`, `policy/sensitivity/habitat/` | Source activation, thresholds, sensitive joins, exposure behavior |
| Release | `release/` / `release/manifests/habitat/` | Release/correction/rollback authority; instances NEEDS VERIFICATION |

---

## Path and schema posture

| Item | Current evidence | Contract posture |
|---|---|---|
| Requested top-level contract | `contracts/domains/habitat/land_cover_observation.md` existed as a scaffold. | Expanded here. |
| Top-level schema | `schemas/contracts/v1/domains/habitat/land_cover_observation.schema.json` exists. | CONFIRMED scaffold; points to this file. |
| Nested contract | `contracts/domains/habitat/land_cover/observation.md` exists and is already expanded. | Existing semantic authority candidate. |
| Nested schema | `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json` exists. | CONFIRMED scaffold; nested home. |
| Field-level validation | Both schemas observed as scaffolds. | NEEDS VERIFICATION. |
| Canonical path decision | Top-level vs nested contract/schema homes conflict. | CONFLICTED / NEEDS VERIFICATION. |

> [!WARNING]
> Do not promote both top-level `land_cover_observation.md` and nested `land_cover/observation.md` as separate authorities. The safest current posture is: this file is a compatibility/schema-aligned surface, while the nested file carries the fuller land-cover sublane semantics, pending ADR/schema migration review.

---

## Observation vs nearby objects

| Object / artifact | What it owns | Boundary |
|---|---|---|
| `LandCoverObservation` | Source-role-aware land-cover classification over declared space/time. | This contract and nested observation contract. |
| `ClassSchemeProfile` | Class scheme namespace/version/legend. | Observation cites it; does not own it. |
| `CoverClassCrosswalk` | Reviewed mapping between class schemes. | Not a silent renderer transform. |
| `LandCoverChangeSummary` | Public-safe comparison between observations. | Derived summary; not source observation. |
| `UncertaintySurface` | Accuracy, footprint, vintage gap, crosswalk uncertainty. | Companion evidence, not observation value. |
| `ModelRunReceipt` | Run record for model/generalization/reclassification. | Required for model-derived outputs. |
| `HabitatPatch` | Discrete habitat unit identity and geometry. | Built downstream; not land-cover observation. |
| `HabitatQualityScore` | Scored habitat quality/condition/suitability. | Consumes observations; not observation itself. |
| `SuitabilityModel` | Modeled suitability surface/score family. | Model output, not observed land cover. |
| Regulatory critical habitat | Authority designation. | Not land-cover observation. |
| Fauna/Flora occurrence | Species/plant occurrence truth. | Land-cover may be context only. |
| Map tile / popup / AI summary | Delivery or interpretation surface. | Never root truth. |

---

## Assertions

A reviewed `LandCoverObservation` should semantically assert:

1. **Observation identity** — deterministic identity from `source_id + class_scheme_id + spatial_scope + temporal_scope + normalized_digest`.
2. **Source identity** — SourceDescriptor, source family, source record, source role, rights, cadence, and citation.
3. **Class-scheme binding** — reviewed class scheme/profile and exact source scheme/version.
4. **Spatial scope** — raster extent, vector extent, analysis unit, tile extent, footprint, or declared geometry with CRS and resolution.
5. **Temporal scope** — source vintage, observed/acquisition period, valid period, retrieval time, release time, and correction time remain distinct.
6. **Valid-pixel support** — valid-pixel footprint, nodata mask, cloud/no-data treatment, and footprint evidence are explicit.
7. **Observation values** — categorical class grid/vector, continuous/fractional surface, wetland class, vegetation type, or source-native classification posture.
8. **Uncertainty posture** — classification accuracy, valid-pixel footprint, source-vintage gap, crosswalk uncertainty where used, and confidence/quality flags.
9. **Evidence binding** — EvidenceRef/EvidenceBundle refs, source artifact digests, raster/vector/table refs, validation reports, and catalog/triplet refs.
10. **Governance state** — policy decision where material, review record, release refs, correction notices, supersession refs, and rollback targets.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating land cover as habitat assertion | Land-cover class is source classification, not Habitat truth by itself. |
| Treating observation as HabitatPatch | Patch delineation is downstream and derived. |
| Treating observation as suitability score | Suitability/quality scoring is separate. |
| Treating observation as species/plant occurrence | Fauna/Flora own occurrence truth. |
| Treating NWI as regulatory wetlands delineation | NWI is observation context, not §404 delineation. |
| Treating NLCD/LANDFIRE/GAP as regulatory critical habitat | Source-role collapse. |
| Treating CDL as Habitat land-cover truth | Agriculture owns crop classification; Habitat may consume context only. |
| Treating crosswalk as silent recode | Crosswalk must be reviewed, citable, and versioned. |
| Treating renderer/tile as evidence | Tiles and styles are delivery surfaces. |
| Treating schema scaffold as validator | Current schema fields are not implemented. |
| Treating watcher output as publication | Watchers emit candidate work/receipts; promotion is governed. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the confirmed scaffold schemas.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM land-cover observation ID. |
| `version` | Object/contract version. |
| `spec_hash` | Normalized digest over observation-relevant content. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `LandCoverObservation`. |
| `source_descriptor_ref` | SourceDescriptor identity, role, rights, cadence, citation. |
| `source_record_ref` | Source-native artifact/table/raster/vector/API/report ref. |
| `source_family` | NLCD, LANDFIRE, GAP, NWI, remote sensing, field survey, state inventory, or accepted enum. |
| `source_role` | observation, context, model, derivative, candidate, synthetic, authority-context, or accepted enum. |
| `class_scheme_ref` | Reviewed class scheme/profile. |
| `class_value` / `continuous_value` | Source-native class or continuous/fractional value representation. |
| `spatial_scope_ref` | Declared extent/footprint/analysis unit. |
| `crs` | Analysis CRS. |
| `delivery_crs` | Delivery CRS where public layer exists. |
| `native_resolution` | Native source resolution. |
| `processed_resolution` | Processed/generalized derivative resolution, if any. |
| `valid_pixel_footprint_ref` | Valid-pixel mask/footprint ref. |
| `nodata_policy_ref` | Nodata/mask treatment. |
| `uncertainty_refs` | Accuracy/footprint/vintage/crosswalk uncertainty. |
| `source_time` | Source publication/vintage time. |
| `observed_time` | Imagery/acquisition/observation period. |
| `valid_time` | Period classification claims to describe. |
| `retrieval_time` | Time KFM retrieved source. |
| `release_time` | Time of governed release, if any. |
| `correction_time` | Time correction applies, if any. |
| `evidence_refs` / `evidence_bundle_refs` | Evidence closure refs behind consequential use. |
| `validation_report_ref` | Validation report for schema/geometry/raster/policy checks. |
| `policy_decision_ref` | PolicyDecision where material. |
| `review_record_ref` | Steward/reviewer state. |
| `release_ref` | ReleaseManifest/PromotionDecision ref if public. |
| `correction_refs` | CorrectionNotice/supersession refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing role, missing class scheme, invalid CRS, missing footprint, stale source, sensitive join, release missing. |

---

## Source-role rules

| Source family / artifact | Normal role | Contract discipline |
|---|---|---|
| NLCD | observation product | Not regulatory law; not critical habitat. |
| LANDFIRE EVT/BPS/FDist | vegetation/fuel-context observation or model/context depending product | Keep exact role/version visible. |
| USGS GAP land cover | categorical observation/context | Keep class scheme and vintage visible. |
| NWI wetlands | wetland-class observation | Not §404 regulatory delineation. |
| NatureServe ecological systems | context/crosswalk authority depending license and activation | Rights and sensitivity review required. |
| State ecological inventories | observation under review/context | Authority class varies; source role declared, not inferred. |
| Remote sensing indices | observation input to derivative | Not land-cover class by itself unless reviewed/classified. |
| USDA NASS CDL | Agriculture-owned crop observation / Habitat adjacency context | Not reclassified silently into Habitat cover. |
| AI-generated classifier | synthetic/candidate/model | Not source truth; requires review, receipt, evidence, and validation. |

---

## Raster and geometry rules

- Categorical rasters use nearest or mode resampling; never bilinear.
- Continuous/fractional rasters may use bilinear only with declared statistics and uncertainty posture.
- Analysis CRS and web-delivery CRS stay separate.
- Native source resolution, processed resolution, and public generalized resolution are not interchangeable.
- Nodata handling must stay consistent through overviews and derived layers.
- Valid-pixel footprints are evidence artifacts, not rendering conveniences.
- Histogram shifts between vintages belong in promotion diff reports, not silent layer rebuilds.
- Public layers are released derivatives; source rasters and work products do not become public by style toggle.

---

## Sensitivity and release

Land-cover observations are generally public-source-friendly, but they become sensitive when joined to rare-species occurrences, rare plants, sensitive habitats, stewardship zones, private/local restricted inventories, archaeological/cultural resources, infrastructure, or other restricted context.

Rules:

- Exact sensitive joins fail closed.
- Public land-cover layers must be released public-safe derivatives.
- Public products must preserve source role and source-vintage badges/citations.
- Style filters are not privacy controls.
- A land-cover observation must not be used to reconstruct sensitive exact location details.
- AI/Focus Mode may summarize released EvidenceBundles only and must `ABSTAIN` or `DENY` when evidence, policy, source role, sensitivity, or release state blocks the request.

---

## Lifecycle

| Phase | LandCoverObservation handling |
|---|---|
| RAW | Source payload/ref captured with source role, rights, sensitivity, citation, source time, retrieval time, and hash. |
| WORK / QUARANTINE | CRS, class scheme, valid-pixel footprint, nodata, identity, evidence, rights, and source role normalized; unresolved issues held. |
| PROCESSED | Validated observation object, normalized raster/vector, uncertainty, footprint, validation report, and evidence refs are emitted. |
| CATALOG / TRIPLET | Catalog records and EvidenceBundles reference observation claims; derived graph/triplet views remain downstream carriers. |
| RELEASE CANDIDATE | Public-safe layer/summary candidates bind manifests, digests, policy decisions, correction path, and rollback target. |
| PUBLISHED | Released public-safe artifacts appear only through governed APIs, layer manifests, Evidence Drawer, Focus Mode, and reports. |
| CORRECTED / SUPERSEDED | New source vintage, class scheme correction, geometry/raster correction, footprint correction, rights change, policy change, or release withdrawal triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve whether top-level `land_cover_observation.md` or nested `land_cover/observation.md` is canonical, or declare a compatibility/deprecation rule.
- [ ] Expand `schemas/contracts/v1/domains/habitat/land_cover_observation.schema.json` beyond scaffold if the top-level path remains supported.
- [ ] Confirm whether `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json` supersedes the top-level schema or remains separate.
- [ ] Add schema-required fields for source descriptor, source role, class scheme, spatial scope, temporal scope, valid-pixel footprint, evidence refs, validation, policy, release, correction, and rollback.
- [ ] Add valid fixtures for NLCD, LANDFIRE, GAP, NWI, remote-sensing continuous surface, field inventory, and public-safe generalized derivative.
- [ ] Add invalid fixtures for missing source role, missing class scheme, bilinear categorical resampling, missing valid-pixel footprint, source-role collapse, CDL-as-Habitat truth, sensitive exact public join, and release without manifest/rollback.
- [ ] Confirm public UI/API layers label land-cover source role, class scheme, source vintage, uncertainty/valid-pixel caveats, and release state.
- [ ] Confirm watchers emit candidate work/receipts only and never publish directly.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Source, class scheme, spatial/temporal scope, footprint, evidence, policy, release, correction, and rollback resolve | `ANSWER` / public-safe observation may support a claim |
| Source role, rights, class scheme, footprint, evidence, sensitivity, release, or rollback is incomplete | `ABSTAIN` / `HOLD` |
| Role collapse, sensitive leak, candidate public path, invalid categorical resampling, renderer-as-truth, or release bypass would occur | `DENY` |
| Schema, validator, source read, digest, evidence lookup, policy lookup, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Target scaffold | Confirms top-level `land_cover_observation.md` existed as scaffold before replacement. | Does not prove contract maturity. |
| Top-level schema scaffold | Confirms `land_cover_observation.schema.json` path and that it points to this contract path. | Does not prove field-level validation. |
| Nested observation contract | Confirms a fuller semantic contract already exists under `land_cover/observation.md`. | Creates path/authority drift that remains unresolved. |
| Land-cover sublane doc | Confirms `LandCoverObservation`, source families, source-role rules, identity basis, lifecycle, raster handling, and ownership boundaries. | Implementation and path placement remain partly PROPOSED. |
| Habitat README | Confirms object-family spine and lifecycle/release/sensitivity posture. | Field realization remains PROPOSED. |
| User-provided authoring role | Requires evidence-grounded repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when this contract or a released observation weakens source-role integrity, class-scheme integrity, evidence support, valid-pixel support, sensitivity posture, or release governance.

Rollback triggers include canonical path conflict unresolved during promotion; source-role correction; source-vintage correction; class-scheme correction; CRS/resolution correction; nodata or valid-pixel footprint correction; artifact digest mismatch; sensitive exact join exposure; categorical raster resampled incorrectly; land-cover source presented as HabitatPatch, suitability, species occurrence, critical habitat, or release authority; candidate observation appearing in public API/UI/AI path; watcher-as-publisher; tile/popup/vector-index/AI-as-truth; or missing release/correction/rollback refs.

Rollback artifacts should include affected observation IDs, source refs, class-scheme refs, spatial/temporal scopes, source/native artifact digests, processed artifact digests, valid-pixel footprint refs, uncertainty refs, evidence refs, validation reports, policy decisions, release refs, correction notices, rollback cards, replacement observations, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is the canonical contract path top-level `land_cover_observation.md` or nested `land_cover/observation.md`? | CONFLICTED / NEEDS VERIFICATION | Habitat steward + schema steward + ADR/migration note. |
| Should the top-level schema remain as compatibility alias, redirect to nested schema, or be deprecated? | NEEDS VERIFICATION | Schema migration PR. |
| Which exact source-role enum values are accepted for land-cover sources? | NEEDS VERIFICATION | Source-role/schema/policy review. |
| Which class schemes are activated first: NLCD, LANDFIRE, GAP, NWI, state inventories, remote-sensing indices? | NEEDS VERIFICATION | Source activation decision and SourceDescriptor review. |
| Where do land-cover watchers, no-op receipts, and drift reports live? | NEEDS VERIFICATION | Pipeline/runbook review. |
| Which public derivatives are allowed: COG, PMTiles, generalized polygons, change summaries, histograms? | NEEDS VERIFICATION | Release manifest and layer descriptor review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contract root.
- [`./land_cover/observation.md`](./land_cover/observation.md) — expanded nested LandCoverObservation contract; current semantic authority candidate.
- [`./land_cover/class_scheme.md`](./land_cover/class_scheme.md) — class-scheme contract.
- [`./land_cover/crosswalk.md`](./land_cover/crosswalk.md) — cover-class crosswalk contract.
- [`./land_cover/change_summary.md`](./land_cover/change_summary.md) — land-cover change summary contract.
- [`./land_cover/model_run_receipt.md`](./land_cover/model_run_receipt.md) — model-run receipt semantics.
- [`./land_cover/uncertainty.md`](./land_cover/uncertainty.md) — land-cover uncertainty semantics.
- [`./domain_observation.md`](./domain_observation.md) — domain observation envelope.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — identity and anti-collapse support.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — layer/view descriptor support.
- [`./habitat_patch.md`](./habitat_patch.md) — downstream patch object contract.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat lane doctrine.
- [`../../../docs/domains/habitat/sublanes/land_cover.md`](../../../docs/domains/habitat/sublanes/land_cover.md) — land-cover sublane doctrine.
- [`../../../schemas/contracts/v1/domains/habitat/land_cover_observation.schema.json`](../../../schemas/contracts/v1/domains/habitat/land_cover_observation.schema.json) — top-level schema scaffold pointing here.
- [`../../../schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json`](../../../schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json) — nested schema scaffold.

[Back to top](#top)
