---
title: "KFM STAC Items Output Directory"
path: "data/stac/items/README.md"
version: "v1.0.0"
last_updated: "2026-01-11"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:data:stac:items:readme:v1.0.0"
semantic_document_id: "kfm-data-stac-items-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:stac:items:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

<div align="center">

# 📦 STAC Items — `data/stac/items/`

![STAC](https://img.shields.io/badge/STAC-Items%20(Feature%20%2B%20Assets)-1f6feb)
![Boundary](https://img.shields.io/badge/Boundary%20Artifacts-STAC%20%2B%20DCAT%20%2B%20PROV-8a8f98)
![Determinism](https://img.shields.io/badge/ETL-deterministic%20%26%20idempotent-0b7285)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-6f42c1)
![Security](https://img.shields.io/badge/Security-classification%20propagation-red)

**STAC Items** are the **asset/granule-level** records that make KFM data:
🗺️ mappable • ⏱️ time-filterable • 🧾 cite-able • 🔎 discoverable

In KFM, Items are part of the **published boundary**: **STAC + DCAT + PROV** must exist **before** Graph/API/UI/Story usage. :contentReference[oaicite:1]{index=1}

</div>

---

## 🚀 Quick links

- 🛰️ STAC root → [`../README.md`](../README.md)
- 🧺 Collections (layer/dataset level) → [`../collections/`](../collections/)
- 📦 Items (granule/asset level) → `./` *(you are here)*
- 🗂️ DCAT (dataset discovery) → [`../../catalog/dcat/`](../../catalog/dcat/)
- 🧬 PROV (lineage bundles) → [`../../prov/`](../../prov/)
- 📦 Processed outputs (actual files) → [`../../processed/`](../../processed/)

> [!IMPORTANT]
> **STAC Items must point to the actual assets** (files or stable endpoints), and carry attribution/license context. :contentReference[oaicite:2]{index=2}

---

<details>
<summary><strong>📌 Table of contents</strong></summary>

- [🎯 What this folder is (and is not)](#-what-this-folder-is-and-is-not)
- [🗂️ Directory layout](#️-directory-layout)
- [🧠 What a STAC Item means in KFM](#-what-a-stac-item-means-in-kfm)
- [🏷️ IDs and naming conventions](#️-ids-and-naming-conventions)
- [🧩 Required fields + KFM profile overlay](#-required-fields--kfm-profile-overlay)
- [📎 Assets: formats, roles, and packaging patterns](#-assets-formats-roles-and-packaging-patterns)
- [🔗 Cross-links: STAC ↔ DCAT ↔ PROV ↔ Graph ↔ API](#-cross-links-stac--dcat--prov--graph--api)
- [🔐 Governance & sensitive data rules](#-governance--sensitive-data-rules)
- [✅ Add / update an Item checklist](#-add--update-an-item-checklist)
- [🧪 Validation & QA gates](#-validation--qa-gates)
- [🧷 Templates](#-templates)
- [🛰️ Special case: streaming / real-time Items](#️-special-case-streaming--real-time-items)
- [📚 Reference shelf](#-reference-shelf)
- [🕰️ Version history](#️-version-history)

</details>

---

## 🎯 What this folder is (and is not)

### ✅ `data/stac/items/` **IS**
- A canonical, machine-validated home for **STAC Item JSON** (“Feature” objects).
- Where KFM defines **time + footprint + assets** for a specific data “slice” (tile, AOI, timestamp, run output, etc.).
- A critical part of the KFM “published boundary” used downstream (Graph → API → UI → Story Nodes → Focus Mode). 

### ❌ `data/stac/items/` is **NOT**
- A storage location for the actual outputs (those live in `data/processed/` as GeoJSON/COGs/Parquet/etc.). :contentReference[oaicite:4]{index=4}
- A replacement for **DCAT** (dataset discovery across dataset types). :contentReference[oaicite:5]{index=5}
- A replacement for **PROV** (lineage + run traceability). :contentReference[oaicite:6]{index=6}

> [!TIP]
> If you’re holding a **file people will download or render**, it’s not an Item — it’s an **asset**.  
> The Item is the **index card** that points to that asset 📇➡️📦

---

## 🗂️ Directory layout

KFM keeps Items grouped by Collection:

```text
data/stac/
├─ 📄 README.md                         # 📘 STAC layout overview + root link conventions + validation pointers
├─ 🗂️ collections/
│  ├─ 📄 README.md                      # 📘 Collection conventions (ids, extent/license/providers, link expectations)
│  └─ 🧾 <collection-id>.json           # One STAC Collection per dataset/product (dataset-level metadata)
└─ 🧷 items/
   ├─ 📄 README.md                      # 👈 you are here 📌 Item naming, required fields, and how items link to assets
   └─ 🗂️ <collection-id>/              # Items grouped under their parent collection id
      ├─ 🧾 <item-id>.json              # STAC Item snapshot (assets/hrefs/mediaTypes/roles + datetime or start/end)
      ├─ 🧾 <item-id>.json              # Another snapshot (different time/run/version; keep ids unique)
      └─ ➕ …                            # Additional items (append-only; never edit past snapshots without a new run)
```

> [!NOTE]
> This layout keeps **joins cheap**:
> - `collection-id` is the stable “layer/dataset family”
> - `item-id` is the stable “granule/slice/instance”

---

## 🧠 What a STAC Item means in KFM

A STAC Item answers:

- **What is this artifact instance?** (tile? county snapshot? a year/month slice?)
- **Where/when is it?** (geometry/bbox + datetime or interval)
- **Where are the files?** (`assets.*.href`)
- **Who/what produced it?** (provenance hooks + attribution/license)

KFM’s map UI is designed to hide/show layers by time and browse layers interactively; the timeline relies on item temporal fields being correct. :contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}

> [!IMPORTANT]
> Treat temporal + spatial metadata as **user-facing** — because it is. If the bbox or datetime is wrong, the story is wrong.

---

## 🏷️ IDs and naming conventions

### The “stable ID” rule ✅
KFM expects **stable identifiers across artifacts** so Graph/API/UI can join data without brittle heuristics. 

Recommended identifier layers:

| Concept | Example | Used for |
|---|---|---|
| `dataset_id` (KFM global) | `kfm.ks.hydrology.flood_extent.1993.v1` | DCAT join key + cross-system references |
| `collection-id` (STAC) | `ks-hydrology-flood-extent-1993-v1` | `data/stac/collections/<id>.json` |
| `item-id` (STAC) | `ks-hydrology-flood-extent-1993-v1__1993-07-15` | `data/stac/items/<collection-id>/<item-id>.json` |

KFM naming guidance for dataset IDs emphasizes *state/region + theme + time* and explicit versioning. 

### File naming convention (recommended)
Keep “file = id”:

```text
data/stac/items/<collection-id>/<item-id>.json
```

### Item ID patterns (pick one per collection)
Common (and diff-friendly) patterns:

- **Single timestamp slice**:  
  `<collection-id>__YYYY-MM-DD`  
  Example: `ks-ndvi-landsat8-v1__2025-06-01`

- **Monthly**:  
  `<collection-id>__YYYY-MM`  
  Example: `ks-precip-prism-v1__2024-09`

- **Tile/AOI + time**:  
  `<collection-id>__<tile-or-aoi>__YYYY-MM-DD`  
  Example: `ks-geology-surficial-v1__tile-14-22__2026-01-01`

- **Run-scoped artifact** (when needed):  
  `<collection-id>__run-<run_id>`  
  Example: `ks-ocr-corpus-v1__run-20260111-021530Z`

> [!CAUTION]
> Avoid random IDs for Items unless you’re modeling truly unique events. Stable IDs are how KFM stays joinable and “boringly reliable.” 

---

## 🧩 Required fields + KFM profile overlay

KFM profiles extend base standards and CI validates against them. :contentReference[oaicite:12]{index=12}

### Minimum STAC Item fields (practical baseline)
An Item should include:

- `stac_version`
- `type: "Feature"`
- `id`
- `collection` (must match Collection `id`)
- `geometry` + `bbox` (WGS84 lon/lat)
- `properties.datetime` **or** `start_datetime` + `end_datetime`
- `assets` (each with `href` + `type` + `roles`)
- `links` (at minimum: `self` + `collection`)

KFM’s documentation explicitly calls out that STAC Items describe dataset metadata like spatial extent, temporal range, source links, and license info. :contentReference[oaicite:13]{index=13}

### KFM-specific overlay (recommended fields)
Depending on the profile/schema, Items may include namespaced keys (example: `kfm:*`) for:

- `kfm:dataset_id` (global join key)
- `kfm:dcat_ref` (DCAT dataset id/path)
- `kfm:prov_ref` or `kfm:prov_activity_id` (lineage hook)
- `kfm:run_id` / `kfm:commit_sha` (reproducibility)
- `kfm:classification` / `kfm:sensitivity` (governance)
- `kfm:quality` / `kfm:uncertainty` (especially for AI/derived layers)

> [!NOTE]
> If your profile doesn’t yet define these, **add them to the profile + schema** instead of inventing one-off keys. :contentReference[oaicite:14]{index=14}

---

## 📎 Assets: formats, roles, and packaging patterns

### “Items point to assets” golden rule 🥇
Items must point to real assets in `data/processed/**` (or stable external storage). :contentReference[oaicite:15]{index=15}

KFM processed outputs commonly include:
- GeoJSON (vector layers)
- Cloud-Optimized GeoTIFF (raster layers)
- Parquet (large tabular data) :contentReference[oaicite:16]{index=16}

### Recommended packaging patterns
KFM’s roadmap explicitly favors **dual-format packaging** when it improves UX + analytics: e.g., **GeoParquet** (analysis) + **PMTiles** (fast visualization), with STAC/DCAT records registering both. :contentReference[oaicite:17]{index=17}

#### Pattern A — Analysis-grade + Web-grade side-by-side
Example asset set inside one Item:

- `assets.data` → GeoParquet (analytics)
- `assets.tiles` → PMTiles (MapLibre/Cesium-friendly)
- `assets.thumbnail` → PNG/JPG preview
- `assets.metadata` → processing report / schema / data dictionary

> [!TIP]
> This is how you avoid “either fast OR correct” false choices: publish both, clearly labeled. :contentReference[oaicite:18]{index=18}

### Asset roles (recommended)
Use STAC `roles` consistently:

- `data` — primary payload
- `overview` — simplified / downsampled variant
- `thumbnail` — small preview
- `metadata` — QA report, schema, data dictionary
- `source` — upstream reference (when allowed)

---

## 🔗 Cross-links: STAC ↔ DCAT ↔ PROV ↔ Graph ↔ API

KFM enforces cross-references so catalogs, graph, and narratives remain in sync. :contentReference[oaicite:19]{index=19}

### Cross-link rules (KFM)
- **STAC Items → Data**: Items must point to the actual assets (or stable endpoints), with attribution/license info. :contentReference[oaicite:20]{index=20}
- **DCAT → STAC/Distribution**: DCAT provides the “dataset landing” record and links to STAC and/or downloads. :contentReference[oaicite:21]{index=21}
- **PROV end-to-end**: PROV must link raw → work → processed and record run/config identifiers. :contentReference[oaicite:22]{index=22}
- **Graph references catalogs**: Neo4j stores references/IDs, not bulky payloads. :contentReference[oaicite:23]{index=23}

> [!IMPORTANT]
> UI never queries Neo4j directly; graph access is mediated via API contracts. 

### “Published boundary” gate ✅
Nothing should become user-facing (Graph/UI/Story/Focus) until:
- STAC Item(s) exist
- DCAT entry exists
- PROV bundle exists :contentReference[oaicite:25]{index=25}

---

## 🔐 Governance & sensitive data rules

KFM is building FAIR/CARE and sovereignty protections into tooling and validation—especially for sensitive locations or person-adjacent data. :contentReference[oaicite:26]{index=26}

### Non-negotiables
- **Classification propagation:** no output artifact can be less restricted than its inputs. 
- **No sensitive location inference:** do not publish precise coordinates for protected places unless policy allows; generalize/withhold as required. :contentReference[oaicite:28]{index=28}
- **Policy gate expectation:** governance rules (including redaction of sensitive coordinates) are intended to be enforced via machine-checkable policy packs in CI. :contentReference[oaicite:29]{index=29}

> [!CAUTION]
> A STAC Item is “metadata”… but metadata can still leak. Treat it as publishable surface area.

---

## ✅ Add / update an Item checklist

### 1) Confirm the asset exists
- [ ] The real file(s) are in `data/processed/**` (or stable external storage). :contentReference[oaicite:30]{index=30}

### 2) Create/Update the Item JSON
- [ ] `data/stac/items/<collection-id>/<item-id>.json`
- [ ] `collection` matches the parent Collection `id`
- [ ] `geometry`/`bbox` is WGS84 (lon/lat) and valid
- [ ] time fields are correct (`datetime` or `start/end`)
- [ ] `assets.*.href` resolves and `type` is accurate
- [ ] license/attribution context is present (directly or via Collection/provider fields) :contentReference[oaicite:31]{index=31}

### 3) Update sibling boundary artifacts
- [ ] DCAT dataset entry exists/updated (`data/catalog/dcat/…`) :contentReference[oaicite:32]{index=32}
- [ ] PROV bundle exists/updated (`data/prov/…`) with run/config identity :contentReference[oaicite:33]{index=33}

### 4) Downstream only after the gate
- [ ] Graph references STAC/DCAT/PROV IDs (no payload duplication) :contentReference[oaicite:34]{index=34}
- [ ] UI consumes through API boundary (no direct graph reads) 

---

## 🧪 Validation & QA gates

### Local sanity checks
```bash
python -m json.tool data/stac/items/<collection-id>/<item-id>.json > /dev/null
```

### STAC validation (recommended)
If `pystac` is available:

```bash
pystac validate data/stac/items/<collection-id>/<item-id>.json
```

### Catalog QA gate (KFM standard)
KFM’s CI is expected to run a Catalog QA tool to catch missing fields / broken links before merge. :contentReference[oaicite:36]{index=36}

```bash
# Example location (per KFM docs):
python tools/validation/catalog_qa/run_catalog_qa.py --root data/ --fail-on-warn
```

> [!TIP]
> Think “metadata is code”: if validation fails, treat it as a contract violation (not a style nit). :contentReference[oaicite:37]{index=37}

---

## 🧷 Templates

<details>
<summary><strong>📄 Minimal STAC Item skeleton (KFM-friendly)</strong></summary>

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "<item-id>",
  "collection": "<collection-id>",

  "geometry": { "type": "Polygon", "coordinates": [] },
  "bbox": [-102.051, 36.993, -94.588, 40.003],

  "properties": {
    "datetime": "2026-01-01T00:00:00Z"
  },

  "assets": {
    "data": {
      "href": "../../processed/<domain>/<dataset>/<version>/artifact.parquet",
      "type": "application/x-parquet",
      "roles": ["data"],
      "title": "Primary data payload"
    },
    "thumbnail": {
      "href": "../../processed/<domain>/<dataset>/<version>/preview.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  },

  "links": [
    {
      "rel": "self",
      "href": "./<item-id>.json",
      "type": "application/json"
    },
    {
      "rel": "collection",
      "href": "../../collections/<collection-id>.json",
      "type": "application/json"
    }
  ],

  "kfm:dataset_id": "kfm.ks.<domain>.<theme>.<time>.v1",
  "kfm:dcat_ref": "../../catalog/dcat/<dataset-id>.jsonld",
  "kfm:prov_ref": "../../prov/<run-id>/prov.jsonld",
  "kfm:classification": "open",
  "kfm:sensitivity": "public"
}
```

</details>

> [!NOTE]
> Use `kfm:*` keys only if/when the KFM STAC profile + schema allow them. :contentReference[oaicite:38]{index=38}

---

## 🛰️ Special case: streaming / real-time Items

KFM’s roadmap includes “Watcher” patterns that ingest real-time feeds and emit STAC Items per observation (e.g., GTFS-RT transit vehicles), with transit-specific fields and timestamps. :contentReference[oaicite:39]{index=39}

### Guidance for event/observation Items
- Prefer **append-only Items** (immutable observations)
- Use precise timestamps (`properties.datetime`)
- Keep geometry as a point (or small bbox) if appropriate
- Put *feed metadata* in properties (route, vehicle_id, source, retrieval time)
- Link PROV to ingestion/retrieval activity (so audit is possible)

> [!IMPORTANT]
> Even streaming data still obeys the boundary rule: STAC + DCAT + PROV, with governance checks. :contentReference[oaicite:40]{index=40}:contentReference[oaicite:41]{index=41}

---

## 📚 Reference shelf

### Core KFM docs (normative-ish)
- `MARKDOWN_GUIDE_v13.md.gdoc` (STAC/DCAT/PROV alignment + invariants) :contentReference[oaicite:42]{index=42}
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx` (data layout, catalog QA gate, formats, UI timeline behavior) :contentReference[oaicite:43]{index=43}:contentReference[oaicite:44]{index=44}
- `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx` (future item patterns: streaming feeds, tiling formats, policy gate direction) :contentReference[oaicite:45]{index=45}:contentReference[oaicite:46]{index=46}

### Project library (supporting, non-normative 🧠)
- GIS + cartography: `python-geospatial-analysis-cookbook.pdf`, `making-maps-a-visual-guide-to-map-design-for-gis.pdf`, `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- Remote sensing: `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- Web viz: `responsive-web-design-with-html5-and-css3.pdf`, `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- Repro/science rigor: `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`, `Understanding Statistics & Experimental Design.pdf`
- Systems & scale: `Scalable Data Management for Future Hardware.pdf`, `Data Spaces.pdf`
- Ethics/policy: `Introduction to Digital Humanism.pdf`, `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- Defensive security reference only: `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`, `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

---

## 🕰️ Version history

| Version | Date | Summary |
|---|---|---|
| v1.0.0 | 2026-01-11 | Initial `data/stac/items/` contract: layout, IDs, cross-links, validation gates, streaming item guidance ✅ |

---

<p align="right"><a href="#-stac-items--datastacitems">⬆️ Back to top</a></p>

