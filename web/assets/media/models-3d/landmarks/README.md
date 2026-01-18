---
title: "🏛️ Landmarks · 3D Models Asset Pack"
version: "v1.0.0"
status: "active"
doc_kind: "Asset Directory README"
last_updated: "2026-01-18"
path: "web/assets/media/models-3d/landmarks/README.md"
doc_uuid: "urn:kfm:doc:assets:models-3d:landmarks:readme:v1.0.0"
---

# 🗿 Landmarks (3D) — `web/assets/media/models-3d/landmarks/`

![glTF](https://img.shields.io/badge/format-glTF%202.0%20%2F%20GLB-5c2d91)
![Cesium](https://img.shields.io/badge/viewer-CesiumJS-2b579a)
![WGS84](https://img.shields.io/badge/geo-EPSG%3A4326%20(WGS84)-0078d7)
![Provenance](https://img.shields.io/badge/principle-provenance--first-success)

> ✅ **Purpose:** Curated, *runtime-ready* 3D landmark models used by the KFM web client (e.g., Focus Mode stories + map viewers).  
> 📌 **Scope:** “Landmarks” = discrete 3D objects (buildings, monuments, formations, artifacts) suitable for interactive web rendering.

---

## 🧭 Quick Nav

- [What belongs here](#-what-belongs-here)
- [Folder & naming conventions](#-folder--naming-conventions)
- [Asset format & quality targets](#-asset-format--quality-targets)
- [Georeferencing & coordinate rules](#-georeferencing--coordinate-rules)
- [Metadata, licensing, provenance](#-metadata-licensing-provenance)
- [How the web app uses these](#-how-the-web-app-uses-these)
- [Add a new landmark](#-add-a-new-landmark)
- [PR checklist](#-pr-checklist)
- [References](#-references)

---

## 📦 What belongs here

### ✅ Yes (in-scope)
- **Small-to-medium 3D assets** that can be shipped as static web media:
  - `*.glb` (preferred)
  - `*.gltf` (+ external textures) if needed
- **Supporting files** that make the asset usable + auditable:
  - a thumbnail/preview (`thumbnail.webp` / `preview.webp`)
  - metadata sidecar(s) (see [Metadata, licensing, provenance](#-metadata-licensing-provenance))
  - attribution/license text

### 🚫 No (out-of-scope)
- **Raw source projects**: `.blend`, `.psd`, raw photogrammetry projects, raw LiDAR, etc.
- **Massive 3D geospatial tilesets** (use streaming via 3D Tiles elsewhere).
  - KFM’s web stack uses CesiumJS and the **open 3D Tiles standard** to stream large 3D geospatial content (LiDAR point clouds, building models, etc.). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

> 💡 Rule of thumb:  
> **If it must stream** → 3D Tiles.  
> **If it can bundle** → put it here.

---

## 🗂️ Folder & naming conventions

### 📁 Canonical layout (per landmark)

Each landmark gets its own **kebab-case** folder:

```text
web/assets/media/models-3d/landmarks/
  monument-rocks/
    model.glb
    thumbnail.webp
    landmark.meta.json
    LICENSE.txt
    SOURCES.md
  keeper-of-the-plains/
    model.glb
    thumbnail.webp
    landmark.meta.json
    LICENSE.txt
    SOURCES.md
```

### 🧩 File naming rules
- Folder name = **stable landmark id** (kebab-case)
- Prefer:
  - `model.glb`
  - `thumbnail.webp` (or `thumbnail.png` if needed)
  - `landmark.meta.json` (required)
- Optional variants:
  - `model.lod0.glb`, `model.lod1.glb` for LOD packs
  - `textures/` if using non-embedded textures (`.gltf` workflow)

---

## 🎛️ Asset format & quality targets

### ✅ Preferred export
- **glTF 2.0 Binary**: `GLB` (single-file deployment, easier caching, fewer missing-texture surprises)

### 🧼 Mesh hygiene (minimum bar)
- Correct normals + tangents (no “inside-out” shading)
- No obvious holes / broken UVs / missing materials
- Avoid extreme geometric redundancy that harms import/render performance  
  (parameter choices during mesh generation/export matter a lot). [oai_citation:1‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

### 🧠 Reality-based vs interpretive
We explicitly label model intent:

- **reality-based** (photogrammetry/LiDAR capture)  
- **interpretive** (reconstruction / hypothetical model) [oai_citation:2‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

And we treat transparency as non-negotiable: models remain trustworthy when we can reconstruct **how** they were made, in context. [oai_citation:3‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

---

## 🧭 Georeferencing & coordinate rules

### 🌍 Display CRS standard
- KFM’s internal display standard is **WGS84 / EPSG:4326** for web consistency, while tracking original CRS in metadata. [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 📐 Coordinate + units guidance
- Store landmark placement in metadata as:
  - `lat`, `lon` (EPSG:4326)
  - optional `alt_m` (meters, if known / needed)
- Store transform separately from geometry:
  - `heading_deg`, `pitch_deg`, `roll_deg`
  - `scale`

> Why? A single GLB may be reused across contexts (different “presentation” transforms) without re-exporting the mesh.

---

## 🧾 Metadata, licensing, provenance

### 🔒 Non-negotiable principle
KFM is **contract-first + provenance-first**: anything shown in the UI must be traceable to cataloged sources and provable processing; unsourced “mystery layers” are not permitted. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

That applies to 3D landmark assets too.

### ✅ Required files per landmark
| File | Required | What it does |
|------|:-------:|--------------|
| `landmark.meta.json` | ✅ | The “data contract” for this model (source, license, location, processing steps, etc.). [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) |
| `LICENSE.txt` | ✅ | The license terms for the model + textures (or a pointer to the upstream license). |
| `SOURCES.md` | ✅ | Human-readable attribution + acquisition notes + links to primary sources. |

### 🧾 `landmark.meta.json` recommended schema (example)

```json
{
  "id": "monument-rocks",
  "title": "Monument Rocks",
  "model_kind": "reality-based",
  "format": "model/gltf-binary",
  "display_crs": "EPSG:4326",
  "location": { "lat": 0.0, "lon": 0.0, "alt_m": null },
  "transform": { "heading_deg": 0, "pitch_deg": 0, "roll_deg": 0, "scale": 1.0 },
  "sources": [
    {
      "title": "Primary source name",
      "license": "CC-BY-4.0 (example)",
      "url": "https://example.org/source",
      "accessed": "YYYY-MM-DD"
    }
  ],
  "provenance": {
    "pipeline_summary": "capture -> mesh cleanup -> retopo/decimate -> bake -> export -> optimize",
    "tools": [
      { "name": "Blender", "version": "X.Y.Z" },
      { "name": "gltfpack", "version": "X.Y.Z" }
    ],
    "inputs": [
      { "kind": "photos", "ref": "stac://..." },
      { "kind": "pointcloud", "ref": "stac://..." }
    ],
    "notes": "Include any assumptions, reconstruction choices, and QC notes."
  }
}
```

> 🧩 Tip: If you’re already registering artifacts in STAC/DCAT/PROV catalogs (recommended), `landmark.meta.json` can either *be* a STAC Item or map cleanly into one. [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧑‍💻 How the web app uses these

- The KFM web frontend lives under `web/` and includes:
  - MapLibre GL JS for **2D maps**
  - CesiumJS for **3D globe/terrain + 3D viewing** [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM can transition into 3D contexts for narrative “wow + insight” moments (e.g., “Kansas From Above”), potentially focusing on a landmark like **Monument Rocks** with a 3D model. [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 🎥 Camera basics (for previews)
If you’re generating thumbnails or scripted fly-ins, remember: a stable camera definition needs:
- eye point, look-at point, and “up” direction. [oai_citation:10‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)

---

## ➕ Add a new landmark

### 1) Create the folder
```text
web/assets/media/models-3d/landmarks/<landmark-id>/
```

### 2) Drop in the model + preview
- `model.glb`
- `thumbnail.webp`

### 3) Write metadata + sources (required)
- `landmark.meta.json`
- `SOURCES.md`
- `LICENSE.txt`

### 4) Validate & sanity-check
- Open in your local viewer (Cesium / three.js / Blender)
- Confirm:
  - textures load
  - normals look right
  - scale feels plausible
  - metadata is complete and license is explicit

### 5) Register in catalogs (recommended)
KFM treats catalogs/contracts as first-class artifacts (STAC/DCAT/PROV). [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
If your pipeline includes STAC registration, add/update the relevant `data/stac/...` entries (see repo layout conventions). [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ✅ PR checklist

- [ ] Folder name is kebab-case + stable id
- [ ] `model.glb` loads correctly (no missing textures)
- [ ] `thumbnail.webp` renders well and is representative
- [ ] `landmark.meta.json` complete (source + license + location + pipeline steps)
- [ ] `SOURCES.md` includes attribution + acquisition context
- [ ] `LICENSE.txt` is present and legally compatible
- [ ] If interpretive: reconstruction choices + confidence notes are explicit [oai_citation:13‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
- [ ] No “mystery” assets (everything is provenance-linked) [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📚 References

Project & standards docs used to shape this README:

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- MARKDOWN_GUIDE v13 (repo governance + catalogs + structure)  [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Archaeological 3D GIS (model provenance, capture/processing pipeline lessons)  [oai_citation:17‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
- WebGL Programming Guide (camera conventions for web rendering)  [oai_citation:18‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)
