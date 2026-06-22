<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-habitat-quality-score
title: Habitat Quality Score Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Suitability steward
  - OWNER_TBD — Habitat Quality Score steward
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
policy_label: public-with-gates; semantic-contract; habitat; habitat-quality-score; modeled-or-reviewed-score; source-role-aware; evidence-bound; uncertainty-bound; release-gated; non-regulatory; non-prescriptive
tags: [kfm, contracts, habitat, HabitatQualityScore, habitat_quality_score, habitat-quality-score, quality, suitability, score, model-card, model-run-receipt, uncertainty-surface, source-role, evidence, policy, sensitivity, geoprivacy, release, correction, rollback, anti-collapse]
related:
  - ./README.md
  - ./habitat_patch.md
  - ./habitat-patch.contract.md
  - ./SuitabilityModel.md
  - ./suitability_model.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./domain_validation_report.md
  - ./ecological_system.md
  - ./connectivity_edge.md
  - ./corridor.md
  - ./land_cover/observation.md
  - ./land_cover/model_run_receipt.md
  - ./land_cover/uncertainty.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../docs/domains/habitat/sublanes/patch.md
  - ../../../docs/domains/habitat/sublanes/suitability.md
  - ../../../schemas/contracts/v1/domains/habitat/habitat_quality_score.schema.json
  - ../../../policy/domains/habitat/
  - ../../../policy/sensitivity/habitat/
  - ../../../fixtures/domains/habitat/habitat_quality_score/
  - ../../../tests/domains/habitat/habitat_quality_score/
  - ../../../data/registry/sources/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a scaffold at contracts/domains/habitat/habitat_quality_score.md."
  - "This path is the contract_doc path currently referenced by schemas/contracts/v1/domains/habitat/habitat_quality_score.schema.json."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/habitat_quality_score.schema.json, but it is still a PROPOSED scaffold with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "Habitat Quality Score is a scalar or categorical patch-quality measure in the Habitat object-family spine. It is descriptive and evidence-bound, not a management instruction, not regulatory critical habitat, not observed occurrence truth, not a raw model surface, not a HabitatPatch identity, and not release authority."
  - "Open doctrine question: whether HabitatQualityScore always implies model role or may be observed/reviewed from field survey quality remains NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Quality Score Contract — Habitat

> Semantic contract for `HabitatQualityScore`: a governed scalar or categorical Habitat measure attached to a declared patch, place, model output, or public-safe aggregate, preserving source role, scoring method, evidence, uncertainty, sensitivity posture, release state, correction lineage, and rollback support.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: Habitat Quality Score" src="https://img.shields.io/badge/object-Habitat_Quality_Score-blue">
  <img alt="Role: descriptive score" src="https://img.shields.io/badge/role-descriptive__score-6f42c1">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: not management instruction" src="https://img.shields.io/badge/boundary-not__management__instruction-critical">
</p>

`contracts/domains/habitat/habitat_quality_score.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Score vs nearby objects](#score-vs-nearby-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Scoring support](#scoring-support) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/habitat_quality_score.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/habitat_quality_score.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Truth posture:** Habitat doctrine confirms `Habitat Quality Score` as a canonical Habitat object-family term and suitability docs treat it as a suitability-central object. Field-level schema shape, fixtures, validators, source registry activation, policy runtime, release artifacts, map/UI behavior, Focus Mode behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> A `HabitatQualityScore` is descriptive, never prescriptive. It does not tell a manager what to do, does not assert species occurrence, does not designate regulatory critical habitat, does not replace patch identity, does not erase model uncertainty, and does not publish itself.

---

## Meaning

`HabitatQualityScore` records a quality value, class, band, index, or score attached to a declared Habitat scope, such as a `HabitatPatch`, public-safe aggregate, model output, or reviewed analysis unit.

It answers:

- What habitat unit or public-safe scope is being scored?
- What does the score measure: quality, integrity, condition, suitability, resilience, degradation, restoration potential, or another declared metric?
- Which scoring method, source inputs, source roles, model run, review state, and uncertainty support the score?
- Whether the score is observed/reviewed, modeled, derived, aggregate, or context-driven.
- Which EvidenceRefs, EvidenceBundles, validation reports, policy decisions, review records, release manifests, correction notices, and rollback targets govern consequential use?

A score may support Habitat reasoning, map views, and Focus Mode explanations, but it must remain visibly bounded by scoring method, source role, uncertainty, scope, and release state.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Habitat Quality Score meaning | `contracts/domains/habitat/habitat_quality_score.md` | Schema-aligned semantic contract |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/habitat_quality_score.schema.json` | CONFIRMED scaffold; field shape not enforced |
| Habitat object-family doctrine | `docs/domains/habitat/README.md` | Names Habitat Quality Score as a canonical object family |
| Suitability doctrine | `docs/domains/habitat/sublanes/suitability.md` | Treats Habitat Quality Score as suitability-central modeled/governed object |
| Model-vs-observation doctrine | `docs/domains/habitat/MODEL_VS_OBSERVATION.md` | Requires source-role anti-collapse and states score is descriptive, not prescriptive |
| Patch support | `contracts/domains/habitat/habitat_patch.md` | Score usually attaches to a patch or public-safe patch aggregate |
| Suitability support | `contracts/domains/habitat/SuitabilityModel.md` | Score may be derived from or used by a suitability model |
| Model receipt support | `contracts/domains/habitat/land_cover/model_run_receipt.md` or future Habitat-wide receipt contract | Required when score is model-derived; exact home NEEDS VERIFICATION |
| Uncertainty support | `contracts/domains/habitat/land_cover/uncertainty.md` or future Habitat-wide uncertainty contract | Required where modeled/derived score uncertainty is material |
| Policy | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Expected role-collapse and sensitivity gates; contents NEEDS VERIFICATION |
| Release | `release/` / `release/manifests/habitat/` | Expected release/correction/rollback authority; instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/habitat_quality_score.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Habitat Quality Score` |
| Schema properties | Empty object |
| Required fields | None visible in the scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/MISSING_OR_PLANNED_FILES.md` |
| Contract doc pointer | `contracts/domains/habitat/habitat_quality_score.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this file is semantic guidance and review vocabulary only.

---

## Score vs nearby objects

| Object / artifact | What it owns | Boundary |
|---|---|---|
| `HabitatQualityScore` | Scored condition/quality/suitability-like measure over a declared Habitat scope. | This contract. |
| `HabitatPatch` | Discrete habitat unit identity and geometry. | Score may attach to patch; not patch identity. |
| `SuitabilityModel` | Modeled suitability surface/model family. | Score may derive from model; not model definition by itself. |
| `ModelRunReceipt` | Auditable run record. | Required companion for model-derived scores. |
| `UncertaintySurface` | Spatial or score uncertainty. | Must not be dropped from modeled/derived score release. |
| `LandCoverObservation` | Observed land-cover evidence. | May support score inputs; not the score itself. |
| `EcologicalSystem` | Ecological-system classification. | May support quality context; not score truth by itself. |
| `ConnectivityEdge` / `Corridor` | Connectivity relations/geometries. | May consume or contextualize scores; not score authority. |
| Regulatory critical habitat | Authority designation. | A quality score is not a designation. |
| Fauna/Flora occurrence | Species occurrence truth. | Score may use public-safe context only under policy/geoprivacy. |
| Map layer / tile / popup | Delivery surface. | Never score truth or release authority. |

---

## Assertions

A reviewed `HabitatQualityScore` should semantically assert:

1. **Scored subject** — patch, aggregate, grid cell, model output, stewardship unit, or public-safe scope.
2. **Score value** — numeric value, class, band, rank, confidence category, or enum.
3. **Score meaning** — quality, condition, suitability, integrity, restoration potential, degradation, resilience, or another declared metric.
4. **Scoring method** — field review, rule set, model, weighted index, crosswalk, expert assessment, or aggregate method.
5. **Source role** — observed/reviewed, model, derivative, aggregate, context, regulatory-context, candidate, synthetic, or accepted enum.
6. **Source support** — SourceDescriptor refs, source record refs, source vintage, method citation, rights, and authority limits.
7. **Evidence support** — EvidenceRef/EvidenceBundle refs before consequential use.
8. **Uncertainty support** — uncertainty bounds, score confidence, validation metrics, model card, receipt, and caveats where material.
9. **Policy support** — sensitivity, rights, source-role, geometry exposure, and release policy decisions where material.
10. **Release support** — ReleaseManifest, public artifact refs, correction path, and rollback target before public use.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating score as management instruction | KFM is not a management or alert authority. |
| Treating score as regulatory critical habitat | Score is not an authority designation. |
| Treating score as species occurrence | Fauna/Flora own occurrence truth. |
| Treating score as observed fact when model-derived | Hides assumptions and uncertainty. |
| Dropping uncertainty to simplify public display | Misrepresents confidence as fact. |
| Treating score as patch identity | Patch identity and geometry are separate. |
| Treating candidate score as public | Candidate material remains WORK/QUARANTINE or review-only. |
| Treating AI-computed score as source truth | AI is interpretive and evidence-subordinate. |
| Treating schema scaffold as implemented validator | Current schema is only a scaffold. |
| Treating score as release authority | Release decisions live under release/governance objects. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the confirmed scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM habitat quality score ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized digest over score-relevant content. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `HabitatQualityScore`. |
| `score_id` | Stable score identifier. |
| `scored_subject_ref` | HabitatPatch, aggregate, grid cell, model output, or public-safe scope being scored. |
| `scored_subject_kind` | patch, aggregate, model_output, grid_cell, stewardship_unit, analysis_unit, or accepted enum. |
| `score_value` | Numeric score or categorical value. |
| `score_unit` | Unit or unitless index description. |
| `score_class` | low/medium/high, poor/fair/good, unsuitable/marginal/suitable, or accepted enum. |
| `score_direction` | Whether higher means better, worse, more suitable, more degraded, etc. |
| `score_metric` | quality, condition, suitability, integrity, restoration_potential, degradation, resilience, or accepted enum. |
| `score_method_ref` | Method, model card, ruleset, field protocol, or weighted-index spec. |
| `source_descriptor_refs` | Source identity, role, rights, cadence, attribution, authority limits. |
| `source_record_refs` | Source-native raster/vector/table/report/API refs. |
| `source_role` | observed, reviewed, model, derivative, aggregate, administrative, candidate, synthetic, context, regulatory-context, or accepted enum. |
| `habitat_patch_refs` | Patches scored or consumed. |
| `suitability_model_refs` | SuitabilityModel refs when score is model-derived. |
| `model_run_receipt_ref` | Required where scoring is model-derived. |
| `model_card_ref` | Model-card or method-card ref where required. |
| `uncertainty_refs` | UncertaintySurface or score-confidence refs. |
| `validation_metric_refs` | Validation metric or calibration refs. |
| `input_evidence_refs` | Inputs used in scoring. |
| `evidence_refs` / `evidence_bundle_refs` | Evidence closure refs behind consequential use. |
| `spatial_scope_ref` | Declared spatial support. |
| `public_geometry_ref` | Public-safe geometry if score is mapped. |
| `source_time` / `observed_time` / `valid_time` / `retrieval_time` / `release_time` / `correction_time` | Distinct time dimensions; do not collapse. |
| `policy_decision_ref` | PolicyDecision where material. |
| `redaction_receipt_refs` | Generalization/redaction receipts for public mapped scores. |
| `review_record_ref` | Steward review record. |
| `release_ref` | ReleaseManifest or PromotionDecision ref. |
| `correction_refs` | CorrectionNotice, recalculation, supersession, replacement score refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing source, unresolved role, missing model receipt, missing uncertainty, sensitive exact exposure, stale inputs, release missing. |

---

## Scoring support

| Support family | Likely role | Required handling |
|---|---|---|
| Field review / inventory quality notes | observed / reviewed | Keep reviewer, date, method, scope, and limits visible. |
| Land-cover observations | observed / context | Preserve source vintage and class scheme. |
| Ecological systems | observed/model/context depending source | Keep class scheme and source role visible. |
| Suitability models | model | Require model card, ModelRunReceipt, uncertainty, validation, and public modeled label. |
| Soil / Hydrology / Hazards context | context | Consumed through governed joins; source domains retain ownership. |
| Fauna/Flora occurrence context | context only, public-safe | Geoprivacy/sensitivity gates apply; never occurrence truth. |
| Stewardship/administrative context | administrative/context | May constrain interpretation or release; not habitat truth by itself. |
| AI-generated score | synthetic/candidate | Not source truth; requires review, evidence, and validation. |

---

## Source-role rules

| Role | HabitatQualityScore handling | Failure mode |
|---|---|---|
| `observed` / `reviewed` | Score comes from direct field/inventory review or reviewed protocol. | Review-as-regulatory or missing protocol. |
| `model` / `modeled` | Score comes from model under stated assumptions. | Modeled-as-observed or modeled-as-regulatory. |
| `derivative` | Score is computed from other KFM objects. | Derived-as-primary source. |
| `aggregate` | Score is summarized over public-safe unit. | Aggregate-as-exact. |
| `context` | Score consumes context from another domain. | Habitat adopts neighboring-lane truth. |
| `candidate` | Unreviewed model/pipeline output. | Candidate-as-public. |
| `synthetic` | AI/simulated score. | Synthetic-as-source. |
| `regulatory-context` | Score references regulatory layer as context only. | Score-as-designation. |

---

## Sensitivity and release

Quality scores can reveal sensitive habitat indirectly when attached to exact patches, rare-species context, private stewardship details, or high-resolution modeled habitat.

Rules:

- A public score must not reveal sensitive exact habitat or occurrence-linked geometry.
- Public mapped scores must use released public-safe geometries or aggregates.
- Modeled scores must stay labeled as modeled, with uncertainty and model/run support visible.
- Scores without sufficient evidence, source role, uncertainty, policy, release state, or rollback support must not be promoted.
- AI/Focus Mode may summarize only released evidence-backed scores and must `ABSTAIN` or `DENY` when support or policy is insufficient.
- A score may support review or prioritization discussion, but it is not a management instruction.

---

## Lifecycle

| Phase | HabitatQualityScore handling |
|---|---|
| RAW | Source inputs, scoring protocol/model, score payload, source role, rights, sensitivity, citation, time, and hashes are captured but not public truth. |
| WORK / QUARANTINE | Candidate score is normalized; missing method, missing receipt, unresolved role, missing uncertainty, rights gaps, or sensitivity failures are held with reasons. |
| PROCESSED | Reviewed score binds subject, method, role, spatial/temporal scope, input digests, evidence refs, validation report, policy posture, uncertainty, and correction state. |
| CATALOG / TRIPLET | Score claims may be projected only with EvidenceBundle refs, source-role caveats, uncertainty, and public-safe geometry posture. |
| RELEASE CANDIDATE | Public score layers/API payloads require policy/review, public-safe geometry or aggregate, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe score objects or derivatives appear through governed APIs, map surfaces, Evidence Drawer, Focus Mode, or reports. |
| CORRECTED / SUPERSEDED | Source update, model update, method correction, recalculation, geometry correction, evidence correction, policy change, or release withdrawal triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/habitat/habitat_quality_score.schema.json` beyond an empty scaffold.
- [ ] Decide whether `HabitatQualityScore` always implies modeled output or may also be observed/reviewed from field protocols.
- [ ] Confirm canonical source-role enum spelling, including `model` vs `modeled` and `authority` vs `regulatory`.
- [ ] Define model-card / method-card requirements for score-generating models or scoring protocols.
- [ ] Add valid fixtures for reviewed field score, model-derived score, patch-level score, aggregate score, public-safe mapped score, and corrected/recalculated score.
- [ ] Add invalid fixtures for missing scored subject, missing method, missing source role, modeled-as-observed, modeled-as-regulatory, score-as-management-instruction, missing model receipt, missing uncertainty, sensitive exact public exposure, candidate-as-public, and missing rollback target.
- [ ] Add validator checks for score value/class, score direction, scored subject, method/model refs, evidence refs, policy refs, uncertainty refs, release refs, and correction lineage.
- [ ] Add tests proving public map/UI/AI surfaces cannot present scores as regulatory critical habitat, species occurrence, management instruction, or source-free truth.
- [ ] Confirm release tests proving public clients consume released public-safe score artifacts only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Subject, method, role, scope, evidence, uncertainty, policy, release, and rollback all resolve | `ANSWER` / public-safe score may support a claim |
| Evidence, role, method, uncertainty, rights, sensitivity, release, or rollback support is incomplete | `ABSTAIN` / `HOLD` |
| Role collapse, sensitive leak, candidate public path, missing uncertainty, management-instruction framing, or release bypass would occur | `DENY` |
| Schema, validator, source read, digest, evidence lookup, model receipt lookup, policy lookup, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Target scaffold | Confirms `habitat_quality_score.md` existed as scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms `habitat_quality_score.schema.json` path and that schema points to this contract path. | Does not prove field-level validation. |
| Habitat README | Confirms Habitat Quality Score as a canonical object family and confirms source/observed/valid/retrieval/release/correction time separation. | Field realization remains PROPOSED. |
| Suitability sublane | Confirms score is suitability-central and governed as evidence-supported, time-aware, public-safe claim. | Sublane path and model-card requirements remain partly NEEDS VERIFICATION. |
| Model-vs-observation doc | Confirms anti-collapse role separation, descriptive-not-prescriptive posture, and open question about whether quality scores are always modeled. | Exact schema/policy/test enforcement remains NEEDS VERIFICATION. |
| User-provided authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized score weakens method integrity, source-role separation, evidence support, uncertainty posture, sensitivity posture, or release integrity.

Rollback triggers include score value/class recalculation; method/model change; missing/changed model-run receipt; missing/changed uncertainty; source-role, source-vintage, temporal-scope, artifact-digest, evidence, policy, or release corrections; modeled score shown as observed/regulatory; score presented as occurrence, critical habitat, management instruction, or patch identity; sensitive exact score geometry leaked publicly; candidate score appeared in public API/UI/AI path; tile/popup/AI/vector-index-as-truth; or missing release/correction/rollback refs.

Rollback artifacts should include affected score IDs, scored subject refs, method/model refs, model-run receipt refs, uncertainty refs, source refs, source-role refs, temporal-scope refs, artifact digests, evidence refs, validation reports, policy decisions, redaction receipts, release refs, correction notices, rollback cards, replacement scores, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Does `HabitatQualityScore` always imply `model` role, or can field-reviewed quality scores be `observed` / `reviewed`? | NEEDS VERIFICATION | Habitat steward + schema/policy review. |
| Which fields must be required in `habitat_quality_score.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| What is the canonical model-card or method-card field set for score-producing models/protocols? | NEEDS VERIFICATION | Suitability contract/schema/policy review. |
| Which score classes and directions are allowed? | NEEDS VERIFICATION | Domain steward + schema enum review. |
| Which public geometry/aggregation roles are allowed for mapped scores? | NEEDS VERIFICATION | Policy, redaction, and release review. |
| Which source families are activated first for Habitat Quality Score? | NEEDS VERIFICATION | Source activation decision and SourceDescriptor review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contracts root.
- [`./habitat_patch.md`](./habitat_patch.md) — HabitatPatch contract.
- [`./SuitabilityModel.md`](./SuitabilityModel.md) — modeled suitability contract.
- [`./domain_observation.md`](./domain_observation.md) — domain observation envelope.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — deterministic identity and anti-collapse support.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — layer/view descriptor support.
- [`./domain_validation_report.md`](./domain_validation_report.md) — validation-report support.
- [`./ecological_system.md`](./ecological_system.md) — ecological-system classification contract.
- [`./land_cover/model_run_receipt.md`](./land_cover/model_run_receipt.md) — model-run receipt semantics currently under land-cover; cross-sublane home NEEDS VERIFICATION.
- [`./land_cover/uncertainty.md`](./land_cover/uncertainty.md) — uncertainty semantics currently under land-cover; cross-sublane home NEEDS VERIFICATION.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat lane doctrine.
- [`../../../docs/domains/habitat/sublanes/suitability.md`](../../../docs/domains/habitat/sublanes/suitability.md) — suitability and quality-score doctrine.
- [`../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md`](../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md) — source-role anti-collapse doctrine.
- [`../../../schemas/contracts/v1/domains/habitat/habitat_quality_score.schema.json`](../../../schemas/contracts/v1/domains/habitat/habitat_quality_score.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
