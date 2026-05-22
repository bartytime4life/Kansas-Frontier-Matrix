<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-landfire-landfire
title: LANDFIRE Vegetation and Fuels — Source Catalog Entry
type: standard
subtype: source-catalog-entry
version: v0.2
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward for landfire + Habitat/Flora/Fauna/Hazards domain stewards>
created: 2026-05-21
updated: 2026-05-21
policy_label: public
related:
  - docs/sources/catalog/landfire/README.md
  - docs/sources/catalog/landfire/evt.md
  - docs/sources/catalog/landfire/ldist.md
  - docs/sources/catalog/landfire/fuels.md
  - docs/sources/catalog/landfire/disturbance.md
  - docs/sources/catalog/README.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/PROFILES.md
  - docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - docs/sources/catalog/OPEN-QUESTIONS.md
  - docs/sources/catalog/_template/SOURCE_PRODUCT_TEMPLATE.md
  - docs/sources/catalog/isric/README.md
  - docs/sources/catalog/usgs/README.md
  - docs/sources/catalog/nrcs/README.md
  - docs/sources/catalog/kansas/README.md
  - docs/sources/catalog/kansas/kbs.md
  - docs/sources/catalog/kansas/kdwp.md
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
tags: [kfm, sources, catalog, landfire, land-cover, vegetation, fuels, fire, evt, bps, evc, evh, ldist, fbfm13, fbfm40, usnvc, nvc-code, cog, pmtiles, kfm-p2-idea-0028, kfm-p18-prog-0032, kfm-p25-prog-0010, kfm-p25-idea-0010, kfm-p25-feat-0005, kfm-p25-prog-0024, kfm-p25-prog-0025, ml-k-067]
notes:
  - >-
    v0.2 promotes the v0.1 PROPOSED scaffold (placeholder body with
    `Yes / No (NEEDS VERIFICATION)` cells; `connectors/lf/` two-letter
    abbreviation; no atlas-card citations) into a full umbrella per-product
    page consistent with sibling v0.2 product pages in this conversation
    series.
  - >-
    Structural framing (NEW in v0.2) — umbrella vs per-sub-product. This
    page is the LANDFIRE Vegetation and Fuels UMBRELLA per-product page
    under the family-README at `./README.md` (v0.2 in this conversation
    series). Per `KFM-P2-IDEA-0028` (CONFIRMED, Pass 32), LANDFIRE is one of
    four KFM land-cover authorities; "LANDFIRE is fire-focused." Per the
    landfire/ family README v0.2 §4, the LANDFIRE program publishes
    multiple product families, each with its own `SourceDescriptor` per
    `KFM-P25-PROG-0010`. This umbrella page covers the institution-level
    LANDFIRE program posture; per-product detail (EVT, LDist, fuels,
    disturbance) lives in sibling per-sub-product pages.
  - >-
    Connector path correction in v0.2 — OPEN-LFP-01. v0.1 used
    `connectors/lf/` (two-letter abbreviation). v0.2 corrects to
    `connectors/landfire/` (full kebab-case family name at top level). Both
    are "beyond §7.3" until ADR-ratified per OPEN-DSC-14. Same correction
    applied at family-README level in `./README.md` v0.2 OPEN-LF-01.
  - >-
    `connectors/landfire/` lane is **PROPOSED beyond §7.3** per Directory
    Rules v1.2 §7.3 (CONFIRMED at commit
    `b6a27916bbb9e07cbf3752870c867476e1e094e7`): nine canonical families =
    `usgs/`, `fema/`, `noaa/`, `nrcs/`, `kansas/`, `gbif/`, `inaturalist/`,
    `census/`, `local_upload/`. LANDFIRE NOT among them; OPEN-DSC-14 ADR
    pending. Same status as ISRIC v0.2.
  - >-
    Atlas card lineage CONFIRMED (all eight LANDFIRE-specific cards from
    family README v0.2 inherit here): `KFM-P2-IDEA-0028` (CONFIRMED, Pass
    32 — land-cover authority cluster); `KFM-P18-PROG-0032` (active, Pass
    32 — LDist 2025 early-release source descriptor); `KFM-P25-PROG-0010`
    (active, Pass 32 — GAP/LANDFIRE descriptor); `KFM-P25-IDEA-0010`
    (active, Pass 32 — LANDFIRE EVT + USNVC hierarchy);
    `KFM-P25-FEAT-0005` (active, Pass 32 — vegetation facies county map);
    `KFM-P25-PROG-0024` (active, Pass 32 — LANDFIRE EVT county summary
    pipeline; operationally definitive card); `KFM-P25-PROG-0025` (active,
    Pass 32 — USNVC nvc_code metadata crosswalk); `ML-K-067` (Master
    MapLibre — EVT raster → COG with signed derivative provenance).
    Parallel patterns: `KFM-P20-IDEA-0002` (mask-aware HLS vegetation
    analytics); `KFM-P24-PROG-0051` (Soils PMTiles + COG artifact
    contract); `KFM-P13-PROG-0018` (deterministic grid generalization —
    applied weakly).
[/KFM_META_BLOCK_V2] -->

# LANDFIRE Vegetation and Fuels — Source Catalog Entry

> **Umbrella per-product page** for the **LANDFIRE Vegetation and Fuels** program — the interagency (USGS + USFS) source family that produces national vegetation, wildland-fuels, disturbance, and condition layers, carrying a class-map version because class semantics drift. CONFIRMED member of the four-source KFM land-cover authority cluster per `KFM-P2-IDEA-0028`: *"Land cover authorities ingested by KFM include USDA Cropland Data Layer (CDL), NLCD (National Land Cover Database), **LANDFIRE (fire-related land cover)**, and GAP (Gap Analysis Program). Each is ingested with native classification preserved and cross-walked to a common vocabulary where possible."* Parented under [`./README.md`](./README.md) v0.2 (`landfire/` family).

[![Status: draft](https://img.shields.io/badge/status-draft-yellow)](#)
[![doc-version](https://img.shields.io/badge/doc--version-v0.2-blue)](#)
[![family-status](https://img.shields.io/badge/family-beyond%20%C2%A77.3%20(OPEN--DSC--14)-orange)](./README.md)
[![umbrella-of](https://img.shields.io/badge/umbrella%20of-evt%20%E2%9C%99%20ldist%20%E2%9C%99%20fuels%20%E2%9C%99%20disturbance-7e57c2)](./README.md)
[![land-cover-cluster](https://img.shields.io/badge/land--cover-CDL%20%E2%9C%99%20NLCD%20%E2%9C%99%20LANDFIRE%20%E2%9C%99%20GAP-success)](#)
[![focus](https://img.shields.io/badge/focus-fire--related%20land%20cover-c62828)](#)
[![interagency](https://img.shields.io/badge/interagency-USGS%20%2B%20USFS-1565c0)](#)
[![source-role](https://img.shields.io/badge/source--role-observed%20raster%20%2B%20aggregate%20derivative-blue)](#5-source-roles)
[![USNVC](https://img.shields.io/badge/classification-USNVC%20nvc_code-7e57c2)](#)
[![distribution](https://img.shields.io/badge/distribution-COG%20%2B%20PMTiles%2FMVT-informational)](#)
[![rights](https://img.shields.io/badge/rights-US--Federal%20public%20domain%20(NEEDS%20VERIFICATION)-orange)](#)
[![last-updated](https://img.shields.io/badge/last--updated-2026--05--21-informational)](#)

**Status:** `draft` (v0.2) &nbsp;·&nbsp; **Family:** [`landfire`](./README.md) (v0.2 — PROPOSED beyond §7.3 per OPEN-DSC-14) &nbsp;·&nbsp; **Parent family-README:** [`./README.md`](./README.md) v0.2 &nbsp;·&nbsp; **Owners:** `<TODO — docs steward + source steward + habitat/flora/fauna/hazards domain stewards>` &nbsp;·&nbsp; **Last reviewed:** 2026-05-21

---

## Quick jump

- [1. Scope](#1-scope) · [2. Status and source basis](#2-status-and-source-basis) · [3. Repo fit](#3-repo-fit) · [4. Inputs accepted](#4-inputs-accepted)
- [5. Source roles](#5-source-roles) · [6. Sensitivity and publication posture](#6-sensitivity-and-publication-posture) · [7. Pipeline diagram](#7-pipeline-diagram)
- [8. Cadence and freshness](#8-cadence-and-freshness) · [9. Rights and access](#9-rights-and-access) · [10. Authority anchoring](#10-authority-anchoring-and-crosswalks)
- [11. Distribution shape](#11-distribution-shape) · [12. Catalog profiles](#12-catalog-profiles) · [13. Pre-admission checklist](#13-pre-admission-checklist)
- [14. Open verification](#14-open-verification-items) · [15. FAQ](#15-faq) · [16. Related docs](#16-related-docs)
- [Appendix A — Descriptor field placeholders](#appendix-a--descriptor-field-placeholders) · [Appendix B — Atlas idea-card lineage](#appendix-b--atlas-idea-card-lineage) · [Appendix C — Change log](#appendix-c--change-log)

---

## 1. Scope

> [!NOTE]
> **v0.1 → v0.2 promotion.** This page was authored in v0.1 as a thin PROPOSED scaffold (placeholder body, `Yes / No (NEEDS VERIFICATION)` cells, no operational detail beyond the Pass-10 C4-01 provenance fields, no LANDFIRE-specific atlas-card citations). v0.2 promotes it into a full umbrella per-product page consistent with sibling v0.2 product pages (`kansas-mesonet.md`, `kbs.md`, `ku-herbarium.md`, `ku-nhm.md`, etc.) authored earlier in this conversation series.

> [!IMPORTANT]
> **Path correction in v0.2 (connector — OPEN-LFP-01).** v0.1 used `connectors/lf/` (two-letter top-level abbreviation, neither §7.3 family nor full kebab-case). v0.2 corrects to `connectors/landfire/` (full kebab-case family name at top level). Both placements are "beyond §7.3" until ADR-ratified per OPEN-DSC-14. Same correction applied at family-README level (`./README.md` v0.2 OPEN-LF-01).

> [!IMPORTANT]
> **Structural framing (new in v0.2) — umbrella vs per-sub-product.** This dossier is the **LANDFIRE Vegetation and Fuels umbrella per-product page**. Per `KFM-P25-PROG-0010` (CONFIRMED, Pass 32), each LANDFIRE product gets its own `SourceDescriptor`. The family-README at [`./README.md`](./README.md) v0.2 §4 enumerates per-sub-product pages for the major LANDFIRE product families:
> - **EVT** (Existing Vegetation Type) → [`./evt.md`](./evt.md) (PROPOSED) — most-cited in corpus (`KFM-P25-IDEA-0010`, `KFM-P25-FEAT-0005`, `KFM-P25-PROG-0024`, `KFM-P25-PROG-0025`, `ML-K-067`)
> - **LDist 2025** (Limited Disturbance) → [`./ldist.md`](./ldist.md) (PROPOSED) — early-release status per `KFM-P18-PROG-0032`
> - **Fuels** (FBFM13, FBFM40, FVT, FVH, FVC) → [`./fuels.md`](./fuels.md) (PROPOSED)
> - **Historical disturbance** (other than LDist 2025) → [`./disturbance.md`](./disturbance.md) (PROPOSED)
>
> This umbrella page sets institution-level LANDFIRE-program posture (rights, cadence floor, advisory-crosswalk discipline, distribution shape, USNVC integration); the per-sub-product pages set product-specific admission posture. Where this page states posture, the per-sub-product pages **inherit** unless explicitly overridden. Same umbrella-vs-surface pattern as KBS / KSHS / KSU R&E in the kansas/ family.

**This dossier** describes the LANDFIRE Vegetation and Fuels program as a KFM source: what role it plays in the KFM source ladder, what claims its products can support (and which they cannot), the rights / sensitivity / access posture admission must respect, and the lifecycle gates a LANDFIRE-derived record passes before it touches a public surface.

**What this dossier is not.** It is not a `SourceDescriptor` instance, a connector, a policy bundle, a route, a per-sub-product page, or a release manifest. Each of those has its own canonical home.

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 2. Status and source basis

| Claim | Label | Basis |
|---|---|---|
| LANDFIRE is a CONFIRMED KFM land-cover authority. | **CONFIRMED doctrine** | `KFM-P2-IDEA-0028` (CONFIRMED, Pass 32) — "Land cover authorities ingested by KFM include USDA Cropland Data Layer (CDL), NLCD (National Land Cover Database), **LANDFIRE (fire-related land cover)**, and GAP (Gap Analysis Program)." |
| LANDFIRE is the fire-focused member of the four-source land-cover cluster. | **CONFIRMED doctrine** | `KFM-P2-IDEA-0028` — "CDL is annual and crop-focused; NLCD is multi-year and broad; **LANDFIRE is fire-focused**; GAP is biodiversity-focused." |
| Native classification preserved; crosswalks advisory not authoritative. | **CONFIRMED doctrine** | `KFM-P2-IDEA-0028` tension — "Classification crosswalks are inherently lossy; the corpus directs that crosswalks be advisory rather than authoritative." |
| Per-product `SourceDescriptor` shape. | **CONFIRMED active card** | `KFM-P25-PROG-0010` (active, Pass 32) — "A GAP/LANDFIRE descriptor should record ecological system or USNVC classification, product version, raster/vector form, source URI, and thematic role." |
| LANDFIRE EVT + USNVC hierarchy supports county facies summaries. | **CONFIRMED active card** | `KFM-P25-IDEA-0010` (active, Pass 32). |
| Per-county area by `nvc_code` + confidence metrics + signed derivative references. | **CONFIRMED active card** | `KFM-P25-PROG-0024` (active, Pass 32) — operationally definitive LANDFIRE pipeline card. |
| USNVC `nvc_code` crosswalk preserves ecological system + USNVC group + ruderal/natural status + class labels + source version. | **CONFIRMED active card** | `KFM-P25-PROG-0025` (active, Pass 32). |
| Vegetation facies county map renders LANDFIRE/USNVC per-county summaries + confidence from signed derivatives. | **CONFIRMED active card** | `KFM-P25-FEAT-0005` (active, Pass 32). |
| LDist 2025 product family carries early-release status. | **CONFIRMED active card** | `KFM-P18-PROG-0032` (active, Pass 32) — "The LANDFIRE 2025 Limited Disturbance product family should be represented as a source descriptor with early-release status, cadence, rights, and change-detection role." |
| LANDFIRE EVT rasters convert to COGs with signed derivative provenance. | **CONFIRMED active card** | `ML-K-067` (Master MapLibre Components, EXPANDED). |
| `connectors/landfire/` family lane is PROPOSED beyond §7.3. | **PROPOSED** | Directory Rules v1.2 §7.3 nine-family list does NOT include LANDFIRE; OPEN-DSC-14 ADR pending. |
| `connectors/lf/` (v0.1) corrected to `connectors/landfire/` (v0.2). | **PROPOSED** | OPEN-LFP-01 path correction. |
| Specific LANDFIRE product endpoints, version cadence, current LDist 2025 release status. | **NEEDS VERIFICATION** | Not pinned by corpus; per-product descriptors must capture. |

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 3. Repo fit

> [!NOTE]
> Per Directory Rules v1.2 §6.1, `docs/sources/` is the doctrinal home for source-descriptor standards and source families. v0.2 adopts `docs/sources/catalog/<family>/<product>.md` as the catalog convention. **`connectors/landfire/` is PROPOSED beyond §7.3** per OPEN-DSC-14.

This document is **explanation**. It does not store machine-readable descriptors, define object meaning, validate shape, or make admit/deny decisions. Those live in their canonical homes:

| Concern | Canonical home (v0.2 path) | What lives there |
|---|---|---|
| Human-readable catalog entry (this file) | `docs/sources/catalog/landfire/landfire.md` | This document — LANDFIRE Vegetation and Fuels umbrella. |
| Per-sub-product pages | `docs/sources/catalog/landfire/{evt,ldist,fuels,disturbance}.md` | Per-LANDFIRE-product briefs (PROPOSED). |
| Family-level README | `docs/sources/catalog/landfire/README.md` (v0.2) | Parent family-README; lists this umbrella + per-sub-product pages. |
| Source-descriptor standard | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` (PROPOSED) | Field-by-field doctrine for `SourceDescriptor`. |
| Machine-readable descriptor record | `data/registry/sources/landfire/<product>/source_descriptor.yaml` (PROPOSED) | Per-product `SourceDescriptor` per `KFM-P25-PROG-0010` field set. |
| Schema (shape) | `schemas/contracts/v1/source/source_descriptor.schema.json` (default per ADR-0001) | JSON Schema for `SourceDescriptor`. |
| Object-family meaning | `contracts/source/` (semantic Markdown) | What a `SourceDescriptor` means. |
| USNVC crosswalk schema | `schemas/contracts/v1/crosswalk/usnvc_nvc_code.schema.json` (PROPOSED per `KFM-P25-PROG-0025`) | USNVC `nvc_code` metadata crosswalk shape. |
| Admit / restrict / deny policy | `policy/<domain>/` and `policy/sensitivity/` | OPA / policy bundle entries. |
| Connector (fetch + admission) | `connectors/landfire/` — **PROPOSED beyond §7.3** per OPEN-DSC-14. **v0.1 used `connectors/lf/` (incorrect abbreviation); see OPEN-LFP-01.** | Source-specific fetcher; output → `data/raw/<domain>/landfire/<product>/<run_id>/`. |
| Pipelines (executable) | `pipelines/ingest/`, `pipelines/normalize/`, `pipelines/validate/`, `pipelines/catalog/`, `pipelines/publish/` with `pipeline_specs/<domain>/` declarative companion | LANDFIRE EVT county summary pipeline per `KFM-P25-PROG-0024`. |
| Pipeline specs | `pipeline_specs/habitat/landfire-evt-county-summary.yaml` (PROPOSED) | Declarative companion to executable pipeline. |
| Domain receiving lanes | `docs/domains/habitat/`, `docs/domains/flora/`, `docs/domains/fauna/`, `docs/domains/hazards/` | Where LANDFIRE-derived facies/vegetation/fuel/disturbance objects are owned. |
| USNVC crosswalk validator | `tools/validators/usnvc_crosswalk_validator/` (PROPOSED per `KFM-P25-PROG-0025`) | Validates USNVC `nvc_code` metadata against required fields. |

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 4. Inputs accepted

The following classes of LANDFIRE-program material are **in scope** for admission, subject to per-sub-product page detail, source-role tagging, rights resolution, and the standard receipt envelope.

- **Existing Vegetation Type (EVT) rasters** — LANDFIRE-native classification (LANDFIRE class codes preserved); USNVC `nvc_code` crosswalk per `KFM-P25-PROG-0025`; per-county facies summary derivatives per `KFM-P25-PROG-0024`. Treated as **`observed`** raster product at admission; derived county summaries are **`aggregate`** per Atlas §24.1.3. See [`./evt.md`](./evt.md) (PROPOSED) for per-sub-product detail.
- **Biophysical Settings (BPS) rasters** — modeled pre-European-settlement vegetation reference. Treated as **`modeled`** per Atlas §24.1.3 (BPS is a modeled reference, not an observation).
- **Existing Vegetation Cover (EVC) and Existing Vegetation Height (EVH) rasters** — continuous-property surfaces; admit as `observed` raster products.
- **Limited Disturbance (LDist) 2025** — disturbance polygons / rasters per `KFM-P18-PROG-0032` with early-release status flag. Treated as **`observed`** (disturbance observed) at admission; change-detection role explicit. See [`./ldist.md`](./ldist.md) (PROPOSED).
- **Wildland Fuels products** — Fire Behavior Fuel Models (FBFM13, FBFM40), Forest Vegetation Type (FVT), Forest Vegetation Height (FVH), Forest Vegetation Cover (FVC), Fuel Characteristic Classification (FCC), Canopy products. Treated as **`modeled`** per Atlas §24.1.3 (fuel models are modeled abstractions of vegetation properties, not direct observations). See [`./fuels.md`](./fuels.md) (PROPOSED).
- **Historical disturbance products** (other than LDist 2025) — admit as `observed` disturbance per Atlas §24.1.3. See [`./disturbance.md`](./disturbance.md) (PROPOSED).

Every admitted LANDFIRE record carries: source identity (`source_id: landfire-<product>`), source role per Atlas §24.1.3, product version, raster/vector form, source URI, thematic role per `KFM-P25-PROG-0010`, rights posture (US Federal public-domain assumed; NEEDS VERIFICATION), retrieval metadata (ETag / Last-Modified per `C3-01`), content checksum (`spec_hash` per `C5-04`), and a citation back to LANDFIRE. Records lacking a verifiable product-version pin MUST go to `data/quarantine/`.

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 5. Source roles

The source-role taxonomy is **doctrine**, not stylistic preference (Atlas §24.1.3, CONFIRMED Pass-23/32). Each LANDFIRE admission picks exactly one role; corrections produce a *new* descriptor and a `CorrectionNotice`, never an in-place edit.

| Role | Used for LANDFIRE when… | Example |
|---|---|---|
| `observed` | LANDFIRE publishes a raster representing observed vegetation, cover, height, type, or observed disturbance. **Dominant role for EVT, EVC, EVH, LDist, historical disturbance.** | EVT 2022 raster covering Kansas. |
| `modeled` | LANDFIRE publishes a modeled reference or modeled abstraction. **Dominant role for BPS (pre-European-settlement reference) and Fuels (FBFM13/40, FVT/FVH/FVC — fuel models are modeled surfaces).** | BPS 2020 modeled reference; FBFM40 fire behavior fuel model. |
| `aggregate` | LANDFIRE-derived per-county or per-region summary computed from EVT raster. | KFM `KFM-P25-PROG-0024` per-county area by `nvc_code` derived from EVT. |
| `administrative` | LANDFIRE program-level metadata / class-map version index. | LANDFIRE class-map version registry. |
| `candidate` | A pre-validation staging of a newly released product (e.g., LDist 2025 early-release window). | Pre-admission LDist 2025 staging. |

> [!CAUTION]
> **Role-purity is not optional.** Per Atlas §24.1.3 (CONFIRMED), `source_role` is set at admission and never edited in place; corrections produce a new descriptor and a `CorrectionNotice`. A LANDFIRE EVT raster admitted as `observed` MUST NOT be silently reclassified as `modeled` (or vice versa) by downstream code. The EVT vs BPS vs Fuels distinction is exactly this role distinction.

> [!IMPORTANT]
> **BPS is `modeled`, not `observed`.** Biophysical Settings rasters represent *pre-European-settlement reference vegetation* — a modeled reconstruction, not an observation. Citing a BPS surface as "the vegetation at location X" is an anti-collapse failure per Atlas §24.1.2 ("Modeled product labeled as observed → DENY"). Same applies to Fuels products (FBFM13, FBFM40, etc.) — these are modeled abstractions of fuel behavior, not observations.

> [!IMPORTANT]
> **Per-county facies summaries are `aggregate`, not `observed`.** The output of the `KFM-P25-PROG-0024` EVT county summary pipeline (per-county area by `nvc_code` with confidence metrics) is an `aggregate` derivative. Citing "Riley County has 23% mixed-grass prairie" without surfacing the aggregation receipt is an anti-collapse failure per Atlas §24.1.2 ("Aggregate cited as a per-place truth → DENY at trust membrane").

> [!NOTE]
> **`authority` and `regulatory` are NOT LANDFIRE source-role-enum values.** LANDFIRE is an interagency mapping program publishing observed and modeled surfaces; it is not a regulatory body (compare KDWP per `KFM-P19-IDEA-0005`) and not a taxonomic / classification authority (compare USNVC, which IS the classification authority that LANDFIRE crosswalks to per `KFM-P25-PROG-0025`). The USNVC integration is downstream: LANDFIRE = `observed | modeled`, USNVC = classification reference.

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 6. Sensitivity and publication posture

LANDFIRE products are publicly distributed at full spatial resolution by US Federal agencies (USGS + USFS). The sensitivity floor is correspondingly low.

| Sensitivity class | Why LANDFIRE material engages it | Default outcome | `C6-01` rank guideline | Required controls |
|---|---|---|---|---|
| **Public broad-scale vegetation/fuels surfaces** | Standard LANDFIRE distribution. | ALLOW public release at full LANDFIRE-native resolution. | rank 0 (public / open) | Standard receipt envelope; `spec_hash`; `kfm:provenance` block per `C4-01`. |
| **Aggregated per-county facies summaries** | LANDFIRE EVT pipeline outputs per `KFM-P25-PROG-0024`. | ALLOW with `AggregationReceipt` surfaced per Atlas §24.2.1. | rank 0 | Aggregation receipt; confidence metrics surfaced. |
| **Early-release LDist 2025 products** | Stability NEEDS VERIFICATION per `KFM-P18-PROG-0032`. | ALLOW with explicit early-release flag in descriptor + UI surfacing. | rank 0 (with caveat flag) | Early-release flag preserved end-to-end; cadence accommodates product revisions. |
| **LANDFIRE-derived joins with sensitive cross-domain data** | Special-case review only — e.g., LANDFIRE facies join with KBS NHI rare-plant communities or KDWP SINC sensitive-species occurrences. | Sensitive component governs: deny / generalize / quarantine the sensitive component, NOT the LANDFIRE component. | rank inherited from sensitive partner | Per `KFM-P13-PROG-0018` deterministic grid generalization on sensitive partner. |

> [!TIP]
> **`KFM-P13-PROG-0018` applies weakly to LANDFIRE.** The deterministic grid generalization machinery (with rule-version provenance) is operationally critical for sensitive-species locations (KBS NHI, KDWP SINC) and sensitive cultural sites (KHRI, KU NHM Anthropology / Archaeology). It applies only weakly to LANDFIRE because LANDFIRE is publicly distributed at full resolution by US Federal agencies — the public release already establishes the floor. The machinery DOES apply when LANDFIRE-derived analyses *join* sensitive partner data: the join inherits the partner's sensitivity.

> [!WARNING]
> **Early-release products require explicit handling** per `KFM-P18-PROG-0032`. LDist 2025 "should be represented as a source descriptor with early-release status, cadence, rights, and change-detection role." This means the descriptor MUST carry an early-release flag, the connector cadence MUST accommodate product revisions during the early-release window, and the UI surface MUST surface the early-release status to end-users. Treating early-release products as stable releases is a misrepresentation of stability — a soft-but-real cite-or-abstain violation.

> [!TIP]
> **T0–T4 vs `C6-01` 0–5 reconciliation** (same OPEN as sibling v0.2 pages — KHRI OQ-KHRI-14, KSU R&E OQ-KSURE-16, KU Herbarium OPEN-KUHERB-10, KU NHM OPEN-KUNHM-14). For LANDFIRE this is moot because LANDFIRE-direct material sits at rank 0; the open is preserved for inherited-sensitivity scenarios via cross-domain joins.

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 7. Pipeline diagram

```mermaid
flowchart LR
  subgraph LF["LANDFIRE program (external)"]
    direction TB
    EVT_R[EVT raster<br/>observed]
    BPS_R[BPS raster<br/>modeled reference]
    EVC_R[EVC raster<br/>observed continuous]
    EVH_R[EVH raster<br/>observed continuous]
    LDIST_R[LDist 2025<br/>observed disturbance<br/>early-release status]
    FUEL_R[Fuels<br/>FBFM13/40/FVT/FVH/FVC<br/>modeled]
  end

  subgraph CLUSTER["KFM land-cover cluster<br/>KFM-P2-IDEA-0028"]
    CDL[USDA CDL]
    NLCD[USGS NLCD]
    LFM[LANDFIRE<br/>fire-focused]
    GAP[USGS GAP]
  end

  subgraph KFM["KFM governance lanes"]
    CONN[Connector<br/>connectors/landfire/<br/>PROPOSED beyond §7.3<br/>OPEN-DSC-14]
    DESC[SourceDescriptor<br/>data/registry/sources/landfire/&lt;product&gt;/<br/>per KFM-P25-PROG-0010]
    USNVC_X[USNVC crosswalk<br/>per KFM-P25-PROG-0025<br/>ecosystem + USNVC group +<br/>ruderal/natural + class +<br/>source version]
    RAW[(data/raw/&lt;domain&gt;/landfire/&lt;product&gt;/&lt;timestamp&gt;/)]
    WORK[(data/work/&lt;domain&gt;/&lt;run_id&gt;/)]
    EVT_PIPE[EVT county summary pipeline<br/>per-county area by nvc_code<br/>+ confidence metrics<br/>+ signed derivative refs<br/>per KFM-P25-PROG-0024]
    PROC[(data/processed/&lt;domain&gt;/&lt;spec_hash&gt;/<br/>COG continuous rasters<br/>+ PMTiles vector facies<br/>per ML-K-067 + KFM-P24-PROG-0051 parallel)]
    CAT[(data/catalog/<br/>stac | dcat | prov / &lt;domain&gt;/<br/>kfm-landfire-&lt;product&gt;)]
    PUB[(data/published/<br/>vegetation facies county map<br/>per KFM-P25-FEAT-0005)]
  end

  EVT_R --> LFM
  BPS_R --> LFM
  EVC_R --> LFM
  EVH_R --> LFM
  LDIST_R --> LFM
  FUEL_R --> LFM

  LFM --> CONN
  CDL -. advisory only<br/>KFM-P2-IDEA-0028 .-> CONN
  NLCD -. advisory only .-> CONN
  GAP -. advisory only .-> CONN

  CONN --> RAW
  CONN --> DESC
  DESC --> USNVC_X
  RAW --> WORK
  USNVC_X --> WORK
  WORK --> EVT_PIPE
  EVT_PIPE --> PROC
  WORK --> PROC
  PROC --> CAT
  CAT --> PUB

  classDef confirmed fill:#d5e8d4,stroke:#82b366;
  classDef proposed stroke-dasharray: 4 3;
  classDef beyond fill:#fff4e0,stroke:#d4882b;
  class LFM,EVT_R,EVC_R,EVH_R confirmed;
  class BPS_R,FUEL_R confirmed;
  class LDIST_R beyond;
  class CONN,DESC,USNVC_X,EVT_PIPE,RAW,WORK,PROC,CAT,PUB proposed;
```

> [!NOTE]
> Native classification preserved at every stage (per `KFM-P2-IDEA-0028`); cluster-member crosswalks (CDL ↔ NLCD ↔ LANDFIRE ↔ GAP) attach as advisory edges, not authoritative joins. The `EVT county summary pipeline` per `KFM-P25-PROG-0024` is the operationally most-developed LANDFIRE pipeline in the corpus. LDist 2025 highlighted in early-release styling.

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 8. Cadence and freshness

| Concern | Value | Status |
|---|---|---|
| Detection signal | ETag / Last-Modified on LANDFIRE product distribution endpoints | **CONFIRMED operational rule** per `C3-01` smart-sync HTTP validators |
| Cadence (general LANDFIRE) | Per-product; LANDFIRE major-version releases historically every 2–3 years | **NEEDS VERIFICATION** per current LANDFIRE program publishing schedule |
| Cadence (LDist 2025 early-release window) | Likely more frequent than stable releases during early-release window | **NEEDS VERIFICATION** per `KFM-P18-PROG-0032` |
| Class-map version handling | "carrying a class-map version because class semantics drift" — `product_version` field MUST pin the LANDFIRE class-map version | **CONFIRMED operational mechanism** per `KFM-P25-PROG-0010` (records "product version") |
| Snapshot vs incremental | LANDFIRE distributes complete snapshots per major version; incremental change detection for LDist is part of the LDist role per `KFM-P18-PROG-0032` | **CONFIRMED operational rule** |
| Per-product cadence | Defined per per-sub-product page | **PROPOSED** |

> [!IMPORTANT]
> **Class-map version is first-class metadata.** The subtitle of this page ("carrying a class-map version because class semantics drift") is operationally critical: LANDFIRE updates its classification semantics across major versions, so the same `nvc_code` or LANDFIRE-native class may have different meaning in EVT-2014 vs EVT-2020 vs EVT-2022. The `product_version` field per `KFM-P25-PROG-0010` MUST pin the specific class-map version. Joining records across LANDFIRE versions without surfacing the version pin is an anti-collapse risk.

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 9. Rights and access

| Posture dimension | Value | Status | Notes |
|---|---|---|---|
| Rights / terms of use | US Federal public domain (LANDFIRE is jointly produced by USGS and USFS — both US Federal agencies; products published without copyright restriction) | **PROPOSED — NEEDS VERIFICATION per product** | Confirmation required per product; standard US-federal assumption may have exceptions. |
| Attribution requirement | LANDFIRE program citation | **PROPOSED — NEEDS VERIFICATION** | Confirm citation template per product. |
| Redistribution | Generally unrestricted (US Federal public domain) | **PROPOSED — NEEDS VERIFICATION** | |
| Access method | Direct HTTP from LANDFIRE program distribution endpoints | **CONFIRMED operational mechanism** | ETag / Last-Modified per `C3-01`. |
| LANDFIRE distribution endpoint URLs | Per current LANDFIRE program configuration | **NEEDS VERIFICATION** | Not pinned by corpus. |
| Authentication | Public distribution; no authentication for standard products | **PROPOSED — NEEDS VERIFICATION** | |
| Cadence | Per major LANDFIRE release schedule | **NEEDS VERIFICATION** | See §8. |
| Persistent identifiers | LANDFIRE-native class code + USNVC `nvc_code` per `KFM-P25-PROG-0025` + product version | **CONFIRMED operational mechanism** | Three-way preservation; class-map-version aware. |
| Stewardship contact | LANDFIRE program (USGS + USFS) | **NEEDS VERIFICATION** | |
| Live connector in mounted repo | UNKNOWN | **UNKNOWN** | Family lane `connectors/landfire/` PROPOSED beyond §7.3 per OPEN-DSC-14. |

> [!CAUTION]
> **Unknown rights default to deny** per `C5-02` default-deny promotion. While US Federal public domain is the standard assumption for LANDFIRE products (both producing agencies are federal), per-product license verification is still required. Until per-product rights confirmation is recorded in the `SourceDescriptor`, harvested material stays in `data/raw/<domain>/landfire/<product>/` or `data/quarantine/`. The fail-closed posture protects against the rare case where a LANDFIRE product carries non-standard use restrictions.

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 10. Authority anchoring and crosswalks

LANDFIRE records anchor to the relevant external authority for the entity type, with LANDFIRE-native codes stored in parallel per the parallel-anchor rule (see related sibling v0.2 pages for the analogous discipline applied to KU NHM and KANU).

| Entity in LANDFIRE material | Required external anchor | LANDFIRE identifier role | Notes |
|---|---|---|---|
| Vegetation class | **USNVC `nvc_code`** (primary via `KFM-P25-PROG-0025`) | LANDFIRE-native class code preserved in parallel | Crosswalk preserves ecological system, USNVC group, ruderal/natural status, class labels, source version per `KFM-P25-PROG-0025`. **The corpus directs USNVC as the classification authority; LANDFIRE class codes are issuing-institution position.** |
| Cluster cross-walks (CDL, NLCD, GAP) | Member-native class | Advisory only per `KFM-P2-IDEA-0028` | Disagreements are recorded — not silently resolved. |
| Fuel model | LANDFIRE-native fuel-model code | Primary (no external authority) | Fuels are LANDFIRE-defined per `KFM-P25-PROG-0010` "thematic role." |
| Disturbance event | LANDFIRE LDist event identifier | Primary | Cross-walks to USFS FACTS, fire incident IDs PROPOSED. |
| Locality / place | USGS GNIS (primary, `C7-09`) | LANDFIRE pixel center / polygon centroid | County rollups per `KFM-P25-PROG-0024`. |
| Dataset / product version | LANDFIRE product version + class-map version | Primary | Per `KFM-P25-PROG-0010` records "product version"; per `KFM-P25-PROG-0025` records "source version." |
| Disturbance dates | source / observed / valid / retrieval / release / correction times per Atlas §24.8 | Preserved separately | LDist 2025 early-release adds "release" time semantics. |

> [!NOTE]
> Per project doctrine, **USNVC is the vegetation-classification authority** (`KFM-P25-PROG-0025`), and **the LANDFIRE class code is the issuing-institution position** for the specific raster. Both are preserved; the crosswalk records both. When LANDFIRE class semantics drift across major versions (e.g., EVT-2014 vs EVT-2022 disagree on the USNVC mapping for a particular pixel), the disagreement IS the data — recorded with `source_version` per `KFM-P25-PROG-0025`, not silently resolved.

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 11. Distribution shape

LANDFIRE products distribute through KFM as governed derivatives per the corpus-defined shape.

| Stage | Form | Atlas card |
|---|---|---|
| **Source** | LANDFIRE-native rasters (typically GeoTIFF) at LANDFIRE-published resolution | upstream |
| **RAW** | Original bytes preserved with `spec_hash`, ETag, Last-Modified | `C3-01` + `C5-04` |
| **PROCESSED — continuous rasters** | Converted to **Cloud-Optimized GeoTIFF (COG)** with signed derivative provenance | **`ML-K-067`** (CONFIRMED EXPANDED) — "LANDFIRE EVT rasters can be converted to COGs with signed derivative provenance" |
| **PROCESSED — vector derivatives** | Per-county facies summaries computed by EVT pipeline; signed COG/MVT derivatives | **`KFM-P25-PROG-0024`** (operationally definitive); **`KFM-P25-IDEA-0010`** |
| **PROCESSED — USNVC crosswalk** | USNVC `nvc_code` metadata crosswalk records | `KFM-P25-PROG-0025` |
| **CATALOG** | STAC Items per Collection `kfm-landfire-<product>` with `kfm:provenance` block | `C4-01`, `C4-02` |
| **PUBLISHED — map** | PMTiles for vector facies; COG for continuous rasters; rendered via vegetation facies county map | **`KFM-P25-FEAT-0005`** (operationally definitive map feature); `ML-K-067` |

> [!TIP]
> **COG + PMTiles distribution pattern** for LANDFIRE follows the parallel pattern established for Soils in `KFM-P24-PROG-0051` ("Soil mapunit polygons should publish as PMTiles and continuous soil properties as COGs, with provenance metadata, spec_hash, and release references"). The LANDFIRE EVT-derived per-county facies polygons → PMTiles; the underlying EVT raster → COG. Both carry `spec_hash` and signed derivative references per `ML-K-067`.

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 12. Catalog profiles

| Profile | Lane | Used by LANDFIRE? | Justification |
|---|---|---|---|
| **STAC** | `data/catalog/stac/` | **YES** | `KFM-P25-PROG-0010` records source URI, product version, raster/vector form — STAC Item shape; `C4-01` STAC `kfm:provenance` namespace; Collection-id `kfm-landfire-<product>` per `C4-02`. |
| **DCAT** | `data/catalog/dcat/` | **YES** | `C4-05` DCAT distribution applicable to LANDFIRE's public-domain US-federal endpoint distributions. |
| **PROV-O** | `data/catalog/prov/` | **YES** | `C5-08` lineage required + Atlas §24.2.1 receipt catalog; LANDFIRE-derived facies summaries (per `KFM-P25-PROG-0024`) carry full PROV-O lineage to source rasters; signed derivative references per `ML-K-067`. |
| **Domain projection** | `data/catalog/domain/{habitat,flora,fauna,hazards}/` | **YES** | Per `KFM-P25-FEAT-0005` (vegetation facies county map) + `KFM-P25-IDEA-0010` (county facies summaries); LANDFIRE products land in multiple receiving domains. |

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 13. Pre-admission checklist

The following items SHOULD be satisfied before any LANDFIRE product is admitted past `data/raw/`. These are the gates a green-field admission would pass through.

- [ ] **`SourceDescriptor` drafted** for the specific LANDFIRE product per `KFM-P25-PROG-0010` field surface: ecological system / USNVC classification, product version, raster/vector form, source URI, thematic role.
- [ ] **Class-map version pinned** — `product_version` field MUST capture the LANDFIRE class-map version per §8 (class semantics drift across versions).
- [ ] **Source role assigned** per Atlas §24.1.3: `observed` (EVT, EVC, EVH, LDist, historical disturbance), `modeled` (BPS, Fuels — FBFM13/40, FVT/FVH/FVC), or `aggregate` (KFM-derived per-county summaries).
- [ ] **USNVC crosswalk wired** per `KFM-P25-PROG-0025` — `nvc_code` metadata crosswalk validator (`tools/validators/usnvc_crosswalk_validator/` PROPOSED) preserves ecological system + USNVC group + ruderal/natural status + class labels + source version.
- [ ] **Native classification preserved** per `KFM-P2-IDEA-0028` — LANDFIRE-native class codes preserved alongside USNVC mapping; crosswalks attached as advisory.
- [ ] **Rights confirmation** recorded — US Federal public-domain assumption verified per product; non-standard restrictions surfaced.
- [ ] **Early-release flag** set for LDist 2025 per `KFM-P18-PROG-0032` — cadence and UI handling configured.
- [ ] **`SourceActivationDecision`** issued: `allowed | restricted | denied | needs-review`. Connector remains inactive until this exists per `C5-02`.
- [ ] **Anchoring strategy declared** — USNVC `nvc_code` (primary classification authority); LANDFIRE-native code (parallel); GNIS for locality (`C7-09`); product version + class-map version pinned.
- [ ] **Policy gates** — admit / restrict / deny rules per `C5-02` default-deny posture.
- [ ] **Receipt envelope** — admission emits `RawCaptureReceipt`; promotion emits `TransformReceipt`, `ValidationReport`, `EvidenceRef`, `AggregationReceipt` for derived county summaries per Atlas §24.2.1.
- [ ] **Distribution shape** per `ML-K-067` + `KFM-P24-PROG-0051`-parallel — COG for continuous rasters + PMTiles for vector facies derivatives.
- [ ] **Promotion gates** — schema valid, license compliant, provenance complete, spatial integrity verified, temporal consistency, USNVC crosswalk validated.
- [ ] **Rollback target** declared before any `PUBLISHED` transition.

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 14. Open verification items

| # | Item | Owner (PROPOSED) | Why it matters |
|---|---|---|---|
| **OPEN-LFP-01** (PATH CORRECTION) | Connector path corrected from v0.1's `connectors/lf/` (two-letter abbreviation) to v0.2's `connectors/landfire/` (full kebab-case at top level). Mounted-repo verification required. Same correction as family-README v0.2 OPEN-LF-01. | Pipeline owner | Connector-lane naming consistency. |
| **OPEN-LFP-02** (= OPEN-LF-02 = OPEN-DSC-14) | Should `landfire/` be ADR-ratified as a tenth §7.3 canonical family, nested under `connectors/usgs/landfire/`, or some other arrangement? Shared question with ISRIC and GAP. | Docs steward + ADR sponsor | Family-lane status. |
| **OPEN-LFP-03** | Confirm umbrella-vs-per-sub-product page model — this page is the LANDFIRE Vegetation and Fuels umbrella; per-sub-product pages PROPOSED at `./evt.md`, `./ldist.md`, `./fuels.md`, `./disturbance.md`. | Docs steward | Page-graph integrity. |
| **OPEN-LFP-04** | Confirm current LANDFIRE distribution endpoint URL(s) per product. | Source steward | Connector implementation. |
| **OPEN-LFP-05** | Confirm LANDFIRE per-product license terms (US Federal public-domain default; verify any non-standard restrictions). | Source steward | Rights gate per `C5-02`. |
| **OPEN-LFP-06** | Confirm current LDist 2025 release status and early-release-to-stable transition policy per `KFM-P18-PROG-0032`. | Source steward | Cadence determinism. |
| **OPEN-LFP-07** | Confirm USNVC `nvc_code` crosswalk completeness per `KFM-P25-PROG-0025` — every LANDFIRE EVT class anchored? Policy for unanchored classes? | Flora/Habitat domain steward | USNVC anchoring discipline. |
| **OPEN-LFP-08** | Confirm LANDFIRE-vs-CDL-vs-NLCD-vs-GAP advisory-crosswalk operational granularity per `KFM-P2-IDEA-0028` — pixel? polygon? county summary? Evidence Drawer surfacing? | Flora/Habitat domain steward + AI steward | Crosswalk discipline. |
| **OPEN-LFP-09** | Confirm per-county facies pipeline output validation per `KFM-P25-PROG-0024` — confidence metrics threshold + signed-derivative reference format. | Habitat domain steward | Aggregation discipline. |
| **OPEN-LFP-10** | Confirm vegetation facies county map render pattern per `KFM-P25-FEAT-0005` — PMTiles-only, COG-only, or hybrid? | MapLibre steward | Distribution architecture. |
| **OPEN-LFP-11** | Confirm GAP-and-LANDFIRE shared descriptor framing per `KFM-P25-PROG-0010` — does GAP get its own per-product page under LANDFIRE umbrella, its own family `gap/`, or remain shared-descriptor only? Same as family-README OPEN-LF-10. | Docs steward + biodiversity domain steward | Family scope. |
| **OPEN-LFP-12** | Confirm class-map version pinning mechanism per §8 — `product_version` semantics; cross-version join policy. | Habitat domain steward | Version determinism. |
| **OPEN-LFP-13** | Confirm BPS-as-`modeled` and Fuels-as-`modeled` source-role assignments per Atlas §24.1.3; anti-collapse enforcement at AI surfaces. | Flora/Hazards domain stewards + AI steward | Source-role anti-collapse. |
| **OPEN-LFP-14** | Confirm corpus card-ID stability for the eight LANDFIRE-specific cards: `KFM-P2-IDEA-0028`, `KFM-P18-PROG-0032`, `KFM-P25-PROG-0010`, `KFM-P25-IDEA-0010`, `KFM-P25-FEAT-0005`, `KFM-P25-PROG-0024`, `KFM-P25-PROG-0025`, `ML-K-067`. | Docs steward | Card stability. |
| **OPEN-DSC-03** | Namespace pin: `kfm:` vs `ks-kfm:` (shared lane-wide question). | Docs steward | Namespace identity. |

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 15. FAQ

<details>
<summary><strong>How does this page relate to <code>./README.md</code> (LANDFIRE family README)?</strong></summary>

This page is the **LANDFIRE Vegetation and Fuels umbrella per-product page**; [`./README.md`](./README.md) v0.2 is the **`landfire/` family-README**. The family-README sets the `landfire/` family-folder status (PROPOSED beyond §7.3 per OPEN-DSC-14), enumerates the per-product page roster, and orients readers to the family. This page sets institution-level LANDFIRE-program posture (rights, cadence floor, advisory-crosswalk discipline, distribution shape, USNVC integration) and serves as the umbrella for per-sub-product pages (`evt.md`, `ldist.md`, `fuels.md`, `disturbance.md`). The two layers coexist.

</details>

<details>
<summary><strong>Why are BPS and Fuels treated as <code>modeled</code> rather than <code>observed</code>?</strong></summary>

Per Atlas §24.1.3 source-role enum (CONFIRMED), `modeled` is the role for "model output presented as a surface with confidence" while `observed` is the role for direct observations. **BPS** (Biophysical Settings) is a modeled reconstruction of pre-European-settlement vegetation — not an observation of current conditions. **Fuels** products (FBFM13, FBFM40, FVT, FVH, FVC) are modeled abstractions of fuel behavior — not direct observations of fuel state. Treating either as `observed` violates Atlas §24.1.2 anti-collapse rule ("Modeled product labeled as observed → DENY"). The EVT, EVC, EVH rasters ARE `observed` (they represent observed vegetation type / cover / height); the LDist disturbance rasters ARE `observed` (observed disturbance events).

</details>

<details>
<summary><strong>What does "class-map version" mean and why is it first-class metadata?</strong></summary>

LANDFIRE updates its classification semantics across major versions. The same LANDFIRE-native class code (or USNVC `nvc_code` mapping) may have different meaning in EVT-2014 vs EVT-2020 vs EVT-2022. This is the subtitle of this page: "carrying a class-map version because class semantics drift." Per `KFM-P25-PROG-0010`, the descriptor records "product version"; per `KFM-P25-PROG-0025`, the USNVC crosswalk records "source version." Joining LANDFIRE records across major versions without surfacing the version pin is an anti-collapse risk and is not allowed without an explicit cross-version reconciliation receipt.

</details>

<details>
<summary><strong>Why are CDL, NLCD, and GAP shown as "advisory only" crosswalks rather than authoritative joins?</strong></summary>

Per `KFM-P2-IDEA-0028` (CONFIRMED, Pass 32): *"Classification crosswalks are inherently lossy; the corpus directs that crosswalks be advisory rather than authoritative."* When LANDFIRE EVT classifies a Riley County pixel as one vegetation type and USDA CDL classifies the same pixel as a different crop type, the disagreement is recorded — both native classifications are preserved, and the crosswalk attaches as advisory. KFM does not silently resolve the disagreement; the disagreement IS the data.

</details>

<details>
<summary><strong>How does LANDFIRE handle sensitive species or sensitive cultural sites?</strong></summary>

LANDFIRE doesn't — that's the point. LANDFIRE describes broad-scale vegetation and fuels at public spatial resolution; it does not contain species-level occurrence data or cultural-site geometry. Sensitive-species handling lives at the species-data sources (KBS NHI per [`../kansas/kbs.md`](../kansas/kbs.md) v0.2, KDWP SINC per [`../kansas/kdwp.md`](../kansas/kdwp.md) v0.2). Sensitive-cultural-site handling lives at KHRI per [`../kansas/khri.md`](../kansas/khri.md) v0.2 and KU NHM Anthropology per [`../kansas/ku-nhm.md`](../kansas/ku-nhm.md) v0.2. When a LANDFIRE analysis joins to sensitive partner data, the join inherits the partner's sensitivity — per `KFM-P13-PROG-0018` deterministic grid generalization applied to the sensitive component.

</details>

<details>
<summary><strong>What's the operational spine of LANDFIRE in KFM?</strong></summary>

EVT raster → USNVC crosswalk → per-county facies summary → vegetation facies county map. Four atlas cards anchor this pipeline: **`KFM-P25-IDEA-0010`** (EVT + USNVC supports county facies summaries), **`KFM-P25-PROG-0024`** (EVT pipeline computes per-county area by `nvc_code` + confidence + signed derivative refs — operationally definitive), **`KFM-P25-PROG-0025`** (USNVC `nvc_code` crosswalk metadata), **`KFM-P25-FEAT-0005`** (vegetation facies county map render). Plus **`ML-K-067`** (EVT raster → COG with signed derivative provenance). See §11 distribution shape table.

</details>

<details>
<summary><strong>Why is the connector path correction in v0.2 necessary?</strong></summary>

Because v0.1 placed the connector at `connectors/lf/` (two-letter top-level abbreviation, neither §7.3 family nor full kebab-case). v0.2 corrects to `connectors/landfire/` (full kebab-case family name at top level), consistent with other beyond-§7.3 families like ISRIC. Both placements are "beyond §7.3" until ADR-ratified per OPEN-DSC-14; the v0.2 correction picks the placement consistent with full-name kebab-case convention. Same correction applied at family-README level (`./README.md` v0.2 OPEN-LF-01). See OPEN-LFP-01.

</details>

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## 16. Related docs

> [!NOTE]
> Targets below reflect the v0.2 catalog reorganization (`docs/sources/catalog/<family>/<product>.md`, kebab-case slugs). Per-sub-product pages PROPOSED until verified in the mounted repo.

- [`./README.md`](./README.md) — `docs/sources/catalog/landfire/` family README v0.2 (this dossier's parent; lists this umbrella + per-sub-product pages; confirms `connectors/landfire/` as PROPOSED beyond §7.3 per OPEN-DSC-14)
- [`./evt.md`](./evt.md) — per-sub-product page: LANDFIRE Existing Vegetation Type (EVT) (PROPOSED)
- [`./ldist.md`](./ldist.md) — per-sub-product page: LANDFIRE LDist 2025 (Limited Disturbance) early-release (PROPOSED)
- [`./fuels.md`](./fuels.md) — per-sub-product page: LANDFIRE Fuels (FBFM13/40, FVT/FVH/FVC) (PROPOSED)
- [`./disturbance.md`](./disturbance.md) — per-sub-product page: LANDFIRE historical disturbance products (PROPOSED)
- [`../README.md`](../README.md) — `docs/sources/catalog/` index (TODO: create or verify)
- [`../isric/README.md`](../isric/README.md) — sibling beyond-§7.3 family README (parallel structural model, v0.2 in this conversation series)
- [`../usgs/README.md`](../usgs/README.md) — sibling §7.3 family README (USGS is LANDFIRE's primary host agency — potential nesting parent per OPEN-DSC-14)
- [`../nrcs/README.md`](../nrcs/README.md) — sibling §7.3 family README (soil substrate context)
- [`../kansas/README.md`](../kansas/README.md) — sibling §7.3 family README (Kansas-specific land-cover authorities — KBS NHI per `C7-10` complements LANDFIRE)
- [`../kansas/kbs.md`](../kansas/kbs.md) — sibling Kansas-first authority (NHI sensitive-natural-community context)
- [`../kansas/kdwp.md`](../kansas/kdwp.md) — sibling Kansas-first authority (SINC sensitive-species context — see §6 inherited-sensitivity scenarios)
- [`../IDENTITY.md`](../IDENTITY.md) — Collection-id and namespace conventions
- [`../PROFILES.md`](../PROFILES.md) — catalog-profile selection guidance
- [`../RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) — lane-wide rights/sensitivity matrix
- [`../OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) — lane-wide `OPEN-DSC-*` items
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
- [`../../../registers/DRIFT_REGISTER.md`](../../../registers/DRIFT_REGISTER.md) — drift filing
- [`../../../adr/ADR-0001-schema-home.md`](../../../adr/ADR-0001-schema-home.md) — schema-home convention
- Pass-10 Idea Index — **`C4-01`** STAC `kfm:provenance`; **`C4-02`** STAC Collection; **`C4-05`** DCAT distribution; **`C5-02`** default-deny promotion; **`C5-04`** spec-hash-match; **`C5-08`** lineage required; **`C3-01`** smart-sync HTTP validators; **`C7-09`** USGS GNIS
- Pass-23/32 Consolidated Atlas — **`KFM-P2-IDEA-0028`** USDA CDL + NLCD + LANDFIRE + GAP land cover (CONFIRMED, Pass 32); **`KFM-P18-PROG-0032`** LANDFIRE LDist source descriptor (active, Pass 32); **`KFM-P25-PROG-0010`** GAP/LANDFIRE source descriptor (active, Pass 32); **`KFM-P25-IDEA-0010`** LANDFIRE EVT facies mapping (active, Pass 32); **`KFM-P25-FEAT-0005`** vegetation facies county map (active, Pass 32); **`KFM-P25-PROG-0024`** LANDFIRE EVT county summary pipeline (active, Pass 32 — operationally definitive); **`KFM-P25-PROG-0025`** USNVC nvc_code metadata crosswalk (active, Pass 32); **`KFM-P20-IDEA-0002`** mask-aware HLS vegetation analytics (parallel pattern); **`KFM-P24-PROG-0051`** Soils PMTiles/COG artifact contract (parallel distribution model); **`KFM-P13-PROG-0018`** sensitive species grid generalization (applied weakly); Atlas §24.1.2 + §24.1.3 + §24.2.1 + §24.8
- Master MapLibre Components — **`ML-K-067`** LANDFIRE EVT raster → COG with signed derivative provenance

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## Appendix A — Descriptor field placeholders

<details>
<summary><strong>Illustrative SourceDescriptor skeleton for LANDFIRE Vegetation and Fuels</strong></summary>

> [!NOTE]
> The field surface below is **PROPOSED and illustrative**, drawn from `KFM-P25-PROG-0010` (GAP/LANDFIRE descriptor) + `KFM-P18-PROG-0032` (LDist descriptor) + Atlas §24.1.3 source-role enum + sibling v0.2 descriptor sketches. Authoritative shape lives in `schemas/contracts/v1/source/source_descriptor.schema.json` per ADR-0001 (NEEDS VERIFICATION in repo). Do not treat this appendix as a contract.

```yaml
# PROPOSED illustrative skeleton — NOT a contract.
id: TODO/source/landfire-evt-v<product_version>
source_id: landfire-evt                                       # per-product; one of: landfire-evt, landfire-bps, landfire-evc, landfire-evh, landfire-ldist-2025, landfire-fbfm40, etc.
source_family: landfire                                       # v0.2 catalog folder; PROPOSED beyond §7.3 per OPEN-DSC-14
source_family_enum: other                                     # closed enum per KFM-P3-PROG-0001
umbrella_family_ref: landfire-veg-fuels                       # this page's umbrella role
name: LANDFIRE EVT (Existing Vegetation Type)
publisher: LANDFIRE Program (USGS + USFS)
program: LANDFIRE Vegetation and Fuels
land_cover_cluster: KFM-P2-IDEA-0028                          # CONFIRMED — 4-source cluster: CDL ‖ NLCD ‖ LANDFIRE ‖ GAP
focus: fire-related land cover                                # per KFM-P2-IDEA-0028
operational_doctrine_card: KFM-P25-PROG-0024                  # CONFIRMED — operationally definitive LANDFIRE pipeline
descriptor_doctrine_card: KFM-P25-PROG-0010                   # CONFIRMED — descriptor shape per GAP/LANDFIRE
source_role: observed                                         # EVT is observed; BPS/Fuels would be modeled; per-county summaries would be aggregate
role_authority: LANDFIRE Program
ecological_system: <USNVC ecosystem name>                     # per KFM-P25-PROG-0010
usnvc_classification: <USNVC nvc_code>                        # per KFM-P25-PROG-0025
landfire_native_class: <LANDFIRE class code>                  # preserved per KFM-P2-IDEA-0028 native-classification rule
product_version: <LANDFIRE product version>                   # per KFM-P25-PROG-0010 — CRITICAL per §8 class-map version
class_map_version: <LANDFIRE class-map version>               # per §8 — class semantics drift
raster_vector_form: raster                                    # per KFM-P25-PROG-0010
source_uri: TODO                                              # per KFM-P25-PROG-0010 — NEEDS VERIFICATION (per OPEN-LFP-04)
thematic_role: vegetation-type                                # per KFM-P25-PROG-0010
early_release: false                                          # true for ldist-2025 per KFM-P18-PROG-0032
change_detection_role: false                                  # true for ldist-2025 per KFM-P18-PROG-0032
access:
  method: https-direct                                        # LANDFIRE program distribution endpoint
  endpoint_url: TODO                                          # NEEDS VERIFICATION (per OPEN-LFP-04)
  auth: none                                                  # public US-federal distribution
detection:
  signal: ETag / Last-Modified                                # per C3-01
  fallback: product-version polling
rights:
  default_posture: us-federal-public-domain                   # PROPOSED — NEEDS VERIFICATION (per OPEN-LFP-05)
  attribution_required: true                                  # LANDFIRE program citation
  posture_if_unknown: deny                                    # per C5-02
cadence:
  expected: per-major-version                                 # LANDFIRE historical cadence 2-3 years; NEEDS VERIFICATION
  early_release_window: special                               # for ldist-2025 per KFM-P18-PROG-0032
sensitivity:
  rubric_pass10: C6-01                                         # 0-5 rubric
  default_rank: 0                                              # public LANDFIRE products
  inherited_sensitivity_via_joins: true                        # joins with KBS/KDWP/KHRI inherit partner sensitivity
  default_redaction_profile: none                              # n/a at default rank 0
anchoring:
  classification_authority_primary: USNVC nvc_code            # per KFM-P25-PROG-0025
  classification_authority_native: LANDFIRE class code        # preserved per KFM-P2-IDEA-0028
  place_authority: USGS GNIS (C7-09)
  cluster_crosswalk_partners: [cdl, nlcd, gap]
  cluster_crosswalk_status: advisory-only                     # per KFM-P2-IDEA-0028 tension
usnvc_crosswalk:                                              # per KFM-P25-PROG-0025
  ecological_system: required
  usnvc_group: required
  ruderal_natural_status: required
  class_labels: required
  source_version: required
distribution:                                                 # per ML-K-067 + KFM-P24-PROG-0051 parallel
  continuous_raster: COG with signed derivative provenance
  vector_facies: PMTiles
  facies_pipeline: KFM-P25-PROG-0024                          # per-county area by nvc_code + confidence
  map_feature: KFM-P25-FEAT-0005                              # vegetation facies county map
public_release_class: public                                  # rank 0 default
care_review_required: false                                   # LANDFIRE doesn't carry CARE-relevant data
kfm:spec_hash: <computed at promotion: JCS+SHA-256>
status:
  activation_decision: needs-review
  fixtures_present: false
  validators_present: false
  policy_gates_present: false
```

</details>

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## Appendix B — Atlas idea-card lineage

For traceability into the KFM Idea Index spine, this brief draws on the following atlas cards.

<details>
<summary>Click to expand — idea-card lineage</summary>

| Stable ID | Title | Status (atlas) | Relevance to this brief |
|---|---|---|---|
| `KFM-P2-IDEA-0028` | USDA CDL, NLCD, LANDFIRE, GAP for land cover | **CONFIRMED, Pass 32** | **Central card for LANDFIRE.** Names LANDFIRE explicitly as one of four KFM land-cover authorities; "LANDFIRE is fire-focused"; native classification preserved; crosswalks advisory not authoritative. |
| `KFM-P25-PROG-0010` | GAP / LANDFIRE source descriptor | active, Pass 32 | **Descriptor shape card.** Records ecological system / USNVC classification, product version, raster/vector form, source URI, thematic role. |
| `KFM-P25-PROG-0024` | LANDFIRE EVT county summary pipeline | active, Pass 32 | **Operationally definitive LANDFIRE pipeline card.** Per-county area by `nvc_code` + confidence metrics + signed derivative references. |
| `KFM-P25-PROG-0025` | USNVC `nvc_code` metadata crosswalk | active, Pass 32 | **USNVC integration card.** Crosswalk preserves ecological system + USNVC group + ruderal/natural status + class labels + source version. |
| `KFM-P25-IDEA-0010` | LANDFIRE EVT facies mapping | active, Pass 32 | **EVT + USNVC framing card.** LANDFIRE EVT + USNVC hierarchy supports county facies summaries, confidence metrics, signed COG/MVT derivatives. |
| `KFM-P25-FEAT-0005` | Vegetation facies county map | active, Pass 32 | **Map feature card.** Renders LANDFIRE/USNVC per-county facies summaries + confidence from signed derivatives. |
| `KFM-P18-PROG-0032` | LANDFIRE LDist source descriptor | active, Pass 32 | **LDist 2025 early-release card.** Source descriptor with early-release status, cadence, rights, change-detection role. |
| `ML-K-067` | LANDFIRE EVT raster → COG | (Master MapLibre — EXPANDED) | **Distribution shape card.** EVT rasters convert to COGs with signed derivative provenance. |
| `KFM-P20-IDEA-0002` | Mask-aware HLS vegetation analytics | active, Pass 32 | **Parallel evidence pattern.** Bounded analytical claims with explicit cloud / aerosol / fire-screening evidence — applies by parallel to LANDFIRE-derived vegetation analytics. |
| `KFM-P24-PROG-0051` | Soils PMTiles + COG artifact contract | active, Pass 32 | **Parallel distribution pattern.** Polygons → PMTiles, continuous properties → COGs, with provenance metadata, spec_hash, release references. Applied to LANDFIRE per-county facies (PMTiles) + EVT raster (COG). |
| `KFM-P13-PROG-0018` | Sensitive species grid generalization policy | active, Pass 32, EXPANDED | **Applied weakly to LANDFIRE direct.** Applied by inheritance when LANDFIRE joins to sensitive partner data (KBS NHI, KDWP SINC). |
| `KFM-P19-IDEA-0005` | KDWP listing canonical regulatory context | active, Pass 32 | **Referenced for contrast.** LANDFIRE is `observed | modeled`, not `regulatory`. |
| `C4-01` | STAC `kfm:provenance` namespace | CONFIRMED (Pass-10) | Provenance block shape for LANDFIRE STAC Items. |
| `C4-02` | STAC Collection (`kfm-<org>-<product>`) | CONFIRMED (Pass-10) | Collection-id convention: `kfm-landfire-<product>`. |
| `C4-05` | DCAT distribution | CONFIRMED (Pass-10) | Applicable to LANDFIRE distributions. |
| `C5-02` | Default-deny promotion | CONFIRMED (Pass-10) | Anchors deny-by-default rights posture. |
| `C5-04` | Spec-hash-match gate | CONFIRMED (Pass-10) | Promotion gate. |
| `C5-08` | Lineage required | CONFIRMED (Pass-10) | OpenLineage trail back to receipts. |
| `C3-01` | Smart-sync HTTP validators | CONFIRMED (Pass-10) | ETag + Last-Modified watcher mechanism. |
| `C7-09` | USGS GNIS | CONFIRMED (Pass-10) | Place anchor for county rollups. |
| `C6-01` | Sensitivity rubric 0–5 | CONFIRMED (Pass-10) | LANDFIRE direct material sits at rank 0; inheritance via joins. |
| Atlas §24.1.2 | Anti-collapse failure modes | CONFIRMED (Pass-23/32) | "Modeled product labeled as observed → DENY"; "Aggregate cited as a per-place truth → DENY at trust membrane." Operationally critical for BPS / Fuels vs EVT and for per-county facies summaries vs pixel-level claims. |
| Atlas §24.1.3 | Source-role enum (Master Source-Role Anti-Collapse Register) | CONFIRMED (Pass-23/32) | `observed | regulatory | modeled | aggregate | administrative | candidate | synthetic`; LANDFIRE primary roles `observed` (EVT, EVC, EVH, LDist, disturbance) and `modeled` (BPS, Fuels). |
| Atlas §24.2.1 | Master receipt catalog | CONFIRMED (Pass-23/32) | `SourceDescriptor`, `RawCaptureReceipt`, `TransformReceipt`, `ValidationReport`, `AggregationReceipt`. |
| Atlas §24.8 | Time discipline | CONFIRMED (Pass-23/32) | source / observed / valid / retrieval / release / correction times preserved separately. LDist 2025 early-release adds release-time complexity. |
| **Directory Rules v1.2 §7.3** | Nine canonical connector families | CONFIRMED at commit `b6a27916...` | LANDFIRE not in nine — OPEN-DSC-14 ADR pending. |

</details>

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

## Appendix C — Change log

| Date | Author | Change | Reviewed by |
|---|---|---|---|
| 2026-05-21 | `<docs-steward — TODO>` | Initial v0.1 PROPOSED scaffold: title, overview placeholder, source-authority pointer, catalog-profiles table with `Yes / No (NEEDS VERIFICATION)` cells, collection identity, Pass-10 C4-01 provenance fields, temporal/geometry/rights placeholders, validation pointers, related-contracts/connectors/pipelines pointers, examples pointer, open-questions list (3 generic items), last-reviewed footer. Path: `docs/sources/catalog/landfire/landfire.md` (already in v0.2 catalog convention). Connector path `connectors/lf/` — INCORRECT (two-letter abbreviation). | `<TODO — initial scaffold only>` |
| 2026-05-21 | `<docs-steward — TODO>` | **v0.2 revision (same-day promotion).** Promotes v0.1 PROPOSED scaffold to full umbrella per-product page brief consistent with sibling v0.2 product pages. **Structural reframings:** (a) **Umbrella-vs-per-sub-product model** (NEW in v0.2) — frames this page as the LANDFIRE Vegetation and Fuels UMBRELLA per-product page parented under `./README.md` v0.2 (landfire/ family README), with per-sub-product pages PROPOSED at `./evt.md`, `./ldist.md`, `./fuels.md`, `./disturbance.md`. Per-product `SourceDescriptor` requirement per `KFM-P25-PROG-0010`. Mirrors the umbrella patterns of KBS / KSHS / KSU R&E in the kansas/ family. Surfaced as IMPORTANT callout in §1 and OPEN-LFP-03. (b) **Connector path correction OPEN-LFP-01** — v0.1's `connectors/lf/` (two-letter abbreviation, neither §7.3 family nor full kebab-case) corrected to `connectors/landfire/` (full kebab-case family name at top level). Both placements are "beyond §7.3" until ADR-ratified per OPEN-DSC-14. Same correction as family-README v0.2 OPEN-LF-01. Surfaced as IMPORTANT callout in §1. (c) **§7.3 status clarification** — explicit acknowledgment that `connectors/landfire/` is NOT in the nine-family canonical list (CONFIRMED at commit `b6a27916...`: `usgs/`, `fema/`, `noaa/`, `nrcs/`, `kansas/`, `gbif/`, `inaturalist/`, `census/`, `local_upload/`). Surfaced via family-status badge and §1 IMPORTANT callout. **Substantive doctrinal additions:** (d) explicit citation to **`KFM-P2-IDEA-0028`** (CONFIRMED Pass 32 — central card naming LANDFIRE as one of four KFM land-cover authorities; "LANDFIRE is fire-focused"; native classification preserved; crosswalks advisory) — central card; v0.1 did not cite. (e) explicit citation to **`KFM-P25-PROG-0010`** (active Pass 32 — GAP/LANDFIRE descriptor; ecological system / USNVC classification + product version + raster/vector form + source URI + thematic role) — descriptor shape card; v0.1 did not cite. (f) explicit citation to **`KFM-P25-PROG-0024`** (active Pass 32 — LANDFIRE EVT county summary pipeline; per-county area by `nvc_code` + confidence + signed derivative refs) — operationally definitive card; v0.1 did not cite. (g) explicit citation to **`KFM-P25-PROG-0025`** (active Pass 32 — USNVC `nvc_code` metadata crosswalk; ecological system + USNVC group + ruderal/natural status + class labels + source version); v0.1 did not cite. (h) explicit citation to **`KFM-P25-IDEA-0010`** (active Pass 32 — LANDFIRE EVT + USNVC hierarchy for county facies summaries); v0.1 did not cite. (i) explicit citation to **`KFM-P25-FEAT-0005`** (active Pass 32 — vegetation facies county map render); v0.1 did not cite. (j) explicit citation to **`KFM-P18-PROG-0032`** (active Pass 32 — LDist 2025 early-release source descriptor); v0.1 did not cite. (k) explicit citation to **`ML-K-067`** (Master MapLibre — EVT raster → COG with signed derivative provenance); v0.1 did not cite. (l) Parallel-pattern citations to `KFM-P20-IDEA-0002` (mask-aware HLS vegetation analytics), `KFM-P24-PROG-0051` (Soils PMTiles + COG artifact contract — distribution pattern), `KFM-P13-PROG-0018` (deterministic grid generalization — applied weakly); `KFM-P19-IDEA-0005` (referenced for contrast). (m) Atlas §24.1.2 anti-collapse + §24.1.3 source-role enum + §24.2.1 receipt catalog + §24.8 time discipline citations throughout. (n) Land-cover cluster framing: LANDFIRE positioned alongside CDL (crop-focused), NLCD (broad multi-year), GAP (biodiversity-focused) per `KFM-P2-IDEA-0028`; advisory-only crosswalks explicit. (o) Source-role discipline elevated: EVT/EVC/EVH/LDist/disturbance = `observed`; BPS/Fuels = `modeled`; per-county facies summaries = `aggregate`. Two IMPORTANT callouts in §5 distinguishing these. (p) Distribution shape: COG (continuous rasters) + PMTiles (vector facies) per `ML-K-067` + `KFM-P24-PROG-0051`-parallel. (q) USNVC integration: `nvc_code` as first-class identifier preserved alongside LANDFIRE-native code per `KFM-P25-PROG-0025`. (r) Class-map-version discipline: §8 IMPORTANT callout on class-semantics drift; `product_version` field per `KFM-P25-PROG-0010` as first-class metadata. (s) Early-release-product handling: §6 WARNING callout citing `KFM-P18-PROG-0032`. (t) Inherited-sensitivity-via-joins discipline: §6 row 4; §15 FAQ Q5 on LANDFIRE joins with KBS NHI / KDWP SINC / KHRI / KU NHM; reference to sibling v0.2 pages. (u) Added §1 NOTE callout: v0.1 → v0.2 promotion. (v) Added §1 IMPORTANT callout: connector path correction OPEN-LFP-01. (w) Added §1 IMPORTANT callout: umbrella-vs-per-sub-product model. (x) Added §2 status table (13 rows with explicit corpus citations). (y) Added §3 repo-fit table (12 rows including USNVC crosswalk schema + validator paths). (z) Added §4 inputs accepted (six product classes with per-product source-role assignment + sibling page links). (aa) Added §5 source-roles table (5 rows) + 4 callouts (CAUTION role-purity, IMPORTANT BPS-is-modeled, IMPORTANT aggregate-not-observed, NOTE not-authority-not-regulatory). (bb) Added §6 sensitivity table (4 rows) + 3 callouts (TIP P13 applies weakly, WARNING early-release handling, TIP T0-T4-vs-0-5). (cc) Built §7 Mermaid lifecycle diagram with three subgraphs (LANDFIRE program, KFM land-cover cluster, KFM governance lanes) showing observed-vs-modeled-vs-aggregate distinctions + advisory-only crosswalks + USNVC crosswalk node + EVT pipeline + LDist early-release styling. (dd) Built §8 cadence table (6 rows) + IMPORTANT callout on class-map-version-as-first-class-metadata. (ee) Built §9 rights table (10 rows) + CAUTION callout on unknown-rights-fail-closed per `C5-02`. (ff) Built §10 authority anchoring table (7 rows) + NOTE callout on USNVC-is-authority-LANDFIRE-is-issuing-institution-position. (gg) Built §11 distribution shape table (7 rows) + TIP callout on COG+PMTiles-parallel-to-Soils. (hh) Built §12 catalog profiles table (4 rows, all YES with corpus justification). (ii) Built §13 pre-admission checklist (14 items). (jj) Built §14 open-verification register (15 items OPEN-LFP-01 through OPEN-LFP-14 + OPEN-DSC-03). (kk) Built §15 FAQ (7 Q&A entries: umbrella relationship, BPS-Fuels-modeled rationale, class-map-version semantics, advisory-crosswalk rationale, sensitive-data handling, operational spine, connector path correction). (ll) Built §16 related-docs (5 per-sub-product pages + 5 sibling family READMEs + supporting docs + corpus-card reference group). (mm) Built Appendix A descriptor sketch (KFM-P25-PROG-0010 field surface + KFM-P18-PROG-0032 early-release extensions + USNVC crosswalk block + distribution block). (nn) Built Appendix B atlas idea-card lineage (25 cards). (oo) Built Appendix C change log (this entry). (pp) Updated meta block to v0.2 with full related-docs list (33 entries) and 5-paragraph notes block. (qq) Updated badges: added doc-version, family-status, umbrella-of, land-cover-cluster, focus, interagency, source-role, USNVC, distribution, rights, last-updated. | `<flora-domain-steward / habitat-domain-steward / hazards-domain-steward / fauna-domain-steward — TODO>` |

[Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)

---

<sub>**Last updated:** 2026-05-21 · **Status:** `draft` (v0.2) · **Brief class:** umbrella per-product page · **Parent family-README:** [`./README.md`](./README.md) v0.2 · **Owners:** _TODO — docs steward + source steward + habitat/flora/fauna/hazards domain stewards_</sub>

<sub>**Family lane:** `connectors/landfire/` — PROPOSED beyond §7.3 per OPEN-LFP-02 / OPEN-DSC-14 (canonical nine: `usgs/`, `fema/`, `noaa/`, `nrcs/`, `kansas/`, `gbif/`, `inaturalist/`, `census/`, `local_upload/`). v0.1's `connectors/lf/` corrected to v0.2's `connectors/landfire/` per OPEN-LFP-01.</sub>

<sub>**Authority of this brief:** umbrella per-product page; cites authority, does not own it. The per-LANDFIRE-product `SourceDescriptor`s are the source of truth for rights, sensitivity, cadence, citation, version pinning.</sub>

<sub>**Land-cover cluster:** LANDFIRE (fire-focused) ‖ USDA CDL (crop-focused annual) ‖ USGS NLCD (broad multi-year) ‖ USGS GAP (biodiversity-focused) per `KFM-P2-IDEA-0028`. Native classification preserved; crosswalks advisory.</sub>

<sub>**Source-role discipline:** EVT/EVC/EVH/LDist/disturbance = `observed`; BPS/Fuels = `modeled`; per-county facies summaries = `aggregate`. Anti-collapse enforcement per Atlas §24.1.2.</sub>

<sub>**Operational spine:** EVT raster → USNVC crosswalk → per-county facies summary → vegetation facies county map. `KFM-P25-IDEA-0010` + `KFM-P25-PROG-0024` (operationally definitive) + `KFM-P25-PROG-0025` + `KFM-P25-FEAT-0005` + `ML-K-067`.</sub>

<sub>**Class-map version:** first-class metadata per `KFM-P25-PROG-0010`; class semantics drift across LANDFIRE major versions.</sub>

<sub>**Related doctrine:** [`../../../doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) · [`../../../doctrine/lifecycle-law.md`](../../../doctrine/lifecycle-law.md) · [`../../../doctrine/truth-posture.md`](../../../doctrine/truth-posture.md) · [`../../../registers/AUTHORITY_LADDER.md`](../../../registers/AUTHORITY_LADDER.md) · [`../../../registers/DRIFT_REGISTER.md`](../../../registers/DRIFT_REGISTER.md)</sub>

<sub>[↑ Back to top](#landfire-vegetation-and-fuels--source-catalog-entry)</sub>
