# 🧩 Shared 3D Assets  
**Path:** `web/assets/3d/shared/`

![viewer](https://img.shields.io/badge/viewer-MapLibre%20%2B%20CesiumJS-informational)
![formats](https://img.shields.io/badge/formats-glTF%20%7C%203D%20Tiles%20%7C%20PNG%2FJPEG-blue)
![scope](https://img.shields.io/badge/scope-shared%20assets-success)
![docs](https://img.shields.io/badge/docs-living%20README-orange)

> [!IMPORTANT]
> **This folder is for _shared, reusable_ 3D “UI-shipped” assets.**  
> If an asset is **evidence-bearing** (historic reconstruction, scanned artifact mesh, LiDAR-derived surface, etc.), it should follow the **data pipeline + catalogs** (STAC/DCAT/PROV) and be served via governed APIs/tiles—not quietly embedded in the UI.

---

## 🧭 What lives here

✅ **Good fits** for `web/assets/3d/shared/`:
- **Reusable glTF/GLB models** used across multiple scenes (markers, UI props, measurement gizmos, “orientation” helpers).
- **Textures** (PNG/JPEG) used by those models (atlases, decals, patterns).
- **Shared shaders/material snippets** (if your frontend build allows it).
- **Thumbnails/posters** for UI previews.
- A **manifest/registry** so the app can load assets by ID (instead of hard-coded paths).

🚫 **Not** a good fit:
- “Official” **dataset outputs** (3D Tiles for terrain/buildings, point clouds, photogrammetry captures) that belong to `data/processed/…` and catalogs.
- Story-specific media (belongs under `docs/reports/story_nodes/<story>/assets/`).
- Anything with unclear license/provenance.

---

## 🧱 Relationship to the KFM stack

KFM’s web UI typically includes:
- **MapLibre (2D)** and **CesiumJS (3D)** viewers
- **3D Tiles** for streamed geospatial 3D content

This folder is the **shared, static** asset layer used by the web app—not the governed data catalog.

---

## 🗂️ Suggested folder layout

> [!NOTE]
> You can evolve this structure, but keep **stable asset IDs** and avoid renaming paths casually.

```text
web/assets/3d/shared/
├── 📁 models/
│   ├── 📁 glb/                 # Small, UI-shipped models (binary glTF)
│   └── 📁 tilesets/            # Tiny dev/demo tilesets only (NOT “official” data)
├── 📁 textures/
│   ├── 📁 png/                 # Alpha, masks, crisp UI decals
│   ├── 📁 jpg/                 # Photographic/albedo where alpha not needed
│   └── 📁 atlases/             # Texture atlases (optional)
├── 📁 shaders/                 # Optional: shared shader snippets
├── 📁 thumbnails/              # UI previews / posters
├── 📁 meta/                    # Asset contracts / provenance sidecars
└── 📄 assets.manifest.json     # Registry: assetId → file(s) + metadata pointers
```

---

## 🏷️ Naming conventions

**Goal:** predictable imports + grep-friendly IDs + stable URLs.

### File & folder names
- Use **kebab-case**: `prairie-grass.glb`, `wagon-wheel.glb`
- Avoid spaces and “final_FINAL_v2” naming.
- Prefer **explicit type hints** in the name when it helps:
  - `marker-arrow.glb`, `ui-compass.glb`, `decal-trail-dots.png`

### Asset IDs
Use an ID that’s stable across refactors:

- `shared/<category>/<slug>`
  - Examples:
    - `shared/ui/marker-arrow`
    - `shared/ui/compass`
    - `shared/props/wagon-wheel`

---

## 📦 Supported asset types

### 1) glTF / GLB models (recommended for UI-shipped models)
- Prefer **`.glb`** for a single-file artifact.
- Keep models **lightweight** and “web-first”.

**Recommended minimum per model:**
- `models/glb/<slug>.glb`
- `meta/<slug>.asset.json`
- `thumbnails/<slug>.png` (or `.jpg`) optional but strongly encouraged

### 2) 3D Tiles tilesets (use sparingly here)
If you keep **tiny** demo tilesets for local dev:
- `models/tilesets/<slug>/tileset.json`
- `meta/<slug>.asset.json`

> [!WARNING]
> **Do not stash “real” 3D Tiles datasets here** to bypass governance/catalog requirements.

### 3) Textures (PNG/JPEG)
General guidance:
- **PNG**: alpha, masks, crisp edges, UI decals
- **JPEG**: photographic textures where alpha isn’t needed, smaller file sizes

---

## 🧾 Asset contracts and provenance

KFM is contract-first / provenance-first—**even for UI assets**.  
Every shared asset should have a minimal metadata sidecar:

### `meta/<slug>.asset.json` (example)

```json
{
  "schemaVersion": "1.0.0",
  "id": "shared/ui/marker-arrow",
  "title": "Marker Arrow",
  "type": "ui-model",
  "format": "glb",
  "files": {
    "model": "models/glb/marker-arrow.glb",
    "thumbnail": "thumbnails/marker-arrow.png",
    "textures": [
      "textures/png/marker-arrow-albedo.png"
    ]
  },
  "license": {
    "spdx": "CC0-1.0",
    "attribution": null
  },
  "provenance": {
    "source": "Internal",
    "creator": "KFM Team",
    "createdAt": "2026-01-14",
    "processing": [
      "Modeled in Blender",
      "Exported as GLB",
      "Texture atlas baked"
    ]
  },
  "notes": "Reusable UI arrow marker for map and 3D scenes."
}
```

> [!TIP]
> If an asset is derived from external sources (scans, imagery, museum collections, etc.), **put real attribution + license here** (and store deeper provenance in the governed catalogs where appropriate).

---

## 🧭 Coordinate systems, scale, and “why is my model gigantic?” 😅

### UI-shipped models
- Establish a project convention (example: **meters**).
- Keep pivots/origins consistent (e.g., base at ground, centered).

### Geospatial models (if ever referenced here)
- Be explicit in metadata about:
  - CRS / reference frame
  - vertical datum assumptions
  - units and scaling

> [!NOTE]
> If a model must be placed on the globe (Cesium), treat it like governed data: validate placement logic, document assumptions, and prefer streaming formats when large.

---

## 🚀 Performance checklist (WebGL/Cesium reality)

3D on the web is constrained by:
- GPU memory bandwidth
- texture sizes
- draw calls
- mobile thermal throttling

### ✅ Recommended optimization moves
- Reduce polygon count where it’s not visually meaningful
- Bake details into textures (normal maps) where appropriate
- Prefer texture atlases over many tiny textures
- Keep texture dimensions reasonable (use power-of-two when possible)
- Provide a thumbnail/poster so the UI can show “loading” states gracefully

> [!IMPORTANT]
> **If the UI gets slow after adding an asset, treat it as a regression.**  
> Asset work is performance work.

---

## ➕ How to add a new shared asset

### Step 1 — Decide where it belongs
Use this quick decision table:

| If the asset is… | Put it in… |
|---|---|
| A reusable UI prop/model | ✅ `web/assets/3d/shared/` |
| Story-specific media | `docs/reports/story_nodes/<story>/assets/` |
| Evidence-bearing / data product | `data/processed/...` + STAC/DCAT/PROV + API/tiles |
| Experimental prototype | `mcp/experiments/...` |

### Step 2 — Add files
- `models/glb/<slug>.glb`
- `meta/<slug>.asset.json`
- `thumbnails/<slug>.png` (recommended)
- textures under `textures/png|jpg/...`

### Step 3 — Register in the manifest
Update `assets.manifest.json` so code loads by ID.

```json
{
  "schemaVersion": "1.0.0",
  "assets": [
    {
      "id": "shared/ui/marker-arrow",
      "meta": "meta/marker-arrow.asset.json"
    }
  ]
}
```

### Step 4 — Verify in both viewers (when relevant)
- Check in **MapLibre** (if used as a marker/overlay)
- Check in **Cesium** (if used in 3D context)

### Step 5 — PR checklist
- ✅ Asset has metadata contract
- ✅ License/provenance is clear
- ✅ Performance impact reviewed
- ✅ Thumbnail included (or explicitly not needed)

---

## 🔐 Security & licensing (non-negotiable)

- **Never** add assets with unclear rights or unknown origin.
- Prefer assets with clear licenses (and record them in metadata).
- Treat all third-party files as **untrusted inputs** during pipeline steps.

> [!CAUTION]
> This repository is public-facing by design. Assume anything committed can be redistributed.

---

## ✅ PR Review Checklist

- [ ] Asset files are in the correct folder
- [ ] `meta/<slug>.asset.json` exists and is complete
- [ ] `assets.manifest.json` updated (if applicable)
- [ ] Texture formats are appropriate (PNG vs JPEG)
- [ ] Thumbnails included (unless not applicable)
- [ ] No copyrighted/uncleared assets
- [ ] Performance impact considered (especially mobile)
- [ ] No “hidden dataset” slipped into `web/`

---

## 📚 Project Library & Reference Shelf (all project files)

> [!NOTE]
> These references are part of the project’s shared knowledge base—use them to keep assets **fast**, **traceable**, **well-designed**, and **governed**.

<details>
<summary><strong>🗺️ KFM Architecture, Governance, Docs</strong></summary>

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf  
- Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf  
- MARKDOWN_GUIDE_v13.md.gdoc  
- Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx  
- Introduction to Digital Humanism.pdf  
- On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf  
- Principles of Biological Autonomy - book_9780262381833.pdf  

</details>

<details>
<summary><strong>🧠 3D, WebGL, Web UX</strong></summary>

- webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf  
- responsive-web-design-with-html5-and-css3.pdf  
- compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf  

</details>

<details>
<summary><strong>🌍 GIS, Cartography, Remote Sensing, 3D GIS</strong></summary>

- python-geospatial-analysis-cookbook.pdf  
- Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf  
- making-maps-a-visual-guide-to-map-design-for-gis.pdf  
- Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf  
- Archaeological 3D GIS_26_01_12_17_53_09.pdf  
- PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf  

</details>

<details>
<summary><strong>📈 Stats, ML, and Analytics (for QC + performance modeling)</strong></summary>

- regression-analysis-with-python.pdf  
- Regression analysis using Python - slides-linear-regression.pdf  
- Understanding Statistics & Experimental Design.pdf  
- think-bayes-bayesian-statistics-in-python.pdf  
- graphical-data-analysis-with-r.pdf  
- Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf  

</details>

<details>
<summary><strong>⚙️ Simulation, Optimization, Graphs (R&amp;D asset generation + analysis)</strong></summary>

- Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf  
- Generalized Topology Optimization for Structural Design.pdf  
- Spectral Geometry of Graphs.pdf  

</details>

<details>
<summary><strong>🗄️ Data Systems &amp; Performance</strong></summary>

- Database Performance at Scale.pdf  
- Scalable Data Management for Future Hardware.pdf  
- Data Spaces.pdf  
- concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf  

</details>

<details>
<summary><strong>🛡️ Security Awareness (defensive use only)</strong></summary>

- ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf  
- Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf  

</details>

<details>
<summary><strong>📚 Programming Compendiums (A–X)</strong></summary>

- A programming Books.pdf  
- B-C programming Books.pdf  
- D-E programming Books.pdf  
- F-H programming Books.pdf  
- I-L programming Books.pdf  
- M-N programming Books.pdf  
- O-R programming Books.pdf  
- S-T programming Books.pdf  
- U-X programming Books.pdf  

</details>

---

## 🧭 Roadmap ideas (optional)

- Add a JSON Schema for `*.asset.json` contracts
- Add an automated “asset lint” check in CI (missing license, missing thumbnail, oversized textures, etc.)
- Add an asset preview page in the web app for fast visual QA
- Introduce lightweight LOD rules for shared models

---
