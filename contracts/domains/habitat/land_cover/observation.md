<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-land-cover-observation
title: Land Cover Observation Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
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
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; habitat; land-cover; observation; LandCoverObservation; source-role-aware; source-vintage-aware; evidence-bound; valid-pixel-aware; release-gated
tags: [kfm, contracts, habitat, land_cover, observation, LandCoverObservation, land-cover-observation, class-scheme, source-vintage, valid-pixel-footprint, categorical-raster, continuous-raster, nlcd, landfire, gap, nwi, remote-sensing, evidence, source-role, policy, release, correction, rollback]
related:
  - ../README.md
  - ./class_scheme.md
  - ./crosswalk.md
  - ./change_summary.md
  - ./model_run_receipt.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/
  - ../../../../policy/domains/habitat/land_cover/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../fixtures/domains/habitat/land_cover/observation/
  - ../../../../tests/domains/habitat/land_cover/observation/
  - ../../../../pipelines/domains/habitat/land_cover/
  - ../../../../pipeline_specs/habitat/land_cover/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "Expanded from a thin scaffold into a Habitat land-cover LandCoverObservation semantic contract."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json, but it is still a PROPOSED scaffold with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "The land-cover sublane names the object family LandCoverObservation, while this requested file path and paired schema title use observation/Observation. This contract treats observation.md as the current semantic contract for LandCoverObservation unless a later ADR/schema decision says otherwise."
  - "A LandCoverObservation represents a categorical or continuous land-cover classification over a declared spatial and temporal scope. It is not a ClassSchemeProfile, CoverClassCrosswalk, LandCoverChangeSummary, ModelRunReceipt, LayerManifest, HabitatPatch, occurrence record, source activation decision, or release authority by itself."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Land Cover Observation — Habitat

> Semantic contract for `LandCoverObservation`: the Habitat land-cover object that records a governed categorical or continuous land-cover classification over a declared spatial and temporal scope, with explicit source role, class scheme, CRS, resolution, valid-pixel support, evidence refs, policy posture, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Object: LandCoverObservation" src="https://img.shields.io/badge/object-LandCoverObservation-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: observation not release" src="https://img.shields.io/badge/boundary-observation__not__release-critical">
</p>

`contracts/domains/habitat/land_cover/observation.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Observation classes](#observation-classes) · [Source-role rules](#source-role-rules) · [Raster and geometry rules](#raster-and-geometry-rules) · [Observation boundaries](#observation-boundaries) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/land_cover/observation.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Naming posture:** the land-cover sublane names the object family `LandCoverObservation`; the requested path and schema title use `Observation`. This file treats `observation.md` as the current semantic contract for `LandCoverObservation`, pending schema/ADR confirmation.  
> **Truth posture:** Habitat land-cover doctrine defines `LandCoverObservation` as a governed evidence object for categorical or continuous land-cover classification over declared spatial/temporal scope with source role, class scheme, CRS, resolution, valid-pixel support, and evidence references. Field-level schema shape, fixtures, validators, source registry records, policy files, release artifacts, API behavior, UI behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> A `LandCoverObservation` is a source-role-aware observation object. It is **not** a class scheme, crosswalk, change summary, model run receipt, source activation decision, HabitatPatch, species/plant occurrence claim, critical-habitat designation, public layer, release manifest, or AI/UI truth by itself.

---

## Meaning

`LandCoverObservation` records the fact that a source product, reviewed source derivative, or accepted observation artifact classifies a declared spatial scope using a declared land-cover class scheme over a declared temporal scope.

It answers:

- Which source family, source descriptor, source vintage, and source role support the observation?
- Which class scheme encodes the observation?
- What spatial extent, CRS, resolution, valid-pixel footprint, nodata handling, and geometry/raster posture apply?
- What temporal scope is represented: source time, observed/acquisition time, valid period, retrieval time, release time, and correction time?
- Which evidence, artifact digests, validation reports, policy decisions where material, release refs, correction notices, and rollback targets support downstream use?
- Which derived objects may cite it: `CoverClassCrosswalk`, `LandCoverChangeSummary`, `ModelRunReceipt`, `UncertaintySurface`, public layer descriptors, or Habitat/Patch synthesis?

A land-cover observation is evidence-bearing context. It can support later Habitat reasoning, but it must not become HabitatPatch quality, species presence, plant occurrence, critical habitat, hydrology, soil, hazards, agriculture, title, or release truth.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Observation meaning | `contracts/domains/habitat/land_cover/observation.md` | Owned here by request; object-family naming needs verification |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json` | CONFIRMED scaffold; field shape not enforced |
| Class scheme | `contracts/domains/habitat/land_cover/class_scheme.md` | Observation must cite a reviewed class scheme; it does not define it |
| Crosswalk | `contracts/domains/habitat/land_cover/crosswalk.md` | Crosswalks map between schemes; observations do not silently recode |
| Change summary | `contracts/domains/habitat/land_cover/change_summary.md` | Summaries compare observations; they do not replace them |
| Model run receipt | `contracts/domains/habitat/land_cover/model_run_receipt.md` | Receipts record modeled/derived runs; observed inputs remain separate |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Defines observation, source families, identity, lifecycle, raster handling, and public-surface boundaries |
| Source registry | `data/registry/sources/habitat/` | Source identity, source role, rights, cadence, activation |
| Policy | `policy/domains/habitat/land_cover/`, `policy/sensitivity/habitat/` | Source activation, thresholds, sensitive joins, release and exposure behavior |
| Fixtures and tests | `fixtures/domains/habitat/land_cover/observation/`, `tests/domains/habitat/land_cover/observation/` | PROPOSED / NEEDS VERIFICATION |
| Executable logic | `pipelines/domains/habitat/land_cover/` | Expected processing implementation home; not this contract |
| Declarative specs | `pipeline_specs/habitat/land_cover/` | Expected config home; not this contract |
| Release | `release/manifests/habitat/` | Expected release/correction/rollback home; release instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Observation` |
| Schema properties | Empty object |
| Required fields | None visible in the scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/sublanes/land_cover.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this contract is semantic guidance and review vocabulary only.

---

## Assertions

A reviewed `LandCoverObservation` should semantically assert:

1. **Observation identity** — deterministic identity from `source_id + class_scheme_id + spatial_scope + temporal_scope + normalized_digest`.
2. **Source identity** — SourceDescriptor, source family, source record, source role, rights, cadence, and citation.
3. **Class-scheme binding** — a reviewed `ClassSchemeProfile` and exact source scheme/version.
4. **Spatial scope** — raster extent, vector extent, analysis unit, tile extent, footprint, or declared geometry with CRS and resolution.
5. **Temporal scope** — source vintage, observed/acquisition period, valid period, retrieval time, release time, and correction time remain distinct.
6. **Valid-pixel support** — valid-pixel footprint, nodata mask, cloud/mask/no-data treatment, and footprint evidence are explicit.
7. **Observation values** — categorical class grid/vector, continuous/fractional surface, wetland class, vegetation type, or source-native classification posture.
8. **Uncertainty posture** — accuracy, valid-pixel footprint, source-vintage gap, crosswalk uncertainty where used, and confidence/quality flags.
9. **Evidence binding** — EvidenceRef/EvidenceBundle refs, source artifact digests, raster/vector/table refs, validation reports, and catalog/triplet refs.
10. **Governance state** — policy decision where material, review record, release refs, correction notices, supersession refs, and rollback targets.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating observation as class scheme | Class schemes define vocabularies; observations apply them to space/time. |
| Treating observation as crosswalk | Crosswalks map between schemes and require explicit review. |
| Treating observation as change summary | Change summaries compare two observations; observations do not summarize themselves. |
| Treating observation as model receipt | Receipts record transformed/model runs; observations remain source-role-bound inputs or reviewed outputs. |
| Treating modeled output as observed product | Modeled or derived land cover requires model-vs-observation label and receipt. |
| Treating observation as HabitatPatch | Patch sublane owns patch construction and quality. |
| Treating observation as species/plant occurrence | Fauna/Flora own occurrence truth. |
| Treating NWI as regulatory wetland delineation | NWI is wetland observation/context, not §404 determination. |
| Treating CDL as Habitat cover | CDL remains Agriculture-owned adjacency/context. |
| Treating public layer as observation | Layers are downstream carriers and need release artifacts. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM land-cover observation ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized observation digest. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `LandCoverObservation`, pending naming confirmation. |
| `observation_id` | Source/KFM observation identifier. |
| `observation_kind` | Categorical, continuous, fractional, wetland-class, vegetation-type, source-native, modeled, aggregate, or accepted enum. |
| `source_id` | Stable SourceDescriptor handle. |
| `source_descriptor_ref` | Source identity, role, rights, cadence, attribution, authority limits. |
| `source_family` | NLCD, LANDFIRE, GAP, NWI, NatureServe, state inventory, remote-sensing input, CDL adjacency, or accepted enum. |
| `source_role` | Observation product, modeled, adjacency, cross-reference, administrative, candidate, synthetic, or accepted KFM enum. |
| `source_record_ref` | Source-native raster, vector, table, scene, product, report, or API record. |
| `source_vintage` | Source product vintage/year/version. |
| `class_scheme_id` | Referenced ClassSchemeProfile ID. |
| `class_scheme_version` | Referenced class scheme version. |
| `crosswalk_ref` | Reviewed crosswalk ref if observation values were harmonized or translated. |
| `spatial_scope` | Declared spatial extent or analysis scope. |
| `spatial_scope_ref` | Geometry, grid, tile set, county/HUC/ecoregion/project ref, or source footprint ref. |
| `crs_source` | Source CRS. |
| `crs_analysis` | Analysis CRS. |
| `crs_delivery` | Web/public delivery CRS where relevant. |
| `resolution_source` | Native source resolution. |
| `resolution_analysis` | Analysis resolution. |
| `resolution_delivery` | Delivery/generalized resolution where relevant. |
| `raster_or_vector_ref` | Source or processed raster/vector artifact ref. |
| `artifact_digest` | Digest over source or processed observation artifact. |
| `valid_pixel_footprint_ref` | Valid-pixel footprint/mask evidence. |
| `nodata_policy_ref` | Nodata/unknown/unclassified handling ref. |
| `uncertainty_surface_refs` | Accuracy/uncertainty/footprint artifacts. |
| `source_time` | Source publication/assertion time. |
| `observed_time` | Imagery acquisition/product observation period. |
| `valid_time` | Period the classification claims to describe. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `release_time` | Public-safe release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `evidence_refs` | EvidenceRef links. |
| `evidence_bundle_refs` | EvidenceBundle refs behind the observation. |
| `validation_report_ref` | ValidationReport for schema, class scheme, source role, raster handling, geometry, evidence, and public safety. |
| `policy_decision_ref` | PolicyDecision where material. |
| `review_record_ref` | Steward review record. |
| `release_ref` | ReleaseManifest or PromotionDecision ref where publicly surfaced. |
| `correction_refs` | CorrectionNotice, supersession, replacement observation refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing source descriptor, undeclared class scheme, rights unknown, footprint gap, nodata drift, CRS mismatch, resolution mismatch, source-vintage gap, model/observation conflict, release missing. |

---

## Observation classes

| Class | Meaning | Default posture |
|---|---|---|
| `nlcd_categorical` | NLCD categorical land-cover observation. | Observation product; not regulatory or critical-habitat truth. |
| `landfire_evt` | LANDFIRE Existing Vegetation Type observation. | Vegetation observation/context; not fire-behavior prediction. |
| `landfire_bps_or_context` | LANDFIRE BPS/fire-disturbance context. | Context/model caveats required. |
| `gap_land_cover` | USGS GAP/NVC-aligned land-cover observation. | Observation product with source vintage/cadence caveats. |
| `nwi_wetland_class` | NWI wetland-class observation. | Wetland observation/context; not regulatory delineation. |
| `remote_sensing_continuous` | Continuous/fractional remote-sensing input or index. | Observation input; derived classification requires receipt. |
| `state_inventory_context` | State ecological inventory observation under review. | Source role/rights vary. |
| `cdl_adjacency` | USDA NASS CDL crop observation used as adjacency. | Agriculture-owned context; not Habitat cover. |
| `modeled_land_cover` | Derived/model output admitted as observation-like support. | Requires ModelRunReceipt and model-vs-observation label. |
| `candidate_record` | Unreviewed/imported observation. | WORK/QUARANTINE; no public edge. |
| `public_derivative` | Released generalized/summary/reference derivative. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source family / posture | Required handling |
|---|---|
| NLCD | Observation product; does not designate critical habitat or regulatory law. |
| LANDFIRE EVT | Vegetation observation; not fire-behavior prediction. |
| GAP | Land-cover/NVC-aligned observation; preserve sparse cadence and source version. |
| NWI | Wetland observation/context; not §404 regulatory delineation. |
| NatureServe/ecological systems | Cross-reference/control context; rights and sensitive joins NEED VERIFICATION. |
| State ecological inventories | Observation under review; authority class varies by state. |
| Remote-sensing indices | Observation input to derived land-cover/change analysis; modeled outputs need receipts. |
| USDA NASS CDL | Agriculture-owned crop observation adjacency only; do not reclassify as Habitat cover. |
| Watcher candidate | Proposed work/checkpoint only; watchers do not publish. |
| AI-proposed observation | Synthetic/candidate only; not evidence. |

---

## Raster and geometry rules

- Categorical observations use nearest-neighbor or mode-style handling when resampled; never bilinear.
- Continuous/fractional inputs may use bilinear or other methods only when statistics and method are declared.
- Native source resolution is preserved through `PROCESSED` unless a governed derivative is emitted later.
- Analysis CRS and web-delivery CRS stay separate.
- Valid-pixel footprints are evidence artifacts and remain separate from nodata.
- Nodata/unknown/unclassified values must remain consistent through overviews and derivatives.
- Source-vintage histogram shifts belong in promotion diff reports, not silent rebuilt layers.
- Reprojected, resampled, vectorized, generalized, or modeled products must carry manifests and receipts where material.

---

## Observation boundaries

```text
LandCoverObservation != ClassSchemeProfile
LandCoverObservation != CoverClassCrosswalk
LandCoverObservation != LandCoverChangeSummary
LandCoverObservation != ModelRunReceipt
LandCoverObservation != LayerManifest
LandCoverObservation != HabitatPatch
LandCoverObservation != species / plant occurrence
LandCoverObservation != critical-habitat designation
LandCoverObservation != Hydrology / Soil / Hazards / Agriculture truth
LandCoverObservation != release authority
LandCoverObservation != AI summary
```

Any derivative, join, model, renderer, or summary must preserve this boundary.

---

## Sensitivity and release

Land-cover observations are generally public-context inputs when source rights allow, but sensitivity rises when joined to rare species, sensitive habitats, private land, stewardship-sensitive, or exact occurrence records.

Rules:

- No source family is active until SourceDescriptor, source role, rights, fixtures, validators, and source-activation decision exist.
- Public observations require EvidenceRef/EvidenceBundle closure, validation, policy/review where material, release manifest, correction path, and rollback target.
- Sensitive joins to Fauna/Flora fail closed until geoprivacy transform, policy, review, release, and rollback support exist.
- Public tiles and cards must use explicit attribute include-lists and show source vintage, class scheme, and correction/stale state where material.
- Public clients use governed APIs and released artifacts, not RAW/WORK/QUARANTINE/candidate observations.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source rasters, vectors, scenes, tables, legends, footprints, and source terms are captured with source role, rights, sensitivity, citation, time, and hash. |
| WORK / QUARANTINE | Candidate observations normalize CRS, class scheme, valid-pixel footprint, nodata, identity, evidence, and rights; failures are quarantined with reason. |
| PROCESSED | Validated observations, uncertainty surfaces, valid-pixel masks, normalized rasters/vectors, and run receipts may emerge as reviewed candidates. |
| CATALOG / TRIPLET | Catalog records, EvidenceBundles, graph/triplet projections, and release candidates may be emitted only after proof/catalog closure. |
| RELEASE CANDIDATE | Generalized cover layers, comparison views, summaries, and public derivatives require release preflight, policy, validation, correction, and rollback support. |
| PUBLISHED | Released public-safe layers and summaries are served through governed APIs and manifests. |
| CORRECTED / SUPERSEDED | Source update, source-vintage correction, class-scheme correction, footprint correction, geometry correction, policy change, or artifact digest change triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand the paired schema beyond an empty scaffold.
- [ ] Decide whether `LandCoverObservation` or `Observation` is the accepted schema/object-family name.
- [ ] Add valid fixtures for NLCD, LANDFIRE EVT, GAP, NWI, remote-sensing continuous input, state inventory, CDL adjacency, modeled land cover, candidate record, and public derivative examples.
- [ ] Add invalid fixtures for missing source descriptor, missing source role, undeclared class scheme, class-scheme mismatch, missing valid-pixel footprint, nodata drift, categorical bilinear resampling, source-vintage collapse, modeled output labeled observed, sensitive join without geoprivacy receipt, missing EvidenceBundle, missing release manifest, and missing rollback target.
- [ ] Add validator checks for source role, class scheme, CRS/resolution, valid-pixel footprint, nodata, source/observed/valid/retrieval/release/correction times, evidence refs, source activation, sensitivity, and release refs.
- [ ] Add tests proving observations cannot substitute for class schemes, crosswalks, summaries, model receipts, layer manifests, HabitatPatch, occurrence, or release truth.
- [ ] Add release tests proving public clients consume released observations or derivatives only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Source, role, class scheme, scope, times, footprint, evidence, validation, policy, release, and rollback all resolve | `ANSWER` / public-safe observation derivative may be shown |
| Evidence, source role, rights, class scheme, geometry, footprint, sensitivity, or release support is incomplete | `ABSTAIN` / `HOLD` |
| Source role collapses, modeled output is labeled observed, sensitive detail leaks, or release is bypassed | `DENY` |
| Schema, validator, source read, raster read, artifact digest, evidence lookup, policy, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current contract scaffold | Confirms the target file existed as a scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms schema path and current empty schema posture. | Does not prove field-level validation. |
| Habitat land-cover sublane doc | Defines `LandCoverObservation`, class schemes, valid-pixel footprints, source families, source-role boundaries, identity rule, lifecycle, watcher discipline, raster handling, model-vs-observation labels, map products, and cross-lane constraints. | Many field realizations and paths remain PROPOSED. |
| ClassScheme, Crosswalk, ChangeSummary, and ModelRunReceipt contracts | Adjacent semantic contracts that define neighboring object boundaries. | Recent contract content is semantic documentation, not schema enforcement. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | It is an authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized observation weakens source integrity, hides source-role or temporal gaps, leaks sensitive joined context, or makes source/derived products appear more authoritative than their evidence and release state allow.

Rollback triggers include:

- source observation, raster, vector, scene, footprint, source vintage, class scheme, source role, or rights are corrected;
- categorical raster was bilinear-resampled or nodata/valid-pixel handling corrupted;
- observed, modeled, aggregate, adjacency, regulatory, or candidate roles were collapsed;
- CDL or another adjacent-domain product was re-owned as Habitat cover;
- NWI was treated as regulatory wetlands delineation;
- observation was treated as HabitatPatch, species/plant occurrence, critical habitat, Hydrology, Soil, Hazards, Agriculture, title, release, or AI truth;
- sensitive join published without geoprivacy/policy/release support;
- public API/UI/AI used RAW/WORK/QUARANTINE/candidate observations as public truth.

Rollback artifacts should include affected observation IDs, source descriptor refs, source vintages, class scheme refs, footprint refs, raster/vector artifact refs, artifact digests, evidence refs, validation reports, policy decisions, release refs, correction notices, rollback cards, replacement observations, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is the canonical object name `LandCoverObservation` or `Observation`? | NEEDS VERIFICATION | Habitat contract/schema naming review. |
| Which fields must be required in `observation.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Which source families/vintages should be activated first? | NEEDS VERIFICATION | SourceDescriptor activation review. |
| Which observation values are safe for public tiles and Focus Mode cards? | NEEDS VERIFICATION | Attribute include-list, policy, and release fixture review. |
| How should modeled land-cover outputs be admitted without becoming observed products? | NEEDS VERIFICATION | ModelRunReceipt + validator review. |
| How should sensitive joins invalidate or redact public observation derivatives? | NEEDS VERIFICATION | Policy/geoprivacy/release design. |

---

## Related contracts and docs

- `contracts/domains/habitat/land_cover/class_scheme.md` — class schemes used by observations.
- `contracts/domains/habitat/land_cover/crosswalk.md` — reviewed mappings between schemes.
- `contracts/domains/habitat/land_cover/change_summary.md` — summaries comparing observations.
- `contracts/domains/habitat/land_cover/model_run_receipt.md` — receipts for modeled/derived land-cover outputs.
- `docs/domains/habitat/sublanes/land_cover.md` — land-cover sublane doctrine and object-family context.
- `docs/domains/habitat/SOURCE_FAMILIES.md` — Habitat source-family role, rights, and sensitivity posture.
- `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json` — confirmed scaffold schema, pending expansion.
- `policy/domains/habitat/land_cover/` — expected source-role/materiality/public-safety policy home, pending verification.
- `release/manifests/habitat/` — expected release/rollback home, pending verification.

[Back to top](#top)
