<!-- According to a document from 2026-01-17: this README follows KFM’s contract-first + provenance-first documentation expectations. -->

# 🏔️ Kansas DEM (USGS ~10m) — 3D Terrain Tiles (v1)

![DEM](https://img.shields.io/badge/data-DEM-2ea44f)
![Source](https://img.shields.io/badge/source-USGS-1f6feb)
![Resolution](https://img.shields.io/badge/resolution-~10m-orange)
![3D](https://img.shields.io/badge/3D-CesiumJS-purple)
![Version](https://img.shields.io/badge/version-v1-informational)

> [!IMPORTANT]
> This directory contains **web-ready terrain tiles** (a built artifact).  
> **Do not hand-edit tiles** — regenerate via the data pipeline so provenance, metadata, and QA remain valid ✅

---

## 🔎 At a glance

| Item | Value |
|---|---|
| 📍 Repo path | `web/assets/maps/3d/terrain/kansas_dem_usgs_10m/v1/terrain/` |
| 🆔 Dataset ID | `kansas_dem_usgs_10m` |
| 🧷 Version | `v1` |
| 🗺️ Coverage | Kansas (statewide) |
| 📏 Nominal source resolution | ~10 meters |
| 🎯 Purpose | Base terrain surface for the KFM 3D viewer (CesiumJS) |
| 🌐 Expected served URL | `/assets/maps/3d/terrain/kansas_dem_usgs_10m/v1/terrain/` *(depends on bundler/static hosting)* |

---

## 🧭 Quick links

> [!NOTE]
> In KFM, **anything shown in the UI must be traceable** via metadata + lineage.  
> This folder is the *delivery format*; the *truth* lives in the catalog + contracts.

- 🧾 **Data contract (required):** `../data-contract.json` *(or equivalent contract file at the dataset/version level)*
- 🌐 **Catalog outputs (canonical homes):**
  - `data/stac/` — STAC Items/Collections
  - `data/catalog/dcat/` — DCAT dataset records
  - `data/prov/` — PROV lineage bundles
- 📚 **Standards profiles (project-governed):**
  - `docs/standards/KFM_STAC_PROFILE.md`
  - `docs/standards/KFM_DCAT_PROFILE.md`
  - `docs/standards/KFM_PROV_PROFILE.md`

---

## 📦 What’s inside this folder

This folder typically contains a Cesium-compatible terrain tileset (format varies by pipeline: **Quantized-Mesh**, **Heightmap**, etc.).

```text
🗂️ web/assets/maps/3d/terrain/kansas_dem_usgs_10m/v1/terrain/
├── 📄 README.md                     👈 you are here
├── 📄 layer.json                    (common in Cesium terrain)
├── 🗂️ 0/                            (tile pyramid root — example)
│   └── 🗂️ 0/
│       └── 🗂️ 0.terrain             (example tile)
└── 🗂️ ...                           (additional LOD / tile coordinates)
```

> [!TIP]
> If your output format doesn’t match the above (e.g., it uses `tilemapresource.xml`, `.png` heightmaps, or a different tiler layout), **keep this README but update the “Format notes” section** below.

---

## 🚀 Using this terrain in the web viewer (CesiumJS)

KFM’s web viewer integrates **CesiumJS** for 3D globe/terrain visualization. This folder is intended to be served as a static asset and loaded as a terrain provider.

### Example (CesiumJS)

```js
// Example: wire this into your KFM Cesium viewer setup.
// Adjust BASE_URL / asset mount as needed for your bundler (Vite/Next/etc).

import * as Cesium from "cesium";

const terrainUrl =
  `${import.meta.env.BASE_URL}assets/maps/3d/terrain/kansas_dem_usgs_10m/v1/terrain/`;

const viewer = new Cesium.Viewer("cesiumContainer", {
  terrainProvider: await Cesium.CesiumTerrainProvider.fromUrl(terrainUrl),
});
```

### Expected behavior ✅
- Terrain loads without repeated `Tile failed to load` warnings.
- A Kansas-focused view shows realistic relief (subtle but present).
- Switching to other 3D layers (e.g., 3D Tiles content) remains stable.

---

## 🧾 Contract-first & provenance-first requirements

> [!IMPORTANT]
> “No mystery layers.”  
> If this terrain is enabled in UI/Focus Mode, it must be backed by a **data contract** and **catalog records** (STAC/DCAT/PROV), and pass validators/CI.

### Minimum contract checklist (recommended)

<details>
<summary>✅ Expand: required metadata fields (practical minimum)</summary>

- **Source**
  - `source.name` (e.g., `USGS 3DEP / NED`)
  - `source.url` (download/landing page)
  - `source.retrieved_at` (date/time)
- **License / use**
  - `license` (plus attribution requirements if any)
- **Spatial & temporal extent**
  - `bbox` (WGS84) + `geometry` or footprint
  - `temporal_extent` *(if applicable; DEMs may be “publication date” based)*
- **Processing**
  - `processing.steps[]` (mosaic → reprojection → resample → tiling → QA)
  - `processing.tools[]` (versions pinned)
  - `processing.parameters` (tile scheme, max zoom, height scale, etc.)
- **Quality**
  - `qa.checks[]` (tile completeness, min/max elevation sanity, visual spot-check)
- **Lineage**
  - `prov.bundle_ref` (or equivalent pointer into `data/prov/`)

</details>

### Suggested `data-contract.json` skeleton

```json
{
  "id": "kansas_dem_usgs_10m",
  "version": "v1",
  "type": "terrain.dem",
  "title": "Kansas DEM (USGS ~10m) — Terrain Tiles",
  "source": {
    "name": "USGS",
    "url": "https://example.com/replace-with-usgs-source",
    "retrieved_at": "YYYY-MM-DD"
  },
  "license": "TBD",
  "spatial": {
    "crs": "EPSG:4326",
    "bbox": [-102.05, 36.99, -94.59, 40.00]
  },
  "processing": {
    "steps": [
      "Acquire source DEM tiles",
      "Mosaic + clip to Kansas",
      "Reproject to Cesium-friendly CRS",
      "Generate terrain tiles",
      "Run QA validation"
    ]
  },
  "artifacts": {
    "terrain_url_path": "/assets/maps/3d/terrain/kansas_dem_usgs_10m/v1/terrain/"
  }
}
```

> [!NOTE]
> The bbox above is a **placeholder** that matches Kansas’ approximate extent — replace with authoritative bounds from the pipeline output.

---

## 🧱 Performance & Level-of-Detail (LOD) guidance

Terrain is a foundational layer, so treat it like infrastructure:

- 🧊 **Prefer LOD-appropriate elevation**: when zoomed out, use lower-res terrain; when zoomed in, load this ~10m terrain for local relief details.
- 🧠 **Cache smartly**: terrain tiles benefit heavily from HTTP caching (long-lived immutable assets per version).
- 🧰 **Avoid re-encoding in-place**: publish updates as `v2/terrain/` to keep URLs stable for reproducibility.

---

## 🛠️ Regeneration pipeline (conceptual)

```mermaid
flowchart LR
  A[🛰️ Source DEM (USGS)] --> B[🧪 ETL: mosaic/clip/reproject]
  B --> C[🧱 Tile build: terrain format + pyramid]
  C --> D[🌐 Web asset publish (this folder)]
  B --> E[📚 Catalog: STAC/DCAT]
  B --> F[🧬 Lineage: PROV bundle]
  E --> G[🧭 UI + Focus Mode citations]
  F --> G
```

### Suggested build steps (fill in with your actual tooling)
1. ⬇️ Fetch source DEM tiles (raw, read-only)
2. 🧩 Mosaic + clip to Kansas AOI
3. 🧭 Reproject to required CRS (commonly WGS84 / EPSG:4326 for Cesium terrain workflows)
4. 🧱 Generate terrain tiles (pyramid + metadata)
5. ✅ Run validators (contract/schema + spot checks)
6. 📦 Publish to `web/assets/.../v1/terrain/` **only if** QA passes

---

## ✅ QA checklist (pre-merge)

- [ ] Data contract exists and validates (schema + required fields)
- [ ] STAC/DCAT records exist (or are referenced) for the dataset/version
- [ ] PROV lineage bundle exists and links back to the source + processing activity
- [ ] Tiles load in Cesium without persistent errors
- [ ] Visual inspection: Kansas area looks plausible (no “inverted” terrain / wild spikes)
- [ ] Versioning respected: no breaking edits to existing `v1/` artifacts

---

## 🏷️ Versioning policy

- ✅ `v1/` is immutable once published (reproducibility & citations)
- ➕ changes require **new** version folder (e.g., `v2/terrain/`)
- 🧾 each version must have its own contract + catalog lineage

---

## 🙏 Attribution

Terrain source, license, and required attribution **must** be declared in the dataset’s data contract and in catalog records.  
This README intentionally defers to those governed artifacts so the UI can auto-generate credits and citations.

---
