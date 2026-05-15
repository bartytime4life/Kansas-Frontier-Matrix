# 🌾 Agriculture — KFM Domain Lane

> The agriculture lane governs evidence-backed crop, field, rotation, suitability, yield, irrigation, conservation, and agricultural-economy observations for Kansas — published only as aggregate or permissioned products, with field-level and operator-level detail denied by default.

[![Status](https://img.shields.io/badge/status-PROPOSED%20implementation-orange)](#3-status--authority)
[![Doctrine](https://img.shields.io/badge/doctrine-CONFIRMED-success)](#3-status--authority)
[![Authority](https://img.shields.io/badge/root-docs%2Fdomains%20(canonical)-blue)](#5-repo-fit)
[![Lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-lightgrey)](#14-pipeline-shape-raw--published)
[![Sensitivity](https://img.shields.io/badge/sensitivity-T0%20aggregate%20%2F%20T1%20field-yellow)](#12-sensitivity--rights-posture)
[![Policy](https://img.shields.io/badge/policy-cite--or--abstain-green)](#3-status--authority)
[![Schema home](https://img.shields.io/badge/schemas-schemas%2Fcontracts%2Fv1%2Fdomains%2Fagriculture-informational)](#5-repo-fit)
[![Last updated](https://img.shields.io/badge/last%20updated-2026--05--15-blue)](#last-updated)

| Field | Value |
|---|---|
| **Lane** | `docs/domains/agriculture/` |
| **Authority level** | Canonical (lane README); implementation paths are **PROPOSED** until verified against mounted-repo evidence |
| **Status** | `PROPOSED` (implementation) · `CONFIRMED` (doctrine) |
| **Sensitivity default** | `T0` aggregate · `T1` field-candidate · `T4` operator/private-join |
| **Owners** | `<TBD — Agriculture domain steward + Docs steward>` (placeholder) |
| **Source dossier** | `KFM_Agriculture_Domain_Implementation_Dossier_REVISED_2026-04-21.pdf` (SRC-028) |
| **Atlas reference** | Domains Culmination Atlas v1.1, Ch. 9 — Agriculture |
| **Last reviewed** | `2026-05-15` |

---

## Quick jump

[1. Purpose](#1-purpose) ·
[2. Scope & boundary](#2-scope--boundary) ·
[3. Status & authority](#3-status--authority) ·
[4. What belongs here / what doesn't](#4-what-belongs-here--what-doesnt) ·
[5. Repo fit](#5-repo-fit) ·
[6. Proposed lane tree](#6-proposed-lane-tree) ·
[7. Domain at a glance (diagram)](#7-domain-at-a-glance) ·
[8. Ubiquitous language](#8-ubiquitous-language) ·
[9. Canonical object families](#9-canonical-object-families) ·
[10. Source families](#10-source-families) ·
[11. Cross-lane relations](#11-cross-lane-relations) ·
[12. Sensitivity & rights posture](#12-sensitivity--rights-posture) ·
[13. Map layers & viewing products](#13-map-layers--viewing-products) ·
[14. Pipeline shape (RAW → PUBLISHED)](#14-pipeline-shape-raw--published) ·
[15. First credible thin slice](#15-first-credible-thin-slice) ·
[16. Validation & review](#16-validation--review) ·
[17. Verification backlog](#17-verification-backlog) ·
[18. Related folders & docs](#18-related-folders--docs) ·
[19. ADRs](#19-adrs) ·
[20. FAQ](#20-faq) ·
[Appendix](#appendix)

> [!IMPORTANT]
> **Agriculture is rights- and privacy-sensitive.** Field polygons, operator identities, and source-rights-limited datasets are **denied by default** in any public surface. Public products aggregate to county / HUC / grid thresholds and resolve every claim to an `EvidenceBundle`. Field-level publication requires explicit rights, sensitivity review, and a recorded `AggregationReceipt` or `RedactionReceipt`. See [§12](#12-sensitivity--rights-posture).

---

## 1. Purpose

The Agriculture lane represents crops, fields, soils-as-substrate, irrigation, yields, conservation practices, stress indicators, and agricultural economy across Kansas — **as governed, citable, public-safe observations**, not as a private farm-management surface.

It exists to:

- Make agricultural claims **inspectable**: every published claim resolves to an `EvidenceBundle` and carries its source role, sensitivity, time, validation, and release lineage.
- Keep the **trust membrane intact**: public clients and standard UI surfaces read released `LayerManifest` and governed-API products, never canonical / internal stores.
- Honor **source rights and privacy**: USDA NASS terms, Kansas Mesonet usage, HLS/SMAP product terms, and farm-operator privacy fail closed when unclear.
- Provide the agronomic substrate for cross-lane reasoning with Soil, Hydrology, Atmosphere/Air, Hazards, and the Frontier Matrix.

> *CONFIRMED doctrine / PROPOSED implementation.* The dossier and Atlas govern what this lane **owns and means**; the on-disk schemas, validators, fixtures, policies, tests, and pipelines that realize it remain `PROPOSED` until verified against a mounted KFM repository.

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 2. Scope & boundary

### 2.1 What this domain owns

**`CONFIRMED` (doctrine):** Agricultural observations and derivatives, plus a small public-safe family of indicators. Concretely, the lane owns the following twelve object families ([§9](#9-canonical-object-families)):

`CropObservation` · `FieldCandidate` · `CropRotation` · `YieldObservation` · `IrrigationLink` · `ConservationPractice` · `SoilCropSuitability` · `AgriculturalEconomyObservation` · `SupplyChainNode` · `DroughtStressIndicator` · `PestStressIndicator` · `AggregationReceipt`

### 2.2 What this domain explicitly does **not** own

**`CONFIRMED` (doctrine):**

| Concern | Owning lane |
|---|---|
| Soil map units, components, horizons, hydrologic group, MUKEY semantics | **Soil** (`docs/domains/soil/`) |
| Streamflow, gauges, NFHL, water levels, flood context | **Hydrology** (`docs/domains/hydrology/`) |
| Weather observations, climate normals, smoke / AOD context | **Atmosphere / Air** (`docs/domains/atmosphere/`) |
| Drought as a hazard event, disaster declarations | **Hazards** (`docs/domains/hazards/`) |
| Parcels, ownership, title, living-person privacy, DNA | **People / DNA / Land** (`docs/domains/people-dna-land/`) |
| Vegetation taxa, rare-plant geometry | **Flora** (`docs/domains/flora/`) |

Agriculture **cites** Soil, Hydrology, Atmosphere/Air, and People/Land through governed cross-lane joins ([§11](#11-cross-lane-relations)). It never re-defines another lane's canonical truth.

### 2.3 Hard boundary statements

- **No private farm operations.** Operator-identified records do not appear on public surfaces.
- **No field-level sensitive detail without review.** Field polygons may be sensitive; the public default is aggregation to county / HUC / grid thresholds.
- **No source-rights-limited data without review.** Terms for NASS, Mesonet, SCAN, HLS, SMAP, USCRN, and any market/economy source are `NEEDS VERIFICATION` and fail closed until reviewed.
- **No private person-parcel join in public surfaces.** Agriculture × People/Land joins remain restricted by default (`T2` / `T4`).

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 3. Status & authority

| Field | Value |
|---|---|
| **Doctrine status** | `CONFIRMED` — Atlas v1.1 Ch. 9, Encyclopedia §7.7, Build Manual §6.12 |
| **Implementation status** | `PROPOSED` — no mounted repo inspected in this session |
| **Authority class (this README)** | Canonical (per Directory Rules §15) |
| **Authority class (proposed paths)** | `PROPOSED` until verified against mounted repo |
| **Schema home** | `schemas/contracts/v1/domains/agriculture/` (default per ADR-0001 schema home) — `PROPOSED` |
| **Truth posture** | Cite-or-abstain. `EvidenceBundle` outranks generated language, renderer state, tiles, search indexes, graph projections. |
| **Lifecycle invariant** | RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED. Promotion is a **governed state transition, not a file move.** |
| **Trust membrane** | Public clients use governed APIs and released artifacts, never canonical / internal stores. |
| **AI boundary** | Governed AI is interpretive only. Outcomes are `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. No uncited claims about Kansas agriculture. |

> [!NOTE]
> **Doctrine vs. implementation.** When this README says "the lane does X," read it as *"the lane is doctrinally specified to do X; whether the current repo enforces X is `NEEDS VERIFICATION` until a mounted-repo inspection confirms."* Every implementation-shaped statement is `PROPOSED` unless explicitly labeled otherwise.

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 4. What belongs here / what doesn't

This is a `docs/`-scoped README. It explains what the agriculture **lane** is and points to where each kind of agriculture file lives. It does **not** host schemas, policy bundles, fixtures, code, or data — those live under their own responsibility roots, with `domains/agriculture/` as a **segment** inside each root ([§5](#5-repo-fit)).

### 4.1 What belongs in `docs/domains/agriculture/`

| File type | Purpose | Status |
|---|---|---|
| `README.md` *(this file)* | Lane landing page, scope, boundaries, status | `PROPOSED` |
| `overview.md` | Long-form domain narrative; mission, history, viewing products | `PROPOSED` (placeholder) |
| `ubiquitous-language.md` | Glossary of agriculture-specific terms with citation back to dossier | `PROPOSED` (placeholder) |
| `cross-lane-relations.md` | Soil, hydrology, atmosphere, people/land joins and their constraints | `PROPOSED` (placeholder) |
| `sensitivity-and-rights.md` | Tier matrix, allowed transforms, deny-by-default register entries | `PROPOSED` (placeholder) |
| `viewing-products.md` | Map layers, dashboards, Evidence Drawer payloads, Focus Mode rules | `PROPOSED` (placeholder) |
| `thin-slice.md` | First credible slice acceptance criteria and Definition of Done | `PROPOSED` (placeholder) |
| `verification-backlog.md` | Open verification items keyed to dossier sections | `PROPOSED` (placeholder) |

### 4.2 What does **not** belong here

| File type | Belongs in | Reason |
|---|---|---|
| Object schemas (`.schema.json`) | `schemas/contracts/v1/domains/agriculture/` | Shape is owned by `schemas/`, not `docs/`. ADR-0001. |
| Object semantics (Markdown contracts) | `contracts/domains/agriculture/` | Meaning is owned by `contracts/`. |
| OPA / Conftest policy bundles | `policy/domains/agriculture/` | Allow / deny / restrict / abstain decisions are policy authority. |
| Validators, builders, generators | `tools/validators/agriculture/` *(or topic root)* | Repo-wide validation logic. |
| Fixtures (golden / valid / invalid) | `fixtures/domains/agriculture/` | Test inputs are not docs. |
| Pipeline logic | `pipelines/domains/agriculture/` | Executable pipeline logic. |
| Pipeline specs | `pipeline_specs/agriculture/` | Declarative pipeline configs. |
| Connectors (NASS, SSURGO, Mesonet…) | `connectors/<source>/` | Source-specific fetchers are not domain-keyed. |
| RAW / WORK / PROCESSED / PUBLISHED data | `data/<phase>/agriculture/` | Lifecycle data. Promotion is governed. |
| Release manifests, rollback cards | `release/candidates/agriculture/`, `release/manifests/` | Release decisions are not docs. |
| Receipts (`AggregationReceipt`, `RedactionReceipt`, `RunReceipt`) | `data/receipts/`, `data/proofs/` | Trust-bearing artifacts. Never `artifacts/`. |
| Source descriptors | `data/registry/sources/agriculture/` | Source registry. |

> [!WARNING]
> If a file in this directory starts to host schemas, policy, code, or trust-bearing receipts, it is **drift**. Open an entry in `docs/registers/DRIFT_REGISTER.md` per Directory Rules §2.5 and route the file to its actual responsibility root.

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 5. Repo fit

`PROPOSED` lane application of Directory Rules §12 (*Domain Placement Law*): Agriculture lives as a **segment** inside each responsibility root, never as a root folder itself.

### 5.1 Upstream of this README

- **Doctrine** — `docs/doctrine/` (lifecycle law, truth posture, trust membrane, authority ladder, directory rules)
- **Architecture** — `docs/architecture/` (governed-api, map-shell, contract-schema-policy-split)
- **ADRs** — `docs/adr/` (notably `ADR-0001` schema home)
- **Sibling domains** — `docs/domains/{soil,hydrology,atmosphere,hazards,people-dna-land,flora,frontier-matrix}/`

### 5.2 Downstream lanes (cross-root) — `PROPOSED`

```text
contracts/domains/agriculture/
schemas/contracts/v1/domains/agriculture/
policy/domains/agriculture/
tests/domains/agriculture/
fixtures/domains/agriculture/
packages/domains/agriculture/
pipelines/domains/agriculture/
pipeline_specs/agriculture/
data/raw/agriculture/
data/work/agriculture/
data/quarantine/agriculture/
data/processed/agriculture/
data/catalog/domain/agriculture/
data/published/layers/agriculture/
data/registry/sources/agriculture/
release/candidates/agriculture/
```

All paths above are `PROPOSED` until a mounted-repo inspection records them as present. Where the realized repo conflicts with these names, open a `DRIFT_REGISTER.md` entry and resolve by ADR or migration — **do not** silently introduce a parallel `agriculture/` root folder.

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 6. Proposed lane tree

`PROPOSED` directory tree for `docs/domains/agriculture/` only. (The wider lane footprint across other responsibility roots is summarized in [§5](#5-repo-fit).)

```text
docs/domains/agriculture/
├── README.md                       # this file
├── overview.md                     # PROPOSED: long-form narrative
├── ubiquitous-language.md          # PROPOSED: term glossary (§8)
├── cross-lane-relations.md         # PROPOSED: soil/hydro/air/people joins (§11)
├── sensitivity-and-rights.md       # PROPOSED: tier matrix and gates (§12)
├── viewing-products.md             # PROPOSED: map layers, drawer, Focus Mode (§13)
├── thin-slice.md                   # PROPOSED: first credible slice (§15)
└── verification-backlog.md         # PROPOSED: open items (§17)
```

> [!NOTE]
> **No nested implementation.** This directory must not develop a private `schemas/`, `policy/`, `data/`, or `release/` subtree — that is the §13.4 anti-pattern *"Domain folders becoming root folders and fragmenting the lifecycle."*

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 7. Domain at a glance

The agriculture lane sits inside KFM's cross-domain spine, citing soil, hydrology, and atmosphere, and feeding the Frontier Matrix and Hazards (drought) lanes.

```mermaid
flowchart LR
  subgraph EXT["External source families (rights NEEDS VERIFICATION)"]
    NASS["USDA NASS<br/>CDL · QuickStats · Crop Progress"]
    NRCS["NRCS<br/>SSURGO · gSSURGO · SCAN · Conservation Practices"]
    MET["Weather / Soil moisture<br/>Kansas Mesonet · NOAA USCRN"]
    EO["Earth observation<br/>NASA HLS · HLS-VI · SMAP"]
    ECON["Markets / Economy<br/>where permitted"]
  end

  subgraph AG["Agriculture lane (this README)"]
    direction TB
    CO["CropObservation"]
    FC["FieldCandidate"]
    CR["CropRotation"]
    YO["YieldObservation"]
    IL["IrrigationLink"]
    CP["ConservationPractice"]
    SCS["SoilCropSuitability"]
    AEO["AgriculturalEconomyObservation"]
    SCN["SupplyChainNode"]
    DSI["DroughtStressIndicator"]
    PSI["PestStressIndicator"]
    AR["AggregationReceipt"]
  end

  subgraph CITE["Cited lanes (read-only joins)"]
    SOIL["Soil<br/>MUKEY · components"]
    HYD["Hydrology<br/>HUC · gauges · NFHL"]
    AIR["Atmosphere / Air<br/>weather · smoke · AOD"]
    PEO["People / Land<br/>RESTRICTED join"]
  end

  subgraph DS["Downstream (citing)"]
    FM["Frontier Matrix<br/>county-year panels"]
    HAZ["Hazards<br/>drought events"]
  end

  EXT --> AG
  AG -.->|"MUKEY join · suitability"| SOIL
  AG -.->|"irrigation · water-use · drought"| HYD
  AG -.->|"weather · heat · smoke · stress"| AIR
  AG -.->|"parcel join<br/>RESTRICTED"| PEO
  AG --> FM
  AG --> HAZ
```

*Diagram is doctrinal; the realized graph structure depends on mounted-repo schemas, contracts, and policy bundles (`PROPOSED`).*

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 8. Ubiquitous language

`CONFIRMED` terms (per Atlas v1.1 Ch. 9 §C) — meaning constrained by source role, evidence, time, and release state. Field realization is `PROPOSED`.

| Term | Use within Agriculture |
|---|---|
| **Crop Observation** | A bounded, time-keyed observation of crop presence, type, condition, or progress; carries source role, sensitivity, and evidence. |
| **Field Candidate** | A candidate field-shaped geometry derived from CDL or imagery; **never** equated with a private farm-management record. |
| **Crop Rotation** | Multi-year crop sequence at a candidate or aggregate unit; observation, not prescription. |
| **Yield Observation** | Bounded yield evidence at the public-safe aggregation level (county, HUC, grid); operator-level yields are not public. |
| **Soil Crop Suitability** | Derived suitability indicator joining Soil MUKEY semantics with crop suitability rules; downstream of Soil authority. |
| **Drought Stress Indicator** | Public-safe agricultural drought stress derivative; cites hydrology and atmospheric inputs; not an emergency advisory. |
| **Pest Stress Indicator** | Public-safe pest-stress derivative; never a treatment recommendation. |
| **Aggregation Receipt** | Record of public-safe aggregation transform (threshold, unit, k-cell). Required for any field → aggregate publication. |
| **MUKEY** | SSURGO map-unit key; **cited** from Soil, not redefined here. |
| **Component percentage** | SSURGO component proportion within a map unit; **cited** from Soil. |
| **Hydrologic group** | NRCS hydrologic soil group (A/B/C/D); **cited** from Soil. |
| **VWC** | Volumetric water content; soil-moisture observation property cited via Soil / Atmosphere/Air. |
| **Spec hash** | Deterministic content digest used to lock parameters and pipeline specifications for receipt reproducibility. |

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 9. Canonical object families

`CONFIRMED` doctrine / `PROPOSED` field realization. Identity rule for each object family is a `PROPOSED` deterministic basis: *source id + object role + temporal scope + normalized digest*. `CONFIRMED` temporal handling: source / observed / valid / retrieval / release / correction times stay distinct where material.

| Object family | One-line role | Spatial unit (typical) | Sensitivity default |
|---|---|---|---|
| **`CropObservation`** | Bounded crop presence / type / condition / progress evidence | County, HUC, grid cell, candidate field | `T0` aggregate · `T1` field |
| **`FieldCandidate`** | Candidate field-shaped geometry from CDL or imagery | Polygon | `T1` (geometry generalized) · `T4` if operator-joined |
| **`CropRotation`** | Multi-year crop sequence at aggregate or candidate unit | County / HUC / grid / candidate field | `T0` aggregate · `T1` field |
| **`YieldObservation`** | Yield evidence at the public-safe unit | County / HUC | `T0` aggregate · `T4` operator-level |
| **`IrrigationLink`** | Relation linking agricultural unit to water-use context | Polygon / point reference | `T1` default · `T2`/`T4` for private operator joins |
| **`ConservationPractice`** | Practice observation (cover crop, no-till, buffer, etc.) where permitted | Polygon / point | `T1` default · `T2`/`T4` for operator joins |
| **`SoilCropSuitability`** | Derived suitability cell or polygon (cites Soil) | Grid / polygon | `T0` |
| **`AgriculturalEconomyObservation`** | Aggregate market / production / economy indicator | County / region | `T0` aggregate; permitted sources only |
| **`SupplyChainNode`** | Aggregate supply-chain node (elevator, processor, market) | Point / area | `T0` aggregate |
| **`DroughtStressIndicator`** | Public-safe drought stress signal for agriculture | Grid / HUC / county | `T0` |
| **`PestStressIndicator`** | Public-safe pest-stress signal | Grid / region | `T0` |
| **`AggregationReceipt`** | Record of public-safe aggregation transform (threshold, k-cell, unit) | n/a (receipt) | `T0` |

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 10. Source families

`CONFIRMED` source basis: **SRC-AG**, SRC-SOIL, SRC-HYD, EXT-NASS, EXT-SSURGO, EXT-3DEP. Rights and current terms are `NEEDS VERIFICATION` for every external source until a mounted-repo source descriptor is inspected; sensitive joins **fail closed** until reviewed.

| Source family | Role(s) | Rights / sensitivity | Freshness | Status |
|---|---|---|---|---|
| **USDA NASS — CDL** | authority · observation · context · model | terms `NEEDS VERIFICATION`; sensitive joins fail closed | annual; vintage-specific | `PROPOSED` |
| **USDA NASS — QuickStats / Crop Progress** | authority · observation · context | terms `NEEDS VERIFICATION` | weekly / annual | `PROPOSED` |
| **NRCS — SSURGO / Soil Data Access** | authority · observation · context · model | static-vs-observation distinction required | survey vintage | `PROPOSED` (owned by Soil) |
| **NRCS — gSSURGO** | authority · observation · context · model | as SSURGO | survey vintage | `PROPOSED` (owned by Soil) |
| **NRCS — Conservation practice data** | observation · context | rights review required for operator-level | cadence-specific | `PROPOSED` |
| **NRCS — SCAN** | observation · context | usage terms `NEEDS VERIFICATION` | hourly / sub-hourly | `PROPOSED` |
| **Kansas Mesonet** | authority · observation · context | written consent / attribution `NEEDS VERIFICATION` | sub-hourly | `PROPOSED` |
| **NOAA USCRN** | authority · observation · context | public; terms `NEEDS VERIFICATION` | sub-hourly | `PROPOSED` |
| **NASA SMAP** | observation · context · model | product terms `NEEDS VERIFICATION` | daily | `PROPOSED` |
| **NASA HLS / HLS-VI** | observation · context | product terms `NEEDS VERIFICATION` | 2–3 days | `PROPOSED` |
| **Irrigation / water-use sources** | observation · context | rights and disclosure rules `NEEDS VERIFICATION` | varies | `PROPOSED` |
| **Crop insurance / market / economy sources** | observation · context | rights-restricted; permitted-only | varies | `PROPOSED` (deny by default) |
| **Local extension sources** | context · observation | rights and attribution `NEEDS VERIFICATION` | varies | `PROPOSED` |

> [!CAUTION]
> Activating any of these connectors without a `SourceDescriptor`, rights review, and a recorded sensitivity tier is the `connector publishes` anti-pattern. Connectors emit to `data/raw/` or `data/quarantine/`; promotion to public surfaces is gated.

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 11. Cross-lane relations

`CONFIRMED` / `PROPOSED`. Each relation must preserve ownership, source role, sensitivity, and `EvidenceBundle` support. Agriculture **cites**; it never re-defines another lane's truth.

| Related lane | Relation type | Constraint | Default tier on joined output |
|---|---|---|---|
| **Soil** | `MUKEY` joins; suitability support | MUKEY semantics owned by Soil; agriculture consumes via governed join | `T0` |
| **Hydrology** | Irrigation, drought, water-use context | Flow / NFHL / gauge semantics owned by Hydrology; agriculture cites HUC / reach | `T0` aggregate; `T1` if join exposes operator |
| **Atmosphere / Air** | Weather, heat, smoke / AOD, vegetation stress | Weather / climate normals / AOD owned by Atmosphere/Air | `T0` |
| **People / Land** | Farm / operator / parcel context | **Restricted** by default; private person-parcel joins denied; aggregate or de-identified only | `T2` / `T4` for private joins; `T0` aggregate |
| **Frontier Matrix** | Agriculture observations contribute to county-year panels | Agriculture remains the owner of agriculture truth; Frontier Matrix cites | `T0` |
| **Hazards (drought)** | Agricultural drought signals cited as context | Drought-as-event remains a Hazards object; agriculture supplies indicator context | `T0` |
| **Flora** | Vegetation indices / habitat adjacency | Flora owns plant taxa; agriculture does not own vegetation truth | `T0` |

> [!IMPORTANT]
> **People / Land joins are the highest-risk surface in this lane.** Any cross-lane edge that could re-identify a private operator, parcel owner, or living person must be reviewed under the People/DNA/Land sensitivity rules and fail closed until a `RedactionReceipt` and `ReviewRecord` exist.

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 12. Sensitivity & rights posture

The agriculture lane uses the master sensitivity tier scheme (Atlas v1.1 §24.5). Tiers are `PROPOSED` defaults; allowed transforms and required gates must be recorded as receipts and review records.

| Tier | Name | Definition | Audience |
|---|---|---|---|
| `T0` | Open | Public-safe without transforms | Any public client via governed API |
| `T1` | Generalized | Public-safe after generalization / aggregation / redaction | Any public client via governed API |
| `T2` | Reviewer | Released only to authenticated reviewers or domain stewards | Stewards, reviewers, named collaborators |
| `T3` | Restricted | Released only under named agreement (rights / consent / sovereignty) | Named authorized parties only |
| `T4` | Denied | Not released; existence may be released only by steward review | — |

### 12.1 Agriculture-specific tier defaults (`PROPOSED`)

| Object class / surface | Default | Allowed transforms | Required gates |
|---|---|---|---|
| `CropObservation` (county / HUC aggregate) | `T0` | — | release manifest |
| `CropObservation` (`FieldCandidate` join) | `T1` | aggregation to k-cell; geometry generalization | `AggregationReceipt` + `ReviewRecord` |
| `YieldObservation` (operator-level) | `T4` | aggregation to county / HUC → `T0` | `AggregationReceipt` + `ReviewRecord` + `PolicyDecision` |
| `IrrigationLink` (private operator join) | `T4` | aggregation / de-identification → `T1` | `RedactionReceipt` + `ReviewRecord` |
| `ConservationPractice` (operator-identified) | `T4` | aggregation / de-identification → `T1` | `RedactionReceipt` + `ReviewRecord` |
| `AgriculturalEconomyObservation` (permitted source) | `T0` | — | rights confirmation |
| `AgriculturalEconomyObservation` (restricted source) | `T2`/`T4` | per source terms | `PolicyDecision` + `ReviewRecord` |
| `DroughtStressIndicator` / `PestStressIndicator` | `T0` | — | indicator-uncertainty labeling; non-emergency disclaimer |

### 12.2 Deny-by-default register entries

- **Private farm operations** — denied unless rights and review support permit.
- **Field-level sensitive detail** — denied at public surfaces; public products aggregate to county / HUC / grid thresholds.
- **Source-rights-limited data** — denied until terms are recorded and review supports release.
- **Indicator-as-advisory** — agriculture **does not** issue emergency or treatment advisories; advisory framing fails closed.

### 12.3 Tier transitions

Upgrading toward public always requires both a transform receipt and a review record. Downgrading (toward `T4`) only requires a `CorrectionNotice` + `ReviewRecord` and always precedes invalidation of derivatives.

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 13. Map layers & viewing products

`CONFIRMED` doctrine / `PROPOSED` realization. Public viewing products are governed surfaces — they render `LayerManifest` + released `EvidenceBundle`, not raw / canonical stores.

| Product | Object basis | Sensitivity | Notes |
|---|---|---|---|
| Crop / soil / weather dashboard | `CropObservation` + cited Soil + cited Atmosphere/Air | `T0` aggregate | Cross-lane composition only via governed API |
| CDL crop map | `CropObservation` | `T0` | Renders CDL-derived layer; field detail not exposed |
| Public-safe county / HUC aggregation | `CropObservation`, `YieldObservation`, `AggregationReceipt` | `T0` | Aggregation thresholds enforced by gate |
| Irrigation context | `IrrigationLink` aggregate | `T0` / `T1` | Operator joins denied |
| Suitability analysis | `SoilCropSuitability` | `T0` | Soil semantics cited |
| Drought / pest / stress indicators | `DroughtStressIndicator`, `PestStressIndicator` | `T0` | Non-emergency disclaimer; cites Hydrology / Atmosphere |
| Conservation practices where permitted | `ConservationPractice` aggregate | `T0` / `T1` | Operator joins denied |

### 13.1 Cross-cutting viewing products

These apply to **every** map-bearing surface in this lane:

- **Evidence Drawer** — feature click resolves to `EvidenceBundle` → support, policy, review, release, correction lineage. Missing bundle returns `ABSTAIN` / `ERROR`.
- **Time slider / compare / export** — temporal UI and public-safe export with `ExportReceipt`; export preserves evidence and policy.
- **Trust badges** — release state, sensitivity, freshness, and correction lineage are visible on every layer.
- **Sensitivity-redacted view** — public-safe derivative is the default; steward view is gated.
- **Correction / stale-state view** — corrected and stale records are visibly labeled, not hidden.
- **Focus Mode (governed AI)** — evidence-bounded QA; `ANSWER` / `ABSTAIN` / `DENY` / `ERROR`; no uncited claims; `AIReceipt` recorded.

> [!NOTE]
> **MapLibre is a renderer, not a truth source.** The map shell renders released artifacts and view state. It is never the truth store, publication authority, policy authority, citation authority, or AI authority. Cesium / 3D, where used, consumes the same `EvidenceBundle` and `DecisionEnvelope` as 2D.

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 14. Pipeline shape (RAW → PUBLISHED)

`CONFIRMED` doctrine: Agriculture follows the KFM lifecycle invariant. Promotion is a **governed state transition**, not a file move. Each transition is gated, has required artifacts, and fails closed.

```mermaid
flowchart LR
  RAW["RAW<br/>SourceDescriptor present"]
  QUAR["QUARANTINE<br/>policy/rights failures"]
  WORK["WORK<br/>normalized but unvalidated"]
  PROC["PROCESSED<br/>validated objects + receipts"]
  CAT["CATALOG / TRIPLET<br/>EvidenceBundle + graph"]
  PUB["PUBLISHED<br/>LayerManifest + governed API"]

  RAW -->|"Normalize<br/>(TransformReceipt + PolicyDecision)"| WORK
  RAW -.->|"Quarantine reason"| QUAR
  WORK -->|"Validation<br/>(ValidationReport + RedactionReceipt + AggregationReceipt)"| PROC
  PROC -->|"Catalog closure<br/>(EvidenceBundle + projections)"| CAT
  CAT -->|"Release<br/>(ReleaseManifest + ReviewRecord + RollbackCard)"| PUB
  PUB -.->|"Correction<br/>(CorrectionNotice)"| PUB

  classDef quar fill:#fdecea,stroke:#c0392b,color:#641e16;
  classDef pub fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20;
  class QUAR quar;
  class PUB pub;
```

| Stage | Handling | Gate | Required artifacts | Status |
|---|---|---|---|---|
| **RAW** | Capture immutable source payload or reference with source role, rights, sensitivity, citation, time, hash | `SourceDescriptor` exists | `SourceDescriptor`; payload / reference hash | `PROPOSED` |
| **WORK / QUARANTINE** | Normalize schema, geometry, time, identity, evidence, rights, policy; quarantine failures | Validation + policy gate pass, or quarantine reason recorded | `TransformReceipt`; `ValidationReport` (working); `PolicyDecision` | `PROPOSED` |
| **PROCESSED** | Emit validated normalized objects, receipts, public-safe candidates | `EvidenceRef`, `ValidationReport`, digest closure | `ValidationReport` pass; `RedactionReceipt` if sensitivity applies; `AggregationReceipt` if aggregation applies | `PROPOSED` |
| **CATALOG / TRIPLET** | Emit catalog records, `EvidenceBundle`, graph / triplet projections, release candidates | Catalog / proof closure passes | `CatalogMatrix` entry; `EvidenceBundle`; graph / triplet projections | `PROPOSED` |
| **PUBLISHED** | Serve released public-safe artifacts through governed APIs and manifests | Review where required; rollback target; correction path | `ReleaseManifest`; `RollbackCard`; `CorrectionNotice` path; `ReviewRecord` | `PROPOSED` |

### 14.1 Failure-closed outcomes

- Source not admitted → logged as candidate, awaits steward.
- Normalization fails → `QUARANTINE` with structured reason; never silently promotes.
- Validation fails → stay in `WORK`; structured `FAIL` outcome.
- Catalog closure fails → `HOLD` at `PROCESSED`; no public edge.
- Release prerequisites missing → `HOLD` at `CATALOG`; no public surface change.

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 15. First credible thin slice

`PROPOSED` first credible slice (per Encyclopedia §7.7 and Atlas v1.1 Ch. 9):

> **One county-level, crop-year panel using CDL + QuickStats, joined to SSURGO suitability and a Kansas Mesonet weather fixture — with field-level detail denied by default.**

### 15.1 Definition of Done (`PROPOSED`)

- [ ] `SourceDescriptor` exists for NASS CDL, NASS QuickStats, SSURGO (cited from Soil), and one Mesonet station.
- [ ] `CropObservation` and `YieldObservation` schemas pin to `schemas/contracts/v1/domains/agriculture/` and load valid + invalid fixtures.
- [ ] `SoilCropSuitability` cites Soil MUKEY via governed join; never re-defines soil semantics.
- [ ] Policy bundle denies field-level publication absent `AggregationReceipt` + `ReviewRecord`.
- [ ] Validation suite covers: source rights present, county aggregation threshold respected, sensitivity tier recorded, evidence closure, digest stability (`spec_hash`).
- [ ] `EvidenceBundle` resolves for every public claim on the county-year panel.
- [ ] `LayerManifest` references only released bundles.
- [ ] Evidence Drawer payload renders with source, time, sensitivity, release, and correction lineage.
- [ ] `ReleaseManifest` and `RollbackCard` exist; rollback drill is documented.
- [ ] Focus Mode QA on the panel returns `ANSWER` with citations *or* `ABSTAIN` — never uncited.
- [ ] Connectors emit to `data/raw/agriculture/`, never directly to `data/processed/` or `data/published/`.

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 16. Validation & review

### 16.1 How the lane is checked (`PROPOSED`)

| Concern | Validator / check (proposed) | Lives in |
|---|---|---|
| Schema shape | JSON Schema validation | `tools/validators/` against `schemas/contracts/v1/domains/agriculture/` |
| Policy gates | OPA / Conftest bundles | `policy/domains/agriculture/` |
| Sensitivity transforms | Redaction / aggregation receipt presence | `tools/validators/sensitivity/` |
| Evidence closure | `EvidenceBundle` resolution check | `tools/validators/evidence/` |
| Cross-lane joins | Constraint check (no operator joins in public) | `tools/validators/cross-lane/` |
| Lifecycle skips | Pipeline auditor (no `raw → published` jumps) | `tools/validators/lifecycle/` |
| README contract drift | README scan against Directory Rules §15 | `tools/validators/docs/` |

### 16.2 Review burden (`PROPOSED`)

| Change class | Reviewers required |
|---|---|
| README content / scope | Docs steward + Agriculture domain steward |
| Object family additions / renames | Agriculture domain steward + ADR |
| Schema home migration | Schemas steward + ADR (per ADR-0001) |
| Policy bundle changes | Policy steward + Agriculture domain steward |
| Sensitivity tier change | Agriculture domain steward + Privacy / rights reviewer |
| Cross-lane edge to People/Land | Agriculture steward + People/Land steward + rights reviewer |
| Release manifest | Release authority distinct from author (when materiality applies) |

CODEOWNERS entries are `PROPOSED` and depend on mounted-repo `CODEOWNERS` file.

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 17. Verification backlog

Items copied forward from Atlas v1.1 Ch. 9 §N. Each is `NEEDS VERIFICATION` until mounted-repo evidence (files, schemas, registry entries, tests, logs, emitted artifacts, review records, or release manifests) settles it.

- [ ] **Verify NASS CDL + QuickStats + Crop Progress activation.** Evidence: connector specs, source descriptors, ingestion logs, terms.
- [ ] **Verify Kansas Mesonet and HLS / SMAP product terms.** Evidence: rights documents, source descriptors, attribution records.
- [ ] **Verify public release sensitivity rules for farm / operator joins.** Evidence: policy bundles in `policy/domains/agriculture/`, deny-by-default register entries.
- [ ] **Verify Agriculture API and layer registry.** Evidence: governed-API route table, layer manifests under `data/published/layers/agriculture/`.
- [ ] **Verify ADR linkage for schema home defaults.** Evidence: `docs/adr/ADR-0001-schema-home.md` and any agriculture-specific ADRs.
- [ ] **Verify presence of `AggregationReceipt` schema and validator.** Evidence: schema file and fixture coverage.
- [ ] **Verify cross-lane join contracts with Soil, Hydrology, Atmosphere/Air, People/Land.** Evidence: cross-lane contracts under `contracts/` or `docs/architecture/`.
- [ ] **Verify rollback drill artifact for the first credible thin slice.** Evidence: `release/rollback_cards/` entry plus drill log.

Open and track these in `docs/registers/VERIFICATION_BACKLOG.md`.

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 18. Related folders & docs

> Internal links — relative when both targets are inside `docs/`. All targets `PROPOSED` until verified in the mounted repo.

**Sibling domains**

- [`../soil/`](../soil/) — owns Soil semantics; agriculture cites MUKEY, components, hydrologic group
- [`../hydrology/`](../hydrology/) — owns water observations, NFHL; agriculture cites for irrigation and drought
- [`../atmosphere/`](../atmosphere/) — owns weather and AOD; agriculture cites for stress and growing-season context
- [`../hazards/`](../hazards/) — owns drought / disaster events; agriculture supplies indicator context
- [`../people-dna-land/`](../people-dna-land/) — owns parcels, ownership, living-person privacy; agriculture joins restricted
- [`../flora/`](../flora/) — owns plant taxa; agriculture does not own vegetation truth
- [`../frontier-matrix/`](../frontier-matrix/) — county-year panels cite agriculture

**Doctrine**

- [`../../doctrine/lifecycle-law.md`](../../doctrine/lifecycle-law.md) — RAW → PUBLISHED invariant *(PROPOSED)*
- [`../../doctrine/truth-posture.md`](../../doctrine/truth-posture.md) — cite-or-abstain *(PROPOSED)*
- [`../../doctrine/trust-membrane.md`](../../doctrine/trust-membrane.md) — public clients use governed APIs *(PROPOSED)*
- [`../../doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement law (§12 Domain Placement Law; §15 README Contract)

**Architecture**

- [`../../architecture/governed-api.md`](../../architecture/governed-api.md) — finite-outcome envelope *(PROPOSED)*
- [`../../architecture/map-shell.md`](../../architecture/map-shell.md) — MapLibre is downstream of trust *(PROPOSED)*
- [`../../architecture/contract-schema-policy-split.md`](../../architecture/contract-schema-policy-split.md) — meaning / shape / decision split *(PROPOSED)*

**Cross-root lanes (paths `PROPOSED`)**

- `contracts/domains/agriculture/`
- `schemas/contracts/v1/domains/agriculture/`
- `policy/domains/agriculture/`
- `tests/domains/agriculture/`
- `fixtures/domains/agriculture/`
- `pipelines/domains/agriculture/`
- `pipeline_specs/agriculture/`
- `data/raw/agriculture/`, `data/work/agriculture/`, `data/quarantine/agriculture/`, `data/processed/agriculture/`, `data/catalog/domain/agriculture/`, `data/published/layers/agriculture/`, `data/registry/sources/agriculture/`
- `release/candidates/agriculture/`

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 19. ADRs

| ADR | Topic | Status |
|---|---|---|
| `ADR-0001` | Schema home (`schemas/contracts/v1/...` canonical) | Accepted *(PROPOSED — verify in `docs/adr/`)* |
| *TODO* | Agriculture aggregation thresholds (k-cell, county, HUC) | `PROPOSED` |
| *TODO* | Agriculture × People/Land join policy | `PROPOSED` |
| *TODO* | Indicator-vs-advisory boundary for `DroughtStressIndicator` / `PestStressIndicator` | `PROPOSED` |
| *TODO* | NASS / Mesonet / HLS / SMAP rights handling | `PROPOSED` |

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## 20. FAQ

<details>
<summary><strong>Why isn't there an <code>agriculture/</code> folder at the repo root?</strong></summary>

Per Directory Rules §3 and §12, **a folder MUST appear at repo root only if it carries one or more repo-wide responsibilities**. "Agriculture" is a domain, not a repo-wide responsibility. Domains live as **segments** inside responsibility roots: `docs/domains/agriculture/`, `schemas/contracts/v1/domains/agriculture/`, `policy/domains/agriculture/`, and so on. A root-level `agriculture/` folder is the §13.4 anti-pattern — *Domain folders becoming root folders and fragmenting the lifecycle.*
</details>

<details>
<summary><strong>Can I publish a field-level crop map?</strong></summary>

Not by default. Field-level publication requires:

1. Rights confirmation from the source steward.
2. Sensitivity tier review (default `T1` after generalization; `T4` if operator-identifiable).
3. A recorded `AggregationReceipt` or `RedactionReceipt`.
4. A `ReviewRecord` and (for `T1` → `T0`) a `ReleaseManifest`.

Without those, the field-level publish path **fails closed** at the policy gate. Aggregate (county / HUC / grid) products are the public default.
</details>

<details>
<summary><strong>Is <code>SoilCropSuitability</code> agriculture or soil?</strong></summary>

It is an **agriculture** object family. Soil owns `SoilMapUnit`, `SoilComponent`, `Horizon`, `HydrologicSoilGroup`, and so on. Agriculture **cites** those via a governed join (e.g., `MUKEY`) and emits its own derived suitability object. The suitability *interpretation* is agriculture's responsibility; the soil *semantics* remain Soil's authority.
</details>

<details>
<summary><strong>Can the agriculture lane issue drought advisories?</strong></summary>

No. Agriculture emits `DroughtStressIndicator` as a **public-safe indicator** — it is descriptive, evidence-bound, and uncertainty-labeled. KFM is **not** an emergency-alert authority; that boundary holds for all lanes (Atlas v1.1 §24.5 hazards row: *T4 forever*). Treatment recommendations are likewise out of scope for `PestStressIndicator`.
</details>

<details>
<summary><strong>What goes in <code>contracts/domains/agriculture/</code> vs. <code>schemas/contracts/v1/domains/agriculture/</code>?</strong></summary>

Per Directory Rules §13.1 and ADR-0001:

- **`contracts/domains/agriculture/`** — Markdown that defines what each object **means** (semantics, source-role constraints, temporal handling, identity rule).
- **`schemas/contracts/v1/domains/agriculture/`** — JSON Schema (or equivalent) that defines what each object **looks like** on the wire.

Two parallel schema homes is a §13.1 anti-pattern. The `schemas/` path is canonical; `contracts/` carries semantic Markdown only.
</details>

<details>
<summary><strong>How does Focus Mode behave on agriculture surfaces?</strong></summary>

Focus Mode is evidence-bounded QA with finite outcomes: `ANSWER` (cited), `ABSTAIN`, `DENY`, or `ERROR`. Every reply on an agriculture surface must:

- Resolve `EvidenceRef` → released `EvidenceBundle`.
- Pass policy and sensitivity checks (no operator-identifying claims; no advisory framing).
- Record an `AIReceipt`.

Uncited generation is `DENY`; missing bundle is `ABSTAIN` / `ERROR`. Generated language never substitutes for evidence, policy, review state, or release state.
</details>

<details>
<summary><strong>Where do <code>AggregationReceipt</code> and <code>RedactionReceipt</code> live?</strong></summary>

Trust-bearing receipts live under `data/receipts/` and `data/proofs/` — **not** under `artifacts/`. Putting receipts in `artifacts/` is the §13.2 anti-pattern (*mixing proof, process memory, build output, and release decisions*). `artifacts/` is for build / docs / qa / temporary content only.
</details>

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

## Appendix

<details>
<summary><strong>A. Atlas v1.1 Ch. 9 — Agriculture: section anchors</strong></summary>

| Atlas section | Topic | Mapped here |
|---|---|---|
| §9.A | Domain identity and one-line purpose | §1 Purpose |
| §9.B | Scope, boundary, explicit non-ownership | §2 Scope & boundary |
| §9.C | Ubiquitous language | §8 |
| §9.D | Key source families | §10 |
| §9.E | Main object families | §9 |
| §9.F | Cross-lane relations | §11 |
| §9.G | Map and viewing products | §13 |
| §9.H | Pipeline shape (RAW → PUBLISHED) | §14 |
| §9.I | AI and Focus Mode possibilities | §13.1 |
| §9.M | Publication, correction, rollback | §14, §16 |
| §9.N | Verification backlog | §17 |
</details>

<details>
<summary><strong>B. Programming-possibilities backlog placement</strong></summary>

Per Encyclopedia §12 (Programming Possibilities Backlog), Agriculture sits in **Phase 5 — Domain expansion**, after the trust spine (Phase 0), hydrology proof lane (Phase 1), soil/habitat/fauna (Phase 2), MapLibre + Evidence Drawer (Phase 3), and governed AI Focus Mode (Phase 4). All phases are `PROPOSED`.

Rollback path for the Agriculture slice: per-domain rollback via `RollbackCard`; disable sensitive joins on failure.
</details>

<details>
<summary><strong>C. Anti-patterns to avoid in this lane</strong></summary>

From Directory Rules §13 and Atlas v1.1 §24.9, applied to Agriculture:

| Anti-pattern | What it looks like here | Counter-rule |
|---|---|---|
| Domain folder at repo root | `agriculture/` at root with its own `data/`, `schemas/`, etc. | Use the lane pattern (§5) |
| Parallel schema home | `contracts/domains/agriculture/*.schema.json` and `schemas/contracts/v1/domains/agriculture/*.schema.json` diverge | `schemas/` canonical; `contracts/` is semantic Markdown only |
| Public route reads canonical store | UI reads `data/processed/agriculture/` directly | Go through governed API |
| Connector publishes | An ag connector writes to `data/processed/agriculture/` | Connectors emit to `data/raw/` or `data/quarantine/` |
| Watcher publishes | A worker writes to `data/published/layers/agriculture/` | Watcher-as-non-publisher: emit candidates and receipts only |
| Lifecycle skip | Pipeline writes `data/raw/agriculture/` → `data/published/...` | All phases run; promotion is governed |
| Trust content in `artifacts/` | `AggregationReceipt` or `ReleaseManifest` lands in `artifacts/` | Receipts → `data/receipts/` / `data/proofs/`; release → `release/` |
| Documentation as truth | A statement in this README cited as the canonical decision | Promote to ADR or `control_plane/` register |
</details>

<details>
<summary><strong>D. Glossary cross-reference</strong></summary>

Terms used here that live in other lanes or in cross-cutting doctrine:

- `EvidenceBundle`, `EvidenceRef` — cross-cutting (ENCY doctrine)
- `SourceDescriptor` — owned by source steward (cross-cutting)
- `LayerManifest` — owned by MapLibre / governed API
- `ReleaseManifest`, `RollbackCard`, `CorrectionNotice` — owned by release authority (`release/`)
- `ValidationReport`, `RunReceipt`, `DecisionEnvelope` — cross-cutting trust artifacts
- `AIReceipt`, `RuntimeResponseEnvelope` — owned by Governed AI doctrine
- `MUKEY`, `SoilMapUnit`, `SoilComponent`, `Horizon`, `HydrologicSoilGroup` — owned by **Soil**
- `HUC`, `Watershed`, `Reach`, `GaugeSite`, `FlowObservation`, `NFHLZone` — owned by **Hydrology**
- `WeatherObservation`, `ClimateNormal` — owned by **Atmosphere / Air**
- `LandParcel`, `PersonAssertion` — owned by **People / Land**
- `FrontierDefinition`, `CountyYearPanel` — owned by **Frontier Matrix**
</details>

[Back to top ↑](#-agriculture--kfm-domain-lane)

---

### Related docs

- Atlas: `KFM Domains Culmination Atlas v1.1` — Ch. 9 (Agriculture); Ch. 24.5 (Sensitivity tiers); Ch. 24.6 (Pipeline gates)
- Encyclopedia: `KFM Domain and Capability Encyclopedia v0.1` — §7.7 (Agriculture)
- Build Manual: `KFM Unified Implementation Architecture Build Manual` — §6.12 (Agriculture)
- Dossier: `KFM_Agriculture_Domain_Implementation_Dossier_REVISED_2026-04-21.pdf` (SRC-028)
- Doctrine: `docs/doctrine/directory-rules.md` §12 (Domain Placement Law), §15 (README Contract)
- Sibling lane READMEs: `docs/domains/{soil,hydrology,atmosphere,hazards,people-dna-land,flora,frontier-matrix}/README.md` *(PROPOSED)*

<a id="last-updated"></a>**Last updated:** `2026-05-15` · **Lane README version:** `v1 (PROPOSED)` · **Doctrine basis:** Atlas v1.1 (2026-05-12)

[⤴ Back to top](#-agriculture--kfm-domain-lane)
