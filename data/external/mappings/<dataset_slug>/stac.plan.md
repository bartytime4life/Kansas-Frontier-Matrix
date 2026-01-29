# 🛰️ STAC Plan — `<dataset_slug>`

![Status](https://img.shields.io/badge/status-draft-yellow)
![Catalog](https://img.shields.io/badge/catalog-STAC%20%2B%20DCAT%20%2B%20PROV-blue)
![Domain](https://img.shields.io/badge/domain-external-7b68ee)

> **File:** `data/external/mappings/<dataset_slug>/stac.plan.md`  
> **Purpose:** Define exactly how `<dataset_slug>` becomes **STAC Collection + Item(s)** and how it cross-links to **DCAT + PROV** before anything downstream can consume it.

---

## 🧭 Table of Contents

- [🎯 Goal](#-goal)
- [🧩 Where this fits in the KFM pipeline](#-where-this-fits-in-the-kfm-pipeline)
- [📁 Expected repo paths](#-expected-repo-paths)
- [🏷️ IDs, slugs, and naming rules](#️-ids-slugs-and-naming-rules)
- [📦 Dataset facts (fill-in)](#-dataset-facts-fill-in)
- [🗺️ STAC modeling decisions](#️-stac-modeling-decisions)
  - [1) Collection plan](#1-collection-plan)
  - [2) Item plan](#2-item-plan)
  - [3) Asset plan](#3-asset-plan)
  - [4) Extensions + KFM-specific fields](#4-extensions--kfm-specific-fields)
- [🔗 Cross-catalog linking](#-cross-catalog-linking)
- [🧪 Validation & CI readiness](#-validation--ci-readiness)
- [🕰️ Versioning & update strategy](#️-versioning--update-strategy)
- [✅ Definition of Done](#-definition-of-done)
- [📎 Appendix: Templates](#-appendix-templates)

---

## 🎯 Goal

Convert the external dataset `<dataset_slug>` into **KFM-publishable** artifacts by defining:

- ✅ **STAC Collection** (dataset-level)
- ✅ **STAC Item(s)** (granules / distributable units)
- ✅ **Asset mapping** (what files are assets, roles, media types, naming)
- ✅ **Cross-links** to:
  - **DCAT** (high-level discovery / distribution)
  - **PROV** (end-to-end lineage and run identifiers)

This document is a *plan* (human-facing), but it should be specific enough that a pipeline can implement it deterministically. 🧱

---

## 🧩 Where this fits in the KFM pipeline

KFM treats datasets as “published” only after the **catalog boundary artifacts** exist.

**Stages (non-negotiable):**  
`raw → work → processed → catalogs (STAC/DCAT/PROV) → graph → API → UI/story`

This plan covers the **catalogs** stage and defines what the **processed** outputs must look like to support clean STAC Items.

---

## 📁 Expected repo paths

### 📂 Domain layout (this dataset lives under `external/`)

```text
📁 data/
├─ 📁 stac/                                   🛰️ STAC geospatial catalog (JSON)
│  ├─ 📁 collections/                          🧩 STAC Collections (JSON)
│  └─ 📁 items/                                📦 STAC Items (JSON)
├─ 📁 catalog/                                 🗂️ DCAT discovery layer
│  └─ 📁 dcat/                                  🧾 DCAT Dataset entries (JSON-LD)
├─ 📁 prov/                                    🧬 provenance bundles (per run / per dataset)
└─ 📁 external/                                🌐 external sources lane (snapshots → staging → promoted)
   ├─ 📁 raw/
   │  └─ 📁 <dataset_slug>/                    🧾 raw source drops (read-only / never overwrite)
   ├─ 📁 work/
   │  └─ 📁 <dataset_slug>/                    🧪 intermediate outputs + experiments (ephemeral)
   ├─ 📁 processed/
   │  └─ 📁 <dataset_slug>/                    ✅ final outputs (what STAC Items point to)
   └─ 📁 mappings/
      └─ 📁 <dataset_slug>/                    🧩 mapping docs + crosswalks (this plan lives here)
```

### 📌 Outputs this plan expects to produce

| Artifact | Path (canonical) | Notes |
|---|---|---|
| STAC Collection | `data/stac/collections/<collection_id>.json` | One per dataset |
| STAC Items | `data/stac/items/<collection_id>/<item_id>.json` | Many per dataset |
| DCAT Entry | `data/catalog/dcat/<dataset_slug>.jsonld` | Links to STAC +/or data |
| PROV Bundle | `data/prov/<dataset_slug>/<run_id>.prov.json` | Lineage + run metadata |
| Processed Assets | `data/external/processed/<dataset_slug>/...` | The “real” payload |

---

## 🏷️ IDs, slugs, and naming rules

### dataset_slug ✅
**Format:** `kebab-case`, stable, no spaces, no dates unless the dataset is inherently date-based.

**Examples:**  
- `usgs-hydrography-nhd`  
- `kshs-historic-maps`  
- `census-1900-kansas`

---

### STAC Collection ID ✅

Pick one:

- **Option A (simple):** `external-<dataset_slug>`
- **Option B (globally explicit):** `kfm-external-<dataset_slug>`

> **Decision:** ☐ A ☐ B  
> **Chosen:** `<collection_id> = __________________________`

---

### STAC Item ID strategy ✅

STAC Items should represent **granules** (what a user would download / what is independently meaningful).

Pick one of these common strategies:

1. **Per processed file (default)** 🧱  
   - One Item per distributable file (GeoParquet, COG, GeoJSON, CSV, etc.)
2. **Per time slice** 🕰️  
   - One Item per year/month/day (if time series)
3. **Per tile / grid cell** 🧩  
   - One Item per spatial tile (if imagery at scale)
4. **Per region** 🗺️  
   - One Item per county/tract/management area (if partitioned)

> **Decision:** ☐ Per file ☐ Per time slice ☐ Per tile ☐ Per region  
> **Chosen:** _______________________________________________

**Item ID template (recommended):**
- `external-<dataset_slug>__<granule_key>`
  - `granule_key` should be stable (date, tile id, region id, or filename stem)

---

## 📦 Dataset facts (fill-in)

> This section becomes the authoritative “inputs” for STAC Collection fields like `description`, `license`, `providers`, keywords, and summaries.

| Field | Value |
|---|---|
| Human title | `<title>` |
| Short description | `<1–3 sentences>` |
| Provider / Publisher | `<org>` |
| Source URL(s) | `<url(s)>` |
| License | `<SPDX or plain text>` |
| Spatial scope | `Kansas / CONUS / global / unknown` |
| Temporal scope | `<start> → <end> (or “none”)` |
| Update cadence | `static / annual / monthly / ad-hoc` |
| Primary geometry | `raster / vector / tabular` |
| Sensitive / restricted? | `public / restricted / confidential` |
| Key fields (if vector/tabular) | `<id fields, date fields, geometry fields>` |
| Processing summary | `<what we do to it (reproject, clip, normalize, etc.)>` |

---

## 🗺️ STAC modeling decisions

### 1) Collection plan

**Goal:** One Collection that “hangs” all Items for `<dataset_slug>`.

**Collection must capture:**
- Spatial extent (bbox / geometry coverage at dataset level)
- Temporal extent (interval)
- License + provider(s)
- Keywords and discoverability metadata
- KFM-specific provenance hooks (per profile)

#### Collection extent plan
- **Spatial:** derived from union of all item bboxes (preferred), or known bounding polygon.
- **Temporal:** derived from min/max of Item datetimes (if time-aware), else use a single interval or omit time slicing.

> **Decision:**  
> ☐ extent computed from items  
> ☐ extent defined from known boundary (attach boundary file in processed/)

---

### 2) Item plan

**Goal:** Item = smallest independently useful unit.

#### Item geometry & bbox plan
- Use exact footprint if available (preferred).
- Else use bbox derived from geometry column / raster bounds.

> **Decision:**  
> ☐ exact footprint available  
> ☐ bbox-only acceptable

#### Datetime plan
Pick one:

- **Single datetime** per item (e.g., image capture date)  
- **Start/end datetime** (time range) stored in item properties (recommended when time spans)

> **Decision:** ☐ single datetime ☐ start/end range ☐ none (static)

---

### 3) Asset plan

STAC assets are what users (and pipelines) actually consume.

#### Processed formats (recommended defaults)
Choose what you will publish as **processed**:

- **Raster:** COG (`.tif`) + optional overviews  
- **Vector:** GeoParquet (`.parquet`) + optional GeoJSON sample  
- **Tabular:** CSV/Parquet + separate metadata/README

> **Chosen processed payload(s):**  
> ☐ COG ☐ GeoParquet ☐ GeoJSON ☐ CSV ☐ Parquet ☐ Other: ________

#### Asset keys & roles
Define asset keys (consistent across items):

| Asset key | Role(s) | File pattern | Notes |
|---|---|---|---|
| `data` | `["data"]` | `.../<granule>.{tif|parquet|geojson|csv}` | Primary payload |
| `metadata` | `["metadata"]` | `.../<granule>.meta.json` | Optional sidecar |
| `thumbnail` | `["thumbnail"]` | `.../<granule>.png` | Optional |
| `documentation` | `["documentation"]` | `.../README.md` | Optional |
| `tiles` | `["tiles"]` | `.../<granule>.mbtiles` | Optional |

> **Rule:** Every Item must have at least one `data` asset.

#### HREF rules (portable STAC)
- Prefer **repo-relative** hrefs (stable inside Git checkout).
- If assets live in object storage, use **stable absolute URLs** and pin version identifiers.

> **Decision:** ☐ relative hrefs ☐ absolute hrefs (with version pin)

---

### 4) Extensions + KFM-specific fields

KFM uses profiles that extend base standards with project-specific fields (notably: provenance + uncertainty).

#### Required (per KFM profile)
- ☐ include KFM provenance reference field(s)
- ☐ include uncertainty / confidence indicators where applicable
- ☐ include classification / sensitivity propagation fields

> **Implementation note:** Do *not* invent ad-hoc fields. If you need a field that isn’t in `KFM_STAC_PROFILE.md`, propose a profile extension.

---

## 🔗 Cross-catalog linking

### STAC → processed data
- Every STAC Item must link to the asset(s) under `data/external/processed/<dataset_slug>/...`.

### STAC ↔ PROV
- Each STAC Item should link (directly or via KFM profile field) to the PROV bundle for the run that produced it.
- PROV must capture: raw inputs → work intermediates → processed outputs → agents (human/software) → parameters.

### DCAT → STAC/Distribution
- DCAT entry should include distribution links pointing to:
  - the STAC Collection (discovery)
  - and/or direct downloads for canonical processed artifacts

### Graph references catalogs (not payloads)
- If this dataset feeds Neo4j, graph nodes should reference STAC Item IDs (or stable identifiers), not embed blobs.

---

## 🧪 Validation & CI readiness

### Automated checks (must pass)
- ☐ STAC JSON validates against schema + KFM profile
- ☐ All `href` targets exist (or are reachable)
- ☐ BBox/geometry validity checks (no NaNs, correct winding, etc.)
- ☐ License present and consistent across Collection + Items
- ☐ Classification not “downgraded” vs inputs (propagation check)
- ☐ PROV bundle exists and references inputs/outputs
- ☐ DCAT entry exists and links to STAC/distributions

### Manual review (recommended)
- ☐ Metadata completeness (keywords, description, providers)
- ☐ Sensitivity review (sovereignty / protected locations)
- ☐ Spot-check a sample of items for bbox/time correctness

---

## 🕰️ Versioning & update strategy

KFM expects dataset evolution to be explicit.

### Choose a versioning scheme
Pick one:

- **Semantic version:** `v1.0.0`, `v1.1.0`, etc.
- **Run-based version:** `run-<YYYYMMDD>-<shortsha>`
- **Source-snapshot version:** `src-<provider_release_id>`

> **Chosen:** _______________________________________________

### What changes when a new version lands?
- Processed outputs go to a new versioned folder OR overwrite in-place with explicit version tags.
- DCAT + PROV link to predecessor (revision chain).
- STAC Items:
  - either new items per version (preferred for auditability)
  - or update existing items with `version` property (only if your governance allows it)

> **Decision:**  
> ☐ new Items per version (audit-friendly)  
> ☐ update existing Items (requires strong review)

---

## ✅ Definition of Done

**This STAC plan is “done” when:**

- ☐ All decisions above are filled in (no placeholders)
- ☐ Collection ID + Item strategy are finalized
- ☐ Asset keys/roles are defined and match actual processed outputs
- ☐ Cross-links to DCAT + PROV are specified clearly
- ☐ Validation steps are listed and repeatable
- ☐ Sensitivity/license notes are explicit (if applicable)

**The dataset is “publishable” when:**

- ☐ `data/external/processed/<dataset_slug>/...` exists
- ☐ `data/stac/collections/<collection_id>.json` exists
- ☐ `data/stac/items/<collection_id>/...` exist
- ☐ `data/catalog/dcat/<dataset_slug>.jsonld` exists
- ☐ `data/prov/<dataset_slug>/<run_id>.prov.json` exists
- ☐ CI passes all catalog + governance gates

---

## 📎 Appendix: Templates

<details>
<summary>📄 STAC Collection template (skeleton)</summary>

```json
{
  "type": "Collection",
  "stac_version": "1.0.0",
  "id": "<collection_id>",
  "title": "<human title>",
  "description": "<1–3 paragraphs>",
  "license": "<license>",
  "providers": [
    {
      "name": "<provider name>",
      "roles": ["producer", "processor", "host"],
      "url": "<provider url>"
    }
  ],
  "extent": {
    "spatial": { "bbox": [[<minx>, <miny>, <maxx>, <maxy>]] },
    "temporal": { "interval": [[ "<start-iso>", "<end-iso>" ]] }
  },
  "links": [
    { "rel": "root", "href": "<relative-or-absolute>", "type": "application/json" }
  ],
  "summaries": {
    "kfm:domain": ["external"],
    "kfm:dataset_slug": ["<dataset_slug>"]
  }
}
```
</details>

<details>
<summary>📄 STAC Item template (skeleton)</summary>

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "<item_id>",
  "collection": "<collection_id>",
  "geometry": { "type": "Polygon", "coordinates": [] },
  "bbox": [<minx>, <miny>, <maxx>, <maxy>],
  "properties": {
    "datetime": "<iso-datetime-or-null>",
    "start_datetime": "<optional>",
    "end_datetime": "<optional>",
    "title": "<optional>",
    "description": "<optional>",
    "license": "<optional-override-or-inherit>"
  },
  "assets": {
    "data": {
      "href": "data/external/processed/<dataset_slug>/<granule>.<ext>",
      "type": "<media-type>",
      "roles": ["data"],
      "title": "Primary data"
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/<collection_id>.json", "type": "application/json" }
  ]
}
```
</details>

<details>
<summary>🧠 Optional: AI-assisted metadata drafting (workflow)</summary>

- ☐ Use a local or CI-driven assistant to draft STAC JSON from filenames + samples.
- ☐ Human reviews and corrects:
  - extents (bbox/time)
  - license/provider
  - asset roles/media types
  - provenance pointers
- ☐ Commit only after review (no “auto-merge” metadata).

</details>

