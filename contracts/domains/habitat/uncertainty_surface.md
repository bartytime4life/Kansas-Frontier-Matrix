<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-uncertainty-surface
title: UncertaintySurface Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Uncertainty steward
  - OWNER_TBD — Suitability steward
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
policy_label: public-with-gates; semantic-contract; habitat; uncertainty-surface; model-uncertainty; spatial-uncertainty; accuracy-aware; source-role-aware; evidence-bound; release-gated; rollback-aware
tags: [kfm, contracts, habitat, UncertaintySurface, uncertainty_surface, uncertainty, modeled-habitat, suitability, habitat-quality-score, model-run-receipt, valid-pixel-footprint, source-vintage, confidence, evidence, policy, sensitivity, release, correction, rollback]
related:
  - ./README.md
  - ./suitability_model.md
  - ./SuitabilityModel.md
  - ./habitat_quality_score.md
  - ./model_run_receipt.md
  - ./land_cover/uncertainty.md
  - ./land_cover/observation.md
  - ./land_cover/change_summary.md
  - ./land_cover/model_run_receipt.md
  - ./land_cover_observation.md
  - ./habitat_patch.md
  - ./restoration_opportunity.md
  - ./stewardship_zone.md
  - ./connectivity_edge.md
  - ./corridor.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./domain_validation_report.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/CANONICAL_PATHS.md
  - ../../../docs/domains/habitat/sublanes/suitability.md
  - ../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../schemas/contracts/v1/domains/habitat/uncertainty_surface.schema.json
  - ../../../schemas/contracts/v1/domains/habitat/land_cover/uncertainty.schema.json
  - ../../../policy/domains/habitat/uncertainty_label.rego
  - ../../../policy/sensitivity/habitat/
  - ../../../fixtures/domains/habitat/uncertainty_surface/
  - ../../../tests/domains/habitat/test_uncertainty.*
  - ../../../data/registry/sources/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a scaffold at contracts/domains/habitat/uncertainty_surface.md."
  - "This top-level path is the contract_doc path currently referenced by schemas/contracts/v1/domains/habitat/uncertainty_surface.schema.json and is listed in docs/domains/habitat/CANONICAL_PATHS.md."
  - "The paired schema exists, but it is still a PROPOSED scaffold with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "A land-cover-specific uncertainty contract already exists at contracts/domains/habitat/land_cover/uncertainty.md. This top-level contract treats UncertaintySurface as the Habitat-wide object family, with land_cover/uncertainty.md as a specialization, not a competing authority."
  - "UncertaintySurface describes confidence, coverage, accuracy, model fitness, footprint, resolution, temporal, crosswalk, and public-generalization uncertainty. It is not an observation, not a model, not a proof object, not a policy decision, not release authority, and not something public surfaces may hide to simplify the story."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UncertaintySurface Contract — Habitat

> Semantic contract for `UncertaintySurface`: the Habitat object that carries spatial, temporal, model, classification, geometry, footprint, source-vintage, confidence, and public-generalization uncertainty alongside modeled, observed, scored, or derived Habitat products.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: UncertaintySurface" src="https://img.shields.io/badge/object-UncertaintySurface-blue">
  <img alt="Boundary: uncertainty is required" src="https://img.shields.io/badge/boundary-uncertainty__required-critical">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Publication: co-release gated" src="https://img.shields.io/badge/publication-co--release__gated-critical">
</p>

`contracts/domains/habitat/uncertainty_surface.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Top-level vs land-cover uncertainty](#top-level-vs-land-cover-uncertainty) · [Uncertainty vs trust objects](#uncertainty-vs-trust-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Uncertainty classes](#uncertainty-classes) · [Display obligations](#display-obligations) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/uncertainty_surface.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/uncertainty_surface.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Related specialization:** `contracts/domains/habitat/land_cover/uncertainty.md` already exists for land-cover uncertainty.  
> **Truth posture:** Habitat doctrine confirms `UncertaintySurface` as a canonical Habitat object family for spatial uncertainty attached to modeled products. Field-level schema shape, fixtures, validators, policy runtime, emitted instances, release artifacts, API/UI behavior, Focus Mode behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> An `UncertaintySurface` is not decorative metadata. If a Habitat product needs uncertainty to be interpreted safely, uncertainty must travel with the product or the product is held, abstained, or denied for public use.

---

## Meaning

`UncertaintySurface` records what KFM knows, does not know, cannot safely expose, or cannot safely overstate about a Habitat observation, model, score, patch, corridor, restoration candidate, stewardship context, or public-safe derivative.

It answers:

- What product, score, patch, surface, corridor, or candidate does this uncertainty describe?
- What uncertainty type applies: model confidence, probability bounds, class accuracy, source-vintage gap, valid-pixel footprint, nodata mask, crosswalk lossiness, geometry quality, resolution quality, public generalization caveat, or sensitivity-driven suppression?
- Which source roles, model cards, model-run receipts, source vintages, artifacts, validation reports, EvidenceBundles, policy decisions, and release refs support the uncertainty statement?
- What must a map, Evidence Drawer, Focus Mode card, API payload, export, or AI answer show so users do not confuse modeled, derived, generalized, or incomplete products with stronger truth?

Uncertainty is not a failure to hide. In KFM, uncertainty is part of the inspectable claim.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Habitat-wide uncertainty meaning | `contracts/domains/habitat/uncertainty_surface.md` | Top-level semantic contract requested here |
| Habitat-wide schema | `schemas/contracts/v1/domains/habitat/uncertainty_surface.schema.json` | CONFIRMED scaffold pointing to this file |
| Land-cover specialization | `contracts/domains/habitat/land_cover/uncertainty.md` | Sublane-specific specialization for land-cover accuracy, footprint, nodata, source-vintage, and crosswalk uncertainty |
| Suitability model | `contracts/domains/habitat/suitability_model.md` | Requires uncertainty for public modeled products |
| Habitat quality score | `contracts/domains/habitat/habitat_quality_score.md` | Score confidence/fitness support |
| Model run receipt | `contracts/domains/habitat/model_run_receipt.md` | Required for modeled/derived uncertainty; receipt is not the uncertainty surface itself |
| Canonical path map | `docs/domains/habitat/CANONICAL_PATHS.md` | Lists top-level UncertaintySurface path and schema path while noting schema-home slug conflict |
| Habitat doctrine | `docs/domains/habitat/README.md` | Confirms object-family membership and lifecycle/release gates |
| Suitability doctrine | `docs/domains/habitat/sublanes/suitability.md` | Requires model cards, receipts, uncertainty, sensitivity, and release posture for modeled habitat |
| Policy | `policy/domains/habitat/uncertainty_label.rego`, `policy/sensitivity/habitat/` | Expected uncertainty/public-label and sensitivity gates; implementation NEEDS VERIFICATION |
| Release | `release/manifests/habitat/` | Release/correction/rollback authority; instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/uncertainty_surface.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Uncertainty Surface` |
| Schema properties | Empty object |
| Required fields | None visible in scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/MISSING_OR_PLANNED_FILES.md` |
| Contract doc pointer | `contracts/domains/habitat/uncertainty_surface.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this contract is semantic guidance and review vocabulary only.

---

## Top-level vs land-cover uncertainty

This top-level contract defines the Habitat-wide `UncertaintySurface` object family. The existing `land_cover/uncertainty.md` file specializes that object for land-cover observations and land-cover-derived products.

| Scope | Appropriate path | Example uncertainty |
|---|---|---|
| Habitat-wide uncertainty | `contracts/domains/habitat/uncertainty_surface.md` | Suitability model confidence, habitat quality score confidence, corridor model uncertainty, restoration candidate uncertainty, public generalized geometry caveat |
| Land-cover-specific uncertainty | `contracts/domains/habitat/land_cover/uncertainty.md` | Classification accuracy, valid-pixel footprint, nodata mask, source-vintage gap, crosswalk uncertainty, raster quality |
| Release decision | `release/manifests/habitat/` | Whether uncertainty-bearing artifact may be public |
| Evidence support | EvidenceBundle / ValidationReport | Whether the uncertainty statement is admissibly supported |

> [!WARNING]
> Do not treat the top-level and land-cover uncertainty files as competing authorities. The top-level contract defines the Habitat-wide object family; the land-cover file specializes it for land-cover products. A schema steward should still confirm whether the schema hierarchy mirrors this split.

---

## Uncertainty vs trust objects

| Object / artifact | What it owns | Boundary |
|---|---|---|
| `UncertaintySurface` | Confidence, uncertainty, coverage, fitness, caveats, or exposure limits for a Habitat object/output. | This contract. |
| `SuitabilityModel` | Modeled suitability meaning. | Must co-release uncertainty when public. |
| `HabitatQualityScore` | Quality/condition/suitability-like score. | Score uncertainty must not be hidden. |
| `ModelRunReceipt` | Run/process memory. | May produce uncertainty; not proof or release. |
| `ValidationReport` | Validator findings. | May validate uncertainty object; does not replace it. |
| `EvidenceBundle` | Evidence support for claims. | Must resolve for consequential uncertainty claims. |
| `PolicyDecision` | Allow/restrict/deny/abstain. | Controls exposure; uncertainty does not decide policy. |
| `ReleaseManifest` | Publication authority. | Required for public uncertainty artifacts. |
| Map/UI/AI surface | Delivery or explanation. | Must display uncertainty obligations; never becomes uncertainty truth. |

---

## Assertions

A reviewed `UncertaintySurface` should semantically assert:

1. **Uncertainty identity** — stable uncertainty ID, object role, uncertainty kind, target object ref, temporal scope, and normalized digest.
2. **Target binding** — the Habitat object/output it describes: `SuitabilityModel`, `HabitatQualityScore`, `HabitatPatch`, `ConnectivityEdge`, `Corridor`, `RestorationOpportunity`, `StewardshipZone`, `LandCoverObservation`, `EcologicalSystem`, or released derivative.
3. **Uncertainty kind** — model confidence, prediction interval, classification accuracy, source-vintage gap, valid-pixel footprint, nodata mask, crosswalk lossiness, geometry/resolution quality, public generalization caveat, or sensitivity-driven suppression.
4. **Artifact support** — uncertainty raster, vector, mask, table, report, confusion matrix, validation metric, model-card section, receipt output, or public-safe summary.
5. **Source-role preservation** — observed, modeled, regulatory, derivative, candidate, synthetic, aggregate, and context roles remain visible.
6. **Temporal support** — source, observed, valid, retrieval, run, release, and correction times remain distinct where material.
7. **Spatial support** — extent, footprint, CRS, resolution, valid-pixel support, geometry quality, delivery generalization, and public exposure class are explicit.
8. **Evidence binding** — EvidenceRefs, EvidenceBundles, ValidationReports, artifact digests, source descriptors, model cards, receipts, policy decisions, and release refs resolve before consequential use.
9. **Display obligations** — map/API/UI/AI surfaces show uncertainty, confidence, stale state, source-vintage caveat, model-vs-observation badge, and generalization warning where material.
10. **Correction and rollback support** — correction, supersession, release withdrawal, and rollback targets are auditable.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating missing uncertainty as certainty | Unsupported confidence is a truth-posture defect. |
| Dropping uncertainty to simplify a map | Misrepresents confidence and can expose sensitive context. |
| Treating uncertainty as observation truth | Uncertainty describes confidence or support; it does not classify land cover or habitat. |
| Treating uncertainty as proof | EvidenceBundle/proof support remains separate. |
| Treating receipt output as uncertainty truth | Receipts record process; uncertainty requires its own semantics and evidence. |
| Treating UI opacity, color ramps, or toggles as uncertainty | Style is delivery, not evidence. |
| Treating generalized public layer uncertainty as source accuracy | Public generalization caveats must identify transformation and lossiness. |
| Treating model uncertainty as observed accuracy | Modeled uncertainty carries model/run/source-role caveats. |
| Treating sensitive suppression as scientific absence | Suppression means withheld/limited exposure, not absence. |
| Treating schema scaffold as implementation readiness | Current schema is a scaffold; validation enforcement remains unverified. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the confirmed scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM uncertainty-surface ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized uncertainty digest. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `UncertaintySurface`. |
| `uncertainty_id` | Stable uncertainty object identifier. |
| `uncertainty_kind` | model_confidence, prediction_interval, classification_accuracy, valid_pixel_footprint, nodata_mask, source_vintage_gap, crosswalk_uncertainty, geometry_quality, resolution_quality, public_generalization_caveat, sensitivity_suppression, or accepted enum. |
| `target_object_ref` | Habitat object/output this uncertainty describes. |
| `target_object_family` | SuitabilityModel, HabitatQualityScore, HabitatPatch, LandCoverObservation, Corridor, etc. |
| `target_artifact_refs` | Raster/vector/table/layer/card/export artifacts to which uncertainty applies. |
| `artifact_ref` | Uncertainty raster/vector/table/mask/report artifact ref. |
| `artifact_digest` | Digest for uncertainty artifact. |
| `model_card_ref` | Model-card support where modeled uncertainty is involved. |
| `model_run_receipt_ref` | ModelRunReceipt for modeled/derived uncertainty. |
| `validation_metric_refs` | Fitness, calibration, confidence, accuracy, confusion matrix, or validation report refs. |
| `valid_pixel_footprint_ref` | Footprint/mask ref when relevant. |
| `nodata_policy_ref` | Nodata/unknown/unclassified handling ref. |
| `source_descriptor_refs` | Source identity, role, rights, cadence, attribution, authority limits. |
| `source_role` | observed, model/modeled, derivative, aggregate, regulatory-context, candidate, synthetic, or accepted enum. |
| `source_vintage_refs` | Source product vintages or run vintages. |
| `class_scheme_refs` | Class schemes involved in classification uncertainty. |
| `crosswalk_refs` | Crosswalks involved in mapping uncertainty. |
| `spatial_scope_ref` | Extent, footprint, grid, patch, corridor, watershed, aggregate, or released public-safe scope. |
| `crs_source` / `crs_analysis` / `crs_delivery` | Source, analysis, and delivery CRS where material. |
| `resolution_source` / `resolution_analysis` / `resolution_delivery` | Source, analysis, and delivery resolution. |
| `confidence_summary` | Public-safe confidence statement. |
| `coverage_summary` | Public-safe valid-pixel/coverage/gap statement. |
| `uncertainty_bounds` | Numeric/statistical bounds where applicable. |
| `public_display_obligations` | Badges, warnings, caveats, labels, or export fields required for public surfaces. |
| `sensitivity_refs` | Sensitive join, rare species, stewardship, rights, cultural, infrastructure, or geoprivacy refs. |
| `policy_decision_refs` | PolicyDecision refs controlling exposure/release. |
| `review_record_ref` | Human/steward review state. |
| `release_ref` | ReleaseManifest / PromotionDecision ref if public. |
| `correction_refs` | CorrectionNotice/supersession refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing target, missing artifact digest, missing model card, missing receipt, missing footprint, stale source, missing uncertainty, sensitive exposure, release missing. |

---

## Uncertainty classes

| Class | Meaning | Default posture |
|---|---|---|
| `model_confidence` | Model confidence or model fitness support. | Requires model card and receipt. |
| `prediction_interval` | Numeric/statistical interval or bounds. | Requires method support and validation context. |
| `classification_accuracy` | Accuracy/confusion/producer-user accuracy support for categorical product. | Public-safe when source rights allow; cite source/version. |
| `valid_pixel_footprint` | Mask/footprint of contributing pixels/observations. | Evidence artifact in its own right. |
| `nodata_mask` | Nodata/unknown/unclassified treatment support. | Must remain distinct from valid-pixel footprint. |
| `source_vintage_gap` | Gap/cadence/staleness information for source vintages. | Must travel with observations and summaries. |
| `crosswalk_uncertainty` | Lossiness/ambiguity from class or source crosswalk. | Required when schemes are harmonized. |
| `geometry_quality` | CRS/topology/extent/precision/generalization caveat. | Public display must not imply exactness. |
| `resolution_quality` | Native, analysis, rollup, and web-delivery resolution caveat. | Prevents silent mixing of unlike products. |
| `public_generalization_caveat` | Public derivative caveat after simplification, redaction, buffering, aggregation, or suppression. | Release/receipt support required. |
| `sensitivity_suppression` | Detail withheld because publication would expose sensitive context. | Must not be interpreted as absence. |
| `candidate_record` | Unreviewed or incomplete uncertainty support. | WORK/QUARANTINE; no public edge. |

---

## Display obligations

Uncertainty must remain visible enough to prevent false certainty.

| Surface | Required behavior |
|---|---|
| Map layer | Show modeled status, uncertainty mode, confidence class, source-vintage badge, generalized-geometry warning, or coverage caveat where material. |
| Evidence Drawer | Link uncertainty artifact, model card, model-run receipt, source docs, validation report, policy decision, and EvidenceBundle refs. |
| Focus Mode | Cite uncertainty support before explaining suitability, quality, change, class, confidence, corridor, or restoration opportunity. |
| Public export | Include source/vintage/class scheme/model/uncertainty fields or deny export. |
| AI answer | Treat uncertainty as evidence context; do not generate confidence not backed by evidence. |
| Release review | Confirm uncertainty and public caveats are co-released with the target product. |

---

## Sensitivity and release

Uncertainty can reveal sensitive context indirectly. A high-confidence suitability surface, low-uncertainty habitat prediction, or suppressed uncertainty in a sensitive area can expose rare species, stewardship-only context, private land implications, cultural/archaeological context, or infrastructure-adjacent risk.

Rules:

- Public uncertainty must not reveal restricted exact geometry, hidden source payloads, rights-limited internals, or suppressed sensitive context.
- Public modeled products must co-release uncertainty, or release must be denied/held.
- Public generalized products must disclose the generalization/suppression caveat; they must not imply source precision.
- Missing uncertainty must not be displayed as certainty.
- Uncertainty linked to sensitive occurrence, rare plant, private/stewardship, cultural/archaeological, infrastructure, or rights-restricted joins requires policy review.
- Public clients use governed APIs and released artifacts, not RAW/WORK/QUARANTINE/candidate uncertainty objects.

---

## Lifecycle

| Phase | UncertaintySurface handling |
|---|---|
| RAW | Source accuracy docs, masks, model diagnostics, raster QA, validation metrics, cloud/nodata masks, and source caveats remain source-bound. |
| WORK / QUARANTINE | Candidate uncertainty artifacts are normalized, source-role checked, artifact-digested, linked to target objects, checked for CRS/resolution/nodata/sensitivity, and held if evidence or rights are incomplete. |
| PROCESSED | Reviewed uncertainty surfaces/footprints/masks/summaries receive identity, target refs, artifact digests, model-card/receipt refs where needed, evidence refs, validation reports, and correction posture. |
| CATALOG / TRIPLET | Uncertainty claims may be cataloged with EvidenceBundle refs, target linkage, temporal scope, source-role caveats, and sensitivity posture. |
| RELEASE CANDIDATE | Public uncertainty mode, cards, exports, layer descriptors, and summaries require policy/review, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe uncertainty artifacts or summaries appear through governed APIs, maps, Focus Mode, reports, exports, or AI surfaces. |
| CORRECTED / SUPERSEDED | Source accuracy correction, mask correction, source-vintage update, crosswalk update, model receipt update, artifact digest change, calibration update, or generalization change triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/habitat/uncertainty_surface.schema.json` beyond an empty scaffold.
- [ ] Confirm that top-level `uncertainty_surface.md` is the Habitat-wide contract and `land_cover/uncertainty.md` is a specialization.
- [ ] Confirm canonical enum values for `uncertainty_kind`, `target_object_family`, `source_role`, and `public_display_obligations`.
- [ ] Confirm whether schema-home segmented slug remains or ADR-S-01 selects the flat form.
- [ ] Add valid fixtures for model confidence, prediction interval, classification accuracy, valid-pixel footprint, nodata mask, source-vintage gap, crosswalk uncertainty, geometry quality, resolution quality, public generalization caveat, sensitivity suppression, candidate, and public derivative examples.
- [ ] Add invalid fixtures for missing target ref, missing source descriptor, missing artifact digest, missing model card, missing model-run receipt, missing valid-pixel footprint, missing uncertainty presented as certainty, nodata/footprint collapse, stale source without caveat, model uncertainty without receipt, public exact sensitive geometry, missing EvidenceBundle, missing release manifest, and missing rollback target.
- [ ] Add validator checks for target attachment, uncertainty kind, artifact digest, CRS/resolution, nodata policy, valid-pixel footprint, source vintage, temporal scope, evidence refs, model-card refs, receipt refs, policy refs, release refs, and correction lineage.
- [ ] Add tests proving uncertainty cannot substitute for observations, models, model receipts, validation reports, policy decisions, release manifests, or public layers.
- [ ] Add release tests proving public clients consume released uncertainty artifacts or summaries only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Target ref, uncertainty kind, artifact digest, confidence/footprint/accuracy support, evidence, validation, policy, release, and rollback all resolve | `ANSWER` / public-safe uncertainty can be shown |
| Evidence, source role, rights, artifact, footprint, sensitivity, or release support is incomplete | `ABSTAIN` / `HOLD` |
| Missing uncertainty would be presented as certainty, restricted detail would leak, source roles collapse, or release is bypassed | `DENY` |
| Schema, validator, source read, raster read, artifact digest, evidence lookup, policy, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Target scaffold | Confirms top-level `uncertainty_surface.md` existed as scaffold before replacement. | Does not prove contract maturity. |
| Top-level schema scaffold | Confirms `uncertainty_surface.schema.json` path and that it points to this contract path. | Does not prove field-level validation. |
| Habitat README | Confirms `UncertaintySurface` as a canonical Habitat object family and confirms lifecycle/sensitivity/publication posture. | Field realization remains PROPOSED. |
| Habitat canonical paths | Confirms top-level meaning/schema/policy/test path mapping and schema-home conflict. | Does not prove implementation or tests exist. |
| Land-cover uncertainty contract | Confirms a land-cover-specific UncertaintySurface specialization exists. | It is semantic documentation, not schema enforcement. |
| Suitability sublane doc | Confirms modeled habitat needs uncertainty, model cards, receipts, sensitivity, release, and rollback posture. | Sublane path/status and implementation remain partly PROPOSED. |
| Model-vs-observation doc | Confirms co-release requirement and publication-deny behavior for missing uncertainty/model card/receipt. | Several policy/schema enforcement claims remain PROPOSED / NEEDS VERIFICATION. |
| User-provided authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized `UncertaintySurface` weakens source integrity, hides confidence/coverage gaps, leaks sensitive joined context, or makes observed, modeled, scored, or derived Habitat outputs appear more certain than evidence allows.

Rollback triggers include uncertainty artifact correction; source accuracy document correction; valid-pixel footprint correction; nodata mask correction; model-card or model-run receipt correction; source-vintage update; class scheme or crosswalk update; artifact digest mismatch; public caveat omission; missing uncertainty displayed as certainty; sensitive joined uncertainty leaking exact occurrence or stewardship-sensitive context; public API/UI/AI using RAW/WORK/QUARANTINE/candidate uncertainty as public truth; or uncertainty dropped from a released suitability model, quality score, change summary, corridor, restoration candidate, map card, export, or Focus Mode explanation.

Rollback artifacts should include affected uncertainty IDs, target object refs, source descriptor refs, source vintages, model-card refs, model-run receipt refs, class-scheme refs, crosswalk refs, footprint refs, artifact refs/digests, evidence refs, validation reports, policy decisions, release refs, correction notices, rollback cards, replacement uncertainty objects, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is the top-level `UncertaintySurface` contract now canonical for Habitat-wide uncertainty, with `land_cover/uncertainty.md` retained as specialization? | NEEDS VERIFICATION | Habitat steward + schema steward review. |
| Which fields must be required in `uncertainty_surface.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Which uncertainty kinds are allowed for suitability, quality scores, corridors, restoration candidates, and public generalized layers? | NEEDS VERIFICATION | Contract/schema/policy review. |
| Which uncertainty values are safe for public tiles, exports, and Focus Mode cards? | NEEDS VERIFICATION | Attribute include-list, policy, and release fixture review. |
| How should missing uncertainty be rendered without falsely implying certainty? | NEEDS VERIFICATION | Map/UI and Focus Mode design review. |
| Which policy files enforce co-release and missing-uncertainty denial? | NEEDS VERIFICATION | Policy root inspection and tests. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contracts root.
- [`./suitability_model.md`](./suitability_model.md) — schema-aligned suitability model contract.
- [`./habitat_quality_score.md`](./habitat_quality_score.md) — habitat quality score contract.
- [`./model_run_receipt.md`](./model_run_receipt.md) — Habitat-wide model-run receipt contract.
- [`./land_cover/uncertainty.md`](./land_cover/uncertainty.md) — land-cover-specific uncertainty specialization.
- [`./land_cover/observation.md`](./land_cover/observation.md) — land-cover observation contract.
- [`./land_cover_observation.md`](./land_cover_observation.md) — top-level land-cover observation compatibility contract.
- [`./habitat_patch.md`](./habitat_patch.md) — HabitatPatch contract.
- [`./restoration_opportunity.md`](./restoration_opportunity.md) — restoration opportunity contract.
- [`./stewardship_zone.md`](./stewardship_zone.md) — stewardship zone contract.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat lane doctrine.
- [`../../../docs/domains/habitat/CANONICAL_PATHS.md`](../../../docs/domains/habitat/CANONICAL_PATHS.md) — canonical path map.
- [`../../../docs/domains/habitat/sublanes/suitability.md`](../../../docs/domains/habitat/sublanes/suitability.md) — suitability sublane doctrine.
- [`../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md`](../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md) — model-vs-observation and co-release doctrine.
- [`../../../schemas/contracts/v1/domains/habitat/uncertainty_surface.schema.json`](../../../schemas/contracts/v1/domains/habitat/uncertainty_surface.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
