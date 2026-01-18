# 🏞️ Terrain GLB Assets (KFM)

![Asset](https://img.shields.io/badge/asset-terrain%20mesh%20(GLB)-informational)
![Format](https://img.shields.io/badge/format-glTF%202.0%20(GLB)-blue)
![Policy](https://img.shields.io/badge/policy-contract--first%20%26%20provenance--first-purple)
![Runtime](https://img.shields.io/badge/runtime-web%20viewer%20(2D%2F3D)-orange)

📍 **Path:** `web/assets/media/models-3d/glb/terrain/`

This folder holds **terrain meshes in `.glb`** (glTF binary) intended for **web-friendly 3D rendering** inside Kansas Frontier Matrix (KFM). These assets are *visual terrain geometry* (not raw elevation rasters) and should be treated as **governed, attributable artifacts**.

> [!IMPORTANT]
> **If a terrain model appears in the UI / Story Nodes / Focus Mode, it must be traceable.**  
> No “mystery terrain.” Every GLB here must have a clear source + license + processing lineage via KFM’s metadata approach. 🧾🔍

---

<details>
<summary>📚 Table of Contents</summary>

- [✅ What belongs here](#-what-belongs-here)
- [🚫 What does NOT belong here](#-what-does-not-belong-here)
- [🗂️ Folder layout](#️-folder-layout)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🧾 Terrain manifest](#-terrain-manifest)
  - [Required fields](#required-fields)
  - [Example manifest](#example-manifest)
- [🧭 Coordinate, scale, and georeferencing rules](#-coordinate-scale-and-georeferencing-rules)
- [⚡ Performance & LOD guidance](#-performance--lod-guidance)
- [➕ Adding a new terrain model](#-adding-a-new-terrain-model)
- [🧪 QA checklist](#-qa-checklist)
- [🔗 Related KFM docs & standards](#-related-kfm-docs--standards)

</details>

---

## ✅ What belongs here

Use this folder for **small, curated terrain meshes** that the web client can load quickly, such as:

- 🧩 **Story-scoped terrain patches** (battlefields, river crossings, town sites, trail segments)
- 🏁 **“Hero” scenes** used for demos, onboarding, or narrative focus moments
- 🧪 **Prototypes / previews** of pipeline outputs (with explicit metadata + provenance pointers)

## 🚫 What does NOT belong here

Avoid committing or shipping very large terrain datasets as raw GLBs:

- 🏔️ Statewide / regional high-resolution DEM meshes (too large for “bundle-style” assets)
- ☁️ LiDAR point clouds as GLB (use appropriate streaming formats instead)
- 📦 Anything that should be **streamed** (prefer Cesium-friendly formats like 3D Tiles where applicable)

> [!NOTE]
> If you find yourself needing “lots of tiles” or “lots of LODs,” you probably want a **streaming terrain strategy** rather than adding more GLBs here.

---

## 🗂️ Folder layout

Recommended structure (sidecars are part of the “contract-first” approach):

```text
web/assets/media/models-3d/glb/terrain/
├── README.md
├── <terrain_id>--v<semver>.glb
├── <terrain_id>--v<semver>.manifest.json
└── <terrain_id>--v<semver>.preview.webp   (optional but recommended)
```

> [!TIP]
> Keep the **GLB** focused on geometry/materials, and keep **georeferencing + provenance** in the manifest JSON (plus KFM catalogs).

---

## 🏷️ Naming conventions

Use **stable IDs** that communicate *place + timeslice + intent*.

**Pattern:**
`<place_or_tile>--<timeslice_or_period>--<source_or_method>--v<semver>`

**Examples:**
- `ks-flint-hills--1850--dem-derived--v1.0.0.glb`
- `ks-kaw-river-crossing--1864--hand-modeled--v0.3.0.glb`
- `ks-fort-leavenworth--1870--photogrammetry--v2.1.0.glb`

Rules:
- ✅ lowercase, kebab-case (`-`)
- ✅ semver for versioning (`v1.2.3`)
- ✅ never overwrite an older version; publish a new version instead 🧱

---

## 🧾 Terrain manifest

Every GLB **must** have a sidecar manifest:

`<terrain_id>--v<semver>.manifest.json`

Why?
- 🧾 Enforces a **data contract** (who/what/when/where/how)
- 🧭 Captures **georeferencing** (how to place the model in-world)
- 🧠 Lets Story Nodes / Focus Mode link terrain to datasets & citations without hardcoding paths

### Required fields

| Field | Required | Example | Notes |
|---|:---:|---|---|
| `id` | ✅ | `ks-flint-hills--1850--dem-derived` | Stable logical ID (no version) |
| `version` | ✅ | `1.0.0` | SemVer version |
| `title` | ✅ | `Flint Hills Terrain (c. 1850)` | Human-readable |
| `asset` | ✅ | `./ks-flint-hills--1850--dem-derived--v1.0.0.glb` | Relative path |
| `bbox_wgs84` | ✅ | `[-96.9, 38.4, -96.2, 39.1]` | `[minLon,minLat,maxLon,maxLat]` |
| `crs_display` | ✅ | `EPSG:4326` | Web display CRS |
| `crs_source` | ✅ | `EPSG:26914` | Original processing CRS (if known) |
| `vertical_datum` | ✅ | `NAVD88` / `EGM96` / `unknown` | Be explicit |
| `units` | ✅ | `meters` | For vertex scale + elevations |
| `up_axis` | ✅ | `Y` | glTF convention |
| `anchor_wgs84` | ✅ | `{ "lon": -96.55, "lat": 38.77, "height_m": 420.0 }` | “Placement anchor” |
| `transform` | ✅ | `{ "type": "ENU", "matrix4": [...] }` | Placement transform |
| `sources` | ✅ | `[{...}]` | Source datasets + citations |
| `license` | ✅ | `{ "spdx": "CC-BY-4.0", "text": "…" }` | Required |
| `processing` | ✅ | `{...}` | Pipeline, params, run IDs, etc. |
| `catalog_refs` | ✅ | `{ "stac_item": "...", "dcat_dataset": "...", "prov_activity": "..." }` | Cross-linking |

### Example manifest

```json
{
  "id": "ks-flint-hills--1850--dem-derived",
  "version": "1.0.0",
  "title": "Flint Hills Terrain (c. 1850)",
  "description": "Small terrain mesh for narrative visualization (Flint Hills region).",
  "asset": "./ks-flint-hills--1850--dem-derived--v1.0.0.glb",
  "preview": "./ks-flint-hills--1850--dem-derived--v1.0.0.preview.webp",

  "bbox_wgs84": [-96.9, 38.4, -96.2, 39.1],
  "crs_display": "EPSG:4326",
  "crs_source": "EPSG:26914",
  "vertical_datum": "unknown",
  "units": "meters",
  "up_axis": "Y",

  "anchor_wgs84": { "lon": -96.55, "lat": 38.77, "height_m": 420.0 },

  "transform": {
    "type": "ENU",
    "notes": "Model local origin is near anchor point; matrix places model in engine world-space.",
    "matrix4": [
      1, 0, 0, 0,
      0, 1, 0, 0,
      0, 0, 1, 0,
      0, 0, 0, 1
    ]
  },

  "sources": [
    {
      "name": "Example DEM Source",
      "type": "raster-dem",
      "citation": "USGS ...",
      "license": "Public Domain / ...",
      "url_or_id": "stac:item:usgs-dem-..."
    }
  ],

  "processing": {
    "pipeline": "kfm-terrain-mesh",
    "run_id": "2026-01-18T00:00:00Z__abc123",
    "commit": "abc123",
    "steps": [
      "clip_dem_to_bbox",
      "smooth_optional",
      "mesh_generate",
      "decimate",
      "uv_generate",
      "export_glb"
    ],
    "parameters": {
      "target_triangles": 250000,
      "vertical_exaggeration": 1.0
    }
  },

  "catalog_refs": {
    "stac_item": "stac:item:ks-flint-hills--1850--dem-derived--v1.0.0",
    "dcat_dataset": "dcat:dataset:ks-flint-hills--terrain",
    "prov_activity": "prov:activity:kfm-terrain-mesh__2026-01-18__abc123"
  }
}
```

> [!NOTE]
> The manifest is **not optional**. If we can’t explain how it was made and where it came from, we can’t responsibly render it in KFM. 🧾✅

---

## 🧭 Coordinate, scale, and georeferencing rules

Terrain GLBs are typically authored in a **local coordinate system** (easy to model, easy to decimate). The web engine must then place them correctly into **world space**.

Rules of thumb:
- ✅ Keep vertex units in **meters** (no “mystery scale”)
- ✅ Ensure consistent **up-axis** (`Y` for glTF)
- ✅ The **manifest must provide** a placement strategy (`anchor_wgs84` + `transform`)
- ✅ Record both:
  - `crs_source` (what the data was processed in)
  - `crs_display` (what the UI uses for placement & overlays)

> [!TIP]
> When in doubt, treat the GLB as **local geometry**, and treat the manifest as the **bridge** to geospatial truth.

---

## ⚡ Performance & LOD guidance

Terrain can get heavy fast. Keep it web-friendly:

- 🧊 Prefer **smaller coverage** + **better storytelling** over huge meshes
- 🪚 Decimate intelligently (preserve ridgelines / waterways / breaks)
- 🧵 Keep textures sane (avoid gigantic textures unless absolutely needed)
- 🧱 Consider LOD patterns when appropriate:
  - `LOD0` = close view
  - `LOD1` = mid
  - `LOD2` = far (optional)

> [!CAUTION]
> If adding a GLB noticeably slows initial page load or low-end GPUs, it’s too big for this folder.

---

## ➕ Adding a new terrain model

1. 🗺️ **Define the intent**
   - What story / focus moment needs this terrain?
   - What is the spatial + temporal scope?

2. 🧰 **Create the mesh**
   - Generate from DEM, lidar-derived surface, or hand-model (as appropriate)
   - Use a 3D tool (e.g., Blender) and keep the origin meaningful (local origin placement matters)

3. 🎨 **Export `.glb`**
   - Confirm scale in meters and axis orientation
   - Apply materials cleanly (don’t rely on engine hacks)

4. 🧾 **Write the manifest**
   - Include license + attribution
   - Include placement anchor + transform
   - Include processing steps and pipeline identifiers

5. 🧬 **Register provenance**
   - Ensure this terrain is represented in KFM’s catalog ecosystem (STAC/DCAT/PROV) with cross-links

6. 🧪 **Validate**
   - Run the QA checklist below

---

## 🧪 QA checklist

**Geometry & rendering**
- [ ] Model loads in the target web viewer without errors
- [ ] Correct orientation (not flipped / rotated unexpectedly)
- [ ] Correct scale (meters; no “giant Kansas” problem 😅)
- [ ] Normals look correct (no broken lighting)
- [ ] No obvious seams / holes / z-fighting

**Geospatial sanity**
- [ ] `bbox_wgs84` matches intended placement
- [ ] `anchor_wgs84` is inside the bbox
- [ ] Transform method documented and reproducible
- [ ] CRS + vertical datum recorded (or explicitly “unknown”)

**Governance**
- [ ] License included (SPDX where possible)
- [ ] Sources listed with citations/IDs
- [ ] No restricted/sensitive terrain published without governance review

---

## 🔗 Related KFM docs & standards

These are the “source of truth” references for how artifacts should move through KFM:

- 📘 `docs/MASTER_GUIDE_v13.md`
- 🧾 `docs/standards/KFM_STAC_PROFILE.md`
- 🧾 `docs/standards/KFM_DCAT_PROFILE.md`
- 🧾 `docs/standards/KFM_PROV_PROFILE.md`
- 🧩 `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- ⚖️ `docs/governance/ROOT_GOVERNANCE.md`
- 🧭 `docs/governance/SOVEREIGNTY.md`
- 🧠 `docs/governance/ETHICS.md`

---

### 🧷 Mini-glossary

- **GLB**: Binary glTF file (mesh + materials, optionally textures)
- **glTF**: Web-first 3D asset standard (Khronos)
- **CRS**: Coordinate Reference System (e.g., `EPSG:4326`)
- **DEM/DTM**: Elevation models (raster) often used to generate terrain meshes
- **LOD**: Levels of Detail (multiple mesh resolutions for performance)

✅ If you’re adding terrain: **make it fast, make it traceable, make it reproducible.**
