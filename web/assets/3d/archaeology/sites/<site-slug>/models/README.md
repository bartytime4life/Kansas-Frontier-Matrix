---
title: "🏺 Archaeology 3D Models — <site-slug>"
path: "web/assets/3d/archaeology/sites/<site-slug>/models/README.md"
status: "active"
version: "0.1.0"
last_updated: "2026-01-25"
owners:
  - "KFM (Kansas Frontier Matrix) — Archaeology/3D"
tags:
  - archaeology
  - 3d
  - cesium
  - 3d-tiles
  - gltf
  - provenance
  - fair-care
---

# 🏺 Archaeology 3D Models — `<site-slug>`

![status](https://img.shields.io/badge/status-active-brightgreen)
![scope](https://img.shields.io/badge/scope-site_models-blue)
![formats](https://img.shields.io/badge/formats-GLB%20%7C%203D%20Tiles-informational)
![governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-important)
![ui](https://img.shields.io/badge/viewers-MapLibre%20%2B%20Cesium-8A2BE2)

> **Goal:** Store **web-ready** 3D models (and their required metadata) for one archaeology site so the KFM UI can render them in **2D/3D mode** (MapLibre + Cesium), power **Story Nodes**, and keep everything **auditable** (provenance-first, sensitivity-aware). 🧾🗺️

---

## 🧭 Quick start

### ✅ This folder is for…
- **Published, web-consumable** 3D assets for this site:
  - `*.glb` (recommended for smaller, single-object models)
  - `3D Tiles` tilesets (recommended for large/streaming content like point clouds or city-scale reconstructions)
- A small, predictable set of **sidecar metadata files** (license, provenance, placement, previews).

### 🚫 This folder is NOT for…
- Raw photogrammetry outputs (`.rcproj`, huge `.obj`, full-res textures, raw point clouds)  
  → those belong in the **data intake / processing** side of the repo, then **export** to web-ready assets here.

> [!IMPORTANT]
> KFM is **evidence-first** and **governance-first**. If your model can’t be traced back to sources (and doesn’t respect sensitivity rules), it doesn’t ship. ✅

---

## 🧩 Site slug rules (`<site-slug>`)

Use a stable, URL-safe slug:
- ✅ `lowercase-kebab-case`
- ✅ prefer historically stable names (`oak-grove-mound-1`, `smoky-hill-village`)
- ✅ keep it short, no special chars
- ❌ avoid spaces, underscores, changing names, or “temp” slugs

---

## 📁 Directory layout (recommended)

> This layout is designed for: **static hosting**, **offline packs**, and **simple indexing**.

```text
📁 web/assets/3d/archaeology/sites/<site-slug>/models/
├─ 📄 README.md                         👈 you are here
├─ 📄 models.index.json                 👈 UI-facing index (required)
├─ 📄 models.schema-version.txt         👈 quick compatibility marker (recommended)
│
├─ 📁 <model-id>/
│  ├─ 🧱 model.glb                      👈 OR tileset.json (see below)
│  ├─ 🗺️ placement.json                 👈 where/how to place it (required for GLB)
│  ├─ 🧾 meta.json                      👈 model “data contract” (required)
│  ├─ 🧬 prov.jsonld                    👈 provenance (required)
│  ├─ ⚖️ LICENSE.txt                    👈 license + attribution (required)
│  ├─ 🖼️ preview.webp                   👈 thumbnail/hero (required)
│  ├─ 📸 screenshots/                   👈 optional extra views
│  └─ 🧊 lod/                           👈 optional LOD variants
│
└─ 📁 <tileset-id>/                     👈 3D Tiles package (if used)
   ├─ 🧩 tileset.json
   ├─ 📁 tiles/
   └─ (same sidecars: meta/prov/license/preview)
```

---

## 📦 Model package contract

### ✅ Required files (per model folder)

| File | Required | Purpose |
|---|---:|---|
| `meta.json` | ✅ | Minimum metadata (“data contract”) for UI, catalog, and governance |
| `prov.jsonld` | ✅ | Provenance trail (sources + processing steps) |
| `LICENSE.txt` | ✅ | License + attribution requirements |
| `preview.webp` | ✅ | Thumbnail / preview for catalog, story steps, popups |
| `model.glb` **or** `tileset.json` | ✅ | The asset itself |
| `placement.json` | ✅ (GLB) | Geo placement + orientation + scale for Cesium placement |
| `models.index.json` (root) | ✅ | Index of models for this site |

### 🧰 Optional (but strongly recommended)

| File/Folder | Why it helps |
|---|---|
| `screenshots/` | Better reviews + Story Node usage |
| `lod/` | Performance control across devices |
| `qa.json` | Validation output + budgets (triangles, textures, size) |
| `notes.md` | Field notes, reconstruction assumptions, uncertainties |

---

## 🗂️ `models.index.json` (UI-facing index)

This file is the “table of contents” for models at this site.

### Minimal example

```json
[
  {
    "id": "mound-a-scan-v1",
    "title": "Mound A — Photogrammetry Scan (v1)",
    "kind": "scan",
    "format": "glb",
    "path": "./mound-a-scan-v1/model.glb",
    "preview": "./mound-a-scan-v1/preview.webp",
    "meta": "./mound-a-scan-v1/meta.json",
    "prov": "./mound-a-scan-v1/prov.jsonld",
    "license": "./mound-a-scan-v1/LICENSE.txt",
    "placement": "./mound-a-scan-v1/placement.json",
    "time": { "start": "2024-06-01", "end": "2024-06-01" },
    "sensitivity": "restricted-location"
  }
]
```

### `kind` suggestions (keep it simple)
- `scan` 🧱 (photogrammetry / LiDAR-derived mesh)
- `reconstruction` 🏛️ (interpretive historical reconstruction)
- `artifact` 🏺 (portable object / museum item)
- `terrain` 🗻 (local DEM mesh / terrain cutout)
- `context` 🧭 (surrounding landscape / site context)

---

## 🧾 `meta.json` (model “data contract”)

KFM expects **structured metadata** so the UI can:
- show provenance (“map behind the map”),
- enforce sensitivity,
- filter by time,
- and let Focus Mode cite it cleanly.

### Suggested skeleton

```json
{
  "model_id": "mound-a-scan-v1",
  "site_slug": "<site-slug>",
  "title": "Mound A — Photogrammetry Scan (v1)",
  "summary": "High-resolution surface scan of Mound A captured during 2024 field season.",
  "kind": "scan",
  "created": "2024-06-01",
  "time": { "start": "2024-06-01", "end": "2024-06-01" },

  "spatial": {
    "display_geometry_policy": "generalized",
    "bbox_wgs84": [-99.0000, 38.0000, -98.9990, 38.0010]
  },

  "units": { "linear": "m" },

  "source": {
    "capture_method": "photogrammetry",
    "contributors": ["<name/team>", "<org>"],
    "equipment": ["<camera/drone/lidar>"]
  },

  "rights": {
    "license_spdx": "CC-BY-4.0",
    "attribution": "© <owner/org>, used under CC-BY 4.0"
  },

  "sensitivity": {
    "classification": "restricted-location",
    "reason": "Protects site integrity from looting/vandalism.",
    "release_policy": "public-geometry-generalized"
  },

  "links": {
    "story_nodes": ["story:<id-or-slug>"],
    "graph_entities": ["place:<id>", "site:<id>"]
  }
}
```

---

## 🗺️ `placement.json` (for GLB placement in Cesium)

Use this when you’re loading a plain `GLB` (not a 3D Tiles tileset).

```json
{
  "anchor": { "lng": -99.000123, "lat": 38.000456, "height_m": 0.0 },
  "orientation": { "heading_deg": 0, "pitch_deg": 0, "roll_deg": 0 },
  "scale": 1.0,
  "altitude_mode": "clampToGround",
  "notes": "If sensitivity requires, anchor may be generalized and exact placement handled server-side."
}
```

> [!NOTE]
> If the **location is sensitive**, do **not** commit precise anchors. Use generalized placement and rely on restricted access + server-side placement when needed. 🔐

---

## 🧠 Coordinate, CRS, and “don’t break alignment” rules

- **Display CRS:** WGS84 / EPSG:4326 (web standard)  
- **Track original CRS:** keep it in metadata/provenance (don’t lose science for convenience)
- **Units:** meters for elevation/scale whenever possible
- **Orientation:** document your “up” axis, and any correction rotations you apply during export

---

## ⏳ Time metadata is not optional

KFM treats **time as a first-class filter**:
- Reconstructions should declare the **represented time** (e.g., “circa 1850” or an explicit range).
- Scans should declare the **capture time**.

Use ISO 8601-like dates (`YYYY-MM-DD`) and ranges.

---

## 🔐 Sensitivity, ethics, and access control

Archaeology content often carries real-world risk. KFM’s UI and governance model expects you to classify and handle it responsibly:

### Common sensitivity patterns
- `public` ✅ (safe to show exact placement)
- `restricted-location` 🔐 (model may be shown, but location must be generalized)
- `restricted-content` 🛑 (model itself restricted, not just placement)
- `indigenous-sensitive` 🪶 (requires community guidance & CARE-aligned policy)

### Practical rules
- ✅ Prefer **generalized display geometry** for sites where disclosure creates risk.
- ✅ Keep a clear **reason** + **release policy** in `meta.json`.
- ✅ Ensure “no output is less restricted than its inputs” (don’t publish derived assets that leak restricted details).

> [!WARNING]
> Never publish exact coordinates, access paths, or “how to find it” hints for sensitive sites. This is a hard stop. 🛑

---

## 🧬 Provenance rules (evidence-first)

Every model must be traceable:
- what it came from (sources),
- how it was processed (tools + parameters),
- who did what,
- when it happened,
- and what uncertainty/assumptions exist (especially for reconstructions).

### Minimal provenance expectations
- **Source(s):** capture session logs, surveys, archival references
- **Processing:** cleanup/decimation steps, texture baking, compression
- **Outputs:** final GLB / 3D Tiles plus checksums

If you can’t explain it, **don’t ship it**.

---

## 🗺️ How the UI will use these models

### 2D + 3D
- **2D MapLibre** is the primary map experience
- **3D Cesium** is used when 3D adds value (terrain, structures, LiDAR, reconstructions)

### Story Nodes 🎬
Models should be easy to reference inside Story Node steps:
- each step can point at a model id from `models.index.json`
- the step can include a “fly to” camera + a model toggle

### Popups & provenance 🧾
Expect the UI to show:
- title, summary, preview,
- license + attribution,
- provenance links,
- sensitivity warnings / lock icons (when applicable)

---

## 🧰 Conversion & optimization tips (web reality check)

### GLB (good for single models)
- ✅ mesh decimation / LOD
- ✅ texture compression (KTX2/Basis if supported)
- ✅ Draco mesh compression where appropriate
- ✅ keep it lightweight for browsers + mobile

### 3D Tiles (good for big data)
- ✅ point clouds / LiDAR
- ✅ city-scale building models
- ✅ streaming LOD at zoom levels

> [!TIP]
> If a model is too large for the repo (or for static hosting), consider publishing it as a **signed artifact** (OCI/ORAS + provenance attachments) and referencing it from the catalog/index. 📦🔏

---

## ✅ “Definition of Done” checklist (per model)

- [ ] Model is **web-ready** (`.glb` or `3D Tiles`)
- [ ] `meta.json` completed (title, time, rights, sensitivity, spatial policy)
- [ ] `prov.jsonld` completed (sources + processing steps)
- [ ] `LICENSE.txt` includes attribution + license terms
- [ ] `preview.webp` present and representative
- [ ] `placement.json` present (**GLB only**) and respects sensitivity rules
- [ ] Entry added to `models.index.json`
- [ ] Story Node(s) updated (if applicable)
- [ ] Model reviewed for **location leakage** + **unintended details**
- [ ] Performance sanity check on a mid-range device (LOD/size ok)

---

## 🧱 Example model IDs (naming convention)

Use:  
`<feature>-<kind>-v<major>` or `<feature>-<kind>-<yyyymmdd>`

Examples:
- `mound-a-scan-v1`
- `village-core-reconstruction-v2`
- `burial-feature-artifact-20250110`

---

## 📚 Project docs this README aligns with

This folder’s rules are aligned with the project’s core docs on:
- provenance-first publishing, policy packs, and data intake
- 2D/3D UI design (MapLibre + Cesium, 3D Tiles)
- time filtering as a first-class concept
- Focus Mode governance + citations

Recommended reading in the repo/docs library:
- *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation*
- *KFM – Comprehensive Architecture, Features, and Design*
- *KFM – AI System Overview*
- *KFM – Comprehensive UI System Overview*
- *KFM – Data Intake – Technical & Design Guide*
- *Innovative Concepts to Evolve KFM*
- *Additional Project Ideas (artifact registries, provenance attachments)*
- *Comprehensive Markdown Guide (governance triggers, doc standards)*
- *Scientific Method / Master Coder Protocol (reproducibility + rigor)*
- Reference packs (PDF portfolios): AI concepts, data management, WebGL/archaeology, language/tooling resources

---

## 🆘 Troubleshooting

<details>
<summary><strong>Model loads but is rotated / upside down</strong></summary>

- Confirm axis conventions during export (Y-up vs Z-up).
- Apply a documented correction rotation and record it in `prov.jsonld` + `placement.json`.
</details>

<details>
<summary><strong>Model is too heavy / crashes mobile</strong></summary>

- Add LODs, reduce texture size, enable compression.
- Consider 3D Tiles for streaming.
- Consider external signed artifact storage (OCI/ORAS) for large binaries.
</details>

<details>
<summary><strong>Sensitivity concern: does this leak site location?</strong></summary>

- Remove precise anchors/coordinates.
- Use generalized geometry policy in `meta.json`.
- Ensure restricted content is not included in public builds or indices.
</details>

