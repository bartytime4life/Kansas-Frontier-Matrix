# 🏛️🧊 Site 3D Models (`.glb`) — KFM Web Assets

![format](https://img.shields.io/badge/format-GLB%20%28glTF%202.0%29-2ea44f)
![scope](https://img.shields.io/badge/scope-sites%20%7C%20places-blue)
![viewer](https://img.shields.io/badge/viewer-MapLibre%20%2B%20CesiumJS-purple)
![principle](https://img.shields.io/badge/principle-provenance--first-orange)
![governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-informational)

This folder contains **curated, web-deliverable** 3D site models in **binary glTF (`.glb`)** form. These are intended for **KFM’s web frontend** (React) where 2D/3D visualization is supported via **MapLibre (2D)** and **CesiumJS (3D)**, including opt-in 3D experiences (e.g., story-node moments like “Kansas From Above” showcasing terrain + a landmark model). 🗺️✨

> [!IMPORTANT]
> **Provenance-first rule:** If a model can show up in the UI, it must be **traceable** (sources + processing steps) and **licensed** for redistribution. No “mystery meshes.” 🧾🔍

---

## 🧭 Contents

- [📦 What belongs here](#-what-belongs-here)
- [🗂️ Recommended folder layout](#️-recommended-folder-layout)
- [🧾 Site model “asset contract”](#-site-model-asset-contract)
- [🌎 Geospatial alignment](#-geospatial-alignment)
- [🧬 Provenance & catalog integration](#-provenance--catalog-integration)
- [⚙️ Export & optimization guidelines](#️-export--optimization-guidelines)
- [✅ PR checklist](#-pr-checklist)
- [🆘 Troubleshooting](#-troubleshooting)
- [📚 Reference docs](#-reference-docs)

---

## 📦 What belongs here

✅ **Good fits**
- Small-to-medium **single-site** models used in:
  - Story nodes 🎬
  - A “focus” scene in Cesium/3D 🏔️
  - A side-panel model viewer 🧊
- **Curated** assets meant to ship with the web app (or be mirrored here for fast public delivery).

🚫 **Not a good fit**
- Raw photogrammetry outputs (hundreds of MB/GB) 📸🧱
- Massive region-scale 3D data (LiDAR point clouds, city meshes) 🏙️
  - Use **3D Tiles streaming** for large geospatial 3D content instead (Cesium-native approach).

---

## 🗂️ Recommended folder layout

Prefer **one folder per site** so metadata + previews stay co-located.

```text
📁 web/
└─ 📁 assets/
   └─ 📁 media/
      └─ 📁 models-3d/
         └─ 📁 glb/
            └─ 📁 sites/
               ├─ 📄 README.md
               ├─ 📁 monument-rocks/              🏞️ (example slug)
               │  ├─ 🧊 model.glb                 (required)
               │  ├─ 🖼️ preview.webp              (required)
               │  ├─ 🧾 meta.json                 (required)
               │  └─ 📚 sources.md                (recommended)
               └─ 📁 flint-hills-overlook/
                  ├─ 🧊 model.glb
                  ├─ 🖼️ preview.webp
                  ├─ 🧾 meta.json
                  └─ 📚 sources.md
```

> [!TIP]
> If you *must* keep a flat layout, keep the same contract with consistent naming:
> `site-slug.glb`, `site-slug.meta.json`, `site-slug.preview.webp`, etc.  
> Folder-per-site scales better. 📦➡️📁

---

## 🧾 Site model “asset contract”

Each site model **must** ship with:

### ✅ Required files
- `model.glb` 🧊  
  Binary glTF 2.0 model (prefer embedded textures).
- `preview.webp` 🖼️  
  UI thumbnail / poster image (fast to load; used in lists and cards).
- `meta.json` 🧾  
  Machine-readable metadata + provenance hooks.

### 👍 Strongly recommended
- `sources.md` 📚  
  Human-readable provenance narrative + citations (good for review, auditing, and story writing).

### Optional (only when needed)
- `lod/` 🪜  
  LOD variants (e.g., `lod0.glb`, `lod1.glb`, `lod2.glb`) for performance tiers.
- `collision.glb` 🧱  
  Simplified collider mesh if the viewer needs it.
- `notes.md` 📝  
  Modeling notes, known quirks, and post-processing decisions.

---

## 🧾 `meta.json` schema (minimal but opinionated)

KFM’s broader system is designed to treat artifacts as **governed, traceable** objects. For site models, `meta.json` is the *minimum* contract the web app and API layer can rely on.

### ✅ Required fields

```json
{
  "id": "urn:kfm:site-model:monument-rocks",
  "slug": "monument-rocks",
  "title": "Monument Rocks (Chalk Pyramids)",
  "description": "Reality-based surface model for public viewing and educational storytelling.",
  "asset": {
    "type": "model/gltf-binary",
    "path": "model.glb",
    "preview": "preview.webp"
  },
  "geospatial": {
    "crs_display": "EPSG:4326",
    "origin_wgs84": { "lon": -100.0, "lat": 39.0, "elev_m": 0 },
    "units": "meters",
    "axis": "Y-up",
    "local_origin_hint": "Model coordinates are local; UI positions using origin + transform."
  },
  "provenance": {
    "sources": [
      {
        "kind": "photogrammetry|lidar|survey|archive",
        "citation": "…",
        "license": "…",
        "retrieved": "YYYY-MM-DD"
      }
    ],
    "processing_steps": [
      { "step": "reconstruction", "tool": "…", "version": "…", "notes": "…" },
      { "step": "alignment", "tool": "…", "version": "…", "notes": "…" },
      { "step": "optimization", "tool": "…", "version": "…", "notes": "…" }
    ]
  },
  "governance": {
    "visibility": "public|restricted",
    "care_label": "Public|Sensitive",
    "attribution": "…"
  },
  "version": "v1.0.0",
  "last_updated": "YYYY-MM-DD"
}
```

> [!NOTE]
> The values above are examples. **Do not publish sensitive coordinates** for protected locations. Use generalized origins and/or restricted visibility when required. 🛡️

---

## 🌎 Geospatial alignment

KFM’s web display standard emphasizes **WGS84 / EPSG:4326** for consistency on the web (while still tracking original CRS in metadata). For 3D models, we follow the same spirit:

### 🎯 Rules of thumb
- Keep model coordinates **local** (small numbers) to avoid floating precision issues in 3D rendering engines.
- Record **where** and **how** to place the model in the world via metadata:
  - `origin_wgs84` (anchor point)
  - optional `transform` (rotation/scale/offset)
- Always state **units** (use meters as the default web/3D standard).
- Avoid non-uniform scale when possible; it can cause shading/normal issues in WebGL pipelines.

### Optional: explicit transform
If your viewer needs deterministic placement:

```json
{
  "geospatial": {
    "origin_wgs84": { "lon": -100.0, "lat": 39.0, "elev_m": 0 },
    "transform": {
      "rotation_euler_deg": [0, 0, 0],
      "scale": 1.0,
      "offset_local_m": [0, 0, 0]
    }
  }
}
```

---

## 🧬 Provenance & catalog integration

KFM is built around **traceability**:
- Users should be able to inspect **sources** and **processing steps**.
- Artifacts should be **cataloged** and **governed**, not just dropped into a folder.

### ✅ Minimum (for this folder)
- `meta.json` includes sources + processing steps.
- `sources.md` narrates provenance with citations.

### ⭐ Preferred (system-wide best practice)
For official/public datasets, also create/attach:
- **STAC item** (describing the asset + spatial/temporal scope)
- **DCAT entry** (dataset-level catalog metadata)
- **PROV** record (who/what/when/how produced the derived model)

This aligns with the project’s lifecycle: *ingest → process → validate → catalog → graph → API → UI*. 🧠🔗

#### Example: STAC asset stub (illustrative)
```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "site-model-monument-rocks",
  "properties": {
    "title": "Monument Rocks — Site Model",
    "datetime": "YYYY-MM-DDT00:00:00Z"
  },
  "geometry": { "type": "Point", "coordinates": [-100.0, 39.0] },
  "assets": {
    "model": {
      "href": "/assets/media/models-3d/glb/sites/monument-rocks/model.glb",
      "type": "model/gltf-binary",
      "roles": ["data"]
    },
    "preview": {
      "href": "/assets/media/models-3d/glb/sites/monument-rocks/preview.webp",
      "type": "image/webp",
      "roles": ["thumbnail"]
    }
  }
}
```

> [!IMPORTANT]
> If a model is a *true evidence artifact*, the canonical record should exist in the governed data/cat/prov system (STAC/DCAT/PROV), even if the web app serves a copy from `web/assets/…`. ✅

---

## ⚙️ Export & optimization guidelines

These are practical defaults for web delivery (especially for opt-in 3D scenes).

### 🧱 Geometry budget (guideline)
- Prefer clean topology; remove hidden/internal faces.
- Target “fast to stream”:
  - fewer draw calls
  - reasonable triangle count
  - compressed textures where possible

### 🖼️ Textures
- Prefer a single texture atlas when feasible.
- Keep textures power-of-two (e.g., 1024, 2048).
- Use Web-friendly formats (WebP / KTX2) depending on pipeline.

### 🧭 Orientation & scale
- Apply transforms (especially scale) before export to reduce surprises in lighting and normals.
- Verify in a viewer after export (Cesium + any secondary validator).

### 🧪 QA sanity checks
- No missing textures/materials
- Correct pivot/origin assumptions
- Preview image matches model
- `meta.json` passes any schema validation used by the API/UI

---

## ✅ PR checklist

When adding/updating a model, your PR should include:

- [ ] 🧊 `model.glb` added/updated
- [ ] 🖼️ `preview.webp` added/updated
- [ ] 🧾 `meta.json` complete (id/slug/title + geospatial + provenance)
- [ ] 📚 `sources.md` includes human-readable citations (recommended)
- [ ] 🧭 Placement validated in the viewer (2D/3D context where applicable)
- [ ] 🧪 Asset loads on a “mid-tier” device without choking (basic perf sanity)
- [ ] 🛡️ Governance tags set correctly (public vs restricted; CARE label if needed)

---

## 🆘 Troubleshooting

### “Model looks too dark / lighting is weird”
- Check normals and whether you exported with unapplied transforms.
- Avoid non-uniform scaling unless you know your renderer handles normal matrices correctly.

### “It loads locally but not in production”
- Check path casing (case-sensitive on many servers).
- Confirm MIME types are served correctly for `.glb`.
- Confirm the web build pipeline copies these files to the correct output directory.

### “Model is huge / slow”
- Consider LODs (`lod/`) and/or shifting to a 3D Tiles pipeline for streaming if it’s truly geospatial-scale.

---

## 📚 Reference docs

These project docs informed conventions used here (provenance-first, governed artifacts, 2D/3D web stack, and GIS-integrated 3D workflows):

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**
- 🧭 **KFM Markdown / Data Lifecycle Guide (STAC + DCAT + PROV alignment)**
- 🏺 **Archaeological 3D GIS** (practical workflows for georeferenced 3D meshes + database linkage)
- ✍️ **Comprehensive Markdown Guide** (governed docs, YAML front-matter, provenance in documentation)

---
