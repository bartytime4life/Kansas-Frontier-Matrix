<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domain-archaeology-architecture
title: Archaeology Domain — Architecture
type: standard
version: v1
status: draft
owners: TODO — Archaeology domain steward · Sensitivity reviewer · Cultural/sovereignty review liaison · Docs steward · Release authority
created: 2026-05-15
updated: 2026-05-15
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/truth-posture.md
  - docs/architecture/governed-api.md
  - docs/domains/archaeology/README.md
  - docs/runbooks/archaeology/PROMOTION_RUNBOOK.md
  - docs/runbooks/archaeology/ROLLBACK_RUNBOOK.md
  - contracts/domains/archaeology/
  - schemas/contracts/v1/domains/archaeology/
  - policy/domains/archaeology/
  - policy/sensitivity/archaeology/
tags: [kfm, domain, archaeology, architecture, sensitive-lane, deny-default]
notes:
  - "Doctrine is CONFIRMED from [ENCY] §7.13, [DOM-ARCH], and [DIRRULES]. Implementation maturity is UNKNOWN until verified against mounted-repo evidence."
  - "Every PROPOSED path follows Directory Rules §12 (Domain Placement Law); none is asserted as present in the live repo."
  - "Single-file vs folder pattern for docs/domains/<domain>/architecture is an open ADR; this file follows the established <domain>/ARCHITECTURE.md precedent in adjacent lanes."
[/KFM_META_BLOCK_V2] -->

# Archaeology Domain — Architecture

Governed, evidence-first, sensitivity-bounded architecture for KFM's Archaeology and Cultural Heritage lane — where **exact site locations deny by default** and every public claim must be downstream of evidence, rights, steward review, and release state.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![doctrine: CONFIRMED](https://img.shields.io/badge/doctrine-CONFIRMED-blue)
![implementation: PROPOSED](https://img.shields.io/badge/implementation-PROPOSED-lightgrey)
![sensitivity: deny--by--default](https://img.shields.io/badge/sensitivity-deny--by--default-critical)
![lane: archaeology](https://img.shields.io/badge/lane-archaeology-purple)
![lifecycle: RAW%E2%86%92PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-success)
![last updated: 2026--05--15](https://img.shields.io/badge/last%20updated-2026--05--15-informational)

| Field | Value |
|---|---|
| **Status** | Draft · doctrine CONFIRMED · implementation PROPOSED |
| **Owners** | TODO — Archaeology domain steward · Sensitivity reviewer · Cultural/sovereignty review liaison |
| **Authority basis** | `[ENCY]` §7.13 · `[DOM-ARCH]` · `[DIRRULES]` §12 · `[GAI]` §24.3 |
| **Public posture** | Deny-by-default for exact sites, burial/sacred materials, oral history, collection security |
| **Lifecycle** | RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED |
| **Last updated** | 2026-05-15 |

> [!CAUTION]
> This domain is on the **sensitive lane**. Exact site coordinates, burial / human-remains records, sacred-place attributes, oral-history payloads, and collection-security details **fail closed** at every gate. No section of this document authorizes a release; releases are governed by `ReleaseManifest`, `EvidenceBundle`, policy gates, and an explicit cultural / steward review record.

---

## Mini-TOC

1. [Mission and boundary](#1-mission-and-boundary)
2. [Scope — owned and not owned](#2-scope--owned-and-not-owned)
3. [Ubiquitous language](#3-ubiquitous-language)
4. [Lane layout](#4-lane-layout)
5. [Canonical object families](#5-canonical-object-families)
6. [Source families and source roles](#6-source-families-and-source-roles)
7. [Lifecycle and pipeline shape](#7-lifecycle-and-pipeline-shape)
8. [Sensitivity, rights, and publication posture](#8-sensitivity-rights-and-publication-posture)
9. [Cross-lane relations](#9-cross-lane-relations)
10. [Governed API surfaces and finite outcomes](#10-governed-api-surfaces-and-finite-outcomes)
11. [Governed AI behavior](#11-governed-ai-behavior)
12. [Validators, tests, and fixtures](#12-validators-tests-and-fixtures)
13. [Publication, correction, and rollback](#13-publication-correction-and-rollback)
14. [Verification backlog](#14-verification-backlog)
15. [Open ADRs and questions](#15-open-adrs-and-questions)
16. [Related docs](#16-related-docs)

---

## 1. Mission and boundary

**CONFIRMED doctrine** — The Archaeology lane preserves archaeological and cultural heritage knowledge through strict sensitivity, cultural/steward review, a candidate-versus-confirmed distinction, and exact-location denial by default. It owns archaeological sites, surveys, artifacts, features, contexts, excavation units, remote-sensing anomalies, LiDAR candidates, geophysics, 3D documentation, collections/accessions, and chronology. It **MUST NOT** publish exact sites, sacred places, burial / human-remains records, or culturally sensitive material without proper review. (`[ENCY]` §7.13.A; `[DOM-ARCH]`)

**CONFIRMED doctrine** — A `CandidateFeature` (e.g., a LiDAR anomaly, a remote-sensing signature) is **not** an `ArchaeologicalSite`. Promotion from candidate to confirmed is a governed state transition, never a file move or a UI label change. (`[DOM-ARCH]` §E; `[DIRRULES]` §3)

**CONFIRMED doctrine** — Archaeology operates inside KFM's trust membrane: public clients and normal UI surfaces consume governed APIs, not canonical or internal stores; AI may summarize or compare released evidence but is never a root truth source. (`[DIRRULES]` §7.1; `[GAI]`)

> [!NOTE]
> The mission statement is doctrine-bearing. Specific implementation paths quoted later in this document are **PROPOSED** until verified against mounted-repo evidence; doctrine itself is **CONFIRMED**.

[Back to top ↑](#archaeology-domain--architecture)

---

## 2. Scope — owned and not owned

### 2.1 Owned by this lane

**CONFIRMED / PROPOSED** — Archaeology owns the following object families (`[DOM-ARCH]` §B; `[ENCY]` §7.13.C):

- `ArchaeologicalSite` · `Survey` · `Artifact` · `Feature` · `Context` · `ExcavationUnit`
- `RemoteSensingAnomaly` · `LiDARCandidate` · `GeophysicsObservation` · `ThreeDDocumentation`
- `CulturalReview` · `StewardReview` · `CollectionAccession` · `ChronologyAssertion`
- `SensitivityTransform` · `CandidateFeature` · `PublicationTransformReceipt`

### 2.2 Explicitly not owned

**CONFIRMED / PROPOSED** — These lanes provide context but **MUST NOT** confirm sites or bypass archaeological sensitivity (`[DOM-ARCH]` §B):

| Lane | Provides context for | Forbidden behavior |
|---|---|---|
| Spatial Foundation | Base geometry, CRS, generalization profiles | Asserting site identity or releasing exact archaeological geometry |
| Roads / Rail / Trade | Historic routes, cultural paths | Promoting a route to a site without steward review |
| Settlements / Infrastructure | Forts, missions, townsites, reservation communities | Folding archaeological provenience into settlement metadata |
| Hazards | Threat, erosion, fire, flood, exposure context | Re-exposing exact-site geometry through a hazard surface |
| Geology | Subsurface and surficial geology context | Treating geophysics anomalies as confirmed cultural features |
| People / Genealogy / DNA / Land | Cultural affiliations, ownership context | Bypassing sovereignty / rights review |

### 2.3 Architectural posture

```text
Archaeology is a SENSITIVE LANE.
  → Default outcome for ambiguous exposure = DENY.
  → Public claim authority = EvidenceBundle + ReleaseManifest + ReviewRecord + PolicyDecision(allow).
  → AI authority = ABSTAIN unless released EvidenceBundle exists.
  → Promotion authority = governed state transition, never a file move.
```

[Back to top ↑](#archaeology-domain--architecture)

---

## 3. Ubiquitous language

**CONFIRMED term / PROPOSED field realization** — Each term is used inside this domain with meaning constrained by source role, evidence, time, and release state (`[DOM-ARCH]` §C; `[ENCY]` §7.13).

| Term | Role | Notes |
|---|---|---|
| `ArchaeologicalSite` | Confirmed cultural / archaeological location with provenance and review | Public exact geometry denied by default |
| `SiteComponent` | Sub-element of a site (e.g., feature cluster, occupation) | Inherits parent sensitivity |
| `CulturalTemporalPeriod` | Cultural / chronological framework (period, phase, complex) | Distinct from absolute date ranges |
| `SurveyProject` | Authorized field / desktop survey activity | Source for survey coverage products |
| `SurveyTransect` | Spatial unit within a SurveyProject | Coverage geometry is generalizable; raw transect geometry may be restricted |
| `ExcavationUnit` | Controlled excavation locus (e.g., test unit, block) | Access-controlled; preserves stratigraphic context |
| `ProvenienceContext` | Spatial / stratigraphic placement of an `ArtifactRecord` | Identity tied to `ExcavationUnit` + `StratigraphicUnit` |
| `StratigraphicUnit` | Discrete depositional / disturbance unit | Required for interpretive chronology |
| `ArtifactRecord` | Catalogued artifact with provenience | Public release requires collection-rights review |
| `CollectionRepositoryRecord` | Museum / accession-level record | Includes accession ID, repository, access class |
| `CandidateFeature` | Remote-sensing / LiDAR / geophysics anomaly **not** confirmed as a site | **MUST NOT** be served on public surfaces as a site |
| `PublicationTransformReceipt` | Audit record of every public-safe transform (generalization, redaction, suppression) | Attaches to the released artifact |
| `SensitivityTransform` | The transform operation itself (e.g., 1 km offset, cell aggregation, attribute drop) | Parameterized, reviewable, reversible only by re-promotion |
| `CulturalReview` | Cultural-authority / community review record | Holds release state where required |
| `StewardReview` | Domain-steward review record | Governs promotion and rollback |

> [!TIP]
> KFM terminology is preserved exactly. Do not paraphrase `EvidenceBundle` → "evidence package", `CandidateFeature` → "candidate site", or `SensitivityTransform` → "redaction" in code, schemas, or release artifacts. Drift is filed in `docs/registers/DRIFT_REGISTER.md`.

[Back to top ↑](#archaeology-domain--architecture)

---

## 4. Lane layout

**PROPOSED** — Per Directory Rules §12 (Domain Placement Law), `archaeology` is a **lane** under each responsibility root, never a root folder. The tree below is **PROPOSED** until inspected against the mounted repo (`[DIRRULES]` §12).

### 4.1 Lane map (Mermaid)

```mermaid
flowchart LR
  classDef doctrine fill:#eef,stroke:#88a,color:#113
  classDef code fill:#efe,stroke:#7a7,color:#131
  classDef data fill:#fef,stroke:#a7a,color:#311
  classDef proof fill:#ffe,stroke:#aa7,color:#331

  subgraph DOC["docs/"]
    D1["docs/domains/archaeology/<br/>ARCHITECTURE.md (this file)"]:::doctrine
    D2["docs/runbooks/archaeology/<br/>PROMOTION · ROLLBACK · INTAKE"]:::doctrine
    D3["docs/adr/<br/>(archaeology-relevant ADRs)"]:::doctrine
  end

  subgraph DEFN["meaning + shape + admissibility"]
    C1["contracts/domains/archaeology/"]:::code
    S1["schemas/contracts/v1/domains/archaeology/"]:::code
    P1["policy/domains/archaeology/<br/>policy/sensitivity/archaeology/"]:::code
  end

  subgraph PROOF["enforcement"]
    T1["tests/domains/archaeology/"]:::proof
    F1["fixtures/domains/archaeology/"]:::proof
    V1["tools/validators/<br/>(shared, lane-aware)"]:::proof
  end

  subgraph RUN["runtime"]
    PK1["packages/domains/archaeology/"]:::code
    PL1["pipelines/domains/archaeology/<br/>pipeline_specs/archaeology/"]:::code
  end

  subgraph LIFE["lifecycle data"]
    R1["data/raw/archaeology/"]:::data
    W1["data/work/archaeology/<br/>data/quarantine/archaeology/"]:::data
    PR1["data/processed/archaeology/"]:::data
    CT1["data/catalog/domain/archaeology/<br/>data/triplets/...<br/>data/published/layers/archaeology/"]:::data
    REG1["data/registry/sources/archaeology/"]:::data
  end

  subgraph REL["release"]
    RC1["release/candidates/archaeology/"]:::doctrine
    RM1["release/manifests/"]:::doctrine
    RB1["release/rollback_cards/"]:::doctrine
  end

  D1 --> DEFN
  DEFN --> PROOF
  DEFN --> RUN
  RUN --> LIFE
  LIFE --> REL
  REL --> RM1
```

### 4.2 Proposed lane paths

**PROPOSED — every path is governed by Directory Rules §12; none is asserted as present.**

<details>
<summary><strong>Show / hide the full proposed path list</strong></summary>

```text
docs/domains/archaeology/
contracts/domains/archaeology/
schemas/contracts/v1/domains/archaeology/
policy/domains/archaeology/
policy/sensitivity/archaeology/
tests/domains/archaeology/
fixtures/domains/archaeology/
packages/domains/archaeology/
pipelines/domains/archaeology/
pipeline_specs/archaeology/
data/raw/archaeology/
data/work/archaeology/
data/quarantine/archaeology/
data/processed/archaeology/
data/catalog/domain/archaeology/
data/published/layers/archaeology/
data/registry/sources/archaeology/
release/candidates/archaeology/
docs/runbooks/archaeology/
```

</details>

### 4.3 Authority split (cross-reference)

| Layer | Owns | Does **not** own |
|---|---|---|
| `contracts/` | Object meaning (Markdown) — what `ArchaeologicalSite` *is* | Machine validation, admissibility |
| `schemas/` | Machine-checkable shape (JSON Schema, JSON-LD context) | Object meaning, allow/deny |
| `policy/` | Admissibility, allow / deny / restrict / abstain | Object meaning, shape |
| `tests/` + `fixtures/` | Proof that contracts, schemas, and policy are enforceable | Source of canonical decision |

This split is doctrinal (`[DIRRULES]` §6.3–6.5). Schemas live under `schemas/contracts/v1/...` per ADR-0001; any divergence between `contracts/<x>.schema.json` and `schemas/contracts/v1/...` is **drift** and must be migrated.

[Back to top ↑](#archaeology-domain--architecture)

---

## 5. Canonical object families

**CONFIRMED doctrine / PROPOSED implementation** — Identity is deterministic: `source_id + object_role + temporal_scope + normalized_digest`. Source, observed, valid, retrieval, release, and correction times stay distinct where material (`[DOM-ARCH]` §E).

| Object family | Purpose | Identity rule | Sensitivity default |
|---|---|---|---|
| `ArchaeologicalSite` | Confirmed cultural / archaeological location | PROPOSED deterministic basis (see above) | **Exact geometry denied** by default |
| `SiteComponent` | Sub-element of a site | Inherits parent identity scope | Inherits parent sensitivity |
| `Survey` / `SurveyProject` | Authorized survey activity | Project identifier + steward authority + temporal scope | Coverage generalizable; raw transect restricted |
| `SurveyTransect` | Spatial unit within a SurveyProject | Project + transect index + geometry digest | Restricted by default |
| `ExcavationUnit` | Controlled excavation locus | Project + unit identifier + temporal scope | Access-controlled |
| `Artifact` / `ArtifactRecord` | Catalogued artifact | Repository + accession + catalog identifier | Collection-rights review required |
| `Feature` | In-context cultural feature | Parent site / unit + feature identifier | Inherits parent sensitivity |
| `Context` / `ProvenienceContext` | Spatial / stratigraphic placement | Excavation unit + stratigraphic unit | Required for interpretive chronology |
| `StratigraphicUnit` | Discrete depositional / disturbance unit | Excavation unit + unit identifier | Required; access-controlled |
| `RemoteSensingAnomaly` | Anomaly from imagery, multispectral, etc. | Source acquisition + geometry digest | **Not a site**; quarantine until reviewed |
| `LiDARCandidate` | LiDAR-derived candidate feature | Acquisition + footprint + geometry digest | **Not a site**; quarantine until reviewed |
| `GeophysicsObservation` | Magnetometry, GPR, resistivity record | Acquisition + grid + measurement profile | Source-rights bounded |
| `ThreeDDocumentation` | 3D site / object models | Acquisition method + processing receipt | Access-controlled; reality-boundary note required |
| `CollectionAccession` | Museum / repository accession | Repository + accession identifier | Rights bounded |
| `ChronologyAssertion` | Period / phase / absolute-date claim | Source + method + scope | Cite-or-abstain |
| `CulturalReview` | Cultural-authority review record | Subject + reviewer authority + decision time | Required for sensitive promotion |
| `StewardReview` | Domain-steward review record | Subject + steward + decision time | Required for promotion |
| `SensitivityTransform` | Public-safe transform operation | Method + parameters + input digest | Receipts retained |
| `PublicationTransformReceipt` | Audit record of public-safe transform | SensitivityTransform + output digest | Attached to released artifact |
| `CandidateFeature` | Pre-review candidate (LiDAR / RS / geophys) | Source + acquisition + geometry digest | **Public DENY** until promoted |

[Back to top ↑](#archaeology-domain--architecture)

---

## 6. Source families and source roles

### 6.1 Source families (CONFIRMED domain doctrine / NEEDS VERIFICATION rights & cadence per source)

| Source family | Role(s) (`source_role`) | Rights / sensitivity | Status |
|---|---|---|---|
| State site inventory / SHPO or equivalent | `authority` / `observation` / `context` | NEEDS VERIFICATION; sensitive joins fail closed | `[DOM-ARCH]` `[ENCY]` |
| Public NRHP-like listings | `authority` / `context` | NEEDS VERIFICATION | `[DOM-ARCH]` `[ENCY]` |
| Field survey forms | `observation` | NEEDS VERIFICATION; restricted by default | `[DOM-ARCH]` `[ENCY]` |
| Excavation records and provenience packets | `observation` / `context` | NEEDS VERIFICATION; restricted | `[DOM-ARCH]` `[ENCY]` |
| Artifact / collection / repository records | `observation` / `context` | NEEDS VERIFICATION; rights bounded | `[DOM-ARCH]` `[ENCY]` |
| Lab reports (dating, residue, materials) | `observation` / `model` | NEEDS VERIFICATION; method receipts required | `[DOM-ARCH]` `[ENCY]` |
| Historic maps / plats / land records / newspapers | `context` | NEEDS VERIFICATION; vintage-specific | `[DOM-ARCH]` `[ENCY]` |
| Oral history and cultural knowledge | `authority` (cultural) / `context` | NEEDS VERIFICATION; **steward / community protocol required** | `[DOM-ARCH]` `[ENCY]` |
| LiDAR / remote sensing / geophysics (per `[ENCY]` §7.13) | `observation` (candidate-producing) | NEEDS VERIFICATION; generalized public outputs only | `[ENCY]` §7.13.B |

### 6.2 Source-role vocabulary (PROPOSED — pending ADR; cross-cutting)

**CONFIRMED / PROPOSED** — `source_role` is a `SourceDescriptor` field with the enum below (`[ENCY]` §24.1.3). Its canonical schema home defaults to `schemas/contracts/v1/source/source_descriptor.json` per ADR-0001 (`[DIRRULES]` §7.4).

| `source_role` value | Meaning | Archaeology-lane behavior |
|---|---|---|
| `observed` | Direct measurement / survey / observation | May feed `Feature`, `Artifact`, `ExcavationUnit` evidence |
| `regulatory` | Authority designation (e.g., NRHP listing) | Listing ≠ site evidence; preserve role |
| `modeled` | Derived from a model (e.g., predictive surface) | Always carries `role_model_run_ref`; never a confirmed site |
| `aggregate` | Spatial / temporal aggregation | Geometry-scope guard; matrix-cell semantics |
| `administrative` | Compiled / collated record | Role-tag preserved; not promoted to observed event |
| `candidate` | Pre-review LiDAR / RS / geophysics anomaly | `role_candidate_disposition` ∈ {pending, merged, rejected, quarantined}; **PUBLISHED edge forbidden until merged** |
| `synthetic` | Modeled or generated representation | `role_synthetic_basis` + Reality Boundary Note required |

> [!IMPORTANT]
> Source role cannot be inferred from convenience. A LiDAR anomaly is `candidate`, not `observed`, until a `CulturalReview` and `StewardReview` promote it. (`[ENCY]` §24.1; `[DOM-ARCH]` §K)

[Back to top ↑](#archaeology-domain--architecture)

---

## 7. Lifecycle and pipeline shape

### 7.1 Pipeline (Mermaid)

```mermaid
flowchart LR
  RAW["RAW<br/>SourceDescriptor exists<br/>rights · sensitivity · citation · time · hash"]
  WORK["WORK / QUARANTINE<br/>normalize schema, geometry, time,<br/>identity, evidence, rights, policy"]
  PROC["PROCESSED<br/>EvidenceRef · ValidationReport · digest closure<br/>public-safe candidates"]
  CAT["CATALOG / TRIPLET<br/>EvidenceBundle · graph projection<br/>release candidates"]
  PUB["PUBLISHED<br/>ReleaseManifest · correction path<br/>rollback target · review state"]

  RAW -->|"admission +<br/>source activation"| WORK
  WORK -->|"validation +<br/>policy gate pass"| PROC
  WORK -.->|"failure"| Q["quarantine<br/>(reason recorded)"]
  PROC -->|"catalog / proof closure"| CAT
  CAT -->|"governed promotion<br/>(steward + cultural review)"| PUB
  PUB -.->|"correction"| CN["CorrectionNotice"]
  PUB -.->|"rollback drill"| RB["RollbackCard"]

  classDef raw fill:#fee,stroke:#a77,color:#311
  classDef work fill:#feb,stroke:#a87,color:#321
  classDef proc fill:#eef,stroke:#77a,color:#113
  classDef cat fill:#efe,stroke:#7a7,color:#131
  classDef pub fill:#dfd,stroke:#5a5,color:#020
  class RAW raw
  class WORK,Q work
  class PROC proc
  class CAT cat
  class PUB,CN,RB pub
```

### 7.2 Stage handling and gates

**CONFIRMED doctrine / PROPOSED lane application** (`[DIRRULES]` §3 lifecycle invariant; `[DOM-ARCH]` §H):

| Stage | Handling | Gate | Status |
|---|---|---|---|
| **RAW** | Capture immutable source payload or reference with source role, rights, sensitivity, citation, time, and hash | `SourceDescriptor` exists | PROPOSED |
| **WORK / QUARANTINE** | Normalize schema, geometry, time, identity, evidence, rights, and policy; hold failures with a recorded quarantine reason | Validation **and** policy gate pass, or `quarantine_reason` recorded | PROPOSED |
| **PROCESSED** | Emit validated normalized objects, receipts, and public-safe candidates | `EvidenceRef` + `ValidationReport` + digest closure exist | PROPOSED |
| **CATALOG / TRIPLET** | Emit catalog records, `EvidenceBundle`s, graph / triplet projections, release candidates | Catalog / proof closure passes | PROPOSED |
| **PUBLISHED** | Serve released public-safe artifacts through governed APIs and manifests | `ReleaseManifest` + correction path + rollback target + review / policy state exist | PROPOSED |

> [!WARNING]
> **Watcher-as-non-publisher.** Connectors and watchers emit to `data/raw/archaeology/` or `data/quarantine/archaeology/` only. They **MUST NOT** write to `data/processed/`, `data/catalog/`, `data/published/`, or `release/`. Promotion is a governed state transition, never a file move. (`[DIRRULES]` §13.5)

[Back to top ↑](#archaeology-domain--architecture)

---

## 8. Sensitivity, rights, and publication posture

This is the **load-bearing section** of the Archaeology lane. Everything else inherits from it.

### 8.1 Deny-by-default register

**CONFIRMED** — From the cross-cutting sensitive / deny-by-default register (`[ENCY]` §13):

| Class | Examples | Default outcome | Required controls | Source |
|---|---|---|---|---|
| **Archaeology — site coordinates** | Burial / sacred / culturally sensitive materials | **DENY exact public location by default** | Cultural / steward review · suppression / generalization · `SensitivityTransform` + `PublicationTransformReceipt` | `SRC-ARCH` |
| **Sacred / culturally sensitive places** | Oral history, cultural routes, sacred sites | **DENY until steward review and access class approve** | Consultation record · `SensitivityTransform` | `SRC-ARCH`, `SRC-ROAD` |
| **Source-rights-limited records** | Licensed, restricted, no-redistribution, uncertain terms | **DENY public release until terms resolved** | Rights register · attribution · no public derivative if barred | `SRC-BUILD` |
| **Exact sensitive locations** | Any exact point that increases harm risk | **DENY by default** | Redaction / generalization · audit | `SRC-DIR` |

### 8.2 Closing rule (CONFIRMED)

> [!CAUTION]
> Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state **blocks** public promotion. The safe state is quarantine, denial, restriction, or abstention until rights, source role, access conditions, cadence, and release class are recorded. (`[ENCY]`; `[DIRRULES]`; Unified Build Manual §§8, 18–19)

### 8.3 Public viewing products (PROPOSED)

**PROPOSED — derived from `[DOM-ARCH]` §G**:

- Public generalized site summaries
- Public survey-coverage summaries (geometry generalized, raw transects withheld)
- Candidate-feature surfaces (clearly labeled, **never** as confirmed sites)
- Remote-sensing anomaly surfaces (generalized, candidate-tagged)
- Steward-only review maps (restricted; not on public surfaces)
- Restricted exact-geometry review (steward / authorized researchers only)
- Chronology / context views (period-level, source-tagged)
- Threat / risk review views (with exact-site denial)

**CONFIRMED cross-cutting viewing products** (`[MAP-MASTER]`; `[GAI]`): Evidence Drawer · time-aware state · trust badges · sensitivity-redacted view · correction / stale-state view · governed Focus Mode.

### 8.4 Sensitivity transform contract (PROPOSED)

Every public release of an archaeology-derived artifact **MUST** carry a `PublicationTransformReceipt` that records:

- the input digest (canonical, hashed)
- the `SensitivityTransform` method and parameters
- the output digest
- the cultural / steward review reference
- the policy decision reference
- the rights basis

A release without a matching `PublicationTransformReceipt` **MUST** fail at the `policy/promotion/` gate.

[Back to top ↑](#archaeology-domain--architecture)

---

## 9. Cross-lane relations

### 9.1 Inbound and outbound relations (CONFIRMED / PROPOSED)

From `[DOM-ARCH]` §F and `[DOM-ARCH-ATLAS]` §24.4.13. Every relation **must** preserve ownership, source role, sensitivity, and `EvidenceBundle` support:

| This domain | Related lane | Relation | Constraint |
|---|---|---|---|
| Archaeology | Spatial Foundation | Exact / public geometry split and transform receipts | Public surface receives generalized geometry only |
| Archaeology | Roads / Rail | Historic routes and cultural paths | Site coords denied; cultural routes steward-reviewed |
| Archaeology | Settlements | Forts, missions, townsites, reservation communities | Cultural temporal period bounds settlement interpretation; site coords denied |
| Archaeology | Hazards | Threat, erosion, fire, flood, exposure context | Exact-site denial preserved through hazard surfaces |
| Archaeology | Planetary / 3D | Generalized 3D representation | Admitted only with steward review + reality-boundary note |
| Archaeology | People / Genealogy / DNA / Land | Cultural affiliations | Cited with rights, sovereignty, and steward review |

### 9.2 Relation map (Mermaid)

```mermaid
flowchart TB
  ARCH(("Archaeology<br/>(sensitive lane)"))
  SF["Spatial Foundation"]
  RR["Roads · Rail · Trade"]
  ST["Settlements · Infrastructure"]
  HZ["Hazards"]
  P3D["Planetary · 3D"]
  PPL["People · Genealogy · DNA · Land"]
  GEO["Geology"]

  SF -- "generalized geometry +<br/>transform receipt" --> ARCH
  RR -- "historic routes<br/>(site coords denied)" --> ARCH
  ST -- "fort/mission/townsite context" --> ARCH
  HZ -- "exposure context<br/>(exact-site denial)" --> ARCH
  GEO -- "subsurface context" --> ARCH

  ARCH -- "cultural temporal period<br/>(bounds interpretation)" --> ST
  ARCH -- "generalized 3D +<br/>reality-boundary note" --> P3D
  ARCH -- "cultural affiliation<br/>(rights + sovereignty review)" --> PPL

  classDef sensitive fill:#fee,stroke:#a44,color:#411,stroke-width:2px
  classDef neighbor fill:#eef,stroke:#77a,color:#113
  class ARCH sensitive
  class SF,RR,ST,HZ,P3D,PPL,GEO neighbor
```

[Back to top ↑](#archaeology-domain--architecture)

---

## 10. Governed API surfaces and finite outcomes

### 10.1 Surfaces (PROPOSED; exact routes UNKNOWN until verified)

Every Archaeology API surface returns a **finite outcome** from KFM's outcome envelope (`[GAI]` §24.3; `[DOM-ARCH]` §J):

| Surface | DTO / artifact | Finite outcomes | Status |
|---|---|---|---|
| Archaeology feature / detail resolver | `ArchaeologyDecisionEnvelope` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED governed API surface; exact route UNKNOWN |
| Archaeology layer manifest resolver | `LayerManifest` / domain layer descriptor | `ANSWER` / `DENY` / `ERROR` | PROPOSED; public-safe release only |
| Evidence Drawer payload | `EvidenceDrawerPayload` + `EvidenceBundle` projection | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; evidence and policy filtered |
| Focus Mode answer | `RuntimeResponseEnvelope` + `AIReceipt` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; AI never root truth |
| Correction submit | `CorrectionNoticeCandidate` | `ACCEPTED` / `DENY` / `ERROR` | PROPOSED |
| Review decision | `ReviewRecord` | `ALLOW` / `RESTRICT` / `DENY` / `ERROR` | PROPOSED |

### 10.2 Outcome semantics (CONFIRMED doctrine)

| Outcome | When |
|---|---|
| `ANSWER` | Evidence sufficient · policy permits · release state allows · review state (if required) recorded |
| `ABSTAIN` | Evidence insufficient / incomplete · AI cannot cite · stale with no released alternative |
| `DENY` | Policy, rights, sensitivity, or release state forbids. **Sensitive lanes default here.** |
| `ERROR` | Missing schema, malformed query, contract violation, infrastructure failure |
| `HOLD` | Promotion / release / correction paused pending steward, rights-holder, or policy review |
| `PASS` / `FAIL` | Validator-class outcomes; internal to admission and promotion gates |

> [!NOTE]
> **Trust membrane.** Public clients and normal UI surfaces consume `apps/governed-api/` only. They **MUST NOT** read `data/processed/`, `data/catalog/`, or `data/published/` directly. (`[DIRRULES]` §7.1)

[Back to top ↑](#archaeology-domain--architecture)

---

## 11. Governed AI behavior

**CONFIRMED doctrine / PROPOSED implementation** (`[GAI]`; `[DOM-ARCH]` §L):

| AI behavior | Rule |
|---|---|
| **Permitted** | Summarize released Archaeology `EvidenceBundle`s · compare evidence across released artifacts · explain limitations and uncertainty · draft `StewardReview` notes for human approval |
| **Required abstention** | `ABSTAIN` when `EvidenceBundle` is missing, citations cannot be validated, source roles conflict, temporal scope is insufficient, or the user asks for unsupported inference |
| **Required denial** | `DENY` direct RAW / WORK / QUARANTINE access · sensitive-location exposure · uncited authoritative claims · emergency-alert replacement · exact-site geometry exposure |
| **Receipt** | Emit `AIReceipt` and `RuntimeResponseEnvelope` with `outcome`, `evidence_refs`, `policy_decision`, and `citation_validation` |

> [!IMPORTANT]
> AI text is **never** evidence. AI surfaces consume released `EvidenceBundle`s; they do not author them. The Atlas v1.1 anti-pattern register explicitly flags **"synthetic content presented as observed reality"** and **"AI text treated as evidence"** as `DENY` cases for the Archaeology lane. (`[ENCY]` §24.1)

[Back to top ↑](#archaeology-domain--architecture)

---

## 12. Validators, tests, and fixtures

**PROPOSED test families** (`[DOM-ARCH]` §K; cross-cutting `[ENCY]`):

- **EvidenceBundle-required tests** — every public Archaeology claim must resolve `EvidenceRef → EvidenceBundle`
- **Candidate-not-site tests** — `CandidateFeature` and `LiDARCandidate` **MUST NOT** appear on public surfaces as a confirmed `ArchaeologicalSite`
- **Public no-leak tests** — no exact site geometry, burial / sacred attributes, or oral-history payload reaches a public surface without an explicit, reviewed `PublicationTransformReceipt`
- **Rights and cultural-review tests** — releases lacking `CulturalReview` (where required) or rights basis fail at the promotion gate
- **Exact sensitive geometry denial** — explicit `DENY` fixtures for exact-site, burial, sacred, and oral-history geometry
- **Catalog closure tests** — `EvidenceBundle`, `ValidationReport`, and digest closure exist before catalog promotion
- **AI exact-location denial** — Focus Mode and Evidence Drawer surfaces deny exact-site coordinates regardless of phrasing
- **Stale-state handling** — released artifacts past freshness thresholds are flagged or rolled back, not silently served
- **Rollback drill** — `RollbackCard` produces a verifiable rollback target before any sensitive release

Cross-cutting test surfaces (CONFIRMED): schema validation · source-descriptor validation · rights validation · sensitivity validation · evidence closure · temporal logic · geometry validity · policy deny tests · citation validation · release-manifest validation · no-network fixtures · non-regression tests.

> [!TIP]
> Validators live under `tools/validators/` (canonical) and are exercised by `tests/domains/archaeology/`. A validator that lives only in a test file is an anti-pattern (`[DIRRULES]` §13.5).

[Back to top ↑](#archaeology-domain--architecture)

---

## 13. Publication, correction, and rollback

**CONFIRMED doctrine / PROPOSED implementation** (`[ENCY]` Appendix E; `[DOM-ARCH]` §M):

Every Archaeology publication **MUST** carry the following before crossing the trust membrane to a public surface:

1. **`ReleaseManifest`** — the published artifact set with digests, policy posture, and rollback target
2. **`EvidenceBundle`** — resolved evidence with source, provenance, scope, citation, and review context
3. **`ValidationReport`** + policy support — schema, rights, sensitivity, evidence closure
4. **Review state** — `CulturalReview` (where required), `StewardReview`, and any rights-holder consultation record
5. **Correction path** — `CorrectionNotice` route exists; users can submit corrections; releases reachable for tombstoning
6. **Stale-state rule** — freshness threshold and stale-state handling are declared
7. **Rollback target** — `RollbackCard` produced; rollback drill verifies the path

> [!CAUTION]
> Separation of duties applies. The same actor **SHOULD NOT** simultaneously author content, approve cultural / steward review, and authorize release. The release authority, sensitivity reviewer, and domain steward are distinct roles. (`[DIRRULES]` §16; `[ENCY]`)

[Back to top ↑](#archaeology-domain--architecture)

---

## 14. Verification backlog

**NEEDS VERIFICATION** — items this document cannot resolve without mounted-repo evidence, fixtures, manifests, logs, or accepted ADRs (`[DOM-ARCH]` §N):

<details>
<summary><strong>Show / hide the verification backlog</strong></summary>

- [ ] **Steward authority and confidentiality.** Who holds `StewardReview` authority for each `SourceDescriptor` family? What confidentiality contract binds reviewers?
- [ ] **Public geometry thresholds and transform profiles.** Define generalization radius, cell-aggregation buckets, attribute-drop policies, and the per-class `SensitivityTransform` profiles.
- [ ] **Oral history / cultural knowledge protocol.** Codify the consultation, consent, attribution, and revocation flow before any oral-history payload approaches a public surface.
- [ ] **Emergency public-layer disablement and rollback drill.** Verify a reversible kill-switch path for archaeology layers and a periodic rollback drill cadence.
- [ ] **Schema home decision.** Confirm canonical schema home is `schemas/contracts/v1/domains/archaeology/` per ADR-0001, or open an ADR if drift is found.
- [ ] **Single-file vs folder pattern.** Decide whether `docs/domains/<domain>/ARCHITECTURE.md` (single file, as here) or `docs/domains/<domain>/architecture/` (folder) is the cross-domain convention; apply uniformly.
- [ ] **Source endpoints, cadence, rights.** Verify endpoints, freshness, redistribution terms, and sensitivity flags for every source family in §6.1.
- [ ] **Governed API framework.** Confirm framework, routing convention, DTO style, and the canonical route for Archaeology surfaces.
- [ ] **Policy engine.** Confirm OPA / Conftest availability and parity-test approach for `policy/domains/archaeology/` and `policy/sensitivity/archaeology/`.
- [ ] **CI conventions.** Confirm `.github/workflows/` pattern before introducing `archaeology-ci.yml`, `archaeology-promotion.yml`, etc.
- [ ] **Owners.** Replace `TODO — Archaeology domain steward · Sensitivity reviewer · Cultural/sovereignty review liaison` placeholders with grounded owners and CODEOWNERS entries.
- [ ] **Repo state.** No claim in this document about path presence, route existence, schema URI, test coverage, or release maturity is verified against the live repo.

</details>

[Back to top ↑](#archaeology-domain--architecture)

---

## 15. Open ADRs and questions

**OPEN — ADRs likely required before stable promotion of this lane:**

| Proposed ADR | Question | Citation basis |
|---|---|---|
| `ADR-archaeology-schema-home` | Confirm `schemas/contracts/v1/domains/archaeology/` as canonical | `[DIRRULES]` §7.4 |
| `ADR-archaeology-source-roles` | Lock the source-role enum for the Archaeology lane (cross-reference §24.1.3) | `[ENCY]` §24.1.3 |
| `ADR-archaeology-sensitivity-policy` | Define exact-internal vs public-safe geometry thresholds, precision buckets, and `SensitivityTransform` parameter library | `[DOM-ARCH]` §I; `[ENCY]` §13 |
| `ADR-archaeology-cultural-review-protocol` | Codify cultural / community / steward review obligations, consent, and revocation | `[DOM-ARCH]` §B; `[ENCY]` §7.13 |
| `ADR-archaeology-public-layer-strategy` | Define the MapLibre public layer set, generalization method, candidate-vs-confirmed UX, and freshness chips | `[DOM-ARCH]` §G; `[MAP-MASTER]` |
| `ADR-archaeology-3d-admission-policy` | Constrain `ThreeDDocumentation` admission to the public path (reality-boundary note, generalized representation) | `[ENCY]` §24.4.13; `[MAP-MASTER]` |
| `ADR-domain-architecture-doc-pattern` | Decide single-file `ARCHITECTURE.md` vs `architecture/` folder uniformly across all domain lanes | cross-domain |

[Back to top ↑](#archaeology-domain--architecture)

---

## 16. Related docs

<details>
<summary><strong>Lane companions, doctrine, ADRs, and runbooks (PROPOSED paths)</strong></summary>

- **Lane companions** (PROPOSED): [`README.md`](README.md) · `CURRENT_STATE.md` · `SOURCE_REGISTRY.md` · `DATA_MODEL.md` · `PIPELINES_AND_LIFECYCLE.md` · `PUBLICATION_AND_POLICY.md` · `UI_AND_EVIDENCE_DRAWER.md` · `VERIFICATION_BACKLOG.md` · `CHANGELOG.md` · `ROADMAP.md` · `GLOSSARY.md`
- **Doctrine roots**: [`../../doctrine/`](../../doctrine/) · [`../../doctrine/directory-rules.md`](../../doctrine/directory-rules.md) · [`../../doctrine/lifecycle-law.md`](../../doctrine/lifecycle-law.md) · [`../../doctrine/trust-membrane.md`](../../doctrine/trust-membrane.md) · [`../../doctrine/truth-posture.md`](../../doctrine/truth-posture.md)
- **Architecture neighbors**: [`../../architecture/governed-api.md`](../../architecture/governed-api.md) · [`../../architecture/contract-schema-policy-split.md`](../../architecture/contract-schema-policy-split.md) · [`../../architecture/map-shell.md`](../../architecture/map-shell.md)
- **Runbooks** (PROPOSED, partly drafted): [`../../runbooks/archaeology/PROMOTION_RUNBOOK.md`](../../runbooks/archaeology/PROMOTION_RUNBOOK.md) · [`../../runbooks/archaeology/ROLLBACK_RUNBOOK.md`](../../runbooks/archaeology/ROLLBACK_RUNBOOK.md)
- **Cross-domain neighbors**: [`../settlements-infrastructure/ARCHITECTURE.md`](../settlements-infrastructure/ARCHITECTURE.md) · [`../people-dna-land/ARCHITECTURE.md`](../people-dna-land/ARCHITECTURE.md) · [`../roads-rail-trade/ARCHITECTURE.md`](../roads-rail-trade/ARCHITECTURE.md) · [`../hazards/ARCHITECTURE.md`](../hazards/ARCHITECTURE.md) · [`../geology/ARCHITECTURE.md`](../geology/ARCHITECTURE.md)
- **ADRs (proposed)**: [`../../adr/`](../../adr/) — see §15
- **Registers**: [`../../registers/AUTHORITY_LADDER.md`](../../registers/AUTHORITY_LADDER.md) · [`../../registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) · [`../../registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md)

</details>

[Back to top ↑](#archaeology-domain--architecture)

---

<sub>Authority basis: `[ENCY]` §7.13 · `[DOM-ARCH]` · `[DIRRULES]` §12 · `[GAI]` §24.3 · `[MAP-MASTER]`. Every implementation path is PROPOSED until verified against mounted-repo evidence; doctrine is CONFIRMED. Last reviewed: 2026-05-15.</sub>

[Back to top ↑](#archaeology-domain--architecture)
