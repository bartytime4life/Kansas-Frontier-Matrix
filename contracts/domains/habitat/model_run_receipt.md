<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-model-run-receipt
title: Model Run Receipt Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Model-run steward
  - OWNER_TBD — Receipt steward
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
policy_label: public-with-gates; semantic-contract; habitat; model-run-receipt; receipt-not-proof; model-vs-observation; source-role-aware; source-vintage-aware; evidence-bound; uncertainty-bound; release-gated; rollback-aware
tags: [kfm, contracts, habitat, ModelRunReceipt, model_run_receipt, model-run, receipt, run-receipt, receipt-not-proof, suitability, habitat-quality-score, modeled-habitat, uncertainty-surface, model-card, source-role, evidence, policy, release, correction, rollback, anti-collapse]
related:
  - ./README.md
  - ./SuitabilityModel.md
  - ./habitat_quality_score.md
  - ./uncertainty_surface.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./domain_validation_report.md
  - ./habitat_patch.md
  - ./ecological_system.md
  - ./connectivity_edge.md
  - ./corridor.md
  - ./land_cover/model_run_receipt.md
  - ./land_cover/observation.md
  - ./land_cover/crosswalk.md
  - ./land_cover/change_summary.md
  - ./land_cover/uncertainty.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../docs/domains/habitat/sublanes/suitability.md
  - ../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../schemas/contracts/v1/domains/habitat/model_run_receipt.schema.json
  - ../../../schemas/contracts/v1/domains/habitat/land_cover/README.md
  - ../../../policy/domains/habitat/
  - ../../../policy/sensitivity/habitat/
  - ../../../fixtures/domains/habitat/model_run_receipt/
  - ../../../tests/domains/habitat/model_run_receipt/
  - ../../../data/registry/sources/habitat/
  - ../../../data/receipts/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a top-level scaffold at contracts/domains/habitat/model_run_receipt.md."
  - "This top-level path is currently referenced by schemas/contracts/v1/domains/habitat/model_run_receipt.schema.json."
  - "The paired top-level schema exists, but it is still a PROPOSED scaffold with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "A land-cover-specific receipt contract already exists at contracts/domains/habitat/land_cover/model_run_receipt.md. This top-level contract treats ModelRunReceipt as the Habitat-wide receipt family, with land_cover/model_run_receipt.md as a specialization, not a competing authority."
  - "A ModelRunReceipt is process memory. It is not EvidenceBundle proof, not a policy decision, not a review approval, not a catalog record, not a ReleaseManifest, and not publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Model Run Receipt Contract — Habitat

> Semantic contract for `ModelRunReceipt`: the Habitat receipt object that records a specific model, transform, scoring, generalization, reclassification, redaction, or derived-output run without turning that run into source truth, proof, policy approval, review approval, release authority, or public claim support by itself.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: ModelRunReceipt" src="https://img.shields.io/badge/object-ModelRunReceipt-blue">
  <img alt="Boundary: receipt not proof" src="https://img.shields.io/badge/boundary-receipt__not__proof-critical">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release__gated-critical">
</p>

`contracts/domains/habitat/model_run_receipt.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Top-level vs sublane receipts](#top-level-vs-sublane-receipts) · [Receipt vs trust objects](#receipt-vs-trust-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Receipt classes](#receipt-classes) · [Model-vs-observation rules](#model-vs-observation-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/model_run_receipt.md`  
> **Top-level schema path:** `schemas/contracts/v1/domains/habitat/model_run_receipt.schema.json`  
> **Schema posture:** paired top-level schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Related specialization:** `contracts/domains/habitat/land_cover/model_run_receipt.md` already exists for land-cover-derived runs.  
> **Truth posture:** Habitat doctrine confirms `Model Run Receipt` as a canonical Habitat object family. Top-level field shape, fixtures, validators, policy runtime, emitted receipt instances, release artifacts, API/UI behavior, Focus Mode behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> A `ModelRunReceipt` is process memory. It records what ran, with which inputs, configuration, environment, outputs, digests, and caveats. It does **not** prove that an output is true, public-safe, reviewed, policy-allowed, released, or fit for consequential use.

---

## Meaning

`ModelRunReceipt` records the auditable facts of a Habitat model or transformation run.

It may cover:

- suitability-model inference;
- habitat-quality scoring;
- modeled-habitat generation;
- land-cover reclassification, generalization, vectorization, or change analysis;
- ecological-system classification support;
- uncertainty-surface generation;
- valid-pixel-footprint generation;
- habitat-patch derivation;
- connectivity/corridor derivation;
- public-safe geometry generalization or sensitivity transform;
- watcher candidate generation;
- AI-assisted candidate production, when allowed and reviewed under AI receipt policy.

It answers:

- Which model, transform, tool, workflow, or AI-assisted procedure ran?
- Which exact inputs, source vintages, SourceDescriptors, class schemes, model cards, config values, policies, thresholds, and environment were used?
- Which output artifacts, candidate objects, summaries, public-safe derivatives, or withheld artifacts were produced?
- Which source-role labels, model-vs-observation badges, uncertainty refs, evidence refs, policy refs, validation refs, release refs, correction refs, and rollback refs must follow the outputs?

Receipts make runs inspectable. They do not make claims true.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Habitat-wide receipt meaning | `contracts/domains/habitat/model_run_receipt.md` | Top-level semantic contract requested here |
| Habitat-wide schema | `schemas/contracts/v1/domains/habitat/model_run_receipt.schema.json` | CONFIRMED scaffold pointing to this file |
| Land-cover specialization | `contracts/domains/habitat/land_cover/model_run_receipt.md` | Sublane-specific specialization for land-cover-derived runs |
| Suitability doctrine | `docs/domains/habitat/sublanes/suitability.md` | Requires model cards, receipts, and uncertainty for modeled suitability products |
| Model-vs-observation doctrine | `docs/domains/habitat/MODEL_VS_OBSERVATION.md` | Requires model outputs to stay labeled as model, not observed or regulatory |
| Trust-object separation | `docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md` | States receipt ≠ proof ≠ catalog ≠ publication as proposed ADR doctrine |
| Source registry | `data/registry/sources/habitat/` | Source identity, source role, rights, cadence, activation |
| Receipt instances | `data/receipts/habitat/` | PROPOSED / NEEDS VERIFICATION instance home for Habitat receipts |
| Policy | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Source-role, model-card, uncertainty, sensitivity, and release gates |
| Release | `release/manifests/habitat/` | Release/correction/rollback authority; instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/model_run_receipt.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Model Run Receipt` |
| Schema properties | Empty object |
| Required fields | None visible in the scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/MISSING_OR_PLANNED_FILES.md` |
| Contract doc pointer | `contracts/domains/habitat/model_run_receipt.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this contract is semantic guidance and review vocabulary only.

---

## Top-level vs sublane receipts

This top-level contract is the Habitat-wide receipt family for modeled or transformed Habitat outputs. The existing `land_cover/model_run_receipt.md` contract is a specialization for land-cover-derived runs.

| Receipt scope | Appropriate path | Example run |
|---|---|---|
| Habitat-wide model or transform | `contracts/domains/habitat/model_run_receipt.md` | Suitability model inference, habitat-quality score computation, patch/corridor derivation, uncertainty generation |
| Land-cover-specific model or transform | `contracts/domains/habitat/land_cover/model_run_receipt.md` | NLCD reclassification, LANDFIRE crosswalk application, valid-pixel footprint derivation, land-cover generalization |
| Release decision | `release/manifests/habitat/` | Publishing a released surface, score, corridor, or layer |
| Proof/evidence closure | EvidenceBundle / proof roots | Proving a public claim has admissible support |

> [!WARNING]
> Do not treat top-level and land-cover receipts as competing authorities. The top-level contract defines the Habitat-wide receipt family; the land-cover contract specializes that family for land-cover processing. A schema steward should still confirm whether the schema hierarchy mirrors this split.

---

## Receipt vs trust objects

A `ModelRunReceipt` is deliberately separate from KFM proof, catalog, policy, review, and release objects.

| Object family | Meaning | Relationship to this contract |
|---|---|---|
| `ModelRunReceipt` | Process memory for a specific model/transform run. | This contract defines Habitat-wide semantics. |
| `EvidenceBundle` / proof | Admissible evidence support for a claim. | A receipt may cite proof; it is not proof. |
| `ValidationReport` | Validator findings over inputs, outputs, receipts, and contracts. | A receipt may be validated; it does not validate itself. |
| `PolicyDecision` | Allow/restrict/deny/abstain decision. | A receipt may cite policy; it does not decide policy. |
| `ReviewRecord` | Steward review. | A receipt may be reviewed; it is not review approval. |
| `ReleaseManifest` / `PromotionDecision` | Publication authority. | A receipt may support release; it does not publish. |
| `Catalog` / `Triplet` | Discovery/graph projection. | A receipt may be cataloged; cataloging is not proof or release. |
| `LayerManifest` | Released layer descriptor. | A receipt can describe how an artifact was made; the layer manifest governs serving. |
| `AIReceipt` | AI invocation/process receipt. | May be required for AI-assisted generation or summarization; not source truth. |

---

## Assertions

A reviewed `ModelRunReceipt` should semantically assert:

1. **Run identity** — deterministic identity from `model_id + model_version + inputs_digest + config_digest + spec_hash` or an approved Habitat-wide equivalent.
2. **Model or transform identity** — model/tool/workflow name, version, code digest, container/tool digest, model-card ref, method ref, or policy-controlled transform ref.
3. **Input closure** — exact input observations, source descriptors, source vintages, class schemes, model cards, masks, thresholds, EvidenceRefs, and policy inputs.
4. **Configuration closure** — all configuration values materially affecting output, including CRS, resolution, resampling, random seed, thresholds, crosswalks, redaction/generalization, and role labels.
5. **Output inventory** — artifact refs, digests, public-safe derivatives, withheld artifacts, candidate objects, summaries, tileset inputs, validation artifacts, and failure artifacts.
6. **Source-role preservation** — observed inputs remain observed; model outputs remain model; regulatory sources remain regulatory; derived outputs remain derivative.
7. **Temporal discipline** — run time, model version time, source time, observed time, valid time, retrieval time, release time, and correction time remain distinct where material.
8. **Uncertainty posture** — uncertainty surfaces, bounds, confidence, model limitations, known failure modes, and omitted uncertainty are explicit.
9. **Evidence and validation support** — EvidenceRef/EvidenceBundle refs and ValidationReport refs are present before outputs become consequential.
10. **Release and rollback posture** — release refs, correction refs, rollback refs, cache invalidation, and suppression instructions exist before public exposure.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating receipt as proof | Receipts record process; proof requires EvidenceBundle/ProofPack-style support. |
| Treating receipt as publication | ReleaseManifest / PromotionDecision owns publication. |
| Treating receipt as policy decision | Policy owns allow/restrict/deny/abstain. |
| Treating receipt as review approval | Steward review remains a separate object. |
| Treating modeled output as observed source | Model-vs-observation labels must travel with outputs. |
| Treating modeled output as regulatory critical habitat | Regulatory designations require competent-authority source role. |
| Treating uncertainty-free output as acceptable | Uncertainty must be co-released or the output is held/denied. |
| Treating a renderer transform as a receipt | Renderers display released artifacts; transforms must be recorded upstream. |
| Treating generalized output as exact geometry | Generalized artifacts need transform receipts and geometry role. |
| Treating watcher output as publication | Watchers observe and record candidate work; they do not publish. |
| Treating receipt as source activation | SourceDescriptor and source-activation decisions remain separate. |
| Treating AI prose as a receipt | Receipts come from controlled run metadata, not inferred narrative. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the confirmed scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM model-run receipt ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized receipt digest. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `ModelRunReceipt`. |
| `run_id` | Stable run identifier. |
| `run_kind` | suitability_inference, quality_score, land_cover_reclassification, patch_derivation, corridor_derivation, uncertainty_generation, redaction_transform, watcher_candidate, ai_assisted_candidate, or accepted enum. |
| `model_id` | Model/transform/tool ID. |
| `model_version` | Version of model/tool/workflow. |
| `model_card_ref` | Model card or method card where applicable. |
| `code_ref` | Code/workflow reference. |
| `code_digest` | Digest of executable code/workflow. |
| `environment_ref` | Runtime/container/environment reference. |
| `environment_digest` | Digest of environment where material. |
| `input_refs` | Input object/artifact refs. |
| `inputs_digest` | Digest over ordered input set. |
| `source_descriptor_refs` | Source identity, role, rights, cadence, and citation. |
| `source_role_refs` | Role refs for input and output objects. |
| `config_ref` | Configuration file/object ref. |
| `config_digest` | Digest over effective config. |
| `policy_input_refs` | Policy versions and thresholds used by run. |
| `random_seed` | Seed when stochastic behavior matters. |
| `spatial_scope_ref` | Declared run scope. |
| `temporal_scope_ref` | Declared time scope. |
| `run_time` | Time run executed. |
| `source_time_refs` | Source vintage/time refs. |
| `observed_time_refs` | Observed/acquisition time refs. |
| `valid_time_refs` | Valid period refs. |
| `retrieval_time_refs` | Retrieval time refs. |
| `output_refs` | Output artifact/object refs. |
| `output_digests` | Output artifact digests. |
| `withheld_output_refs` | Withheld/restricted artifacts. |
| `uncertainty_refs` | UncertaintySurface/bounds/confidence refs. |
| `validation_report_refs` | ValidationReport refs over inputs, outputs, and receipt. |
| `evidence_refs` / `evidence_bundle_refs` | Evidence closure refs used by consequential outputs. |
| `policy_decision_refs` | PolicyDecision refs where material. |
| `review_record_ref` | Steward review state. |
| `release_ref` | ReleaseManifest or PromotionDecision ref if output is public. |
| `correction_refs` | CorrectionNotice/re-run/supersession refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing source role, missing model card, missing uncertainty, stale inputs, invalid geometry, policy failure, candidate-only, release missing. |

---

## Receipt classes

| Receipt class | Typical output | Required companion posture |
|---|---|---|
| Suitability inference | SuitabilityModel surface or score | Model card, uncertainty, validation, evidence, policy, release if public |
| Habitat quality score | HabitatQualityScore | Method/model card, uncertainty/confidence, scored subject, release if public |
| Land-cover reclassification | Derived LandCoverObservation or crosswalk output | Class scheme, crosswalk, source role, raster discipline |
| Habitat patch derivation | HabitatPatch candidate | Patch geometry role, source support, sensitivity, review |
| Connectivity/corridor derivation | ConnectivityEdge or Corridor candidate | Method support, cost/resistance assumptions, uncertainty, public-safe geometry |
| Redaction/generalization | Public-safe derivative | Transform receipt details, policy, reviewer, residual risk, rollback |
| Watcher candidate | PROPOSED_WORK_RECORD or candidate artifact | Non-publisher invariant; review required before promotion |
| AI-assisted candidate | Candidate doc/object/summary | AIReceipt, source evidence, review, never source truth |

---

## Model-vs-observation rules

- A model output is labeled `model` or equivalent; it is not observed land cover.
- A regulatory source is labeled `regulatory` or `authority`; it is not modeled habitat.
- A derived object carries method support and source-role lineage; it is not a primary source.
- If one artifact would need two roles to describe honestly, split it into two governed objects.
- Suitability surfaces, quality scores, and modeled habitat require resolvable model cards, model-run receipts, and uncertainty support before publication.
- AI surfaces must abstain when role, evidence, model card, uncertainty, policy, or release support is insufficient.

---

## Sensitivity and release

Model-run receipts can reveal sensitive inputs, restricted geometry, private stewardship context, rare-species joins, model assumptions, or withheld artifacts. Public receipt exposure must therefore be staged and policy-aware.

Rules:

- Public receipts may need redacted input refs, generalized geometry, or steward-only exact metadata.
- A receipt may support release, but it never grants release.
- Receipts for sensitive outputs must link to policy decisions, redaction receipts/transform records, review records, release refs, correction refs, and rollback refs.
- Public map/UI/AI surfaces must use released public-safe artifacts and citation surfaces, not direct receipt internals.
- Style filters, popups, vector indexes, graph projections, and summaries are not sensitivity controls.

---

## Lifecycle

| Phase | ModelRunReceipt handling |
|---|---|
| RAW | Run intent, input refs, source roles, source vintages, rights, sensitivity, and expected outputs are captured but not public truth. |
| WORK / QUARANTINE | Run executes or is held; failures, missing source roles, missing model cards, missing uncertainty, invalid geometry, and sensitivity issues are recorded. |
| PROCESSED | Receipt binds run identity, inputs digest, config digest, model/tool version, outputs, validation refs, evidence refs, and policy refs where material. |
| CATALOG / TRIPLET | Receipt may be discoverable or referenced as process lineage; catalog/triplet views do not become proof or release. |
| RELEASE CANDIDATE | Outputs that cite the receipt must also resolve validation, policy, evidence, model card, uncertainty, release manifest, correction path, and rollback target. |
| PUBLISHED | Only approved public-safe receipt summaries or references are exposed; internal exact metadata may remain restricted. |
| CORRECTED / SUPERSEDED | Re-run, source update, model update, config correction, evidence correction, policy change, sensitivity review, or release withdrawal triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/habitat/model_run_receipt.schema.json` beyond an empty scaffold.
- [ ] Confirm how the top-level Habitat-wide receipt schema relates to `land_cover/model_run_receipt.md` and any future sublane receipt schemas.
- [ ] Confirm canonical source-role enum spelling, including `model` vs `modeled` and `authority` vs `regulatory`.
- [ ] Confirm model-card/method-card required fields for suitability, quality, patch, connectivity, corridor, and redaction runs.
- [ ] Add valid fixtures for suitability inference, habitat-quality score run, land-cover reclassification, patch derivation, corridor derivation, uncertainty generation, redaction/generalization transform, watcher candidate, and AI-assisted candidate.
- [ ] Add invalid fixtures for missing model card, missing input digest, missing config digest, missing uncertainty, modeled-as-observed, modeled-as-regulatory, candidate-as-public, receipt-as-proof, receipt-as-release, and missing rollback target.
- [ ] Add validator checks for run identity, model/tool version, inputs digest, config digest, source roles, source vintages, outputs, uncertainty refs, evidence refs, policy refs, validation refs, release refs, correction refs, and rollback refs.
- [ ] Add tests proving public map/UI/AI surfaces cannot treat receipts as proof, publication, policy, source truth, or release authority.
- [ ] Confirm release tests proving public clients consume released public-safe artifacts only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Run, inputs, config, outputs, source roles, evidence, validation, uncertainty, policy, release, correction, and rollback resolve | `ANSWER` / receipt may support a public-safe claim |
| Evidence, model card, source role, uncertainty, sensitivity, release, or rollback support is incomplete | `ABSTAIN` / `HOLD` |
| Receipt-as-proof, receipt-as-publication, role collapse, sensitive leak, candidate public path, or release bypass would occur | `DENY` |
| Schema, validator, source read, digest, evidence lookup, model-card lookup, policy lookup, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Target scaffold | Confirms top-level `model_run_receipt.md` existed as scaffold before replacement. | Does not prove contract maturity. |
| Top-level schema scaffold | Confirms `model_run_receipt.schema.json` path and that it points to this contract path. | Does not prove field-level validation. |
| Land-cover receipt contract | Confirms a sublane-specific ModelRunReceipt specialization already exists. | Does not define the top-level Habitat-wide schema. |
| Habitat README | Confirms `Model Run Receipt` as a canonical Habitat object family and confirms lifecycle/release posture. | Field realization remains PROPOSED. |
| Model-vs-observation doc | Confirms source-role anti-collapse, model-card, receipt, and uncertainty burden for modeled outputs. | Exact policy/schema enforcement remains NEEDS VERIFICATION. |
| Suitability sublane doc | Confirms suitability products require model cards, receipts, and uncertainty as governed doctrine. | Sublane path/status and implementation remain partly PROPOSED. |
| ADR-0011 | Confirms proposed doctrine that receipt ≠ proof ≠ catalog ≠ publication. | ADR itself is proposed and does not prove implementation. |
| User-provided authoring role | Requires evidence-grounded repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a receipt or receipt-dependent output weakens source-role integrity, model-card integrity, input/config closure, uncertainty posture, evidence support, sensitivity posture, or release governance.

Rollback triggers include model/version correction; input digest correction; config digest correction; source-vintage correction; source-role correction; missing or changed model card; missing uncertainty; output digest mismatch; invalid generalization/redaction; sensitive exact input leak; modeled output presented as observed or regulatory; receipt treated as proof, policy, review, release, catalog, source activation, or publication; candidate output appearing in public API/UI/AI path; watcher-as-publisher; tile/popup/vector-index/AI-as-truth; or missing release/correction/rollback refs.

Rollback artifacts should include affected run IDs, model/tool refs, model card refs, input refs, source refs, source-role refs, temporal-scope refs, config refs, input/config/output digests, uncertainty refs, evidence refs, validation reports, policy decisions, redaction receipts, release refs, correction notices, rollback cards, replacement receipts, replacement outputs, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is `model_run_receipt.md` the canonical Habitat-wide receipt contract, with sublane-specific specializations underneath? | NEEDS VERIFICATION | Habitat steward + schema steward review. |
| Should future sublanes own their own receipt schemas, or should all Habitat model receipts conform to this top-level schema? | NEEDS VERIFICATION | ADR/schema migration note. |
| Which fields must be required in `model_run_receipt.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| What model-card/method-card field set is required by suitability, patch, corridor, quality-score, and redaction runs? | NEEDS VERIFICATION | Contract/schema/policy review. |
| Which receipt metadata can be public when inputs include sensitive habitat/occurrence joins? | NEEDS VERIFICATION | Policy, sensitivity, and release review. |
| Where should Habitat receipt instances live: `data/receipts/habitat/`, run-specific family homes, or another ADR-backed path? | NEEDS VERIFICATION | Directory Rules + ADR-0011 review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contract root.
- [`./SuitabilityModel.md`](./SuitabilityModel.md) — suitability model contract.
- [`./habitat_quality_score.md`](./habitat_quality_score.md) — habitat quality score contract.
- [`./domain_observation.md`](./domain_observation.md) — domain observation envelope.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — identity and anti-collapse support.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — layer/view descriptor support.
- [`./domain_validation_report.md`](./domain_validation_report.md) — validation-report support.
- [`./habitat_patch.md`](./habitat_patch.md) — HabitatPatch contract.
- [`./connectivity_edge.md`](./connectivity_edge.md) — connectivity-edge contract.
- [`./corridor.md`](./corridor.md) — corridor contract.
- [`./land_cover/model_run_receipt.md`](./land_cover/model_run_receipt.md) — land-cover-specific receipt specialization.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat lane doctrine.
- [`../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md`](../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md) — source-role anti-collapse doctrine.
- [`../../../docs/domains/habitat/sublanes/suitability.md`](../../../docs/domains/habitat/sublanes/suitability.md) — suitability, model-card, receipt, and uncertainty doctrine.
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) — receipt/proof/catalog/publication separation doctrine.
- [`../../../schemas/contracts/v1/domains/habitat/model_run_receipt.schema.json`](../../../schemas/contracts/v1/domains/habitat/model_run_receipt.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
