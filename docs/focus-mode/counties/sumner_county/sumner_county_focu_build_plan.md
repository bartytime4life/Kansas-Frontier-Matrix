<!-- [KFM_META_BLOCK_V2]
doc_id: NEEDS_VERIFICATION
title: Sumner County Focus Mode Build Plan
type: county-focus-mode-build-plan
version: v0.1-proposed
status: PROPOSED
release_status: NEEDS_VERIFICATION
county_name: Sumner County
county_slug: sumner
lane_slug: sumner-county
created: 2026-06-09
updated: 2026-06-09
owners:
  focus_mode_owner: NEEDS_VERIFICATION
  evidence_steward: NEEDS_VERIFICATION
  agriculture_reviewer: NEEDS_VERIFICATION
  transport_history_reviewer: NEEDS_VERIFICATION
  hydrology_reviewer: NEEDS_VERIFICATION
  archaeology_cultural_reviewer: NEEDS_VERIFICATION
  infrastructure_security_reviewer: NEEDS_VERIFICATION
  privacy_property_reviewer: NEEDS_VERIFICATION
  rights_reviewer: NEEDS_VERIFICATION
  release_approver: NEEDS_VERIFICATION
defining_public_safe_boundary: >-
  Sumner County's Chisholm Trail, historic railroad, agriculture, planning,
  river, municipal-airport, utility, road, parcel, and emergency-service
  sources may support generalized, time-bounded interpretation, but must not
  become present-day property-access or route permission, title or landowner
  profiling, current rail/airport/utility/road/emergency operations,
  infrastructure-vulnerability analysis, private-well or water-right
  conclusions, live flood/tornado/weather guidance, or exact archaeological,
  burial, sacred, or other sensitive cultural-location disclosure.
collision_search:
  supplied_completed_register: CONFIRMED absent
  current_conversation_register: CONFIRMED Butler, Cheyenne, Nemaha, and Russell completed; Sumner absent
  live_county_index: CONFIRMED listed not-started on 2026-06-09
  exact_title_search: CONFIRMED no result
  filename_search: CONFIRMED no result
  slug_search: CONFIRMED no result
  branch_search: CONFIRMED no result
  pull_request_search: CONFIRMED no result
  issue_search: CONFIRMED no result
  accessible_project_materials: CONFIRMED no Sumner County plan found
  exhaustive_private_deleted_local_prior_chat_absence: NEEDS_VERIFICATION
directory_rules_basis:
  principle: responsibility root outranks topic name
  observed_template_path: docs/focus-mode/counties/<county-slug>-county/build-plan.md
  path_divergence: docs/focus-mode/ and docs/focus-modes/ references coexist
  legacy_path: docs/focus-mode/counties/<county>_county/<county>_county_focus_mode_build_plan.md
  path_status: PROPOSED / NEEDS_VERIFICATION
official_sources_checked:
  - Sumner County official website
  - Sumner County Comprehensive Plan page
  - Sumner County Farming in Sumner page
  - Sumner County Railroad History page
  - City of Wellington official website
  - U.S. Census Bureau QuickFacts
  - USDA NASS 2022 Sumner County profile
  - National Weather Service Wichita
implementation_claim: none
repository_modification_claim: none
review_or_validation_claim: none
promotion_or_publication_claim: none
truth_labels: [CONFIRMED, PROPOSED, NEEDS_VERIFICATION, UNKNOWN]
finite_outcomes: [ANSWER, ABSTAIN, DENY, ERROR]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Sumner County Focus Mode — Build Plan

> **Wheat, Chisholm Trail memory, railroad development, border-county settlement, planning, rivers, and municipal systems—without turning historic corridors or public records into present-day access, operational, ownership, safety, or infrastructure-vulnerability conclusions.**

**Product thesis:** Build a governed, map-first, time-aware Sumner County explainer that connects the county's wheat economy, historic cattle-trail and railroad development, Wellington and other communities, county planning, later hydrology and geology, and current public-authority redirects while preserving source roles, property boundaries, infrastructure security, cultural sensitivity, currentness, correction, and rollback.

![status](https://img.shields.io/badge/status-PROPOSED-yellow)
![county](https://img.shields.io/badge/county-Sumner%20County-blue)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)
![boundary](https://img.shields.io/badge/boundary-no%20access%2Foperations%2Fvulnerability%20inference-orange)
![outcomes](https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-6f42c1)
![release](https://img.shields.io/badge/release-NEEDS%20VERIFICATION-lightgrey)

> [!IMPORTANT]
> **Defining public-safe boundary.** Historic Chisholm Trail and railroad evidence may explain county development, but it does not establish present-day public access, road status, easement, ownership, active rail status, or safe travel. Public parcel, airport, utility, road, planning, and emergency sources must not become owner profiles, infrastructure-vulnerability products, live operational guidance, or exact sensitive cultural-location disclosure.

## Status and identity

| Field | Value | Truth posture |
|---|---|---|
| County | Sumner County, Kansas | `CONFIRMED` |
| FIPS | `20191` | `CONFIRMED` |
| Slug | `sumner` | `PROPOSED` |
| Lane | `sumner-county` | `PROPOSED` |
| Artifact | `sumner_county_focus_mode_build_plan.md` | `CONFIRMED` |
| Created / updated | 2026-06-09 | `CONFIRMED` |
| Implementation | Not claimed | `UNKNOWN` |
| Source admission | Not performed | `CONFIRMED` |
| Validation/review | Not performed | `CONFIRMED` |
| Release/publication | Not performed | `CONFIRMED` |
| Canonical repo path | Singular/plural convention unresolved | `NEEDS_VERIFICATION` |
| Exhaustive collision absence | Not provable across private/deleted/local artifacts | `NEEDS_VERIFICATION` |

## Quick links

[Operating posture](#1-operating-posture) · [Why this county](#2-why-this-county) · [Product thesis](#3-product-thesis) · [Scope](#4-scope-boundary) · [Layers](#5-first-demo-layers) · [Journeys](#6-user-journeys) · [UI](#7-ui-surfaces) · [Objects](#8-governed-object-model) · [Repository](#9-proposed-repository-shape) · [Phases](#10-build-phases) · [PRs](#11-first-pr-sequence) · [Acceptance](#12-acceptance-checklist) · [Fixtures](#13-fixture-plan) · [Risks](#14-risk-register) · [Sources](#15-source-seed-list) · [Questions](#16-open-verification-questions) · [Milestone](#17-recommended-first-milestone)

## Executive build note

Sumner County is a strong next proof slice because it combines:

- **large-scale crop agriculture:** USDA NASS reports 1,013 farms, 750,650 acres in farms, $181.886 million in products sold, a 92% crop / 8% livestock-products split, and 24,047 irrigated acres for 2022;
- **historic corridors:** county pages cover the Chisholm Trail and railroad development, but those historical narratives do not establish current access or operations;
- **planning and property-adjacent systems:** the county exposes a comprehensive-plan index, parcel and tax search, appraiser mapping, planning/zoning, road/bridge, and emergency-management surfaces;
- **municipal infrastructure:** Wellington exposes airport, electric, water, wastewater, streets, GIS, fire/EMS, zoning, and city-lake information that is useful as authority context but unsafe as a vulnerability map;
- **operational hazards:** NWS Wichita is the appropriate current authority for tornado, flood, fire-weather, and related warnings;
- **future environmental layers:** Chikaskia/Arkansas watershed context, lowland geology, soils, groundwater, and floodplain sources are promising but require admission and must not become private-well, drainage-liability, or property-level conclusions.

### Collision result

| Check | Result | Status |
|---|---|---|
| Supplied register | Sumner absent | `CONFIRMED` |
| Recent plans | Butler, Cheyenne, Nemaha, Russell completed; Sumner absent | `CONFIRMED` |
| Live index | Sumner listed `not-started` | `CONFIRMED` |
| Title/filename/slug searches | No match | `CONFIRMED` |
| Branch/PR/issue searches | No match | `CONFIRMED` |
| Accessible project materials | No plan found | `CONFIRMED` |
| Private/deleted/local/prior-chat artifacts | Not exhaustive | `NEEDS_VERIFICATION` |

### Directory Rules basis

The observed template uses:

`docs/focus-mode/counties/<county-slug>-county/build-plan.md`

Human planning belongs under `docs/`; semantic meaning under `contracts/`; machine shape under `schemas/`; policy under `policy/`; fixtures under `fixtures/`; deployables under `apps/`; lifecycle evidence and published data under `data/`; release decisions under `release/`.

Repository references also use `docs/focus-modes/`, so the divergence must be resolved before integration. All paths below remain `PROPOSED / NEEDS_VERIFICATION`.

## Evidence boundary

| Label | This plan's use |
|---|---|
| `CONFIRMED` | Collision searches performed; checked official sources; verified Census/NASS values; artifact created. |
| `PROPOSED` | Product, boundary, layers, objects, paths, policies, fixtures, tests, UI, release and rollback design. |
| `NEEDS_VERIFICATION` | Exhaustive collision absence, canonical path, rights, geometry authority, trail/rail precision, cultural review, current operations, source admission, release approval. |
| `UNKNOWN` | Current implementation, CI, admitted sources, runtime behavior, EvidenceBundles, validation, release, correction and rollback execution. |

---

# 1. Operating posture

## 1.1 Governing rules

1. `EvidenceBundle` outranks county-history prose, planning summaries, map symbols, search results, and generated language.
2. Public UI reads governed APIs and released artifacts only.
3. Public UI must not read `RAW`, `WORK`, `QUARANTINE`, parcel/tax systems, direct rail/airport/utility/emergency sources, or direct model output.
4. Preserve `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`.
5. Promotion is a governed state transition.
6. Historic trail, historic rail, current road, active railroad, parcel boundary, easement, and legal access are distinct.
7. A published comprehensive plan is not proof of adoption, implementation, funding, or current legal effect.
8. Parcel, tax, appraisal, deed, zoning, and map sources are not title or owner-profile authority.
9. Municipal airport, utility, road, GIS, fire/EMS, and shelter pages do not authorize tactical or vulnerability analysis.
10. Historical and cultural narratives do not replace KSHS or Nation-authoritative review.
11. NASS and Census remain time-bounded aggregates.
12. Current hazards and operations redirect to current authorities.
13. Every result is `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.

## 1.2 Finite outcomes

| Outcome | Use |
|---|---|
| `ANSWER` | Released evidence supports a bounded cited answer. |
| `ABSTAIN` | Evidence, status, rights, authority, currentness, or precision is insufficient. |
| `DENY` | Access, owner profiling, exact infrastructure, vulnerability, private-water, individual-farm, or sensitive cultural precision is prohibited. |
| `ERROR` | Contract, evidence, citation, policy, manifest, integrity, or service failure. |

## 1.3 Trust membrane

```mermaid
flowchart LR
    S[Official source] --> I[Source intake]
    I --> R[RAW]
    R --> G{Identity · role · rights · time · sensitivity}
    G -->|unclear/unsafe| Q[WORK / QUARANTINE]
    G -->|admissible| P[PROCESSED]
    P --> E[EvidenceRef → EvidenceBundle]
    E --> C[CATALOG / TRIPLET]
    C --> V{Policy · citation · review · release}
    V -->|fail| H[HOLD / ABSTAIN / DENY]
    V -->|pass| M[ReleaseManifest]
    M --> A[Governed API / released tiles]
    A --> U[Public UI]
    U --> O[ANSWER / ABSTAIN / DENY / ERROR]
```

## 1.4 County guardrails

| Topic | Guardrail |
|---|---|
| Chisholm Trail | Generalized history only; no present road, easement, parcel, or access conclusion. |
| Historic rail | No inference of current ownership, operations, cargo, crossings, access, or safety. |
| Current transportation | No live rail/road/airport schedule, closure, routing, maintenance, weak-point, or disruption analysis. |
| Agriculture | County aggregates only; preserve suppression; no farm/field/producer inference. |
| Planning | Publish/adopt/amend/implement/supersede remain distinct. |
| Parcel/tax/appraisal | No title, ownership, debt, access, valuation, or living-person profile. |
| Utilities | Authority redirect/generalized category only; no topology, capacity, dependency, or failure-path analysis. |
| Emergency/shelter | No capacity, tactical routing, response-gap, or vulnerability scoring. |
| Rivers/floodplain | No live flood, drainage-liability, private-well, water-right, or property-level conclusion. |
| Archaeology/culture | Exact sites, burials, sacred places, and discovery-enabling descriptions withheld. |
| Weather | Historical interpretation allowed after review; current warning questions redirect. |

## 1.5 Candidate reason codes

| Code | Outcome | Meaning |
|---|---|---|
| `SU-EVIDENCE-MISSING` | `ABSTAIN` | Evidence does not resolve. |
| `SU-EVIDENCE-STALE` | `ABSTAIN` | Evidence outside time window. |
| `SU-PLAN-STATUS-UNCLEAR` | `ABSTAIN` | Plan status unresolved. |
| `SU-TRANSPORT-STATUS-UNCLEAR` | `ABSTAIN` | Current route/operation unresolved. |
| `SU-RIGHTS-UNCLEAR` | `ABSTAIN` | Reuse rights unresolved. |
| `SU-LIVE-HAZARD-REDIRECT` | `ABSTAIN` | Current authority required. |
| `SU-PROPERTY-ACCESS` | `DENY` | Title/easement/access request. |
| `SU-OWNER-PROFILE` | `DENY` | Landowner/living-person profiling. |
| `SU-INDIVIDUAL-FARM` | `DENY` | Operation-level inference. |
| `SU-INFRASTRUCTURE-EXACT` | `DENY` | Exact operational infrastructure. |
| `SU-VULNERABILITY-ANALYSIS` | `DENY` | Weak-point/dependency/disruption analysis. |
| `SU-ARCHAEOLOGY-EXACT` | `DENY` | Exact sensitive cultural location. |
| `SU-PRIVATE-WATER` | `DENY` | Private-well/water-right/property water conclusion. |
| `SU-INTEGRITY-FAIL` | `ERROR` | Integrity/citation/schema failure. |
| `SU-SERVICE-UNAVAILABLE` | `ERROR` | Governed dependency unavailable. |

---

# 2. Why this county

## 2.1 Selection screen

| Candidate | Result | Decision |
|---|---|---|
| Butler, Cheyenne, Nemaha, Russell | Completed in current conversation | Reject |
| Graham | Live index `draft` | Reject |
| Sumner | Not in register, live index `not-started`, no searched collision | **Select** |
| Wichita / Lane | Unused candidates | Hold |

## 2.2 Proof-slice rationale

| Dimension | Value | Governance challenge |
|---|---|---|
| Agriculture | Major wheat and crop economy | Aggregate-only; no field/operation inference |
| Chisholm Trail | Strong historic identity | Historic corridor ≠ public access |
| Railroad history | Multiple lines and successor narratives | Historic line ≠ current operations |
| Planning | Comprehensive-plan chapters | Publication ≠ adoption/implementation |
| Property systems | Parcel/tax/appraiser/deeds | Public availability ≠ title/profile authority |
| Municipal systems | Airport, utilities, GIS, roads, fire/EMS | No operational dependency/vulnerability map |
| Border/corridors | Oklahoma boundary and north-south routes | Cross-jurisdiction and time-aware route status |
| Hazards | Tornado/flood history plus NWS current authority | Historical event ≠ current warning |
| Hydrology/geology | River, floodplain, groundwater and lowlands candidates | No private-water/property conclusion |
| Culture/archaeology | County history surfaces | Exact sites and authority require fail-closed review |

## 2.3 Distinct value

Sumner County tests **time-separated corridor truth**: nineteenth-century cattle trails, abandoned rail grades, active railways, present highways, private parcels, public rights-of-way, airports, utilities, and emergency routes cannot be flattened into one line layer. Historical continuity does not create present-day rights.

## 2.4 Public benefit

Users can learn county agriculture, historic transportation, settlement and planning while seeing:

- which source role supports each statement;
- when the evidence applies;
- whether geometry is historical, reconstructed, current, generalized, or unknown;
- why access and operations cannot be inferred;
- where current official authorities must answer.

---

# 3. Product thesis

## 3.1 Thesis

**Sumner County Focus Mode will explain agriculture, historic cattle and railroad corridors, planning, settlements, and later environmental context through released evidence while refusing present-day access inference, owner profiling, current transport/utility/emergency operations, infrastructure vulnerability, private-water conclusions, and exact sensitive cultural locations.**

## 3.2 Promises

- Evidence-visible and cite-or-abstain.
- Historic/current routes visually distinct.
- `access_status` visible.
- Agriculture remains aggregate and dated.
- Planning status explicit.
- Current operations redirect.
- Sensitive cultural precision withheld.
- Correction and rollback inspectable.

## 3.3 Non-promises

No title, easement, ownership, access, current rail/airport/utility operation, hazardous cargo, weak-point, shelter-capacity, live hazard, private-well, water-right, property-flood, individual-farm, or exact archaeology conclusion.

---

# 4. Scope boundary

| Class | Content | Posture |
|---|---|---|
| First slice | County frame, communities, Census, NASS 2022, historical rail card, generalized trail card, plan index, authority redirects | `PROPOSED` |
| Deferred | Exact trail/rail geometry, current transportation, hydrology, floodplain, soils/geology, historic maps, utilities, airport, archaeology | `DEFER` |
| Denied | Owner profiles, access permission, exact infrastructure, vulnerability, private water, exact sensitive sites | `DENY` |
| Excluded | Restricted, tactical, credentialed, rights-unclear, privacy-invasive, unsafe material | `EXCLUDE` |

### Boundary applications

- **Historical route:** may explain past movement; cannot establish current access.
- **Property:** may use safe aggregates only; no owner or title profile.
- **Infrastructure:** authority categories and redirects only; no topology or weakness.
- **Water/hazards:** historical/scientific context only; current and property-level questions abstain.
- **Culture:** exact sensitive locations and unreviewed Nation-related claims withheld.
- **Rights:** public visibility is not derivative-display permission.

---

# 5. First demo layers

| Priority | Card/layer | Seed | Gates | Status |
|---|---|---|---|---|
| 1 | County frame and communities | Census + county | FIPS, vintage, CRS, digest | `PROPOSED` |
| 2 | 2022 agriculture | NASS | Year, suppression, aggregate policy | `PROPOSED` |
| 3 | Population/economy | Census | Vintage and methodology | `PROPOSED` |
| 4 | Historical railroad development | County rail history | Historical role; no current inference | `PROPOSED` |
| 5 | Generalized Chisholm Trail | County seed + later KSHS/NPS/Nation review | Geometry authority, culture, access denial | `DEFER` |
| 6 | Comprehensive-plan index | County | Chapter identity; adoption/implementation status | `PROPOSED` |
| 7 | Wellington authority card | City | Redirect only for airport/utilities/fire/streets | `PROPOSED` |
| 8 | Hazard authority card | NWS | Current redirect/expiry | `PROPOSED` |
| 9 | River/watershed | USGS/KGS/KDHE/FEMA candidates | No private-water/property claim | `DEFER` |
| 10 | Current transport | KDOT/FRA/FAA candidates | No operations/vulnerability | `DEFER` |
| 11 | Archaeology/culture | KSHS/Nation candidates | No exact locations | `DEFER` |
| 12 | Owner, active operations, exact infrastructure/sites | Various | Fail closed | `DENY` |

```mermaid
flowchart TB
    B[County frame]
    C[Census]
    A[NASS agriculture]
    R[Historic rail]
    T[Generalized trail]
    P[Plan index]
    W[Wellington authority]
    O[Operational redirects]
    E[Evidence Drawer]
    G[Boundary panel]
    B --> C
    B --> A
    B --> R
    B --> T
    B --> P
    B --> W
    B --> O
    C --> E
    A --> E
    R --> E
    T --> E
    P --> E
    W --> E
    E --> G
```

### Layer-card truth contract

Each card carries stable ID, knowledge character, source role, document status, EvidenceRefs, temporal/spatial basis, geometry confidence, rights, sensitivity, access status, transform receipt, PolicyDecision, CitationValidationReport, ReviewRecord, ReleaseManifest, CorrectionNotice, RollbackPlan, and county boundary notice.

---

# 6. User journeys

## Learning journeys

1. **Agriculture:** answer with 2022 NASS totals and no operation inference.
2. **Railroad history:** explain historical development while current ownership/operation remains separate.
3. **Chisholm Trail:** show reviewed generalized corridor with `access_status=not_established`.
4. **Planning:** list plan chapters without asserting adoption or implementation.
5. **County frame:** compare 2025 population estimate 22,312 and 2020 Census count 22,382.

## Trust journeys

- Historic rail selection shows source date, geometry confidence, current status `UNKNOWN`, and no access claim.
- Plan card separates publication, adoption, amendment and implementation.
- Parcel + trail + owner query returns `DENY`.
- Source correction versions geometry and preserves prior release.

## Negative journeys

| Request | Outcome | Reason |
|---|---|---|
| Drive/walk old trail across a parcel | `ABSTAIN`/`DENY` | `SU-PROPERTY-ACCESS` |
| List owners along trail/rail | `DENY` | `SU-OWNER-PROFILE` |
| Active trains/cargo/crossing weak point | `DENY` | Infrastructure/vulnerability |
| Airport access and weak security | `DENY` | `SU-INFRASTRUCTURE-EXACT` |
| Utility failure dependency map | `DENY` | `SU-VULNERABILITY-ANALYSIS` |
| Shelter capacity ranking | `DENY` | Tactical emergency analysis |
| Plan proposal currently law | `ABSTAIN` | `SU-PLAN-STATUS-UNCLEAR` |
| Identify farm behind crop total | `DENY` | `SU-INDIVIDUAL-FARM` |
| Private well safe | `DENY` | `SU-PRIVATE-WATER` |
| Exact archaeology/burial coordinates | `DENY` | `SU-ARCHAEOLOGY-EXACT` |
| Tornado warning/flooded road now | `ABSTAIN` | `SU-LIVE-HAZARD-REDIRECT` |

---

# 7. UI surfaces

## Required surfaces

- Header with release, freshness, correction, and boundary badges.
- Map canvas using released sources only.
- Layer drawer with historical/current, source role, status, time, rights, sensitivity, geometry confidence, and access status.
- Evidence Drawer with claim, EvidenceBundle, publisher, dates, geometry, rights, policy, review, transform, correction, release and rollback.
- Distinct answer, denial, abstention and error panels.
- Timeline/status panel.
- County boundary panel.
- Official-authority redirect panel.
- Correction/release panel.
- Accessible legend.

## County boundary panel

> **Historic corridor does not establish present rights.** Sumner County trail and railroad evidence may explain the past, but it does not establish a current public road, easement, crossing, active line, ownership, or permission. Public airport, utility, road, parcel, planning, and emergency records must not become profiles, tactical operations, vulnerability analysis, or live hazard guidance.

## Legend

| Term | Meaning |
|---|---|
| Historical corridor | Past route evidence, not present access |
| Reconstructed geometry | Derived alignment with uncertainty |
| Current transportation | Present route/operation needing current authority |
| Planning document | Published material, not automatic implementation |
| Statistical aggregate | County summary, not individual operation/person |
| Access not established | No legal permission conclusion |
| Operational redirect | Current authority link |
| Generalized geometry | Precision reduced by policy |
| Sensitive withheld | Detail not released |
| Generated summary | Downstream text subordinate to evidence |

```mermaid
sequenceDiagram
    participant U as User
    participant UI as Focus UI
    participant API as Governed API
    participant P as Policy
    participant E as Evidence Resolver
    participant R as Released Artifacts

    U->>UI: Ask/select
    UI->>API: Context + request
    API->>P: Precheck access/privacy/operations
    alt prohibited
        P-->>API: DENY
        API-->>UI: DENY + reason
    else potentially safe
        P-->>API: Continue
        API->>E: Resolve EvidenceRefs
        E->>R: Fetch bundles/manifests
        R-->>E: Released evidence
        E-->>API: Resolution
        API->>P: Postcheck role/time/rights/geometry
        alt sufficient
            P-->>API: ANSWER
            API-->>UI: Cited ANSWER
        else insufficient/current authority needed
            P-->>API: ABSTAIN
            API-->>UI: ABSTAIN + redirect
        else failure
            API-->>UI: ERROR
        end
    end
```

---

# 8. Governed object model

## Shared concepts

`SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `PolicyDecision`, `RuntimeResponseEnvelope`, `CitationValidationReport`, `ReleaseManifest`, `AIReceipt`, `ReviewRecord`, `CorrectionNotice`, and `RollbackPlan`.

## County candidates

| Object | Purpose |
|---|---|
| `SumnerCountyFrame` | FIPS, geometry, CRS, border relations |
| `HistoricCorridorCard` | Historical subject, date, source, confidence, non-access claim |
| `HistoricAlignmentGeometry` | Derived geometry with provenance |
| `AccessStatusDecision` | `not_established`, `public_confirmed`, `restricted`, `unknown` |
| `CurrentTransportAuthorityRef` | Current road/rail/airport redirect |
| `PlanningDocumentStatus` | published/adopted/amended/implemented/superseded/unknown |
| `AgricultureCountySnapshot` | NASS aggregate and suppression |
| `MunicipalSystemAuthorityCard` | Safe service category and redirect |
| `InfrastructurePrecisionDecision` | exact/generalized/withheld |
| `SensitiveCulturalTransform` | Redaction/generalization receipt |

## Anti-collapse rules

Historic trail ≠ public road; historic rail ≠ active railroad; plan publication ≠ implementation; parcel/tax/deed ≠ title/profile; utility/airport page ≠ system topology or security state; NASS ≠ individual farm; Census ≠ living person; generated prose cannot infer access or restore withheld precision.

## Minimal `ANSWER`

```json
{
  "schema_version": "1.0",
  "outcome": "ANSWER",
  "question": "What did the 2022 Census of Agriculture report?",
  "answer": "USDA NASS reported 1,013 farms, 750,650 acres in farms, $181.886 million in products sold, 92 percent crop sales, and 24,047 irrigated acres. These are 2022 county aggregates.",
  "county_fips": "20191",
  "evidence_refs": ["kfm:evidence-ref:nass:2022:sumner-ks"],
  "policy_decision": {
    "outcome": "ALLOW",
    "reason_codes": ["PUBLIC_AGGREGATE", "SUPPRESSION_PRESERVED"]
  },
  "reporting_year": 2022,
  "release_manifest_ref": "NEEDS_VERIFICATION",
  "rollback_ref": "NEEDS_VERIFICATION"
}
```

## `ABSTAIN`

```json
{
  "schema_version": "1.0",
  "outcome": "ABSTAIN",
  "question": "Can I drive the historic trail across this property?",
  "reason_codes": ["SU-PROPERTY-ACCESS", "SU-PRECISION-UNSUPPORTED"],
  "explanation": "Historical corridor evidence does not establish a present road, easement, ownership, or permission.",
  "authority_redirect": "Relevant landowner and local road authority"
}
```

## `DENY`

```json
{
  "schema_version": "1.0",
  "outcome": "DENY",
  "question": "Combine owners with rail, airport, and utility weak points.",
  "reason_codes": [
    "SU-OWNER-PROFILE",
    "SU-INFRASTRUCTURE-EXACT",
    "SU-VULNERABILITY-ANALYSIS"
  ],
  "explanation": "KFM does not combine personal or property records with exact operational infrastructure to create profiles or vulnerability analysis."
}
```

## Deterministic identity and `spec_hash`

Candidate IDs use FIPS + geometry vintage; publisher + source title + event/revision + digest; corridor ID + evidence digest + transform version; plan title + publication/adoption date; NASS year + FIPS; policy version + request class + evidence digest.

`spec_hash` should cover schema/contract versions, historical/current classification, geometry reconstruction and confidence, access rules, infrastructure generalization, privacy thresholds, planning-status vocabulary, expiry windows, layer composition, evidence resolution, citation validation, and UI behavior. Exact canonicalization remains `NEEDS_VERIFICATION`; JCS + SHA-256 is `PROPOSED`.

---

# 9. Proposed repository shape

| Responsibility | Candidate path | Status |
|---|---|---|
| Build plan | `docs/focus-mode/counties/sumner-county/build-plan.md` | `PROPOSED / NEEDS_VERIFICATION` |
| Requested artifact | `sumner_county_focus_mode_build_plan.md` | Deliverable only |
| Lane docs | `docs/focus-mode/counties/sumner-county/` | `PROPOSED / NEEDS_VERIFICATION` |
| Contract | `contracts/focus_mode/sumner_county_focus_mode.md` | `PROPOSED / NEEDS_VERIFICATION` |
| Shared schema | `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json` | Reuse candidate |
| Extension schema | `schemas/contracts/v1/focus_mode/sumner_county_extension.schema.json` | Only if justified |
| Sources | `data/catalog/sources/sumner-county/source_descriptors.yaml` | `PROPOSED / NEEDS_VERIFICATION` |
| Fixtures | `fixtures/focus_modes/sumner-county/{valid,invalid}/` | `PROPOSED / NEEDS_VERIFICATION` |
| Policy | `policy/focus_modes/sumner-county/` | `PROPOSED / NEEDS_VERIFICATION` |
| UI | `apps/explorer-web/src/focus-modes/sumner-county/` | `PROPOSED / NEEDS_VERIFICATION` |
| Mock API | `apps/governed-api/fixtures/focus-modes/sumner-county/` | `PROPOSED / NEEDS_VERIFICATION` |
| Release | `release/candidates/focus-modes/sumner-county/` | `PROPOSED / NEEDS_VERIFICATION` |
| Published payload | `data/published/api_payloads/focus-modes/sumner-county.json` | Later only |

```text
docs/focus-mode/counties/sumner-county/
  README.md
  build-plan.md
  layer-registry.md
  evidence-model.md
  acceptance-checklist.md
  source-seed-list.md
  public-safety-notes.md

contracts/focus_mode/
schemas/contracts/v1/focus_mode/
fixtures/focus_modes/sumner-county/{valid,invalid}/
policy/focus_modes/sumner-county/
apps/explorer-web/src/focus-modes/sumner-county/
apps/governed-api/fixtures/focus-modes/sumner-county/
data/catalog/sources/sumner-county/
release/candidates/focus-modes/sumner-county/
```

### Placement prohibitions

No root-level county, Chisholm Trail, railroad, wheat, or corridor folder; no parallel authority homes; no parcel/tax/owner copy in docs/UI; no direct active infrastructure or archaeology data in public code; no publication by file move.

No proposed county-specific file is claimed to exist.

---

# 10. Build phases

| Phase | Entry | Output | Exit | Rollback |
|---|---|---|---|---|
| 0 Collision/path | Current repo | Memo/path decision | No collision/parallel lane | Stop |
| 1 Documentation | Phase 0 clear | Seven draft docs | Required sections/labels | Revert |
| 2 Source ledger | Docs drafted | Candidates + rights/status matrix | No assumed admission | Remove |
| 3 Shared objects | Repo inspected | Reuse map/extension proposal | No duplicate authority | Revert |
| 4 Fixtures | Shape stable | Valid/invalid packs | Schema/negative tests | Remove |
| 5 Policy/validators | Invalid pack | Access/privacy/operations rules | High-risk fail closed | Revert |
| 6 Mock API/UI | Tests pass | Static UI/envelopes | No direct source access | Disable |
| 7 Dry-run release | Mock passes | Manifest/citations/correction/rollback | Closure without alias | Delete candidate |
| 8 Optional release | Independent approval | Static public-safe payload | Gates A–G | Repoint prior |

```mermaid
flowchart TD
    A[Collision/path] --> B[Docs]
    B --> C[Source ledger/boundary]
    C --> D[Contract/schema reuse]
    D --> E[Fixtures]
    E --> F[Policy/validators]
    F --> G[Mock API/UI]
    G --> H[Dry-run proof]
    H --> I{Go/no-go}
    I -->|No| J[Hold/correct]
    I -->|Yes| K[Optional release]
```

---

# 11. First PR sequence

1. Verification and documentation control.
2. Source ledger/admission and public-safe boundary.
3. Contracts/schemas or shared-object reuse.
4. Valid and invalid fixtures.
5. Policy and validators.
6. Mock governed API/UI.
7. Dry-run release proof.
8. Only then optional minimal public-safe publication.

> [!CAUTION]
> Live parcel/tax/deed, active railroad, airport, utility, road, emergency, flood, weather, archaeology, private-well, or current-access integration and public release are not first-PR work.

---

# 12. Acceptance checklist

## Governance/evidence

- [ ] All answer claims resolve to EvidenceBundles.
- [ ] Source role, time, rights, geometry, status and sensitivity visible.
- [ ] Generated language remains downstream.
- [ ] Promotion, correction and rollback auditable.

## Role and boundary

- [ ] Historic trail does not imply access.
- [ ] Historic rail does not imply active operation.
- [ ] Plan publication does not imply implementation.
- [ ] Parcel/tax/deed does not become title/profile.
- [ ] Airport/utility/emergency pages do not become vulnerability truth.
- [ ] No individual-farm inference.
- [ ] No exact archaeology/burial/sacred location.
- [ ] No private-water or live-hazard conclusion.

## Currentness/UI

- [ ] Historic/current symbology distinct.
- [ ] Access status visible.
- [ ] Operational sources expire or redirect.
- [ ] NASS and Census vintages explicit.
- [ ] Four outcomes distinct and accessible.
- [ ] Evidence Drawer resolves.
- [ ] Corrections and release state visible.

## Placement/validation/release

- [ ] Directory Rules/path divergence resolved.
- [ ] No parallel authority root.
- [ ] Schemas/reason codes/citations/digests validate.
- [ ] Invalid fixtures fail closed.
- [ ] Public client cannot access nonreleased stores.
- [ ] ReleaseManifest, review, correction and rollback complete.
- [ ] No in-place overwrite.

---

# 13. Fixture plan

## Valid fixtures

| Fixture | Expected |
|---|---|
| `valid-answer-nass-2022.json` | `ANSWER` |
| `valid-answer-census-vintages.json` | `ANSWER` |
| `valid-answer-railroad-history.json` | `ANSWER` |
| `valid-answer-plan-index.json` | `ANSWER` |
| `valid-answer-trail-generalized.json` | `ANSWER` |
| `valid-abstain-current-rail.json` | `ABSTAIN` |
| `valid-abstain-trail-access.json` | `ABSTAIN` |
| `valid-abstain-live-weather.json` | `ABSTAIN` |
| `valid-deny-owner-corridor-join.json` | `DENY` |
| `valid-deny-vulnerability.json` | `DENY` |
| `valid-deny-archaeology.json` | `DENY` |
| `valid-error-integrity.json` | `ERROR` |

## Invalid/fail-closed fixtures

| Fixture | Failure |
|---|---|
| `invalid-answer-no-evidence.json` | Validation fail |
| `invalid-historic-trail-as-road.json` | Fail |
| `invalid-historic-rail-as-active.json` | Fail |
| `invalid-plan-as-implemented.json` | Fail |
| `invalid-owner-trail-join.json` | `DENY` |
| `invalid-active-train-cargo.json` | `DENY` |
| `invalid-crossing-disruption.json` | `DENY` |
| `invalid-airport-security.json` | `DENY` |
| `invalid-utility-dependency.json` | `DENY` |
| `invalid-shelter-ranking.json` | `DENY` |
| `invalid-archaeology-coordinates.json` | `DENY` |
| `invalid-private-well.json` | `DENY` |
| `invalid-nass-farm-inference.json` | `DENY` |
| `invalid-suppressed-reconstruction.json` | `DENY` |
| `invalid-stale-warning.json` | `ERROR`/`ABSTAIN` |
| `invalid-web-visibility-rights.json` | `ABSTAIN` |
| `invalid-release-no-rollback.json` | Gate fail |
| `invalid-correction-overwrite.json` | Fail |

### Highest-risk pack

Historic route as current public road; owner joins; active train/cargo and crossing vulnerability; airport access control; utility dependency; shelter capacity; exact archaeology; private well/water right; individual farm/suppression reconstruction; release without correction/rollback.

---

# 14. Risk register

| Risk | Likelihood | Impact | Mitigation | Release |
|---|---|---|---|---|
| Historic trail implies access | High | High | Access status and strong notice | Block |
| Historic rail treated current | High | High | Separate source families | Block |
| Corridor + parcel profiles owners | High | High | Deny joins; no direct connector | Block |
| Rail/airport/utility vulnerability | Medium | Critical | Exclude/generalize/security review | Block |
| Emergency/shelter tactical analysis | Medium | High | Redirect only | Block |
| Plan publication mistaken for implementation | High | High | Status vocabulary/evidence gate | Block |
| History treated as archaeology/cultural authority | Medium | High | KSHS/Nation review | Defer |
| Public page treated as license | High | Medium | Per-asset rights review | Hold |
| NASS 2022 presented current | High | Medium | Year labels | Block |
| Suppressed values reconstructed | Medium | High | Query/join controls | Block |
| Flood layer becomes property safety advice | Medium | High | Generalized only | Block |
| Private-water inference | Medium | High | Deny/redirect | Block |
| Historic geometry overstates accuracy | High | Medium | Confidence/uncertainty | Hold |
| Stale warning/road status | High | High | Expiry/redirect | Block |
| Correction or rollback untested | Medium | High | Dry-run | Block |
| Path divergence | High | Medium | ADR/drift resolution | Block merge |
| AI hides uncertainty | High | High | Citation validation/finite outcomes | Block |

---

# 15. Source seed list

## Official sources checked

### Sumner County official website
- URL: https://co.sumner.ks.us/
- Role: county administrative authority and local historical publisher.
- Verified: officials, budgets, deeds, tax/parcel/appraiser links, emergency management, planning, comprehensive plan, road/bridge, and county-history categories.
- Limits: changing content; property/privacy; archaeology; rights; operational currentness.
- Status: `CONFIRMED checked / NEEDS_VERIFICATION for admission`.

### Sumner County Comprehensive Plan
- URL: https://co.sumner.ks.us/departments/planning___zoning_environmental_health/comprehensive_plan.php
- Role: county planning-document index.
- Verified: table of contents, Chapters 1–9, figures and tables.
- Limits: linked-document rights; publication does not prove adoption or implementation.
- Status: `CONFIRMED checked / candidate`.

### Farming in Sumner
- URL: https://co.sumner.ks.us/about_sumner_county/county_history/farming_in_sumner.php
- Role: local historical interpretation.
- Verified: county farming narrative and reproduced 1877 letter discussing crops, gypsum, education and pre-rail transport.
- Limits: historical only; copyright/public-domain review; no current claim.
- Status: `CONFIRMED checked / contextual candidate`.

### Railroad History
- URL: https://co.sumner.ks.us/about_sumner_county/county_history/railroad_history/index.php
- Role: local historical interpretation.
- Verified: multiple historic line names, dates, arrivals, changes and successor narratives.
- Limits: no current ownership, operations, cargo, access, crossing or vulnerability conclusion.
- Status: `CONFIRMED checked / historical candidate`.

### City of Wellington
- URL: https://www.cityofwellington.net/
- Role: municipal administrative and operational authority.
- Verified: airport, electric, water, wastewater, streets, GIS, planning, fire/EMS, police, lake recreation, storm-shelter and current-notice surfaces.
- Limits: rapid currentness; infrastructure/security; asset-level rights.
- Status: `CONFIRMED checked / redirect-first candidate`.

### Census QuickFacts
- URL: https://www.census.gov/quickfacts/fact/table/sumnercountykansas/PST045225
- Role: federal statistical authority.
- Verified: 2025 estimate 22,312; 2020 count 22,382; land area 1,181.67 square miles; FIPS 20191.
- Limits: mixed vintages, sampling/suppression, no person inference.
- Status: `CONFIRMED checked / candidate`.

### USDA NASS 2022 County Profile
- URL: https://www.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/County_Profiles/Kansas/cp20191.pdf
- Role: federal agricultural statistical authority.
- Verified: 1,013 farms; 750,650 acres; $181.886 million sold; 92/8 crop/livestock split; 24,047 irrigated acres; major crop acreages; `(D)` flag.
- Limits: 2022 aggregate; no operation inference; preserve suppression.
- Status: `CONFIRMED checked / candidate`.

### NWS Wichita
- URL: https://www.weather.gov/ict/
- Role: current operational weather authority.
- Verified: hazards, radar, forecasts, rivers/lakes, fire weather, climate and reporting.
- Limits: rapidly expiring products; redirect instead of durable cache.
- Status: `CONFIRMED checked / redirect-only first slice`.

## Candidate sources for later verification

KDOT county and railroad maps; FRA and rail operators; FAA airport data; KSHS/KHRI; NPS; Nation-authoritative sources; USGS hydrography/water data; FEMA NFHL/NRI; KGS lowlands/geology; NRCS SSURGO; KDHE; parcel/tax/appraiser systems; city utility documents; historic maps/aerials; Kansas Turnpike Authority.

## Source-admission checklist

- [ ] Publisher, canonical URL, stable ID and source role verified.
- [ ] Historical/current/operational status assigned.
- [ ] Publication/event/adoption/effective/retrieval/expiry times captured.
- [ ] Rights, attribution and derivative-display permission reviewed.
- [ ] Geometry authority, CRS, scale, vintage and confidence recorded.
- [ ] Access implications reviewed.
- [ ] Privacy, property, archaeology, culture, infrastructure and emergency sensitivity reviewed.
- [ ] Suppression/small-cell risk reviewed.
- [ ] Checksum and acquisition receipt recorded.
- [ ] Candidate enters WORK/QUARANTINE.
- [ ] Reviewer decision recorded.
- [ ] Correction/supersession source identified.
- [ ] Public transform receipt and rollback closure complete.

---

# 16. Open verification questions

1. Does a Sumner plan exist in a private/deleted/local/prior-chat artifact?
2. Which Focus Mode path is canonical?
3. Which shared contracts/schemas/policies already exist?
4. Which sources are authoritative for Chisholm Trail geometry and cultural interpretation?
5. What uncertainty/generalization is required for the trail?
6. Which current roads or public access points are authoritative?
7. Which rail lines are active and what fields are public-safe?
8. How should abandoned grades be represented without encouraging trespass?
9. What is the comprehensive plan's date, adoption, amendment and implementation status?
10. May linked plan chapters and county-history content be transformed?
11. May parcel/tax/appraiser data be used in aggregate, and at what threshold?
12. Which airport and utility fields are public-safe?
13. Which shelter/fire/EMS/road/GIS details must be redirect-only?
14. Which USGS/FEMA/KGS/NRCS/KDHE sources are fit?
15. How are private-well, drainage, flood and water-right inferences prevented?
16. How are NASS suppression flags preserved?
17. Which Nations should review cultural narratives?
18. Which archaeology/burial/sacred locations must always be withheld?
19. How do corrections propagate across cards, API, tiles, search and AI?
20. Which rollback object/path, reviewers and gates A–G are canonical?

---

# 17. Recommended first milestone

## Milestone name

**Sumner County Historic-Corridor Access and Infrastructure Boundary Proof**

## Milestone statement

Create a no-network fixture demonstration that answers agriculture, railroad-history, population and plan-index questions; presents one generalized Chisholm Trail card with `access_status=not_established`; abstains from current rail/road/airport/utility/hazard and plan-implementation questions; denies owner-profile, access, vulnerability, private-water, exact-archaeology and individual-farm requests; errors on integrity failure; and proves correction/rollback closure without publication.

## Deliverables

Collision/path memo; seven draft lane docs; source ledger; historic/current corridor contract; access-status vocabulary; planning-status vocabulary; boundary policy; shared-object reuse map; all four outcome fixture families; highest-risk invalid pack; policy and citation fixtures; mock Evidence Drawer/timeline; authority redirects; dry-run ReleaseManifest; CorrectionNotice; RollbackPlan; validation report.

## Definition of done

- [ ] Collision and path rechecked.
- [ ] No live connector or admission claim.
- [ ] Agriculture answer preserves 2022 and suppression.
- [ ] Railroad answer explicitly historical.
- [ ] Trail geometry generalized with no access implication.
- [ ] Plan index does not claim implementation.
- [ ] Current operations/hazards abstain and redirect.
- [ ] Owner, access, vulnerability, archaeology, private-water and farm requests fail closed.
- [ ] Integrity failure returns `ERROR`.
- [ ] Boundary visible throughout UI.
- [ ] Dry-run release includes correction and rollback.
- [ ] Nothing is published.

## Go/no-go

| Gate | Go | No-go |
|---|---|---|
| Collision | No authoritative collision | Existing plan |
| Placement | One approved lane | Parallel authority |
| Evidence | All answer refs resolve | Missing evidence |
| Corridor/access | States explicit | Historic route shown public/current |
| Privacy/security | Profiles and exact assets denied | Reidentification/vulnerability |
| Planning | Statuses separate | Status collapse |
| Rights/currentness | Recorded and expiring | Visibility treated as license/stale answer |
| UI | Four outcomes distinct | Non-answer resembles answer |
| Release | Correction/rollback complete | Missing closure |
| Publication | Independent approval | Unresolved high-risk item |

---

# Appendix A — Public-safe narrative skeleton

1. **County frame and time:** geography, communities, Oklahoma boundary, Census vintages.
2. **Agriculture in 2022:** farms, acreage, sales, wheat and other crops, irrigation, suppression.
3. **Chisholm Trail memory:** generalized history, cultural perspectives, uncertainty, no access implication.
4. **Railroads and development:** historic lines, grain movement, settlement, no current-operation inference.
5. **Planning and property records:** plan status, privacy, no title/profile conclusions.
6. **Wellington municipal systems:** authority categories and operational redirects, no vulnerability mapping.
7. **Rivers, geology and hazards:** deferred scientific sources, NWS current redirect, no property/private-water advice.
8. **Inspect, correct and roll back:** Evidence Drawer, source roles, geometry correction, supersession and release history.

Closing: Sumner County Focus Mode is not a public-access map, title service, railroad/airport operations system, infrastructure-security tool, private-water adviser, emergency service, or archaeology locator.

---

# Appendix B — Required negative-path reason-code categories

| Category | Code | Outcome |
|---|---|---|
| Missing/stale evidence | `SU-EVIDENCE-MISSING`, `SU-EVIDENCE-STALE` | `ABSTAIN` |
| Plan/transport status | `SU-PLAN-STATUS-UNCLEAR`, `SU-TRANSPORT-STATUS-UNCLEAR` | `ABSTAIN` |
| Rights/current hazard | `SU-RIGHTS-UNCLEAR`, `SU-LIVE-HAZARD-REDIRECT` | `ABSTAIN` |
| Property/access | `SU-PROPERTY-ACCESS` | `DENY` |
| Owner/farm profile | `SU-OWNER-PROFILE`, `SU-INDIVIDUAL-FARM` | `DENY` |
| Infrastructure/vulnerability | `SU-INFRASTRUCTURE-EXACT`, `SU-VULNERABILITY-ANALYSIS` | `DENY` |
| Archaeology/culture | `SU-ARCHAEOLOGY-EXACT` | `DENY` |
| Private water | `SU-PRIVATE-WATER` | `DENY` |
| Integrity/dependency/release | `SU-INTEGRITY-FAIL`, `SU-SERVICE-UNAVAILABLE`, `SU-RELEASE-CLOSURE-FAIL` | `ERROR` |

`ANSWER` requires evidence closure, citations, policy allow, temporal/spatial fitness, review and release. `DENY` must not echo sensitive identities, routes, coordinates or operational details. `ERROR` never falls back to uncited generation.

---

# Appendix C — References and evidence-use note

## Checked references

1. Sumner County official website — https://co.sumner.ks.us/ — checked 2026-06-09.
2. Sumner County Comprehensive Plan — https://co.sumner.ks.us/departments/planning___zoning_environmental_health/comprehensive_plan.php — checked 2026-06-09.
3. Farming in Sumner — https://co.sumner.ks.us/about_sumner_county/county_history/farming_in_sumner.php — checked 2026-06-09.
4. Railroad History — https://co.sumner.ks.us/about_sumner_county/county_history/railroad_history/index.php — checked 2026-06-09.
5. City of Wellington — https://www.cityofwellington.net/ — checked 2026-06-09.
6. Census QuickFacts — https://www.census.gov/quickfacts/fact/table/sumnercountykansas/PST045225 — checked 2026-06-09.
7. USDA NASS 2022 Sumner County profile — https://www.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/County_Profiles/Kansas/cp20191.pdf — checked 2026-06-09.
8. NWS Wichita — https://www.weather.gov/ict/ — checked 2026-06-09.

## Evidence-use note

This plan is not an EvidenceBundle, source-admission decision, legal determination, title/access/easement advice, current railroad/airport/utility/road/emergency service, infrastructure-vulnerability product, private-well/water-right assessment, individual-farm or owner profile, archaeology locator, release manifest or published product.

No repository modification, implementation, validation, review, promotion, deployment or publication is claimed.

---

**End of Sumner County Focus Mode Build Plan**

[Back to top](#top)
