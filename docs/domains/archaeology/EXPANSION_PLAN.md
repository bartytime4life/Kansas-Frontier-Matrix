<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/archaeology/expansion-plan
title: Archaeology Domain — Expansion Plan
type: standard
version: v0.1
status: draft
owners: TODO — Archaeology lane steward; Docs steward
created: 2026-05-15
updated: 2026-05-15
policy_label: public
related:
  - docs/domains/archaeology/README.md
  - docs/domains/README.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/standards/PROV.md
  - control_plane/domain_lane_register.yaml
tags: [kfm, domain, archaeology, cultural-heritage, expansion-plan, sensitivity]
notes:
  - All path-shaped claims are PROPOSED until verified against mounted-repo evidence.
  - Sensitivity defaults follow Atlas v1.1 §24.5 tier matrix.
[/KFM_META_BLOCK_V2] -->

# Archaeology Domain — Expansion Plan

> Governed expansion roadmap for the **Archaeology / Cultural Heritage** lane of the Kansas Frontier Matrix — evidence-first, deny-by-default for exact site geometry, and bounded by steward and cultural review.

[![Status: Draft](https://img.shields.io/badge/status-draft-yellow)](#)
[![Authority: Doctrine ✦ Implementation PROPOSED](https://img.shields.io/badge/authority-doctrine%20%E2%9C%A6%20impl%20PROPOSED-blue)](#)
[![Lifecycle: RAW → PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-informational)](#7-lifecycle-pipeline-raw--published)
[![Sensitivity: T4 default](https://img.shields.io/badge/sensitivity-T4%20default-critical)](#8-sensitivity--rights-posture)
[![Last reviewed: 2026-05-15](https://img.shields.io/badge/last%20reviewed-2026--05--15-lightgrey)](#)
[![Doc type: standard](https://img.shields.io/badge/doc%20type-standard-success)](#)

| Field | Value |
|---|---|
| **Status** | Draft |
| **Owners** | TODO — Archaeology lane steward; Docs steward |
| **Last updated** | 2026-05-15 |
| **Authority of doctrine** | CONFIRMED via `[DOM-ARCH]`, `[ENCY] §7.13` / Atlas Ch. 15, `[DIRRULES]` |
| **Authority of paths** | PROPOSED — no mounted repo inspected this session |
| **Supersedes** | — (new doc) |

---

## Contents

1. [Purpose & Scope](#1-purpose--scope)
2. [Position in KFM](#2-position-in-kfm)
3. [Doctrinal Invariants](#3-doctrinal-invariants)
4. [Ubiquitous Language](#4-ubiquitous-language)
5. [Canonical Object Families](#5-canonical-object-families)
6. [Lane Scaffolding (Directory Layout)](#6-lane-scaffolding-directory-layout)
7. [Lifecycle Pipeline (RAW → PUBLISHED)](#7-lifecycle-pipeline-raw--published)
8. [Sensitivity & Rights Posture](#8-sensitivity--rights-posture)
9. [Cross-Lane Relations](#9-cross-lane-relations)
10. [Map & Viewing Products](#10-map--viewing-products)
11. [Thin-Slice Plan (Phase 5.A)](#11-thin-slice-plan-phase-5a)
12. [Expansion Phases & Milestones](#12-expansion-phases--milestones)
13. [Validators, Tests & Fixtures](#13-validators-tests--fixtures)
14. [Governed AI Behavior in this Lane](#14-governed-ai-behavior-in-this-lane)
15. [Publication, Correction & Rollback](#15-publication-correction--rollback)
16. [Verification Backlog & Open Questions](#16-verification-backlog--open-questions)
17. [Related Documents](#17-related-documents)

---

## 1. Purpose & Scope

> **CONFIRMED doctrine / PROPOSED implementation.**
> Govern archaeological sites, surveys, artifacts, contexts, excavation units, remote-sensing and LiDAR candidates, geophysics, 3D documentation, cultural/steward review, chronology, sensitivity transforms, and public-safe summaries — under deny-by-default exact-geometry rules and cultural-sovereignty review. `[DOM-ARCH]` `[ENCY] §7.13`

This **Expansion Plan** is the lane-level roadmap. It states what the Archaeology domain owns, what it does **not** own, where its files belong by Directory Rules §12, how it moves data through the KFM lifecycle, and what must be true before any release reaches a public surface. It is **not** a release decision, not a policy authority, and not a substitute for `policy/sensitivity/archaeology/` or for steward and cultural review.

**In-scope responsibility (CONFIRMED doctrine):**

- Archaeological sites, components, and cultural temporal periods.
- Surveys, transects, shovel tests, test units, excavation units, provenience context, stratigraphic units.
- Artifacts, features, contexts, collection accessions, chronology assertions.
- Remote-sensing anomalies, LiDAR candidates, geophysics observations.
- 3D documentation of sites and excavation units (admission-gated, never substitute for evidence).
- Sensitivity transforms, redactions, generalizations, and steward / cultural review records.

**Explicit non-ownership (CONFIRMED doctrine):**

- Roads/Rail, People/Land, Geology, Hazards, and Spatial Foundation supply *context*; they cannot confirm sites or bypass archaeological sensitivity. `[DOM-ARCH]` `[ENCY] §7.13`
- Planetary / 3D is an **alternate renderer** under admission, not an alternate truth path. `[MAP-MASTER]` `[DIRRULES]`
- KFM is never a life-safety, alert, or law-enforcement authority for looting incidents.

---

## 2. Position in KFM

> [!NOTE]
> This plan is one of the **per-lane** expansion plans contemplated by the Encyclopedia §21 roadmap (Phase 5 "Domain expansion") and by the Unified Manual §6.7 "Archaeology" lane summary. It carries doctrine forward; it does not invent new doctrine.

```mermaid
flowchart LR
  classDef root fill:#eef,stroke:#446;
  classDef doc fill:#efe,stroke:#464;
  classDef lane fill:#fee,stroke:#a44;

  DR["docs/doctrine/<br/>directory-rules.md"]:::doc
  ENC["[ENCY] §7.13<br/>Archaeology &amp; Cultural Heritage"]:::doc
  ATL["Atlas v1.1 Ch. 15 +<br/>§24.4.13 / §24.5"]:::doc
  DOMARCH["[DOM-ARCH]<br/>Archaeology dossier"]:::doc
  ROAD["[UNIFIED] §6.7<br/>Archaeology lane summary"]:::doc

  THIS["docs/domains/archaeology/<br/><b>EXPANSION_PLAN.md</b><br/>(this doc)"]:::root

  CONTRACTS["contracts/domains/archaeology/<br/>(PROPOSED)"]:::lane
  SCHEMAS["schemas/contracts/v1/domains/archaeology/<br/>(PROPOSED)"]:::lane
  POLICY["policy/domains/archaeology/<br/>policy/sensitivity/archaeology/<br/>(PROPOSED)"]:::lane
  TESTS["tests/domains/archaeology/<br/>fixtures/domains/archaeology/<br/>(PROPOSED)"]:::lane
  DATA["data/&lt;phase&gt;/archaeology/<br/>(PROPOSED)"]:::lane

  DR --> THIS
  ENC --> THIS
  ATL --> THIS
  DOMARCH --> THIS
  ROAD --> THIS

  THIS --> CONTRACTS
  THIS --> SCHEMAS
  THIS --> POLICY
  THIS --> TESTS
  THIS --> DATA
```

**Citations used in this doc (short names):**

| Short name | Source | Role |
|---|---|---|
| `[DOM-ARCH]` | Archaeology dossier (`KFM_Archaeology_Architecture_Plan_PDF_Only.pdf`) | Lane policy and implementation posture |
| `[ENCY]` | Encyclopedia §7.13 / §21 (`kfm_encyclopedia.pdf`) | Domain spine, programming backlog |
| `[ATLAS-v1.1]` | Domains Culmination Atlas v1.1, Ch. 15 + §24.4.13 + §24.5 + §24.6 | Doctrine extension; tier matrix; pipeline gates |
| `[DIRRULES]` | Directory Rules | Placement, lifecycle, README contract |
| `[UNIFIED]` | Unified Implementation Architecture Build Manual §6.7 | Lane summary; phase overlay |
| `[MAP-MASTER]` | Master MapLibre / Components-Functions-Features | Renderer doctrine; H3 r7 floor; CARE chips |
| `[GAI]` | Governed AI doctrine | AI ABSTAIN / DENY behavior in this lane |
| `[DDD]` | Domain-Driven Design Reference | Bounded-context, ubiquitous-language baseline |

---

## 3. Doctrinal Invariants

> [!WARNING]
> **Exact archaeological site locations are denied by default.** Burial, human remains, sacred sites, unresolved cultural sensitivity, collection security, private-landowner details, and looting-risk exposure all **fail closed**. `[DOM-ARCH]` `[ENCY] §7.13` `[ATLAS-v1.1] §24.5`

The following invariants govern every change to this lane. They are **CONFIRMED doctrine**. A change that bends one of these is an ADR-bearing action, not a routine PR.

1. **Lifecycle law.** `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`. Promotion is a **governed state transition, not a file move**. `[DIRRULES] §0`
2. **Trust membrane.** Public clients and normal UI surfaces consume governed APIs and released artifacts; never canonical or internal stores. `[DIRRULES] §7.1`
3. **Cite-or-abstain.** No public claim without `EvidenceBundle` closure. Uncited content cannot be elevated to a release surface. `[GAI]` `[ENCY]`
4. **Candidate-vs-confirmed.** `RemoteSensingAnomaly` and `LiDARCandidate` are **not** sites. Promotion to `ArchaeologicalSite` requires steward review and `EvidenceBundle` support. `[DOM-ARCH]`
5. **Exact-geometry denial.** Public products are generalized; geometry below an **H3 r7** floor is prohibited for sensitive archaeology products without review. `[MAP-MASTER]` (SRC-061, pp. 228–229)
6. **Sovereignty review.** Tribal and steward review govern cultural affiliation, sacred-site, and human-remains material. CARE labels and sovereignty notice chips are required in UI surfaces that touch this lane. `[MAP-MASTER]` `[ATLAS-v1.1] §24.4.13`
7. **3D is a renderer, not a truth path.** 3D site and excavation models are admission-gated; admission requires `RepresentationReceipt` + `RealityBoundaryNote`. `[ATLAS-v1.1] §24.4.13` `[MAP-MASTER]`
8. **Reversibility.** Every release has a rollback target and a correction path; tier downgrades (toward less public) never require an upgrade-style transform receipt. `[ATLAS-v1.1] §24.5.3`
9. **Watcher-as-non-publisher.** Connectors and watchers emit candidates and receipts; they do not publish. `[DIRRULES] §13`

---

## 4. Ubiquitous Language

> Following `[DDD]`: terms inside this lane MUST be used precisely. External standards (CIDOC-CRM, PROV-O) crosswalk *to* these terms; they do not rename them.

| Term | Meaning (CONFIRMED doctrine) | Anti-meaning (do not conflate) |
|---|---|---|
| **ArchaeologicalSite** | Confirmed site assertion with `EvidenceBundle` support and steward review state. | A `RemoteSensingAnomaly` or `LiDARCandidate`. |
| **SiteComponent** | A spatially or temporally distinct component within a site. | A separate site. |
| **CulturalTemporalPeriod** | Cultural-period classification used to bind chronology to context. | A calendar date or an `ExcavationUnit` date. |
| **SurveyProject / SurveyTransect / ShovelTest / TestUnit / ExcavationUnit** | Successively more invasive evidence-collection units, each with its own provenience. | A "site" by themselves. |
| **ProvenienceContext / StratigraphicUnit** | Spatial-temporal provenance of artifacts within an excavation. | An artifact's modern museum location. |
| **RemoteSensingAnomaly / LiDARCandidate / GeophysicsObservation** | Candidate-finding evidence; **not** site truth. | A confirmed site. |
| **ThreeDDocumentation** | Admission-gated 3D record with `RepresentationReceipt`. | Sovereign truth or a substitute for evidence. |
| **CulturalReview / StewardReview** | Recorded review by the appropriate cultural / steward authority. | Internal QA. |
| **CollectionAccession** | Museum / collection accession record. | Field-discovery record. |
| **ChronologyAssertion** | Dated claim with method, sample context, and uncertainty. | An assumed date. |
| **SensitivityTransform / RedactionReceipt** | The record of generalization, fuzzing, aggregation, or withholding applied before release. | The release itself. |

---

## 5. Canonical Object Families

> CONFIRMED doctrine for ownership; **PROPOSED** for deterministic-identity basis (`source id + object role + temporal scope + normalized digest`). `[ATLAS-v1.1] Ch. 15`

<details>
<summary><strong>Full object-family table</strong> (click to expand)</summary>

| Object family | Owned by Archaeology | Citing lanes (CONFIRMED) | Default tier | Notes |
|---|---|---|---|---|
| `ArchaeologicalSite` | ✅ | Settlements (historical context, generalized); Planetary/3D (admission-gated) | **T4** → T1 only via steward review + `RedactionReceipt` | Exact geometry never T0. |
| `SiteComponent` | ✅ | — | T4 / T1 | Inherits site sensitivity. |
| `CulturalTemporalPeriod` | ✅ | Settlements; Frontier Matrix | **T0** | Public; not a coordinate. |
| `SurveyProject` | ✅ | — | T0 (coverage) / T2 (detail) | Survey *coverage* is releasable; precise transects often T2. |
| `SurveyTransect` / `ShovelTest` / `TestUnit` | ✅ | — | T2 / T4 | Steward-only by default. |
| `ExcavationUnit` | ✅ | — | T2 / T4 | Access-controlled. |
| `ProvenienceContext` / `StratigraphicUnit` | ✅ | — | T2 / T4 | Bound to excavation. |
| `Artifact` / `Feature` / `Context` | ✅ | Settlements; People/Land (ethnobotanical/historical context) | T1 / T2 | Object metadata can be public; spatial detail rarely. |
| `RemoteSensingAnomaly` | ✅ | — | T4 default | **Not a site.** Candidate label required. |
| `LiDARCandidate` | ✅ | — | T4 default | **Not a site.** Generalized derivative only. |
| `GeophysicsObservation` | ✅ | — | T2 / T4 | Method, instrument, and uncertainty required. |
| `ThreeDDocumentation` | ✅ | Planetary/3D | T1 / T2 / T4 | Requires `RepresentationReceipt` + `RealityBoundaryNote`. |
| `CulturalReview` | ✅ | — | T2 (audit) | Sovereignty-bearing record. |
| `StewardReview` | ✅ | — | T2 (audit) | Required for any tier upgrade above T4. |
| `CollectionAccession` | ✅ | — | T0 / T1 | Public metadata; collection security may restrict. |
| `ChronologyAssertion` | ✅ | Frontier Matrix; Settlements | T0 / T1 | Method and uncertainty mandatory. |
| `SensitivityTransform` | ✅ | All | T2 (audit) | Pairs with every release in this lane. |

</details>

---

## 6. Lane Scaffolding (Directory Layout)

> **PROPOSED paths.** Per `[DIRRULES] §12` "Domain Placement Law," archaeology lives as a **segment** inside responsibility roots, never as a root itself. Every path below is PROPOSED until verified against a mounted repository.

```text
# Archaeology lane scaffolding — PROPOSED
docs/domains/archaeology/                       # this folder (human explanation)
  ├── README.md                                  # PROPOSED — lane README per §15 contract
  ├── EXPANSION_PLAN.md                          # this file
  └── ...

contracts/domains/archaeology/                  # object-family meaning
schemas/contracts/v1/domains/archaeology/       # machine-checkable shape (canonical per ADR-0001)
policy/domains/archaeology/                     # admissibility policy
policy/sensitivity/archaeology/                 # deny-by-default + transform rules
tests/domains/archaeology/                      # enforceability proof
fixtures/domains/archaeology/                   # golden / valid / invalid fixtures
packages/domains/archaeology/                   # shared library (if needed)
pipelines/domains/archaeology/                  # executable pipeline logic
pipeline_specs/archaeology/                     # declarative pipeline config

data/raw/archaeology/                           # immutable source captures (T4)
data/work/archaeology/                          # in-flight normalization
data/quarantine/archaeology/                    # failures and holds
data/processed/archaeology/                     # validated normalized objects
data/catalog/domain/archaeology/                # catalog + EvidenceBundles
data/triplets/archaeology/                      # graph projections (if applicable)
data/published/layers/archaeology/              # public-safe layers ONLY
data/registry/sources/archaeology/              # SourceDescriptors for this lane

release/candidates/archaeology/                 # ReleaseManifest candidates
```

```mermaid
flowchart TB
  classDef governance fill:#eef,stroke:#446,color:#113;
  classDef build fill:#efe,stroke:#464,color:#131;
  classDef data fill:#fee,stroke:#a44,color:#311;
  classDef release fill:#ffe,stroke:#aa4,color:#331;

  subgraph G["Governance &amp; Meaning"]
    direction LR
    DOCS["docs/domains/archaeology/"]:::governance
    CONTRACTS["contracts/domains/archaeology/"]:::governance
    SCHEMAS["schemas/contracts/v1/domains/archaeology/"]:::governance
    POL["policy/domains/archaeology/<br/>policy/sensitivity/archaeology/"]:::governance
  end

  subgraph B["Build &amp; Enforcement"]
    direction LR
    PKG["packages/domains/archaeology/"]:::build
    PIPE["pipelines/domains/archaeology/<br/>pipeline_specs/archaeology/"]:::build
    TESTS["tests/domains/archaeology/<br/>fixtures/domains/archaeology/"]:::build
  end

  subgraph D["Lifecycle Data"]
    direction LR
    RAW["data/raw/archaeology/"]:::data
    WORK["data/work/archaeology/<br/>data/quarantine/archaeology/"]:::data
    PROC["data/processed/archaeology/"]:::data
    CAT["data/catalog/domain/archaeology/<br/>data/triplets/archaeology/"]:::data
    PUB["data/published/layers/archaeology/"]:::data
    REG["data/registry/sources/archaeology/"]:::data
  end

  subgraph R["Release"]
    direction LR
    REL["release/candidates/archaeology/"]:::release
  end

  G --> B --> D --> R
  REG --- RAW
```

> [!NOTE]
> Cross-domain files (e.g., a shared geometry-generalization validator used by Archaeology **and** Fauna) live in the **lowest common responsibility root** without a domain segment — for example `tools/validators/<topic>/` rather than `tools/validators/domains/archaeology/`. `[DIRRULES] §12`

---

## 7. Lifecycle Pipeline (RAW → PUBLISHED)

> CONFIRMED doctrine / **PROPOSED** lane application. Each stage is governed by `[ATLAS-v1.1] §24.6` master pipeline gates. Promotion fails closed.

```mermaid
flowchart LR
  RAW[("RAW<br/>immutable source capture")] -->|Admission gate<br/>SourceDescriptor + hash| WORK
  WORK[("WORK / QUARANTINE<br/>normalize · validate · policy-check")] -->|Validation gate<br/>ValidationReport + RedactionReceipt| PROC
  PROC[("PROCESSED<br/>validated normalized objects")] -->|Catalog closure<br/>EvidenceBundle + digest closure| CAT
  CAT[("CATALOG / TRIPLET<br/>EvidenceBundle + graph projection")] -->|Release gate<br/>ReleaseManifest + rollback target + ReviewRecord| PUB
  PUB[("PUBLISHED<br/>governed API + public-safe layers")]

  WORK -. quarantine .-> QUAR[("QUARANTINE<br/>reason recorded; never silent promote")]
  PUB -. correction .-> COR[("CorrectionNotice<br/>+ RollbackCard")]
  COR --> PUB
```

| Gate (transition) | Required artifacts (PROPOSED minimum) | Failure outcome | Status |
|---|---|---|---|
| **Admission** (— → RAW) | `SourceDescriptor` (role, authority, rights, sensitivity, cadence), payload hash | Source rejected; candidate logged for steward | PROPOSED |
| **Normalization** (RAW → WORK / QUARANTINE) | `TransformReceipt`, working `ValidationReport`, `PolicyDecision`; quarantine reason on failure | Quarantine with reason; never silent promote | PROPOSED |
| **Validation** (WORK → PROCESSED) | Passing `ValidationReport`; `RedactionReceipt` if sensitivity applies; `AggregationReceipt` if applies | Stay in WORK; structured FAIL outcome | PROPOSED |
| **Catalog closure** (PROCESSED → CATALOG / TRIPLET) | `CatalogMatrix` entry, `EvidenceBundle`, graph / triplet projections | HOLD at PROCESSED; no public edge | PROPOSED |
| **Release** (CATALOG / TRIPLET → PUBLISHED) | `ReleaseManifest`, rollback target, correction path, `ReviewRecord` (Steward + Cultural where required) | HOLD at CATALOG; no public surface change | PROPOSED |
| **Correction** (PUBLISHED → PUBLISHED′) | `CorrectionNotice` linking superseded release; downstream derivatives identified | Stale-state badge; rollback if material | PROPOSED |

[↑ Back to top](#contents)

---

## 8. Sensitivity & Rights Posture

> [!CAUTION]
> The Archaeology lane is the strictest sensitivity lane in KFM apart from People/DNA. Default-tier reasoning is **CONFIRMED doctrine**; transform rules are **PROPOSED** until policy bundles are reviewed.

### 8.1 Tier matrix (extends `[ATLAS-v1.1] §24.5`)

| Object class | Default tier | Allowed transforms (PROPOSED) | Required gates |
|---|---|---|---|
| Archaeology — exact site location | **T4** | Steward review + cultural review + generalized geometry (coarse cell, ≥ H3 r7) + `RedactionReceipt` → T2 or T1. | `RedactionReceipt` + `ReviewRecord` + `PolicyDecision` |
| Archaeology — human remains / sacred sites / burial | **T4 (effectively forever)** | No transform releases to T0 / T1. T3 only under explicit named authorization. | Sovereignty review + `ReviewRecord` + `PolicyDecision` |
| Archaeology — survey coverage (footprint only) | T1 | Aggregated / generalized public-safe summary. | `AggregationReceipt` or `RedactionReceipt` |
| Archaeology — `CulturalTemporalPeriod`, chronology | T0 | None required (no geometry). | Standard release gates |
| Archaeology — `RemoteSensingAnomaly` / `LiDARCandidate` | **T4** | Generalized derivative + candidate label + steward review → T1 / T2. | `RedactionReceipt` + `ReviewRecord` |
| Archaeology — `ThreeDDocumentation` | T2 / T4 | Generalization / clipping / withholding + `RepresentationReceipt` + `RealityBoundaryNote` → T1 / T2. | Steward review + `RedactionReceipt` + `RepresentationReceipt` |
| Archaeology — `CollectionAccession` (catalog metadata) | T0 / T1 | Suppress provenance keys for at-risk collections. | Steward review where applicable |
| AI surface (Focus Mode) — exact-location queries | **T4** | No transform permits AI to emit exact archaeological coordinates. | `PolicyDecision` + `AIReceipt`; AI returns `DENY` |

### 8.2 Tier transitions (CONFIRMED doctrine)

```mermaid
flowchart LR
  T4 -- "PolicyDecision + ReviewRecord + agreement" --> T3
  T4 -- "PolicyDecision + ReviewRecord" --> T2
  T4 -- "RedactionReceipt + ReviewRecord" --> T1
  T3 -- "PolicyDecision + ReviewRecord" --> T2
  T2 -- "RedactionReceipt + ReviewRecord" --> T1
  T1 -- "ReleaseManifest + ReviewRecord" --> T0
  T0 -. "CorrectionNotice + ReviewRecord" .-> T4
  T1 -. "CorrectionNotice + ReviewRecord" .-> T4
  T2 -. "CorrectionNotice + ReviewRecord" .-> T4
```

> **Reading rule:** a tier *upgrade* (toward more public) always needs both a transform receipt **and** a review record. A tier *downgrade* (toward less public) never needs both — a `CorrectionNotice` alone is sufficient. `[ATLAS-v1.1] §24.5.3`

### 8.3 Deny-by-default register (this lane)

| Denied by default | Allowed only when | Validator |
|---|---|---|
| Exact site coordinates | Steward review + transform receipt + `EvidenceBundle` | Exact-sensitive-geometry denial test |
| Sub-H3-r7 geometry on public archaeology products | Steward approval + alternative generalization scheme | H3 floor test |
| Burial / human-remains exposure | Never to T0 / T1; T3 only under named authorization | Sovereignty-review deny test |
| Looting-risk detail (recent disturbance, intact deposits, etc.) | Steward + rights-holder review | Looting-risk policy test |
| AI direct emission of exact coordinates | Never | AI exact-location denial test |
| Unattributed Focus Mode summary | Never | Citation validation test |

[↑ Back to top](#contents)

---

## 9. Cross-Lane Relations

> CONFIRMED doctrine for edge ownership; **PROPOSED** for edge-specific schemas and policy bindings. `[ATLAS-v1.1] §24.4.13`

| This lane | Related lane | Relation type | Constraint |
|---|---|---|---|
| Archaeology | Spatial Foundation | Exact / public geometry split and transform receipts | Public products carry `SensitivityTransform`; raw geometry never leaks via spatial joins. |
| Archaeology | Roads / Rail / Trade Routes | Historic routes and cultural paths | Site coords denied; corridor context allowed under steward review. |
| Archaeology | Settlements / Infrastructure | Forts, missions, townsites, reservation communities | Cultural temporal period and survey context bound interpretation; site coords denied. |
| Archaeology | Hazards | Threat, erosion, fire, flood, exposure context | Hazard context allowed; KFM is **never** an alert authority. |
| Archaeology | Planetary / 3D | Admission-only 3D representation | `RepresentationReceipt` + `RealityBoundaryNote` required; generalization preserved. |
| Archaeology | People / Genealogy / Land | Cultural affiliations | Cited only with rights, sovereignty, and steward review. |

---

## 10. Map & Viewing Products

> PROPOSED viewing products. Every product crosses the Evidence Drawer, trust-badge, sensitivity-redacted view, and correction / stale-state view. `[MAP-MASTER]` `[GAI]`

| Viewing product | Public tier | Required elements |
|---|---|---|
| Public generalized site summary | T1 | CARE label + sovereignty notice chip + generalized geometry + Evidence Drawer |
| Public survey-coverage summary | T1 | Aggregated footprint + `AggregationReceipt` |
| Candidate-feature surface (LiDAR / remote sensing) | T1 (generalized) | "Candidate, not site" label; trust badge; uncertainty class |
| Steward-only exact-site review | T2 | Authenticated session + `ReviewRecord`; never accessible to public client |
| Restricted exact-geometry review | T3 | Named-party agreement; audit log; correction path |
| Chronology / context view | T0 | Period, method, uncertainty — no precise locations |
| 3D site documentation (admission-gated) | T1 / T2 | `RepresentationReceipt` + `RealityBoundaryNote` |
| Threat / risk review view (steward) | T2 | Steward review + redaction-receipt audit |
| Focus Mode (governed AI) | T1 / T2 | `AIReceipt`; ANSWER / ABSTAIN / DENY / ERROR envelope; citation validation |

[↑ Back to top](#contents)

---

## 11. Thin-Slice Plan (Phase 5.A)

> **CONFIRMED doctrine / PROPOSED implementation.**
> Per `[DOM-ARCH] §N` (domain thin-slice plan) and `[ENCY]` Phase 5 of the programming-possibilities backlog.

**Thin slice goal.** Prove that the Archaeology lane can take a single synthetic candidate through the full lifecycle without leaking exact geometry, under realistic policy and review gates.

**Slice contents (PROPOSED):**

1. **One synthetic `RemoteSensingAnomaly` or `LiDARCandidate` fixture** — exact geometry denied at every public seam.
2. **One steward-only exact-geometry review record.**
3. **One public generalized tile** (≥ H3 r7) bound to the candidate, carrying `SensitivityTransform` and `RedactionReceipt`.
4. **One `EvidenceBundle`** for the public-safe derivative.
5. **One `StewardReview` + `CulturalReview` pair** with reviewer identity, decision, and timestamp.
6. **One `ReleaseManifest`** with a paired `RollbackCard` and a documented correction path.
7. **One AI Focus Mode exchange** that DENIES exact-location queries and ABSTAINS when evidence is insufficient.

```mermaid
flowchart TB
  A["Synthetic candidate fixture<br/>(LiDARCandidate, no real coords)"] --> B["WORK normalization<br/>+ ValidationReport"]
  B --> C["Steward + Cultural review<br/>(records)"]
  C --> D["RedactionReceipt<br/>generalize to ≥ H3 r7"]
  D --> E["EvidenceBundle assembly<br/>+ CatalogMatrix entry"]
  E --> F["ReleaseManifest + RollbackCard"]
  F --> G["Public generalized tile<br/>+ Evidence Drawer + CARE chip"]
  G --> H["Focus Mode test<br/>(DENY exact-coords; ABSTAIN if unsupported)"]

  F -. correction .-> X["CorrectionNotice + rollback drill"]
  X --> F
```

**Exit criteria (PROPOSED):**

- No exact geometry crosses the public seam at any point.
- All seven artifact types above exist and validate.
- AI surface never emits exact archaeological coordinates.
- Rollback drill restores the previous release state from `RollbackCard`.

---

## 12. Expansion Phases & Milestones

> CONFIRMED doctrine for sequencing intent; **PROPOSED** for any concrete milestone date or owner. Sequencing follows `[ENCY] §21` and `[UNIFIED] §6.7`. The hydrology lane is the **safest** first proof-bearing slice; archaeology expansion proceeds only **after** the hydrology pattern is established. `[ENCY] §21` `[UNIFIED] §6.7`

| Phase | Scope (PROPOSED) | Exit criteria | Rollback / failure posture |
|---|---|---|---|
| **A. Lane scaffolding** | Land per-root READMEs (§15 contract) for the archaeology lane segments listed in §6; cite `[DIRRULES]`. | Each affected README meets the §15 contract; drift register has no open lane-placement entries. | Revert doc PR; preserve correction note. |
| **B. Source ledger** | Register `SourceDescriptor`s for state historic-preservation records, tribal / steward record protocols, excavation reports, museum / collection accessions, LiDAR / remote-sensing / geophysics, historical maps, 3D documentation. | `data/registry/sources/archaeology/` populated; all rights and sensitivity classes set. | Remove sources without rights; mark NEEDS VERIFICATION. |
| **C. Schemas + no-network fixtures** | Object-family schemas (§5) under `schemas/contracts/v1/domains/archaeology/`; valid + invalid fixtures under `fixtures/domains/archaeology/`. | Schemas validate fixtures; no real coordinates present. | Remove schema wave if ADR fails. |
| **D. Validators + policy gates** | Reason-coded `DENY / ABSTAIN / ERROR / HOLD` outcomes for the validators listed in §13. Deny-by-default policy bundles under `policy/sensitivity/archaeology/`. | All §13 tests pass on fixtures; deny-by-default verified. | Disable validator only if a stronger gate replaces it. |
| **E. Thin slice** | Execute §11 plan end-to-end on synthetic data. | All seven artifact types exist and validate; AI DENY/ABSTAIN behavior verified. | Disable public seam; rollback to pre-slice state. |
| **F. Cross-lane edges** | Activate `[ATLAS-v1.1] §24.4.13` edges with Settlements, Roads/Rail, Hazards, Planetary/3D, Spatial Foundation, People/Land — each as a separate, reviewed PR. | Edge tests pass; site coords still denied at every seam. | Disable individual edges; keep core lane. |
| **G. UI integration** | Public generalized layer + Evidence Drawer + CARE / sovereignty chips + candidate-not-site labels in the map shell. `[MAP-MASTER]` | Accessibility tests pass; trust badges visible; no leakage paths in browser DOM. | Revert layer registry entry. |
| **H. Governed AI Focus Mode** | Archaeology-aware Focus Mode with citation validation, exact-location DENY, and explainability overlays. `[MAP-MASTER]` (ML-061-162) | All `[GAI]` finite-outcome tests pass for this lane. | Disable AI adapter. |

[↑ Back to top](#contents)

---

## 13. Validators, Tests & Fixtures

> PROPOSED set; doctrine basis is `[DOM-ARCH] K. Validators, tests, fixtures` and `[MAP-MASTER]` sensitive-geometry tests.

| Validator / test | What it proves | Failure outcome |
|---|---|---|
| `EvidenceBundle`-required test | No public claim without resolved evidence. | `DENY` (publication blocked). |
| Candidate-not-site test | `RemoteSensingAnomaly` / `LiDARCandidate` cannot be promoted to `ArchaeologicalSite` without steward review. | `HOLD`. |
| Public no-leak test | No exact site coordinates appear in any published artifact, tile, drawer payload, or AI response. | `DENY`. |
| Rights and cultural-review test | Releases without `CulturalReview` + `StewardReview` records are blocked where required. | `DENY`. |
| Exact sensitive geometry denial | Geometry below H3 r7 prohibited for sensitive archaeology products. | `DENY`. |
| Catalog closure test | `EvidenceRef` resolves; digests close; `CatalogMatrix` entry exists. | `HOLD`. |
| AI exact-location denial | Focus Mode must `DENY` exact-coordinate queries and `ABSTAIN` when evidence is insufficient. | `DENY` / `ABSTAIN`. |
| Generalization-log audit | Every released tile has a paired `RedactionReceipt` describing the generalization. | `DENY`. |
| 3D admission gate | `ThreeDDocumentation` releases require `RepresentationReceipt` + `RealityBoundaryNote`. | `HOLD`. |
| Rollback drill | `RollbackCard` restores prior release; `CorrectionNotice` issued. | `ERROR` (rollback drill failed). |

> [!TIP]
> Fixtures live under `fixtures/domains/archaeology/` (PROPOSED). Per `[DIRRULES] §13.5`, fixtures must not be duplicated across `tests/fixtures/` and root `fixtures/` — choose one authority and document it in both READMEs.

---

## 14. Governed AI Behavior in this Lane

> CONFIRMED doctrine / PROPOSED implementation. `[GAI]` `[DOM-ARCH] L` `[MAP-MASTER]` ML-061-162, ML-061-163.

AI in the Archaeology lane is **interpretive, never sovereign**. It MAY:

- Summarize released `EvidenceBundle`s.
- Compare evidence sources and explain limitations.
- Draft `StewardReview` notes for human review.
- Describe `CulturalTemporalPeriod` context using cited evidence.

It MUST:

- `ABSTAIN` when evidence is insufficient.
- `DENY` where policy, rights, sensitivity, or release state blocks the request — explicitly including any request that would produce exact archaeological coordinates.
- Wrap every response in a `RuntimeResponseEnvelope` with finite outcomes `ANSWER | ABSTAIN | DENY | ERROR`.
- Emit an `AIReceipt` for every Focus Mode interaction, citing the `EvidenceBundle`s consulted.

**Example doctrinal answer pattern (paraphrased from `[MAP-MASTER]` ML-061-163):**

> *"This summary describes generalized cultural-activity zones, not exact archaeological locations. Coordinates below the H3 r7 floor are denied. Steward review records: [refs]. Sources: [refs]."*

---

## 15. Publication, Correction & Rollback

> CONFIRMED doctrine / PROPOSED implementation. `[DOM-ARCH] M` `[ENCY] Appendix E` `[ATLAS-v1.1] §24.6`

Publication in this lane requires **all** of the following to be present and pass closure:

1. `ReleaseManifest` referencing the candidate.
2. `EvidenceBundle` with closed `EvidenceRef`s.
3. `ValidationReport` (passing).
4. `PolicyDecision` (ANSWER).
5. `RedactionReceipt` for any sensitivity transform applied.
6. `StewardReview` + `CulturalReview` records where required (default: required for any site-bearing release).
7. Correction path (resolvable `CorrectionNotice` target).
8. `RollbackCard` with a tested rollback drill.

> [!IMPORTANT]
> **Release authority must be distinct from the original author** when materiality applies. Separation-of-duties for archaeology releases that touch site identity, sacred-site context, or cultural affiliation. `[ATLAS-v1.1] §24.7` (Reviewer Role / Separation-of-Duties matrix).

A correction is a **publication-class event**, not an edit. It emits its own receipts and may demote a published tier to a stricter one without an upgrade-style transform receipt.

---

## 16. Verification Backlog & Open Questions

> Items below are **explicitly unresolved** in this plan and SHOULD be tracked in `docs/registers/VERIFICATION_BACKLOG.md` and / or addressed via ADR. Path-shaped items are PROPOSED until repository inspection confirms them.

| Item | Status | What would settle it |
|---|---|---|
| Lane-segment paths in §6 match the mounted repo. | NEEDS VERIFICATION | `git ls-tree` inspection against `[DIRRULES] §5` canonical tree. |
| `policy/sensitivity/archaeology/` bundle is the canonical home for deny-by-default. | NEEDS VERIFICATION | Inspect `policy/` and `policies/` (compatibility); confirm ADR. |
| Schema home for archaeology objects is `schemas/contracts/v1/domains/archaeology/`. | NEEDS VERIFICATION | Inspect ADR-0001 and current schema roots. |
| H3 r7 floor remains the agreed generalization threshold. | NEEDS VERIFICATION | Steward / cultural-review approval of fixture; policy rule under `policy/sensitivity/archaeology/`. |
| State-historic-preservation source rights, including redistribution and steward responsibilities. | NEEDS VERIFICATION | `SourceDescriptor` review; legal / steward sign-off. |
| Tribal / cultural review protocol — which authorities review which categories. | NEEDS VERIFICATION | Sovereignty review; protocol documentation. |
| Critical-collection security thresholds for `CollectionAccession` publishing. | NEEDS VERIFICATION | Museum / collection steward protocol. |
| 3D admission policy — `RepresentationReceipt` schema and `RealityBoundaryNote` template. | NEEDS VERIFICATION | `[MAP-MASTER]` admission policy ADR. |
| Reviewer separation-of-duties for archaeology releases. | NEEDS VERIFICATION | `[ATLAS-v1.1] §24.7` operationalization. |
| Lane README (`docs/domains/archaeology/README.md`) status. | UNKNOWN | Mount repo and inspect, or author one. |
| Owners listed in the meta block. | TODO (placeholder) | Lane steward assignment. |
| Mounted-repo evidence for any lane folder. | UNKNOWN | No mounted repo this session. |

<details>
<summary><strong>Open design questions (click to expand)</strong></summary>

- Should `RemoteSensingAnomaly` and `LiDARCandidate` share a common candidate-object base type, or remain distinct schemas? (PROPOSED: distinct, with a shared `CandidateFeature` mixin.)
- Should `ThreeDDocumentation` carry `RepresentationReceipt` inline or via reference? (PROPOSED: reference, to keep public derivatives small.)
- What chronology-uncertainty scheme is used for `ChronologyAssertion` — calibrated radiocarbon ranges, cultural-period tags, or both? (PROPOSED: both, with method recorded.)
- Should `CollectionAccession` records cross-reference People/Land for historic ownership? (PROPOSED: only via aggregated / generalized layers; private joins denied.)
- Should a synthetic looting-incident fixture exist to test no-leak behavior? (PROPOSED: yes, with all coordinates synthetic; reviewer approval required.)
</details>

[↑ Back to top](#contents)

---

## 17. Related Documents

| Document | Purpose |
|---|---|
| [`docs/domains/archaeology/README.md`](./README.md) | Lane orientation README (TODO — author per `[DIRRULES] §15` contract). |
| [`docs/domains/README.md`](../README.md) | Cross-domain lane index (TODO). |
| [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) | Canonical placement and lifecycle doctrine. `[DIRRULES]` |
| [`docs/doctrine/lifecycle-law.md`](../../doctrine/lifecycle-law.md) | Lifecycle invariant (TODO — link target NEEDS VERIFICATION). |
| [`docs/doctrine/trust-membrane.md`](../../doctrine/trust-membrane.md) | Public-path discipline (TODO — link target NEEDS VERIFICATION). |
| [`docs/standards/PROV.md`](../../standards/PROV.md) | W3C PROV-O / PAV provenance crosswalk. |
| [`policy/sensitivity/archaeology/`](../../../policy/sensitivity/archaeology/) | Deny-by-default policy bundle (PROPOSED home). |
| [`schemas/contracts/v1/domains/archaeology/`](../../../schemas/contracts/v1/domains/archaeology/) | Machine-checkable object shapes (PROPOSED home). |
| [`contracts/domains/archaeology/`](../../../contracts/domains/archaeology/) | Object-family meaning (PROPOSED home). |
| Atlas v1.1 Ch. 15 + §24.4.13 + §24.5 | Doctrine extension; cross-lane edges; sensitivity tier matrix. `[ATLAS-v1.1]` |
| Encyclopedia §7.13 + §21 | Domain spine; programming-possibilities backlog. `[ENCY]` |
| Unified Manual §6.7 (Archaeology) | Lane summary; phase overlay. `[UNIFIED]` |
| Master MapLibre / Components doc | Renderer doctrine; H3 r7 floor; CARE chips; Focus Mode. `[MAP-MASTER]` |

---

<div align="center">

**Kansas Frontier Matrix · Archaeology Domain · Expansion Plan**

`v0.1 · 2026-05-15 · draft`

[Related docs](#17-related-documents) · [Verification backlog](#16-verification-backlog--open-questions) · [↑ Back to top](#contents)

</div>
