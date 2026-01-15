# 🏛️ Archaeology Sites — 3D Web Assets

![Asset Type](https://img.shields.io/badge/assets-3D%20archaeology%20sites-2b6cb0)
![Preferred Format](https://img.shields.io/badge/preferred-glTF%2FGLB-f59e0b)
![Provenance](https://img.shields.io/badge/provenance-required-22c55e)
![Sensitivity](https://img.shields.io/badge/sensitivity-supported-8b5cf6)
![Status](https://img.shields.io/badge/status-WIP-fbbf24)

> [!IMPORTANT]
> **If it shows up in the UI, it must be traceable.**  
> This folder follows a **contract-first + provenance-first** approach: no “mystery assets,” ever. 🧾🔍

---

## 🎯 Purpose

This directory contains **web-ready 3D assets** (and their **metadata**) for archaeological sites used by the Kansas Frontier Matrix web experience.

✅ Optimized for **fast loading** in browsers  
✅ Designed for **auditability** (sources + licenses + processing steps)  
✅ Supports **ethical publishing** (sensitive sites / redacted locations)  

---

## 📦 What belongs here (and what doesn’t)

### ✅ Belongs here
- **Web-friendly** models (`.glb` / glTF 2.0), LODs, thumbnails 🧊
- **Site metadata** (“data contract”) for provenance + usage terms 🧾
- **Viewer-friendly** transforms (local-to-world) and bounds 🧭

### ❌ Does *not* belong here
- Raw photogrammetry projects (`.psx`, `.rcproj`) or raw scans
- Massive un-decimated meshes or uncompressed textures
- Anything without a clear **license + source + attribution**

> [!TIP]
> Keep raw source material in a separate **ingestion / pipeline** location. This folder is the **published** (web) artifact layer.

---

## 🗂️ Folder layout

Each site gets a **single folder** (kebab-case slug), containing a minimal “site package”.

```text
web/assets/3d/archaeology/sites/
├─ 📘 README.md                       ← you are here
├─ 🏺 <site-slug>/
│  ├─ 🧾 site.meta.json                ← REQUIRED (data contract + viewer hints)
│  ├─ 🖼️ preview.jpg|png               ← REQUIRED (card/thumbnail)
│  ├─ 📦 models/
│  │  ├─ 🧊 <site-slug>_lod0.glb        ← OPTIONAL (hero/high)
│  │  ├─ 🧊 <site-slug>_lod1.glb        ← REQUIRED (default)
│  │  └─ 🧊 <site-slug>_lod2.glb        ← OPTIONAL (mobile/low)
│  ├─ 🧩 textures/                     ← OPTIONAL (prefer embedded/KTX2)
│  └─ 📄 README.md                     ← OPTIONAL (site-specific notes)
```

---

## 🏷️ Naming conventions

- **Site folder**: `lowercase-kebab-case`
  - ✅ `pawnee-rock`
  - ✅ `smoky-hill-river-terrace`
  - ❌ `PawneeRock` / `Pawnee_Rock` / `site01`

- **Model files**:
  - `models/<site-slug>_lod{n}.glb`
  - If only one model exists, use **LOD1** as default.

---

## 🧾 Required metadata: `site.meta.json`

This file is the **single source of truth** for:
- provenance (sources, attribution, license)
- spatial/temporal extent (as appropriate)
- processing history
- viewer hints (units, up-axis, transforms, bounds, LOD selection)
- sensitivity controls (location redaction)

### ✅ Minimum required fields

| Field | Required | Why |
|------|----------|-----|
| `id`, `slug`, `title` | ✅ | stable identifiers + UI display |
| `license.spdx` + `license.attribution` | ✅ | legal + credit |
| `sources[]` | ✅ | traceability |
| `processing[]` | ✅ | reproducibility + trust |
| `location.visibility` | ✅ | sensitive-site handling |
| `assets.models[]` | ✅ | links to `.glb` files |
| `viewer.units`, `viewer.upAxis` | ✅ | correct scale/orientation |

---

## 🧩 `site.meta.json` template (copy/paste)

> [!NOTE]
> This is intentionally “STAC-ish” without forcing full STAC compliance inside `web/assets/`.  
> If you later publish to a catalog, this structure can be mapped into STAC/DCAT/PROV-O.

```json
{
  "schemaVersion": "1.0",
  "id": "kfm-arch-site-example-001",
  "slug": "example-site",
  "title": "Example Site (Placeholder)",
  "summary": "Short description suitable for a site card.",
  "siteType": "archaeological-site",

  "period": {
    "label": "Unknown / TBD",
    "startYear": null,
    "endYear": null
  },

  "location": {
    "visibility": "generalized",
    "crs": "EPSG:4326",
    "centroidLonLat": [-95.0000, 39.0000],
    "bboxLonLat": [-95.0010, 38.9990, -94.9990, 39.0010]
  },

  "assets": {
    "preview": "preview.jpg",
    "models": [
      {
        "path": "models/example-site_lod1.glb",
        "lod": 1,
        "role": "default",
        "units": "m",
        "trianglesApprox": 150000,
        "bytesApprox": 12000000,
        "sha256": "REPLACE_ME"
      }
    ]
  },

  "viewer": {
    "units": "m",
    "upAxis": "Y",
    "recommendedLod": 1,

    "georeferencing": {
      "strategy": "local-enu-anchor",
      "anchorLonLatH": [-95.0000, 39.0000, 0.0],
      "notes": "Mesh stored near origin for WebGL precision; anchor places it on the globe/map."
    }
  },

  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Replace with required attribution text (institution, project, authors).",
    "restrictions": "Any additional usage terms (if applicable)."
  },

  "sources": [
    {
      "type": "primary",
      "title": "Field photogrammetry capture (Example)",
      "publisher": "Replace",
      "date": "YYYY-MM-DD",
      "citation": "Replace with formal citation (preferred).",
      "url": null,
      "notes": "Where this came from and what permission was granted."
    }
  ],

  "processing": [
    {
      "step": "Photogrammetry reconstruction",
      "tool": "Agisoft Metashape (or equivalent)",
      "date": "YYYY-MM-DD",
      "inputs": ["photoset-001"],
      "outputs": ["models/example-site_lod1.glb"],
      "notes": "Key settings, alignment method, scaling/georeferencing method."
    },
    {
      "step": "Mesh cleanup + decimation + export",
      "tool": "Blender / MeshLab / pipeline tool",
      "date": "YYYY-MM-DD",
      "notes": "Decimation target, texture bake details, compression choices."
    }
  ],

  "sensitivity": {
    "isSensitive": false,
    "reason": null,
    "publishExactLocation": false
  }
}
```

---

## 🧭 Georeferencing strategy (web-friendly)

Archaeological 3D workflows often produce **georeferenced models** using ground control points (GCPs). That’s great for GIS—  
…but for the web, extremely large coordinate values can cause **precision issues**.

### ✅ Recommended approach: **local model + anchor**
- Keep the mesh in **local coordinates near (0,0,0)** (meters).
- Store an **anchor** (lon/lat/elevation) + notes in `site.meta.json`.
- If needed, also store a transform matrix in metadata (future expansion).

> [!TIP]
> This mirrors common GIS↔️3D workflows where models may be exported in geo coordinates *or* replaced with a local-coordinate copy to avoid scale/projection problems.

---

## 🧊 Model format + optimization rules

### Preferred format
- ✅ **glTF 2.0 binary (`.glb`)** for the web viewer

### Strongly recommended
- 🔻 **LOD tiers** (`lod0`, `lod1`, `lod2`)
- 🧵 Texture optimization (downscale huge textures, avoid excessive unique maps)
- 🗜️ Compression where supported by your viewer pipeline
  - geometry compression (e.g., Draco / meshopt)
  - texture compression (e.g., KTX2/Basis)

### Practical budgets (guidelines, not laws)
- `lod1` target: **~100k–300k triangles**, **< 25 MB** per model (when possible)
- Mobile `lod2`: **< 100k triangles**, aggressively compressed textures

---

## 🧪 QA checklist (PR gate vibes ✅)

Before a site is “publishable”:

- [ ] `site.meta.json` exists and includes **source + license + attribution**
- [ ] `processing[]` includes at least **two steps** (reconstruction + web export)
- [ ] `preview.jpg/png` exists and looks correct
- [ ] Model opens correctly (scale, orientation, textures)
- [ ] Units confirmed (`viewer.units: "m"`)
- [ ] Sensitivity reviewed (`location.visibility`, `sensitivity.*`)
- [ ] Hashes filled in (at least `sha256` for default model)
- [ ] No raw/private data accidentally included

---

## 🧭 Ethics, privacy, and sensitive sites

> [!WARNING]
> Publishing high-fidelity 3D data + exact locations can increase looting risk and can violate community expectations.

Use `location.visibility` + `sensitivity` fields to control what’s public:
- `exact` → only when explicitly allowed
- `generalized` → centroid/bbox fuzzed (recommended default)
- `hidden` → no coordinates in public web assets

Also consider:
- consultation with descendant / stakeholder communities
- redaction of vulnerable features (burials, caches, etc.)
- “need-to-know” access patterns for private datasets

---

## 🔁 Suggested pipeline (from field → web)

```mermaid
flowchart LR
  A[📸 Capture: photos / scans] --> B[🧭 Scale + georeference (GCPs)]
  B --> C[🧼 Clean mesh + decimate]
  C --> D[🧊 Export GLB + LODs]
  D --> E[🧾 Write site.meta.json (contract)]
  E --> F[✅ Validate: license + sources + hashes]
  F --> G[🌐 Publish to web/assets/…/sites/<slug>/]
```

---

## 📚 References (project grounding)

- **KFM technical design:** contract-first + provenance-first; metadata required for anything surfaced in UI.  
- **Archaeological 3D GIS practice:** field-to-GIS workflows, building reusable 3D model libraries, georeferencing + publication patterns.  
- **Digital humanism:** human-centered, privacy/security-aware design—useful when dealing with sensitive cultural heritage.

---

## ✅ Next good additions (optional, future-proofing)

<details>
<summary>✨ Ideas we can implement soon</summary>

- 📄 `site.meta.schema.json` (JSON Schema) + validator in CI
- 🧾 `CITATION.cff` or `citations.bib` per site for clean academic export
- 🗺️ Auto-generated STAC items from `site.meta.json`
- 🧪 Model linting (triangle count, embedded textures, missing normals)
- 🧠 Hook metadata into Focus Mode citations/attribution rendering

</details>
