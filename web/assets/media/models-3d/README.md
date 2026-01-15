# 🧱 `web/assets/media/models-3d/` — Web-Ready 3D Models

![KFM](https://img.shields.io/badge/KFM-Web%20Assets-2b6cb0?style=flat-square)
![3D](https://img.shields.io/badge/3D-Cesium%20%7C%20WebGL-1f2937?style=flat-square)
![Streaming](https://img.shields.io/badge/Streaming-3D%20Tiles%20Friendly-111827?style=flat-square)
![Governance](https://img.shields.io/badge/Governance-STAC%20%2B%20DCAT%20%2B%20PROV-065f46?style=flat-square)

This folder is the **frontend-shippable 3D media bin** for Kansas Frontier Matrix (KFM): small, curated 3D models that can be loaded directly by the web UI when appropriate.  
KFM’s frontend is designed for browser-based access using standard web technologies [oai_citation:0‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H), and its UI stack includes **MapLibre (2D)** + **CesiumJS (3D)**, using the **open 3D Tiles standard** to stream geospatial 3D when needed [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi).

> [!IMPORTANT]
> **Not everything belongs here.**  
> - ✅ **Good here:** lightweight models used as UI media (landmarks, “story props”, demos, small annotated artifacts).  
> - ❌ **Not here:** big/streamed geospatial datasets (LiDAR point clouds, city-scale buildings, terrain meshes) → those should ship as **3D Tiles** (or similar) via KFM’s governed data pipeline [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi).

---

## 🧭 Quick Links

- [✅ What belongs here](#-what-belongs-here)
- [🗂️ Recommended folder layout](#️-recommended-folder-layout)
- [📦 Formats & conventions](#-formats--conventions)
- [🛰️ Georeferencing & CRS rules](#️-georeferencing--crs-rules)
- [🧾 Metadata & provenance requirements](#-metadata--provenance-requirements)
- [⚡ Performance budgets](#-performance-budgets)
- [🔍 PR checklist](#-pr-checklist)
- [📚 References](#-references)

---

## ✅ What belongs here

### ✅ Include
- **Small GLB models** used directly in the web UI (e.g., a landmark model used inside a story step).
- **UI-adjacent 3D media**: educational models, illustrative reconstructions, small “focus mode” visuals.
- **Demo/preview assets** for developing the 3D viewer pipeline.

### ❌ Exclude
- **Massive 3D datasets** intended for streaming and progressive loading → use **3D Tiles** pipelines and serve via Cesium-friendly endpoints [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi).
- **Voxel volumes** or extremely heavy representations unless explicitly justified (voxel representations can require large storage and are costly for web delivery) [oai_citation:4‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2).
- Source project files (e.g., `.blend`, raw scans) unless you’re intentionally shipping them (usually: don’t).

---

## 🗂️ Recommended folder layout

> Keep models discoverable, self-contained, and “diff-friendly”. One model = one folder.

```text
📁 web/
  📁 assets/
    📁 media/
      📁 models-3d/
        📄 README.md
        📄 models.index.json              (optional manifest for UI)
        📁 landmarks/
          📁 monument_rocks/
            🧊 monument_rocks.glb
            🧾 monument_rocks.meta.json
            🖼️ monument_rocks.thumb.webp
        📁 artifacts/
          📁 buffalo_skull_demo/
            🧊 buffalo_skull_demo.glb
            🧾 buffalo_skull_demo.meta.json
            🖼️ buffalo_skull_demo.thumb.webp
        📁 ui/
          📁 compass_marker/
            🧊 compass_marker.glb
            🧾 compass_marker.meta.json
```

---

## 📦 Formats & conventions

### Preferred formats
| Format | Use | Notes |
|---|---:|---|
| **`.glb`** ✅ | Web shipping | Single-file (mesh + materials + textures). Great for bundling & caching. |
| `.gltf` ⚠️ | Web shipping | Multi-file (references external textures/buffers). Use only when needed. |
| `.3dtiles` / tileset.json ✅ | Streaming geospatial | Use when shipping **true geospatial 3D** (terrain/LiDAR/buildings). Cesium/3D Tiles friendly [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi). |

### Naming
KFM emphasizes consistent naming and **lower_case_with_underscores** for files and folders [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi).

**Folder:** `lower_case_with_underscores/`  
**Files:** `same_as_folder.(glb|meta.json|thumb.webp)`

Example:
```text
📁 monument_rocks/
  🧊 monument_rocks.glb
  🧾 monument_rocks.meta.json
  🖼️ monument_rocks.thumb.webp
```

---

## 🛰️ Georeferencing & CRS rules

KFM’s internal web-facing standard is **WGS84 (EPSG:4326)** for alignment in the web map, while still tracking the original CRS in metadata [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi).

### If the model is **geospatial** (placed on the globe / terrain)
- ✅ Include original CRS + transform details in metadata.
- ✅ Provide a **WGS84-aligned** placement path (or explicit conversion notes).
- ✅ Prefer streaming as **3D Tiles** when it’s more than a one-off object [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi).

### If the model is **non-geospatial** (local coordinates / “object viewer”)
- ✅ Specify units (meters recommended), “up” axis (Y-up typical), and scale factor in metadata.
- ✅ Treat it as media: still provenance-linked, but not map-projected.

---

## 🧾 Metadata & provenance requirements

KFM is contract-first and provenance-first: content is expected to be traceable and governed [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU).  
KFM’s policy requires **STAC/DCAT/PROV alignment** for new datasets or evidence artifacts, with CI validation against defined profiles [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU). Additionally, KFM’s invariants state **“Provenance first”** before graph/UI use [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU).

> [!NOTE]
> This folder is “web assets”, but **models used as evidence** (story/focus content) should still be treated as governed artifacts: **cataloged + licensed + provenance-linked** [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU).

### ✅ Required sidecar: `*.meta.json`
Every model in this folder must include a `*.meta.json` that captures **license + attribution + provenance pointers** (and CRS/units as applicable). KFM also treats schemas like code and expects validation gates (CI) to enforce metadata completeness [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi).

#### Minimal metadata template (copy/paste)
```json
{
  "id": "monument_rocks",
  "title": "Monument Rocks (demo model)",
  "description": "Lightweight landmark model for web preview and story steps.",
  "model_type": "reality_based",
  "representation": "surface",
  "files": {
    "glb": "monument_rocks.glb",
    "thumbnail": "monument_rocks.thumb.webp"
  },
  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Author/Institution Name",
    "source_url": "SOURCE_URL_OR_CITATION_ID"
  },
  "provenance": {
    "stac_item_id": "kfm.ks.landmarks.monument_rocks.v1",
    "dcat_dataset_id": "kfm.ks.landmarks.monument_rocks",
    "prov_activity_id": "prov:activity:monument_rocks_build_v1",
    "notes": "Capture scan → cleanup → decimate → bake textures → export GLB."
  },
  "spatial": {
    "is_georeferenced": false,
    "crs_original": null,
    "crs_web": "EPSG:4326",
    "units": "meters"
  },
  "performance": {
    "triangles": 0,
    "textures": [
      { "name": "albedo", "resolution": "2048x2048", "format": "webp" }
    ],
    "approx_download_mb": 0
  },
  "version": "v1"
}
```

### 🏷️ Model types (recommended taxonomy)

Borrowing from 3D GIS/heritage practice, distinguish:
- **Reality-based models**: represent the object/site “as captured” at acquisition time.
- **Interpretative models**: hypothetical reconstructions of past states [oai_citation:15‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2).

Also capture the representation style:
- `surface` (mesh)
- `boundary` (solid / volumetric boundary model)
- `volume` (voxel) — avoid shipping unless explicitly justified for the web [oai_citation:16‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2).

---

## ⚡ Performance budgets

WebGL makes 3D accessible directly in browsers (no plugins) and is intended for rich web experiences [oai_citation:17‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)—but we still need to respect mobile/low-end GPUs.

### Suggested targets (tune per use-case)
| Target | “Good” | “Upper bound” | Notes |
|---|---:|---:|---|
| GLB size | ≤ 5 MB | ≤ 15 MB | Prefer multiple LODs over one huge mesh. |
| Triangles | ≤ 50k | ≤ 200k | Per model instance in-view. |
| Texture size | 1–2× 2K | 4K max | Prefer WebP/AVIF for web delivery. |
| Materials | ≤ 3 | ≤ 8 | Fewer materials = fewer draw calls. |

### Optimization tips (practical)
- Reduce poly count (decimate) + preserve silhouette.
- Bake normals/ambient occlusion.
- Use texture atlases when possible.
- Consider mesh compression (Draco / meshopt) if supported by the loader pipeline.

---

## 🧪 Add / update flow (recommended)

```mermaid
flowchart LR
  A[🧾 Source / Scan / Model] --> B[🧹 Cleanup & Normalize]
  B --> C[📐 Scale & Units]
  C --> D[🗜️ Optimize (LOD, bake, compress)]
  D --> E[🧊 Export GLB]
  E --> F[🧾 Write meta.json]
  F --> G[🔍 Preview in viewer]
  G --> H[✅ PR + CI checks]
```

---

## 🔍 PR checklist

### Required ✅
- [ ] Model is in its own folder under a logical category (`landmarks/`, `artifacts/`, `ui/`, etc.)
- [ ] `*.glb` exists and loads successfully in the web viewer
- [ ] `*.meta.json` exists with **license + attribution + provenance pointers** [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] File/folder names use **lower_case_with_underscores** [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] If georeferenced: original CRS is captured and WGS84 alignment is described [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Strongly recommended ⭐
- [ ] Add a thumbnail (`*.thumb.webp`)
- [ ] Document triangle count + approximate size in metadata
- [ ] If it’s evidence/story content: ensure it’s also cataloged (STAC/DCAT/PROV) per KFM policy [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📚 References

- KFM frontend uses MapLibre (2D) + CesiumJS (3D) and streams geospatial 3D via **3D Tiles** [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- KFM naming + metadata validation expectations (CRS tracking, WGS84 normalization, schema/CI thinking) [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- KFM contract-first + provenance-first pipeline ordering and governed artifacts [oai_citation:24‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:25‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- STAC/DCAT/PROV required alignment policy + CI validation of profiles [oai_citation:26‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- Interpretative vs reality-based model distinction (heritage/3D GIS practice) [oai_citation:27‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
- Surface/boundary/volume representations; voxel storage costs are high [oai_citation:28‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
- WebGL role in enabling 3D graphics in browsers [oai_citation:29‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)
