<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-land-cover-model-run-receipt
title: Land Cover Model Run Receipt Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Model-run steward
  - OWNER_TBD — Receipt steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; habitat; land-cover; model-run-receipt; receipt-not-proof; model-vs-observation; source-vintage-aware; evidence-bound; release-gated
tags: [kfm, contracts, habitat, land_cover, model_run_receipt, ModelRunReceipt, RunReceipt, model-run, receipt, modeled-land-cover, reclassification, generalization, inputs-digest, config-digest, source-vintage, source-role, evidence, policy, release, correction, rollback]
related:
  - ../../README.md
  - ./class_scheme.md
  - ./crosswalk.md
  - ./change_summary.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/model_run_receipt.schema.json
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/
  - ../../../../policy/domains/habitat/land_cover/
  - ../../../../fixtures/domains/habitat/land_cover/model_run_receipt/
  - ../../../../tests/domains/habitat/land_cover/model_run_receipt/
  - ../../../../pipelines/domains/habitat/land_cover/
  - ../../../../pipeline_specs/habitat/land_cover/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "Expanded from a thin scaffold into a Habitat land-cover Model Run Receipt semantic contract."
  - "The expected paired schema path schemas/contracts/v1/domains/habitat/land_cover/model_run_receipt.schema.json was not found in the current GitHub inspection. Schema placement and field-level enforcement remain NEEDS VERIFICATION."
  - "The land-cover sublane names the object family Model Run Receipt / RunReceipt for modeled land-cover-derived output. This requested file path is model_run_receipt.md and is treated as the current semantic contract unless a later ADR/schema decision says otherwise."
  - "A model run receipt records what a model, reclassification, generalization, or derived land-cover run did. It is a process receipt, not EvidenceBundle proof, not source truth, not release authority, and not public layer approval."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Land Cover Model Run Receipt — Habitat

> Semantic contract for `ModelRunReceipt`: the Habitat land-cover receipt object that records a modeled, derived, reclassified, generalized, vectorized, summarized, or otherwise transformed run without turning that run into source truth, proof, publication authority, or an observed land-cover product.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Object: ModelRunReceipt" src="https://img.shields.io/badge/object-ModelRunReceipt-blue">
  <img alt="Schema: missing" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Boundary: receipt not proof" src="https://img.shields.io/badge/boundary-receipt__not__proof-critical">
</p>

`contracts/domains/habitat/land_cover/model_run_receipt.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Receipt vs trust objects](#receipt-vs-trust-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Receipt classes](#receipt-classes) · [Model-vs-observation rules](#model-vs-observation-rules) · [Source-role and time rules](#source-role-and-time-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/land_cover/model_run_receipt.md`  
> **Expected schema path:** `schemas/contracts/v1/domains/habitat/land_cover/model_run_receipt.schema.json`  
> **Schema posture:** expected paired schema path was **not found** during current inspection; field-level schema shape, fixtures, validators, tests, and CI coverage remain **NEEDS VERIFICATION**.  
> **Truth posture:** Habitat land-cover doctrine identifies `Model Run Receipt` as the receipt for land-cover-derived modeled output, with identity based on `model_id + model_version + inputs_digest + config_digest + spec_hash`. The doctrine also requires model-vs-observation labeling. Current implementation depth remains **NEEDS VERIFICATION** beyond the files inspected here.

> [!CAUTION]
> A model run receipt is process memory. It records what a model or transform did; it does **not** prove the modeled output is true, public-safe, evidence-complete, policy-approved, reviewed, released, or suitable for Habitat/Fauna/Flora claims by itself.

---

## Meaning

`ModelRunReceipt` records a reproducible account of a land-cover modeling or transformation run.

It may cover:

- reclassification or class harmonization that uses a reviewed `CoverClassCrosswalk`;
- generalization or vectorization used to create public-safe cover layers;
- modeled land-cover products derived from remote-sensing inputs;
- change-detection or histogram-drift runs that create review candidates;
- valid-pixel mask generation, uncertainty-surface generation, or footprint derivation;
- sensitivity-redacted derivatives for joined Habitat/Fauna/Flora views;
- any land-cover-derived modeled output where model-vs-observation labeling matters.

It answers:

- Which model or transform ran?
- Which exact input observations, class schemes, crosswalks, source vintages, masks, configs, thresholds, and environment were used?
- Which output artifacts, digests, summaries, or candidates were emitted?
- Which source-role labels, model-vs-observation warnings, geometry/CRS/resolution rules, and public-safety caveats must follow the outputs?
- Which EvidenceRefs, ValidationReports, PolicyDecisions, ReleaseManifests, CorrectionNotices, and RollbackCards are required before outputs can support public claims?

A receipt is useful because it makes a run inspectable. It is dangerous if treated as proof.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Model-run receipt meaning | `contracts/domains/habitat/land_cover/model_run_receipt.md` | Owned here by request; naming/schema placement needs verification |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/land_cover/model_run_receipt.schema.json` | NOT FOUND in current inspection; PROPOSED / NEEDS VERIFICATION |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Defines modeled land cover, model run receipt identity, lifecycle, source-role, raster handling, and public-surface boundaries |
| Trust-object separation | `docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md` | Confirms receipt ≠ proof ≠ catalog ≠ publication as proposed ADR doctrine |
| Class scheme input | `contracts/domains/habitat/land_cover/class_scheme.md` | Source/target scheme context for model or reclass runs |
| Crosswalk input | `contracts/domains/habitat/land_cover/crosswalk.md` | Reviewed mapping context; no silent recodes |
| Change summary output | `contracts/domains/habitat/land_cover/change_summary.md` | Downstream summary may cite run receipt but remains separate |
| Source registry | `data/registry/sources/habitat/` | Source identity, source role, rights, cadence, activation |
| Policy | `policy/domains/habitat/land_cover/`, `policy/sensitivity/habitat/` | Thresholds, public-safety, sensitive-join, and release gating |
| Executable logic | `pipelines/domains/habitat/land_cover/` | Expected processing implementation home; not this contract |
| Declarative specs | `pipeline_specs/habitat/land_cover/` | Expected model/run configuration home; not this contract |
| Release | `release/manifests/habitat/` | Expected release/correction/rollback home; release instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Expected schema path | `schemas/contracts/v1/domains/habitat/land_cover/model_run_receipt.schema.json` |
| Current inspection result | NOT FOUND |
| Schema status | UNKNOWN / NEEDS VERIFICATION |
| Required fields | UNKNOWN |
| Additional properties | UNKNOWN |
| Validator path | PROPOSED / NEEDS VERIFICATION |
| Fixture path | `fixtures/domains/habitat/land_cover/model_run_receipt/` is expected but unverified |

Until a paired schema is created or found, this contract is semantic guidance and review vocabulary only.

---

## Receipt vs trust objects

A `ModelRunReceipt` is deliberately separate from KFM proof, catalog, policy, and release objects.

| Object family | Meaning | Relationship to this contract |
|---|---|---|
| `ModelRunReceipt` | Process memory of a specific model/transform run. | This contract defines its Habitat land-cover semantics. |
| `EvidenceBundle` / proof | Admissible evidence support for a claim. | A receipt may cite proof; it is not proof. |
| `ValidationReport` | Validator findings over inputs/outputs/receipts. | A receipt may be validated; it does not validate itself. |
| `PolicyDecision` | Allow/restrict/deny/abstain decision. | A receipt may cite policy; it does not decide policy. |
| `ReviewRecord` | Steward review. | A receipt may be reviewed; it is not review approval. |
| `ReleaseManifest` / `PromotionDecision` | Publication authority. | A receipt may support release; it does not publish. |
| `Catalog` / `Triplet` | Discovery/graph projection. | A receipt may be cataloged; cataloging is not proof or release. |
| `LayerManifest` | Released layer descriptor. | A receipt can describe how an artifact was made; the layer manifest governs serving. |

---

## Assertions

A reviewed `ModelRunReceipt` should semantically assert:

1. **Run identity** — deterministic run identity from `model_id + model_version + inputs_digest + config_digest + spec_hash`.
2. **Model identity** — model/transform/tool name, version, code digest, container/tool digest, or method ref.
3. **Input closure** — exact input observations, class schemes, crosswalks, source vintages, masks, thresholds, and source descriptors.
4. **Configuration closure** — all config values that materially affect outputs, including CRS, resolution, resampling, generalization, thresholds, crosswalk versions, and random seeds where material.
5. **Output inventory** — output artifact refs, digests, public-safe derivatives, summaries, candidate records, and withheld artifacts.
6. **Source-role preservation** — observed source products remain observed inputs; modeled outputs remain modeled outputs.
7. **Temporal discipline** — run time, model version, source vintage, observed/valid time, retrieval time, release time, and correction time remain distinct.
8. **Raster discipline** — categorical versus continuous raster handling, nodata propagation, valid-pixel footprint, analysis CRS, web-delivery CRS, overviews, and area drift are recorded where material.
9. **Evidence and validation support** — EvidenceRef/EvidenceBundle refs and ValidationReport refs are present before claims become consequential.
10. **Release and rollback posture** — receipt links to release, correction, rollback, cache invalidation, or suppression instructions where outputs reach public surfaces.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating receipt as proof | ADR-0011 separates receipts from proofs; proof requires EvidenceBundle/ProofPack-style support. |
| Treating receipt as publication | ReleaseManifest / PromotionDecision owns publication. |
| Treating receipt as policy decision | Policy owns allow/restrict/deny/abstain. |
| Treating modeled output as observed product | Model-vs-observation labels must travel with outputs. |
| Treating a reclassification as a crosswalk | Crosswalks are reviewed, versioned mapping objects; receipts only record use. |
| Treating a renderer transform as a model receipt | Renderers display released artifacts; they must not silently transform source truth. |
| Treating generalized output as exact source geometry | Generalized artifacts need geometry role, transform record, and release support. |
| Treating watcher output as publication | Watchers observe and record proposed work; they do not publish. |
| Treating receipt as source activation | SourceDescriptor and source-activation decisions remain separate. |
| Treating AI-generated prose as receipt | Receipts must be emitted from controlled run metadata, not inferred narrative. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema creation/expansion. They are not enforced by a confirmed schema in this session.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM model-run receipt ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized receipt digest. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `ModelRunReceipt`, pending naming/schema confirmation. |
| `run_id` | Stable run identifier. |
| `run_kind` | Reclassification, generalization, vectorization, model inference, uncertainty generation, valid-pixel footprint, change-detection, watcher candidate, redaction, or accepted enum. |
| `model_id` | Model/transform/tool ID. |
| `model_version` | Model/transform/tool version. |
| `model_code_digest` | Digest of code that executed the run. |
| `model_config_ref` | Config file/ref. |
| `config_digest` | Digest of config inputs. |
| `inputs_ref` | Structured input set ref. |
| `inputs_digest` | Digest over input refs and relevant source heads. |
| `source_descriptor_refs` | SourceDescriptor refs for source inputs. |
| `source_vintage_refs` | Source vintage refs for observations/scenes/products. |
| `land_cover_observation_refs` | Input observation refs. |
| `class_scheme_refs` | Class schemes used. |
| `crosswalk_refs` | Reviewed crosswalks used. |
| `threshold_profile_refs` | Threshold/materiality policy refs used. |
| `valid_pixel_footprint_refs` | Footprints/masks used or emitted. |
| `uncertainty_refs` | UncertaintySurface refs used or emitted. |
| `analysis_unit_refs` | County/HUC/ecoregion/project/grid refs where relevant. |
| `crs_analysis` | CRS used for analysis. |
| `crs_delivery` | CRS used for web/public delivery where material. |
| `resolution_input` | Native/input resolution. |
| `resolution_output` | Output/rollup/generalized resolution. |
| `resampling_method` | nearest, mode, bilinear, cubic, aggregate, custom, or accepted enum. |
| `nodata_policy_ref` | Nodata/unknown handling policy/ref. |
| `run_time` | Execution time of the run. |
| `source_time` | Source publication/assertion time for inputs. |
| `observed_time` | Observation/acquisition time for source products. |
| `valid_time` | Valid time for output claim or source observation. |
| `retrieval_time` | KFM source retrieval time. |
| `release_time` | Public-safe release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `output_artifact_refs` | Output raster/vector/table/layer/summary refs. |
| `output_artifact_digests` | Digests of output artifacts. |
| `public_derivative_refs` | Public-safe derived outputs, if any. |
| `withheld_artifact_refs` | Restricted/internal outputs not public. |
| `model_vs_observation_label` | Required label: modeled, derived, generalized, reclassified, vectorized, observed-input, or accepted enum. |
| `evidence_refs` | EvidenceRef links. |
| `evidence_bundle_refs` | EvidenceBundle refs that support consequential use. |
| `validation_report_ref` | ValidationReport over the receipt and outputs. |
| `policy_decision_ref` | PolicyDecision where material. |
| `review_record_ref` | Steward review record. |
| `redaction_receipt_ref` | Receipt for sensitive/generalized/redacted outputs. |
| `aggregation_receipt_ref` | Receipt for aggregate public derivative outputs. |
| `release_ref` | ReleaseManifest or PromotionDecision ref. |
| `correction_refs` | CorrectionNotice, supersession, replacement output refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing input digest, missing config digest, undeclared crosswalk, invalid resampling, nodata drift, source-vintage gap, model/observation collapse, rights unknown, release missing. |

---

## Receipt classes

| Receipt class | Meaning | Default posture |
|---|---|---|
| `reclassification_run` | Reclassifies or harmonizes cover classes using reviewed schemes/crosswalks. | Requires crosswalk refs; never silent. |
| `generalization_run` | Generalizes geometry/raster/vector output for public serving. | Requires geometry role and transform caveats. |
| `vectorization_run` | Converts raster cover into vector polygons/tiles. | Derived output; not source raster. |
| `model_inference_run` | Produces modeled land-cover output from inputs. | Must carry model-vs-observation label. |
| `valid_pixel_footprint_run` | Emits valid-pixel or nodata mask artifacts. | Evidence artifact support required. |
| `uncertainty_surface_run` | Emits accuracy/uncertainty/footprint surfaces. | Align to source observation temporal scope. |
| `change_detection_run` | Computes histograms/deltas or candidate change summaries. | Review candidate until release support exists. |
| `watcher_candidate_run` | Watcher/no-op/source-drift checkpoint and proposed work record. | Watchers do not publish. |
| `sensitive_join_redaction_run` | Applies geoprivacy or sensitive-join transform. | Fails closed without policy/review/release. |
| `public_derivative_run` | Produces a released-ready derivative candidate. | Requires validation, policy, release, correction, rollback support. |

---

## Model-vs-observation rules

- Observed federal products such as NLCD, LANDFIRE, GAP, NWI, or remote-sensing inputs remain source observations when admitted by SourceDescriptor.
- Any reclassification, harmonization, model inference, vectorization, generalization, smoothing, aggregation, or sensitivity-redaction output is a derived or modeled output.
- A modeled output can support Habitat reasoning only with explicit receipt, source-role label, EvidenceBundle closure, validation, and release gating.
- Render model-vs-observation labels wherever outputs surface in maps, cards, APIs, evidence drawers, Focus Mode, or exports.
- A derived layer that looks visually identical to an observed product is still a different evidentiary object.

---

## Source-role and time rules

| Rule | Required behavior |
|---|---|
| Run time != source time | Record model execution separately from source publication. |
| Source vintage != model version | Preserve both; do not collapse product vintages into model release numbers. |
| Observed/valid period != retrieval time | Keep acquisition/valid period separate from harvest time. |
| Release time != run time | Running a model does not publish its outputs. |
| Correction time != rerun time by default | A rerun becomes correction only when linked to CorrectionNotice/supersession. |
| Observed input != modeled output | Preserve role boundary through output metadata and UI labels. |
| Candidate watcher output != public product | Watchers create review input, not release. |

---

## Sensitivity and release

Land-cover model receipts may be low sensitivity when inputs and outputs are public, but sensitivity rises when outputs join to rare species, exact occurrences, private land, stewardship-sensitive context, or restricted source terms.

Rules:

- Receipts can be public metadata only when they omit restricted internals and have release support.
- Public outputs require release manifests, rollback targets, correction paths, policy/review where material, and evidence closure.
- Sensitive joins must fail closed until geoprivacy/redaction receipt, policy decision, review, and release support exist.
- Public layers must not expose hidden inputs, config secrets, proprietary terms, internal paths, exact sensitive geometry, or restricted source payloads.
- Public clients use governed APIs and released artifacts; they do not read receipt internals as source truth.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source inputs and source descriptors are captured; no model receipt is public truth. |
| WORK / QUARANTINE | Candidate run records capture inputs/configs/outputs and quarantine missing digests, rights gaps, invalid resampling, hidden crosswalks, or sensitivity failures. |
| PROCESSED | Reviewed receipts bind model ID/version, input/config digests, output artifact digests, source vintages, labels, and validation refs. |
| CATALOG / TRIPLET | Receipt may be cataloged or referenced by graph claims, but receipt remains separate from proof and publication. |
| RELEASE CANDIDATE | Outputs and receipt metadata undergo policy, evidence, validation, public-safety, correction, and rollback preflight. |
| PUBLISHED | Only released public-safe output artifacts and approved receipt metadata appear through governed interfaces. |
| CORRECTED / SUPERSEDED | Input update, model version change, config correction, crosswalk correction, threshold change, output digest change, or sensitivity update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Confirm or create the paired schema at `schemas/contracts/v1/domains/habitat/land_cover/model_run_receipt.schema.json`.
- [ ] Decide accepted object-family name: `ModelRunReceipt`, `Model Run Receipt`, or `RunReceipt`.
- [ ] Add valid fixtures for reclassification, generalization, vectorization, model inference, valid-pixel footprint, uncertainty surface, change detection, watcher candidate, sensitive-join redaction, and public derivative receipts.
- [ ] Add invalid fixtures for missing input digest, missing config digest, undeclared crosswalk, invalid raster resampling, nodata drift, modeled output labeled observed, source vintage collapse, public release missing, sensitive join without redaction receipt, AI-generated receipt, and missing rollback target.
- [ ] Add validator checks for model ID/version, inputs digest, config digest, output artifact digests, source vintages, class schemes, crosswalks, CRS/resolution, nodata, model-vs-observation labels, evidence refs, policy refs, release refs, and correction lineage.
- [ ] Add tests proving receipt cannot substitute for EvidenceBundle, PolicyDecision, ReleaseManifest, ReviewRecord, or LayerManifest.
- [ ] Add no-network fixtures so CI can validate receipts without live source access.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Inputs, config, source vintages, output digests, labels, evidence, validation, policy, release, and rollback all resolve | `ANSWER` / public-safe receipt metadata may be shown |
| Evidence, source role, digest, config, rights, sensitivity, or release support is incomplete | `ABSTAIN` / `HOLD` |
| Receipt would be treated as proof/publication, modeled output would be labeled observed, or restricted detail would leak | `DENY` |
| Schema, validator, source read, artifact read, digest, model run, evidence lookup, policy, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current contract scaffold | Confirms the target file existed as a scaffold before replacement. | Does not prove contract maturity. |
| Expected schema lookup | Expected paired schema path was not found during current inspection. | Does not prove no schema exists elsewhere; naming/path remains NEEDS VERIFICATION. |
| Habitat land-cover sublane doc | Defines modeled land cover, Model Run Receipt identity, source-role boundaries, lifecycle, watcher discipline, raster handling, model-vs-observation labels, map products, and cross-lane relations. | Many field realizations and paths remain PROPOSED. |
| ADR-0011 | Confirms proposed doctrine that receipt ≠ proof ≠ catalog ≠ publication. | ADR status is proposed and current implementation remains UNKNOWN per the ADR itself. |
| ClassScheme, Crosswalk, and ChangeSummary contracts | Adjacent semantic contracts for source schemes, reviewed mappings, and summaries that may be inputs/outputs of model runs. | Recent contract content is semantic documentation, not schema enforcement. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | It is an authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized model-run receipt weakens source integrity, hides model/observation distinctions, leaks restricted inputs/configs, or lets modeled outputs appear more authoritative than their evidence/release state allows.

Rollback triggers include:

- model ID/version, code digest, config digest, or input digest is wrong;
- output artifact digest changes unexpectedly;
- source vintage or observed/valid/retrieval/release/correction time collapses;
- categorical raster was bilinear-resampled or nodata/valid-pixel handling was corrupted;
- a crosswalk or class scheme changed without rerun/correction lineage;
- model output was rendered or described as observed source product;
- receipt was used as EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, or LayerManifest;
- sensitive join or restricted config/input detail leaked into public outputs;
- public API/UI/AI used WORK/QUARANTINE/candidate receipt outputs as public truth.

Rollback artifacts should include affected receipt IDs, model IDs/versions, input refs/digests, config refs/digests, output artifact refs/digests, source vintages, class scheme refs, crosswalk refs, threshold refs, evidence refs, validation reports, policy decisions, release refs, correction notices, rollback cards, replacement receipts, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Where is the accepted paired schema for `model_run_receipt.md`? | NEEDS VERIFICATION | Schema-root inspection and/or schema PR. |
| Is the canonical object name `ModelRunReceipt`, `Model Run Receipt`, or `RunReceipt`? | NEEDS VERIFICATION | Habitat contract/schema naming review. |
| Which receipt fields are safe for public display versus steward-only audit? | NEEDS VERIFICATION | Policy/release fixture review. |
| Which model/transform types require representation receipts or additional proof objects? | NEEDS VERIFICATION | ADR-0011 + model-run validator review. |
| How should watcher checkpoints relate to model-run receipts? | NEEDS VERIFICATION | Watcher non-publisher invariant and pipeline design review. |
| How should stale receipts invalidate public layer caches and change-summary cards? | NEEDS VERIFICATION | Release/runtime/cache invalidation design. |

---

## Related contracts and docs

- `contracts/domains/habitat/land_cover/class_scheme.md` — class schemes that may be input to model runs.
- `contracts/domains/habitat/land_cover/crosswalk.md` — reviewed crosswalks used by reclassification/harmonization runs.
- `contracts/domains/habitat/land_cover/change_summary.md` — summaries that may be emitted from or cite modeled/change-detection runs.
- `docs/domains/habitat/sublanes/land_cover.md` — land-cover sublane doctrine and object-family context.
- `docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md` — proposed trust-object separation doctrine.
- `policy/domains/habitat/land_cover/` — expected threshold/model/release policy home, pending verification.
- `release/manifests/habitat/` — expected release/rollback home, pending verification.

[Back to top](#top)
