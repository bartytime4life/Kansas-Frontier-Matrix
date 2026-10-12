<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-land-cover-change-summary
title: Land Cover Change Summary Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
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
policy_label: public-with-gates; semantic-contract; habitat; land-cover; change-summary; source-vintage-aware; threshold-governed; evidence-bound; release-gated; public-safe-derivative
tags: [kfm, contracts, habitat, land_cover, change_summary, LandCoverChangeSummary, land-cover-change, change-rate, materiality, threshold-profile, source-vintage, class-scheme, public-safe, evidence, source-role, policy, release, correction, rollback]
related:
  - ../../README.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/change_summary.schema.json
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/
  - ../../../../policy/domains/habitat/land_cover/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../fixtures/domains/habitat/land_cover/change_summary/
  - ../../../../tests/domains/habitat/land_cover/change_summary/
  - ../../../../pipelines/domains/habitat/land_cover/
  - ../../../../pipeline_specs/habitat/land_cover/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "Expanded from a thin scaffold into a Habitat LandCoverChangeSummary semantic contract."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/land_cover/change_summary.schema.json, but it is still a PROPOSED scaffold with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "LandCoverChangeSummary means a public-safe summary of net/relative change between two LandCoverObservation records over an analysis unit. It does not replace the observations, source rasters, source descriptors, thresholds, policy decisions, release manifests, EvidenceBundles, or map layers."
  - "Default materiality thresholds and county analysis-unit anchoring are inherited from the land-cover sublane doctrine as PROPOSED field realization; threshold policy and validator behavior remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Land Cover Change Summary — Habitat

> Semantic contract for `LandCoverChangeSummary`: the Habitat land-cover object that summarizes net and relative change between two governed `LandCoverObservation` records over a declared analysis unit, using a versioned threshold profile, source-vintage discipline, evidence closure, policy review, correction, and rollback support.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Object: LandCoverChangeSummary" src="https://img.shields.io/badge/object-LandCoverChangeSummary-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: summary not source raster" src="https://img.shields.io/badge/boundary-summary__not__source__raster-critical">
</p>

`contracts/domains/habitat/land_cover/change_summary.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Summary classes](#summary-classes) · [Materiality and thresholds](#materiality-and-thresholds) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/land_cover/change_summary.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/land_cover/change_summary.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Truth posture:** Habitat land-cover doctrine defines `LandCoverChangeSummary` as a public-safe summary of change between two `LandCoverObservation` objects over an analysis unit. Field-level schema shape, fixtures, validators, threshold policy files, source registry records, release artifacts, API behavior, UI behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> A `LandCoverChangeSummary` is a derived summary. It is **not** the source raster, not a `LandCoverObservation`, not a class-scheme crosswalk, not a HabitatPatch, not a species/plant occurrence claim, not a critical-habitat designation, not a policy decision, not a release manifest, and not a public layer by itself.

---

## Meaning

`LandCoverChangeSummary` records a governed, public-safe comparison between two versioned land-cover observations over a declared analysis unit.

It answers:

- Which two `LandCoverObservation` records are being compared?
- Which source families, source vintages, class schemes, valid-pixel footprints, CRS/resolution assumptions, and evidence refs support the comparison?
- Which analysis unit was used: county, HUC, ecoregion, grid, project area, or another reviewed unit?
- Which threshold profile decided whether a change was material?
- Which per-class area, percentage, gain/loss, transition, and uncertainty summaries are public-safe?
- Which validation report, policy decision where material, release manifest, correction notice, and rollback target govern downstream use?

This contract is deliberately narrower than land-cover processing. It defines the meaning of the **summary object** after source observations and source-vintage comparisons have been normalized and reviewed.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Change-summary meaning | `contracts/domains/habitat/land_cover/change_summary.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/land_cover/change_summary.schema.json` | CONFIRMED scaffold; field shape not enforced |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Defines sublane scope, terms, object family, lifecycle, thresholds, and public products |
| Source registry | `data/registry/sources/habitat/` | Source identity, role, rights, cadence, activation |
| Threshold policy | `policy/domains/habitat/land_cover/` | Expected home for versioned materiality thresholds; contents NEEDS VERIFICATION |
| Sensitivity policy | `policy/sensitivity/habitat/` | Expected home for sensitive joins and public-safe exposure; contents NEEDS VERIFICATION |
| Fixtures and tests | `fixtures/domains/habitat/land_cover/change_summary/`, `tests/domains/habitat/land_cover/change_summary/` | PROPOSED / NEEDS VERIFICATION |
| Executable logic | `pipelines/domains/habitat/land_cover/` | Expected processing home; not this contract |
| Declarative specs | `pipeline_specs/habitat/land_cover/` | Expected config home; not this contract |
| Release | `release/manifests/habitat/` | Expected release/correction/rollback home; release instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/land_cover/change_summary.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Change Summary` |
| Schema properties | Empty object |
| Required fields | None visible in the scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/sublanes/land_cover.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this contract is semantic guidance and review vocabulary only.

---

## Assertions

A reviewed `LandCoverChangeSummary` should semantically assert:

1. **Summary identity** — deterministic ID from source observations, analysis unit, threshold profile, class scheme/crosswalk posture, and normalized digest.
2. **Observation pair** — `from_obs_id` and `to_obs_id` are distinct reviewed `LandCoverObservation` records.
3. **Source-vintage discipline** — source time, observed/valid period, retrieval time, release time, and correction time remain distinct.
4. **Analysis unit** — county, HUC, ecoregion, project boundary, grid, or reviewed unit with geometry/version support.
5. **Class-scheme compatibility** — direct same-scheme comparison or explicit reviewed crosswalk; never silent recode.
6. **Valid-pixel support** — nodata, cloud/mask gaps, source footprint, and valid-pixel footprint are accounted for.
7. **Materiality posture** — threshold profile ID and pass/warn/fail state are explicit.
8. **Change values** — area and percentage deltas by class, transition matrix where supported, gain/loss summaries, and uncertainty caveats.
9. **Evidence closure** — EvidenceRef/EvidenceBundle, validation report, source descriptors, artifact digests, and catalog/triplet refs resolve before public claims.
10. **Release and rollback posture** — release manifest, correction path, rollback target, stale-state rule, and public-safe display behavior are present for PUBLISHED use.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating the summary as a source raster | Source rasters remain RAW/PROCESSED artifacts with their own digests and provenance. |
| Treating summary as `LandCoverObservation` | The summary compares observations; it does not replace them. |
| Treating change as habitat quality | Suitability/patch/ecological-system contracts own those claims. |
| Treating land-cover change as species occurrence | Fauna/Flora own occurrence truth; cover is context only. |
| Treating NWI/NLCD/LANDFIRE/GAP classes as interchangeable | Class schemes require explicit crosswalks and caveats. |
| Treating county thresholds as universal | Threshold generalization beyond county is PROPOSED / NEEDS VERIFICATION. |
| Treating watcher output as publication | Watchers emit proposed work records/checkpoints; they do not publish. |
| Treating a rendered histogram/card as evidence | UI summaries are downstream carriers; EvidenceBundle carries support. |
| Treating public release as implied by low sensitivity | ReleaseManifest, policy/review, correction, and rollback support are still required. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM change-summary ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized summary digest. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `LandCoverChangeSummary`. |
| `summary_id` | Source/KFM summary identifier. |
| `from_obs_id` | Earlier/baseline LandCoverObservation ID. |
| `to_obs_id` | Later/comparison LandCoverObservation ID. |
| `from_source_vintage` | Source vintage for the baseline observation. |
| `to_source_vintage` | Source vintage for the comparison observation. |
| `analysis_unit_id` | County/HUC/ecoregion/grid/project unit ID. |
| `analysis_unit_kind` | County, HUC, ecoregion, grid, project, custom, or accepted enum. |
| `analysis_unit_geometry_ref` | Geometry/version of the analysis unit. |
| `class_scheme_ref` | Shared class scheme or comparison scheme ref. |
| `crosswalk_ref` | Reviewed crosswalk if schemes differ. |
| `valid_pixel_footprint_refs` | Footprint/mask refs used in comparison. |
| `threshold_profile_id` | Versioned materiality threshold profile. |
| `threshold_results` | Pass/warn/fail per threshold family. |
| `class_delta_table_ref` | Per-class hectare/percentage delta table. |
| `transition_matrix_ref` | Optional class-transition matrix. |
| `uncertainty_refs` | UncertaintySurface or accuracy/footprint refs. |
| `source_descriptor_refs` | SourceDescriptor refs for observations and inputs. |
| `source_role_summary` | Source roles preserved through comparison. |
| `source_time` | Source publication/assertion time where material. |
| `observed_time` | Observation/acquisition period where material. |
| `valid_time` | Valid interval for comparison claim. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `release_time` | Public-safe release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `evidence_refs` | EvidenceRef links. |
| `evidence_bundle_refs` | EvidenceBundle refs behind the summary. |
| `validation_report_ref` | Validation report for schema, thresholds, class schemes, source vintages, and public safety. |
| `policy_decision_ref` | Policy decision where material. |
| `review_record_ref` | Steward review record. |
| `redaction_receipt_ref` | Receipt if geometry or detail is generalized/redacted. |
| `aggregation_receipt_ref` | Receipt if summary is aggregate public derivative. |
| `release_ref` | ReleaseManifest or PromotionDecision ref. |
| `correction_refs` | CorrectionNotice, supersession, and replacement summary refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Source-vintage mismatch, class-scheme mismatch, threshold gap, area drift, footprint gap, rights unknown, stale source, evidence incomplete, release missing. |

---

## Summary classes

| Class | Meaning | Default posture |
|---|---|---|
| `county_change_summary` | County analysis-unit delta, matching the corpus-anchored threshold pattern. | Preferred first implementation target. |
| `huc_change_summary` | Hydrologic analysis-unit delta. | PROPOSED / NEEDS VERIFICATION; Hydrology boundary applies. |
| `ecoregion_change_summary` | Ecoregion analysis-unit delta. | PROPOSED / NEEDS VERIFICATION; Habitat ecoregion context only. |
| `project_area_change_summary` | Steward-defined project boundary delta. | Requires boundary/version evidence. |
| `grid_change_summary` | Fixed grid/tiling summary. | Requires scale and privacy review. |
| `sensitive_join_summary` | Change summary joined to Fauna/Flora/sensitive context. | Fails closed unless geoprivacy/review/release support exists. |
| `candidate_record` | Unreviewed summary or watcher proposal. | WORK/QUARANTINE; no public edge. |
| `public_derivative` | Released public-safe summary card, API payload, or layer-linked summary. | Requires release manifest and rollback target. |

---

## Materiality and thresholds

Materiality thresholds are policy inputs, not hard-coded display logic.

Default doctrine-backed thresholds for county-scale change review:

| Threshold | Meaning | Status |
|---|---|---|
| Reclassification fraction > 2% | Any class reclassification above 2% of analysis-unit area. | CONFIRMED corpus idea; field enforcement NEEDS VERIFICATION |
| Net area change > max(250 ha, 0.15%) | Any net per-class delta over the larger of 250 ha or 0.15% of analysis-unit hectares. | CONFIRMED corpus idea; field enforcement NEEDS VERIFICATION |
| Boundary tests | Test just below, at, and above threshold across analysis-unit scales. | CONFIRMED corpus idea; fixtures NEEDS VERIFICATION |

> [!WARNING]
> The land-cover sublane anchors these thresholds to **county** analysis units. Applying them to HUCs, ecoregions, project areas, or grids is **PROPOSED / NEEDS VERIFICATION** until reviewed as policy and validator behavior.

---

## Source-role rules

| Source or product posture | Required handling |
|---|---|
| NLCD, LANDFIRE, GAP, NWI observations | Preserve source family, source role, class scheme, source vintage, rights, and valid-pixel footprint. |
| Remote-sensing indices | Observation input may feed change analysis, but derived classification/model output must carry model-vs-observation labels. |
| CDL / agriculture adjacency | CDL remains Agriculture-owned context; do not reclassify into Habitat cover without governed adjacency. |
| Crosswalked classes | Crosswalk must be explicit, reviewed, versioned, and citable. |
| Watcher-generated change proposal | Treat as `candidate_record` / proposed work, not publication. |
| Joined sensitive occurrence context | Owning domain retains truth; Habitat change summary cannot bypass geoprivacy. |

---

## Sensitivity and release

Land-cover change summaries are generally public-safe when they remain aggregate and source-cited. Sensitivity rises when they are joined to rare species, exact occurrence, private land, stewardship-sensitive, or protected-resource context.

Rules:

- Public summaries must retain source vintages, class schemes, thresholds, analysis unit, uncertainty, and evidence links.
- Public cards, histograms, or map popups are downstream carriers, not EvidenceBundles.
- Attribute include-lists prevent raw or sensitive fields from leaking into public layers.
- Sensitive joins fail closed until geoprivacy transform, policy decision, review, release, correction path, and rollback target exist.
- Public clients use governed APIs and released artifacts, not RAW/WORK/QUARANTINE/candidate records.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source rasters, vectors, scenes, tables, footprints, and class legends remain immutable source-bound artifacts. |
| WORK / QUARANTINE | Candidate summaries are computed, checked for class-scheme compatibility, threshold profile, source vintages, footprints, rights, sensitivity, and evidence gaps. |
| PROCESSED | Reviewed summaries receive identity, observation refs, threshold results, delta tables, validation report refs, and correction posture. |
| CATALOG / TRIPLET | Summary claims may be cataloged with EvidenceBundle refs, source role, temporal scope, analysis unit, and anti-collapse caveats. |
| RELEASE CANDIDATE | Public-safe summary cards/layers/API payloads require policy/review, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe summaries appear through governed APIs, map surfaces, Focus Mode, or reports. |
| CORRECTED / SUPERSEDED | Source-vintage update, threshold policy change, geometry correction, class-scheme change, crosswalk correction, or evidence correction triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand the paired schema beyond an empty scaffold.
- [ ] Decide accepted required fields for observation pair, analysis unit, class scheme/crosswalk, threshold profile, delta table, and evidence refs.
- [ ] Create valid fixtures for county, HUC, ecoregion, project-area, candidate, sensitive-join-denied, and public-derivative summaries.
- [ ] Create invalid fixtures for missing observation refs, same observation on both sides, missing threshold profile, incompatible class schemes without crosswalk, source-vintage collapse, footprint mismatch, rights unknown, sensitive join without geoprivacy receipt, missing EvidenceBundle, and missing release/rollback refs.
- [ ] Add validator checks for class-scheme compatibility, area accounting, threshold materiality, valid-pixel footprint, temporal separation, source-role preservation, and public-safe output.
- [ ] Add policy tests proving thresholds are policy inputs and not hard-coded renderer logic.
- [ ] Add release tests proving public clients consume released summaries only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Observation pair, class scheme, thresholds, evidence, policy, release, and rollback all resolve | `ANSWER` / public-safe summary may be shown |
| Evidence, class scheme, source vintage, threshold, rights, geometry, sensitivity, or release support is incomplete | `ABSTAIN` / `HOLD` |
| Sensitive detail would leak, source roles collapse, class schemes silently recode, or release is bypassed | `DENY` |
| Schema, validator, source read, raster read, evidence lookup, policy, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current contract scaffold | Confirms the target file existed as a scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms schema path and current empty schema posture. | Does not prove field-level validation. |
| Habitat land-cover sublane doc | Defines land-cover scope, LandCoverObservation, LandCoverChangeSummary, thresholds, lifecycle, map products, and source-role boundaries. | Many field realizations and paths remain PROPOSED. |
| Habitat source-family dossier | Confirms source-family/source-role discipline, rights verification, and sensitive join posture. | Per-family activation remains PROPOSED / NEEDS VERIFICATION. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | It is an authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized `LandCoverChangeSummary` weakens source integrity, hides threshold/materiality gaps, leaks sensitive joined context, or makes a change card/layer look more authoritative than its evidence and release state allow.

Rollback triggers include:

- source observation, raster, footprint, class scheme, crosswalk, or source vintage is corrected;
- threshold profile changes or was applied to the wrong analysis-unit type;
- source-vintage times were collapsed or silently overwritten;
- class schemes were compared without a reviewed crosswalk;
- area accounting or valid-pixel footprint is wrong;
- summary was treated as habitat quality, occurrence truth, critical-habitat designation, hydrology/soil/hazards truth, or release approval;
- sensitive join published without geoprivacy/policy/release support;
- public API/UI/AI used RAW/WORK/QUARANTINE/candidate summaries as public truth.

Rollback artifacts should include affected summary IDs, from/to observation IDs, source descriptor refs, class-scheme/crosswalk refs, analysis unit refs, threshold profile refs, delta table refs, evidence refs, validation reports, policy decisions, receipts, release refs, correction notices, rollback cards, replacement summaries, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which fields must be required in `change_summary.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Should `LandCoverChangeSummary` be camel-case contract filename or current snake-case path? | NEEDS VERIFICATION | Habitat contract naming ADR or local convention review. |
| Are county thresholds accepted for HUC, ecoregion, project-area, or grid summaries? | NEEDS VERIFICATION | Policy/steward review. |
| Which source-family vintages are admitted for first implementation? | NEEDS VERIFICATION | SourceDescriptor activation review. |
| Which public summary fields are safe for map tiles and Focus Mode cards? | NEEDS VERIFICATION | Attribute include-list, policy, and release fixture review. |
| How should stale or superseded summaries invalidate public layer caches? | NEEDS VERIFICATION | Release/runtime/cache invalidation design. |

---

## Related contracts and docs

- `docs/domains/habitat/sublanes/land_cover.md` — land-cover sublane doctrine and object-family context.
- `docs/domains/habitat/SOURCE_FAMILIES.md` — Habitat source-family role, rights, and sensitivity posture.
- `schemas/contracts/v1/domains/habitat/land_cover/change_summary.schema.json` — confirmed scaffold schema, pending expansion.
- `policy/domains/habitat/land_cover/` — expected threshold and policy home, pending verification.
- `release/manifests/habitat/` — expected release/rollback home, pending verification.

[Back to top](#top)
