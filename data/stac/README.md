# 🛰️ STAC Catalog — `data/stac/`

![STAC](https://img.shields.io/badge/STAC-Collections%20%2B%20Items-2ea44f)
![Metadata](https://img.shields.io/badge/metadata-JSON-blue)
![Boundary%20Artifacts](https://img.shields.io/badge/publish%20gate-STAC%20%2B%20DCAT%20%2B%20PROV-purple)

> ✅ **Publish gate (non‑negotiable):** In KFM, data is not considered “published” until the **catalog boundary artifacts** exist — **STAC + DCAT + PROV** — *before* Graph/API/UI/Story consumption.  
> 🧭 Canonical ordering: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.

---

## 🎯 What this folder is

This directory is the **SpatioTemporal Asset Catalog (STAC)** home for KFM — the machine-readable index of **processed geospatial assets** (rasters, vectors, tiles, documents-as-assets) with:

- 🗺️ **Spatial** footprint (geometry/bbox)
- 🕰️ **Temporal** coverage (datetime / start+end)
- 🧾 **Discovery metadata** (keywords, descriptions, providers, license)
- 🧬 **Provenance hooks** (links to source attribution + `data/prov/` lineage bundles)
- 🔗 **Cross-layer linkage** to **DCAT** dataset entries (high-level discovery) + downstream Graph/API/UI

If the UI can “find it”, the API can “serve it”, or Focus Mode can “cite it” — it should be represented here.

---

## ✅ What belongs here (and what doesn’t)

### ✅ Yes (metadata only)
- 📁 `collections/` — STAC **Collection** JSON files (dataset-level metadata)
- 📁 `items/` — STAC **Item** JSON files (asset-level metadata)
- 📄 (optional) root **Catalog** file (often `catalog.json`) to tie everything together

### 🚫 No (data bytes)
- No GeoTIFFs, no Parquet, no PMTiles, no PDFs.  
  Those live in **`data/processed/**`** (or stable object storage) and are referenced by **STAC assets**.

---

## 🗂️ Directory layout (v13)

```text
data/stac/
├── 📄 README.md
├── 📄 catalog.json                      # (optional) root STAC Catalog
├── 📁 collections/
│   ├── 📄 <collection_id>.json          # OR /<collection_id>/collection.json (either is fine; be consistent)
│   └── 📄 <collection_id_2>.json
└── 📁 items/
    ├── 📁 <collection_id>/
    │   ├── 📄 <item_id>.json
    │   └── 📄 <item_id_2>.json
    └── 📁 <collection_id_2>/
        └── 📄 <item_id>.json
```

> 🧠 KFM convention: **Collections live in `data/stac/collections/` and Items in `data/stac/items/`**.

---

## 🔗 Related “boundary artifact” folders (neighbors)

- 📦 **Processed data (assets live here):** `../processed/`
- 🧾 **DCAT dataset catalog (discovery layer):** `../catalog/dcat/`
- 🧬 **PROV lineage bundles (how it was made):** `../prov/`
- 🧱 **Schemas (machine validation):** `../../schemas/stac/` *(expected in v13 layout)*
- 📏 **Standards / Profiles:** `../../docs/standards/KFM_STAC_PROFILE.md`

---

## 🧭 The KFM STAC philosophy (rules that keep us sane)

### 1) 🧾 Metadata is a contract (contract-first)
STAC JSON here is a **contract artifact** — it should be schema-valid and stable.

### 2) 🧬 Provenance before narrative (evidence-first)
Every Item should be linkable to:
- its **processed asset(s)** (`data/processed/**` or stable storage), and
- a **PROV record** describing inputs + processing steps, and
- a **DCAT record** that makes the dataset discoverable.

### 3) ♻️ Deterministic + reproducible
If the same inputs/configs run again, we should produce the same outputs — and the metadata should reflect that with stable IDs and clear lineage.

---

## 📌 Naming conventions (boring = scalable)

### Collection IDs
- ✅ lowercase, snake_case
- ✅ stable across time
- ✅ avoids spaces
- ✅ should match DCAT dataset id when possible

Examples:
- `ks_landsat_scenes`
- `ks_hydrology_1880`
- `ks_soils_sda`

### Item IDs
- ✅ unique within a collection
- ✅ include time + tile/scene key when relevant

Examples:
- `landsat_2020_06_01_path032_row033`
- `dem_3dep_1m_tile_15t_2023`
- `treaty_scan_1854_page_03_georef`

---

## 🧾 Required metadata checklists

### ✅ STAC Collection minimum
- `stac_version`
- `type: "Collection"`
- `id`, `title`, `description`
- `extent.spatial.bbox` and `extent.temporal.interval`
- `license`
- `links[]` (at least `self`, `root`, and any children/parents depending on structure)
- `providers[]` *(recommended)*

### ✅ STAC Item minimum
- `stac_version`
- `type: "Feature"`
- `id`
- `collection`
- `geometry` + `bbox`
- `properties.datetime` **or** `properties.start_datetime` + `properties.end_datetime`
- `links[]` (`self`, `root`, `parent`, `collection`)
- `assets{}` (must contain at least one “real” asset)

> 🧬 KFM expectation: Items should also carry **source attribution** and **license** info (either in Item properties or via Collection/provider fields) and link to PROV/DCAT where applicable.

---

## 📦 Asset conventions (how we describe the files)

KFM emphasizes open, interoperable, web-friendly formats:
- 🖼️ **Raster:** Cloud-Optimized GeoTIFF (COG), tile pyramids, PMTiles / XYZ tiles
- 🧭 **Vector:** GeoJSON, GeoPackage, GeoParquet
- 🧾 **Docs / Reports as assets:** PDF/HTML/MD (when they are publishable “evidence artifacts”)

### Suggested asset keys + roles
Common asset keys:
- `data` → the primary dataset artifact
- `tiles` → tileset entrypoint (PMTiles / XYZ template)
- `thumbnail` → small preview
- `overview` → medium preview
- `metadata` → QA report / stats JSON / README snapshot

Common roles:
- `["data"]`, `["tiles"]`, `["thumbnail"]`, `["overview"]`, `["metadata"]`

### `href` guidance
- Prefer **relative** `href` when assets live in-repo (`data/processed/**`)
- Use **absolute** `href` for stable object storage URLs (S3/HTTPS), but don’t bake in ephemeral signed URLs

---

## 🧬 Cross-layer linkage (STAC ↔ DCAT ↔ PROV)

To keep catalogs, graph, and narratives in sync:

### STAC → Data
- Items must point to the actual assets (files or stable endpoints) — usually under `data/processed/**`.

### DCAT → STAC / Distribution
- The DCAT dataset entry should include distribution links referencing:
  - the STAC Collection/Item(s), and/or
  - direct download endpoints.

### PROV end-to-end
- PROV should link raw → work → processed outputs and reference run/config identifiers.

### Practical link pattern (recommended)
In `links[]` for Collections/Items, add *project-consistent* relations, for example:

- `rel: "about"` → DCAT dataset JSON-LD entry (`data/catalog/dcat/<dataset>.jsonld`)
- `rel: "provenance"` → PROV bundle (`data/prov/<dataset_or_item>.prov.json`)
- `rel: "via"` → primary source listing / citation record (if you maintain `data/sources/**`)

> 🧠 STAC allows additional link relations — keep them consistent across the repo.

---

## 🛠️ Adding a new dataset (or “evidence artifact”) to STAC

### Step 0 — Put the bytes somewhere stable ✅
- Store final outputs in: `data/processed/<domain>/...`
- Keep filenames stable and meaningful.

### Step 1 — Create/Update the Collection 🧺
- Add a Collection JSON under `collections/`
- Fill out `extent`, `license`, `providers`, and descriptive metadata.

### Step 2 — Create Item(s) 📍
- Add Item JSON files under `items/<collection_id>/`
- Each Item should:
  - reference the correct `collection`
  - declare geometry/bbox/time
  - include at least one asset with a valid `href`

### Step 3 — Wire provenance + discovery 🧬🧾
- Ensure the dataset also has:
  - a DCAT entry in `data/catalog/dcat/`
  - a PROV bundle in `data/prov/`
- Link to them from STAC (see linkage section above).

### Step 4 — Validate 🧪
- Run STAC validation + JSON schema checks (see next section)
- CI should fail if the boundary artifacts are incomplete.

---

## 🧪 Validation (local + CI mindset)

### Local (recommended)
- ✅ Validate JSON structure (basic lint)
- ✅ Validate against STAC spec
- ✅ Validate against KFM STAC profile (when implemented)

Example approaches:
- `stac-validator` (Python)
- `stac-check` / JSON schema validation tooling
- your pipeline’s built-in validators (preferred once available)

> 🧱 CI expectation: missing PROV/DCAT links, broken `href`s, or invalid STAC should fail the build.

---

## 🧩 Minimal examples (copy/paste starters)

### Example: Collection (skeleton)
```json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "ks_example_dataset",
  "title": "Kansas Example Dataset",
  "description": "Short description of what this dataset is and why it exists.",
  "license": "proprietary-or-spdx-id",
  "extent": {
    "spatial": { "bbox": [[-102.0, 36.9, -94.6, 40.1]] },
    "temporal": { "interval": [["1850-01-01T00:00:00Z", "1900-12-31T23:59:59Z"]] }
  },
  "links": [],
  "providers": [
    { "name": "KFM", "roles": ["processor", "host"] }
  ]
}
```

### Example: Item (skeleton)
```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_example_item_1900",
  "collection": "ks_example_dataset",
  "geometry": { "type": "Polygon", "coordinates": [] },
  "bbox": [-102.0, 36.9, -94.6, 40.1],
  "properties": {
    "datetime": "1900-01-01T00:00:00Z"
  },
  "links": [
    { "rel": "collection", "href": "../../collections/ks_example_dataset.json", "type": "application/json" },
    { "rel": "provenance", "href": "../../../prov/ks_example_dataset.prov.json", "type": "application/json" },
    { "rel": "about", "href": "../../../catalog/dcat/ks_example_dataset.jsonld", "type": "application/ld+json" }
  ],
  "assets": {
    "data": {
      "href": "../../../processed/example/ks_example_dataset_1900.geojson",
      "type": "application/geo+json",
      "roles": ["data"],
      "title": "Primary dataset output"
    }
  }
}
```

---

## 🚨 Common gotchas (save yourself pain)

- ❌ **Don’t** put raw or intermediate data here — only metadata.
- ❌ **Don’t** ship Items without a corresponding Collection.
- ❌ **Don’t** use unstable URLs in `assets.href` (avoid signed links).
- ✅ **Do** keep IDs stable across re-runs; version changes should be explicit and traceable.
- ✅ **Do** ensure anything used by UI/Focus Mode is backed by STAC + DCAT + PROV.

---

## 🧭 Where to go next

- 📘 Master guide (pipeline rules): `../../docs/MASTER_GUIDE_v13.md`
- 📏 STAC profile (KFM-specific fields): `../../docs/standards/KFM_STAC_PROFILE.md`
- 🧾 DCAT catalog rules: `../catalog/dcat/README.md` *(if present; otherwise add one)*
- 🧬 PROV lineage rules: `../prov/README.md` *(if present; otherwise add one)*

🌾 If it’s not cataloged, it’s not shippable.