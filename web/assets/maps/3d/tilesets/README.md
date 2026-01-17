# 3D Tilesets 🧱🌎

![Format](https://img.shields.io/badge/format-3D%20Tiles-blue)
![Viewer](https://img.shields.io/badge/viewer-CesiumJS-6f42c1)
![CRS](https://img.shields.io/badge/CRS-WGS84%20(EPSG%3A4326)-success)
![Policy](https://img.shields.io/badge/policy-provenance--first-critical)

> 📌 Path: `web/assets/maps/3d/tilesets/`  
> 🗺️ KFM’s web viewer pairs **MapLibre (2D)** + **CesiumJS (3D)** and streams 3D geospatial content via the open **3D Tiles** standard.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

## What this folder is ✅

This directory holds **streaming-ready 3D tilesets** (terrain, meshes, point clouds, etc.) that the web app can load as static assets. The `web/` front-end includes an `assets/` area for static files.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

## What this folder is not 🚫

This is **not** the right place for:
- raw source data (LAS/LAZ, full-resolution DEM GeoTIFFs, photogrammetry projects)
- scratch exports or “mystery layers” without metadata

KFM is *contract-first* and *provenance-first*: anything that appears in the UI should be traceable to cataloged sources and documented processing, enforced via required metadata + validation.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## TL;DR ✅

- 📦 **One tileset per folder** → `/<tileset-id>/tileset.json`
- 🧾 Include a `metadata.json` **data contract** (required) + provenance (strongly recommended).  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- 🌐 Serve in **WGS84 (EPSG:4326)** for web consistency; record original CRS and any reprojection in provenance.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- 🚀 Keep repo-friendly demos here; ship “real” large tilesets via **CDN / tile server** when needed.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## Folder layout 📁

```text
web/assets/maps/3d/tilesets/
├── 📄 README.md                       # 📄 you are here 📌
├── 🗂️🧾 _catalog.json                  # 🗂️ optional: UI-friendly listing/labels
└── 📦 <tileset-id>/                    # 📦 e.g. ks-dem-10m-v1
    ├── 🧱🧾 tileset.json                # 🧱 required: 3D Tiles entrypoint
    ├── 🧾🏷️ metadata.json               # 🧾 required: data contract (source, license, extent, processing…)
    ├── 🧬🧾 provenance.json             # 🧬 recommended: pipeline lineage + tool versions
    ├── 🏷️📄 attribution.md              # 🏷️ recommended: human-readable credits/attribution text
    ├── 🖼️ preview.jpg                   # 🖼️ optional: thumbnail for catalogs/Story Nodes
    └── 🧩 tiles/                        # 🧩 typical: batched tile payloads (b3dm/glb/pnts/…)
        ├── 0/
        └── ➕ …
```

> 💡 `metadata.json` is the machine-readable contract; `attribution.md` is the human-readable “what is this / who made it / who to credit” page.

---

## Common tileset types 🧩

KFM’s 3D mode is meant for data with a vertical or volumetric dimension (topography, point clouds, buildings, etc.) and can stream large 3D datasets as you zoom.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Examples you’ll likely store here:

- 🏔️ **Terrain**: DEM-derived terrain tiles (often converted to **quantized-mesh** or **3D Tiles** for Cesium).  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- ☁️ **LiDAR point clouds** (3D Tiles)
- 🧱 **Building models / city meshes**
- 🗿 **Landmark photogrammetry models** (3D Tiles / glTF payloads)

> ⚠️ 3D is computationally heavier than 2D, so treat it as an *opt-in* “zoom in for depth” feature, not a default.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## Loading tilesets in the web app 🖥️

In 3D mode, CesiumJS loads tilesets by URL (typically pointing at `tileset.json`). KFM’s viewer stack is designed specifically for this MapLibre↔Cesium split.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

```ts
// Example: add a tileset from this folder
const tileset = await Cesium.Cesium3DTileset.fromUrl(
  "/assets/maps/3d/tilesets/<tileset-id>/tileset.json"
);

viewer.scene.primitives.add(tileset);
viewer.zoomTo(tileset);
```

---

## Data contract: `metadata.json` 🧾

KFM treats metadata + lineage as first-class. It uses open standards (e.g., STAC / DCAT / PROV-O) and requires each dataset to ship with a metadata JSON “data contract” describing **source, license, spatial/temporal extent, and processing steps**, enforced via validators + CI checks.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Minimal template (copy/paste) 🧰

```json
{
  "id": "ks-dem-10m-v1",
  "title": "Kansas DEM (10m) — Terrain Tileset",
  "type": "terrain",
  "format": "3dtiles",
  "tilesetUrl": "/assets/maps/3d/tilesets/ks-dem-10m-v1/tileset.json",

  "crs": {
    "display": "EPSG:4326",
    "original": "EPSG:xxxx",
    "notes": "Reprojected on ingest; see provenance.json"
  },

  "vertical": {
    "units": "m",
    "datum": "unknown"
  },

  "extent": {
    "bboxWgs84": [-102.051, 36.993, -94.588, 40.003],
    "temporal": { "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" }
  },

  "license": "CC-BY-4.0",
  "attribution": "USGS (example)",
  "sources": [
    { "name": "Source dataset name", "url": "SOURCE_URL_OR_ARCHIVE_REF" }
  ],

  "processing": [
    {
      "step": "reproject",
      "tool": "gdalwarp",
      "params": "…",
      "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
    },
    {
      "step": "tile",
      "tool": "3d-tiler",
      "params": "…",
      "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
    }
  ]
}
```

### Provenance & “no mystery layers” 🔎

The UI should make it easy to inspect the source and metadata of any visible layer, exposing “the map behind the map” rather than treating it as a black box.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Recommended practice:
- ✅ store machine-readable lineage in `provenance.json`
- ✅ keep a human-readable `attribution.md`
- ✅ record tool versions + key parameters (repeatability)
- ✅ include license + attribution text verbatim (compliance)

---

## Coordinate systems & units 🌐

KFM’s web-facing projection standard is **WGS84 (EPSG:4326)**; data arriving in other projections is reprojected on ingest and recorded in provenance.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**Rules of thumb:**
- ✅ Serve a consistent CRS for rendering
- 🧾 Always record `crs.original`
- ⛰️ Standardize vertical units (meters recommended) and document the vertical datum

---

## Performance, LOD, and hosting 🏎️

KFM explicitly calls out tiling/caching strategies (XYZ tiles, CDN, etc.) and Level-of-Detail (LOD) management, extending the same idea to 3D terrain (lower-res until zoomed in).  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### When static assets aren’t enough 📈

As data volume grows, the architecture supports introducing specialized services (e.g., a dedicated **tile server**) instead of bundling everything into the web app.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**Suggested split:**
- 🧪 **Repo/static** (this folder): small demos, fixtures, story-specific “wow” tilesets
- ☁️ **CDN/object storage**: large statewide terrain, dense point clouds, city meshes
- 🧰 **Tile service**: when you need auth, analytics, request logging, or controlled access

### Optional: Cesium ion workflow ☁️

Some pipelines upload 3D content to **Cesium ion**, which optimizes and tiles it for streaming to a web app via CesiumJS.  [oai_citation:16‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq)

If using this route, keep **the authoritative data contract + attribution** in KFM (don’t let “ion settings” become the only source of truth).

---

## Add a tileset (checklist) ➕

1. 📁 Create: `web/assets/maps/3d/tilesets/<tileset-id>/`
2. 🧱 Add: `tileset.json` (entrypoint)
3. 🧾 Add: `metadata.json` (required contract)  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
4. 🧬 Add: `provenance.json` + `attribution.md` (recommended)  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
5. 🖼️ Optional: `preview.jpg`
6. 🗂️ Register it in your tileset catalog/config (e.g. `_catalog.json`)
7. ✅ Validate locally:
   - [ ] loads in CesiumJS (no console errors)
   - [ ] correct position + height
   - [ ] attribution visible somewhere in the UI
   - [ ] license + sources + processing recorded

---

## Troubleshooting 🧯

<details>
<summary><strong>Tileset loads but appears in the wrong place</strong></summary>

- Confirm `crs.display` is WGS84 and any reprojection was recorded.  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Check bounding volumes / transforms inside `tileset.json`
- Verify units (degrees vs meters) in your pipeline metadata

</details>

<details>
<summary><strong>3D mode is slow</strong></summary>

- Make sure LOD/geometric error is configured sensibly (coarse → fine)
- Consider serving heavy tilesets via CDN or a tile service rather than bundling in the web app.  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Keep 3D as opt-in, especially on mobile/low-power devices.  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

</details>

---

## Alternatives & interoperability 🔁

If you need a lightweight (non-web) 3D delivery path, the project design also mentions exporting to **KML/KMZ** (including “regionated” KML tiles for progressive loading in Google Earth).  [oai_citation:23‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## Design sources 📚

This README follows the project’s documented intent for:
- MapLibre (2D) + CesiumJS (3D) viewer integration and 3D Tiles streaming  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Contract-first + provenance-first metadata and validation (no mystery layers)  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- WGS84 (EPSG:4326) as the web standard + reprojection tracked in provenance  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Tiling/caching + CDN/tile server scaling patterns and LOD practices  [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- DEM/terrain conversion guidance for Cesium (quantized mesh / 3D tiles)  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Optional Cesium ion tiling/streaming workflow  [oai_citation:30‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq)
- Optional KML/KMZ regionation path for Google Earth  [oai_citation:31‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
