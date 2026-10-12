<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-soil-domain-feature-identity
title: Domain Feature Identity Contract — Soil
type: semantic-contract
version: v0.3.0
status: draft; PROPOSED_INACTIVE candidate profile implemented; support-type-separation-required; non-canonical; non-publisher
owners:
  - OWNER_TBD — Soil domain steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-23
updated: 2026-08-24
policy_label: public; contracts; soil; domain-feature-identity; deterministic-candidate; source-role-aware; support-type-separation; temporal-scope-aware; evidence-bound; fixture-first; release-gated; rollback-aware; not-source-truth; not-canonical-authority; not-etl-code; not-publication-authority
owning_root: contracts/
responsibility: Semantic meaning and authority limits for the Soil DomainFeatureIdentity candidate profile
truth_posture: CONFIRMED closed PROPOSED_INACTIVE schema, deterministic validator, synthetic fixture matrix, and focused tests; NEEDS VERIFICATION canonical adoption, broader coverage, runtime integration, release, and publication
tags: [kfm, contracts, soil, domain-feature-identity, SoilMapUnit, SoilComponent, Horizon, ComponentHorizonJoin, SoilProperty, HydrologicSoilGroup, SoilMoistureObservation, Pedon, SoilProfileView, ErosionRisk, SuitabilityRating, SoilTimeCaveat, SSURGO, SDA, gSSURGO, gNATSGO, Mesonet, SCAN, USCRN, SMAP, SourceDescriptor, EvidenceRef, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard]
related:
  - ./README.md
  - ./component_horizon_join.md
  - ./soil_map_unit.md
  - ./soil_component.md
  - ./horizon.md
  - ./soil_property.md
  - ./hydrologic_soil_group.md
  - ./soil_moisture_observation.md
  - ./pedon.md
  - ./soil_profile_view.md
  - ./erosion_risk.md
  - ./suitability_rating.md
  - ./soil_time_caveat.md
  - ../../../docs/domains/soil/README.md
  - ../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../docs/domains/soil/ARCHITECTURE.md
  - ../../../docs/domains/soil/API_CONTRACTS.md
  - ../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../pipelines/domains/soil/README.md
  - ../../../schemas/contracts/v1/domains/soil/domain_feature_identity.schema.json
  - ../../../schemas/contracts/v1/domains/soil/README.md
  - ../../../tools/validators/domains/soil/validate_domain_feature_identity.py
  - ../../../policy/domains/soil/README.md
  - ../../../fixtures/domains/soil/domain_feature_identity/
  - ../../../tests/validators/domains/soil/test_domain_feature_identity.py
  - ../../../release/candidates/soil/
notes:
  - "Expanded from a greenfield scaffold at contracts/domains/soil/domain_feature_identity.md."
  - "The `created` date records the v0.2 semantic-contract expansion; the earlier scaffold's creation date remains unestablished."
  - "Repository status reconciled at main@362d6590b9516596ad1c34a64781c13bf85d52c8."
  - "The paired schema is now a closed PROPOSED_INACTIVE fixture-first candidate with a deterministic validator, five synthetic cases, and five focused tests."
  - "Soil architecture proposes the identity rule `source id + object role + temporal scope + normalized digest` across Soil object families. This contract gives that rule semantic meaning for the Soil lane."
  - "Support-type separation remains mandatory: static survey, gridded derivative, station observation, satellite grid, pedon/profile evidence, and interpretation cannot be collapsed by identity logic."
  - "The implemented profile validates only bounded synthetic candidates; it does not create canonical identity, execute ETL joins, activate a source, resolve evidence, approve public API behavior, release, publish, or render a map."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Feature Identity Contract — Soil

> Semantic contract for `domain_feature_identity`: the broad Soil-domain identity envelope used to identify Soil objects across source family, object role, support type, time scope, evidence, policy, release state, and rollback lineage — without becoming JSON Schema, ETL code, source truth, public layer truth, API authority, or AI answer authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: soil" src="https://img.shields.io/badge/domain-soil-8B4513">
  <img alt="Object: domain feature identity" src="https://img.shields.io/badge/object-domain__feature__identity-purple">
  <img alt="Schema: bounded inactive candidate" src="https://img.shields.io/badge/schema-bounded__inactive__candidate-orange">
  <img alt="Support type: separate" src="https://img.shields.io/badge/support--type-separate-critical">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release--gated-orange">
</p>

`contracts/domains/soil/domain_feature_identity.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Identity model](#identity-model) · [Object-family coverage](#object-family-coverage) · [Source-role and support rules](#source-role-and-support-rules) · [Sensitivity and publication posture](#sensitivity-and-publication-posture) · [Invariants](#invariants) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Rollback](#rollback) · [Evidence basis](#evidence-basis) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Owner:** `OWNER_TBD`  
> **Contract path:** `contracts/domains/soil/domain_feature_identity.md`  
> **Schema path checked:** `schemas/contracts/v1/domains/soil/domain_feature_identity.schema.json` — **closed `PROPOSED_INACTIVE` fixture-first candidate**
> **Executable path checked:** `tools/validators/domains/soil/validate_domain_feature_identity.py` with five synthetic cases and five focused tests
> **Truth posture:** the bounded candidate shape, deterministic hash/ID rule, support-role matrix, finite outcomes, and denial of public/effect overclaims are confirmed from current repository evidence. Canonical adoption, complete object/support-family coverage, source admission, policy integration, runtime API/UI behavior, release, publication, correction propagation, and rollback invalidation remain **NEEDS VERIFICATION**.

> [!CAUTION]
> This contract defines identity meaning only. It does **not** validate JSON, execute source ingestion, decide source activation, publish a layer, prove a soil property, or authorize an AI answer.

---

## Meaning

`domain_feature_identity` is the Soil lane's broad identity envelope for matching, naming, deduplicating, citing, comparing, and explaining Soil objects without collapsing object families, source roles, support types, or time axes.

It applies to identity support for:

- `SoilMapUnit`
- `SoilComponent`
- `Horizon`
- `ComponentHorizonJoin`
- `SoilProperty`
- `HydrologicSoilGroup`
- `SoilMoistureObservation`
- `Pedon`
- `SoilProfileView`
- `ErosionRisk`
- `SuitabilityRating`
- `SoilTimeCaveat`

The architecture-level identity rule is:

```text
source id + object role + temporal scope + normalized digest
```

This contract makes that rule inspectable. It states what must be preserved when KFM claims that two Soil records refer to the same object, when a record is a candidate match, or when an object is safe to render as a public feature.

---

## Repo fit

| Responsibility | Path | Role |
|---|---|---|
| Contract lane | `contracts/domains/soil/domain_feature_identity.md` | This semantic identity contract. |
| Soil contract README | `contracts/domains/soil/README.md` | Defines `contracts/domains/soil/` as meaning-only and lists Soil object-family contract candidates. |
| Paired candidate schema | `schemas/contracts/v1/domains/soil/domain_feature_identity.schema.json` | Closed `PROPOSED_INACTIVE` candidate shape; fixes public use and all authority effects to `false`. |
| Candidate validator | `tools/validators/domains/soil/validate_domain_feature_identity.py` | Deterministic hash/ID, source identity, temporal scope, canonical arrays, and support-role checks with `PASS`, `DENY`, and `ERROR`. |
| Soil architecture | `docs/domains/soil/ARCHITECTURE.md` | Defines object families, identity rule, source families, support-type separation, lifecycle, and cross-lane boundaries. |
| Soil API posture | `docs/domains/soil/API_CONTRACTS.md` | Defines governed API posture, finite outcomes, public trust membrane, and support-type separation. |
| Soil lifecycle inventory | `docs/domains/soil/DATA_LIFECYCLE.md` | Lists owned Soil object families, source families, lifecycle posture, and sensitivity defaults. |
| Soil pipeline lane | `pipelines/domains/soil/README.md` | Describes executable pipeline scope and clarifies pipelines own the how, not object meaning or release approval. |
| Policy | `policy/domains/soil/` | Allow/deny/restrict/abstain, rights, sensitivity, and release gating. |
| Tests / fixtures | `tests/validators/domains/soil/test_domain_feature_identity.py`, `fixtures/domains/soil/domain_feature_identity/cases.json` | Five focused tests and five synthetic cases prove the bounded candidate matrix. |
| Release / rollback | `release/candidates/soil/` and release roots | Publication, correction, and rollback authority. |

---

## Schema posture

A paired schema exists at:

```text
schemas/contracts/v1/domains/soil/domain_feature_identity.schema.json
```

The confirmed schema is a closed, fixture-first candidate profile. It defines:

- profile `kfm.domains.soil.domain-feature-identity.v1`;
- status `PROPOSED_INACTIVE` and version `1.0.0`;
- deterministic `id` and full SHA-256 `spec_hash` shapes;
- object family, object role, support type, source identity, temporal scope,
  evidence references, match status, and limitations;
- `additionalProperties: false` and `public_use_allowed: false`; and
- canonical-identity, evidence, policy, review, release, and publication effects
  fixed to `false`.

> [!WARNING]
> The schema and validator prove only the bounded `PROPOSED_INACTIVE` candidate
> profile. Enumerated fields are machine-checked for that profile, but this does
> not make the profile canonical, complete across every Soil object/support
> family, active, released, public, or suitable as a runtime API contract.

---

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Defining Soil object identity semantics | Yes | Must preserve object family, source role, support type, source-native ID, time scope, evidence refs, and limitations. |
| Deterministic matching/deduplication guidance | Conditional | Must use stable inputs and expose candidate/confirmed/conflicted posture. |
| Supporting Evidence Drawer identity explanation | Conditional | Requires EvidenceBundle resolution and public-safe projection. |
| Supporting Focus Mode explanation | Conditional | AI may explain released identity only with finite outcomes and citations. |
| Supporting pipeline candidate identity records | Conditional | Pipeline candidates remain unpublished until validation, catalog/triplet, policy, review, and release closure. |
| Connecting identity to map layers or API details | Conditional | Public surfaces must use governed API and released artifacts. |
| Publishing source IDs as public truth by themselves | No | Source-native IDs support identity but do not replace evidence, source role, or release state. |
| Replacing object-family contracts | No | `SoilMapUnit`, `SoilComponent`, `Horizon`, etc. still need their own meaning contracts where material. |

---

## Exclusions

`domain_feature_identity` must not be used as:

| Misuse | Required outcome |
|---|---|
| JSON Schema / machine validation | Use `schemas/contracts/v1/domains/soil/` or ADR-selected schema home. |
| ETL implementation or fuzzy matcher | Use `pipelines/domains/soil/` and tests. |
| SourceDescriptor or source registry record | Use source registry roots and SourceDescriptor contracts. |
| Object-family payload replacement | Use specific object-family contracts/schemas. |
| Map-unit, component, horizon, property, observation, pedon, or interpretation truth by itself | Resolve owning object evidence. |
| Public API response shape | Use API schemas and governed API contracts. |
| Release approval | Use PolicyDecision, ReviewRecord, ReleaseManifest, correction path, and RollbackCard. |
| AI answer authority | Focus Mode remains evidence-subordinate and finite-outcome constrained. |

---

## Recommended fields

The following fields carry semantic meaning in this contract. The current
candidate schema enforces the bounded subset described below; broader lifecycle
and runtime bindings remain proposed.

| Field | Meaning |
|---|---|
| `id` | Deterministic candidate identifier derived from the first 24 hex characters of the candidate digest; not canonical authority. |
| `version` | Candidate-profile version, fixed to `1.0.0` in the current schema. |
| `spec_hash` | Full SHA-256 over sorted compact candidate JSON after removing `id` and `spec_hash`. |
| `domain` | Expected value: `soil`. |
| `object_family` | SoilMapUnit, SoilComponent, Horizon, ComponentHorizonJoin, SoilProperty, HydrologicSoilGroup, SoilMoistureObservation, Pedon, SoilProfileView, ErosionRisk, SuitabilityRating, or SoilTimeCaveat. |
| `object_role` | Role in the soil lane: survey carrier, component, vertical layer, lineage join, property, classification, observation, profile, interpretation, temporal caveat, etc. |
| `support_type` | Static survey, gridded derivative, station observation, satellite grid, pedon/profile, or interpretation support tag. |
| `source_ref` | SourceDescriptor/source registry ref. |
| `source_role` | Source role for this identity use. |
| `source_native_id` | Source-native key or identifier, if available. |
| `source_native_key_family` | MUKEY, COKEY, CHKEY, station ID, grid cell ID, pedon ID, profile ID, source-specific key, etc. |
| `normalized_digest` | Deterministic digest over normalized identity inputs. |
| `match_status` | Candidate, confirmed, conflicted, superseded, denied, or unknown. |
| `observed_time` | Time the source observation was made, if applicable. |
| `source_time` | Source creation/publication/update time. |
| `valid_time` | Interval the identity applies to, if known. |
| `retrieval_time` | KFM retrieval/freeze time. |
| `release_time` | KFM release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `evidence_refs` | EvidenceRefs or EvidenceBundle refs. |
| `policy_decision_ref` | PolicyDecision governing use/publication. |
| `review_ref` | ReviewRecord or steward review ref. |
| `release_manifest_ref` | ReleaseManifest or MapReleaseManifest ref. |
| `rollback_ref` | RollbackCard or rollback target. |
| `limitations` | Caveats: identity envelope only; not source truth, not object payload, not release approval. |

---

## Identity model

A reviewed Soil identity envelope should bind source identity, KFM object family, support type, time scope, digest, evidence, and release posture.

```text
domain_feature_identity = {
  domain,
  object_family,
  object_role,
  support_type,
  source_ref,
  source_role,
  source_native_id,
  source_native_key_family,
  temporal_scope,
  normalized_digest,
  match_status,
  evidence_refs,
  policy_decision_ref,
  review_ref,
  release_manifest_ref,
  rollback_ref
}
```

The exact `PROPOSED_INACTIVE` candidate shape is implemented by the paired schema
and validator. A canonical or public serialized identity shape remains **NEEDS
VERIFICATION**.

---

## Object-family coverage

| Object family | Identity concern | Guardrail |
|---|---|---|
| `SoilMapUnit` | Survey map-unit identity and polygon/unit carrier. | MUKEY-like keys do not become parcel/farm truth. |
| `SoilComponent` | Component identity within a map unit. | Component identity does not replace map-unit or horizon identity. |
| `Horizon` | Vertical layer identity with depth/context. | Horizon identity is not a map polygon by itself. |
| `ComponentHorizonJoin` | Lineage identity linking map unit, component, and horizon. | Join identity does not execute ETL or prove properties. |
| `SoilProperty` | Property identity with method/unit/depth context. | Property values need method, unit, depth, support type, and evidence. |
| `HydrologicSoilGroup` | Runoff-potential classification identity. | Not a flood observation, forecast, or hydrology truth. |
| `SoilMoistureObservation` | Station or satellite observation identity. | Station, satellite, and survey support must not collapse. |
| `Pedon` / `SoilProfileView` | Profile-level identity. | Profile identity is evidence, not broad map-unit truth by itself. |
| `ErosionRisk` | Interpretive risk product identity. | Not an authoritative hazard product. |
| `SuitabilityRating` | Interpretive suitability identity. | Not legal, economic, or operational advice. |
| `SoilTimeCaveat` | Temporal limitation identity. | Caveat must remain attached to stale or time-bounded products. |

---

## Source-role and support rules

| Rule | Requirement |
|---|---|
| Object family is mandatory | A Soil identity without an object family is not reviewable. |
| Support type is mandatory | Static survey, gridded derivative, station observation, satellite grid, pedon/profile, and interpretation cannot masquerade as one surface. |
| Source role is per use | A source may be authority for one use and context for another; identity must record the use-specific role. |
| Source-native IDs are evidence inputs, not identity truth alone | MUKEY/COKEY/CHKEY/station/grid/pedon IDs support identity but must not replace evidence and source-role posture. |
| Normalized digest is deterministic but not sovereign | A digest aids matching; it does not publish or prove a claim. |
| Time axes remain separate | Source time, observed time, valid time, retrieval time, release time, and correction time must not collapse. |
| Public claims require EvidenceBundle resolution | If evidence cannot resolve, return ABSTAIN, DENY, or ERROR; do not invent identity. |

---

## Sensitivity and publication posture

| Surface | Default posture | Reason |
|---|---|---|
| Static survey identities | Public-safe if source, rights, evidence, and release support it | Survey context is typically public but still governed. |
| Gridded derivative identities | Public-safe if released and caveated | Derivatives must not masquerade as survey truth. |
| Station or satellite observation identities | Review / caveat by source family and scale | Point/grid observations can be misread as broader truth. |
| Pedon/profile identities | Review / caveat by source and locality | Profile-level evidence is not map-unit truth by itself. |
| Interpretive identities | Caveated and method-visible | Suitability/erosion interpretations need explicit limitations. |
| Farm-specific, owner-specific, operational, or private sensor identities | Review / restrict / deny by default | Soil doctrine marks these as not public-by-default. |
| Candidate/model/OCR identities | Review only | Automated identity support does not close evidence. |

---

## Invariants

1. **Identity is not object truth by itself.** It is the envelope that makes object identity inspectable.
2. **Support type is part of identity.** Static survey, gridded derivative, station, satellite, pedon/profile, and interpretation identities must not collapse.
3. **Source role is first-class.** Authority, observation, context, model, candidate, and derived roles remain distinct by use.
4. **Native keys are not enough.** Source-native IDs support identity; they do not replace EvidenceBundle or release state.
5. **Time is part of identity.** Source, observed, valid, retrieval, release, and correction times remain distinct where material.
6. **Digest is deterministic, not sovereign.** Matching hashes help review; they do not decide truth. 
7. **Release is separate.** A valid identity does not publish anything without PolicyDecision, ReviewRecord, ReleaseManifest, and RollbackCard where required.
8. **AI is downstream.** Focus Mode may explain only released evidence and policy-permitted identity context.
9. **No direct internal-store reads.** Public clients use governed APIs and released artifacts only.
10. **Path variance remains ADR-sensitive.** Do not use this file to settle contract/schema path variance by tone.

---

## Lifecycle

```mermaid
flowchart LR
  SRC["SourceDescriptor\nrole + rights + cadence"] --> RAW["RAW"]
  RAW --> WQ["WORK / QUARANTINE"]
  WQ --> PROC["PROCESSED\nnormalized soil candidates"]
  PROC --> ID["DomainFeatureIdentity\nsource + role + support + time + digest"]
  ID --> CAT["CATALOG / TRIPLET\nEvidenceBundle refs"]
  CAT --> REVIEW["PolicyDecision + ReviewRecord"]
  REVIEW --> REL["ReleaseManifest + RollbackCard"]
  REL --> PUB["governed API / map / Evidence Drawer / Focus Mode"]

  CONTRACT["contracts/domains/soil/domain_feature_identity.md\nmeaning only"] -. guides .-> ID
  SCHEMA["schemas/contracts/v1/domains/soil/domain_feature_identity.schema.json\nbounded inactive candidate"] -. validates .-> PROC
  POLICY["policy/domains/soil/\nallow/deny/restrict/abstain"] -. gates .-> REVIEW
```

---

## Validation

Before this contract is treated as mature, maintainers should verify:

- [x] paired schema is closed and fixes the candidate profile to `PROPOSED_INACTIVE`;
- [x] schema includes object family, object role, support type, source identity,
  temporal scope, evidence refs, match status, limitations, public-use denial, and
  explicit false authority effects;
- [x] focused fixtures/tests prove one valid candidate plus support-role, public,
  effect, and hash fail-closed cases;
- [ ] fixtures cover all Soil object families, support types, native key families,
  candidate/confirmed/conflicted/superseded identity, stale source vintage, and
  correction lineage;
- [ ] policy, review, release, API/UI, correction, revocation, and rollback
  integration is implemented and independently proved;
- [ ] public map, Evidence Drawer, Focus Mode, exports, and AI summaries use only released/governed identity projections;
- [ ] rollback invalidates linked processed records, catalog/triplet refs, layers, drawer payloads, exports, caches, graph projections, and AI summaries that cited a withdrawn identity.

---

## Rollback

Rollback is required if this contract:

- claims schema, validator, fixture, test, policy, release, API, ETL, map, graph, or runtime behavior exists without proof;
- treats DomainFeatureIdentity as JSON Schema, ETL code, source truth, object payload truth, released-layer truth, or AI authority;
- weakens support-type separation;
- hides source-role conflict, native-key gaps, source vintage, valid-time limits, candidate status, supersession, or correction lineage;
- exposes farm-specific, owner-specific, operational, or private sensor detail without policy/release support;
- normalizes direct UI access to internal lifecycle stores or direct model output.

Rollback target: revert `contracts/domains/soil/domain_feature_identity.md` to prior scaffold blob `84ed1e166084da6d300aa765ab41bc6fefe6c035`, record drift if authority boundaries were affected, and invalidate downstream derivatives that relied on weakened Soil identity semantics.

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior `contracts/domains/soil/domain_feature_identity.md` | `CONFIRMED` | Target file existed as a greenfield scaffold. | Scaffold did not define authoritative semantic contract content. |
| `schemas/contracts/v1/domains/soil/domain_feature_identity.schema.json` | `CONFIRMED bounded candidate schema` | Closed `PROPOSED_INACTIVE` shape, required identity/source/evidence fields, public-use denial, and false authority effects. | Does not establish canonical adoption, active use, release, or publication. |
| `tools/validators/domains/soil/validate_domain_feature_identity.py` | `CONFIRMED executable` | Deterministic candidate digest/ID, support-role separation, source/temporal/canonical-array checks, and finite outcomes. | Local candidate evaluation only; no source, evidence, policy, review, release, or publication effect. |
| `fixtures/domains/soil/domain_feature_identity/cases.json` and focused test | `CONFIRMED synthetic proof` | One valid case plus denial/error polarity for role collapse, authority overclaim, and hash mismatch. | Does not cover all enumerated object/support families or runtime consumers. |
| `contracts/domains/soil/README.md` | `CONFIRMED contract-lane rule` | Defines this folder as semantic meaning only and lists Soil object-family contract candidates. | Does not prove object schema, validator, or release maturity. |
| `docs/domains/soil/ARCHITECTURE.md` | `CONFIRMED doctrine / PROPOSED field realization` | Defines Soil object families, identity rule, source families, support-type separation, cross-lane limits, and lifecycle posture. | Does not prove implementation. |
| `docs/domains/soil/API_CONTRACTS.md` | `CONFIRMED doctrine / PROPOSED implementation` | Defines governed Soil API posture, finite outcomes, trust membrane, and support-type separation. | Route names and runtime behavior remain UNKNOWN / NEEDS VERIFICATION. |
| `docs/domains/soil/DATA_LIFECYCLE.md` | `CONFIRMED navigational register / PROPOSED implementation` | Lists owned Soil object families, source families, sensitivity defaults, and lifecycle posture. | It is a navigational register, not implementation proof. |
| `pipelines/domains/soil/README.md` | `CONFIRMED pipeline-lane doctrine / NEEDS VERIFICATION executable behavior` | Places Soil identity candidates in executable pipeline flow while stating pipeline logic does not own object meaning or release decisions. | Does not prove ETL behavior. |
| Uploaded KFM authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-first, implementation-honest, visually polished Markdown with visible verification and rollback posture. | Authoring guidance, not implementation proof. |

---

## Open questions

| ID | Question | Status |
|---|---|---|
| OQ-SOIL-DFI-01 | Should Soil `domain_feature_identity` remain a domain-specific contract, or should it inherit from a cross-domain identity schema? | OPEN / DOMAIN + SCHEMA REVIEW |
| OQ-SOIL-DFI-02 | Which source-native key families are canonical across SSURGO/SDA, gSSURGO/gNATSGO, station observations, satellite grids, pedons, and interpretations? | OPEN / SOURCE + SCHEMA REVIEW |
| OQ-SOIL-DFI-03 | Which match-status enum is canonical for candidate, confirmed, conflicted, superseded, denied, and unknown identities? | OPEN / SCHEMA REVIEW |
| OQ-SOIL-DFI-04 | How should normalized digest inputs be pinned so identity remains deterministic but reversible through evidence? | OPEN / VALIDATION REVIEW |
| OQ-SOIL-DFI-05 | How should Evidence Drawer and Focus Mode display source-native ID, support type, and match status without elevating identity to source truth? | OPEN / MAP/UI REVIEW |
| OQ-SOIL-DFI-06 | How should rollback invalidate layers, drawer payloads, Focus Mode claims, exports, caches, graph projections, and AI summaries after an identity correction? | OPEN / RELEASE REVIEW |

<p align="right"><a href="#top">Back to top</a></p>
