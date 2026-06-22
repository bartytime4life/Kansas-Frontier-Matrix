<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-restoration-opportunity
title: Restoration Opportunity Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Restoration steward
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
policy_label: public-with-gates; semantic-contract; habitat; restoration-opportunity; candidate-site; evidence-bound; policy-aware; source-role-aware; sensitivity-aware; release-gated; rollback-aware
tags: [kfm, contracts, habitat, RestorationOpportunity, restoration_opportunity, restoration, candidate-site, opportunity-surface, habitat-patch, suitability, quality-score, connectivity, stewardship-zone, evidence, policy, sensitivity, release, correction, rollback]
related:
  - ./README.md
  - ./habitat_patch.md
  - ./habitat_quality_score.md
  - ./SuitabilityModel.md
  - ./connectivity_edge.md
  - ./corridor.md
  - ./stewardship_zone.md
  - ./ecological_system.md
  - ./land_cover_observation.md
  - ./model_run_receipt.md
  - ./uncertainty_surface.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./domain_validation_report.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/CANONICAL_PATHS.md
  - ../../../docs/domains/habitat/sublanes/README.md
  - ../../../docs/domains/habitat/sublanes/suitability.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../schemas/contracts/v1/domains/habitat/restoration_opportunity.schema.json
  - ../../../policy/domains/habitat/restoration.rego
  - ../../../policy/sensitivity/habitat/
  - ../../../fixtures/domains/habitat/restoration_opportunity/
  - ../../../tests/domains/habitat/test_restoration.*
  - ../../../data/registry/sources/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a thin scaffold at contracts/domains/habitat/restoration_opportunity.md."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/restoration_opportunity.schema.json, but remains a PROPOSED scaffold with empty properties and additionalProperties=true."
  - "Habitat doctrine confirms Restoration Opportunity as a canonical object family with purpose 'Restoration candidate site'; field realization remains PROPOSED."
  - "This contract defines a restoration candidate/opportunity object. It is not restoration approval, not a management order, not a land-access decision, not funding eligibility, not regulatory designation, and not public release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Restoration Opportunity Contract — Habitat

> Semantic contract for `RestorationOpportunity`: the Habitat candidate-site object that records where restoration may be worth review, why it may be worth review, which evidence supports that interpretation, and which policy, sensitivity, review, release, correction, and rollback gates must resolve before any public or operational use.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: RestorationOpportunity" src="https://img.shields.io/badge/object-RestorationOpportunity-blue">
  <img alt="Boundary: candidate not directive" src="https://img.shields.io/badge/boundary-candidate__not__directive-critical">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release__gated-critical">
</p>

`contracts/domains/habitat/restoration_opportunity.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Candidate vs decision objects](#candidate-vs-decision-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Evidence inputs](#evidence-inputs) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/restoration_opportunity.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/restoration_opportunity.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Truth posture:** Habitat doctrine confirms `Restoration Opportunity` as a canonical Habitat object family. Field shape, fixtures, validators, policy runtime, emitted instances, release artifacts, API/UI behavior, Focus Mode behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> A `RestorationOpportunity` is a candidate/evidence object. It must not be framed as permission to act, restoration approval, a management order, funding eligibility, land-access clearance, regulatory determination, emergency advice, or safety/legal instruction.

---

## Meaning

`RestorationOpportunity` records a Habitat-domain candidate site, area, patch, corridor segment, stewardship-adjacent unit, or modeled surface cell where restoration may be worth human review.

It answers:

- What place, patch, analysis unit, corridor segment, or public-safe generalized area is being proposed as a restoration opportunity?
- Which evidence supports the candidate: land cover, ecological system, habitat patch, quality score, suitability model, connectivity/corridor context, hydrology/soil context, stewardship context, or source observations?
- Which model, method, threshold, score, or review rule produced the candidate?
- Which source roles, source vintages, uncertainty surfaces, model-run receipts, policy decisions, and sensitivity controls must travel with the candidate?
- Which gate must be passed before the candidate can be rendered, summarized, exported, or published?

A restoration opportunity may support prioritization discussions, maps, review queues, and release candidates. It does not authorize restoration work.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Semantic meaning | `contracts/domains/habitat/restoration_opportunity.md` | Defines the Habitat object meaning and boundaries |
| Machine schema | `schemas/contracts/v1/domains/habitat/restoration_opportunity.schema.json` | CONFIRMED scaffold pointing to this contract path |
| Habitat doctrine | `docs/domains/habitat/README.md` | Confirms object-family membership, lifecycle, sensitivity, and publication posture |
| Canonical path map | `docs/domains/habitat/CANONICAL_PATHS.md` | Lists this object family and its contract/schema/policy/test paths |
| Sublane index | `docs/domains/habitat/sublanes/README.md` | Lists restoration opportunity as a Habitat sublane/object family candidate |
| Supporting objects | `habitat_patch`, `habitat_quality_score`, `SuitabilityModel`, `connectivity_edge`, `corridor`, `stewardship_zone`, `uncertainty_surface`, `model_run_receipt` | Inputs or companion objects; not owned by this file |
| Policy | `policy/domains/habitat/restoration.rego`, `policy/sensitivity/habitat/` | PROPOSED / NEEDS VERIFICATION admissibility and exposure gates |
| Evidence/proof | EvidenceBundle / ValidationReport / fixtures / tests | Must support consequential or public claims |
| Release | `release/manifests/habitat/` | Publication/correction/rollback authority; instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/restoration_opportunity.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Restoration Opportunity` |
| Schema properties | Empty object |
| Required fields | None visible in scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/MISSING_OR_PLANNED_FILES.md` |
| Contract doc pointer | `contracts/domains/habitat/restoration_opportunity.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this contract is semantic guidance and review vocabulary only.

---

## Candidate vs decision objects

A `RestorationOpportunity` is intentionally upstream of decision authority.

| Object or artifact | Meaning | Boundary |
|---|---|---|
| `RestorationOpportunity` | Candidate site/area/surface worth review. | This contract defines the candidate object. |
| `HabitatPatch` | Discrete habitat unit. | May be input/support, not automatically a restoration candidate. |
| `HabitatQualityScore` | Quality/condition score. | May support opportunity ranking; not a directive. |
| `SuitabilityModel` | Modeled suitability surface. | May support candidate generation; not observed or regulatory truth. |
| `ConnectivityEdge` / `Corridor` | Connectivity support. | May support restoration rationale; not restoration approval. |
| `StewardshipZone` | Stewardship/management context. | Context only unless policy/review grants use. |
| `ModelRunReceipt` | Run/process memory. | Required for derived/model candidates; not proof or release. |
| `UncertaintySurface` | Uncertainty/confidence support. | Must travel with modeled candidate outputs. |
| `PolicyDecision` | Allow/restrict/deny/abstain. | Policy decides exposure/eligibility posture; candidate does not. |
| `ReviewRecord` | Steward review. | Required where material; not the candidate itself. |
| `ReleaseManifest` | Publication authority. | Candidate may be released only through governed release. |

---

## Assertions

A reviewed `RestorationOpportunity` should semantically assert:

1. **Candidate identity** — deterministic ID from source/support refs, object role, spatial scope, temporal scope, method/config digest, and normalized candidate digest.
2. **Candidate geometry or scope** — exact, generalized, grid, watershed, patch, corridor segment, or other declared spatial support with exposure class.
3. **Opportunity rationale** — evidence-supported reason for candidacy, such as degraded quality, high suitability, corridor bottleneck, adjacency to protected habitat, hydrologic restoration context, invasive pressure, or other reviewed factor.
4. **Supporting evidence** — EvidenceRefs/EvidenceBundles for input observations, scores, models, patches, corridors, stewardship context, and source artifacts.
5. **Method support** — scoring method, model run receipt, thresholds, weights, config digest, model card/method card, and uncertainty refs where derived or modeled.
6. **Source-role lineage** — observed, modeled, regulatory, derivative, context, and candidate roles remain visible and never collapse.
7. **Temporal scope** — source, observed, valid, retrieval, run, release, and correction times remain distinct where material.
8. **Sensitivity posture** — exposure risk, rare-species joins, private-land context, cultural/archaeological context, and stewardship constraints are recorded and fail closed where unresolved.
9. **Review and policy posture** — review state, PolicyDecision, release state, correction path, and rollback target are visible before public use.
10. **Non-directive posture** — candidate status remains explicit; no operational action is implied.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating opportunity as approval | Approval/permission is outside this object; policy/review/release governs exposure only. |
| Treating opportunity as management order | KFM is not a management, emergency, legal, or safety authority. |
| Treating opportunity as funding eligibility | Funding/program rules require separate authoritative sources. |
| Treating opportunity as land-access clearance | Land ownership, title, and access permissions are separate governed domains/sources. |
| Treating opportunity as regulatory designation | Regulatory habitat/critical-habitat authority remains separate. |
| Treating model output as observed truth | Suitability/quality-derived candidates remain modeled/derived. |
| Treating sensitive exact geometry as public | Exact occurrence-linked or sensitive candidate geometry denies by default. |
| Treating source context as adopted Habitat truth | Soil, hydrology, agriculture, fauna, flora, hazards, archaeology, and land context keep their own ownership. |
| Treating a receipt as proof | Receipts record process; EvidenceBundle/proof support is separate. |
| Treating a map layer as the object | Map tiles, popups, screenshots, scenes, summaries, and AI text are delivery/interpretive surfaces. |
| Treating watcher output as published opportunity | Watchers may emit candidates; promotion is governed. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the confirmed scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM restoration-opportunity ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized digest of candidate semantics. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `RestorationOpportunity`. |
| `candidate_role` | candidate, review_candidate, public_safe_candidate, released_summary, or accepted enum. |
| `spatial_scope_ref` | Patch, polygon, corridor segment, grid cell, watershed, generalized geometry, or analysis unit. |
| `geometry_exposure_class` | exact, generalized, suppressed, delayed, steward_only, public_safe, or accepted enum. |
| `temporal_scope_ref` | Source/observed/valid/run/release/correction time bundle. |
| `supporting_object_refs` | HabitatPatch, HabitatQualityScore, SuitabilityModel, ConnectivityEdge, Corridor, StewardshipZone, LandCoverObservation, EcologicalSystem refs. |
| `external_context_refs` | Soil, hydrology, hazards, agriculture, flora/fauna, protected-area, or other governed context refs. |
| `source_descriptor_refs` | Source identity, role, rights, cadence, citation. |
| `evidence_refs` / `evidence_bundle_refs` | Evidence support for the candidate and rationale. |
| `rationale_codes` | Reason codes: low quality, high potential, connectivity bottleneck, riparian/wetland context, invasive pressure, fragmentation, etc. |
| `score_refs` | Quality/suitability/priority score refs where used. |
| `model_run_receipt_refs` | Required for modeled or derived candidate generation. |
| `uncertainty_refs` | Spatial/model/classification uncertainty refs. |
| `threshold_profile_ref` | Threshold/weighting profile used to classify opportunity. |
| `sensitivity_refs` | Sensitive join, rare species, private land, cultural/archaeological, stewardship, or infrastructure risk refs. |
| `policy_decision_refs` | PolicyDecision refs controlling exposure/release. |
| `review_record_ref` | Human/steward review state. |
| `release_ref` | ReleaseManifest / PromotionDecision ref if public. |
| `correction_refs` | CorrectionNotice/supersession refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing evidence, missing method, missing model receipt, missing uncertainty, sensitive exact geometry, source-role gap, release missing. |

---

## Evidence inputs

| Input class | Use in opportunity reasoning | Required caveat |
|---|---|---|
| `HabitatPatch` | Candidate unit or supporting spatial unit. | Patch is not automatically a restoration opportunity. |
| `LandCoverObservation` | Current/observed cover context. | Source role, class scheme, source vintage, valid-pixel footprint, and uncertainty travel with it. |
| `EcologicalSystem` | Ecological-system context. | Classification limits and source role remain visible. |
| `HabitatQualityScore` | Quality/condition support. | Score is descriptive, not prescriptive. |
| `SuitabilityModel` | Potential/fit support. | Model card, receipt, uncertainty, and model label required. |
| `ConnectivityEdge` / `Corridor` | Connectivity/corridor support. | Derived method and assumptions travel with the candidate. |
| `StewardshipZone` | Management/stewardship context. | Context only; not permission, ownership, or directive. |
| Fauna/Flora joins | Species or vegetation context. | Sensitive occurrences and rare plants fail closed unless generalized/reviewed. |
| Soil/Hydrology/Hazards/Agriculture | Context factors. | Ownership and source-role boundaries preserved. |

---

## Sensitivity and release

Restoration candidates can be sensitive even when each input appears public. Sensitivity can arise from rare-species habitat inference, exact occurrence-linked geometry, private-land implications, stewardship context, cultural/archaeological proximity, infrastructure implications, or public pressure on vulnerable locations.

Rules:

- Exact sensitive joins fail closed.
- Public products use generalized, redacted, aggregated, delayed, or steward-reviewed derivatives.
- Candidate maps must visibly label candidate status and must not imply action, permission, priority mandate, or regulatory status.
- Public-safe derivatives need EvidenceBundle support, validation, policy allow, review state where required, ReleaseManifest, correction path, and rollback target.
- AI/Focus Mode must `ABSTAIN` or `DENY` when source support, role, sensitivity, evidence, review, or release state is unresolved.

---

## Lifecycle

| Phase | RestorationOpportunity handling |
|---|---|
| RAW | Candidate inputs are captured as source payloads/refs with source role, rights, sensitivity, citation, time, and hash. |
| WORK / QUARANTINE | Candidate generation runs in work; unresolved rights, sensitivity, model/score gaps, missing uncertainty, or source-role ambiguity are quarantined. |
| PROCESSED | Validated candidates bind geometry/scope, rationale, evidence refs, method/receipt refs, uncertainty refs, policy refs, and review state. |
| CATALOG / TRIPLET | Catalog/triplet projections may point to candidates; they do not replace canonical objects or evidence. |
| RELEASE CANDIDATE | Public-safe candidate summaries/layers are assembled with ReleaseManifest, correction path, rollback target, and review/policy/evidence closure. |
| PUBLISHED | Only released public-safe artifacts are served through governed APIs and public UI surfaces; exact restricted candidates remain withheld or staged. |
| CORRECTED / SUPERSEDED | Source update, model/score change, sensitivity change, reviewer decision, policy change, or release withdrawal triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/habitat/restoration_opportunity.schema.json` beyond an empty scaffold.
- [ ] Confirm canonical source-role and candidate-role enum values.
- [ ] Confirm policy location and behavior for `policy/domains/habitat/restoration.rego` or equivalent.
- [ ] Add valid fixtures for patch-based, suitability-based, quality-score-based, connectivity-based, riparian/wetland-context, and public-safe generalized restoration candidates.
- [ ] Add invalid fixtures for missing evidence, missing method, missing model receipt, missing uncertainty, sensitive exact public geometry, source-role collapse, candidate-as-directive, candidate-as-regulatory, candidate-as-funding-eligibility, and release without rollback.
- [ ] Add validator checks for spatial scope, temporal scope, source roles, rationale codes, evidence refs, model receipts, uncertainty refs, policy decisions, review records, release refs, correction refs, and rollback refs.
- [ ] Confirm public UI labels candidate status clearly and prevents management/directive wording.
- [ ] Confirm Focus Mode abstains when evidence, sensitivity, policy, review, or release support is missing.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Candidate, evidence, method, sensitivity, policy, review, release, correction, and rollback resolve | `ANSWER` / public-safe candidate may support a claim |
| Evidence, method, uncertainty, sensitivity, review, release, or rollback support is incomplete | `ABSTAIN` / `HOLD` |
| Candidate-as-directive, sensitive exact public exposure, source-role collapse, role-as-regulatory, or release bypass would occur | `DENY` |
| Schema, validator, source read, digest, evidence lookup, policy lookup, review lookup, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Target scaffold | Confirms `restoration_opportunity.md` existed as scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms `restoration_opportunity.schema.json` path and that it points to this contract. | Does not prove field-level validation. |
| Habitat README | Confirms `Restoration Opportunity` as a canonical Habitat object family and confirms lifecycle/sensitivity/publication posture. | Field realization remains PROPOSED. |
| Habitat sublane index | Confirms restoration opportunity is treated as a Habitat object-family sublane candidate. | Sublane paths remain PROPOSED / NEEDS VERIFICATION. |
| Habitat canonical paths | Confirms proposed contract/schema/policy/test path mapping and schema-home conflict. | Path realization and enforcement remain partly PROPOSED. |
| User-provided authoring role | Requires evidence-grounded repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a restoration candidate or candidate-dependent output weakens source-role integrity, evidence support, method transparency, uncertainty posture, sensitivity posture, policy/review separation, release governance, or public wording boundaries.

Rollback triggers include source update; candidate-geometry correction; score/model correction; threshold/config correction; missing model receipt; missing uncertainty; source-role correction; private-land or stewardship misinterpretation; sensitive exact geometry exposure; rare-species/rare-plant inference exposure; candidate presented as directive, approval, funding eligibility, land-access permission, or regulatory designation; public API/UI/AI exposure without release/correction/rollback refs; watcher-as-publisher; tile/popup/vector-index/AI-as-truth; or missing evidence/policy/review closure.

Rollback artifacts should include affected candidate IDs, supporting object refs, source refs, source-role refs, rationale refs, method/config refs, model-run receipts, uncertainty refs, evidence refs, validation reports, policy decisions, review records, release refs, correction notices, rollback cards, replacement candidates, suppression instructions, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which `candidate_role` values are canonical for restoration opportunity? | NEEDS VERIFICATION | Contract/schema/policy review. |
| Which source families and supporting objects may generate restoration candidates first? | NEEDS VERIFICATION | Habitat steward + Source steward activation review. |
| Which model-card/method-card fields are required when candidates are model-derived? | NEEDS VERIFICATION | Suitability/model-run receipt schema review. |
| Which public geometry exposure classes are allowed for restoration candidates? | NEEDS VERIFICATION | Sensitivity/release policy review. |
| Is `policy/domains/habitat/restoration.rego` the accepted policy path? | NEEDS VERIFICATION | Policy root inspection and ADR/path review. |
| Can any restoration candidate ever be public at exact geometry? | NEEDS VERIFICATION | Sensitivity, rights, stewardship, and release review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contract root.
- [`./habitat_patch.md`](./habitat_patch.md) — habitat patch contract.
- [`./habitat_quality_score.md`](./habitat_quality_score.md) — quality score contract.
- [`./SuitabilityModel.md`](./SuitabilityModel.md) — suitability model contract.
- [`./connectivity_edge.md`](./connectivity_edge.md) — connectivity edge contract.
- [`./corridor.md`](./corridor.md) — corridor contract.
- [`./model_run_receipt.md`](./model_run_receipt.md) — model-run receipt contract.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — identity and anti-collapse support.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — layer/view descriptor support.
- [`./domain_validation_report.md`](./domain_validation_report.md) — validation-report support.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat lane doctrine.
- [`../../../docs/domains/habitat/CANONICAL_PATHS.md`](../../../docs/domains/habitat/CANONICAL_PATHS.md) — Habitat canonical path map.
- [`../../../docs/domains/habitat/sublanes/README.md`](../../../docs/domains/habitat/sublanes/README.md) — Habitat sublane index.
- [`../../../schemas/contracts/v1/domains/habitat/restoration_opportunity.schema.json`](../../../schemas/contracts/v1/domains/habitat/restoration_opportunity.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
