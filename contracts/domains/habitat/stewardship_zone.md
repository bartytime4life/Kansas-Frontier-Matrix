<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-stewardship-zone
title: StewardshipZone Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Stewardship steward
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
policy_label: public-with-gates; semantic-contract; habitat; stewardship-zone; management-context; evidence-bound; policy-aware; source-role-aware; sensitivity-aware; release-gated; rollback-aware; non-directive
tags: [kfm, contracts, habitat, StewardshipZone, stewardship_zone, stewardship, management-context, administrative-context, access-sensitive, habitat-patch, restoration-opportunity, evidence, policy, sensitivity, release, correction, rollback, anti-collapse]
related:
  - ./README.md
  - ./habitat_patch.md
  - ./restoration_opportunity.md
  - ./habitat_quality_score.md
  - ./SuitabilityModel.md
  - ./connectivity_edge.md
  - ./corridor.md
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
  - ../../../docs/architecture/ecology-cross-domain.md
  - ../../../schemas/contracts/v1/domains/habitat/stewardship_zone.schema.json
  - ../../../policy/domains/habitat/stewardship_zone.rego
  - ../../../policy/sensitivity/habitat/
  - ../../../fixtures/domains/habitat/stewardship_zone/
  - ../../../tests/domains/habitat/test_stewardship_zone.*
  - ../../../data/registry/sources/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a thin scaffold at contracts/domains/habitat/stewardship_zone.md."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/stewardship_zone.schema.json, but remains a PROPOSED scaffold with empty properties and additionalProperties=true."
  - "Habitat doctrine confirms StewardshipZone as a canonical object family with purpose 'Stewardship / management context'; field realization remains PROPOSED."
  - "This contract defines stewardship context and exposure rules. It is not land ownership, title, access permission, restoration approval, funding eligibility, regulatory designation, or management instruction."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# StewardshipZone Contract — Habitat

> Semantic contract for `StewardshipZone`: the Habitat context object that records a stewardship, management, administrative, conservation, or access-sensitive zone as evidence-bound context for Habitat reasoning without turning that context into land ownership, public access permission, restoration approval, management direction, or release authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: StewardshipZone" src="https://img.shields.io/badge/object-StewardshipZone-blue">
  <img alt="Boundary: context not permission" src="https://img.shields.io/badge/boundary-context__not__permission-critical">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release__gated-critical">
</p>

`contracts/domains/habitat/stewardship_zone.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Context vs decision objects](#context-vs-decision-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Evidence inputs](#evidence-inputs) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/stewardship_zone.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/stewardship_zone.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Truth posture:** Habitat doctrine confirms `StewardshipZone` as a canonical Habitat object family. Field shape, fixtures, validators, policy runtime, emitted instances, release artifacts, API/UI behavior, Focus Mode behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> A `StewardshipZone` is context. It must not be treated as land title, land ownership, public access permission, site-entry authorization, restoration approval, funding eligibility, regulatory determination, emergency advice, or management instruction.

---

## Meaning

`StewardshipZone` records a Habitat-domain stewardship or management-context area used to interpret Habitat objects and public-safe derivatives.

It may describe:

- conservation or stewardship program boundaries;
- managed habitat areas;
- restoration-planning context;
- protected-area or conservation-area context;
- public-safe stewardship summaries;
- access-sensitive exact zones withheld from public output;
- administrative or review zones used to route policy decisions;
- context for HabitatPatch, RestorationOpportunity, SuitabilityModel, Corridor, ConnectivityEdge, or HabitatQualityScore interpretation.

It answers:

- Which stewardship or management-context area is being referenced?
- Which source, source role, rights posture, temporal scope, and geometry exposure class support it?
- Which Habitat objects, public-safe layers, or candidate reviews may cite it?
- Which access, sensitivity, ownership, cultural, ecological, or infrastructure risks are triggered by public exposure?
- Which EvidenceRefs, EvidenceBundles, validation reports, policy decisions, review records, release manifests, correction notices, and rollback targets govern use?

A stewardship zone may help interpret candidate restoration or habitat context. It does not authorize action.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Semantic meaning | `contracts/domains/habitat/stewardship_zone.md` | Defines the Habitat object meaning and boundaries |
| Machine schema | `schemas/contracts/v1/domains/habitat/stewardship_zone.schema.json` | CONFIRMED scaffold pointing to this contract path |
| Habitat doctrine | `docs/domains/habitat/README.md` | Confirms object-family membership, lifecycle, sensitivity, and publication posture |
| Canonical path map | `docs/domains/habitat/CANONICAL_PATHS.md` | Lists this object family and its contract/schema/policy/test paths |
| Sublane index | `docs/domains/habitat/sublanes/README.md` | Lists stewardship zone as a Habitat sublane/object family candidate |
| Cross-domain ecology doctrine | `docs/architecture/ecology-cross-domain.md` | Reinforces atomic ownership and cross-domain composition boundaries |
| Supporting objects | `habitat_patch`, `restoration_opportunity`, `habitat_quality_score`, `SuitabilityModel`, `connectivity_edge`, `corridor`, `uncertainty_surface`, `model_run_receipt` | Inputs or companion objects; not owned by this file |
| Policy | `policy/domains/habitat/stewardship_zone.rego`, `policy/sensitivity/habitat/` | PROPOSED / NEEDS VERIFICATION admissibility and exposure gates |
| Evidence/proof | EvidenceBundle / ValidationReport / fixtures / tests | Must support consequential or public claims |
| Release | `release/manifests/habitat/` | Publication/correction/rollback authority; instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/stewardship_zone.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Stewardship Zone` |
| Schema properties | Empty object |
| Required fields | None visible in scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/MISSING_OR_PLANNED_FILES.md` |
| Contract doc pointer | `contracts/domains/habitat/stewardship_zone.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this contract is semantic guidance and review vocabulary only.

---

## Context vs decision objects

A `StewardshipZone` is intentionally separate from ownership, access, operations, and release authority.

| Object or artifact | Meaning | Boundary |
|---|---|---|
| `StewardshipZone` | Habitat stewardship/management context area. | This contract defines context semantics. |
| `HabitatPatch` | Discrete habitat unit. | May overlap zone; not automatically stewardship context. |
| `RestorationOpportunity` | Candidate site worth review. | May cite zone; zone does not approve restoration. |
| `HabitatQualityScore` | Quality/condition score. | May be summarized by zone; not zone authority. |
| `SuitabilityModel` | Modeled suitability surface. | May be interpreted by zone; model remains modeled. |
| `ConnectivityEdge` / `Corridor` | Connectivity support. | May cross zones; zone does not certify movement. |
| Land/title/access record | Ownership or legal/access authority. | Outside this contract; must come from owning source/domain. |
| `PolicyDecision` | Allow/restrict/deny/abstain. | Policy controls exposure/use; zone does not. |
| `ReviewRecord` | Steward review. | Required where material; not the zone itself. |
| `ReleaseManifest` | Publication authority. | Public zone layer requires governed release. |

---

## Assertions

A reviewed `StewardshipZone` should semantically assert:

1. **Zone identity** — deterministic ID from source/support refs, object role, spatial scope, temporal scope, source role, and normalized digest.
2. **Zone role** — stewardship_context, management_context, administrative_context, conservation_context, review_zone, public_safe_summary, restricted_exact_zone, or accepted enum.
3. **Geometry or scope** — exact, generalized, aggregate, watershed, grid, public-safe, delayed, withheld, or steward-only spatial support.
4. **Source and rights support** — SourceDescriptor refs, source record refs, rights, citation, source role, source vintage, and authority limits.
5. **Context support** — HabitatPatch, RestorationOpportunity, HabitatQualityScore, SuitabilityModel, ConnectivityEdge, Corridor, EcologicalSystem, LandCoverObservation, or other context refs where material.
6. **Temporal scope** — source, observed, valid, retrieval, release, and correction times remain distinct where material.
7. **Sensitivity posture** — exact location, private/steward-only context, rare-species joins, rare plants, cultural/archaeological proximity, infrastructure, or access-sensitive risks are recorded and fail closed where unresolved.
8. **Evidence support** — EvidenceRefs/EvidenceBundles for the zone and any public interpretation.
9. **Review and policy posture** — review state, PolicyDecision, release state, correction path, and rollback target before public use.
10. **Non-permission posture** — public or private access, ownership, legal status, and management authority are never inferred from the zone alone.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating zone as land ownership/title | Ownership/title requires separate authoritative evidence. |
| Treating zone as public access permission | Access requires explicit source authority; this object is context. |
| Treating zone as restoration approval | RestorationOpportunity/review/release are separate, and none imply operational approval. |
| Treating zone as management order | KFM is not a management, emergency, legal, or safety authority. |
| Treating zone as funding eligibility | Funding/program eligibility requires separate authoritative source. |
| Treating zone as regulatory designation | Regulatory authority remains separate and source-role-specific. |
| Treating zone as habitat truth | Zone is context; habitat truth stays with HabitatPatch, observations, scores, models, etc. |
| Treating sensitive exact geometry as public | Exact sensitive stewardship context denies by default. |
| Treating source context as adopted Habitat truth | Soil, hydrology, agriculture, fauna, flora, hazards, archaeology, infrastructure, and land/title domains retain ownership. |
| Treating a map layer as the object | Tiles, popups, screenshots, summaries, and AI text are delivery/interpretive surfaces. |
| Treating watcher output as published zone | Watchers may emit candidates; promotion is governed. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the confirmed scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM stewardship-zone ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized digest of zone semantics. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `StewardshipZone`. |
| `zone_role` | stewardship_context, management_context, administrative_context, conservation_context, review_zone, restricted_exact_zone, public_safe_summary, or accepted enum. |
| `spatial_scope_ref` | Polygon, patch set, corridor segment, watershed, grid, administrative zone, generalized geometry, or analysis unit. |
| `geometry_exposure_class` | exact, generalized, aggregate, suppressed, delayed, steward_only, public_safe, or accepted enum. |
| `temporal_scope_ref` | Source/observed/valid/retrieval/release/correction time bundle. |
| `source_descriptor_refs` | Source identity, role, rights, cadence, citation. |
| `source_record_refs` | Source-native table, GIS layer, report, agreement, program boundary, or API refs. |
| `authority_limit_note` | Human-readable limit on what the source can and cannot authorize. |
| `supporting_object_refs` | HabitatPatch, RestorationOpportunity, HabitatQualityScore, SuitabilityModel, ConnectivityEdge, Corridor, LandCoverObservation, EcologicalSystem refs. |
| `external_context_refs` | Soil, hydrology, hazards, agriculture, flora/fauna, land/title/access, cultural/archaeological, or infrastructure context refs. |
| `evidence_refs` / `evidence_bundle_refs` | Evidence support for the zone and any public interpretation. |
| `sensitivity_refs` | Private/steward-only, rare species, rare plants, cultural/archaeological, infrastructure, access, or rights risk refs. |
| `policy_decision_refs` | PolicyDecision refs controlling exposure/release. |
| `review_record_ref` | Human/steward review state. |
| `release_ref` | ReleaseManifest / PromotionDecision ref if public. |
| `correction_refs` | CorrectionNotice/supersession refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing source, missing authority limits, rights unknown, access ambiguity, sensitive exact geometry, source-role gap, release missing. |

---

## Evidence inputs

| Input class | Use in stewardship-zone reasoning | Required caveat |
|---|---|---|
| Program or stewardship boundary | Core zone source. | Does not imply ownership or access permission unless source explicitly supports that claim. |
| Protected-area / conservation-area context | Conservation context. | Authority and release posture vary by source. |
| HabitatPatch | Habitat unit inside/near zone. | Zone does not redefine patch truth. |
| RestorationOpportunity | Candidate site inside/near zone. | Zone does not approve action. |
| HabitatQualityScore | Quality summary inside zone. | Score is descriptive, not prescriptive. |
| SuitabilityModel | Potential/fit context. | Model card, receipt, uncertainty, and modeled label required. |
| ConnectivityEdge / Corridor | Connectivity context. | Derived assumptions travel with the relation. |
| Fauna/Flora joins | Species/vegetation context. | Sensitive occurrences and rare plants fail closed unless generalized/reviewed. |
| Soil/Hydrology/Hazards/Agriculture/Land context | Context factors. | Ownership and source-role boundaries preserved. |

---

## Sensitivity and release

Stewardship zones can expose sensitive ecological, private, operational, cultural, or access information even when the source boundary appears public.

Rules:

- Exact sensitive stewardship geometry fails closed.
- Public products use generalized, redacted, aggregated, delayed, or steward-reviewed derivatives.
- A public zone must not imply access permission, legal ownership, restoration approval, priority mandate, or regulatory status.
- Public-safe derivatives need EvidenceBundle support, validation, policy allow, review state where required, ReleaseManifest, correction path, and rollback target.
- Any join to sensitive occurrence, rare plant, private access, cultural/archaeological, infrastructure, or stewardship-only source context requires policy review.
- AI/Focus Mode must `ABSTAIN` or `DENY` when source support, role, sensitivity, evidence, review, or release state is unresolved.

---

## Lifecycle

| Phase | StewardshipZone handling |
|---|---|
| RAW | Zone inputs are captured as source payloads/refs with source role, rights, sensitivity, citation, time, and hash. |
| WORK / QUARANTINE | Zone normalization runs in work; unresolved rights, access ambiguity, sensitivity, missing authority limits, or source-role ambiguity are quarantined. |
| PROCESSED | Validated zones bind geometry/scope, source role, evidence refs, authority-limit notes, policy refs, and review state. |
| CATALOG / TRIPLET | Catalog/triplet projections may point to zones; they do not replace canonical objects or evidence. |
| RELEASE CANDIDATE | Public-safe zone summaries/layers are assembled with ReleaseManifest, correction path, rollback target, and review/policy/evidence closure. |
| PUBLISHED | Only released public-safe artifacts are served through governed APIs and public UI surfaces; exact restricted zones remain withheld or staged. |
| CORRECTED / SUPERSEDED | Source update, geometry change, rights change, sensitivity change, reviewer decision, policy change, or release withdrawal triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/habitat/stewardship_zone.schema.json` beyond an empty scaffold.
- [ ] Confirm canonical `zone_role` and `geometry_exposure_class` enum values.
- [ ] Confirm policy location and behavior for `policy/domains/habitat/stewardship_zone.rego` or equivalent.
- [ ] Confirm how land/title/access authority is referenced without being adopted by Habitat.
- [ ] Add valid fixtures for conservation-area context, stewardship-program boundary, public-safe generalized zone, restricted exact zone, restoration-context zone, and corrected/superseded zone.
- [ ] Add invalid fixtures for missing source, missing authority-limit note, access-as-permission, zone-as-title, zone-as-regulatory-designation, zone-as-management-order, sensitive exact public geometry, source-role collapse, and release without rollback.
- [ ] Add validator checks for spatial scope, temporal scope, source roles, rights/authority limits, exposure class, evidence refs, policy decisions, review records, release refs, correction refs, and rollback refs.
- [ ] Confirm public UI labels stewardship context clearly and prevents ownership/access/directive wording.
- [ ] Confirm Focus Mode abstains when evidence, sensitivity, policy, review, or release support is missing.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Zone, evidence, source role, authority limits, sensitivity, policy, review, release, correction, and rollback resolve | `ANSWER` / public-safe zone may support a claim |
| Evidence, authority limits, rights, sensitivity, review, release, or rollback support is incomplete | `ABSTAIN` / `HOLD` |
| Zone-as-permission, zone-as-title, zone-as-directive, sensitive exact public exposure, source-role collapse, or release bypass would occur | `DENY` |
| Schema, validator, source read, digest, evidence lookup, policy lookup, review lookup, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Target scaffold | Confirms `stewardship_zone.md` existed as scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms `stewardship_zone.schema.json` path and that it points to this contract. | Does not prove field-level validation. |
| Habitat README | Confirms `StewardshipZone` as a canonical Habitat object family and confirms lifecycle/sensitivity/publication posture. | Field realization remains PROPOSED. |
| Habitat canonical paths | Confirms proposed contract/schema/policy/test path mapping and schema-home conflict. | Path realization and enforcement remain partly PROPOSED. |
| Habitat sublane index | Confirms stewardship zone is treated as a Habitat sublane/object family candidate. | Sublane paths remain PROPOSED / NEEDS VERIFICATION. |
| Ecology cross-domain doctrine | Confirms atomic ownership and cross-domain composition boundaries. | It is an architecture doctrine and does not prove Habitat implementation. |
| User-provided authoring role | Requires evidence-grounded repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a stewardship-zone object or zone-dependent output weakens source-role integrity, evidence support, authority-limit transparency, sensitivity posture, ownership/access boundaries, review separation, release governance, or public wording boundaries.

Rollback triggers include source update; zone geometry correction; rights/authority-limit correction; access or ownership misinterpretation; stewardship-only context exposed publicly; sensitive exact geometry exposure; rare-species/rare-plant inference exposure; cultural/archaeological or infrastructure risk exposure; zone presented as title, permission, directive, approval, funding eligibility, or regulatory designation; public API/UI/AI exposure without release/correction/rollback refs; watcher-as-publisher; tile/popup/vector-index/AI-as-truth; or missing evidence/policy/review closure.

Rollback artifacts should include affected zone IDs, supporting object refs, source refs, source-role refs, authority-limit notes, geometry/exposure refs, sensitivity refs, evidence refs, validation reports, policy decisions, review records, release refs, correction notices, rollback cards, replacement zones, suppression instructions, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which `zone_role` values are canonical for StewardshipZone? | NEEDS VERIFICATION | Contract/schema/policy review. |
| Which source families may create stewardship zones first? | NEEDS VERIFICATION | Habitat steward + Source steward activation review. |
| How should land/title/access authority be linked without being adopted by Habitat? | NEEDS VERIFICATION | Cross-domain/land-title/source-role review. |
| Which public geometry exposure classes are allowed for stewardship zones? | NEEDS VERIFICATION | Sensitivity/release policy review. |
| Is `policy/domains/habitat/stewardship_zone.rego` the accepted policy path? | NEEDS VERIFICATION | Policy root inspection and ADR/path review. |
| Can any stewardship zone ever be public at exact geometry? | NEEDS VERIFICATION | Sensitivity, rights, stewardship, and release review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contract root.
- [`./habitat_patch.md`](./habitat_patch.md) — habitat patch contract.
- [`./restoration_opportunity.md`](./restoration_opportunity.md) — restoration opportunity contract.
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
- [`../../../docs/architecture/ecology-cross-domain.md`](../../../docs/architecture/ecology-cross-domain.md) — cross-domain composition and atomic ownership doctrine.
- [`../../../schemas/contracts/v1/domains/habitat/stewardship_zone.schema.json`](../../../schemas/contracts/v1/domains/habitat/stewardship_zone.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
