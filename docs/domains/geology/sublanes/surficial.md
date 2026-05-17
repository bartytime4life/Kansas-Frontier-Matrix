<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/geology-sublane-surficial
title: Geology · Surficial Sublane
type: standard
version: v0.1
status: draft
owners: <kfm-geology-stewards>  <!-- PLACEHOLDER — confirm with CODEOWNERS -->
created: 2026-05-17
updated: 2026-05-17
policy_label: public
related:
  - docs/domains/geology/README.md
  - docs/standards/PROV.md
  - docs/standards/PMTILES.md
  - docs/standards/OGC-API-TILES.md
  - directory-rules.md
tags: [kfm, domain, geology, surficial, sublane, standard]
notes:
  - "Sublane segment 'docs/domains/<domain>/sublanes/<name>.md' is PROPOSED; Directory Rules do not yet define it. ADR recommended."
  - "Implementation-layer claims are PROPOSED pending mounted-repo verification."
[/KFM_META_BLOCK_V2] -->

# Geology · Surficial Sublane

> Governing doctrine for the **surficial** facet of the Kansas Frontier Matrix Geology domain — Quaternary and unconsolidated map units, their evidence, lifecycle, cross-lane relations, and public-safe release posture.

![status](https://img.shields.io/badge/status-draft-yellow)
![type](https://img.shields.io/badge/type-domain%20doctrine-blue)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-purple)
![policy](https://img.shields.io/badge/policy-public%E2%80%93with%20gates-green)
![placement](https://img.shields.io/badge/placement-PROPOSED-orange)
<!-- TODO: replace placeholder badge URLs once CI, owners, and registry IDs are confirmed against the mounted repo. -->

| Field        | Value |
|---           |---    |
| **Status**   | Draft — doctrine grounded, implementation claims PROPOSED |
| **Owners**   | `<kfm-geology-stewards>` *(placeholder — confirm against `CODEOWNERS`)* |
| **Updated**  | 2026-05-17 |
| **Scope**    | Surficial sublane of the Geology domain — Quaternary deposits, unconsolidated cover, surficial map units |
| **Parent**   | `docs/domains/geology/README.md` *(PROPOSED parent landing page)* |

---

## Contents

1. [Scope and boundary](#1-scope-and-boundary)
2. [Repo placement and the sublane segment](#2-repo-placement-and-the-sublane-segment)
3. [Ubiquitous language](#3-ubiquitous-language)
4. [Source families](#4-source-families)
5. [Object families owned in this sublane](#5-object-families-owned-in-this-sublane)
6. [Spatial and temporal model](#6-spatial-and-temporal-model)
7. [Pipeline shape — RAW → PUBLISHED](#7-pipeline-shape--raw--published)
8. [Map and viewing products](#8-map-and-viewing-products)
9. [Cross-lane relations](#9-cross-lane-relations)
10. [Sensitivity, rights, and publication posture](#10-sensitivity-rights-and-publication-posture)
11. [Publication, correction, and rollback](#11-publication-correction-and-rollback)
12. [Verification backlog and open questions](#12-verification-backlog-and-open-questions)
13. [Related docs](#13-related-docs)

---

## 1. Scope and boundary

> [!NOTE]
> The Geology domain **CONFIRMED owns** bedrock geology, surficial geology, geologic age, structures, geomorphology, boreholes, well logs, cores, geophysics, geochemistry, minerals, oil/gas/resource deposits, and extraction/reclamation context. This sublane governs the **surficial** facet only.

**This sublane owns the doctrinal handling of surficial map material within Geology**: the depiction, evidence support, lifecycle, and release of surficial map units (Quaternary alluvium, terrace deposits, eolian/loess cover, glacial materials where applicable, colluvium, residuum), the surficial-context fraction of `GeologyBoundaryVersion`, and the cross-lane bridges from surficial material into adjacent lanes.

**It explicitly does not own:**

- **Bedrock** unit truth, lithology of consolidated rock, or stratigraphic correlation below the surficial mantle — those belong to other Geology sublanes (PROPOSED: `bedrock`, `stratigraphy`, `structures`).
- **Soil** map units, components, horizons, or soil properties — Soil retains canonical authority. The Geology→Soil cross-lane is **parent material and surficial context** only (CONFIRMED doctrine).
- **Hydrology** measurements, regulatory flood zones, or aquifer water-level truth — Hydrology retains canonical authority. The Geology→Hydrology cross-lane is **hydrostratigraphy and aquifer context without replacing measurements** (CONFIRMED doctrine).
- **Hazards risk** (landslide, subsidence, liquefaction) — Hazards retains canonical risk authority. Surficial context informs but does not own risk (CONFIRMED doctrine).
- **Archaeology, ownership/lease/permit/title claims, and UI/AI statements** — these remain outside canonical Geology truth (CONFIRMED doctrine).

> [!IMPORTANT]
> Per corpus pattern (PROPOSED organizational decomposition, CONFIRMED anti-collapse principle): bedrock, surficial geology, stratigraphy, lithology, structures, geomorphology, boreholes, geophysics, geochemistry, mineral occurrences, extraction sites, and public-safe resource layers are kept **distinct** within Geology. A surficial polygon is not a soil mapunit; a Quaternary cover is not a bedrock unit; and neither is automatically a public truth claim.

[⬆ Back to top](#contents)

---

## 2. Repo placement and the sublane segment

> [!CAUTION]
> The path segment `docs/domains/<domain>/sublanes/<name>.md` is **PROPOSED**. `directory-rules.md` defines the `docs/domains/<domain>/` lane (§4 Step 3, §12 Domain Placement Law) but does not currently define a `sublanes/` segment. The flat alternative `docs/domains/geology/surficial.md` is permitted by the existing lane rule. Choose-and-freeze recommended via ADR; until then, this segment is **PROPOSED / NEEDS VERIFICATION**.

The repo-placement basis for this file:

| Concern | Rule | Status |
|---|---|---|
| Domain lives as a **segment** inside a responsibility root, not as a root folder | `directory-rules.md` §4 Step 3, §12 | CONFIRMED rule |
| Human-facing explanation goes under `docs/` | `directory-rules.md` §4 Step 1 placement table | CONFIRMED rule |
| Geology lane appears as `docs/domains/geology/...` | `directory-rules.md` §12 (uniform domain pattern) | CONFIRMED rule |
| `sublanes/` as an intra-domain segment | Not defined in `directory-rules.md` | **PROPOSED** convention — ADR recommended |
| Co-lane homes for schemas, policy, fixtures, lifecycle data | `directory-rules.md` §12 | CONFIRMED rule; per-sublane sub-segments are **PROPOSED** until ADR |

### How this sublane fits the Geology lane

```mermaid
flowchart TB
    classDef domain fill:#eef,stroke:#225,stroke-width:2px,color:#000
    classDef sublane fill:#fff,stroke:#888,color:#000
    classDef focus fill:#ffd,stroke:#b80,stroke-width:3px,color:#000
    classDef adj fill:#efe,stroke:#272,color:#000

    GEOL["Geology domain<br/>(CONFIRMED owner)"]:::domain
    BED["bedrock"]:::sublane
    SUR["surficial<br/>(this doc)"]:::focus
    STR["structures"]:::sublane
    STRAT["stratigraphy"]:::sublane
    LITH["lithology"]:::sublane
    BORE["boreholes / well logs"]:::sublane
    GEO["geophysics / geochemistry"]:::sublane
    RES["resources / minerals"]:::sublane
    REC["extraction / reclamation"]:::sublane
    HYDS["hydrostratigraphy"]:::sublane

    GEOL --> BED
    GEOL --> SUR
    GEOL --> STR
    GEOL --> STRAT
    GEOL --> LITH
    GEOL --> BORE
    GEOL --> GEO
    GEOL --> RES
    GEOL --> REC
    GEOL --> HYDS

    SOIL["Soil<br/>(parent material owner)"]:::adj
    HYD["Hydrology<br/>(aquifer/measurement owner)"]:::adj
    HAZ["Hazards<br/>(risk owner)"]:::adj
    ARCH["Archaeology<br/>(site owner, deny-default)"]:::adj

    SUR -. "parent-material / surficial<br/>context (advisory)" .-> SOIL
    SUR -. "surficial aquifer /<br/>hydrostratigraphic context" .-> HYD
    SUR -. "landslide / subsidence /<br/>liquefaction context" .-> HAZ
    SUR -. "Quaternary stratigraphic<br/>context (no exact sites)" .-> ARCH
```

> [!NOTE]
> The sublane breakdown of Geology shown above (bedrock, surficial, structures, …) is **CONFIRMED as a corpus organizational pattern** for keeping Geology objects distinct (anti-collapse). Whether each appears as a literal `sublanes/<name>` directory or as a flat file under `docs/domains/geology/` is **PROPOSED** and remains an open ADR question. *See* [§12](#12-verification-backlog-and-open-questions).

### Co-lane companions (PROPOSED, pending ADR)

If the `sublanes/` convention is accepted, this sublane is expected to have parallel companions under the corresponding responsibility roots. None of the following paths are claimed to exist in the current repo:

```text
docs/domains/geology/sublanes/surficial.md                          ← this file
contracts/domains/geology/sublanes/surficial/                       ← PROPOSED
schemas/contracts/v1/domains/geology/sublanes/surficial/            ← PROPOSED (per ADR-0001 schema-home rule)
policy/domains/geology/sublanes/surficial/                          ← PROPOSED
tests/domains/geology/sublanes/surficial/                           ← PROPOSED
fixtures/domains/geology/sublanes/surficial/                        ← PROPOSED
pipelines/domains/geology/                                          ← PROPOSED (sublane segment optional)
pipeline_specs/geology/                                             ← PROPOSED
data/raw/geology/                                                   ← PROPOSED (lifecycle root)
data/published/layers/geology/surficial/                            ← PROPOSED
data/registry/sources/geology/                                      ← PROPOSED
release/candidates/geology/                                         ← PROPOSED
```

> [!WARNING]
> All paths above are **PROPOSED / NEEDS VERIFICATION** without mounted-repo inspection. Per `directory-rules.md` Step 4–5 (Confirm authority; Cite the rule), creation of any new canonical sibling under `data/`, a new compatibility root, or any divergent schema/policy home requires an ADR.

[⬆ Back to top](#contents)

---

## 3. Ubiquitous language

| Term | Status | Definition |
|---|---|---|
| **SurficialUnit** | CONFIRMED term / PROPOSED field realization | A delimited body of unconsolidated or semi-consolidated material at or near the land surface (alluvium, terrace, eolian, loess, colluvium, residuum, glacial where applicable). Meaning is constrained by source role, evidence, time, and release state. |
| **GeologyBoundaryVersion** | CONFIRMED term / PROPOSED field realization | A versioned snapshot of unit boundaries, including the surficial subset. Carries source authority, vintage, and digest. |
| **Lithology** *(of surficial cover)* | CONFIRMED term / PROPOSED field realization | The compositional character of a surficial body (sand, silt, clay, gravel, loess, organic) — referenced, not duplicated, when surficial units share a controlled lithology vocabulary. |
| **Hydrostratigraphic Unit** *(surficial fraction)* | CONFIRMED term / PROPOSED field realization | The surficial portion of a hydrostratigraphic frame (e.g., alluvial aquifer cover). Surfaces here are **advisory context** for Hydrology; Hydrology owns measurement truth. |
| **Surficial Map Unit (public-safe derivative)** | PROPOSED | A generalized, release-stage derivative of `SurficialUnit` suitable for public delivery (PMTiles/COG), with explicit generalization and rights provenance. |
| **Quaternary Context** | PROPOSED (definitional) | The temporal frame within which most surficial units fall. Tracked via `temporal_scope` on the object identity rule. Not a substitute for stratigraphic correlation truth. |

> [!NOTE]
> KFM-specific casing is preserved: `SurficialUnit`, `GeologyBoundaryVersion`, `Hydrostratigraphic Unit`. Do not silently rewrite to generic equivalents (`surficial_unit`, `boundaryVersion`, etc.) — these names are part of the project's ubiquitous language.

[⬆ Back to top](#contents)

---

## 4. Source families

Surficial mapping draws from a subset of the Geology domain's source families. The first three rows are CONFIRMED corpus citations for the Geology lane; the remainder are referenced where applicable to surficial workstreams. Rights, current terms, and freshness cadence are NEEDS VERIFICATION per source.

| Source family | Role *(per source-role registry)* | Surficial relevance | Rights / sensitivity | Freshness | Status |
|---|---|---|---|---|---|
| **Kansas Geological Survey data and maps** | authority / observation / context / model (per source role) | Primary Kansas surficial coverage | Sensitive joins fail closed; current terms NEEDS VERIFICATION | Source-vintage or cadence specific | CONFIRMED listed; rights NEEDS VERIFICATION |
| **KGS surficial geology and geologic maps** | authority / observation / context / model | Direct surficial unit mapping authority for Kansas | Sensitive joins fail closed; current terms NEEDS VERIFICATION | Source-vintage or cadence specific | CONFIRMED listed; rights NEEDS VERIFICATION |
| **USGS NGMDB and GeMS** | authority / observation / context / model | National geologic map database; GeMS schema for surficial map data interchange | Sensitive joins fail closed; current terms NEEDS VERIFICATION | Source-vintage or cadence specific | CONFIRMED listed; rights NEEDS VERIFICATION |
| **3DEP / terrain** | observation / context | Surficial unit delineation often draws on terrain derivatives (slope, curvature, relative relief) | Public-domain, but **EXTERNAL** lineage and STAC metadata gates apply | Source-vintage specific | CONFIRMED related; surficial use PROPOSED |
| **KGS/KDHE WWC5 and water-well program** | observation / context (adjacent) | Drillers' logs constrain surficial thickness/contacts | Sensitive joins fail closed | Source-vintage | CONFIRMED listed in Geology lane; surficial use PROPOSED |
| **Soil parent material** *(Soil lane)* | adjacent / advisory only | Soil parent-material attributes provide **adjacent** lineage; Geology does **not** consume Soil as truth | Per Soil lane sensitivity rules | Per Soil cadence | Adjacent — Soil owns |

> [!IMPORTANT]
> Each source carries a **source role** (authority, observation, context, model) that gates how derived claims may be presented. A KGS surficial map can be cited as **authority** for its mapped extent; a terrain-derivative classification is at best **model** output and must be labeled as such.

[⬆ Back to top](#contents)

---

## 5. Object families owned in this sublane

Object identity in KFM follows the **PROPOSED deterministic basis**: `source id + object role + temporal scope + normalized digest`. **CONFIRMED temporal handling** requires source, observed, valid, retrieval, release, and correction times to remain distinct where material.

| Object | Owner | Surficial relevance | Identity rule | Temporal handling |
|---|---|---|---|---|
| **SurficialUnit** | This sublane | Primary unit — owns the surficial map unit lifecycle | PROPOSED deterministic basis | CONFIRMED distinct temporal fields |
| **GeologyBoundaryVersion** *(surficial fraction)* | Geology domain (shared) | Boundary version snapshot scoped to surficial polygons | PROPOSED deterministic basis | CONFIRMED distinct temporal fields |
| **Lithology** *(surficial reference)* | Geology domain (shared) | Compositional reference for surficial bodies | PROPOSED deterministic basis | CONFIRMED distinct temporal fields |
| **HydrostratigraphicUnit** *(surficial portion only)* | Geology domain (shared) | Surficial cap of a hydrostratigraphic frame; advisory to Hydrology | PROPOSED deterministic basis | CONFIRMED distinct temporal fields |
| **BoreholeReference** *(surficial intersection)* | Geology domain (boreholes sublane) | **Referenced**, not owned here — surficial thickness/contacts derived from logs | PROPOSED deterministic basis | CONFIRMED distinct temporal fields |

> [!NOTE]
> Cross-sublane references must resolve through **`EvidenceRef → EvidenceBundle`**, not via direct database joins. A surficial polygon's claim that "alluvial cover thickness here is ~6 m" is supported by a bundled set of borehole references (with role = observation), terrain context (role = model), and source map (role = authority).

[⬆ Back to top](#contents)

---

## 6. Spatial and temporal model

**Geometry (CONFIRMED doctrine, applied):** polygons for surficial units; lines for surficial contacts when delivered separately; points only when a surficial sample is the object (rare — usually a `BoreholeReference` instead); rasters only for terrain-derivative companions, not as a substitute for mapped polygons.

**Generalization rule (PROPOSED, derived from MapLibre lane doctrine):** delivery to public clients passes through topology-aware simplification (e.g., Mapshaper / TopoJSON-style shared-arc) before tiling, to preserve shared boundaries. Public PMTiles for surficial layers MUST descend from a canonical processed GeoParquet, not from raw source downloads. *See* [`docs/standards/PMTILES.md`](../../../standards/PMTILES.md).

**Temporal model:**

- **Geologic time** — Quaternary frame is the typical scope; capture as part of `temporal_scope` on identity, not as a substitute for stratigraphic correlation.
- **Source vintage** — every release carries the source map's publication and digital release date.
- **System time** — observed, valid, retrieval, release, and correction times remain distinct (CONFIRMED doctrine).
- **Interpretation version** — track interpretation revisions explicitly when a surficial polygon is re-delineated.

<details>
<summary><strong>Geometry-and-precision quick reference</strong> (illustrative)</summary>

| Use | Geometry | Public-precision posture | Note |
|---|---|---|---|
| Polygon unit map | Polygon | Generalized for public PMTiles | Topology-aware simplification required before tile build |
| Unit boundary contact | LineString | Generalized | Boundary line digest tied to the polygon |
| Borehole-derived thickness point | Point | **Referenced**, not the canonical object | Borehole sublane is canonical |
| Terrain derivative (slope, relief) | Raster (COG) | Public-safe with COG profile + STAC | Treat as **model** role; never as observation |
| 3D subsurface volume | Volume / voxel | Conditional only; reality-boundary controls apply | Per `MAP-MASTER` 2D-default doctrine |

*Illustrative; not a schema declaration.*

</details>

[⬆ Back to top](#contents)

---

## 7. Pipeline shape — RAW → PUBLISHED

**CONFIRMED doctrine / PROPOSED sublane application:** the surficial sublane follows the same lifecycle as the Geology domain and all other KFM domains. Promotion is a **governed state transition**, not a file move.

| Stage | Handling | Gate | Status |
|---|---|---|---|
| **RAW** | Capture immutable source payload or reference with source role, rights, sensitivity, citation, time, and hash. | `SourceDescriptor` exists | PROPOSED |
| **WORK / QUARANTINE** | Normalize schema, geometry, time, identity, evidence, rights, and policy; hold failures. | Validation and policy gate pass, or quarantine reason recorded | PROPOSED |
| **PROCESSED** | Emit validated normalized objects, receipts, and public-safe candidates (e.g., canonical GeoParquet of surficial polygons). | `EvidenceRef`, `ValidationReport`, and digest closure exist | PROPOSED |
| **CATALOG / TRIPLET** | Emit catalog records (STAC/DCAT), EvidenceBundles, graph/triplet projections, and release candidates. | Catalog/proof closure passes | PROPOSED |
| **PUBLISHED** | Serve released public-safe artifacts (PMTiles, COG, generalized GeoJSON) through governed APIs and manifests. | `ReleaseManifest`, correction path, rollback target, review/policy state exist | PROPOSED |

```mermaid
flowchart LR
    RAW["RAW<br/>SourceDescriptor"] --> WQ["WORK / QUARANTINE<br/>Validation + Policy"]
    WQ --> PROC["PROCESSED<br/>GeoParquet + RunReceipt"]
    PROC --> CAT["CATALOG / TRIPLET<br/>STAC / DCAT / EvidenceBundle"]
    CAT --> PUB["PUBLISHED<br/>PMTiles · COG · LayerManifest"]

    WQ -. quarantine .-> QH["quarantine hold<br/>with reason"]
    PUB -. correction .-> CN["CorrectionNotice"]
    PUB -. rollback .-> RB["RollbackCard"]

    classDef gate fill:#eef,stroke:#225,color:#000
    classDef hold fill:#fee,stroke:#a22,color:#000
    classDef post fill:#efe,stroke:#272,color:#000
    class RAW,WQ,PROC,CAT,PUB gate
    class QH hold
    class CN,RB post
```

> [!WARNING]
> **Watcher-as-non-publisher (CONFIRMED invariant).** A watcher or connector for KGS, NGMDB, or any surficial source emits to `data/raw/` or `data/quarantine/` only. It does **not** write to `data/processed/`, `data/catalog/`, `data/published/`, or `release/`. Promotion is a governed decision (PolicyDecision → PromotionDecision → ReleaseManifest), not a side-effect of a fetch.

[⬆ Back to top](#contents)

---

## 8. Map and viewing products

**PROPOSED domain viewing products (Geology lane corpus):** bedrock unit map; **surficial unit map**; structure/fault view; stratigraphy/correlation view; borehole public-generalized view; mineral occurrence/deposit summary; extraction/reclamation context.

**This sublane's primary product:** the **surficial unit map**, delivered as:

- A canonical processed **GeoParquet** as vector truth (per corpus pattern: "GeoParquet is vector truth for derived tiles").
- A public **PMTiles** layer derived from the GeoParquet (per `docs/standards/PMTILES.md` and the MapLibre delivery doctrine; KGS M-118 is a CONFIRMED candidate source).
- Optional **COG** companions for terrain derivatives (slope, hillshade, relief) when those support unit interpretation.
- A **LayerManifest** linking the layer to its catalog source (STAC/DCAT) and render hints.

**CONFIRMED doctrine cross-cutting viewing products** apply uniformly: Evidence Drawer, time-aware state, trust badges, sensitivity-redacted view, correction / stale-state view, and governed Focus Mode.

> [!IMPORTANT]
> **No popup as Evidence Drawer substitute.** A click on a surficial polygon must resolve through the governed API to an EvidenceBundle, not surface a free-text popup standing in for cited evidence. The popup may summarize and link; the claim resolves in the Drawer.

[⬆ Back to top](#contents)

---

## 9. Cross-lane relations

| This sublane | Related lane | Relation type | Constraint | Status |
|---|---|---|---|---|
| Surficial | **Soil** | Soil consumes surficial as **parent material / surficial context** (advisory; not regulatory or aggregate). Soil owns mapunit/horizon truth. | Preserve ownership, source role, sensitivity, and EvidenceBundle support | CONFIRMED doctrine |
| Surficial | **Hydrology** | Surficial unit and lithology provide **groundwater context (advisory)**; Hydrology owns measurements and regulatory hydrology. | Preserve ownership, source role, sensitivity, and EvidenceBundle support | CONFIRMED doctrine |
| Surficial | **Hazards** | Surficial geology provides **landslide / subsidence / liquefaction context**; Hazards owns risk classification. | Preserve ownership, source role, sensitivity, and EvidenceBundle support | CONFIRMED doctrine |
| Surficial | **Archaeology** | Quaternary stratigraphic context may bound interpretation; Archaeology owns sites and applies **deny-by-default for exact locations**. | Preserve ownership, source role, sensitivity, and EvidenceBundle support; never expose archaeological coordinates as a side-effect of surficial detail | CONFIRMED doctrine (sensitivity); join PROPOSED |
| Surficial | **Spatial Foundation** | Receives CRS, scale, geometry, and layer/representation grammar from Spatial Foundation. | Renderer/Focus surfaces stay downstream of released evidence | CONFIRMED doctrine |
| Surficial | **People / Land** | Lease, parcel, operator relations **cannot prove deposits**; relation is advisory only. | Preserve ownership, source role, sensitivity, and EvidenceBundle support | CONFIRMED doctrine |

> [!NOTE]
> Each cross-lane edge is governed by both lanes simultaneously. A surficial-to-Hydrology link must satisfy this sublane's evidence rules **and** the Hydrology lane's measurement-authority and source-role rules. When in doubt, both lanes get a vote.

[⬆ Back to top](#contents)

---

## 10. Sensitivity, rights, and publication posture

**Default posture:** surficial geology is **broadly public-suitable** when sources are properly cited, generalization is recorded, and rights are confirmed. This sublane is far less sensitive than archaeology, fauna nest sites, or living-person data — but it is **not** unconditionally public.

| Concern | Posture | Basis |
|---|---|---|
| Source rights and licensing for KGS / USGS / NGMDB inputs | Each source's current terms NEEDS VERIFICATION; default deny on rights ambiguity | CONFIRMED corpus rule (KFM-IDX-POL-002, Rights and License Verification Gate) |
| Joins to **extraction sites** or **active mining/leasing** | Restrict; coordinate with the Resources/Reclamation sublanes; advisory only | CONFIRMED corpus rule (anti-collapse for resource layers) |
| Joins to **archaeology** via surficial stratigraphy | **Deny-by-default** for exact archaeological coordinates regardless of surficial precision | CONFIRMED (KFM-IDX-POL-001, Deny-by-Default for Sensitive Exact Locations) |
| Joins to **infrastructure** via surficial substrate | Critical-asset detail is restricted; surficial coverage itself is public-safe | CONFIRMED (Settlements/Infrastructure deny-default for critical-asset detail) |
| Joins to **person / parcel** identifiers | Living-person and person-parcel joins fail closed | CONFIRMED (People/Land deny-default) |
| **Generalization** for public tiles | Topology-aware simplification with a recorded **transform receipt**; never style-only hiding of sensitive geometry | CONFIRMED doctrine ("No sensitive geometry hidden only by style filters") |
| **Vintage / freshness** marking | Required on every released layer; stale-state view available | CONFIRMED cross-cutting doctrine |

> [!WARNING]
> **Cite-or-abstain.** A surficial claim that is not supported by a resolvable `EvidenceBundle` does not become a public truth. The governed API returns **ABSTAIN** rather than fluent prose when an `EvidenceRef` fails to resolve.

[⬆ Back to top](#contents)

---

## 11. Publication, correction, and rollback

Surficial publication requires the full release object set (CONFIRMED doctrine, applied):

- **SourceDescriptor** for every input source family used (KGS, NGMDB, etc.).
- **EvidenceBundle** resolving each public claim (unit identity, mapped extent, vintage).
- **ValidationReport** covering schema, geometry validity, topology, CRS, temporal scope, and policy gates.
- **RunReceipt(s)** capturing the deterministic build of GeoParquet → PMTiles / COG.
- **PolicyDecision** and **PromotionDecision** documenting governed state transitions.
- **ReleaseManifest** binding all of the above to a release id, with `spec_hash` reproducibility.
- **LayerManifest** binding the released MapLibre layer to its catalog source and render hints.
- **CorrectionNotice** template and **RollbackCard** prepared **before** release, not afterward.

> [!IMPORTANT]
> **No release without a rehearsed rollback.** A release plan that lacks a runnable `RollbackCard` is not a release; it is an unreviewed publication path. The Corrections lane provides the public-facing notice channel when a release later proves incorrect.

[⬆ Back to top](#contents)

---

## 12. Verification backlog and open questions

| Item | Evidence that would settle it | Status |
|---|---|---|
| Confirm `docs/domains/geology/sublanes/<name>.md` segment vs flat `docs/domains/geology/<name>.md` | An ADR in `docs/adr/` resolving the intra-domain convention, with a drift entry if existing files conflict | **OPEN** — ADR recommended |
| Confirm `docs/domains/geology/README.md` exists or stands in as Geology lane landing | Mounted-repo `ls` of `docs/domains/geology/` | NEEDS VERIFICATION |
| Confirm the SurficialUnit schema home and contract path | Inspection of `schemas/contracts/v1/domains/geology/` and `contracts/domains/geology/` per ADR-0001 | NEEDS VERIFICATION |
| Confirm KGS surficial source current rights, vintage, and connector status | Mounted-repo `data/registry/sources/geology/` entries; SourceDescriptor; live source terms check | NEEDS VERIFICATION |
| Confirm USGS NGMDB / GeMS schema crosswalk | Mounted-repo schemas; ValidationReport against a GeMS fixture | NEEDS VERIFICATION |
| Confirm KGS M-118 ingestion path → PMTiles | Mounted-repo pipeline_specs / pipelines / fixtures; PMTiles digest receipt | NEEDS VERIFICATION |
| Confirm generalization transform parameters and topology-aware tooling choice | Mounted-repo tool config (e.g., Mapshaper / TopoJSON params); transform receipts | NEEDS VERIFICATION |
| Confirm the surficial LayerManifest binding pattern in `apps/explorer-web/` | Mounted-repo `apps/explorer-web/` + layer registry | NEEDS VERIFICATION |
| Confirm CI/test coverage for surficial fixture (valid + invalid + topology) | Mounted-repo `tests/domains/geology/` + CI logs | NEEDS VERIFICATION |
| Confirm owners line in `CODEOWNERS` for this file | Mounted-repo `CODEOWNERS` inspection | NEEDS VERIFICATION |
| Confirm placement of generalization receipts (in `data/receipts/` vs `data/proofs/`) | Mounted-repo + ADR resolution of the receipts/proofs split | NEEDS VERIFICATION |

[⬆ Back to top](#contents)

---

## 13. Related docs

- [`docs/domains/geology/README.md`](../README.md) — Geology domain landing *(PROPOSED parent — NEEDS VERIFICATION)*
- [`directory-rules.md`](../../../../directory-rules.md) — Repository placement law
- [`docs/standards/PROV.md`](../../../standards/PROV.md) — W3C PROV-O / PAV provenance profile
- [`docs/standards/PMTILES.md`](../../../standards/PMTILES.md) — PMTiles v3 governance and conformance profile
- [`docs/standards/OGC-API-TILES.md`](../../../standards/OGC-API-TILES.md) — OGC API Tiles delivery
- [`docs/standards/ISO-19115.md`](../../../standards/ISO-19115.md) — ISO 19115 crosswalk
- [`docs/standards/OAI-PMH.md`](../../../standards/OAI-PMH.md) — OAI-PMH harvest governance
- *(PROPOSED siblings)* `docs/domains/geology/sublanes/bedrock.md`, `structures.md`, `boreholes.md`, `resources.md`, `reclamation.md`, `hydrostratigraphy.md`
- *(PROPOSED adjacent)* `docs/domains/soil/README.md`, `docs/domains/hydrology/README.md`, `docs/domains/hazards/README.md`

> [!NOTE]
> Relative-link targets above assume the `sublanes/` segment. If the ADR resolves to flat sibling files, link targets shift one level shallower.

---

**Last updated:** 2026-05-17 · **Version:** v0.1 (draft) · **Doc ID:** `kfm://doc/geology-sublane-surficial`

[⬆ Back to top](#contents)
