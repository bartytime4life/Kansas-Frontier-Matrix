<!-- [KFM_META_BLOCK_V2]
doc_id: NEEDS_VERIFICATION
title: Nemaha County Focus Mode Build Plan
type: county-focus-mode-build-plan
version: v0.1-proposed
status: PROPOSED
release_status: NEEDS_VERIFICATION
county_name: Nemaha County
county_slug: nemaha
lane_slug: nemaha-county
created: 2026-06-09
updated: 2026-06-09
owners:
  focus_mode_owner: NEEDS_VERIFICATION
  evidence_steward: NEEDS_VERIFICATION
  agriculture_reviewer: NEEDS_VERIFICATION
  planning_reviewer: NEEDS_VERIFICATION
  infrastructure_security_reviewer: NEEDS_VERIFICATION
  privacy_property_reviewer: NEEDS_VERIFICATION
  cultural_reviewer: NEEDS_VERIFICATION
  rights_reviewer: NEEDS_VERIFICATION
  release_approver: NEEDS_VERIFICATION
defining_public_safe_boundary: >-
  Nemaha County planning, agriculture, wind-energy, parcel/map, road,
  utility-district, and emergency-service sources may support generalized,
  time-bounded public interpretation, but must not become title or access
  advice, living-person or landowner profiles, individual-farm inference,
  project endorsement or opposition, infrastructure-vulnerability analysis,
  emergency-response detail, or current operational guidance.
collision_search:
  supplied_completed_register: CONFIRMED absent
  current_conversation: CONFIRMED Butler and Cheyenne completed; Nemaha not completed
  live_county_index: CONFIRMED listed not-started on 2026-06-09
  exact_title_search: CONFIRMED no result
  filename_search: CONFIRMED no result
  slug_search: CONFIRMED no result
  branch_search: CONFIRMED no result
  pull_request_search: CONFIRMED no result
  issue_search: CONFIRMED no result
  accessible_project_materials: CONFIRMED no county-plan collision found
  exhaustive_private_deleted_prior_chat_absence: NEEDS_VERIFICATION
directory_rules_basis:
  primary_rule: responsibility root outranks topic name
  observed_template_path: docs/focus-mode/counties/<county-slug>-county/build-plan.md
  path_divergence: docs/focus-mode/ and docs/focus-modes/ references coexist
  older_convention: docs/focus-mode/counties/<county>_county/<county>_county_focus_mode_build_plan.md
  path_status: PROPOSED / NEEDS_VERIFICATION
official_sources_checked:
  - Nemaha County official website
  - Nemaha County Wind Farm Projects page
  - Nemaha County County Maps page
  - U.S. Census Bureau QuickFacts
  - USDA NASS 2022 Census of Agriculture county profile
  - National Weather Service Topeka
implementation_claim: none
repository_modification_claim: none
review_or_validation_claim: none
promotion_or_publication_claim: none
truth_labels: [CONFIRMED, PROPOSED, NEEDS_VERIFICATION, UNKNOWN]
finite_outcomes: [ANSWER, ABSTAIN, DENY, ERROR]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Nemaha County Focus Mode — Build Plan

> **A governed northeast-Kansas planning, agriculture, wind-energy, settlement, and public-map proof slice—without turning public records into ownership profiles, access advice, infrastructure exposure, project advocacy, or live operational guidance.**

**Product thesis:** Build a map-first, evidence-visible Nemaha County learning surface that explains county-scale agriculture, settlement, planning, wind-project governance, public service districts, transportation context, and later environmental layers while preserving source roles, privacy, rights, currentness, public safety, correction, and rollback.

![status](https://img.shields.io/badge/status-PROPOSED-yellow)
![county](https://img.shields.io/badge/county-Nemaha%20County-blue)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)
![boundary](https://img.shields.io/badge/boundary-no%20ownership%2Faccess%2Fvulnerability%20inference-orange)
![outcomes](https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-6f42c1)
![release](https://img.shields.io/badge/release-NEEDS%20VERIFICATION-lightgrey)
![repo](https://img.shields.io/badge/repo%20modified-no-lightgrey)

> [!IMPORTANT]
> **Defining public-safe boundary.** Nemaha County planning, agriculture, wind-energy, parcel/map, road, utility-district, and emergency-service sources may support generalized, time-bounded public interpretation. They must not become title or access advice, living-person or landowner profiles, individual-farm inference, project endorsement or opposition, turbine/transmission/haul-route vulnerability analysis, emergency-response detail, or current operational guidance.

## Status and identity

| Field | Value | Truth posture |
|---|---|---|
| County | Nemaha County, Kansas | `CONFIRMED` |
| County FIPS | `20131` | `CONFIRMED` from Census QuickFacts |
| County slug | `nemaha` | `PROPOSED` |
| Lane slug | `nemaha-county` | `PROPOSED` |
| Deliverable | `nemaha_county_focus_mode_build_plan.md` | `CONFIRMED` |
| Created / updated | 2026-06-09 | `CONFIRMED` |
| Planning status | Build plan only | `CONFIRMED` |
| Implementation | Not claimed | `UNKNOWN` |
| Source admission | Not performed | `CONFIRMED` |
| Validation / review | Not performed | `CONFIRMED` |
| Release / publication | Not performed | `CONFIRMED` |
| Canonical repo path | Unresolved singular/plural convention | `NEEDS_VERIFICATION` |
| Exhaustive collision absence | Not provable across private/deleted artifacts | `NEEDS_VERIFICATION` |

## Quick links

- [Executive build note](#executive-build-note)
- [Evidence boundary](#evidence-boundary)
- [1. Operating posture](#1-operating-posture)
- [2. Why this county](#2-why-this-county)
- [3. Product thesis](#3-product-thesis)
- [4. Scope boundary](#4-scope-boundary)
- [5. First demo layers](#5-first-demo-layers)
- [6. User journeys](#6-user-journeys)
- [7. UI surfaces](#7-ui-surfaces)
- [8. Governed object model](#8-governed-object-model)
- [9. Proposed repository shape](#9-proposed-repository-shape)
- [10. Build phases](#10-build-phases)
- [11. First PR sequence](#11-first-pr-sequence)
- [12. Acceptance checklist](#12-acceptance-checklist)
- [13. Fixture plan](#13-fixture-plan)
- [14. Risk register](#14-risk-register)
- [15. Source seed list](#15-source-seed-list)
- [16. Open verification questions](#16-open-verification-questions)
- [17. Recommended first milestone](#17-recommended-first-milestone)
- [Appendices](#appendix-a--public-safe-narrative-skeleton)

## Executive build note

Nemaha County is a strong next KFM proof slice because its official public surfaces expose several source families that are useful but easy to misuse:

1. The county publishes planning, budget, resolution, commission, and 2023 comprehensive-plan materials.
2. Its Wind Farm Projects page indexes Soldier Creek and Irish Creek documents, including agreements, project/site maps, haul-route and transmission-line material, complaint-resolution, decommissioning, contribution, development, road-use, and engineering documents.
3. Its County Maps page lists 911 roads, electric districts, water districts, EMS districts, fire districts, school districts, and commissioner districts.
4. USDA NASS reports a large, high-value 2022 agricultural economy: 834 farms, 410,751 acres in farms, $447.989 million in products sold, 42% crop sales and 58% livestock/poultry/product sales, with only 2,312 irrigated acres.
5. Census QuickFacts reports a 2025 population estimate of 10,054, a 2020 count of 10,273, and 717.43 square miles of land—an appropriate setting for testing small-cell and reidentification safeguards.
6. County emergency, road, health, and service pages are valuable authority redirects but not safe sources for tactical or cached operational conclusions.

The first implementation slice should be fixture-only. It should prove that KFM can explain public planning and wind-energy governance neutrally, preserve agricultural suppression, generalize public districts, refuse privacy-invasive joins, and show correction and rollback closure.

### Collision result

| Check | Result | Status |
|---|---|---|
| Supplied completed register | Nemaha absent | `CONFIRMED` |
| Current conversation | Butler and Cheyenne completed; Nemaha absent | `CONFIRMED` |
| Live county index | Nemaha listed `not-started` | `CONFIRMED` |
| Exact title search | No match | `CONFIRMED` for search performed |
| Filename search | No match | `CONFIRMED` |
| Slug search | No match | `CONFIRMED` |
| Branch search | No match | `CONFIRMED` |
| PR / issue search | No match | `CONFIRMED` |
| Accessible project materials | No Nemaha plan found | `CONFIRMED` |
| Private/deleted/local/prior-chat artifacts | Not exhaustive | `NEEDS_VERIFICATION` |

### Directory Rules basis

Human planning belongs under `docs/`; object meaning under `contracts/`; machine shape under `schemas/`; policy decisions under `policy/`; samples under `fixtures/`; validators under `tools/`; deployable UI/API under `apps/`; lifecycle data under `data/`; release decisions under `release/`.

The inspected county template uses:

`docs/focus-mode/counties/<county-slug>-county/build-plan.md`

Other repository material references `docs/focus-modes/`, and older lineage used an underscored verbose filename. The divergence must be resolved through current repository authority or an ADR. All proposed paths remain `PROPOSED / NEEDS_VERIFICATION`.

## Evidence boundary

| Label | Supported use |
|---|---|
| `CONFIRMED` | Collision searches performed; official sources in §15 checked; Census and NASS facts cited; artifact generated. |
| `PROPOSED` | Scope, boundary, layers, objects, paths, policies, fixtures, tests, UI, milestones, release and rollback design. |
| `NEEDS_VERIFICATION` | Exhaustive collision absence, final path, rights, geometry authority, source currentness, security classification, reviewers, shared-object reuse, release approval. |
| `UNKNOWN` | Current implementation, CI/test state, admitted sources, runtime routes, policy enforcement, EvidenceBundles, releases, corrections, rollbacks. |

---

# 1. Operating posture

## 1.1 Governing rules

1. `EvidenceBundle` outranks prose, maps, dashboards, snippets, summaries, and AI.
2. Public UI reads governed APIs and released artifacts only.
3. Public UI must not read `RAW`, `WORK`, `QUARANTINE`, parcel/tax systems, restricted project documents, or direct model output.
4. Preserve `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`.
5. Promotion is a governed decision, not a file move.
6. A planning proposal is not adoption; adoption is not implementation.
7. An agreement is not a current project-status feed.
8. A site or route map is not title, ownership, access, or security clearance.
9. Public map availability does not authorize unrestricted recombination.
10. NASS county statistics remain aggregates; suppressed values remain suppressed.
11. Parcel, tax, appraisal, meeting, project, and map data must not be joined into living-person or landowner profiles.
12. Emergency, electric, water, transmission, haul-route, fire, EMS, and 911 detail is security-reviewed and generalized or withheld.
13. Exact archaeology, burials, sacred places, rare species, nests, roosts, and den sites fail closed.
14. Current hazard and operational questions redirect to official authorities.
15. Every result is `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.

## 1.2 Truth and finite-outcome key

| Label/outcome | Meaning |
|---|---|
| `CONFIRMED` | Verified this run. |
| `PROPOSED` | Recommended but not implemented. |
| `NEEDS_VERIFICATION` | Checkable before use. |
| `UNKNOWN` | Unsupported or unresolved. |
| `ANSWER` | Released evidence supports a bounded cited answer. |
| `ABSTAIN` | Evidence/status/rights/currentness/precision is insufficient. |
| `DENY` | Privacy, security, sensitivity, or prohibited transformation blocks the request. |
| `ERROR` | Contract, evidence, citation, manifest, policy, integrity, or service failure. |

## 1.3 Trust membrane

```mermaid
flowchart LR
    S[Official source] --> I[SourceIntakeRecord]
    I --> R[RAW]
    R --> G{Identity, role, rights,
time, sensitivity, integrity}
    G -->|unclear or unsafe| Q[WORK / QUARANTINE]
    G -->|admissible| P[PROCESSED]
    P --> E[EvidenceRef → EvidenceBundle]
    E --> C[CATALOG / TRIPLET]
    C --> V{Policy + citation + review
+ release closure}
    V -->|fail| H[HOLD / ABSTAIN / DENY]
    V -->|pass| M[ReleaseManifest]
    M --> A[Governed API / released tiles]
    A --> U[Public Focus Mode]
    U --> O[ANSWER / ABSTAIN / DENY / ERROR]
```

## 1.4 County guardrails

| Topic | Guardrail |
|---|---|
| Wind projects | Neutral, dated document-role explanation only; no advocacy, legal conclusion, current-status inference, owner profile, or vulnerable geometry. |
| Project/site/haul/transmission maps | Generalize or withhold; no dependency or disruption analysis. |
| Parcel/tax/appraisal | Reviewed aggregates only, if admitted; never title, ownership, access, fraud, debt, or living-person truth. |
| 911, EMS, fire, electric, water | Service-area context only after security review; no capacity, weakness, or response-time inference. |
| Agriculture | County aggregates only; preserve `(D)`, `(Z)`, and other suppression/quality flags. |
| Planning documents | Label draft, proposal, adoption, amendment, implementation, supersession, and unknown separately. |
| Meetings/public comments | Participation evidence, not authoritative factual findings; do not profile participants. |
| Hydrology/soil | No private-well, drainage-liability, water-right, farm-prescription, or property-risk conclusion. |
| History/culture | Reviewed public interpretation only; precise sensitive locations withheld. |
| Weather/hazards | Historic interpretation may be released; current guidance redirects to NWS/local authorities. |

## 1.5 Candidate reason codes

| Code | Outcome | Meaning |
|---|---|---|
| `NM-EVIDENCE-MISSING` | `ABSTAIN` | Required evidence unresolved. |
| `NM-EVIDENCE-STALE` | `ABSTAIN` | Evidence outside currentness window. |
| `NM-PROPOSAL-NOT-ADOPTION` | `ABSTAIN` | Proposal does not prove adoption. |
| `NM-WIND-PROJECT-STATUS` | `ABSTAIN` | Current project status unverified. |
| `NM-RIGHTS-UNCLEAR` | `ABSTAIN` | Reuse/derivative rights unresolved. |
| `NM-PROPERTY-LEGAL` | `ABSTAIN` | Title/access/tax/legal question requires authority. |
| `NM-OWNER-PROFILE` | `DENY` | Landowner/living-person profiling. |
| `NM-INDIVIDUAL-FARM` | `DENY` | Individual agricultural operation inference. |
| `NM-INFRASTRUCTURE-EXACT` | `DENY` | Exact or vulnerability-relevant infrastructure detail. |
| `NM-TACTICAL-RESPONSE` | `DENY` | Emergency capability/routing/gap analysis. |
| `NM-ARCHAEOLOGY-EXACT` | `DENY` | Exact cultural-sensitive location. |
| `NM-SENSITIVE-ECOLOGY` | `DENY` | Exact sensitive ecology location. |
| `NM-LIVE-HAZARD-REDIRECT` | `ABSTAIN` | Current authority must answer. |
| `NM-INTEGRITY-FAIL` | `ERROR` | Digest/schema/manifest/citation failure. |
| `NM-SERVICE-UNAVAILABLE` | `ERROR` | Governed dependency unavailable. |

---

# 2. Why this county

## 2.1 Selection screen

| Candidate | Register/index result | Decision |
|---|---|---|
| Butler | Completed in current conversation despite stale index | Reject |
| Cheyenne | Completed in current conversation despite stale index | Reject |
| Graham | Live index marks `draft` | Reject |
| Nemaha | Not in register; live index `not-started`; no collision found | **Select** |
| Sumner | Unused candidate | Hold |
| Russell | Unused candidate | Hold |

## 2.2 Distinct proof-slice value

Nemaha County tests a source-governance problem not central to the preceding plans: **public planning and infrastructure-adjacent documents that are useful but unsafe to flatten into a single public truth layer.**

KFM must represent term sheets, development agreements, decommissioning agreements, complaint-resolution agreements, road-use agreements, site maps, route maps, planning materials, public maps, NASS statistics, Census estimates, and official notices as distinct evidence roles with distinct dates and limitations.

## 2.3 Public benefit

The public can:

- understand what types of project and planning documents the county publishes;
- inspect a neutral timeline without assuming proposals were adopted or projects remain current;
- explore 2022 agriculture without identifying operations;
- compare 2020 Census and 2025 estimate vintages;
- view generalized public-district context safely;
- inspect source roles, rights, currentness, correction, and release history;
- reach the correct official authority for current or legal questions.

## 2.4 Official anchors

| Anchor | Evidence checked |
|---|---|
| County government and planning | Official county website |
| Soldier Creek / Irish Creek document families | County Wind Farm Projects page |
| Public district map categories | County Maps page |
| Population/economy/geography | Census QuickFacts |
| Agriculture | USDA NASS 2022 profile |
| Current weather authority | NWS Topeka |

---

# 3. Product thesis

## 3.1 Thesis

**Nemaha County Focus Mode will explain planning, agriculture, wind-energy governance, settlements, public districts, and later environmental context through released evidence while refusing ownership profiling, access conclusions, project advocacy, infrastructure exposure, individual-farm inference, and live operational guidance.**

## 3.2 First-product promises

- Evidence and source roles visible.
- Neutral project/process language.
- Proposal/adoption/implementation separated.
- County statistics remain aggregates.
- Public district geometry is generalized or withheld.
- Rights and currentness visible.
- Missing support produces finite non-answer outcomes.
- Corrections and rollback remain inspectable.

## 3.3 Non-promises

No title, ownership, tax, access, zoning, contract, easement, project-benefit, property-value, owner-profile, individual-farm, infrastructure-vulnerability, emergency-capability, current-warning, or precise sensitive-site conclusion.

---

# 4. Scope boundary

| Scope | Examples | Posture |
|---|---|---|
| First public-safe slice | County frame, communities, Census aggregates, 2022 NASS card, planning timeline, wind document-role index, official redirects | `PROPOSED` |
| Deferred | Hydrology, soils, geology, habitat, KDOT, FEMA, detailed district geometry, current project status | `DEFER` |
| Denied by default | Owner profiles, exact infrastructure, tactical emergency analysis, individual farms, sensitive cultural/ecological sites | `DENY` |
| Excluded | Restricted, credentialed, rights-unclear, tactical, unsafe, privacy-invasive material | `EXCLUDE` |

### County-specific boundaries

- **Privacy/property:** Public records are not title or access truth and cannot be joined into profiles.
- **Infrastructure:** Exact transmission, haul, electric, water, 911, fire, and EMS detail requires withholding/generalization.
- **Agriculture:** County aggregates only; no operation identification or suppressed-value reconstruction.
- **Planning:** Draft/proposal/adopted/implemented/superseded remain distinct.
- **Neutrality:** Generated language may not advocate for or against a project.
- **Culture/ecology:** Precise sensitive locations withheld.
- **Health/safety:** Current warnings and operational questions redirect to authorities.
- **Rights:** Downloadable does not mean redistributable.

---

# 5. First demo layers

| Priority | Layer/card | Source seed | Evidence/policy gate | Status |
|---|---|---|---|---|
| 1 | County frame and communities | Census + county | Geometry vintage; cross-county Sabetha handling | `PROPOSED` |
| 2 | Population-vintage card | Census | Survey/estimate period visible | `PROPOSED` |
| 3 | 2022 agriculture card | NASS | Suppression preserved; aggregate only | `PROPOSED` |
| 4 | Wind-project document-role index | County | Per-document ID/date/role/rights; no tactical geometry | `PROPOSED` |
| 5 | Planning timeline | County | Proposal/adoption/implementation evidence | `PROPOSED` |
| 6 | Generalized public-district categories | County Maps | Date/rights/security review | `DEFER` |
| 7 | County authority redirect | County | Current page/time | `PROPOSED` |
| 8 | Weather authority redirect | NWS | Redirect only for current products | `PROPOSED` |
| 9 | Roads/hydrology/soils/geology/habitat/history | Official candidates | Source-specific admission | `DEFER` |
| 10 | Parcel/tax/exact infrastructure/tactical assets | Linked systems | Fail closed | `DENY` |

```mermaid
flowchart TB
    B[Released base + county frame]
    C[Communities / Census]
    A[2022 agriculture]
    P[Planning timeline]
    W[Wind document index]
    D[Generalized public districts]
    R[Authority redirects]
    E[Evidence Drawer]
    G[Boundary panel]

    B --> C
    B --> A
    B --> P
    B --> W
    B --> D
    B --> R
    C --> E
    A --> E
    P --> E
    W --> E
    D --> E
    E --> G
```

### Layer-card truth contract

Every card/layer carries stable ID, knowledge character, source role, document type/status, EvidenceRefs, spatial/temporal basis, rights, sensitivity, transform receipt, PolicyDecision, CitationValidationReport, ReviewRecord, ReleaseManifest, CorrectionNotice, RollbackPlan, and county boundary notice.

---

# 6. User journeys

## Public learning

1. **Agriculture:** “What did USDA report in 2022?” → `ANSWER`, with 834 farms, 410,751 acres, $447.989 million, 42/58 sales split, and aggregate limitations.
2. **Wind documents:** “What document types are published for Soldier Creek?” → `ANSWER`, listing categories without legal/status conclusions.
3. **Planning:** “Does the comprehensive plan prove this proposal was implemented?” → `ABSTAIN` unless adoption and implementation evidence resolve.
4. **Population:** “What is the population?” → `ANSWER` with 2025 estimate and 2020 Census count clearly distinguished.
5. **District context:** “Which generalized service district covers this area?” → `ANSWER` only from an admitted safe layer.

## Trust demonstrations

- Evidence Drawer shows each project document separately.
- Timeline distinguishes proposal, adoption, agreement, operation, amendment, retrieval, release, and correction.
- Privacy policy blocks parcel + project + tax + meeting joins.
- Correction panel links superseded documents and releases.

## Denied/abstained requests

| Request | Outcome | Reason |
|---|---|---|
| List project-area landowners | `DENY` | `NM-OWNER-PROFILE` |
| Show exact transmission/haul routes | `DENY` | `NM-INFRASTRUCTURE-EXACT` |
| Identify the farm behind livestock totals | `DENY` | `NM-INDIVIDUAL-FARM` |
| Rank EMS districts by weakness | `DENY` | `NM-TACTICAL-RESPONSE` |
| Decide whether an agreement grants access | `ABSTAIN` | `NM-PROPERTY-LEGAL` |
| Say whether project is “good” or “bad” | `ABSTAIN` | Unsupported normative synthesis |
| Treat a plan as current implementation | `ABSTAIN` | `NM-PROPOSAL-NOT-ADOPTION` |
| Give current warning | `ABSTAIN` | `NM-LIVE-HAZARD-REDIRECT` |

---

# 7. UI surfaces

## Required surfaces

- Header with release, freshness, correction, and boundary badges.
- County map canvas using released sources only.
- Layer drawer with source role, status, time, rights, sensitivity, and release state.
- Evidence Drawer with claim, bundle, publisher, document type, dates, geometry, rights, transform, policy, citation, review, correction, and rollback.
- Distinct answer, denial, abstention, and error panels.
- Timeline/time-basis panel.
- County boundary panel.
- Official-authority redirect panel.
- Correction/release panel.
- Accessible legend.

## Legend vocabulary

| Term | Meaning |
|---|---|
| Proposal | Suggested action, not adoption |
| Adopted policy | Officially adopted within effective scope |
| Agreement | Legal/administrative instrument, not live status |
| Project map | Dated representation, not title/access proof |
| Statistical aggregate | County summary, not an individual operation |
| Public district | Administrative geography, not capacity/vulnerability truth |
| Generalized geometry | Precision reduced by policy |
| Sensitive withheld | Detail not released |
| Operational redirect | Link to current authority |
| Generated summary | Downstream text subordinate to evidence |

```mermaid
sequenceDiagram
    participant U as User
    participant UI as Focus UI
    participant API as Governed API
    participant P as Policy
    participant E as Evidence Resolver
    participant R as Released Artifacts

    U->>UI: Ask / select
    UI->>API: MapContextEnvelope + request
    API->>P: Precheck precision/privacy/security
    alt prohibited
        P-->>API: DENY
        API-->>UI: DENY + reason
    else potentially safe
        P-->>API: Continue
        API->>E: Resolve EvidenceRefs
        E->>R: Fetch released bundles
        R-->>E: Evidence + manifests
        E-->>API: Resolution
        API->>P: Postcheck rights/time/status
        alt sufficient
            P-->>API: ANSWER
            API-->>UI: Cited ANSWER
        else insufficient
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
| `NemahaCountyFrame` | FIPS, geometry, CRS, vintage, cross-county relations |
| `PlanningDocumentStatus` | draft/proposed/adopted/amended/superseded/unknown |
| `WindProjectDocumentCard` | One document’s role, date, rights, sensitivity, non-claims |
| `WindProjectDocumentIndex` | Neutral collection of document cards |
| `InfrastructurePrecisionDecision` | exact/generalized/withheld |
| `AgricultureCountySnapshot` | NASS aggregate and suppression state |
| `PublicDistrictLayerCard` | Safe service-area context |
| `PropertyAggregationDecision` | Whether parcel/tax data may be aggregated |
| `CrossCountyMunicipalityRelation` | Sabetha cross-county context |
| `SmallCellSuppressionDecision` | Reidentification control |

## Anti-collapse rules

Proposal ≠ adoption; adoption ≠ implementation; agreement ≠ current status; map ≠ title/access; public comment ≠ authoritative finding; NASS aggregate ≠ individual farm; county web page ≠ blanket license; generated summary ≠ source authority.

## Minimal `ANSWER`

```json
{
  "schema_version": "1.0",
  "outcome": "ANSWER",
  "question": "What did the 2022 Census of Agriculture report?",
  "answer": "USDA NASS reported 834 farms, 410,751 acres in farms, and $447.989 million in products sold. These are county aggregates for 2022 and do not identify an operation.",
  "county_fips": "20131",
  "knowledge_character": "statistical_aggregate",
  "evidence_refs": ["kfm:evidence-ref:nass:2022:nemaha-ks"],
  "citation_validation_report_ref": "kfm:citation-report:sha256:EXAMPLE",
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
  "question": "Does the comprehensive plan prove the project is approved and operating?",
  "reason_codes": ["NM-PROPOSAL-NOT-ADOPTION", "NM-WIND-PROJECT-STATUS"],
  "explanation": "The checked planning and document-index pages do not establish complete current approval and operating status.",
  "authority_redirect": "Nemaha County official records",
  "policy_decision_ref": "kfm:policy-decision:nemaha:status:sha256:EXAMPLE"
}
```

## `DENY`

```json
{
  "schema_version": "1.0",
  "outcome": "DENY",
  "question": "List landowners along exact transmission and haul routes.",
  "reason_codes": ["NM-OWNER-PROFILE", "NM-INFRASTRUCTURE-EXACT"],
  "explanation": "KFM does not combine property records with exact infrastructure routes to profile people or expose vulnerability-relevant detail.",
  "safe_alternative": "Use a generalized reviewed document index without identities or exact routes."
}
```

## Identity and `spec_hash`

Candidate identity inputs include FIPS + geometry vintage, publisher + document + revision + digest, project ID + document type + date, census year + county FIPS, authority + district type + effective date + geometry digest, and sorted release dependency digests.

`spec_hash` should cover schema version, source revisions, document-status vocabulary, generalization parameters, suppression thresholds, source-role rules, time windows, policy profile, evidence resolution, citation validation, and UI composition. Exact canonicalization remains `NEEDS_VERIFICATION`; JCS + SHA-256 is `PROPOSED`.

---

# 9. Proposed repository shape

## Candidate paths

| Responsibility | Candidate path | Status |
|---|---|---|
| Build plan | `docs/focus-mode/counties/nemaha-county/build-plan.md` | `PROPOSED / NEEDS_VERIFICATION` |
| Requested artifact | `nemaha_county_focus_mode_build_plan.md` | `CONFIRMED` deliverable only |
| Lane docs | `docs/focus-mode/counties/nemaha-county/` | `PROPOSED / NEEDS_VERIFICATION` |
| Semantic contract | `contracts/focus_mode/nemaha_county_focus_mode.md` | `PROPOSED / NEEDS_VERIFICATION` |
| Shared schema | `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json` | `PROPOSED reuse / NEEDS_VERIFICATION` |
| Extension schema | `schemas/contracts/v1/focus_mode/nemaha_county_extension.schema.json` | Only if justified |
| Source descriptors | `data/catalog/sources/nemaha-county/source_descriptors.yaml` | `PROPOSED / NEEDS_VERIFICATION` |
| Fixtures | `fixtures/focus_modes/nemaha-county/{valid,invalid}/` | `PROPOSED / NEEDS_VERIFICATION` |
| Policy | `policy/focus_modes/nemaha-county/` | `PROPOSED / NEEDS_VERIFICATION` |
| UI | `apps/explorer-web/src/focus-modes/nemaha-county/` | `PROPOSED / NEEDS_VERIFICATION` |
| Mock API | `apps/governed-api/fixtures/focus-modes/nemaha-county/` | `PROPOSED / NEEDS_VERIFICATION` |
| Release candidate | `release/candidates/focus-modes/nemaha-county/` | `PROPOSED / NEEDS_VERIFICATION` |
| Published payload | `data/published/api_payloads/focus-modes/nemaha-county.json` | Later only |
| Correction / rollback | Existing responsibility roots, exact paths TBD | `PROPOSED / NEEDS_VERIFICATION` |

```text
docs/focus-mode/counties/nemaha-county/
  README.md
  build-plan.md
  layer-registry.md
  evidence-model.md
  acceptance-checklist.md
  source-seed-list.md
  public-safety-notes.md

contracts/focus_mode/
schemas/contracts/v1/focus_mode/
fixtures/focus_modes/nemaha-county/{valid,invalid}/
policy/focus_modes/nemaha-county/
apps/explorer-web/src/focus-modes/nemaha-county/
apps/governed-api/fixtures/focus-modes/nemaha-county/
data/catalog/sources/nemaha-county/
release/candidates/focus-modes/nemaha-county/
```

### Placement prohibitions

No root-level county/wind-project folder; no parallel schema/contract/policy/source/proof/receipt/release home; no parcel/tax copies in docs/UI; no direct project maps in public UI; no file move treated as promotion.

No proposed county-specific file is claimed to exist.

---

# 10. Build phases

| Phase | Entry | Output | Exit | Rollback |
|---|---|---|---|---|
| 0 Collision/path | Repo access | Memo/path decision | No collision/parallel lane | Stop |
| 1 Documentation | Phase 0 clear | Seven draft docs | Sections/labels/owners | Revert docs |
| 2 Source ledger | Docs drafted | Candidate descriptors/boundary | No assumed admission | Remove candidates |
| 3 Shared-object reuse | Repo objects inspected | Reuse map/extension proposal | No duplicate authority | Revert extension |
| 4 Fixtures | Shapes stable | Valid/invalid packs | Schema + negative tests | Remove fixtures |
| 5 Policy/validators | Invalid pack | Rules/checks | High-risk fail closed | Revert policy |
| 6 Mock API/UI | Tests pass | Static envelopes/UI | No direct nonreleased access | Feature flag off |
| 7 Dry-run release | Mock passes | Manifest/receipts/correction/rollback | Closure without alias | Delete candidate |
| 8 Optional release | Independent approval | Versioned public-safe payload | Gates A–G | Repoint prior release |

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
> Live parcel/tax/map connectors, live project-status integration, emergency feeds, automatic document scraping, and public release are not first-PR work.

---

# 12. Acceptance checklist

## Governance/evidence

- [ ] Every answer claim resolves to EvidenceBundle.
- [ ] Generated language is downstream.
- [ ] Source role/document type/status visible.
- [ ] Rights, time, sensitivity, review recorded.
- [ ] Promotion/correction/rollback auditable.

## Source-role separation

- [ ] Proposal ≠ adoption.
- [ ] Adoption ≠ implementation.
- [ ] Agreement ≠ current status.
- [ ] Map ≠ title/access.
- [ ] Public comment ≠ authoritative finding.
- [ ] NASS aggregate ≠ individual farm.
- [ ] Website visibility ≠ reuse license.

## Public boundary

- [ ] No owner/living-person profile.
- [ ] No title/access/tax/legal conclusion.
- [ ] No individual-farm inference.
- [ ] No exact infrastructure/tactical detail.
- [ ] No exact cultural/ecological sensitive location.
- [ ] Boundary visible in all outcome panels.

## Currentness

- [ ] Document revisions/effective periods captured.
- [ ] Current project status verified or abstained.
- [ ] 2022 agriculture labeled 2022.
- [ ] Current NWS products expire.
- [ ] Superseded documents linked.

## Product/UI

- [ ] Correct county frame and cross-county municipality relation.
- [ ] Layer cards show role/status/time/rights.
- [ ] Evidence Drawer resolves.
- [ ] Four outcomes distinct/accessibile.
- [ ] Geometry generalization visible.
- [ ] Official redirects present.

## Placement/validation/release

- [ ] Directory Rules and path divergence resolved.
- [ ] No parallel authority root.
- [ ] Schemas/reason codes validate.
- [ ] Invalid fixtures fail closed.
- [ ] Citations/digests pass.
- [ ] Public client cannot access nonreleased stores.
- [ ] ReleaseManifest, review, correction, rollback complete.
- [ ] No in-place overwrite.

---

# 13. Fixture plan

## Valid fixtures

| Fixture | Expected |
|---|---|
| `valid-answer-nass-2022.json` | `ANSWER` |
| `valid-answer-census-vintages.json` | `ANSWER` |
| `valid-answer-wind-document-types.json` | `ANSWER` |
| `valid-answer-planning-status.json` | `ANSWER` |
| `valid-abstain-project-status.json` | `ABSTAIN` |
| `valid-abstain-property-legal.json` | `ABSTAIN` |
| `valid-abstain-live-weather.json` | `ABSTAIN` |
| `valid-deny-owner-profile.json` | `DENY` |
| `valid-deny-infrastructure.json` | `DENY` |
| `valid-deny-individual-farm.json` | `DENY` |
| `valid-error-integrity.json` | `ERROR` |

## Invalid/fail-closed fixtures

| Fixture | Failure |
|---|---|
| `invalid-answer-no-evidence.json` | Validation fail |
| `invalid-proposal-as-adopted.json` | Fail |
| `invalid-adopted-as-built.json` | Fail |
| `invalid-agreement-as-current-status.json` | Fail |
| `invalid-owner-profile.json` | `DENY` |
| `invalid-tax-person-join.json` | `DENY` |
| `invalid-exact-transmission.json` | `DENY` |
| `invalid-haul-route-weakness.json` | `DENY` |
| `invalid-ems-gap-analysis.json` | `DENY` |
| `invalid-nass-operation-inference.json` | `DENY` |
| `invalid-suppressed-value-reconstruction.json` | `DENY` |
| `invalid-live-warning-cache.json` | `ERROR`/`ABSTAIN` |
| `invalid-web-visibility-rights.json` | `ABSTAIN` |
| `invalid-release-no-rollback.json` | Gate fail |
| `invalid-correction-overwrite.json` | Fail |

## Fixture-to-test matrix

Schema, evidence closure, document status, privacy, infrastructure security, agricultural suppression, temporal currentness, rights, release closure, and UI outcome tests are required.

### Highest-risk pack

Landowner/project join; tax/person join; exact transmission/haul routes; road/utility vulnerability; EMS/fire gap analysis; proposal-as-adopted; agreement-as-current; NASS operation inference; suppressed-value reconstruction; release without correction/rollback.

---

# 14. Risk register

| Risk | Likelihood | Impact | Mitigation | Release |
|---|---|---|---|---|
| Project map exposes vulnerable infrastructure | High | High | Generalize/withhold/security review | Block |
| Parcel/project joins profile owners | High | High | Deny joins; no direct connector | Block |
| Proposal presented as adopted | High | High | Status vocabulary/evidence gate | Block |
| Agreement presented as current status | High | High | Currentness/role check | Block |
| Generated advocacy | Medium | High | Neutrality tests | Block |
| Route map used for disruption | Medium | High | Deny vulnerability queries | Block |
| Emergency map becomes capability analysis | Medium | High | Generalized only | Block |
| NASS suppression defeated | Medium | High | Preserve flags/no reconstruction | Block |
| 2022 data described current | High | Medium | Reporting-year labels | Block |
| Sabetha county relation misrepresented | Medium | Medium | CrossCountyMunicipalityRelation | Correct |
| Website treated as license | High | Medium | Per-document rights review | Hold |
| Public comments treated as findings | Medium | Medium | Role labels | Hold |
| Project status changes | High | High | Expiry/current-source/abstain | Hold |
| Cultural/ecological precision exposed | Low/Medium | High | Geoprivacy/review | Block |
| Current warning cached | High | High | Redirect/expiry | Block |
| Correction or rollback untested | Medium | High | Dry-run | Block |
| Path divergence creates parallel authority | High | Medium | ADR/drift resolution | Block |

---

# 15. Source seed list

## Official sources checked

### Nemaha County official website

- URL: https://www.nmcoks.us/
- Role: county administrative authority.
- Verified: departments, meetings, budgets, resolutions, planning, map/parcel/tax links, comprehensive-plan links, wind-project links, services.
- Intended use: authority redirects, planning/document index, county identity.
- Limitations: changing notices; privacy/security; no blanket derivative rights.
- Status: `CONFIRMED checked / NEEDS_VERIFICATION for admission`.

### Nemaha County Wind Farm Projects

- URL: https://www.nmcoks.us/wind-farm-projects
- Role: county administrative document index.
- Verified: Soldier Creek term sheet, site map, haul-route/transmission map, complaint-resolution, decommissioning, contribution, development, road-use documents; Irish Creek road-use and engineering-service documents.
- Intended use: neutral document-role index.
- Limitations: each document needs rights/currentness/legal-role/security review; page does not prove current operating status.
- Status: `CONFIRMED checked / candidate with restrictions`.

### Nemaha County County Maps

- URL: https://www.nmcoks.us/maps
- Role: county map index.
- Verified: categories for 911 roads, electric districts, water districts, commissioners, EMS, fire, school districts.
- Intended use: candidate generalized district context.
- Limitations: dates, geometry authority, rights, infrastructure security.
- Status: `CONFIRMED checked / DEFER`.

### Census QuickFacts

- URL: https://www.census.gov/quickfacts/fact/table/nemahacountykansas/PST045225
- Role: federal statistical authority.
- Verified: 2025 estimate 10,054; 2020 Census 10,273; land area 717.43 square miles; FIPS 20131; mixed-vintage statistics and suppression flags.
- Intended use: aggregate cards.
- Limitations: mixed periods, sampling/suppression, no person/household inference.
- Status: `CONFIRMED checked / candidate`.

### USDA NASS 2022 County Profile

- URL: https://www.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/County_Profiles/Kansas/cp20131.pdf
- Role: federal agricultural statistical authority.
- Verified: 834 farms; 410,751 acres; 493-acre average; $447.989 million market value; 42% crops / 58% livestock; 2,312 irrigated acres; suppression markers.
- Intended use: 2022 aggregate card.
- Limitations: no operation identification or suppressed-value inference; not current conditions.
- Status: `CONFIRMED checked / candidate`.

### National Weather Service Topeka

- URL: https://www.weather.gov/top/
- Role: operational weather authority.
- Intended use: current-authority redirect; later climate/hazard candidate.
- Limitations: rapidly expiring products; no stale cached warning.
- Status: `CONFIRMED checked / redirect-only first slice`.

## Candidate sources for later verification

2023 comprehensive-plan PDF/appendices; individual wind-project PDFs/maps; KDOT maps; USGS hydrography/stream data; NRCS SSURGO; KGS geology/glacial sources; KDHE watershed/drinking water; FEMA NFHL/NRI; KDWP/USFWS; KSHS/KHRI; Seneca and Sabetha city sources; ORKA; county parcel/tax/appraiser systems; project operators/regulators; KCC; FAA public airport data.

## Source-admission checklist

- [ ] Publisher/identifier/role verified.
- [ ] Publication/revision/effective dates captured.
- [ ] Access receipt and checksum recorded.
- [ ] Terms/license/attribution/derivative rights reviewed.
- [ ] Geometry authority/scale/CRS/date recorded.
- [ ] Privacy, small-cell, and infrastructure security reviewed.
- [ ] Operational expiry defined.
- [ ] Source-specific non-claims preserved.
- [ ] Candidate enters WORK/QUARANTINE.
- [ ] Validation/review decision recorded.
- [ ] Correction/supersession source identified.
- [ ] Public transform receipt recorded.
- [ ] Release rollback closure complete.

---

# 16. Open verification questions

1. Does another branch/private fork/local artifact/prior chat contain a Nemaha plan?
2. Which Focus Mode path is canonical: singular or plural?
3. Which shared contracts/schemas/policies already exist?
4. Was the 2023 comprehensive plan adopted; what is its effective status?
5. Which project documents are current, amended, or superseded?
6. Which authority proves current Soldier Creek and Irish Creek status?
7. May linked PDFs/maps be redistributed, excerpted, tiled, or generalized?
8. Which county map geometries are authoritative and current?
9. What minimum generalization applies to transmission, haul routes, electric, water, 911, EMS, and fire?
10. How should Sabetha’s cross-county extent be represented?
11. What joins constitute prohibited owner profiling?
12. May parcel/tax/appraisal data be aggregated; at what threshold?
13. How are names in minutes prevented from becoming profiles?
14. How are NASS suppression flags preserved and reconstruction prevented?
15. Which KGS/NRCS/USGS/KDHE/KDOT/FEMA/KDWP/KSHS sources are fit?
16. Which cultural topics require Nation-authoritative review?
17. Which wildlife/habitat layers require geoprivacy?
18. Which correction and rollback objects/paths are canonical?
19. How do corrections propagate through cards, API, tiles, search, and AI retrieval?
20. Which reviewers and gates A–G are mandatory before release?

---

# 17. Recommended first milestone

## Milestone

**Nemaha County Neutral Planning-and-Infrastructure Boundary Proof**

## Statement

Create a no-network fixture demonstration that answers one agriculture question, one neutral wind-document-role question, and one population-vintage question; abstains from current project status and property/legal questions; denies owner-profile, individual-farm, exact-infrastructure, and tactical-response requests; errors on evidence-integrity failure; and proves correction/rollback closure without publication.

## Deliverables

- Collision/path memo.
- Seven draft lane documents.
- Candidate source ledger.
- Document-status vocabulary.
- County boundary policy.
- Shared-object reuse map.
- Four finite-outcome fixture families.
- Highest-risk invalid pack.
- PolicyDecision and CitationValidationReport fixtures.
- Mock Evidence Drawer and timeline.
- Dry-run ReleaseManifest, CorrectionNotice, and RollbackPlan.
- Validation report.

## Definition of done

- [ ] Collision rechecked immediately before merge.
- [ ] Path divergence resolved or drift recorded.
- [ ] No live connector or source-admission claim.
- [ ] Agriculture answer preserves 2022 scope and suppression.
- [ ] Wind answer lists document roles without legal/status inference.
- [ ] Proposal/adoption/implementation remain distinct.
- [ ] Current project status abstains unless verified.
- [ ] Owner-profile, exact infrastructure, individual-farm, and tactical requests deny.
- [ ] Current warning redirects to NWS.
- [ ] Integrity failure returns `ERROR`.
- [ ] Boundary visible in UI.
- [ ] Dry-run release includes correction and rollback.
- [ ] No public alias, payload, route, tile, deployment, or publication.

## Go/no-go

| Gate | Go | No-go |
|---|---|---|
| Collision | No authoritative collision | Existing plan found |
| Placement | One approved lane | Parallel authority |
| Evidence | All answer refs resolve | Missing evidence |
| Status | Proposal/adoption/implementation explicit | Status collapse |
| Privacy | Profiles denied | Reidentification possible |
| Security | Infrastructure generalized/withheld | Vulnerability exposed |
| Rights | Per-document posture recorded | Visibility treated as license |
| Temporal | Currentness/expiry explicit | Old document treated current |
| UI | Four outcomes distinct | Non-answer rendered as answer |
| Release | Correction/rollback complete | Missing closure |
| Publication | Independent approval | Any unresolved high-risk item |

---

# Appendix A — Public-safe narrative skeleton

1. **County frame and time:** Nemaha County, communities, cross-county Sabetha, 2020 Census versus 2025 estimate.
2. **Agriculture as aggregate:** 2022 NASS totals, crop/livestock split, suppression and privacy.
3. **What a wind-project page establishes:** document categories, dates, roles, and non-claims.
4. **Proposal, plan, agreement, implementation:** status vocabulary and evidence transitions.
5. **Public maps and sensitivity:** district categories, generalization, withholding, and recombination risk.
6. **Property-adjacent records without profiles:** title/access non-claims and denied joins.
7. **Current authority:** county and NWS redirects with expiry.
8. **Inspect, correct, roll back:** Evidence Drawer, correction, supersession, release history.

Closing: Nemaha County Focus Mode is not a title service, legal opinion, owner database, project campaign, infrastructure-security tool, emergency system, or live feed.

---

# Appendix B — Negative-path reason-code categories

| Category | Code | Outcome |
|---|---|---|
| Missing evidence | `NM-EVIDENCE-MISSING` | `ABSTAIN` |
| Stale evidence | `NM-EVIDENCE-STALE` | `ABSTAIN` |
| Proposal/adoption ambiguity | `NM-PROPOSAL-NOT-ADOPTION` | `ABSTAIN` |
| Current project status | `NM-WIND-PROJECT-STATUS` | `ABSTAIN` |
| Rights unclear | `NM-RIGHTS-UNCLEAR` | `ABSTAIN` |
| Property/legal | `NM-PROPERTY-LEGAL` | `ABSTAIN` |
| Live hazard | `NM-LIVE-HAZARD-REDIRECT` | `ABSTAIN` |
| Owner profile | `NM-OWNER-PROFILE` | `DENY` |
| Individual farm | `NM-INDIVIDUAL-FARM` | `DENY` |
| Exact infrastructure | `NM-INFRASTRUCTURE-EXACT` | `DENY` |
| Tactical response | `NM-TACTICAL-RESPONSE` | `DENY` |
| Cultural precision | `NM-ARCHAEOLOGY-EXACT` | `DENY` |
| Ecological precision | `NM-SENSITIVE-ECOLOGY` | `DENY` |
| Integrity | `NM-INTEGRITY-FAIL` | `ERROR` |
| Service | `NM-SERVICE-UNAVAILABLE` | `ERROR` |
| Release closure | `NM-RELEASE-CLOSURE-FAIL` | `ERROR` |

`ANSWER` requires citations, evidence closure, policy allow, temporal fitness, and release state. `DENY` must not echo identities or sensitive geometry. `ERROR` must not fall back to generated speculation.

---

# Appendix C — References and evidence-use note

## Checked references

1. Nemaha County official website — https://www.nmcoks.us/ — checked 2026-06-09.
2. Nemaha County Wind Farm Projects — https://www.nmcoks.us/wind-farm-projects — checked 2026-06-09.
3. Nemaha County County Maps — https://www.nmcoks.us/maps — checked 2026-06-09.
4. U.S. Census Bureau QuickFacts — https://www.census.gov/quickfacts/fact/table/nemahacountykansas/PST045225 — checked 2026-06-09.
5. USDA NASS 2022 County Profile — https://www.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/County_Profiles/Kansas/cp20131.pdf — checked 2026-06-09.
6. National Weather Service Topeka — https://www.weather.gov/top/ — checked 2026-06-09.

## Evidence-use note

This plan is not an EvidenceBundle, source-admission decision, legal interpretation, title/access/tax determination, owner profile, individual-farm analysis, wind-project endorsement/opposition statement, current project-status determination, infrastructure-vulnerability analysis, emergency-response analysis, current hazard advisory, sensitivity determination, release manifest, or published product.

No repository modification, implementation, validation, review, promotion, deployment, or publication is claimed.

---

**End of Nemaha County Focus Mode Build Plan**

[Back to top](#top)
