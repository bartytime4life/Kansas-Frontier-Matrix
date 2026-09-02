<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-land-cover-uncertainty
title: Land Cover Uncertainty Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Uncertainty steward
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
policy_label: public-with-gates; semantic-contract; habitat; land-cover; uncertainty; UncertaintySurface; valid-pixel-footprint; accuracy-aware; source-vintage-aware; evidence-bound; release-gated
tags: [kfm, contracts, habitat, land_cover, uncertainty, UncertaintySurface, accuracy, valid-pixel-footprint, nodata, source-vintage-gap, crosswalk-uncertainty, raster-quality, categorical-raster, continuous-raster, evidence, source-role, policy, release, correction, rollback]
related:
  - ../README.md
  - ./observation.md
  - ./class_scheme.md
  - ./crosswalk.md
  - ./change_summary.md
  - ./model_run_receipt.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/uncertainty.schema.json
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/
  - ../../../../policy/domains/habitat/land_cover/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../fixtures/domains/habitat/land_cover/uncertainty/
  - ../../../../tests/domains/habitat/land_cover/uncertainty/
  - ../../../../pipelines/domains/habitat/land_cover/
  - ../../../../pipeline_specs/habitat/land_cover/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "Expanded from a thin scaffold into a Habitat land-cover UncertaintySurface semantic contract."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/land_cover/uncertainty.schema.json, but it is still a PROPOSED scaffold with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "The land-cover sublane names the object family UncertaintySurface, while this requested file path and paired schema title use uncertainty/Uncertainty. This contract treats uncertainty.md as the current semantic contract for UncertaintySurface unless a later ADR/schema decision says otherwise."
  - "UncertaintySurface carries per-observation accuracy, valid-pixel footprint, source-vintage gap, crosswalk uncertainty, raster/geometry quality, and caveats. It is not a LandCoverObservation, ClassSchemeProfile, CoverClassCrosswalk, LandCoverChangeSummary, ModelRunReceipt, LayerManifest, policy decision, or release authority by itself."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Land Cover Uncertainty — Habitat

> Semantic contract for `UncertaintySurface`: the Habitat land-cover object that carries per-observation accuracy, valid-pixel footprint, source-vintage gap, crosswalk uncertainty, raster/geometry quality, and confidence caveats alongside a governed `LandCoverObservation`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Object: UncertaintySurface" src="https://img.shields.io/badge/object-UncertaintySurface-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: uncertainty not observation" src="https://img.shields.io/badge/boundary-uncertainty__not__observation-critical">
</p>

`contracts/domains/habitat/land_cover/uncertainty.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Uncertainty classes](#uncertainty-classes) · [Raster and footprint rules](#raster-and-footprint-rules) · [Source-role rules](#source-role-rules) · [Display and interpretation rules](#display-and-interpretation-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/land_cover/uncertainty.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/land_cover/uncertainty.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Naming posture:** the land-cover sublane names the object family `UncertaintySurface`; the requested path and schema title use `Uncertainty`. This file treats `uncertainty.md` as the current semantic contract for `UncertaintySurface`, pending schema/ADR confirmation.  
> **Truth posture:** Habitat land-cover doctrine defines `UncertaintySurface` as per-observation accuracy and footprint information, aligned to the observation's temporal scope. Field-level schema shape, fixtures, validators, source registry records, policy files, release artifacts, API behavior, UI behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> An `UncertaintySurface` explains confidence, coverage, accuracy, valid-pixel support, and uncertainty. It does **not** replace the land-cover observation, source raster, class scheme, crosswalk, model-run receipt, validation report, policy decision, release manifest, or public layer.

---

## Meaning

`UncertaintySurface` records the uncertainty, accuracy, quality, coverage, and footprint context that must travel with a land-cover observation or derived product.

It answers:

- Which `LandCoverObservation` does this uncertainty object describe?
- What kind of uncertainty is represented: class accuracy, source-vintage gap, valid-pixel footprint, nodata mask, confidence, crosswalk ambiguity, model output uncertainty, geometry/CRS/resolution quality, or public generalization caveat?
- Which source product, source vintage, class scheme, crosswalk, model receipt, artifact digest, validation report, and evidence support this uncertainty statement?
- Which map/UI/API/Focus Mode surfaces must show caveats or uncertainty mode?
- Which corrections, rollback targets, and stale-state warnings apply if the uncertainty support changes?

Uncertainty is not a weakness to hide. In KFM, uncertainty is part of the inspectable claim.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Uncertainty meaning | `contracts/domains/habitat/land_cover/uncertainty.md` | Owned here by request; object-family naming needs verification |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/land_cover/uncertainty.schema.json` | CONFIRMED scaffold; field shape not enforced |
| Observation | `contracts/domains/habitat/land_cover/observation.md` | Uncertainty attaches to observations; it does not replace them |
| Class scheme | `contracts/domains/habitat/land_cover/class_scheme.md` | Class-accuracy and label uncertainty depend on scheme version |
| Crosswalk | `contracts/domains/habitat/land_cover/crosswalk.md` | Crosswalk uncertainty must be explicit where schemes are harmonized |
| Change summary | `contracts/domains/habitat/land_cover/change_summary.md` | Summaries should carry source-vintage, footprint, and crosswalk uncertainty |
| Model run receipt | `contracts/domains/habitat/land_cover/model_run_receipt.md` | Modeled uncertainty outputs must cite receipts; receipts do not replace uncertainty semantics |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Defines uncertainty surface identity, raster discipline, map products, and temporal alignment |
| Source registry | `data/registry/sources/habitat/` | Source identity, source role, rights, cadence, activation |
| Policy | `policy/domains/habitat/land_cover/`, `policy/sensitivity/habitat/` | Public exposure, threshold, sensitive join, and release posture |
| Fixtures and tests | `fixtures/domains/habitat/land_cover/uncertainty/`, `tests/domains/habitat/land_cover/uncertainty/` | PROPOSED / NEEDS VERIFICATION |
| Release | `release/manifests/habitat/` | Expected release/correction/rollback home; release instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/land_cover/uncertainty.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Uncertainty` |
| Schema properties | Empty object |
| Required fields | None visible in the scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/sublanes/land_cover.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this contract is semantic guidance and review vocabulary only.

---

## Assertions

A reviewed `UncertaintySurface` should semantically assert:

1. **Uncertainty identity** — deterministic identity from `observation_id + uncertainty_kind + spec_hash`.
2. **Observation attachment** — linked `LandCoverObservation` and temporal scope alignment.
3. **Uncertainty kind** — accuracy, valid-pixel footprint, nodata, source-vintage gap, crosswalk uncertainty, model output uncertainty, geometry quality, resolution quality, or public generalization caveat.
4. **Artifact support** — uncertainty raster, vector, table, mask, matrix, report, source accuracy document, or public-safe summary ref.
5. **Source role** — uncertainty over observed products, modeled outputs, crosswalked classes, aggregate summaries, or public derivatives remains labeled.
6. **Temporal support** — source time, observed time, valid time, retrieval time, release time, and correction time remain distinct where material.
7. **Spatial support** — footprint, mask, extent, CRS, resolution, nodata, valid-pixel count, and public geometry posture are explicit.
8. **Evidence binding** — EvidenceRef/EvidenceBundle refs, validation report refs, artifact digests, source descriptors, and catalog/triplet refs resolve before consequential use.
9. **Display obligations** — map/API/UI/AI surfaces carry the required confidence, valid-pixel, source-vintage, model-vs-observation, and generalization warnings.
10. **Governance state** — policy, review, release, correction, supersession, and rollback refs govern downstream use.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating uncertainty as observation truth | Uncertainty describes observation quality; it does not classify land cover. |
| Treating missing uncertainty as certainty | Missing uncertainty should trigger `ABSTAIN`, `HOLD`, or warning depending use. |
| Treating valid-pixel footprint as nodata | Footprint and nodata are related but distinct evidence artifacts. |
| Treating accuracy metadata as public release approval | ReleaseManifest and PolicyDecision remain separate. |
| Treating model uncertainty as observed product accuracy | Modeled uncertainty carries ModelRunReceipt and model-vs-observation label. |
| Treating crosswalk uncertainty as class scheme truth | Crosswalk uncertainty describes mapping ambiguity, not scheme definition. |
| Treating generalized public layer uncertainty as source accuracy | Public layer uncertainty must disclose transform/generalization. |
| Treating UI uncertainty mode as evidence | UI overlays are downstream carriers; EvidenceBundle carries support. |
| Treating schema scaffold as implementation readiness | Current schema is a scaffold; validation enforcement remains unverified. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM uncertainty-surface ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized uncertainty digest. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `UncertaintySurface`, pending naming confirmation. |
| `uncertainty_id` | Source/KFM uncertainty object identifier. |
| `uncertainty_kind` | Accuracy, valid-pixel-footprint, nodata-mask, source-vintage-gap, crosswalk-uncertainty, model-uncertainty, geometry-quality, resolution-quality, public-generalization, or accepted enum. |
| `observation_id` | Linked LandCoverObservation ID. |
| `land_cover_observation_ref` | Observation ref this uncertainty object describes. |
| `source_descriptor_ref` | Source identity, role, rights, cadence, attribution, authority limits. |
| `source_family` | NLCD, LANDFIRE, GAP, NWI, NatureServe, state inventory, remote-sensing input, CDL adjacency, or accepted enum. |
| `source_role` | Observation product, modeled, adjacency, cross-reference, administrative, candidate, synthetic, or accepted KFM enum. |
| `source_vintage` | Source product vintage/year/version. |
| `class_scheme_ref` | Referenced class scheme where applicable. |
| `crosswalk_ref` | Crosswalk ref where mapping uncertainty is involved. |
| `model_run_receipt_ref` | ModelRunReceipt for modeled/derived uncertainty. |
| `artifact_ref` | Uncertainty raster/vector/table/mask/report artifact ref. |
| `artifact_digest` | Digest for uncertainty artifact. |
| `valid_pixel_footprint_ref` | Footprint/mask ref when the uncertainty kind is or uses valid-pixel footprint. |
| `nodata_policy_ref` | Nodata/unknown/unclassified handling ref. |
| `accuracy_metric_ref` | Accuracy/confusion matrix/producer-user accuracy/source accuracy ref where available. |
| `confidence_summary` | Public-safe confidence statement. |
| `coverage_summary` | Public-safe statement of valid-pixel coverage or gaps. |
| `source_vintage_gap_summary` | Public-safe gap/cadence/vintage caveat. |
| `crosswalk_uncertainty_summary` | Mapping ambiguity/lossiness statement. |
| `geometry_quality_summary` | Geometry/CRS/resolution/generalization quality statement. |
| `crs_source` | Source CRS where material. |
| `crs_analysis` | Analysis CRS where material. |
| `crs_delivery` | Delivery/public CRS where material. |
| `resolution_source` | Native source resolution. |
| `resolution_analysis` | Analysis resolution. |
| `resolution_delivery` | Delivery/generalized resolution where relevant. |
| `source_time` | Source publication/assertion time. |
| `observed_time` | Observation/acquisition period. |
| `valid_time` | Period the uncertainty claim describes. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `release_time` | Public-safe release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `evidence_refs` | EvidenceRef links. |
| `evidence_bundle_refs` | EvidenceBundle refs behind the uncertainty statement. |
| `validation_report_ref` | ValidationReport for schema, accuracy, footprint, raster handling, evidence, and public safety. |
| `policy_decision_ref` | PolicyDecision where material. |
| `review_record_ref` | Steward review record. |
| `release_ref` | ReleaseManifest or PromotionDecision ref where publicly surfaced. |
| `correction_refs` | CorrectionNotice, supersession, replacement uncertainty refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing observation, missing source descriptor, missing artifact digest, missing footprint, stale source, CRS mismatch, nodata drift, crosswalk uncertainty missing, model receipt missing, release missing. |

---

## Uncertainty classes

| Class | Meaning | Default posture |
|---|---|---|
| `classification_accuracy` | Accuracy/confusion/producer-user accuracy support for a categorical product. | Public-safe when source rights allow; must cite source/version. |
| `valid_pixel_footprint` | Mask/footprint of pixels contributing to the classification. | Evidence artifact in its own right. |
| `nodata_mask` | Nodata/unknown/unclassified treatment support. | Must remain distinct from valid-pixel footprint. |
| `source_vintage_gap` | Gap/cadence/staleness information for source vintages. | Must travel with observation and summaries. |
| `crosswalk_uncertainty` | Lossiness/ambiguity from `CoverClassCrosswalk`. | Required when class schemes are harmonized. |
| `model_output_uncertainty` | Uncertainty emitted by modeled/derived output. | Requires ModelRunReceipt and model label. |
| `geometry_quality` | CRS/topology/extent/precision/generalization caveat. | Public display must not imply exactness. |
| `resolution_quality` | Native, analysis, rollup, and web-delivery resolution caveat. | Prevent silent mixing of 10 m and 30 m products. |
| `public_generalization_caveat` | Public derivative caveat after simplification/redaction/generalization. | Release/receipt support required. |
| `candidate_record` | Unreviewed or incomplete uncertainty support. | WORK/QUARANTINE; no public edge. |

---

## Raster and footprint rules

- Valid-pixel footprint is a first-class evidence artifact, not a display afterthought.
- Nodata/unknown/unclassified handling must be explicit and consistent through overviews and derivatives.
- Categorical uncertainty must not be interpolated as if it were continuous data.
- Continuous uncertainty surfaces may use continuous raster methods only when statistics and method are declared.
- Native source resolution, analysis resolution, and delivery resolution stay distinct.
- Geometry/CRS/resolution changes must preserve transform manifests and caveats.
- Source-vintage gaps and update cadence caveats must travel with observations, summaries, and public layers.
- Crosswalk uncertainty is required when class schemes are compared or harmonized.

---

## Source-role rules

| Source or uncertainty posture | Required handling |
|---|---|
| NLCD/GAP/LANDFIRE/NWI source accuracy | Preserve source product role, source vintage, class scheme, and source documentation. |
| Remote-sensing continuous input uncertainty | Carry input statistics and acquisition/valid time; derived classification needs receipt. |
| Crosswalk uncertainty | Preserve directionality, lossiness, reviewer state, and source/target schemes. |
| Modeled uncertainty | Carry ModelRunReceipt and model-vs-observation label. |
| Generalized public layer caveat | Carry release/generalization support and do not imply source precision. |
| Sensitive joined uncertainty | Preserve owning-domain truth and fail closed until geoprivacy/policy/release resolve. |
| Watcher-generated uncertainty warning | Treat as review candidate; watchers do not publish. |
| AI-proposed uncertainty statement | Synthetic/candidate only; not evidence. |

---

## Display and interpretation rules

Uncertainty must stay visible enough to prevent false certainty.

| Surface | Required behavior |
|---|---|
| Map layer | Show uncertainty mode, source-vintage badge, generalized-geometry warning, or confidence caveat where material. |
| Evidence drawer | Link uncertainty artifact, source docs, validation report, and EvidenceBundle refs. |
| Focus Mode | Cite uncertainty support before explaining change, class, or confidence. |
| Change summary card | Show threshold profile, observation pair, source vintages, and footprint/crosswalk caveats. |
| Public export | Include source/vintage/class scheme/uncertainty fields or deny export. |
| AI answer | Treat uncertainty as evidence context; do not generate confidence not backed by evidence. |

---

## Sensitivity and release

Uncertainty artifacts are often public-safe, but the context they reveal can be sensitive.

Rules:

- Uncertainty linked to rare species, sensitive habitats, protected resources, private land, or exact occurrence joins may require redaction/generalization.
- Public uncertainty mode must avoid leaking restricted exact geometry, hidden source payloads, or rights-limited source internals.
- Public layers and summaries need release manifests, rollback targets, correction paths, policy/review where material, and EvidenceBundle closure.
- Missing uncertainty should not be silently converted into certainty.
- Public clients use governed APIs and released artifacts, not RAW/WORK/QUARANTINE/candidate uncertainty objects.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source accuracy docs, masks, raster QA, confusion matrices, product metadata, cloud/nodata masks, and source caveats remain source-bound. |
| WORK / QUARANTINE | Candidate uncertainty artifacts are normalized, source-role checked, artifact-digested, linked to observations, checked for CRS/resolution/nodata, and held if evidence or rights are incomplete. |
| PROCESSED | Reviewed uncertainty surfaces/footprints/masks receive identity, observation refs, artifact digests, evidence refs, validation reports, and correction posture. |
| CATALOG / TRIPLET | Uncertainty claims may be cataloged with EvidenceBundle refs, observation linkage, temporal scope, and source-role caveats. |
| RELEASE CANDIDATE | Public uncertainty mode, cards, exports, and layer descriptors require policy/review, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe uncertainty artifacts or summaries appear through governed APIs, maps, Focus Mode, or reports. |
| CORRECTED / SUPERSEDED | Source accuracy correction, mask correction, source-vintage update, crosswalk update, model receipt update, artifact digest change, or generalization change triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand the paired schema beyond an empty scaffold.
- [ ] Decide whether `UncertaintySurface` or `Uncertainty` is the accepted schema/object-family name.
- [ ] Add valid fixtures for classification accuracy, valid-pixel footprint, nodata mask, source-vintage gap, crosswalk uncertainty, model output uncertainty, geometry quality, resolution quality, public generalization caveat, candidate, and public derivative examples.
- [ ] Add invalid fixtures for missing observation ref, missing source descriptor, missing artifact digest, missing valid-pixel footprint, nodata/footprint collapse, stale source without caveat, crosswalk uncertainty missing, model uncertainty without receipt, 10 m/30 m silent mixing, public exact sensitive geometry, missing EvidenceBundle, missing release manifest, and missing rollback target.
- [ ] Add validator checks for observation attachment, uncertainty kind, artifact digest, CRS/resolution, nodata policy, valid-pixel footprint, source vintage, temporal scope, evidence refs, policy refs, release refs, and correction lineage.
- [ ] Add tests proving uncertainty cannot substitute for observations, class schemes, crosswalks, model receipts, validation reports, release manifests, or public layers.
- [ ] Add release tests proving public clients consume released uncertainty artifacts or summaries only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Observation ref, uncertainty kind, artifact digest, footprint/accuracy support, evidence, validation, policy, release, and rollback all resolve | `ANSWER` / public-safe uncertainty can be shown |
| Evidence, source role, rights, artifact, footprint, sensitivity, or release support is incomplete | `ABSTAIN` / `HOLD` |
| Missing uncertainty would be presented as certainty, restricted detail would leak, source roles collapse, or release is bypassed | `DENY` |
| Schema, validator, source read, raster read, artifact digest, evidence lookup, policy, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current contract scaffold | Confirms the target file existed as a scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms schema path and current empty schema posture. | Does not prove field-level validation. |
| Habitat land-cover sublane doc | Defines valid-pixel footprint, uncertainty surface identity, source-family roles, lifecycle, raster discipline, spatial/temporal model, uncertainty-mode public product, and model-vs-observation boundaries. | Many field realizations and paths remain PROPOSED. |
| Observation, ClassScheme, Crosswalk, ChangeSummary, and ModelRunReceipt contracts | Adjacent semantic contracts that define neighboring object boundaries. | Recent contract content is semantic documentation, not schema enforcement. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | It is an authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized uncertainty object weakens source integrity, hides accuracy/footprint gaps, leaks sensitive joined context, or makes observation/model outputs appear more certain than evidence allows.

Rollback triggers include:

- source accuracy document, valid-pixel footprint, nodata mask, raster QA, source vintage, class scheme, crosswalk, model receipt, or artifact digest is corrected;
- valid-pixel footprint was collapsed into nodata or hidden from public support;
- uncertainty or source-vintage caveat was dropped from a change summary, map, API, Focus Mode, or export;
- categorical/continuous uncertainty methods were mixed incorrectly;
- analysis/delivery resolutions were silently mixed;
- missing uncertainty was displayed as certainty;
- sensitive joined uncertainty leaked exact occurrence or stewardship-sensitive context;
- public API/UI/AI used RAW/WORK/QUARANTINE/candidate uncertainty as public truth.

Rollback artifacts should include affected uncertainty IDs, observation refs, source descriptor refs, source vintages, class scheme refs, crosswalk refs, model receipt refs, footprint refs, artifact refs/digests, evidence refs, validation reports, policy decisions, release refs, correction notices, rollback cards, replacement uncertainty objects, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is the canonical object name `UncertaintySurface` or `Uncertainty`? | NEEDS VERIFICATION | Habitat contract/schema naming review. |
| Which fields must be required in `uncertainty.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Which source products provide authoritative per-vintage accuracy matrices or masks? | NEEDS VERIFICATION | SourceDescriptor activation review. |
| Which uncertainty values are safe for public tiles, exports, and Focus Mode cards? | NEEDS VERIFICATION | Attribute include-list, policy, and release fixture review. |
| How should crosswalk uncertainty combine with source accuracy in change summaries? | NEEDS VERIFICATION | Land-cover steward + validator review. |
| How should missing uncertainty be rendered without falsely implying certainty? | NEEDS VERIFICATION | Map/UI and Focus Mode design review. |

---

## Related contracts and docs

- `contracts/domains/habitat/land_cover/observation.md` — observations to which uncertainty attaches.
- `contracts/domains/habitat/land_cover/class_scheme.md` — schemes whose class accuracy and labels shape uncertainty.
- `contracts/domains/habitat/land_cover/crosswalk.md` — crosswalks whose lossiness/ambiguity may generate uncertainty.
- `contracts/domains/habitat/land_cover/change_summary.md` — summaries that must carry uncertainty/caveats.
- `contracts/domains/habitat/land_cover/model_run_receipt.md` — receipts for modeled uncertainty outputs.
- `docs/domains/habitat/sublanes/land_cover.md` — land-cover sublane doctrine and object-family context.
- `docs/domains/habitat/SOURCE_FAMILIES.md` — Habitat source-family role, rights, and sensitivity posture.
- `schemas/contracts/v1/domains/habitat/land_cover/uncertainty.schema.json` — confirmed scaffold schema, pending expansion.
- `policy/domains/habitat/land_cover/` — expected uncertainty/source-vintage/public-safety policy home, pending verification.
- `release/manifests/habitat/` — expected release/rollback home, pending verification.

[Back to top](#top)
