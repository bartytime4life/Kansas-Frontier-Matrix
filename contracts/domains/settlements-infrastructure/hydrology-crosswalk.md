<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-settlements-infrastructure-hydrology-crosswalk
title: Hydrology Crosswalk Contract — Settlements / Infrastructure
type: semantic-contract; cross-domain-crosswalk
version: v0.2
status: draft; PROPOSED; schema-missing; canonical-working-lane; slug-CONFLICTED-with-singular-settlement; contextual-only; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Settlements/Infrastructure domain steward
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Map/UI steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — scaffold existed before v0.2 expansion
updated: 2026-06-23
policy_label: public; contracts; settlements-infrastructure; hydrology-crosswalk; cross-domain; contextual-relation; watershed-context; flood-context; water-use-context; evidence-bound; source-role-aware; temporal-scope-aware; policy-aware; sensitivity-aware; release-gated; rollback-aware; not-hydrology-truth; not-settlement-truth; not-flood-warning; not-observed-inundation; not-regulatory-determination; not-publication-authority
tags: [kfm, contracts, settlements-infrastructure, hydrology-crosswalk, hydrology, crosswalk, contextual-relation, Watershed, HUCUnit, HydroFeature, ReachIdentity, GaugeSite, GroundwaterWell, FlowObservation, WaterLevelObservation, WaterQualityObservation, AquiferObservation, Hydrograph, NFHLZone, UpstreamTrace, WaterUseLink, DroughtLink, IrrigationLink, Settlement, Municipality, CensusPlace, Townsite, GhostTown, Fort, Mission, ReservationCommunity, InfrastructureAsset, Facility, ServiceArea, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard]
related:
  - ./README.md
  - ./domain_feature_identity.md
  - ./domain_observation.md
  - ./domain_layer_descriptor.md
  - ./domain_validation_report.md
  - ./evidence-drawer-payload.md
  - ./hazards-crosswalk.md
  - ../settlement/README.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../docs/domains/settlements-infrastructure/MAP_UI_CONTRACTS.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/settlements.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/PUBLICATION_POSTURE.md
  - ../../../contracts/domains/hydrology/domain_layer_descriptor.md
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/hydrology-crosswalk.schema.json
  - ../../../schemas/contracts/v1/domains/hydrology/
  - ../../../policy/domains/settlements-infrastructure/
  - ../../../policy/domains/hydrology/
  - ../../../fixtures/domains/settlements-infrastructure/hydrology-crosswalk/
  - ../../../tests/domains/settlements-infrastructure/
  - ../../../release/candidates/settlements-infrastructure/
  - ../../../release/candidates/hydrology/
notes:
  - "Expanded from a PROPOSED scaffold at contracts/domains/settlements-infrastructure/hydrology-crosswalk.md."
  - "A paired schema at schemas/contracts/v1/domains/settlements-infrastructure/hydrology-crosswalk.schema.json was not found in this task. Field realization remains PROPOSED."
  - "Hydrology doctrine owns watersheds, HUCs, hydro features, reaches, gauges, wells, observations, hydrographs, NFHL regulatory context, upstream traces, and water-use/drought/irrigation links; Settlements/Infrastructure owns settlement and infrastructure identity."
  - "Hydrology doctrine separates regulatory flood context from observed inundation and keeps emergency/life-safety warning behavior outside KFM public authority. This crosswalk preserves that boundary."
  - "This contract defines cross-domain relation meaning. It does not author hydrology truth, settlement truth, infrastructure truth, observed flooding, regulatory determination, public access, map truth, graph truth, policy decision, or publication approval."
  - "The singular contracts/domains/settlement path remains a compatibility / variance surface, not a canonical replacement, unless an ADR resolves otherwise."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Crosswalk Contract — Settlements / Infrastructure

> Semantic contract for `hydrology-crosswalk`: the governed cross-domain relation that lets Settlements/Infrastructure features cite Hydrology records as contextual evidence while preserving domain ownership, source role, temporal scope, policy posture, release state, correction lineage, and rollback targets.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: settlements-infrastructure" src="https://img.shields.io/badge/domain-settlements--infrastructure-blue">
  <img alt="Crosswalk: hydrology" src="https://img.shields.io/badge/crosswalk-hydrology-1f9eda">
  <img alt="Schema: missing" src="https://img.shields.io/badge/schema-missing-red">
  <img alt="Truth: relation not hydro truth" src="https://img.shields.io/badge/truth-relation__not__hydro__truth-blue">
  <img alt="NFHL: regulatory context" src="https://img.shields.io/badge/NFHL-regulatory__context-orange">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release--gated-orange">
</p>

`contracts/domains/settlements-infrastructure/hydrology-crosswalk.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Crosswalk model](#crosswalk-model) · [Relation families](#relation-families) · [Source-role and time rules](#source-role-and-time-rules) · [Publication posture](#publication-posture) · [Invariants](#invariants) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Rollback](#rollback) · [Evidence basis](#evidence-basis) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract / cross-domain crosswalk  
> **Owner:** `OWNER_TBD`  
> **Contract path:** `contracts/domains/settlements-infrastructure/hydrology-crosswalk.md`  
> **Schema path checked:** `schemas/contracts/v1/domains/settlements-infrastructure/hydrology-crosswalk.schema.json` — **not found in this task**  
> **Truth posture:** target path, prior scaffold, Settlements/Infrastructure contract-lane README, Settlements/Infrastructure domain doctrine, Hydrology domain doctrine, Hydrology publication posture, and Hydrology layer-descriptor pattern are confirmed from current repo evidence. Field-level shape, validator behavior, fixture coverage, policy behavior, source registry records, release manifests, governed API routes, public API behavior, map rendering, graph behavior, and runtime behavior remain **NEEDS VERIFICATION**.

> [!CAUTION]
> This contract defines relation meaning only. It does **not** create hydrologic feature truth, observed flooding truth, regulatory determination, settlement truth, infrastructure truth, public map approval, or AI answer authority.

---

## Meaning

`hydrology-crosswalk` records a bounded relation between a Settlements/Infrastructure subject and a Hydrology-domain object.

It may relate a settlement, municipality, census place, historic place, reservation community, asset, facility, service area, operator, condition observation, or dependency to Hydrology context such as:

- `Watershed`
- `HUCUnit`
- `HydroFeature`
- `ReachIdentity`
- `GaugeSite`
- `GroundwaterWell`
- `FlowObservation`
- `WaterLevelObservation`
- `WaterQualityObservation`
- `AquiferObservation`
- `Hydrograph`
- `NFHLZone`
- `UpstreamTrace`
- `WaterUseLink`
- `DroughtLink`
- `IrrigationLink`

The crosswalk answers:

- which Settlements/Infrastructure subject is related to which Hydrology record;
- what kind of contextual relation is being asserted;
- which source role, time role, evidence, policy, review, release, and rollback states control the relation;
- whether the hydrology relation is observed, regulatory, modeled, aggregate, administrative, contextual, candidate, or release-gated;
- what public wording or display must **not** imply.

This contract owns the **cross-domain relation meaning** only. Hydrology owns hydrologic features, observations, regulatory context, source-role discipline, and hydrology publication posture. Settlements/Infrastructure owns settlement and infrastructure identity. EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, correction, and rollback remain separate governance surfaces.

---

## Repo fit

| Responsibility | Path or root | Relationship |
|---|---|---|
| Parent contract lane | `./README.md` | Defines this folder as semantic contracts only. |
| Identity companion | `./domain_feature_identity.md` | Crosswalk subject identity must remain source-role/family/time/evidence aware. |
| Observation companion | `./domain_observation.md` | Observations may support a crosswalk but do not become hydrology truth. |
| Layer descriptor companion | `./domain_layer_descriptor.md` | Crosswalk may be used by a layer descriptor, but layer release remains separate. |
| Validation companion | `./domain_validation_report.md` | Validation can check crosswalk support; it is not approval. |
| Evidence Drawer profile | `./evidence-drawer-payload.md` | Drawer may show the relation after evidence and policy filtering. |
| Hazards crosswalk companion | `./hazards-crosswalk.md` | Adjacent cross-domain relation contract with similar ownership boundaries. |
| Hydrology domain doctrine | `../../../docs/domains/hydrology/README.md` | Defines Hydrology object families, source-role discipline, lane placement, lifecycle, and publication posture. |
| Hydrology publication posture | `../../../docs/domains/hydrology/PUBLICATION_POSTURE.md` | Defines release gates, deny-by-default posture, flood-role separation, and required release artifacts. |
| Hydrology layer descriptor | `../../../contracts/domains/hydrology/domain_layer_descriptor.md` | Sibling contract pattern for Hydrology layer delivery. |
| Paired schema | `../../../schemas/contracts/v1/domains/settlements-infrastructure/hydrology-crosswalk.schema.json` | Not found in this task; do not infer field enforcement. |
| Hydrology schemas | `../../../schemas/contracts/v1/domains/hydrology/` | Expected machine shapes for Hydrology objects; maturity varies and must be verified. |
| Policy | `../../../policy/domains/settlements-infrastructure/`, `../../../policy/domains/hydrology/` | Allow/deny/restrict/abstain and release controls. |
| Release/rollback | `../../../release/candidates/settlements-infrastructure/`, `../../../release/candidates/hydrology/`, release roots | Release, correction, rollback, and derivative invalidation. |

---

## Schema posture

A direct paired schema was checked at:

```text
schemas/contracts/v1/domains/settlements-infrastructure/hydrology-crosswalk.schema.json
```

That file was **not found** in this task.

> [!WARNING]
> Because no paired schema was confirmed, every field below is **PROPOSED** semantic guidance. Do not treat it as machine-enforced until schema, fixtures, validators, policy tests, release checks, governed API behavior, and runtime behavior are verified.

---

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Linking a Settlements/Infrastructure feature to Hydrology context | Yes | Must cite both subject refs and hydrology refs with evidence, source role, and time scope. |
| Supporting watershed, HUC, reach, or upstream context | Conditional | Must preserve that Hydrology owns water-system semantics and Settlements/Infrastructure owns subject identity. |
| Supporting gauge, well, or observation context | Conditional | Must preserve observed/source/retrieval time and observation caveats. |
| Supporting NFHL or flood-regulatory context | Conditional | Must preserve regulatory-context wording and avoid observed-event wording unless separately supported. |
| Supporting water-use, drought, or irrigation context | Conditional | Must preserve source role and cross-domain ownership boundaries. |
| Supporting public map or Evidence Drawer context | Conditional | Requires governed release, policy, review, public geometry rule, and rollback target. |
| Supporting Focus Mode explanation | Conditional | AI must cite evidence and preserve finite outcomes. |
| Certifying current conditions, emergency action, regulatory determination, property/access status, or infrastructure condition | No | Return `ABSTAIN`, `DENY`, or `ERROR` depending on evidence and policy posture. |
| Replacing either domain's objects | No | Use each domain's contracts, schemas, and EvidenceBundles. |

---

## Exclusions

`hydrology-crosswalk` must not be used as:

| Misuse | Required outcome |
|---|---|
| Hydrologic feature truth | Use Hydrology-domain objects and EvidenceBundles. |
| Observed flooding truth | Use Hydrology/Hazards-owned evidence and publication posture; do not infer from relation alone. |
| NFHL-as-observed-event claim | `DENY`; NFHL is regulatory context, not observed inundation. |
| Settlement or infrastructure feature truth | Use Settlements/Infrastructure object-family contracts and EvidenceBundles. |
| Regulatory determination | Use official-source evidence and policy-reviewed wording. |
| Public access or safe-route guidance | `DENY` or `ABSTAIN`; outside this contract. |
| Feature condition or dependency disclosure | Require policy/review and public-safe filtering. |
| Publication approval | Use PolicyDecision, ReviewRecord, ReleaseManifest, correction path, and RollbackCard. |
| AI answer authority | Focus Mode remains evidence-subordinate and finite-outcome constrained. |

---

## Recommended fields

The following fields are **PROPOSED** until a paired schema is added and validated.

| Field | Meaning |
|---|---|
| `id` | Canonical hydrology-crosswalk relation identifier. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic hash over normalized relation content. |
| `domain` | Expected value: `settlements-infrastructure`. |
| `crosswalk_type` | Watershed, HUC, reach, upstream, gauge, well, observation, regulatory-flood-context, water-use, drought, irrigation, review-only, denied, or source-specific type. |
| `settlement_infrastructure_subject_ref` | DomainFeatureIdentity or object-family ref for the Settlements/Infrastructure subject. |
| `settlement_infrastructure_family` | Settlement, Municipality, CensusPlace, GhostTown, Facility, ServiceArea, InfrastructureAsset, Dependency, etc. |
| `hydrology_subject_ref` | Hydrology-domain object ref. |
| `hydrology_family` | Watershed, HUCUnit, HydroFeature, GaugeSite, FlowObservation, NFHLZone, UpstreamTrace, etc. |
| `relation_statement` | Human-readable scoped relation statement. |
| `relation_method` | Spatial join, watershed containment, upstream trace, service-area relation, source cross-reference, model output, aggregate rollup, manual review, or source-specific method. |
| `source_refs` | SourceDescriptor refs from both sides where needed. |
| `evidence_refs` | EvidenceRefs or EvidenceBundle refs. |
| `source_role_summary` | Source-role posture across domains. |
| `temporal_scope` | Source time, observed time, valid time, measurement time, publication time, retrieval time, release time, correction time. |
| `public_geometry_rule` | Exact, generalized, aggregate, hidden, denied, or review-only posture. |
| `hydrology_role_boundary` | Required statement distinguishing observed, regulatory, modeled, aggregate, and contextual hydrology support. |
| `freshness_or_vintage_state` | Fresh, stale, historical, version-pinned, unknown, or not applicable. |
| `sensitivity_label` | Sensitivity/policy tier inherited from both domains. |
| `policy_decision_ref` | PolicyDecision governing use/publication. |
| `review_ref` | ReviewRecord or steward review ref. |
| `release_manifest_ref` | ReleaseManifest or MapReleaseManifest ref. |
| `rollback_ref` | RollbackCard or rollback target. |
| `limitations` | Caveats: crosswalk only; not hydrology truth, not release approval. |

---

## Crosswalk model

A reviewed crosswalk should bind one Settlements/Infrastructure subject to one or more Hydrology refs while preserving ownership boundaries.

```text
hydrology_crosswalk = {
  domain,
  crosswalk_type,
  settlement_infrastructure_subject_ref,
  hydrology_subject_ref,
  relation_method,
  source_role_summary,
  evidence_refs,
  temporal_scope,
  hydrology_role_boundary,
  policy_decision_ref,
  review_ref,
  release_manifest_ref,
  rollback_ref
}
```

The exact serialized shape is **NEEDS VERIFICATION** until the schema and validators are field-complete.

---

## Relation families

| Relation family | Meaning | Guardrail |
|---|---|---|
| `watershed_context` | Subject is located in or related to a watershed/HUC context. | Watershed context is hydrologic context, not settlement truth. |
| `reach_context` | Subject relates to a hydro feature, reach, or stream/river identity. | Hydrology owns hydro feature identity. |
| `upstream_context` | Subject participates in or is referenced by an upstream trace. | Upstream trace is analysis context and must cite evidence/model posture. |
| `gauge_or_well_context` | Subject relates to a gauge site, well, or observation location. | Observations require time/source/vintage discipline. |
| `flow_or_level_observation_context` | Subject relates to flow, water-level, quality, or aquifer observations. | Observation context is not general truth beyond supported scope. |
| `nfhl_context` | Subject relates to NFHL/regulatory flood context. | Regulatory context must not be rendered as observed flooding. |
| `water_use_context` | Subject relates to water-use, drought, or irrigation links. | Preserve cross-domain ownership and source-role boundaries. |
| `review_only_context` | Relation is held for steward/policy review. | Not public until release gates pass. |
| `denied_context` | Relation cannot be exposed under current policy/evidence. | Show safe denial reason only, if surfaced at all. |

---

## Source-role and time rules

| Rule | Requirement |
|---|---|
| Domain ownership stays explicit | Hydrology owns hydrologic records; Settlements/Infrastructure owns subject identity. |
| Source role never collapses | Observed, regulatory, modeled, aggregate, administrative, candidate, contextual, and synthetic support remain distinct. |
| Regulatory context is not observation | NFHL-style context must remain regulatory/version-pinned unless separately supported as another object. |
| Time axes remain separate | Measurement time, source time, valid time, publication time, retrieval time, release time, and correction time must not collapse. |
| Candidate joins stay candidate | Spatial overlap, OCR, model, map label, or connector suggestion does not create public truth. |
| Public claims require EvidenceBundle resolution | If evidence cannot resolve, return ABSTAIN, DENY, or ERROR; do not invent the relation. |

---

## Publication posture

| Surface | Default posture | Reason |
|---|---|---|
| Watershed/HUC relation to public settlement feature | Public-safe if released | Still needs source role, time scope, EvidenceBundle, and release state. |
| Gauge or observation relation | Public-safe only with observation/vintage context | Observation scope and time must remain visible. |
| NFHL/regulatory relation | Version-pinned and caveated | Regulatory context is not observed event or forecast truth. |
| Hydrology relation to sensitive subject detail | Restrict, generalize, or deny by default | Crosswalk can expose protected context. |
| Water-use/drought/irrigation relation | Review as needed | Cross-domain relation may involve rights, source-role, or sensitivity constraints. |
| Candidate/model relation | Review only | Automated relation does not close evidence. |

---

## Invariants

1. **Crosswalk is not ownership transfer.** Each domain keeps its own truth authority.
2. **Hydrology role is preserved.** Observed, regulatory, modeled, aggregate, and contextual hydrology support must not collapse.
3. **NFHL/regulatory context is not observed flooding.** The relation must preserve the regulatory-context boundary.
4. **Evidence outranks relation.** A crosswalk cannot strengthen weak or unresolved evidence.
5. **Time is part of meaning.** Measurement/source/valid/publication/release/correction times must stay distinct where material.
6. **Public geometry is policy-filtered.** Sensitive relations may require aggregation, generalization, review-only status, or denial.
7. **Release is separate.** A valid relation does not publish anything without PolicyDecision, ReviewRecord, ReleaseManifest, and RollbackCard where required.
8. **AI is downstream.** Focus Mode may explain only released evidence and policy-permitted context.
9. **No direct internal-store reads.** Public clients use governed APIs and released artifacts only.
10. **Singular `settlement` remains conflicted.** Do not route canonical crosswalks through the singular compatibility path without ADR.

---

## Lifecycle

```mermaid
flowchart LR
  SI["Settlements / Infrastructure subject\nidentity + evidence"] --> JOIN["HydrologyCrosswalk\nrelation meaning"]
  HYD["Hydrology subject\nwater context + evidence"] --> JOIN
  JOIN --> VALID["DomainValidationReport\nsource role + time + policy preflight"]
  VALID --> CAT["CATALOG / TRIPLET\nEvidenceBundle refs"]
  CAT --> REVIEW["PolicyDecision + ReviewRecord"]
  REVIEW --> REL["ReleaseManifest + RollbackCard"]
  REL --> PUB["governed API / map / Evidence Drawer / Focus Mode"]
  PUB --> OUT["ANSWER / ABSTAIN / DENY / ERROR\nhydrology role boundary visible"]
```

Contracts describe meaning. They do not move data, validate schema shape, execute joins, decide policy, publish artifacts, render maps, or authorize AI answers.

---

## Validation

Before this contract is treated as mature, maintainers should verify:

- [ ] whether this crosswalk needs a paired schema or should be represented through existing relation/triplet schemas;
- [ ] schema includes subject refs for both domains, relation family, source-role summary, time axes, hydrology role boundary, policy/review/release/rollback refs, and public geometry rule;
- [ ] fixtures cover watershed, HUC, reach, upstream, gauge/well, observation, NFHL/regulatory, water-use, drought, irrigation, review-only, denied, and stale/version-pinned contexts;
- [ ] tests prevent crosswalks from becoming hydrology truth, settlement/infrastructure truth, observed flooding truth, regulatory determination, public-access guidance, or publication approval;
- [ ] tests enforce ABSTAIN/DENY/ERROR when evidence, source role, sensitivity, freshness/vintage, or release state is unresolved;
- [ ] rollback invalidates layer descriptors, drawer payloads, Focus Mode citations, exports, caches, graph projections, and AI summaries that cited a withdrawn crosswalk.

---

## Rollback

Rollback is required if this contract:

- claims schema, validator, fixture, test, policy, release, API, map, graph, or runtime behavior exists without proof;
- treats hydrology crosswalks as hydrologic feature truth, observed flooding truth, regulatory determination, settlement/infrastructure truth, public access guidance, release approval, or AI authority;
- hides measurement/vintage/version/correction state or regulatory-context posture;
- exposes sensitive relations through examples, public wording, map layers, or drawer text;
- normalizes direct UI access to internal lifecycle stores or direct model output;
- treats the singular `settlement` path as canonical authority without ADR support.

Rollback target: revert `contracts/domains/settlements-infrastructure/hydrology-crosswalk.md` to prior scaffold blob `b6e2e9071f546a93c606d2618583385e6a918d71`, record drift if authority boundaries were affected, and invalidate downstream derivatives that relied on weakened hydrology-crosswalk semantics.

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior `contracts/domains/settlements-infrastructure/hydrology-crosswalk.md` | `CONFIRMED` | Target file existed as a PROPOSED scaffold sourced from the expansion backlog. | Scaffold did not define authoritative semantic contract content. |
| Paired schema lookup | `CONFIRMED not found in this task` | Justifies schema-missing posture. | Does not rule out alternate schema names or future ADR-selected homes. |
| `contracts/domains/settlements-infrastructure/README.md` | `CONFIRMED contract-lane rule` | Defines this folder as semantic meaning only and points schemas, policy, tests, data, release, and public artifacts to separate roots. | Does not define hydrology-crosswalk fields. |
| `docs/domains/settlements-infrastructure/README.md` | `CONFIRMED doctrine / PROPOSED implementation` | Confirms Settlements/Infrastructure object families, lifecycle, and source/temporal identity posture. | Does not prove crosswalk schema/validator/test implementation. |
| `docs/domains/hydrology/README.md` | `CONFIRMED hydrology doctrine / PROPOSED implementation` | Defines Hydrology ownership of watersheds, HUCs, hydro features, observations, regulatory context, upstream traces, and cross-domain water links. | Does not prove crosswalk implementation. |
| `docs/domains/hydrology/PUBLICATION_POSTURE.md` | `CONFIRMED hydrology publication doctrine / PROPOSED implementation` | Defines release gates, flood-role separation, public-safe geometry posture, required artifacts, and rollback posture. | Does not prove enforcement exists. |
| `contracts/domains/hydrology/domain_layer_descriptor.md` | `CONFIRMED sibling pattern` | Provides Hydrology delivery-support contract pattern with source-role, NFHL/regulatory-context, release, and rollback boundaries. | Hydrology-specific; adapted only where relevant. |
| Uploaded KFM authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-first, implementation-honest, visually polished Markdown with visible verification and rollback posture. | Authoring guidance, not implementation proof. |

---

## Open questions

| ID | Question | Status |
|---|---|---|
| OQ-SI-HYD-XW-01 | Should `hydrology-crosswalk.md` be a standalone contract, a relation schema, or a section of a broader cross-domain relation contract? | OPEN / DOMAIN + SCHEMA REVIEW |
| OQ-SI-HYD-XW-02 | Which Hydrology object families may be linked to which Settlements/Infrastructure object families? | OPEN / CROSS-DOMAIN REVIEW |
| OQ-SI-HYD-XW-03 | Which fields are required to preserve NFHL/regulatory context, observation time, gauge vintage, and hydrology role boundaries? | OPEN / HYDROLOGY REVIEW |
| OQ-SI-HYD-XW-04 | Which relation families must default to aggregation, generalization, review-only status, or denial? | OPEN / POLICY REVIEW |
| OQ-SI-HYD-XW-05 | How should Evidence Drawer and Focus Mode present hydrology crosswalks without implying unsupported current conditions or regulatory determinations? | OPEN / MAP/UI REVIEW |
| OQ-SI-HYD-XW-06 | How should rollback invalidate map labels, drawer payloads, Focus Mode claims, exports, caches, and AI summaries after a crosswalk correction? | OPEN / RELEASE REVIEW |

<p align="right"><a href="#top">Back to top</a></p>
