<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/geology-sublane-bedrock-geology
title: Geology Sublane — Bedrock Geology
type: standard
version: v1
status: draft
owners: <geology-domain-steward> (placeholder — verify against repo CODEOWNERS)
created: 2026-06-03
updated: 2026-06-03
policy_label: public
related:
  - docs/domains/geology/README.md                      # PROPOSED — verify presence
  - docs/domains/geology/sublanes/surficial_geology.md  # PROPOSED sibling
  - docs/domains/geology/sublanes/structures.md         # PROPOSED sibling
  - docs/domains/geology/sublanes/stratigraphy.md       # PROPOSED sibling
  - docs/domains/geology/sublanes/boreholes_wells.md    # PROPOSED sibling
  - docs/domains/geology/sublanes/resources.md          # PROPOSED sibling
  - docs/domains/hydrology/                             # cross-lane: hydrostratigraphy
  - docs/domains/soil/                                  # cross-lane: parent material
  - docs/domains/hazards/                               # cross-lane: fault / subsidence context
  - schemas/contracts/v1/domains/geology/               # PROPOSED schema home (ADR-0001 default)
  - contracts/domains/geology/                          # PROPOSED semantic contract home
  - policy/domains/geology/                              # PROPOSED policy home
  - data/published/layers/geology/                      # PROPOSED layer outputs
  - ai-build-operating-contract.md                      # canonical operating contract
  - directory-rules.md                                  # §12 Domain Placement Law, §5 Canonical Root Tree
  - docs/registers/DRIFT_REGISTER.md                    # filename + sublane-folder routing
tags: [kfm, geology, bedrock, lithostratigraphy, sublane]
notes:
  - "CONTRACT_VERSION = 3.0.0 pinned per ai-build-operating-contract.md."
  - "Filename uses bedrock_geology.md per the requested path. A sibling doc named bedrock.md may also exist; the two MUST NOT both become canonical. Surface as a naming question in DRIFT_REGISTER (see Open Questions OQ-GEOL-BEDROCK-06)."
  - "Object-family names follow Atlas v1.1 Ch. 10C/E canonical casing (StructureFeature, SurficialUnit, etc.). FaultStructure is NOT used (it is drift)."
  - "The docs/domains/<domain>/sublanes/<sublane>.md path is PROPOSED. Directory Rules §12 establishes the responsibility-root lane pattern and shows docs/domains/<domain>/ as a directory, but does not enumerate a sublanes/ subfolder. Resolve via ADR before this layout is treated as canon."
  - "Owners, CI badge URLs, route names, and exact related-doc paths are placeholders pending mounted-repo verification."
[/KFM_META_BLOCK_V2] -->

# 🪨 Geology Sublane — Bedrock Geology

> Governance, semantics, and publication posture for **bedrock geology** inside the KFM Geology / Natural Resources domain lane. *Bedrock* here means consolidated rock units — formations, members, groups, lithologies, ages, contacts, and bedrock-expressed structures — as distinct from the surficial sublane, which owns unconsolidated cover.

[![Status](https://img.shields.io/badge/status-draft-yellow)](#)
[![Authority](https://img.shields.io/badge/authority-doctrine%20CONFIRMED%20%2F%20paths%20PROPOSED-blue)](#)
[![Contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-blueviolet)](#)
[![Policy](https://img.shields.io/badge/policy-public%20when%20generalized-green)](#)
[![Sensitivity](https://img.shields.io/badge/tier-T0%2FT1%20bedrock%20%C2%B7%20T2--T4%20siblings-orange)](#)
[![Lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-lightgrey)](#)
[![Build](https://img.shields.io/badge/CI-TODO-lightgrey)](#)
[![Updated](https://img.shields.io/badge/updated-2026--06--03-informational)](#)

**Status:** draft · **Owners:** `<geology-domain-steward>` *(placeholder)* · **Contract:** `CONTRACT_VERSION = "3.0.0"` · **Last updated:** 2026-06-03

> [!IMPORTANT]
> **Sublane folder is PROPOSED.** Directory Rules **§12 (Domain Placement Law)** establishes the lane pattern and shows `docs/domains/<domain>/` as a directory, but it does **not** enumerate a `sublanes/` subfolder. The path used here — `docs/domains/geology/sublanes/bedrock_geology.md` — should be confirmed by an ADR or migrated to a flat-prefix scheme (for example `docs/domains/geology/SUBLANE-BEDROCK.md`) before the structure is treated as canonical. See [§13 — Open Questions](#13--open-questions) and the [Open Questions Register](#open-questions-register).

> [!NOTE]
> **Filename note.** This file is `bedrock_geology.md`. If a sibling `bedrock.md` also exists in the same folder, the two are competing homes for one responsibility and MUST be reconciled — only one can be canonical. Routed to `docs/registers/DRIFT_REGISTER.md` (OQ-GEOL-BEDROCK-06).

---

## Mini-TOC

- [1 · Scope](#1--scope)
- [2 · Repo Fit](#2--repo-fit)
- [3 · Inputs](#3--inputs)
- [4 · Exclusions](#4--exclusions)
- [5 · Sublane Map (Mermaid)](#5--sublane-map-mermaid)
- [6 · Object Families & Ubiquitous Language](#6--object-families--ubiquitous-language)
- [7 · Source Families & Source Roles](#7--source-families--source-roles)
- [8 · Spatial & Temporal Model](#8--spatial--temporal-model)
- [9 · Map & Viewing Products](#9--map--viewing-products)
- [10 · Pipeline Shape (RAW → PUBLISHED)](#10--pipeline-shape-raw--published)
- [11 · API, Contract & Schema Surfaces](#11--api-contract--schema-surfaces)
- [12 · Sensitivity, Rights, and Publication Posture](#12--sensitivity-rights-and-publication-posture)
- [13 · Open Questions](#13--open-questions)
- [Companion sections](#open-questions-register)
- [Related Docs](#related-docs)

---

## 1 · Scope

**CONFIRMED doctrine / PROPOSED sublane scope.** The bedrock sublane governs the **consolidated-rock surface and subsurface fabric** of the Geology / Natural Resources lane:

- **Lithostratigraphic units** (formations, members, groups) carried as `GeologicUnit` instances typed to consolidated rock, and their map polygons.
- **`Lithology`** descriptors associated with bedrock units (limestone, shale, sandstone, evaporite, etc.).
- **`StratigraphicInterval`** assignments (formal lithostratigraphic intervals referenced by a unit) and **`StratigraphicCorrelation`** assertions across units.
- **`GeologicAge`** (chronostratigraphic age — period / epoch / stage) attached to bedrock units.
- **Bedrock-expressed `StructureFeature`** (faults, folds, contacts) where carried as part of a bedrock map.
- **`CrossSection`** interpretations through bedrock units.
- **`GeologyBoundaryVersion`** — the *interpretation version* and uncertainty attached to a bedrock map.
- Public-safe, generalized **bedrock unit map** delivery.

Doctrine basis: the Geology lane explicitly owns **bedrock/surficial geology, stratigraphy, lithology, structures, geomorphology** and associated subsurface/observational context, and pairs **polygons for units, lines for structures/cross-sections, points for boreholes/samples** (Atlas v1.1 §10A–B; ENCY §7.8).

> [!NOTE]
> "Bedrock" here is a **map sublane**, not a separate bounded context. It reuses the Geology lane's canonical object families with semantics narrowed to **consolidated rock**. `SurficialUnit`, `BoreholeReference`, `Well LogReference`, `Geochemistry SampleReference`, `Mineral Occurrence`, `Resource Deposit`, `ResourceEstimate`, and `Extraction Site` remain in their own sublanes when they exist.

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## 2 · Repo Fit

**PROPOSED placement.** This file lives under the Geology lane segment of the `docs/` responsibility root.

```text
docs/
└── domains/
    └── geology/
        ├── README.md                   # PROPOSED — domain landing
        └── sublanes/                   # PROPOSED — see §13 Open Questions
            ├── bedrock_geology.md      # <— THIS FILE
            ├── surficial_geology.md    # PROPOSED sibling
            ├── stratigraphy.md         # PROPOSED sibling
            ├── structures.md           # PROPOSED sibling
            ├── boreholes_wells.md      # PROPOSED sibling
            ├── geophysics.md           # PROPOSED sibling
            ├── geochemistry.md         # PROPOSED sibling
            └── resources.md            # PROPOSED sibling (mineral/resource/extraction/reclamation)
```

**Directory Rules basis (CONFIRMED against `directory-rules.md`):**

- **§12 Domain Placement Law** — geology is a **lane segment** inside responsibility roots, never a root folder. The example lane uses `docs/domains/<domain>/` as a directory; the `sublanes/` child is an *extension* of that pattern and is **not yet enumerated** in §12.
- **§5 Canonical Root Tree** — `docs/` is the human-facing control-plane root.
- **§4 Placement Protocol (Step 3)** — domain is a segment inside a responsibility root, named in the PR.
- **§13.1 / ADR-0001** — `schemas/contracts/v1/...` is the canonical schema home; `contracts/` retains semantic Markdown only.

**Upstream (doctrine that governs this file):**

- `directory-rules.md` — §12 Domain Placement Law, §5 Canonical Root Tree, §4 Placement Protocol (CONFIRMED).
- `ai-build-operating-contract.md` — canonical operating contract, `CONTRACT_VERSION = "3.0.0"` (CONFIRMED).
- `docs/domains/geology/README.md` — Geology lane charter (PROPOSED; verify presence).
- Atlas v1.1 Ch. 10 — Geology / Natural Resources (CONFIRMED doctrine).
- `kfm_encyclopedia.pdf` §7.8 — Geology and Natural Resources (CONFIRMED doctrine).

**Downstream (artifacts that consume this sublane's semantics):**

- `contracts/domains/geology/` — semantic Markdown contracts for `GeologicUnit`, `StratigraphicInterval`, etc. **(PROPOSED home)**
- `schemas/contracts/v1/domains/geology/` — JSON Schemas per ADR-0001 default. **(PROPOSED home)**
- `policy/domains/geology/` — admissibility and release rules for bedrock layers. **(PROPOSED home)**
- `tests/domains/geology/` and `fixtures/domains/geology/` — bedrock-specific test fixtures. **(PROPOSED home)**
- `data/published/layers/geology/` — released bedrock layer manifests. **(PROPOSED home)**
- `pipeline_specs/geology/` — bedrock ingestion / normalization pipeline specs. **(PROPOSED home)**

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## 3 · Inputs

Material that **belongs** in or is referenced by this sublane:

- **Bedrock map data** from the Kansas Geological Survey (KGS) and USGS — geologic map polygons (unit codes, lithology, age, source map).
- **Stratigraphic nomenclature** for Kansas bedrock (formation / member / group references).
- **Lithologic descriptions** attached to mapped units.
- **Structural overlays** (`StructureFeature`: faults, contacts) when delivered with a bedrock map.
- **Map metadata** — series, vintage, scale, attribution, license, interpretation version.
- **`CrossSection` interpretations** through bedrock units.
- **Generalization receipts** describing how exact polygon geometry was transformed to public-safe form.

> [!TIP]
> Inputs enter via the standard **`SourceDescriptor` → source-activation decision** path. A KGS bedrock map series is not implicitly active; it requires a recorded source role, license review, attribution, and a recorded activation decision before connectors emit to `data/raw/geology/`. *(The named outcome object `SourceActivationDecision` is PROPOSED — verify the exact term against `contracts/` before treating it as canonical.)*

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## 4 · Exclusions

Material that **does not** belong here, and where it goes instead:

| Out of scope for bedrock sublane | Lives in | Canonical object family |
|---|---|---|
| Unconsolidated / Quaternary cover units | `docs/domains/geology/sublanes/surficial_geology.md` *(PROPOSED)* | `SurficialUnit` |
| Borehole logs, well logs, core descriptions | `docs/domains/geology/sublanes/boreholes_wells.md` *(PROPOSED)* | `BoreholeReference`, `Well LogReference` |
| Geophysical surveys (seismic, gravity, magnetics) | `docs/domains/geology/sublanes/geophysics.md` *(PROPOSED)* | *(geophysics object family — verify)* |
| Geochemistry samples and assays | `docs/domains/geology/sublanes/geochemistry.md` *(PROPOSED)* | `Geochemistry SampleReference` |
| Mineral occurrences, resource deposits/estimates, extraction, reclamation | `docs/domains/geology/sublanes/resources.md` *(PROPOSED)* | `Mineral Occurrence`, `Resource Deposit`, `ResourceEstimate`, `Extraction Site` |
| Soil map units, components, horizons, properties | `docs/domains/soil/` (Soil lane) | `SoilMapUnit`, `SoilComponent`, … |
| Aquifer / hydrostratigraphic *measurements* | `docs/domains/hydrology/` (Geology contributes `Hydrostratigraphic Unit` context) | `Hydrostratigraphic Unit` (context only) |
| Hazard / risk assessment derived from bedrock structure | `docs/domains/hazards/` (Geology contributes context, not risk) | — |
| Mineral / lease ownership, title, operator records | `docs/domains/people-dna-land/` (Geology cannot prove ownership) | — |
| Cross-cutting governance (`EvidenceBundle`, `RunReceipt`, `ReleaseManifest` semantics) | `contracts/evidence/`, `contracts/runtime/`, `contracts/release/` *(PROPOSED homes)* | — |

> [!WARNING]
> **Anti-collapse.** A bedrock map polygon is **not** a verified exact unit outcrop, **not** a verified subsurface presence at depth, and **not** a resource estimate. Promotion across that boundary requires evidence, source-role discipline, and a release decision — not visual proximity on a map. This mirrors the Geology lane's explicit non-ownership of ownership / lease / permit / title claims (Atlas v1.1 §10B).

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## 5 · Sublane Map (Mermaid)

PROPOSED — illustrative; reflects doctrine relationships, not a verified runtime graph.

```mermaid
flowchart LR
  subgraph SRC["Sources (CONFIRMED families · Atlas v1.1 §10D)"]
    KGS["KGS data and maps<br/>bedrock map series"]
    KGSMAP["KGS surficial / geologic maps"]
    NGMDB["USGS NGMDB and GeMS"]
  end

  subgraph BEDROCK["Bedrock sublane (this doc)"]
    GU["GeologicUnit<br/>(bedrock-typed)"]
    LI["Lithology"]
    SI["StratigraphicInterval"]
    SC["StratigraphicCorrelation"]
    GA["GeologicAge"]
    SF["StructureFeature<br/>(bedrock-expressed)"]
    CS["CrossSection"]
    BV["GeologyBoundaryVersion"]
  end

  subgraph LIFECYCLE["KFM Lifecycle (CONFIRMED)"]
    RAW["data/raw/geology/"]
    WORK["data/work/<br/>quarantine/geology/"]
    PROC["data/processed/geology/"]
    CAT["data/catalog/domain/geology/"]
    PUB["data/published/layers/geology/"]
  end

  subgraph CROSS["Cross-lane relations (CONFIRMED doctrine · §10F)"]
    SOIL["Soil — parent material"]
    HYD["Hydrology — hydrostratigraphy"]
    HAZ["Hazards — fault context"]
  end

  KGS --> RAW
  KGSMAP --> RAW
  NGMDB --> RAW
  RAW --> WORK --> PROC --> CAT --> PUB

  BEDROCK -. semantics .-> PROC
  BEDROCK -. semantics .-> CAT
  PUB --> SOIL
  PUB --> HYD
  PUB --> HAZ

  classDef proposed fill:#fff8dc,stroke:#bfa040,color:#333;
  classDef confirmed fill:#e8f4ea,stroke:#2e7d32,color:#1b1b1b;
  class BEDROCK proposed;
  class SRC,LIFECYCLE,CROSS confirmed;
```

> [!NOTE]
> The lifecycle path `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED` is **CONFIRMED doctrine** (Directory Rules §0; Atlas v1.1 §1 Operating Law and §10H). The bedrock semantics overlay on this lifecycle; nothing in the sublane bypasses it.

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## 6 · Object Families & Ubiquitous Language

CONFIRMED terms (Atlas v1.1 §10C, §10E; cross-domain object-family spine §2.2); PROPOSED field realizations until the geology schema is mounted.

> [!CAUTION]
> **Casing and naming are load-bearing.** The Atlas uses **`StructureFeature`** (not `FaultStructure`), **`SurficialUnit`**, **`Geochemistry SampleReference`**, **`Well LogReference`**, **`Mineral Occurrence`**, **`Resource Deposit`**, and **`Extraction Site`** with these exact forms. Do not silently rename them to industry-generic equivalents.

| Term | Bedrock-sublane meaning | Identity (PROPOSED) | Citation |
|---|---|---|---|
| **`GeologicUnit`** | A consolidated-rock mapping unit (formation/member/group) as carried by a specific bedrock map series. | `source_id + object_role + temporal_scope + normalized_digest` | Atlas §10C/E; ENCY §7.8 |
| **`Lithology`** | The rock-type descriptor associated with a bedrock unit (e.g., limestone, shale, sandstone). | A **descriptor of** a `GeologicUnit`, not a free-standing object on a map. | Atlas §10C/E |
| **`StratigraphicInterval`** | A formal lithostratigraphic interval (formation/member/group) referenced by a unit. | Same as above. | Atlas §10C/E |
| **`StratigraphicCorrelation`** | A correlation assertion across mapped units; **interpretive** — never raised to canonical map fact without evidence. | Same as above. | Atlas §10C |
| **`GeologicAge`** | A chronostratigraphic age (period / epoch / stage) attached to a bedrock unit. | Vocabulary-bounded; tracked against the source map's age system. | Atlas §10B/C |
| **`StructureFeature`** | A structural feature delivered with the bedrock map (fault trace, fold, contact). | Same identity basis. | Atlas §10C/E |
| **`CrossSection`** | Interpretive section through bedrock units; carries its own evidence and interpretation version. | Same identity basis. | Atlas §10B/E; ENCY §7.8 |
| **`GeologyBoundaryVersion`** | Tracks **interpretation version and uncertainty** for a bedrock map. Each refit / rebound of a unit is a new version, not an overwrite. | Same identity basis. | Atlas §10C/E |

> [!IMPORTANT]
> A bedrock map polygon's identity is **bound to its source map series and vintage**, not to the rock itself. Re-mapping the same outcrop produces a new `GeologyBoundaryVersion`, not a correction of the prior unit's truth value.

<details>
<summary><b>Geology lane object families not owned by the bedrock sublane</b></summary>

These belong to sibling sublanes. Listed here for terminology fidelity (Atlas v1.1 §2.2, §10C/E). The bedrock sublane may **reference** these via cross-lane relations, but MUST NOT promote their content onto a bedrock layer.

- `SurficialUnit` — unconsolidated cover (surficial sublane).
- `BoreholeReference`, `Well LogReference` — subsurface observations (boreholes-wells sublane).
- `Geochemistry SampleReference` — geochemistry sublane.
- `Mineral Occurrence`, `Resource Deposit`, `ResourceEstimate`, `Extraction Site` — resources sublane.
- `Hydrostratigraphic Unit` — geology-owned context that supports the Hydrology lane (cross-lane only).

</details>

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## 7 · Source Families & Source Roles

CONFIRMED source families (Atlas v1.1 §10D). The Geology lane's source ledger is broader than bedrock alone; the families below are the bedrock-relevant subset plus the lane families a bedrock sublane MUST NOT silently co-opt.

| Source family | Bedrock relevance | Source-role posture (CONFIRMED doctrine) | Citation |
|---|---|---|---|
| **KGS data and maps** | Primary bedrock-map authority for Kansas. | authority / observation / context / model **as source role requires**; rights & current terms **NEEDS VERIFICATION**; sensitive joins fail closed. | Atlas §10D |
| **KGS surficial geology and geologic maps** | Bedrock-relevant *only* for the bedrock components; surficial content routes to the surficial sublane. | Same posture. | Atlas §10D |
| **USGS NGMDB and GeMS** | Federal geologic-map database / GeMS schema; compilation-scale bedrock units. | Same posture. | Atlas §10D |
| KGS oil and gas wells and production | **Out of bedrock scope** — subsurface/production; resources & boreholes sublanes. | Same posture; sensitive joins fail closed. | Atlas §10D |
| KCC oil and gas regulatory data | **Out of bedrock scope** — regulatory/operator. | Same posture. | Atlas §10D |
| KGS/KDHE WWC5 and water-well program | **Out of bedrock scope** — water wells. | Same posture. | Atlas §10D |
| KGS LAS digital well logs and well tops | **Out of bedrock scope** — well logs/tops. | Same posture. | Atlas §10D |
| USGS MRDS | **Out of bedrock scope** — mineral resources; resources sublane. | Same posture. | Atlas §10D |
| USGS 3DEP terrain | `terrain_context` only — never a unit-identity source. | Visual context only. | Spatial Foundation §3D / MAP-MASTER |

> [!WARNING]
> **Source roles cannot be inferred from convenience.** A geophysical anomaly is not a confirmed bedrock unit. A borehole encountering a lithology is not a remapped unit boundary. Promotion of evidence across these roles is a **governed state transition**, not a join. The Atlas posture is explicit: each source's role is "authority / observation / context / model **as source role requires**," and **sensitive joins fail closed**.

> [!CAUTION]
> **License / attribution gate (NEEDS VERIFICATION).** The Atlas marks KGS / USGS "rights and current terms" as **NEEDS VERIFICATION** (§10D). KGS / USGS-derived COGs and tile artifacts MUST NOT publish until license and attribution are settled. Bedrock layers MUST fail release when license, source series, or attribution is missing.

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## 8 · Spatial & Temporal Model

CONFIRMED doctrine (Atlas v1.1 §10B/E; ENCY §7.8):

- **Geometry**
  - **Polygons** for bedrock units (`GeologicUnit`).
  - **Lines** for `StructureFeature` (faults, contacts) and `CrossSection` traces.
  - **Cross-sections** as interpretive 2D sections; **3D surfaces / voxels** only when justified, with representation receipts.
- **Interpretation versioning** — every refit produces a new `GeologyBoundaryVersion`; prior versions are preserved in lineage, not overwritten.
- **Uncertainty** — tracked at the unit and at the boundary line (e.g., approximate, inferred, concealed).
- **Temporal handling** (Atlas v1.1 §10E — "source, observed, valid, retrieval, release, and correction times stay distinct where material"):

| Time facet | Bedrock meaning |
|---|---|
| `source_time` | Publication date of the source map. |
| `observed_time` | Field-mapping date, when known. |
| `valid_time` | When the unit is considered current. |
| `retrieval_time` | When KFM pulled the source. |
| `release_time` | When KFM released the derivative. |
| `correction_time` | When a `CorrectionNotice` has been applied. |

> [!TIP]
> Geologic age (Cretaceous, Permian, etc.) and **time-of-mapping** are different. The bedrock sublane must carry **both** — confusing them is a classic anti-collapse failure that the temporal model is built to prevent.

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## 9 · Map & Viewing Products

PROPOSED sublane products (derived from Atlas v1.1 §10G domain viewing products; ENCY §7.8):

| Product | Geometry | Purpose | Status |
|---|---|---|---|
| **Bedrock unit map** | Polygon | Public-safe generalized bedrock unit polygons with unit code, lithology, age, and source vintage. | PROPOSED |
| **Lithology view** | Polygon (derived) | Recolor / re-symbolize the bedrock unit map by lithology class. | PROPOSED |
| **Geologic age view** | Polygon (derived) | Recolor by chronostratigraphic age. | PROPOSED |
| **Bedrock structure overlay** | Line | `StructureFeature` (faults, contacts) delivered with the bedrock map, with uncertainty classes. | PROPOSED |
| **Cross-section view** | Line + 2D section | Interpretive sections through bedrock units; carries representation receipt and evidence burden. | PROPOSED |
| **Interpretation-version diff** | Polygon (compare) | Compare two `GeologyBoundaryVersion` instances; flag changed polygons. | PROPOSED |
| **Uncertainty view** | Polygon (style overlay) | Visualize unit / boundary uncertainty classes. | PROPOSED |

CONFIRMED cross-cutting view doctrine (Atlas §10G "Cross-cutting viewing products"; MAP-MASTER; GAI): every bedrock product participates in **Evidence Drawer, time-aware state, trust badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode**. The bedrock sublane does not define its own renderer; it consumes the same governed map shell / Evidence Drawer / `AIReceipt` envelope as every other lane.

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## 10 · Pipeline Shape (RAW → PUBLISHED)

CONFIRMED doctrine; PROPOSED sublane application. Promotion is a **governed state transition, not a file move** (Directory Rules §0; Atlas v1.1 §10H).

| Stage | Bedrock-sublane handling | Gate | Status |
|---|---|---|---|
| **RAW** | Capture KGS / USGS bedrock map source payload (geometry as delivered + sidecar metadata) with source role, rights, sensitivity, citation, time, hash. | `SourceDescriptor` exists. | PROPOSED |
| **WORK / QUARANTINE** | Normalize CRS, geometry, attribute schema, unit-code crosswalk, age vocabulary, lithology vocabulary, identity, evidence, rights, policy. Hold failures (missing attribution, license unconfirmed, unknown unit code). | Validation + policy gate pass, or quarantine reason recorded. | PROPOSED |
| **PROCESSED** | Emit validated normalized `GeologicUnit` objects, `Lithology` descriptors, `GeologicAge` assignments, `StructureFeature` overlays, and public-safe candidate geometry. Emit `EvidenceRef`, `ValidationReport`; close digest. | `EvidenceRef`, `ValidationReport`, digest closure exist. | PROPOSED |
| **CATALOG / TRIPLET** | Emit catalog records, `EvidenceBundle`s, graph/triplet projections (`GeologicUnit` ↔ `Lithology` ↔ `GeologicAge` ↔ `StratigraphicInterval`), and release candidates. | Catalog / proof closure passes. | PROPOSED |
| **PUBLISHED** | Serve released public-safe bedrock layer artifacts (GeoParquet + COG/PMTiles) through governed APIs and a `ReleaseManifest`. | `ReleaseManifest`, correction path, rollback target, review / policy state exist. | PROPOSED |

> [!CAUTION]
> **Watcher-as-non-publisher invariant.** A bedrock watcher that detects a KGS map series update **MAY emit a candidate `PromotionDecision`**; it MUST NOT write to `data/processed/geology/` or `data/published/layers/geology/` directly. Promotion is reserved to the governed pipeline.

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## 11 · API, Contract & Schema Surfaces

PROPOSED governed surfaces (Atlas v1.1 §10J). All routes are **UNKNOWN** until verified against the mounted repo; outcomes are the canonical finite set.

| Surface | DTO / schema | Finite outcomes | Status |
|---|---|---|---|
| Geology feature / detail resolver | `GeologyDecisionEnvelope` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; exact route UNKNOWN. |
| Geology layer manifest resolver | `LayerManifest` / domain layer descriptor | `ANSWER` / `DENY` / `ERROR` | PROPOSED; public-safe release only. |
| Geology Evidence Drawer payload | `EvidenceDrawerPayload` + `EvidenceBundle` projection | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; evidence- and policy-filtered. |
| Geology Focus Mode answer | `Runtime Response Envelope` + `AIReceipt` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; AI never root truth. |
| Schema responsibility root | `schemas/contracts/v1/` | finite validator outcomes | PROPOSED; verify with Directory Rules + ADR-0001. |

> [!IMPORTANT]
> **Governed AI behavior (Atlas §10L).** AI may summarize released geology `EvidenceBundle`s, compare evidence, explain limitations, and draft steward-review notes. AI MUST `ABSTAIN` when evidence is insufficient and `DENY` where policy, rights, sensitivity, or release state blocks the request. `EvidenceBundle` outranks generated language.

<details>
<summary><b>Proposed validators, tests, and fixtures (Atlas §10K)</b></summary>

All PROPOSED; none verified against a mounted repo:

- Source-role validators (a map source is not silently a subsurface authority).
- Resource-class anti-collapse tests (no `ResourceEstimate` / `Mineral Occurrence` content on a bedrock layer).
- Public-safe geometry tests (generalization rule applied; receipt emitted).
- Borehole / well-log rights tests (sibling sublanes; bedrock layer must not surface them).
- Catalog closure tests (`EvidenceRef` resolves to a populated `EvidenceBundle`).
- AI evidence-before-model tests (`EvidenceBundle` outranks generated language).

</details>

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## 12 · Sensitivity, Rights, and Publication Posture

CONFIRMED / PROPOSED (Atlas v1.1 §10I; ENCY §7.8; operating contract §23.2 sensitive-domain matrix; T0–T4 tier scheme):

- **Bedrock unit polygons** are generally **public-safe when generalized** — **T0** (open) or **T1** (generalized) — provided rights, attribution, license, and source role are settled.
- **Exact borehole, sample, sensitive-resource, well-log, and private-well locations** default to **restricted or generalized** geometry (T2–T4) and live in **other sublanes** — they MUST NOT be promoted via the bedrock sublane (Atlas §10I).
- **Anti-collapse rule:** `Mineral Occurrence`, `Resource Deposit`, `ResourceEstimate`, `Extraction Site`, permit, production, and reserve claims must remain distinct from bedrock map units (Atlas §10I).
- **Default-deny on missing release inputs:** Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state **blocks public promotion** (CONFIRMED doctrine; Atlas §1 Operating Law and §10I; Directory Rules).

| Object class | Default tier | Allowed transform | Required gates |
|---|---|---|---|
| Bedrock unit polygon (generalized) | **T0 / T1** | Generalization where scale demands it. | Standard release gates; `RedactionReceipt` if generalized. |
| Bedrock `StructureFeature` overlay | **T0 / T1** | Generalization; uncertainty classes. | Standard release gates. |
| Exact borehole / sample / well-log location | **T2–T4** *(sibling sublanes)* | Generalize / restrict; never on the bedrock layer. | `RedactionReceipt` + `ReviewRecord` + `PolicyDecision`. |

> [!IMPORTANT]
> **A bedrock map on the map is not a resource map.** A user clicking a bedrock polygon must see the **bedrock unit identity** plus its `EvidenceBundle` — never a resource estimate, an extraction location, or a borehole location, unless those are independently released by their own sublanes.

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## 13 · Open Questions

| # | Question | Evidence that would settle it | Status |
|---|---|---|---|
| 1 | Is `docs/domains/<domain>/sublanes/<sublane>.md` an accepted layout, or should sublane docs use a flat-prefix scheme (e.g., `docs/domains/geology/SUBLANE-BEDROCK.md`)? | An ADR amending Directory Rules §12, or a mounted-repo precedent in another domain. | NEEDS VERIFICATION |
| 2 | Does the Geology lane carry semantic contracts under `contracts/domains/geology/` and machine schemas under `schemas/contracts/v1/domains/geology/` per ADR-0001? | Mounted-repo inspection; ADR-0001 status. | NEEDS VERIFICATION |
| 3 | Which KGS bedrock map series is the **default** authoritative source for Kansas bedrock, and at what scale? | A source-activation decision in `data/registry/sources/geology/`. | UNKNOWN |
| 4 | Are KGS license / attribution terms compatible with COG / PMTiles publication for the chosen series? | License review record; Atlas marks KGS/USGS rights NEEDS VERIFICATION (§10D). | NEEDS VERIFICATION |
| 5 | What is the canonical age-vocabulary (ICS chart edition / KGS local nomenclature) for bedrock `GeologicAge`? | A vocabulary file under `control_plane/` or `schemas/`. | UNKNOWN |
| 6 | Do both `bedrock_geology.md` and `bedrock.md` exist in this folder? If so, which is canonical? | Mounted-repo inspection of `docs/domains/geology/sublanes/`. | NEEDS VERIFICATION |
| 7 | What is the **generalization rule** for the public-safe bedrock unit map (target scale, tolerance, attribute redaction)? | A policy entry under `policy/domains/geology/` plus a generalization receipt fixture. | NEEDS VERIFICATION |
| 8 | What is the exact route for the geology feature / layer / drawer / Focus Mode resolvers? | Mounted-repo route inspection; Atlas §10J marks routes TBD/UNKNOWN. | UNKNOWN |
| 9 | What is the exact name of the source-activation outcome object (`SourceActivationDecision` is PROPOSED)? | `contracts/` semantic-contract inspection. | NEEDS VERIFICATION |

[Back to top ↑](#-geology-sublane--bedrock-geology)

---

## Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-GEOL-BEDROCK-01 | Accept `sublanes/` subfolder vs flat-prefix scheme under `docs/domains/geology/`. | docs steward + directory-rules owner | ADR amending Directory Rules §12; DRIFT_REGISTER entry until resolved. |
| OQ-GEOL-BEDROCK-02 | Confirm geology contract/schema homes (`contracts/domains/geology/`, `schemas/contracts/v1/domains/geology/`). | geology domain steward | Mounted-repo inspection + ADR-0001 check. |
| OQ-GEOL-BEDROCK-03 | Designate default authoritative KGS bedrock map series + scale. | geology domain steward + source authority | Source-activation decision in `data/registry/sources/geology/`. |
| OQ-GEOL-BEDROCK-04 | Resolve KGS/USGS license + attribution for COG/PMTiles publication. | rights reviewer | License review record; close Atlas §10D NEEDS VERIFICATION. |
| OQ-GEOL-BEDROCK-05 | Confirm finite-outcome resolver routes for geology surfaces. | geology domain steward + API owner | Mounted-repo route inspection; close Atlas §10J TBD. |
| OQ-GEOL-BEDROCK-06 | Reconcile `bedrock_geology.md` vs any sibling `bedrock.md` — only one canonical. | docs steward | DRIFT_REGISTER entry + folder inspection. |

## Open verification backlog

These items remain `NEEDS VERIFICATION` before promotion from `draft` to `published`:

1. Sublane folder layout (`sublanes/` vs flat prefix) — Directory Rules §12 silent.
2. Geology contract/schema homes against mounted repo and ADR-0001.
3. Default KGS bedrock map series and scale.
4. KGS/USGS license and attribution terms for tile/COG publication (Atlas §10D rights = NEEDS VERIFICATION).
5. Filename reconciliation (`bedrock_geology.md` vs `bedrock.md`).
6. Resolver route names for geology surfaces (Atlas §10J = TBD/UNKNOWN).
7. Bedrock `GeologicAge` canonical vocabulary.
8. Generalization rule + receipt fixture for the public-safe bedrock map.
9. Exact source-activation outcome object name.

## Changelog v0 → v1

| Change | Type (per contract §37) | Reason |
|---|---|---|
| New sublane doc created at `docs/domains/geology/sublanes/bedrock_geology.md` | new | First bedrock-geology sublane doc under the requested filename. |
| Object families set to Atlas v1.1 §10C/E canonical casing (`StructureFeature`, `SurficialUnit`, …) | new | Terminology fidelity; `FaultStructure` deliberately not used. |
| §7 source families set to the Atlas §10D ledger with bedrock-relevance flags | new | Avoid a generic two-source stub; mirror the actual lane ledger. |
| Added §11 API/contract/schema surfaces from Atlas §10J–L | new | Surface governed resolvers, finite outcomes, and AI posture. |
| Added T0–T4 tier mapping for bedrock object classes | new | Ground §12 in the per-domain sensitivity matrix. |
| Added companion sections (Open Qs register, Verification backlog, Changelog, DoD) | new | Doctrine-doc companion pattern. |

> **Backward compatibility.** New file; no prior anchors to preserve. Anchors use GitHub auto-slug of the H1 "🪨 Geology Sublane — Bedrock Geology"; verify the leading-emoji slug renders as `#-geology-sublane--bedrock-geology` on the target GitHub instance.

## Definition of done

This document is done enough to enter the repository when:

- it is placed according to Directory Rules (sublane-folder question OQ-GEOL-BEDROCK-01 resolved);
- the filename collision with any `bedrock.md` is resolved (OQ-GEOL-BEDROCK-06);
- a docs steward and the geology domain steward review it;
- it is linked from the Geology lane `README.md` / doctrine index;
- it does not conflict with accepted ADRs (ADR-0001 schema home; any sublane-folder ADR);
- the filename and sublane-folder questions are logged in `docs/registers/DRIFT_REGISTER.md`;
- the `GENERATED_RECEIPT.json` planned at authoring time is wired into CI;
- future changes follow the operating contract §37 lifecycle.

---

## Related Docs

PROPOSED — verify each path against the mounted repo before linking.

- `docs/domains/geology/README.md` — Geology lane charter.
- `docs/domains/geology/sublanes/surficial_geology.md` — Sibling sublane for unconsolidated cover (`SurficialUnit`).
- `docs/domains/geology/sublanes/structures.md` — Sibling sublane for structural geology (`StructureFeature`).
- `docs/domains/geology/sublanes/stratigraphy.md` — Sibling sublane for stratigraphic correlation.
- `docs/domains/geology/sublanes/boreholes_wells.md` — Sibling sublane for subsurface observations.
- `docs/domains/geology/sublanes/resources.md` — Sibling sublane for mineral / resource / extraction context.
- `docs/domains/hydrology/` — Cross-lane (hydrostratigraphy).
- `docs/domains/soil/` — Cross-lane (parent material).
- `docs/domains/hazards/` — Cross-lane (fault / landslide / subsidence context).
- `directory-rules.md` §12 — Domain Placement Law; §5 Canonical Root Tree; §4 Placement Protocol.
- `ai-build-operating-contract.md` — canonical operating contract (`CONTRACT_VERSION = "3.0.0"`).
- Atlas v1.1 Ch. 10 — Geology / Natural Resources.
- `kfm_encyclopedia.pdf` §7.8 — Geology and Natural Resources.
- `docs/registers/DRIFT_REGISTER.md` — filename + sublane-folder routing.

---

<details>
<summary><b>Appendix A · Bedrock-sublane checklist (PROPOSED reviewer aid)</b></summary>

A non-normative checklist for PRs that touch bedrock-sublane artifacts. Promote to `docs/runbooks/geology/BEDROCK_REVIEW.md` if it survives use.

- [ ] **Source activation** — `SourceDescriptor` exists; source-activation decision records role, rights, license, attribution.
- [ ] **Source role** — bedrock map source declared as a map authority; not silently used as a subsurface authority.
- [ ] **Schema home** — JSON Schema under `schemas/contracts/v1/domains/geology/...` (ADR-0001 default).
- [ ] **Identity** — `GeologicUnit` identity binds `source_id + object_role + temporal_scope + normalized_digest`.
- [ ] **Interpretation versioning** — every refit produces a new `GeologyBoundaryVersion`; prior versions preserved.
- [ ] **Temporal facets** — source / observed / valid / retrieval / release / correction times carried where material.
- [ ] **Public-safe geometry** — generalization rule applied; `RedactionReceipt` emitted where generalized.
- [ ] **Anti-collapse** — no `Mineral Occurrence`, `Resource Deposit`, `ResourceEstimate`, `Extraction Site`, or borehole-detail content rides in on the bedrock layer.
- [ ] **Evidence closure** — `EvidenceRef` resolves to a populated `EvidenceBundle`.
- [ ] **Release inputs** — `ReleaseManifest`, correction path, rollback target, review/policy state all present.
- [ ] **License / attribution** — KGS / USGS attribution and license text carried in the `LayerManifest`.
- [ ] **Terminology** — `StructureFeature` (not `FaultStructure`); Atlas casing preserved.
- [ ] **Finite outcomes** — resolvers return `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` only.
- [ ] **Cross-lane** — soil / hydrology / hazards joins, if any, preserve ownership, source role, and `EvidenceBundle` support.

</details>

<details>
<summary><b>Appendix B · Anti-pattern register (illustrative)</b></summary>

| Anti-pattern | Symptom | Fix |
|---|---|---|
| **Map-as-truth** | A bedrock polygon is treated as verified subsurface presence at depth. | Restate as a *mapped* unit at the source scale; require borehole / geophysics evidence for depth claims. |
| **Lithology = unit** | UI labels the polygon "Limestone" without referencing the `GeologicUnit`. | Render unit identity first (e.g., "Stone Corral Fm"); `Lithology` is a descriptor of the unit. |
| **Silent re-bound** | A new KGS release overwrites the prior unit polygon without a new `GeologyBoundaryVersion`. | Treat every refit as a new version; preserve prior in lineage; emit a `CorrectionNotice` if it changes a published artifact. |
| **License skipped** | A KGS-derived COG / PMTiles bundle goes to release without recorded license / attribution. | Fail release; require license review and attribution in the `LayerManifest` (Atlas §10D rights = NEEDS VERIFICATION). |
| **Resource bleed** | A bedrock layer surfaces resource-estimate attributes on click. | Strip resource attributes; route `Mineral Occurrence` / `ResourceEstimate` claims through the resources sublane with its own policy posture. |
| **Term drift** | A doc reuses `FaultStructure`. | Use `StructureFeature` per Atlas §10C/E; log drift in DRIFT_REGISTER. |
| **Watcher publishes** | A bedrock watcher writes to `data/processed/geology/` or `data/published/layers/geology/`. | Watcher emits candidate `PromotionDecision` only; promotion is governed. |

</details>

---

**Last updated:** 2026-06-03 · **Doc status:** draft (v1) · **Authority:** doctrine CONFIRMED / paths PROPOSED · **Contract:** `CONTRACT_VERSION = "3.0.0"` · [Back to top ↑](#-geology-sublane--bedrock-geology)
