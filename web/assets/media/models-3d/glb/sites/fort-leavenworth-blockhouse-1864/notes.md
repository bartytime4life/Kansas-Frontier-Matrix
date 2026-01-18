---
title: "🏰 Fort Leavenworth Blockhouse (1864) — 3D Model Notes"
slug: "fort-leavenworth-blockhouse-1864"
asset:
  kind: "3d-model"
  domain: "sites"
  format: "glb"
  status: "draft"
  version: "0.1.0"
  created: "2026-01-18"
  updated: "2026-01-18"
kfm:
  visibility: "public"
  focus_mode_ready: false
  catalogs:
    stac_item_id: "TBD"
    dcat_dataset_id: "TBD"
    prov_bundle_id: "TBD"
    graph_node_id: "TBD"
---

# 🏰 Fort Leavenworth Blockhouse (1864) — 3D Model Notes

![Status](https://img.shields.io/badge/status-draft-yellow)
![Format](https://img.shields.io/badge/format-GLB-blue)
![Domain](https://img.shields.io/badge/domain-sites-green)
![KFM](https://img.shields.io/badge/KFM-provenance--first-6f42c1)
![License](https://img.shields.io/badge/license-TBD-lightgrey)

> [!IMPORTANT]
> This `notes.md` is the **human-readable companion** to the asset.  
> **Publishing rules** (contract-first + provenance-first) require a validated metadata “data contract,” plus catalog/provenance hooks (STAC/DCAT/PROV).[^kfm_contract][^kfm_data_contract]

---

## 🧭 Quick Nav

- [📌 What this is](#-what-this-is)
- [📍 Site + time reference](#-site--time-reference)
- [📦 Folder + file inventory](#-folder--file-inventory)
- [🧱 Representation type](#-representation-type)
- [🧬 Provenance & evidence register](#-provenance--evidence-register)
- [🛠️ Model build pipeline](#️-model-build-pipeline)
- [📐 Spatial reference & orientation](#-spatial-reference--orientation)
- [⚙️ Technical specs & budgets](#️-technical-specs--budgets)
- [✅ QA checklist](#-qa-checklist)
- [🔗 KFM catalog hooks](#-kfm-catalog-hooks)
- [🧩 Web viewer integration notes](#-web-viewer-integration-notes)
- [🗓️ Changelog](#️-changelog)
- [🤝 Credits](#-credits)
- [📚 References](#-references)

---

## 📌 What this is

This folder contains a **glTF 2.0 binary** (`.glb`) 3D model intended for Kansas Frontier Matrix (KFM) site visualization and narrative storytelling.

> [!NOTE]
> The folder name indicates an intended historical “snapshot” year (**1864**) — treat the year as **unverified** until primary sources are attached in the evidence register.[^md_citations]

---

## 📍 Site + time reference

| Field | Value |
|---|---|
| 📍 Place name | Fort Leavenworth (Blockhouse) |
| 🗺️ Place hierarchy | Leavenworth, Kansas, USA *(confirm exact hierarchy used in KFM gazetteer)* |
| 🕰️ Intended time slice | 1864 *(verify with sources; do not publish as fact without citations)* |
| 🧭 Coordinates | **TBD** *(add if allowed; see sensitivity notes)* |
| 🏷️ Tags | `site` `fort` `blockhouse` `kansas` `19th-century` |
| 🔐 Sensitivity class | **TBD** (public / limited / restricted) |

> [!CAUTION]
> If any part of this site is sensitive (e.g., restricted access, culturally sensitive location, or security constraints), **do not publish precise coordinates** and ensure “Focus Mode” cannot leak restricted location details.[^focus_mode_rules]

---

## 📦 Folder + file inventory

**Expected layout** (adjust to match actual files in this folder):

```text
📁 web/assets/media/models-3d/glb/sites/fort-leavenworth-blockhouse-1864/
├─ 🧱 fort-leavenworth-blockhouse-1864.glb        # primary model (preferred name)
├─ 🧱 fort-leavenworth-blockhouse-1864.draco.glb  # optional: Draco-compressed variant
├─ 🖼️ preview.webp                               # optional: larger preview image
├─ 🖼️ thumb.webp                                 # optional: thumbnail for UI lists
├─ 📄 meta.json                                  # REQUIRED: metadata “data contract” (if used in web layer)
└─ 🗒️ notes.md                                   # this file
```

> [!TIP]
> If you only keep one binary: keep the uncompressed **source** GLB + generate compressed derivatives during build/release.

---

## 🧱 Representation type

Choose one (and delete the others when known):

- [ ] **Reality capture** (photogrammetry / LiDAR → mesh)  
- [ ] **Interpretive reconstruction** (modeled from plans, drawings, photos)  
- [ ] **Hybrid** (capture base + reconstruction edits)  

> [!NOTE]
> In cultural heritage workflows, the **quality and transparency of execution** matters: being able to reconstruct *how* the model was made, *in what context*, and *how it should be used* is essential.[^arch_transparency]

---

## 🧬 Provenance & evidence register

KFM requires “no mystery layers”: every visible thing should be traceable to sources + processing steps in metadata/provenance.[^kfm_data_contract][^md_citations]

### ✅ Evidence register (fill this in before publishing)

| Evidence ID | Type | Title / Description | Date | Where stored | License | Notes |
|---|---|---|---|---|---|---|
| E-001 | Photo | TBD | TBD | `data/raw/...` | TBD | Add photographer/collection |
| E-002 | Plan / Drawing | TBD | TBD | `data/raw/...` | TBD | Scan resolution + provenance |
| E-003 | Map | TBD | TBD | `data/raw/...` | TBD | Georeference method if used |
| E-004 | On-site capture | TBD | TBD | `data/raw/...` | TBD | Capture log + GCPs/RTK if any |
| E-005 | Secondary source | TBD | TBD | `data/raw/...` | TBD | Use sparingly; prefer primary |

> [!IMPORTANT]
> If you cite it in narrative or claim it in metadata, it must exist in the evidence register and be linkable.[^md_citations]

---

## 🛠️ Model build pipeline

> [!NOTE]
> Image-based 3D modeling can produce accurate textured models, and these can be **scaled + georeferenced** for use in GIS/web mapping contexts.[^arch_georef]  
> Also: many outcomes depend on **human-made choices** (image overlap, distance, alignment parameters, mesh/export settings) — log those choices.[^arch_human_factor]

### 📋 Pipeline steps (template)

1. **Acquire sources**
   - Capture method: `TBD` (photogrammetry / LiDAR / hand-modeled)
   - Capture device(s): `TBD`
   - Ground control / scale references: `TBD`

2. **Reconstruct / model**
   - Software: `TBD` (Metashape / RealityCapture / Blender / etc.)
   - Key settings: `TBD` (alignment, depth, filtering, decimation)

3. **Clean + optimize**
   - Fix non-manifold geometry
   - Retopology (if needed)
   - UV unwrap (if needed)
   - Bake textures / normals (if needed)

4. **Export**
   - Format: **glTF 2.0 / GLB**
   - PBR workflow: `TBD` (metal-rough recommended)

5. **Web performance pass**
   - LODs: `TBD` (none / 2 levels / 3 levels)
   - Compression: `TBD` (Draco / Meshopt)
   - Textures: `TBD` (WebP / KTX2 BasisU)

6. **Validation**
   - Visual inspection
   - Coordinate + scale verification
   - Metadata contract validation + catalog hooks (STAC/DCAT/PROV)

> [!TIP]
> Store **raw** and **work** artifacts separately from **published** assets. This makes builds reproducible and audits easy.[^md_pipeline]

---

## 📐 Spatial reference & orientation

KFM standardizes web display around WGS84 (EPSG:4326) and tracks original CRS in metadata; units (e.g., meters) should be explicit.[^kfm_crs]

| Property | Value |
|---|---|
| CRS | EPSG:4326 (WGS84) *(if georeferenced)* |
| Units | meters *(recommended)* |
| Up axis | `TBD` (Y-up for glTF; verify exporter) |
| Forward axis | `TBD` |
| Scale | `TBD` (1.0 = meters) |
| Georeference anchor | `TBD` (origin point / pivot) |

> [!CAUTION]
> If model is **not** georeferenced, do not “fake precision.” Mark clearly as *non-georeferenced* and keep placement approximate until anchored.

---

## ⚙️ Technical specs & budgets

Fill these in after optimization:

| Metric | Target | Actual |
|---|---:|---:|
| Triangles | ≤ 100k (site prop) | TBD |
| Materials | ≤ 6 | TBD |
| Textures | ≤ 6 | TBD |
| Max texture size | 2048–4096 | TBD |
| File size | ≤ 15–25 MB | TBD |
| Draw calls | as low as possible | TBD |

> [!NOTE]
> These are **web-first** targets; if you need archival fidelity, keep a high-res source separately and publish a simplified web derivative.

---

## ✅ QA checklist

### Geometry & visuals
- [ ] No missing textures
- [ ] Normals correct (no inverted faces)
- [ ] No obvious z-fighting
- [ ] No non-manifold geometry that breaks renderers
- [ ] Pivot/origin set intentionally (documented)
- [ ] Scale verified against known measurement (documented)

### Metadata & provenance
- [ ] Evidence register filled
- [ ] License confirmed + compatible with KFM publishing
- [ ] Metadata “data contract” complete (id/title/description/tags/bounds/time/license/sources/processing/validation)[^kfm_data_contract]
- [ ] Any narrative claims have citations / provenance links[^md_citations]
- [ ] Sensitivity classification reviewed (no restricted details)[^focus_mode_rules]

### KFM integration
- [ ] STAC item/collection created (or queued)
- [ ] DCAT dataset view created (or queued)
- [ ] PROV bundle created (or queued)
- [ ] Graph node created/linked (place ↔ asset ↔ events ↔ sources)

---

## 🔗 KFM catalog hooks

KFM aligns assets to open standards for discoverability and provenance (STAC, DCAT, PROV-O).[^kfm_contract][^md_pipeline]

### Identifiers (fill in)

| Hook | ID |
|---|---|
| STAC Item | `TBD` |
| STAC Collection | `TBD` |
| DCAT Dataset | `TBD` |
| PROV Bundle | `TBD` |
| Graph Node | `TBD` |

### Suggested slug conventions (recommended)
- Asset slug (this folder): `fort-leavenworth-blockhouse-1864`
- KFM asset id: `kfm:3d:site:fort-leavenworth-blockhouse:1864`
- STAC item id: `kfm-sites-fort-leavenworth-blockhouse-1864-glb`

---

## 🧩 Web viewer integration notes

KFM’s web UI supports 2D (MapLibre) and 3D (Cesium) views; 3D can be used for models and other vertical-dimension data.[^kfm_ui_3d]

### Minimal Three.js load snippet (example)

```js
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";

const loader = new GLTFLoader();
loader.load(
  "/assets/media/models-3d/glb/sites/fort-leavenworth-blockhouse-1864/fort-leavenworth-blockhouse-1864.glb",
  (gltf) => scene.add(gltf.scene),
  undefined,
  (err) => console.error(err),
);
```

### Cesium notes (if georeferenced)
- If the model is georeferenced, prefer **Cesium placement** with a known lon/lat + height.
- For very large/streamed 3D content, KFM references the **3D Tiles** approach via Cesium for efficiency.[^kfm_ui_3d]

---

## 🗓️ Changelog

- **0.1.0 (2026-01-18)** — Initial notes template created; awaiting model metrics + provenance.

---

## 🤝 Credits

| Role | Name / Org | Contact |
|---|---|---|
| Model author | TBD | TBD |
| Reviewer | TBD | TBD |
| Source holders | TBD | TBD |

---

## 📚 References

[^kfm_data_contract]: KFM describes a metadata JSON “data contract” that includes (among other fields) id/title/description/tags/spatial bounds/temporal range/CRS/license/sources/processing steps/validation, and emphasizes “no mystery layers.”  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm_contract]: KFM emphasizes a “contract-first and provenance-first” approach and alignment to open standards (STAC, DCAT, PROV-O) with strict metadata requirements.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^md_pipeline]: The KFM authoring guide reinforces contract-first/provenance-first/deterministic principles and shows an ingest→catalog→graph→API→UI pipeline flow (including MapLibre/Cesium + Focus Mode).  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^md_citations]: The KFM authoring guide requires provenance for claims (citations, source links, and clear separation of facts vs interpretation).  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^focus_mode_rules]: Focus Mode rules include only provenance-linked content, no sensitive location leaks, and clear labeling for AI assistance (opt-in).  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^kfm_crs]: KFM notes WGS84 (EPSG:4326) as an internal standard for web consistency and emphasizes tracking original CRS + units in metadata.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm_ui_3d]: KFM documentation describes MapLibre (2D) + Cesium (3D) integration, including the ability to view 3D models and use 3D Tiles for streaming larger 3D datasets.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^arch_georef]: Archaeological 3D GIS notes that high-resolution 3D models can be imported into georeferenced space, and describes workflows where models are scaled/georeferenced and brought into GIS environments.  [oai_citation:9‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
[^arch_human_factor]: Archaeological 3D GIS highlights that acquisition/processing involves many human choices (capture overlap/distance, alignment and mesh/export parameters) that affect outcomes, so documenting those choices is important.  [oai_citation:10‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
[^arch_transparency]: Archaeological 3D GIS discusses why models are trustworthy when their creation history and context are reconstructable and their appropriate uses/limits are clear.  [oai_citation:11‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
