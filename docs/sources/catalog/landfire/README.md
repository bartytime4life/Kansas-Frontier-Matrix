<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-landfire-readme
title: LANDFIRE source family — Catalog README
type: readme
subtype: source-family-readme
version: v0.2
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward for landfire + Hazards/Habitat/Flora/Fauna domain stewards>
created: 2026-05-21
updated: 2026-05-21
policy_label: public
related:
  - docs/sources/catalog/README.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/PROFILES.md
  - docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - docs/sources/catalog/OPEN-QUESTIONS.md
  - docs/sources/catalog/_template/SOURCE_PRODUCT_TEMPLATE.md
  - docs/sources/catalog/landfire/landfire.md
  - docs/sources/catalog/isric/README.md
  - docs/sources/catalog/usgs/README.md
  - docs/sources/catalog/nrcs/README.md
  - docs/sources/catalog/kansas/README.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/truth-posture.md
  - docs/domains/habitat/README.md
  - docs/domains/flora/README.md
  - docs/domains/fauna/README.md
  - docs/domains/hazards/README.md
  - docs/standards/SENSITIVITY_RUBRIC.md
  - docs/registers/AUTHORITY_LADDER.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/adr/ADR-0001-schema-home.md
  - schemas/contracts/v1/source/source_descriptor.schema.json
  - connectors/landfire/
  - data/registry/sources/
  - policy/sensitivity/
  - policy/rights/
tags: [kfm, sources, catalog, landfire, land-cover, vegetation, fuels, fire, usnvc, evt, ldist, gap, cdl, nlcd, kfm-p2-idea-0028, kfm-p18-prog-0032, kfm-p25-idea-0010, kfm-p25-prog-0010, kfm-p25-prog-0024, kfm-p25-prog-0025, ml-k-067]
notes:
  - >-
    v0.2 promotes the v0.1 thin scaffold (single product reference, generic
    section stubs) into a full family-README brief with corpus-grounded
    LANDFIRE doctrine, parallel to ISRIC v0.2 family README in this
    conversation series. Both LANDFIRE and ISRIC are "beyond §7.3" families
    that scaffold under the same OPEN-DSC-14 ADR-ratification umbrella.
  - >-
    Connector path correction in v0.2 — OPEN-LF-01. v0.1 referenced
    `connectors/lf/` (two-letter top-level abbreviation, not a canonical
    family lane). v0.2 corrects to `connectors/landfire/` (full kebab-case
    family name at top level). Both are "beyond §7.3" until ADR-ratified per
    OPEN-DSC-14; this is the same posture as ISRIC v0.2 OPEN-DSC-14 cluster.
  - >-
    §7.3 canonical families (CONFIRMED at commit
    `b6a27916bbb9e07cbf3752870c867476e1e094e7` per Directory Rules v1.2):
    nine families — `usgs/`, `fema/`, `noaa/`, `nrcs/`, `kansas/`, `gbif/`,
    `inaturalist/`, `census/`, `local_upload/`. **LANDFIRE is NOT in §7.3.**
    OPEN-DSC-14 tracks whether `landfire/` (and parallel `isric/`) should be
    ADR-ratified as a tenth family or migrated under an existing family
    (most plausibly `usgs/` since LANDFIRE is jointly produced by USGS and
    USFS, with USGS as the primary host).
  - >-
    Atlas card lineage CONFIRMED: `KFM-P2-IDEA-0028` (CONFIRMED, Pass 32 —
    "Land cover authorities ingested by KFM include USDA Cropland Data Layer
    (CDL), NLCD (National Land Cover Database), **LANDFIRE (fire-related
    land cover)**, and GAP (Gap Analysis Program). Each is ingested with
    native classification preserved and cross-walked to a common vocabulary
    where possible." Cadence detail: "CDL is annual and crop-focused; NLCD
    is multi-year and broad; **LANDFIRE is fire-focused**; GAP is
    biodiversity-focused." Tension: "Classification crosswalks are
    inherently lossy; the corpus directs that crosswalks be advisory rather
    than authoritative.");  `KFM-P18-PROG-0032` (active, Pass 32 — "The
    LANDFIRE 2025 Limited Disturbance product family should be represented
    as a source descriptor with early-release status, cadence, rights, and
    change-detection role."); `KFM-P25-PROG-0010` (active, Pass 32 —
    "A GAP/LANDFIRE descriptor should record ecological system or USNVC
    classification, product version, raster/vector form, source URI, and
    thematic role."); `KFM-P25-IDEA-0010` (active, Pass 32 — "LANDFIRE EVT
    and USNVC hierarchy can support county facies summaries, confidence
    metrics, and signed COG/MVT derivatives for map delivery.");
    `KFM-P25-FEAT-0005` (active, Pass 32 — "A map layer should render
    LANDFIRE/USNVC per-county facies summaries and confidence metrics from
    signed derivatives."); `KFM-P25-PROG-0024` (active, Pass 32 — "A
    LANDFIRE EVT pipeline should compute per-county area by nvc_code with
    confidence metrics and signed derivative references.");
    `KFM-P25-PROG-0025` (active, Pass 32 — "An USNVC metadata crosswalk
    should preserve ecological system, USNVC group, ruderal/natural status,
    class labels, and source version."); `ML-K-067` (Master MapLibre —
    "LANDFIRE EVT rasters can be converted to COGs with signed derivative
    provenance"); `KFM-P20-IDEA-0002` (active, Pass 32 — mask-aware HLS
    vegetation analytics, parallel evidence pattern); `KFM-P24-PROG-0051`
    (active, Pass 32 — Soils PMTiles/COG artifact contract, parallel
    distribution pattern); `KFM-P13-PROG-0018` (active, Pass 32, EXPANDED
    — deterministic grid generalization with rule-version provenance,
    applied weakly to LANDFIRE which is public-distributed); `C4-01` STAC
    `kfm:provenance`; `C4-02` STAC Collection `kfm-<org>-<product>`;
    `C4-05` DCAT; `C5-02` default-deny promotion; `C5-04` spec-hash-match;
    `C5-08` lineage required; `C3-01` smart-sync HTTP validators.
[/KFM_META_BLOCK_V2] -->

# `landfire` source family — Catalog README

> Source-oriented catalog README for the **LANDFIRE** source family — the interagency (USGS + USFS) program that produces national vegetation, fuels, and disturbance products. CONFIRMED member of the KFM land-cover authority cluster per `KFM-P2-IDEA-0028`: *"Land cover authorities ingested by KFM include USDA Cropland Data Layer (CDL), NLCD (National Land Cover Database), **LANDFIRE (fire-related land cover)**, and GAP (Gap Analysis Program). Each is ingested with native classification preserved and cross-walked to a common vocabulary where possible."*

[![Status: draft](https://img.shields.io/badge/status-draft-yellow)](#)
[![doc-version](https://img.shields.io/badge/doc--version-v0.2-blue)](#)
[![family-status](https://img.shields.io/badge/family-beyond%20%C2%A77.3%20(OPEN--DSC--14)-orange)](#)
[![land-cover-cluster](https://img.shields.io/badge/land--cover-CDL%20%E2%9C%99%20NLCD%20%E2%9C%99%20LANDFIRE%20%E2%9C%99%20GAP-success)](#)
[![focus](https://img.shields.io/badge/focus-fire--related%20land%20cover-c62828)](#)
[![interagency](https://img.shields.io/badge/interagency-USGS%20%2B%20USFS-1565c0)](#)
[![USNVC](https://img.shields.io/badge/classification-USNVC%20hierarchy-7e57c2)](#)
[![distribution](https://img.shields.io/badge/distribution-COG%20%2B%20PMTiles%2FMVT-informational)](#)
[![rights](https://img.shields.io/badge/rights-US--Federal%20public%20domain%20(NEEDS%20VERIFICATION)-orange)](#)
[![last-updated](https://img.shields.io/badge/last--updated-2026--05--21-informational)](#)

**Status:** `draft` (v0.2) &nbsp;·&nbsp; **§7.3 status:** PROPOSED beyond canonical nine — see `OPEN-DSC-14` &nbsp;·&nbsp; **Owners:** `<TODO — docs steward + source steward + hazards/habitat/flora/fauna domain stewards>` &nbsp;·&nbsp; **Last reviewed:** 2026-05-21

---

## Quick jump

- [1. Scope](#1-scope) · [2. Status & doctrinal basis](#2-status--doctrinal-basis) · [3. Repo fit](#3-repo-fit)
- [4. Product pages](#4-product-pages) · [5. Domain reach](#5-domain-reach) · [6. Catalog profiles](#6-catalog-profiles)
- [7. Identity & namespaces](#7-identity--namespaces) · [8. Rights & sensitivity](#8-rights--sensitivity)
- [9. Distribution shape](#9-distribution-shape) · [10. Validation](#10-validation)
- [11. Pipeline diagram](#11-pipeline-diagram) · [12. Related contracts & schemas](#12-related-contracts--schemas)
- [13. Related connectors & pipelines](#13-related-connectors--pipelines) · [14. Open questions](#14-open-questions)
- [15. Related docs](#15-related-docs)
- [Appendix A — Atlas idea-card lineage](#appendix-a--atlas-idea-card-lineage) · [Appendix B — Change log](#appendix-b--change-log)

---

## 1. Scope

> [!NOTE]
> **v0.1 → v0.2 promotion.** v0.1 was a thin family-README scaffold (single product row, generic section stubs, `connectors/lf/` two-letter abbreviation). v0.2 promotes it into a full family-README brief parallel to the ISRIC v0.2 family README in this conversation series. Both LANDFIRE and ISRIC are "beyond §7.3" families that scaffold under the same OPEN-DSC-14 ADR-ratification umbrella.

> [!IMPORTANT]
> **Beyond §7.3 — OPEN-DSC-14.** Per Directory Rules v1.2 §7.3 (CONFIRMED at commit `b6a27916bbb9e07cbf3752870c867476e1e094e7`), the nine canonical connector families are: **`usgs/`, `fema/`, `noaa/`, `nrcs/`, `kansas/`, `gbif/`, `inaturalist/`, `census/`, `local_upload/`**. **`landfire/` is NOT among them.** This family folder was scaffolded because corpus doctrine (`KFM-P2-IDEA-0028` CONFIRMED) names LANDFIRE explicitly as a first-class land-cover authority — a strong doctrinal claim that the corpus expects to be ingested distinctly with native classification preserved. The family awaits ADR ratification under `OPEN-DSC-14` (shared with ISRIC, GAP, and other beyond-§7.3 families). The ADR will resolve: (a) promote `landfire/` as a tenth canonical family, OR (b) nest LANDFIRE under `connectors/usgs/landfire/` since LANDFIRE is co-produced by USGS and hosted on USGS infrastructure, OR (c) some other arrangement.

> [!IMPORTANT]
> **Connector path correction in v0.2 — OPEN-LF-01.** v0.1 referenced `connectors/lf/` (two-letter top-level abbreviation, neither a §7.3 family nor full kebab-case). v0.2 corrects to `connectors/landfire/` (full kebab-case family name at top level). Both placements are "beyond §7.3" until ADR-ratified per OPEN-DSC-14; the v0.2 correction picks the placement consistent with full-name kebab-case convention used elsewhere in the catalog (e.g., `isric/`).

**LANDFIRE** (Landscape Fire and Resource Management Planning Tools) is a CONFIRMED member of the four-source KFM land-cover authority cluster, alongside USDA CDL, NLCD, and GAP. Per `KFM-P2-IDEA-0028` (CONFIRMED, Pass 32), each is "ingested with native classification preserved and cross-walked to a common vocabulary where possible," and "LANDFIRE is fire-focused" — distinguishing it from the crop-focused (CDL), broad multi-year (NLCD), and biodiversity-focused (GAP) cluster members.

This family-README orients readers to the LANDFIRE source family in the KFM catalog: what role LANDFIRE plays, what products are ingested, which domains receive them, what governance contracts apply, and which open questions remain.

**What this dossier is not.** It is not a `SourceDescriptor` instance, a connector, a policy bundle, a STAC catalog row, or a release manifest. Each of those has its own canonical home (see §3 and §12).

[Back to top](#landfire-source-family--catalog-readme)

---

## 2. Status & doctrinal basis

| Claim | Label | Basis |
|---|---|---|
| LANDFIRE is a CONFIRMED KFM land-cover authority. | **CONFIRMED doctrine** | `KFM-P2-IDEA-0028` (CONFIRMED, Pass 32) names LANDFIRE explicitly. |
| LANDFIRE is the fire-focused member of the four-source land-cover cluster. | **CONFIRMED doctrine** | `KFM-P2-IDEA-0028` — "LANDFIRE is fire-focused." |
| Native classification must be preserved; crosswalks are advisory not authoritative. | **CONFIRMED doctrine** | `KFM-P2-IDEA-0028` tension: "Classification crosswalks are inherently lossy; the corpus directs that crosswalks be advisory rather than authoritative." |
| LANDFIRE EVT + USNVC hierarchy supports county facies summaries. | **CONFIRMED active card** | `KFM-P25-IDEA-0010` (active, Pass 32) + `KFM-P25-PROG-0024` (active, Pass 32 — per-county nvc_code area + confidence metrics + signed derivative references). |
| USNVC metadata crosswalk preserves ecological system, USNVC group, ruderal/natural status, class labels, source version. | **CONFIRMED active card** | `KFM-P25-PROG-0025` (active, Pass 32). |
| GAP/LANDFIRE descriptor records ecological system / USNVC classification, product version, raster/vector form, source URI, thematic role. | **CONFIRMED active card** | `KFM-P25-PROG-0010` (active, Pass 32). |
| LANDFIRE 2025 Limited Disturbance (LDist) product family treated with early-release status, cadence, rights, change-detection role. | **CONFIRMED active card** | `KFM-P18-PROG-0032` (active, Pass 32). |
| LANDFIRE EVT rasters can be converted to COGs with signed derivative provenance. | **CONFIRMED active card** | `ML-K-067` (Master MapLibre Components). |
| LANDFIRE/USNVC per-county facies summaries render on map layer from signed derivatives. | **CONFIRMED active card** | `KFM-P25-FEAT-0005` (active, Pass 32) — vegetation facies county map feature. |
| `connectors/landfire/` family lane status. | **PROPOSED beyond §7.3** | Directory Rules v1.2 §7.3 nine-family list does NOT include LANDFIRE; OPEN-DSC-14 ADR pending. |
| `connectors/lf/` (v0.1 path) corrected to `connectors/landfire/` (v0.2). | **PROPOSED** | OPEN-LF-01 path correction. |
| Specific LANDFIRE product endpoints, version cadence, current LDist release status. | **NEEDS VERIFICATION** | Not pinned by corpus; must be captured in per-product descriptors. |

[Back to top](#landfire-source-family--catalog-readme)

---

## 3. Repo fit

> [!NOTE]
> Per Directory Rules v1.2 §6.1, `docs/sources/` is the doctrinal home for source-descriptor standards and source families. v0.2 adopts `docs/sources/catalog/<family>/` as the catalog convention. **`connectors/landfire/` is PROPOSED beyond §7.3** per OPEN-DSC-14 (parallel to ISRIC v0.2 family README).

| Concern | Canonical home (v0.2 path) | What lives there |
|---|---|---|
| Family README (this file) | `docs/sources/catalog/landfire/README.md` | This document. |
| Per-product page(s) | `docs/sources/catalog/landfire/<product>.md` | Per-LANDFIRE-product brief — see §4. |
| Source-descriptor standard | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` (PROPOSED — referenced in plans, NEEDS VERIFICATION in repo) | Field-by-field doctrine for `SourceDescriptor`. |
| Machine-readable descriptor record | `data/registry/sources/landfire/<product>/source_descriptor.yaml` (PROPOSED) | Per-product `SourceDescriptor` per `KFM-P25-PROG-0010` field set. |
| Schema (shape) | `schemas/contracts/v1/source/source_descriptor.schema.json` (default per ADR-0001) | JSON Schema for `SourceDescriptor`. |
| Object-family meaning | `contracts/source/` (semantic Markdown) | What a `SourceDescriptor` means and invariants it carries. |
| Admit / restrict / deny policy | `policy/<domain>/` and `policy/sensitivity/` | OPA / policy bundle entries. |
| Connector (fetch + admission) | `connectors/landfire/` — **PROPOSED beyond §7.3** per OPEN-DSC-14. **v0.1 used `connectors/lf/` (incorrect abbreviation); see OPEN-LF-01.** | Source-specific fetcher; output → `data/raw/<domain>/landfire/<product>/<run_id>/`. |
| Pipelines (executable) | `pipelines/ingest/`, `pipelines/normalize/`, `pipelines/validate/`, `pipelines/catalog/`, `pipelines/publish/` with `pipeline_specs/<domain>/` declarative companion | Vegetation-facies pipeline per `KFM-P25-PROG-0024`; USNVC crosswalk per `KFM-P25-PROG-0025`. |
| Domain receiving lanes | `docs/domains/habitat/`, `docs/domains/flora/`, `docs/domains/fauna/`, `docs/domains/hazards/` | Where LANDFIRE-derived facies/vegetation/fire-context objects are owned. |
| Distribution artifacts | COGs (continuous raster surfaces) + PMTiles/MVT (vector derivatives) per `ML-K-067` + `KFM-P25-IDEA-0010` + `KFM-P24-PROG-0051`-parallel | Map-surface delivery shape. |

[Back to top](#landfire-source-family--catalog-readme)

---

## 4. Product pages

The LANDFIRE program publishes multiple product families. Per `KFM-P2-IDEA-0028`, each LANDFIRE product is admitted with native classification preserved; per `KFM-P25-PROG-0010`, each gets its own `SourceDescriptor` recording ecological system / USNVC classification, product version, raster/vector form, source URI, and thematic role.

| Product page | LANDFIRE product family | Atlas card(s) | Status |
|---|---|---|---|
| [`landfire.md`](./landfire.md) | LANDFIRE Vegetation and Fuels (umbrella per-product page — v0.1 PROPOSED) | `KFM-P2-IDEA-0028`, `KFM-P25-PROG-0010` | PROPOSED |
| `evt.md` (PROPOSED) | LANDFIRE Existing Vegetation Type (EVT) — central card for KFM | `KFM-P25-IDEA-0010`, `KFM-P25-FEAT-0005`, `KFM-P25-PROG-0024`, `KFM-P25-PROG-0025`, `ML-K-067` | PROPOSED |
| `ldist.md` (PROPOSED) | LANDFIRE 2025 Limited Disturbance (LDist) product family | `KFM-P18-PROG-0032` | PROPOSED |
| `fuels.md` (PROPOSED) | LANDFIRE wildland fuels products (FBFM13, FBFM40, FVH, FVC, FVT, etc.) | (implied by `KFM-P2-IDEA-0028` "fire-related land cover" + USFS partner role) | PROPOSED |
| `disturbance.md` (PROPOSED) | LANDFIRE historical disturbance products (other than LDist 2025) | (implied by `KFM-P18-PROG-0032` "change-detection role") | PROPOSED |

> [!TIP]
> **EVT is the operationally most-cited LANDFIRE product in the KFM corpus.** Four atlas cards reference EVT directly: `KFM-P25-IDEA-0010` (facies mapping), `KFM-P25-FEAT-0005` (county map feature), `KFM-P25-PROG-0024` (per-county nvc_code pipeline), `KFM-P25-PROG-0025` (USNVC crosswalk metadata). Plus `ML-K-067` (raster → COG with signed derivative provenance). When drafting the per-product `evt.md`, lift these five cards as the doctrinal spine.

> [!NOTE]
> **LDist 2025 has special status** per `KFM-P18-PROG-0032`: "early-release status." This is operationally meaningful — the descriptor must carry the early-release flag, and the connector cadence must account for product instability during the early-release window. See `KFM-P18-PROG-0032` + OPEN-LF-04.

[Back to top](#landfire-source-family--catalog-readme)

---

## 5. Domain reach

LANDFIRE products land in multiple KFM domains per their thematic role. Per `KFM-P25-PROG-0010`, each descriptor records `thematic_role` explicitly.

| Domain | LANDFIRE product types | Role | Atlas card(s) |
|---|---|---|---|
| **Habitat** | EVT, BPS (Biophysical Settings), EVC (Existing Vegetation Cover), EVH (Existing Vegetation Height) | Vegetation community classification; ecosystem mapping | `KFM-P25-IDEA-0010`, `KFM-P25-FEAT-0005` |
| **Flora** | EVT, USNVC-classified vegetation polygons | Vegetation taxonomy via USNVC hierarchy | `KFM-P25-PROG-0025` |
| **Fauna** | EVT, BPS as habitat substrate | Habitat context for fauna distributions | (via DOM-FAUNA habitat-context relations) |
| **Hazards (fire)** | Fuels products (FBFM13, FBFM40, FVT, FCC), LDist disturbance products | Fuel models + disturbance history for fire-context analytics | `KFM-P18-PROG-0032`, `KFM-P20-IDEA-0002`-parallel |
| **Geology / surficial** | (indirect, via habitat-substrate cross-cutting) | n/a | n/a |
| **Agriculture** | EVT cross-walked against CDL (advisory crosswalk per `KFM-P2-IDEA-0028`) | Land-cover boundary context | `KFM-P2-IDEA-0028` |

> [!CAUTION]
> **Crosswalks are advisory, not authoritative** per `KFM-P2-IDEA-0028` tension paragraph: *"Classification crosswalks are inherently lossy; the corpus directs that crosswalks be advisory rather than authoritative."* When LANDFIRE EVT and USDA CDL describe the same parcel with different classifications, **both are preserved in their native classification**, and the crosswalk is recorded with explicit "advisory" status. KFM does not silently resolve LANDFIRE-vs-CDL disagreements; the disagreement IS the data.

[Back to top](#landfire-source-family--catalog-readme)

---

## 6. Catalog profiles

PROPOSED — see [`PROFILES.md`](../PROFILES.md). Per-product confirmation required. The doctrinal expectations:

| Profile | Lane | LANDFIRE applicability |
|---|---|---|
| **STAC** | `data/catalog/stac/` | **YES** — per `KFM-P25-PROG-0010` (descriptor fields: source URI, product version, raster/vector form) + `C4-01` STAC `kfm:provenance` namespace. LANDFIRE raster products (EVT, BPS, fuels) admit naturally as STAC Item per Collection. Collection-id pattern `kfm-landfire-<product>` per `C4-02`. |
| **DCAT** | `data/catalog/dcat/` | **YES** — per `C4-05` DCAT distribution; LANDFIRE distributes through public-domain US-federal endpoints which admit naturally as DCAT distributions. |
| **PROV-O** | `data/catalog/prov/` | **YES** — per `C5-08` lineage required + Atlas §24.2.1 receipt catalog; LANDFIRE-derived facies summaries (per `KFM-P25-PROG-0024`) carry full PROV-O lineage to source rasters. |
| **Domain projection** | `data/catalog/domain/habitat/`, `data/catalog/domain/flora/`, etc. | **YES** — per `KFM-P25-FEAT-0005` (vegetation facies county map) + `KFM-P25-IDEA-0010` (county facies summaries). |

[Back to top](#landfire-source-family--catalog-readme)

---

## 7. Identity & namespaces

Collection-id and namespace conventions follow [`IDENTITY.md`](../IDENTITY.md).

- **Collection-id pattern (PROPOSED per `C4-02`):** `kfm-landfire-<product>` — e.g., `kfm-landfire-evt`, `kfm-landfire-ldist-2025`, `kfm-landfire-fbfm40`.
- **Source-id pattern (PROPOSED):** `landfire-<product>` — kebab-case, parallel to `ku-nhm-mammalogy`, `kanu`, etc.
- **`source_family` field value:** `landfire` (top-level family — pending OPEN-DSC-14 ADR ratification).
- **`source_family_enum`:** `other` per `KFM-P3-PROG-0001` closed enum.
- **USNVC integration:** per `KFM-P25-PROG-0025`, the USNVC `nvc_code` is a first-class identifier preserved alongside the LANDFIRE-native code; crosswalks record ecological system, USNVC group, ruderal/natural status, class labels, and source version.
- **The namespace pin** (`kfm:` vs. `ks-kfm:`) is unresolved — see `OPEN-DSC-03` in [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md).

[Back to top](#landfire-source-family--catalog-readme)

---

## 8. Rights & sensitivity

| Posture dimension | Value | Status | Notes |
|---|---|---|---|
| Rights / terms | US Federal public domain (LANDFIRE is jointly produced by USGS and USFS — both federal agencies; products published without copyright restriction) | **PROPOSED** — NEEDS VERIFICATION per product | LDist 2025 early-release status may carry use caveats (early-release ≠ public-domain-restricted; verify per `KFM-P18-PROG-0032`). |
| Attribution requirement | LANDFIRE program citation | **PROPOSED — NEEDS VERIFICATION** | Confirm per product. |
| Redistribution | Generally unrestricted; verify per product | **PROPOSED** | |
| Sensitivity floor | **rank 0 (public / open)** for most LANDFIRE products | **PROPOSED** | LANDFIRE is publicly distributed at full spatial resolution; the `KFM-P13-PROG-0018` grid-generalization machinery (deterministic generalization with rule-version provenance) applies only weakly to LANDFIRE because the public release already establishes the floor. |
| CARE applicability | Not generally applicable (LANDFIRE describes broad-scale vegetation/fuels, not culturally sensitive specific places) | **PROPOSED** | Special-case review only if LANDFIRE-derived facies intersect with culturally sensitive cross-domain joins (e.g., archaeology). |
| Early-release product caution | LDist 2025 carries "early-release status" per `KFM-P18-PROG-0032` | **CONFIRMED card** | Descriptor must flag early-release; cadence/policy must accommodate product instability. |

> [!NOTE]
> NEEDS VERIFICATION per product — see [`RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) and [`policy/sensitivity/`](../../../../policy/sensitivity/). Never restate policy here.

[Back to top](#landfire-source-family--catalog-readme)

---

## 9. Distribution shape

LANDFIRE products distribute through KFM as governed derivatives per the corpus-defined shape.

| Stage | Form | Atlas card |
|---|---|---|
| **Source** | LANDFIRE-native rasters (typically GeoTIFF) at LANDFIRE-published resolution | upstream |
| **RAW** | Original bytes preserved with `spec_hash`, ETag, Last-Modified | `C3-01` smart-sync HTTP validators |
| **PROCESSED (continuous rasters)** | Converted to **Cloud-Optimized GeoTIFF (COG)** with signed derivative provenance | `ML-K-067` (CONFIRMED active) + `KFM-P24-PROG-0051`-parallel |
| **PROCESSED (vector derivatives)** | Per-county facies summaries computed by EVT pipeline; signed COG/MVT derivatives | `KFM-P25-PROG-0024`, `KFM-P25-IDEA-0010` |
| **CATALOG** | STAC Items per Collection `kfm-landfire-<product>` with `kfm:provenance` block | `C4-01`, `C4-02` |
| **PUBLISHED (map)** | PMTiles for vector facies; COG for continuous rasters; rendered via vegetation facies county map | `KFM-P25-FEAT-0005`, `ML-K-067` |

> [!TIP]
> **COG + PMTiles distribution pattern** for LANDFIRE follows the parallel pattern established for Soils in `KFM-P24-PROG-0051` ("Soil mapunit polygons should publish as PMTiles and continuous soil properties as COGs, with provenance metadata, spec_hash, and release references"). The LANDFIRE EVT-derived per-county facies polygons → PMTiles; the underlying EVT raster → COG. Both carry `spec_hash` and signed derivative references per `ML-K-067`.

[Back to top](#landfire-source-family--catalog-readme)

---

## 10. Validation

- Markdown lint (NEEDS VERIFICATION — workflow not yet wired).
- Link integrity against repo-relative targets.
- Per-product page conformance to [`_template/SOURCE_PRODUCT_TEMPLATE.md`](../_template/SOURCE_PRODUCT_TEMPLATE.md).
- USNVC `nvc_code` crosswalk validation per `KFM-P25-PROG-0025` — ecological system + USNVC group + ruderal/natural status + class labels + source version must all be present per record.
- LANDFIRE EVT pipeline validation per `KFM-P25-PROG-0024` — per-county area by `nvc_code` + confidence metrics + signed derivative references.
- Native classification preservation validation per `KFM-P2-IDEA-0028` — original LANDFIRE classification must not be lossily collapsed into the common-vocabulary crosswalk.
- Catalog closure (STAC + DCAT + PROV) before promotion per `C5-04` spec-hash-match + `C5-08` lineage required.

[Back to top](#landfire-source-family--catalog-readme)

---

## 11. Pipeline diagram

```mermaid
flowchart LR
  subgraph LF["LANDFIRE universe (external)"]
    EVT[LANDFIRE EVT<br/>Existing Vegetation Type]
    BPS[LANDFIRE BPS<br/>Biophysical Settings]
    LDIST[LANDFIRE LDist 2025<br/>Limited Disturbance<br/>early-release status]
    FUEL[LANDFIRE Fuels<br/>FBFM13/40, FVT, FVH, FVC]
    EVC_EVH[LANDFIRE EVC / EVH<br/>cover / height]
  end

  subgraph CLUSTER["KFM land-cover cluster<br/>KFM-P2-IDEA-0028"]
    CDL[USDA CDL<br/>crop-focused annual]
    NLCD[USGS NLCD<br/>broad multi-year]
    LFM[LANDFIRE<br/>fire-focused]
    GAP[USGS GAP<br/>biodiversity-focused]
  end

  subgraph KFM["KFM governance lanes"]
    CONN[Connector<br/>connectors/landfire/<br/>PROPOSED beyond §7.3<br/>OPEN-DSC-14]
    DESC[SourceDescriptor<br/>data/registry/sources/landfire/&lt;product&gt;/<br/>per KFM-P25-PROG-0010]
    USNVC_X[USNVC crosswalk<br/>KFM-P25-PROG-0025]
    RAW[(data/raw/&lt;domain&gt;/landfire/&lt;product&gt;/&lt;timestamp&gt;/)]
    WORK[(data/work/&lt;domain&gt;/&lt;run_id&gt;/)]
    PROC[(data/processed/&lt;domain&gt;/&lt;spec_hash&gt;/<br/>COG + PMTiles per ML-K-067 + KFM-P24-PROG-0051 parallel)]
    CAT[(data/catalog/<br/>stac | dcat | prov / &lt;domain&gt;/)]
    PUB[(data/published/<br/>vegetation facies county map<br/>KFM-P25-FEAT-0005)]
    EVT_PIPE[EVT county summary pipeline<br/>per-county area by nvc_code<br/>+ confidence metrics<br/>+ signed derivatives<br/>KFM-P25-PROG-0024]
  end

  EVT --> LFM
  BPS --> LFM
  LDIST --> LFM
  FUEL --> LFM
  EVC_EVH --> LFM

  LFM --> CONN
  CDL -. advisory crosswalk only<br/>KFM-P2-IDEA-0028 .-> CONN
  NLCD -. advisory crosswalk only .-> CONN
  GAP -. advisory crosswalk only .-> CONN

  CONN --> RAW
  CONN --> DESC
  DESC --> USNVC_X
  USNVC_X --> WORK
  RAW --> WORK
  WORK --> EVT_PIPE
  EVT_PIPE --> PROC
  PROC --> CAT
  CAT --> PUB

  classDef confirmed fill:#d5e8d4,stroke:#82b366;
  classDef proposed stroke-dasharray: 4 3;
  classDef beyond fill:#fff4e0,stroke:#d4882b;
  class LFM,EVT,BPS,FUEL,EVC_EVH confirmed;
  class LDIST beyond;
  class CONN,DESC,USNVC_X,EVT_PIPE,RAW,WORK,PROC,CAT,PUB proposed;
```

> [!NOTE]
> Native classification is preserved at every stage (per `KFM-P2-IDEA-0028`); advisory-only crosswalks across cluster members (CDL ↔ NLCD ↔ LANDFIRE ↔ GAP) attach as advisory edges, not authoritative joins. The `EVT county summary pipeline` per `KFM-P25-PROG-0024` is the operationally most-developed LANDFIRE pipeline in the corpus.

[Back to top](#landfire-source-family--catalog-readme)

---

## 12. Related contracts & schemas

- [`schemas/contracts/v1/source/`](../../../../schemas/contracts/v1/source/) — machine shape (per ADR-0001).
- [`contracts/`](../../../../contracts/) — object families: FloraTaxon Crosswalk, Vegetation Community, Habitat Association (Flora object families per DOM-FLORA §E); Fuel Model Surface, Disturbance Polygon (Hazards object families).
- USNVC nvc_code metadata crosswalk schema — per `KFM-P25-PROG-0025` (PROPOSED).
- LANDFIRE EVT county summary record schema — per `KFM-P25-PROG-0024` (PROPOSED).
- GAP/LANDFIRE source-descriptor schema — per `KFM-P25-PROG-0010` (PROPOSED).

[Back to top](#landfire-source-family--catalog-readme)

---

## 13. Related connectors & pipelines

- **Connector lane:** `connectors/landfire/` — **PROPOSED beyond §7.3** per OPEN-DSC-14. **v0.1's `connectors/lf/` corrected to `connectors/landfire/` in v0.2** per OPEN-LF-01. Currently empty stub pending OPEN-DSC-14 ADR resolution.
- **Pipelines:** [`pipelines/ingest/`](../../../../pipelines/ingest/), [`pipelines/normalize/`](../../../../pipelines/normalize/), [`pipelines/validate/`](../../../../pipelines/validate/), [`pipelines/catalog/`](../../../../pipelines/catalog/), [`pipelines/publish/`](../../../../pipelines/publish/).
- **Pipeline specs:** `pipeline_specs/habitat/landfire-evt-county-summary.yaml` (PROPOSED) per `KFM-P25-PROG-0024`.
- **Tools:** USNVC crosswalk validator (`tools/validators/usnvc_crosswalk_validator/` PROPOSED) per `KFM-P25-PROG-0025`.

[Back to top](#landfire-source-family--catalog-readme)

---

## 14. Open questions

| # | Item | Owner (PROPOSED) | Why it matters |
|---|---|---|---|
| **OPEN-LF-01** (PATH) | Connector path corrected from v0.1's `connectors/lf/` (two-letter abbreviation) to v0.2's `connectors/landfire/` (full kebab-case). Both placements are "beyond §7.3" until ADR-ratified. | Pipeline owner | Connector-lane naming consistency. |
| **OPEN-LF-02** (= OPEN-DSC-14) | Should `landfire/` be ADR-ratified as a tenth §7.3 canonical family, OR nested under `connectors/usgs/landfire/` since USGS is the primary host agency, OR some other arrangement? Shared question with ISRIC, GAP, and other beyond-§7.3 families. | Docs steward + ADR sponsor | Family-lane status resolution. |
| **OPEN-LF-03** | Confirm full LANDFIRE product list to ingest. Corpus names: EVT (most-cited), BPS, EVC, EVH (implied), LDist 2025, fuels (FBFM13, FBFM40, FVT, FVH, FVC implied). Confirm which carry their own per-product pages vs. share the umbrella `landfire.md`. | Source steward | Per-product page scope. |
| **OPEN-LF-04** | Confirm LDist 2025 early-release cadence and policy posture per `KFM-P18-PROG-0032`. What is the cadence for re-pulling during the early-release window? What is the deprecation policy when LDist 2025 graduates to a stable release? | Source steward | Cadence determinism. |
| **OPEN-LF-05** | Confirm LANDFIRE-vs-CDL-vs-NLCD-vs-GAP advisory-crosswalk operational mechanism per `KFM-P2-IDEA-0028`. When two cluster members disagree on classification for a parcel, the disagreement is preserved — but at what record granularity (pixel? polygon? county summary?), and how is the disagreement surfaced in Evidence Drawer? | Flora/Habitat domain steward + AI steward | Crosswalk discipline. |
| **OPEN-LF-06** | Confirm USNVC `nvc_code` crosswalk completeness per `KFM-P25-PROG-0025`. Does every LANDFIRE EVT class have a USNVC `nvc_code` mapping, or are there gaps? If gaps, what is the policy when EVT records lack USNVC anchoring? | Flora/Habitat domain steward | USNVC anchoring discipline. |
| **OPEN-LF-07** | Confirm vegetation facies county map render pattern per `KFM-P25-FEAT-0005` + `KFM-P25-IDEA-0010`. Is the render PMTiles-only, COG-only, or hybrid? | MapLibre steward | Distribution architecture. |
| **OPEN-LF-08** | Confirm rights & license posture per LANDFIRE product. US Federal public domain assumed but NEEDS VERIFICATION at per-product granularity. | Source steward | Rights gate. |
| **OPEN-LF-09** | Confirm sibling families `landfire/`, `isric/`, and any other beyond-§7.3 families are tracked under a single ADR (OPEN-DSC-14) or separate ADRs per family. | Docs steward | ADR-counting discipline. |
| **OPEN-LF-10** | Confirm `KFM-P25-PROG-0010` GAP-and-LANDFIRE shared descriptor framing — does GAP get its own family folder `gap/`, or does it nest under LANDFIRE (since the descriptor is shared per the card title "GAP LANDFIRE source descriptor")? | Docs steward + biodiversity domain steward | Family scope. |
| **OPEN-LF-11** | Confirm corpus card-ID stability for `KFM-P2-IDEA-0028`, `KFM-P18-PROG-0032`, `KFM-P25-IDEA-0010`, `KFM-P25-FEAT-0005`, `KFM-P25-PROG-0010`, `KFM-P25-PROG-0024`, `KFM-P25-PROG-0025`, `ML-K-067`. | Docs steward | Card stability. |
| **OPEN-DSC-03** | Namespace pin: `kfm:` vs `ks-kfm:` (shared lane-wide question; same as in sibling family READMEs). | Docs steward | Namespace identity. |
| **OPEN-DSC-14** | Catalog-side question: does the `docs/sources/catalog/landfire/` folder structure stay as-is, migrate under `kansas/` (NO — LANDFIRE is national), under `usgs/` (USGS is primary host), or persist as its own beyond-§7.3 family? Shared with ISRIC and GAP. | Docs steward + ADR sponsor | ADR-ratification trigger. |

[Back to top](#landfire-source-family--catalog-readme)

---

## 15. Related docs

> [!NOTE]
> Targets below reflect the v0.2 catalog reorganization (`docs/sources/catalog/<family>/<product>.md`, kebab-case slugs). Per-product pages PROPOSED until verified in the mounted repo. Adjust paths via a `DRIFT_REGISTER` entry rather than silently divergent siblings.

- [`./landfire.md`](./landfire.md) — LANDFIRE Vegetation and Fuels umbrella product page (v0.1 PROPOSED; v0.2 promotion pending)
- `./evt.md` (PROPOSED) — LANDFIRE EVT per-product page
- `./ldist.md` (PROPOSED) — LANDFIRE LDist 2025 per-product page
- `./fuels.md` (PROPOSED) — LANDFIRE fuels per-product page
- [`../README.md`](../README.md) — `docs/sources/catalog/` index (TODO: create or verify)
- [`../isric/README.md`](../isric/README.md) — sibling beyond-§7.3 family README (parallel structural model, v0.2 in this conversation series)
- [`../usgs/README.md`](../usgs/README.md) — sibling §7.3 family README (USGS is LANDFIRE's primary host — potential nesting parent per OPEN-DSC-14)
- [`../nrcs/README.md`](../nrcs/README.md) — sibling §7.3 family README (parallel for soil land-cover context)
- [`../kansas/README.md`](../kansas/README.md) — sibling §7.3 family README (Kansas-specific land-cover authorities like KBS that complement LANDFIRE)
- [`../IDENTITY.md`](../IDENTITY.md) — Collection-id and namespace conventions
- [`../PROFILES.md`](../PROFILES.md) — catalog-profile selection guidance
- [`../RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) — lane-wide rights/sensitivity matrix
- [`../OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) — lane-wide `OPEN-DSC-*` items including OPEN-DSC-14
- [`../../SOURCE_DESCRIPTOR_STANDARD.md`](../../SOURCE_DESCRIPTOR_STANDARD.md) — source-descriptor field standard (PROPOSED — referenced in plans; NEEDS VERIFICATION in repo)
- [`../../../doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — placement law (§6.1, §7.3, §7.4, §9.1)
- [`../../../doctrine/lifecycle-law.md`](../../../doctrine/lifecycle-law.md) — RAW → PUBLISHED governance
- [`../../../doctrine/truth-posture.md`](../../../doctrine/truth-posture.md) — cite-or-abstain
- [`../../../domains/habitat/README.md`](../../../domains/habitat/README.md) — primary receiving domain
- [`../../../domains/flora/README.md`](../../../domains/flora/README.md) — secondary receiving domain
- [`../../../domains/fauna/README.md`](../../../domains/fauna/README.md) — tertiary receiving domain (habitat substrate)
- [`../../../domains/hazards/README.md`](../../../domains/hazards/README.md) — fire-context receiving domain
- [`../../../standards/SENSITIVITY_RUBRIC.md`](../../../standards/SENSITIVITY_RUBRIC.md) — `C6-01` 0–5 rubric (PROPOSED in corpus)
- [`../../../registers/AUTHORITY_LADDER.md`](../../../registers/AUTHORITY_LADDER.md) — authority order
- [`../../../registers/DRIFT_REGISTER.md`](../../../registers/DRIFT_REGISTER.md) — drift filing (including OPEN-DSC-14 ADR-ratification gap)
- [`../../../adr/ADR-0001-schema-home.md`](../../../adr/ADR-0001-schema-home.md) — schema-home convention
- Pass-10 Idea Index — **`C4-01`** STAC `kfm:provenance`; **`C4-02`** STAC Collection; **`C4-05`** DCAT distribution; **`C5-02`** default-deny promotion; **`C5-04`** spec-hash-match; **`C5-08`** lineage required; **`C3-01`** smart-sync HTTP validators
- Pass-23/32 Consolidated Atlas — **`KFM-P2-IDEA-0028`** USDA CDL + NLCD + LANDFIRE + GAP land cover (CONFIRMED, Pass 32); **`KFM-P18-PROG-0032`** LANDFIRE LDist source descriptor (active, Pass 32); **`KFM-P25-PROG-0010`** GAP/LANDFIRE source descriptor (active, Pass 32); **`KFM-P25-IDEA-0010`** LANDFIRE EVT facies mapping (active, Pass 32); **`KFM-P25-FEAT-0005`** vegetation facies county map (active, Pass 32); **`KFM-P25-PROG-0024`** LANDFIRE EVT county summary pipeline (active, Pass 32); **`KFM-P25-PROG-0025`** USNVC nvc_code metadata crosswalk (active, Pass 32); **`KFM-P20-IDEA-0002`** mask-aware HLS vegetation analytics (active, Pass 32, parallel pattern); **`KFM-P24-PROG-0051`** Soils PMTiles/COG artifact contract (active, Pass 32, parallel distribution model); **`KFM-P13-PROG-0018`** sensitive species grid generalization (active, Pass 32, applied weakly)
- Master MapLibre Components — **`ML-K-067`** LANDFIRE EVT raster → COG with signed derivative provenance

[Back to top](#landfire-source-family--catalog-readme)

---

## Appendix A — Atlas idea-card lineage

For traceability into the KFM Idea Index spine, this family README draws on the following atlas cards.

<details>
<summary>Click to expand — idea-card lineage</summary>

| Stable ID | Title | Status (atlas) | Relevance to this README |
|---|---|---|---|
| `KFM-P2-IDEA-0028` | USDA CDL, NLCD, LANDFIRE, GAP for land cover | **CONFIRMED, Pass 32** | **Central card for LANDFIRE.** Names LANDFIRE explicitly as one of four KFM land-cover authorities; "LANDFIRE is fire-focused"; native classification preserved; crosswalks advisory not authoritative. |
| `KFM-P18-PROG-0032` | LANDFIRE LDist source descriptor | active, Pass 32 | LDist 2025 product family with early-release status, cadence, rights, change-detection role. Per-product card. |
| `KFM-P25-PROG-0010` | GAP / LANDFIRE source descriptor | active, Pass 32 | Shared descriptor framing for GAP and LANDFIRE — records ecological system / USNVC classification, product version, raster/vector form, source URI, thematic role. Note: card title combines GAP and LANDFIRE (see OPEN-LF-10). |
| `KFM-P25-IDEA-0010` | LANDFIRE EVT facies mapping | active, Pass 32 | LANDFIRE EVT + USNVC hierarchy supports county facies summaries, confidence metrics, signed COG/MVT derivatives for map delivery. |
| `KFM-P25-FEAT-0005` | Vegetation facies county map | active, Pass 32 | Map layer feature that renders LANDFIRE/USNVC per-county facies summaries and confidence metrics from signed derivatives. |
| `KFM-P25-PROG-0024` | LANDFIRE EVT county summary pipeline | active, Pass 32 | Pipeline computes per-county area by `nvc_code` with confidence metrics and signed derivative references. **Operationally definitive LANDFIRE pipeline in corpus.** |
| `KFM-P25-PROG-0025` | USNVC `nvc_code` metadata crosswalk | active, Pass 32 | Crosswalk preserves ecological system, USNVC group, ruderal/natural status, class labels, source version. |
| `ML-K-067` | LANDFIRE EVT raster → COG | (Master MapLibre — EXPANDED) | LANDFIRE EVT rasters convert to COGs with signed derivative provenance. Distribution shape. |
| `KFM-P20-IDEA-0002` | Mask-aware HLS vegetation analytics | active, Pass 32 | **Parallel evidence pattern.** Bounded analytical claims with explicit cloud, aerosol, and fire-screening evidence — applies by parallel to LANDFIRE-derived vegetation analytics. |
| `KFM-P24-PROG-0051` | Soils PMTiles + COG artifact contract | active, Pass 32 | **Parallel distribution pattern.** Polygons → PMTiles, continuous properties → COGs, with provenance metadata, spec_hash, and release references. Applied to LANDFIRE per-county facies (PMTiles) + EVT raster (COG). |
| `KFM-P13-PROG-0018` | Sensitive species grid generalization policy | active, Pass 32, EXPANDED | **Applied weakly.** LANDFIRE is publicly distributed at full resolution; deterministic grid generalization doctrine applies only weakly here since the public release already establishes the floor. Contrast with KBS NHI / KDWP SINC for sensitive species occurrences. |
| `C4-01` | STAC `kfm:provenance` namespace | CONFIRMED (Pass-10) | Provenance block shape for LANDFIRE STAC Items. |
| `C4-02` | STAC Collection (`kfm-<org>-<product>`) | CONFIRMED (Pass-10) | Collection-id convention: `kfm-landfire-<product>`. |
| `C4-05` | DCAT distribution | CONFIRMED (Pass-10) | Applicable to LANDFIRE distributions. |
| `C5-02` | Default-deny promotion | CONFIRMED (Pass-10) | Anchors deny-by-default rights posture (mild for LANDFIRE since US-federal public-domain). |
| `C5-04` | Spec-hash-match gate | CONFIRMED (Pass-10) | Promotion gate. |
| `C5-08` | Lineage required | CONFIRMED (Pass-10) | OpenLineage trail back to receipts. |
| `C3-01` | Smart-sync HTTP validators | CONFIRMED (Pass-10) | ETag + Last-Modified watcher mechanism. |
| Atlas §24.2.1 | Master receipt catalog | CONFIRMED (Pass-23/32) | `SourceDescriptor`, `RawCaptureReceipt`, `TransformReceipt`, `ValidationReport`. |
| Atlas §24.8 | Time discipline | CONFIRMED (Pass-23/32) | source / observed / valid / retrieval / release / correction times preserved. |
| Directory Rules v1.2 §7.3 | Nine canonical connector families | CONFIRMED at commit `b6a27916...` | LANDFIRE not in nine — OPEN-DSC-14. |

</details>

[Back to top](#landfire-source-family--catalog-readme)

---

## Appendix B — Change log

| Date | Author | Change | Reviewed by |
|---|---|---|---|
| 2026-05-21 | `<docs-steward — TODO>` | Initial v0.1 family-README scaffold: title, overview, single product page row (`landfire.md`), source-authority pointer, generic catalog-profiles stub, identity-and-namespaces stub, rights-and-sensitivity stub, validation stub, related contracts/connectors/pipelines stubs with `connectors/lf/` reference, generic open-questions list, last-reviewed footer. Path: `docs/sources/catalog/landfire/README.md`. Connector path `connectors/lf/` — INCORRECT (two-letter abbreviation, not canonical kebab-case). | `<TODO — initial scaffold only>` |
| 2026-05-21 | `<docs-steward — TODO>` | **v0.2 revision (same-day promotion).** Promotes v0.1 thin scaffold to full family-README brief parallel to ISRIC v0.2 family README in this conversation series. **Structural reframings:** (a) **Connector path correction OPEN-LF-01** — v0.1's `connectors/lf/` (two-letter abbreviation) corrected to `connectors/landfire/` (full kebab-case). Same path-correction pattern as ISRIC v0.2 OPEN-DSC-14. (b) **§7.3 status clarification** — explicit acknowledgment that `landfire/` is NOT in §7.3 canonical nine families (CONFIRMED at commit `b6a27916...`: `usgs/`, `fema/`, `noaa/`, `nrcs/`, `kansas/`, `gbif/`, `inaturalist/`, `census/`, `local_upload/`). Surfaced as IMPORTANT callout in §1 and OPEN-LF-02 / OPEN-DSC-14. **Substantive doctrinal additions:** (c) explicit citation to **`KFM-P2-IDEA-0028`** (CONFIRMED Pass 32 — central card naming LANDFIRE as one of four KFM land-cover authorities; "LANDFIRE is fire-focused"; native classification preserved; crosswalks advisory) — central card for this README; v0.1 cited no atlas cards. (d) explicit citation to **`KFM-P18-PROG-0032`** (active Pass 32 — LANDFIRE LDist 2025 source descriptor with early-release status); v0.1 did not cite. (e) explicit citation to **`KFM-P25-PROG-0010`** (active Pass 32 — GAP/LANDFIRE descriptor records ecological system / USNVC classification, product version, raster/vector form, source URI, thematic role); v0.1 did not cite. (f) explicit citation to **`KFM-P25-IDEA-0010`** (active Pass 32 — LANDFIRE EVT + USNVC hierarchy supports county facies summaries, confidence metrics, signed COG/MVT derivatives); v0.1 did not cite. (g) explicit citation to **`KFM-P25-FEAT-0005`** (active Pass 32 — vegetation facies county map); v0.1 did not cite. (h) explicit citation to **`KFM-P25-PROG-0024`** (active Pass 32 — LANDFIRE EVT county summary pipeline; per-county area by nvc_code + confidence metrics + signed derivative references) — operationally definitive LANDFIRE pipeline card; v0.1 did not cite. (i) explicit citation to **`KFM-P25-PROG-0025`** (active Pass 32 — USNVC nvc_code metadata crosswalk preserves ecological system, USNVC group, ruderal/natural status, class labels, source version); v0.1 did not cite. (j) explicit citation to **`ML-K-067`** (Master MapLibre — LANDFIRE EVT rasters → COGs with signed derivative provenance); v0.1 did not cite. (k) Parallel-pattern citations to `KFM-P20-IDEA-0002` (mask-aware HLS vegetation analytics), `KFM-P24-PROG-0051` (Soils PMTiles/COG artifact contract — distribution pattern), `KFM-P13-PROG-0018` (deterministic grid generalization — applied weakly). (l) Land-cover cluster framing: LANDFIRE positioned alongside CDL (crop-focused), NLCD (broad multi-year), GAP (biodiversity-focused) per `KFM-P2-IDEA-0028`; advisory-only crosswalks explicit. (m) Domain reach framing: LANDFIRE products → Habitat, Flora, Fauna (substrate), Hazards (fire-context), Agriculture (crosswalk). (n) USNVC integration: `nvc_code` as first-class identifier preserved alongside LANDFIRE-native code per `KFM-P25-PROG-0025`. (o) Distribution shape: COG (continuous rasters) + PMTiles (vector facies) per `ML-K-067` + `KFM-P24-PROG-0051`-parallel. (p) Per-product pages enumerated: `landfire.md` (umbrella), `evt.md`, `ldist.md`, `fuels.md`, `disturbance.md` (latter four PROPOSED). (q) Added §1 NOTE callout: v0.1 → v0.2 promotion. (r) Added §1 IMPORTANT callout: beyond §7.3 + OPEN-DSC-14. (s) Added §1 IMPORTANT callout: connector path correction OPEN-LF-01. (t) Added §4 TIP callout: EVT is operationally most-cited LANDFIRE product (four cards + ML-K-067). (u) Added §4 NOTE callout: LDist 2025 early-release status. (v) Added §5 CAUTION callout: crosswalks advisory not authoritative. (w) Added §8 NOTE callout: rights/sensitivity per-product NEEDS VERIFICATION. (x) Added §9 TIP callout: COG + PMTiles distribution pattern parallel to Soils per `KFM-P24-PROG-0051`. (y) Built full §11 Mermaid pipeline diagram with three subgraphs (LANDFIRE universe, KFM land-cover cluster, KFM governance lanes) showing EVT pipeline + USNVC crosswalk + advisory-only crosswalks. (z) Built §14 open verification table with twelve items (OPEN-LF-01 through OPEN-LF-11 + OPEN-DSC-03 + OPEN-DSC-14). (aa) Built §15 related-docs with twenty-three sibling links including sibling family READMEs (`isric/` parallel, `usgs/`, `nrcs/`, `kansas/`) + corpus-card reference group. (bb) Built Appendix A atlas idea-card lineage with 21 cards. (cc) Built Appendix B change log (this entry). (dd) Updated meta block to v0.2 with full related-docs list (28 entries) and 5-paragraph notes block. (ee) Updated badges: added doc-version, family-status, land-cover-cluster, focus, interagency, USNVC, distribution, rights, last-updated. | `<flora-domain-steward / habitat-domain-steward / hazards-domain-steward — TODO>` |

[Back to top](#landfire-source-family--catalog-readme)

---

<sub>**Last updated:** 2026-05-21 · **Status:** `draft` (v0.2) · **Brief class:** family-README · **§7.3 status:** PROPOSED beyond canonical nine — `OPEN-DSC-14` · **Owners:** _TODO — docs steward + source steward + habitat/flora/fauna/hazards domain stewards_</sub>

<sub>**Family lane:** `connectors/landfire/` — PROPOSED beyond §7.3 per OPEN-LF-02 / OPEN-DSC-14 (canonical nine: `usgs/`, `fema/`, `noaa/`, `nrcs/`, `kansas/`, `gbif/`, `inaturalist/`, `census/`, `local_upload/`). v0.1's `connectors/lf/` corrected to v0.2's `connectors/landfire/` per OPEN-LF-01.</sub>

<sub>**Authority of this brief:** family README; cites authority, does not own it. The per-product `SourceDescriptor`s for LANDFIRE products are the source of truth for rights, sensitivity, cadence, citation.</sub>

<sub>**Land-cover cluster:** LANDFIRE (fire-focused) ‖ USDA CDL (crop-focused annual) ‖ USGS NLCD (broad multi-year) ‖ USGS GAP (biodiversity-focused) per `KFM-P2-IDEA-0028`. Native classification preserved; crosswalks advisory.</sub>

<sub>**Operational spine:** EVT county summary pipeline per `KFM-P25-PROG-0024` (per-county area by nvc_code + confidence metrics + signed derivative references); USNVC crosswalk per `KFM-P25-PROG-0025`; vegetation facies county map per `KFM-P25-FEAT-0005`; COG + PMTiles distribution per `ML-K-067` + `KFM-P24-PROG-0051`-parallel.</sub>

<sub>**Related doctrine:** [`../../../doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) · [`../../../doctrine/lifecycle-law.md`](../../../doctrine/lifecycle-law.md) · [`../../../doctrine/truth-posture.md`](../../../doctrine/truth-posture.md) · [`../../../registers/AUTHORITY_LADDER.md`](../../../registers/AUTHORITY_LADDER.md) · [`../../../registers/DRIFT_REGISTER.md`](../../../registers/DRIFT_REGISTER.md)</sub>

<sub>[↑ Back to top](#landfire-source-family--catalog-readme)</sub>
