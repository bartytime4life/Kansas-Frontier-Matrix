# 🏺 Archaeology 3D Assets (KFM) — `web/assets/3d/archaeology`

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-2ea44f)
![3D GIS](https://img.shields.io/badge/3D%20GIS-stratigraphy%20%E2%80%A2%20volumes%20%E2%80%A2%20visibility-1f6feb)
![WebGL](https://img.shields.io/badge/WebGL-ready-orange)
![Format](https://img.shields.io/badge/Preferred%20Format-glTF%202.0%20(GLB)-ff8c00)
![Provenance](https://img.shields.io/badge/Provenance-first-8a2be2)
![Human Centered](https://img.shields.io/badge/Digital%20Humanism-human--centered%20design-6f42c1)

**Purpose:** This folder stores **web-ready 3D archaeology assets** (models + textures + metadata) used by the KFM “living atlas” to make archaeological evidence **searchable, mappable, auditable, and modelable**—not just “pretty.” 🧭🧱

> [!IMPORTANT]
> **Provenance is a first-class asset.** If a model can’t tell you **where it came from**, **how it was processed**, and **what coordinate space it lives in**, it doesn’t ship.

---

## 🧭 Quick Nav
- [What belongs here](#-what-belongs-here)
- [Folder layout](#-folder-layout)
- [Asset standards](#-asset-standards)
- [Provenance & metadata](#-provenance--metadata)
- [3D GIS analysis outputs](#-3d-gis-analysis-outputs)
- [Performance budgets](#-performance-budgets)
- [Security, ethics, and site protection](#-security-ethics-and-site-protection)
- [Contribution workflow](#-contribution-workflow)
- [📚 Project reference shelf](#-project-reference-shelf)

---

## 📦 What belongs here

This directory is for **static 3D artifacts and site recon assets** that the web client can load without bespoke backend transformations.

Typical asset categories:
- 🧱 **Trenches / excavation units** (stratigraphy layers, locus surfaces)
- 🏺 **Artifacts** (photogrammetry scans, curated low-poly GLBs for browsing)
- 🗿 **Features** (walls, foundations, pits, postholes, mounds)
- 🧊 **Volumes** (voxel-derived meshes, CT-derived segmentations, GPR-informed volumes)
- 🌄 **Context surfaces** (local DEM cutouts, orthomosaic drapes, landscape meshes)

Non-goals (store elsewhere):
- ❌ Raw photogrammetry image sets (huge + sensitive)
- ❌ Unprocessed laser point clouds (unless tiled/streamable and explicitly needed)
- ❌ Sensitive site coordinates that increase looting risk (use redaction + access controls)

---

## 🗂 Folder layout

> [!NOTE]
> This layout is designed to support: **(1)** web delivery, **(2)** GIS-grade georeferencing, and **(3)** auditability over time.

```text
web/assets/3d/archaeology/
├── README.md
├── index.json                      # (optional) generated registry for the web app
├── schemas/
│   ├── kfm-3d-asset.schema.json    # JSON Schema for validation
│   └── kfm-provenance.schema.json
├── sites/
│   └── <site_slug>/
│       ├── manifest.json           # what the viewer loads (models, LODs, thumbnails)
│       ├── metadata.yaml           # human-friendly metadata (mirrors manifest fields)
│       ├── provenance.yaml         # capture + processing chain (tooling, params, checksums)
│       ├── citations.bib           # academic citations (optional but encouraged)
│       ├── thumbs/
│       │   ├── hero.webp
│       │   └── card.webp
│       ├── models/
│       │   ├── lod0.glb            # highest detail web-safe
│       │   ├── lod1.glb
│       │   └── lod2.glb
│       ├── textures/
│       │   ├── albedo.ktx2
│       │   ├── normal.ktx2
│       │   └── orm.ktx2            # occlusion/roughness/metallic packed
│       ├── georef/
│       │   ├── crs.wkt             # CRS as WKT (authoritative)
│       │   ├── transform.json      # local→world transform (incl. units + axis)
│       │   └── bounds.geojson      # footprint / bbox in map CRS
│       └── analysis/
│           ├── volumes/
│           │   ├── volume_report.json
│           │   └── volume_mesh.glb
│           └── visibility/
│               ├── viewshed.geojson
│               └── visibility_notes.md
└── artifacts/
    └── <artifact_slug>/            # same structure as sites/, smaller scale
```

### 🏷 Suggested slugs (stable + boring = good)
- `sites/<site_slug>`: `ks_<county>_<site>_<year>`  
  Example: `ks_douglas_riverbend_2024`
- `artifacts/<artifact_slug>`: `ks_<site>_<catalog>_<shortname>`  
  Example: `ks_riverbend_41DG12_sherd_001`

---

## ✅ Asset standards

### 1) Formats (web-first)
**Preferred**
- ✅ **glTF 2.0** as **GLB** (`.glb`) for meshes + materials
- ✅ **KTX2 / BasisU** (`.ktx2`) for GPU-friendly textures
- ✅ **WebP** (`.webp`) for thumbnails and UI imagery

**Allowed (with justification)**
- ⚠️ `.gltf + .bin` (harder to ship; more files)
- ⚠️ `.png` / `.jpg` textures (larger; OK for legacy or very small assets)

**Avoid**
- ❌ `.obj` for final delivery (no modern material pipeline, huge)
- ❌ `.tif` textures for web (use for archival, not web runtime)

> [!TIP]
> If your texture strategy is unclear, start with the **compressed image formats reference** and treat web delivery as a performance problem, not an aesthetic one. 🧩

---

### 2) Units, axes, and scale
- 📏 **Units:** meters (`m`) unless explicitly noted.
- 🧭 **Up axis:** `+Z` (typical glTF).
- 🧱 **Model origin:** local, near the site (avoid far-from-origin precision issues).
- 🧷 **Georeferencing:** store a **local→world** transform in `georef/transform.json`.

Why we’re strict: large coordinate values (like full UTM eastings) can cause WebGL precision jitter; georeferencing via transform preserves GIS truth *and* stable rendering.

---

### 3) Georeferencing strategy (recommended)
Use a **two-space approach**:
1. **Local Space (rendering):** small coordinates near `(0,0,0)` for stability.
2. **World Space (GIS):** `EPSG:*` CRS or WKT + vertical datum.

Store:
- `georef/crs.wkt` → authoritative CRS definition
- `georef/transform.json` → rigid transform (and optional scale) from local→world
- `georef/bounds.geojson` → map footprint for quick UI placement

---

## 🧾 Provenance & metadata

KFM’s platform philosophy is **provenance-first**: every layer, dataset, and AI-backed claim should be traceable. This folder enforces that at the asset level.

### Required files per asset
- `manifest.json` ✅ (runtime contract)
- `provenance.yaml` ✅ (audit trail)
- `thumbs/hero.webp` ✅ (UI)
- `georef/crs.wkt` ✅ (spatial truth)

### `manifest.json` minimal example
```json
{
  "id": "ks_douglas_riverbend_2024_trench_a",
  "kind": "site.trench",
  "title": "Riverbend — Trench A",
  "summary": "3D trench model with stratigraphic layers and feature annotations.",
  "keywords": ["archaeology", "excavation", "stratigraphy", "3d-gis"],
  "license": {
    "spdx": "CC-BY-4.0",
    "notes": "Confirm landowner release stored in project admin records."
  },
  "spatial": {
    "crs_wkt_path": "georef/crs.wkt",
    "transform_path": "georef/transform.json",
    "bounds_geojson_path": "georef/bounds.geojson"
  },
  "assets": {
    "models": [
      { "lod": 0, "path": "models/lod0.glb", "triangles": 450000, "bytes": 24500000 },
      { "lod": 1, "path": "models/lod1.glb", "triangles": 180000, "bytes": 12000000 },
      { "lod": 2, "path": "models/lod2.glb", "triangles": 60000,  "bytes": 4500000 }
    ],
    "textures": [
      { "role": "albedo", "path": "textures/albedo.ktx2" },
      { "role": "normal", "path": "textures/normal.ktx2" },
      { "role": "orm",    "path": "textures/orm.ktx2" }
    ],
    "thumbnails": {
      "hero": "thumbs/hero.webp",
      "card": "thumbs/card.webp"
    }
  },
  "provenance_path": "provenance.yaml",
  "created_utc": "2026-01-14T00:00:00Z"
}
```

### `provenance.yaml` (audit chain) example
```yaml
capture:
  method: photogrammetry
  device: "Sony A7R IV"
  date_utc: "2024-06-18T15:20:00Z"
  operator: "KFM Field Team"
  notes: "Overcast, cross-polarized lighting where possible."

processing:
  - step: "alignment"
    tool: "Metashape"
    version: "2.x"
    params: { quality: "high", keypoint_limit: 40000 }
  - step: "mesh_cleanup"
    tool: "Blender"
    version: "4.x"
    params: { decimate_ratio: 0.35, apply_scale: true }
  - step: "export"
    tool: "glTF exporter"
    version: "Blender built-in"
  - step: "optimize"
    tool: "gltfpack"
    version: "1.x"
    params: { meshopt: true, draco: false }

integrity:
  sha256:
    models/lod0.glb: "..."
    textures/albedo.ktx2: "..."

citations:
  - key: "DellUntoLandeschi_3DGIS_2022"
    why_it_matters: "3D GIS framing for stratigraphy, visibility, and volumetric interpretation."
```

> [!CAUTION]
> If you change **anything** about a mesh or texture, update:
> - `provenance.yaml` (new processing step + tool versions)
> - checksums
> - `manifest.json` size/triangle counts (if tracked)

---

## 🔎 3D GIS analysis outputs

This folder doesn’t just store meshes—it supports **3D GIS-style interpretation** where analysis is reproducible and inspectable.

### Recommended analysis products
- 👁️ **3D visibility** (viewsheds, line-of-sight samples, observation points)
- 🧊 **Volumes** (cut/fill, feature volumes, depositional units)
- 🪨 **Surface + subsurface** linkages (context surfaces + excavated volumes)
- 🧭 **Stratigraphic sequencing** (layer IDs, Harris-matrix references if available)

### Output conventions
- `analysis/volumes/volume_report.json`
  - volume measurements, method, uncertainty assumptions
- `analysis/visibility/viewshed.geojson`
  - polygons or sample rays with CRS declared in metadata
- `analysis/*/*.md`
  - “interpretation notes” that separate **observations** from **inferences** ✅

> [!NOTE]
> This follows a 3D GIS mindset: a model is not “the past,” it’s a **knowledge artifact** with assumptions, measurement error, and interpretive layers.

---

## 🚀 Performance budgets

Treat performance as a design constraint (database-scale thinking applies to assets too).

### Suggested per-asset budgets (tweak per target device)
- 📦 **LOD0 GLB:** ≤ 25–40 MB
- 🧱 **LOD0 triangles:** ≤ 500k (site) / ≤ 150k (artifact)
- 🖼️ **Texture set total:** ≤ 16–32 MB (KTX2)
- 🧠 **Materials:** keep to a small set; bake where possible
- 🧊 **Draw calls:** prefer mesh merging and atlasing when it doesn’t destroy semantics

### Delivery principles
- 🧩 Prefer **progressive detail** (LOD switching) over “one giant mesh”
- 🗜️ Use compressed textures and geometry optimizers
- 🧭 Keep rendering coordinates local for numeric stability

---

## 🔐 Security, ethics, and site protection

KFM is built to augment human understanding—not to enable harm.

Checklist:
- 🕵️ **Looting risk:** if location is sensitive, store redacted bounds and gate access.
- 🧑‍⚖️ **Rights & releases:** confirm landowner/tribal permissions where applicable.
- 🧾 **License clarity:** every asset must declare license and restrictions.
- 🧠 **AI outputs:** if an AI-generated note references this asset, it must cite sources and remain advisory (no “black box” claims).

> [!IMPORTANT]
> “Open” does not mean “reckless.” We default to **transparent + responsible**, aligned with digital humanism principles and emerging AI governance thinking.

---

## 🔧 Contribution workflow

### ✅ Add a new site asset
1. Create folder: `sites/<site_slug>/`
2. Add **LOD models**: `models/lod0.glb`, `lod1.glb`, `lod2.glb`
3. Add textures (prefer KTX2): `textures/*.ktx2`
4. Add `thumbs/hero.webp` + `thumbs/card.webp`
5. Add `georef/crs.wkt` + `georef/transform.json` + `georef/bounds.geojson`
6. Write `manifest.json` + `provenance.yaml`
7. (Optional) Add `citations.bib` + `analysis/*`
8. Update root registry (`index.json`) if your app uses it

### 🧪 Validate (recommended)
- Run JSON schema validation on `manifest.json`
- Sanity-check georef: bounds overlay in map view
- Confirm LOD switching doesn’t pop wildly (scale/origin consistent)

### PR checklist ✅
- [ ] Stable slug naming
- [ ] Provenance chain includes tools + versions
- [ ] License declared + notes
- [ ] CRS + transform provided
- [ ] Thumbnails present
- [ ] LODs present (or rationale documented)
- [ ] Size/triangle budgets respected (or justified)
- [ ] Sensitive data reviewed (risk: looting / privacy)

---

## 🧠 How this ties into KFM architecture

This folder supports clean-architecture separation:
- **Domain:** archaeological entities (sites, features, artifacts)
- **Services:** ingest → validate → analyze (volumes/visibility) → publish
- **Adapters:** web viewer (WebGL), data stores (e.g., PostGIS), search index

The key idea: web assets remain **portable**, while metadata preserves interoperability (data-spaces thinking) and auditability.

---

## 📚 Project reference shelf

Below is the **full** project library currently shaping this module. Use it as “design intent documentation” for decisions made here. 📘✨

<details>
<summary><strong>📚 All project PDFs (what each one contributes)</strong></summary>

| File | How it informs this folder (practical use) |
|---|---|
| **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf** | Vision: provenance-first, auditable layers, clean architecture; informs metadata + traceability mindset. |
| **Archaeological 3D GIS_26_01_12_17_53_09.pdf** | 3D GIS practice: stratigraphy, surface/subsurface, visibility, volumes; informs `analysis/` outputs + interpretation notes. |
| **making-maps-a-visual-guide-to-map-design-for-gis.pdf** | Cartographic clarity; informs UI thumbnails, legends, and how 3D layers appear in map context. |
| **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf** | Mobile-first spatial UX; informs thumbnail sizes, interaction patterns, and “field-to-web” assumptions. |
| **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf** | Rendering fundamentals; informs format choices (GLB), coordinate precision, and WebGL-safe budgets. |
| **responsive-web-design-with-html5-and-css3.pdf** | Responsive UI constraints; informs asset preview components + touch-first interactions. |
| **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf** | Image compression tradeoffs; informs texture/thumbnail decisions (plus migration path to KTX2/WebP). |
| **python-geospatial-analysis-cookbook.pdf** | Geospatial processing patterns; informs scripts for bounds, CRS transforms, QA checks. |
| **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf** | Context layers (DEM, NDVI, orthos); informs how 3D assets “snap” to remote sensing context. |
| **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf** | DB patterns; informs how metadata/manifests can be stored + queried (esp. when paired with PostGIS). |
| **Database Performance at Scale.pdf** | Performance thinking; informs streaming, LOD strategy, and “treat assets like workloads.” |
| **Scalable Data Management for Future Hardware.pdf** | Scaling assumptions; informs batch pipelines and future-proofing storage/index design. |
| **Data Spaces.pdf** | Interoperability and data-sharing mindset; informs schema design + portability across tools/orgs. |
| **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf** | Modeling rigor; informs uncertainty notes + reproducible simulation/analysis outputs. |
| **Generalized Topology Optimization for Structural Design.pdf** | Reconstruction/structural reasoning; informs future “hypothesis models” vs evidence models separation. |
| **Spectral Geometry of Graphs.pdf** | Graph-based spatial analysis; informs future connectivity/visibility networks and topological descriptors. |
| **Understanding Statistics & Experimental Design.pdf** | Measurement + validation mindset; informs QA, uncertainty, and reproducible comparisons across seasons. |
| **graphical-data-analysis-with-r.pdf** | Exploratory analysis; informs quick EDA for derived metrics (volumes, visibility stats). |
| **regression-analysis-with-python.pdf** | Predictive modeling patterns; informs derived metrics modeling (e.g., erosion risk vs site exposure). |
| **Regression analysis using Python - slides-linear-regression.pdf** | Lightweight reference for regression; supports quick modeling and reporting. |
| **think-bayes-bayesian-statistics-in-python.pdf** | Bayesian uncertainty; informs expressing uncertainty in interpretations (vs false precision). |
| **Understanding Machine Learning: From Theory to Algorithms.pdf** | ML foundations; informs responsible ML integration (especially evaluation and generalization). |
| **Introduction to Digital Humanism.pdf** | Human-centered/ethical design; informs safeguards, explainability, and participatory workflows. |
| **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf** | Governance + conceptual framing; informs AI-feature boundaries and compliance-minded metadata. |
| **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf** | Defensive security; informs access controls and safe publishing practices (no sensitive leakage). |
| **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf** | Security awareness; used only as “know the attacker mindset” for defensive hardening. |
| **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf** | Real-time ingestion patterns; informs future sensor-to-3D workflows and pipeline concurrency. |
| **Principles of Biological Autonomy - book_9780262381833.pdf** | Systems thinking; informs modeling “living landscapes” and non-reductionist interpretations. |
| **A programming Books.pdf** | General reference library (language breadth) for implementation tasks. |
| **B-C programming Books.pdf** | General reference library. |
| **D-E programming Books.pdf** | General reference library. |
| **F-H programming Books.pdf** | General reference library. |
| **I-L programming Books.pdf** | General reference library. |
| **M-N programming Books.pdf** | General reference library. |
| **O-R programming Books.pdf** | General reference library. |
| **S-T programming Books.pdf** | General reference library. |
| **U-X programming Books.pdf** | General reference library. |
| **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf** | Practical deep learning reference for later stages (classification/segmentation), when governance + data quality are ready. |
| **Implementing Programming Languages (embedded in the programming books collection)** | Supports future DSLs for querying/transforming spatiotemporal + 3D assets. |
| **MATLAB Notes for Professionals (embedded in the programming books collection)** | Quick reference for matrix/geometry operations and prototyping transforms. |
| **Bash Notes for Professionals (embedded in the programming books collection)** | Pipeline scripting + reproducible CLI workflows. |

</details>

---

## 🧩 Glossary (quick)
- **LOD**: Level of Detail (multiple mesh resolutions for streaming)
- **CRS**: Coordinate Reference System (your spatial truth contract)
- **WKT**: Well-Known Text (portable CRS encoding)
- **KTX2**: GPU-friendly compressed texture container
- **glTF/GLB**: Web-native 3D format (materials + mesh)

---

## 🗺️ Roadmap ideas (optional)
- 🧱 Cesium 3D Tiles pipeline for massive landscapes
- 🧭 Harris Matrix integration (stratigraphic relationships as graph)
- 🧊 Voxel workflows for CT/GPR-informed volumes
- 🔎 Semantic annotations (features/artifacts) with provenance-linked confidence

—  
**Folder owner:** KFM 3D + Archaeology module  
**Last updated:** 2026-01-14
