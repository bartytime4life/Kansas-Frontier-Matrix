---
title: "KFM Web Sample Assets"
doc_kind: "Runbook"
version: "v1.0.0"
status: "active"
last_updated: "2026-01-14"
license: "CC-BY-4.0"
sensitivity: "public"
care_label: "Public"
---

# 🧪 `web/assets/samples/` — Sample Assets & Fixtures

![scope](https://img.shields.io/badge/scope-web%2Fassets%2Fsamples-blue)
![purpose](https://img.shields.io/badge/purpose-demos%20%7C%20tests%20%7C%20storybook%20%7C%20docs-7c3aed)
![rule](https://img.shields.io/badge/rule-no%20production%20evidence%20here-red)
![formats](https://img.shields.io/badge/formats-GeoJSON%20%7C%20TopoJSON%20%7C%20PNG%2FWebP%20%7C%20GLB%20%7C%20JSON-informational)

> [!NOTE]
> This folder is **UI-only**: small, safe, and reviewable assets used to demo the web experience (MapLibre/Cesium-style viewers), drive component examples, and provide test fixtures.  
> **Authoritative datasets must come from the governed pipeline (ETL → catalogs → API → UI).** 🧾🧬

---

## 🧭 Why this folder exists

KFM’s web UI needs **tiny, deterministic assets** for:
- 🧩 UI component development (menus, legends, charts, popovers)
- 🧪 unit/integration/e2e tests (stable fixtures)
- 🗺️ demo layers (offline-friendly, quick to load)
- 📚 docs + screenshots (consistent visuals in PRs/issues)
- 🧠 “Focus Mode”/Story tooling prototypes (non-authoritative examples only)

---

## 🚫 What does **not** belong here

> [!WARNING]
> Avoid turning this folder into a shadow data-pipeline. If it’s “real evidence,” it does **not** belong here.

**Do not store**:
- ❌ production/published evidence layers (anything meant to be “truth”)
- ❌ sensitive data (personal data, culturally sensitive locations, restricted layers)
- ❌ large datasets (anything that needs tiling, LFS, or a CDN)
- ❌ “mystery data” (no license, no source, no metadata)
- ❌ executable payloads (scripts, HTML with inline JS, SVGs with scripts, etc.)

If a layer is meant to appear as “evidence” in the UI, it should be published through the normal KFM pathway (data + STAC/DCAT/PROV + API boundary), then referenced by the UI. ✅

---

## 📁 Recommended layout

> [!TIP]
> If the repo already has a different structure, keep it — but try to align to the conventions below for consistency.

```text
web/assets/samples/
├── 📄 README.md
├── 🧾🗂️ samples.catalog.json              # 👈 registry the UI can load
├── 🧩 _shared/
│   ├── 🖼️ thumbnails/                     # common previews (webp/png)
│   ├── ⚖️ licenses/                       # reusable license texts
│   └── 📐 schemas/                        # optional JSON schemas for samples
├── 🧭 vector/                             # geojson/topojson/pmtiles pointers
├── 🗺️ raster/                             # small png/webp + worldfiles if needed
├── 🧱 tiles/                              # tiny demo tilesets or pointers
├── 🧊 3d/                                 # glb / 3d-tiles demo assets
├── 📈 analytics/                          # chart JSON, regression fixtures, etc.
└── 🧰 ui/                                 # icons, placeholder images, mock panels
```

---

## 📦 “Sample Contract” (what every sample should include)

| Required | File | Purpose |
|---:|---|---|
| ✅ | `sample.meta.json` | 🧾 provenance, license, bbox/time, sensitivity label |
| ✅ | `preview.webp` (or `.png`) | 🖼️ thumbnail for UI picker/docs |
| ✅ | `data.*` | 🗺️ the actual sample payload (GeoJSON/TopoJSON/PNG/GLB/JSON) |
| ✅ | `LICENSE.txt` *or* `license_ref` in meta | ⚖️ legal clarity (no guessing) |
| ⛳ | `style.json` | 🎨 MapLibre style snippet (for layer rendering) |
| ⛳ | `README.md` | 🧠 per-sample notes (only if complex) |

> [!NOTE]
> “⛳ Optional” becomes required if the UI can’t render the sample without it.

---

## 🧾 Metadata sidecar: `sample.meta.json`

We keep sample assets **boringly traceable** — even when they’re synthetic.

### Minimum fields (recommended)

```json
{
  "id": "kfm.sample.vector.kansas-counties.v1",
  "title": "Kansas Counties (Demo)",
  "kind": "vector",
  "role": ["demo", "fixture"],
  "description": "Tiny simplified county polygons for UI demos and tests.",
  "format": "geojson",
  "crs": "EPSG:4326",
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "time": { "start": null, "end": null },

  "license": "CC0-1.0",
  "attribution": "Synthetic / derived for demo purposes",
  "sources": [
    { "label": "Describe real source if derived; otherwise say 'synthetic'.", "type": "synthetic" }
  ],

  "sensitivity": "public",
  "care_label": "Public",

  "checksums": { "data": "sha256:..." },
  "build": {
    "generated_by": "tools/make_sample_counties.py",
    "generated_at": "2026-01-14",
    "notes": "Simplified geometry, reduced precision."
  }
}
```

### Notes 📝
- **`id`** should be stable and versioned (`v1`, `v2`, …).
- **`role`** clarifies intent: `demo`, `fixture`, `docs`, `storybook`, `benchmark`.
- **`sensitivity` + `care_label`** are required even for demos. If you’re unsure, treat it as **restricted** and do not add it.

---

## 🗺️ Geospatial sample guidelines

### Vector (GeoJSON / TopoJSON)
- ✅ Prefer **TopoJSON** for anything polygon-heavy (smaller payloads).
- ✅ Keep coordinates in **WGS84 (EPSG:4326)** unless there’s a strong reason not to.
- ✅ Simplify geometry and reduce precision (UI needs shape, not survey-grade accuracy).
- ✅ Keep properties small and documented (avoid 100+ fields).

**Rules of thumb**
- 🎯 Single-file target: **≤ 500KB**
- 🧪 Test fixture target: **≤ 50KB**
- 🧊 If it can’t fit: store a *pointer* (URL) + metadata — don’t commit the blob here.

### Raster (PNG/WebP for UI)
- ✅ Prefer **WebP** for photographic/continuous-tone previews.
- ✅ Prefer **PNG** for sharp lines, labels, or transparency (icons/overlays).
- ✅ If georeferencing is needed for a demo overlay: include a tiny worldfile (`.wld`) or document the mapping in meta.

### Tiles (vector/raster/3D)
- ✅ Small demo tilesets are okay.
- ✅ For anything large, store **only a pointer** plus provenance metadata.

---

## 🧊 3D samples (GLB / 3D Tiles)

KFM’s UI may optionally use 3D (Cesium-style visualization). Keep these lean:
- ✅ Use **glTF binary (`.glb`)** for standalone models
- ✅ Use **3D Tiles** only if the demo truly needs streaming/chunking
- ✅ Include a preview thumbnail + camera hints in meta (`center`, `heading`, `pitch`)

**Performance budget**
- 🎯 `.glb` target: **≤ 2MB**
- 🎯 3D Tiles demo: **≤ 10MB total** (or use remote hosting)

---

## 📈 Analytics samples (charts, regression, bayes, stats)

Samples here power:
- chart components 📊
- tooltips + legends 🧷
- “method cards” / “model cards” style UI 🧠

**Guidelines**
- ✅ Include **units**, **n**, and **confidence/uncertainty** fields where relevant.
- ✅ If you include a fitted model fixture, include:
  - model type (linear/logistic/bayes)
  - parameters
  - evaluation metrics
  - clear disclaimer: “demo only”

Example structure:

```json
{
  "id": "kfm.sample.analytics.regression.v1",
  "title": "Demo regression fixture",
  "kind": "analytics",
  "role": ["fixture"],
  "series": [{ "x": 1, "y": 2.3 }, { "x": 2, "y": 2.9 }],
  "fit": { "type": "linear", "beta0": 1.7, "beta1": 0.6, "r2": 0.81 },
  "units": { "x": "year", "y": "index" },
  "sensitivity": "public",
  "care_label": "Public",
  "license": "CC0-1.0",
  "sources": [{ "type": "synthetic" }]
}
```

---

## ⚡ Performance budgets & caching

> [!IMPORTANT]
> Samples should make the UI feel instant on a cold load.

### Budgets (recommended)
- 📦 Total folder size: **≤ 25MB**
- 🧩 Any single sample payload: **≤ 2MB** (prefer far less)
- 🖼️ Thumbnails: **≤ 150KB** each (WebP preferred)

### Tips 🛠️
- Precompute anything expensive (joins, aggregations, topology cleanup).
- Use deterministic generation scripts where possible.
- Avoid “accidental megabytes” (high-res PNGs, dense GeoJSON, uncompressed meshes).

---

## ♿ Accessibility & responsive rules

KFM’s UI aims to be responsive and accessible, so samples should support that:
- ✅ Thumbnails must be legible at mobile sizes.
- ✅ Prefer color palettes that remain readable for color-vision deficiencies.
- ✅ Don’t bake meaning only into color — include labels/legend hints in meta.

If a sample is used in docs or story demos:
- ✅ Provide alt-text in the consuming markdown/story config
- ✅ Avoid tiny text in images (use UI labels instead)

---

## 🔐 Security & safety guardrails

Even “just samples” can be a security surface. Keep it clean:
- ✅ Treat all sample parsing as untrusted (defensive parsing in the UI).
- ✅ No inline scripts in SVG, no HTML payloads, no weird MIME surprises.
- ✅ Don’t store credentials, tokens, or internal hostnames in fixtures.
- ✅ Prefer JSON over arbitrary embedded formats.

---

## ✅ Contribution checklist (Definition of Done)

When adding or updating a sample:

- [ ] The asset is **small** and within budgets
- [ ] A `sample.meta.json` exists and includes **license + sources**
- [ ] Sensitivity is set (`public` / `restricted` / etc.) and **CARE label** is present
- [ ] A `preview.webp/png` exists
- [ ] `samples.catalog.json` updated (if the UI needs to list it)
- [ ] No PII / sensitive cultural locations / restricted data
- [ ] No executable content (scripts, HTML payloads, SVG scripts)
- [ ] If derived, meta includes **how** it was derived (script, parameters, date)
- [ ] The UI renders it on desktop + mobile breakpoints (quick sanity check)

---

## 🧩 `samples.catalog.json` (registry file)

The catalog is a simple index the UI can read to populate “Samples” pickers.

```json
[
  {
    "id": "kfm.sample.vector.kansas-counties.v1",
    "title": "Kansas Counties (Demo)",
    "kind": "vector",
    "paths": {
      "meta": "vector/kansas-counties/sample.meta.json",
      "data": "vector/kansas-counties/data.geojson",
      "preview": "vector/kansas-counties/preview.webp",
      "style": "vector/kansas-counties/style.json"
    },
    "ui": {
      "map": { "center": [-98.0, 38.5], "zoom": 5.5 },
      "tags": ["kansas", "boundaries", "demo"]
    }
  }
]
```

---

## 🧰 Mini-recipes (how samples are usually produced)

> [!TIP]
> Keep generators in `tools/` or `src/pipelines/` and store the **output** here (small + stable).

Common patterns:
- 🗺️ Extract a tiny subset from PostGIS → export GeoJSON/TopoJSON  
- 🧼 Simplify geometry + reduce precision → shrink payload  
- 🖼️ Render a thumbnail → WebP  
- 🧾 Emit `sample.meta.json` + checksums → traceability  

---

## 🔗 Related KFM docs (recommended reading)

- 📘 Master Guide (pipeline + contracts): `docs/MASTER_GUIDE_v13.md`
- 🧾 Governance / ethics / sovereignty: `docs/governance/`
- 🧱 Schemas (STAC/DCAT/PROV/UI): `schemas/`
- 🗺️ Story Nodes templates: `docs/templates/`

---

## 📚 Reference shelf (project library) — *what shaped these conventions*

<details>
<summary><strong>Open the full project file index 📚✨</strong></summary>

### 🧠 Core KFM design & governance
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf
- Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design.pdf
- MARKDOWN_GUIDE_v13.md (Master Guide v13 draft)
- Comprehensive Markdown Guide: Syntax, Extensions, and Best Practices (docx)

### 🗺️ Cartography, GIS, and mapping UX
- Making Maps: A Visual Guide to Map Design for GIS
- Mobile Mapping: Space, Cartography and the Digital
- Archaeological 3D GIS
- Python Geospatial Analysis Cookbook
- Cloud-Based Remote Sensing with Google Earth Engine (Fundamentals & Applications)

### 🧊 3D, simulation, and modeling
- WebGL Programming Guide (Interactive 3D Graphics)
- Scientific Modeling and Simulation (NASA-grade guide)
- Generalized Topology Optimization for Structural Design
- Spectral Geometry of Graphs

### 📊 Stats, analysis, and uncertainty
- Understanding Statistics & Experimental Design
- Graphical Data Analysis with R
- Regression Analysis with Python (book)
- Regression Analysis using Python (slides)
- Think Bayes (Bayesian statistics in Python)

### 🗄️ Data systems & performance
- PostgreSQL Notes for Professionals
- Database Performance at Scale
- Scalable Data Management for Future Hardware
- Data Spaces

### ⚖️ Human-centered + legal/ethical framing
- Introduction to Digital Humanism
- On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age
- Principles of Biological Autonomy

### 🔐 Security awareness (for defensive posture only)
- Ethical Hacking and Countermeasures (secure network infrastructures)
- Gray Hat Python (security & reverse engineering)

### 🧰 Programming library bundles (multi-book PDFs)
- A programming Books.pdf
- B-C programming Books.pdf
- D-E programming Books.pdf
- F-H programming Books.pdf
- I-L programming Books.pdf
- M-N programming Books.pdf
- O-R programming Books.pdf
- S-T programming Books.pdf
- U-X programming Books.pdf

### 🖼️ Media formats
- Compressed Image File Formats (JPEG/PNG/GIF/XBM/BMP)

</details>

---

### ✅ Bottom line

If someone opens a sample six months from now, they should be able to answer:
**“What is this, why is it here, who can use it, and where did it come from?”** 🧭✅
