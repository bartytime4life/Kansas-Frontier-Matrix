---
title: "🪨 Monument Rocks — 3D Model Sources"
path: "web/assets/3d/shared/models/monument-rocks/sources/README.md"
version: "v0.1.0"
status: "draft"
last_updated: "2026-01-16"
doc_kind: "Asset Source README"
license: "TBD"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
asset_id: "kfm:asset:3d:model:monument-rocks"
export_targets:
  - "glTF 2.0 (.gltf/.glb)"
  - "Cesium/3D Tiles (optional)"
---

# 🪨 Monument Rocks — Sources (3D Model)

![status](https://img.shields.io/badge/status-draft-yellow)
![asset](https://img.shields.io/badge/asset-3D%20model-blue)
![export](https://img.shields.io/badge/export-glTF%2FGLB-7c3aed)
![provenance](https://img.shields.io/badge/provenance-required-111827)

> [!IMPORTANT]
> This `sources/` folder is the **authoring + provenance home** for the Monument Rocks model.
> It may contain *large* raw inputs (photos, scans, point clouds) and tool project files.
> **Do not** import these directly into the web app — ship only the optimized exports.

---

## 📘 Overview

### Purpose 🎯
This folder exists so we can:
- ✅ Rebuild the Monument Rocks 3D model from scratch (repeatable pipeline)
- ✅ Prove where every input came from (provenance-first)
- ✅ Export **web-ready** assets (glTF/GLB, optionally 3D Tiles) for the KFM front-end viewer(s) (Cesium, etc.)[^kfm-web-viewers][^kfm-3d-modeling-plan]

### Audience 👥
- 🧑‍💻 Devs integrating the model into the KFM web viewer
- 🧑‍🎨 3D/geo folks maintaining photogrammetry + optimization steps
- 🧾 Reviewers checking **license + provenance** before anything ships

### Key terms (quick defs) 🧠
- **Photogrammetry / image-based 3D modeling**: reconstructing a 3D scene from overlapping photos into a dense point cloud + textured mesh.[^img-based-3d-modeling]
- **glTF / GLB**: common web-friendly formats for 3D assets; GLB is the binary “single-file” variant.
- **3D Tiles**: streaming format commonly used with Cesium for large geospatial 3D content.[^kfm-web-viewers]

---

## 🎯 Scope

| ✅ In scope (belongs here) | 🚫 Out of scope (belongs elsewhere) |
|---|---|
| 📸 Raw & selected photo sets (EXIF preserved) | 🧳 Final web payloads that are served in production |
| 🧩 Photogrammetry project files (Metashape / Meshroom / etc.) | 🗺️ Unattributed “mystery” assets (not allowed) |
| ☁️ Point clouds, intermediate meshes, decimation logs | 🔁 Duplicated exports (keep one canonical export set) |
| 🧠 Blender/source scene files, bake configs | 🧪 Experimental WIP files not tied to a reproducible build |
| 🧾 Provenance + license documentation | 🧱 App code (React/Cesium/MapLibre) |

---

## 🗂️ Expected directory layout

> [!NOTE]
> If your actual layout differs, **update this README** so future rebuilds don’t require archeology.  
> (This is intentionally “canonical” rather than guessing file names.)

```text
📁 web/assets/3d/shared/models/monument-rocks/
└─ 📁 sources/
   ├─ 📄 README.md                        ← you are here 🧭
   ├─ 📁 provenance/                      ← “no mystery layers” zone ✅
   │  ├─ 📄 metadata.json                 ← required data contract (template below)
   │  ├─ 📄 LICENSE.txt                   ← license text or pointer
   │  └─ 📄 ATTRIBUTION.md                ← credits + attributions
   ├─ 📁 photos_raw/                      ← untouched originals (prefer LFS)
   ├─ 📁 photos_selected/                 ← curated set used for reconstruction
   ├─ 📁 reconstruction/                  ← photogrammetry outputs (dense cloud, mesh)
   ├─ 📁 cleanup/                         ← retopo/decimation/mesh fixes
   ├─ 📁 textures/                        ← bakes + texture atlases
   ├─ 📁 blender/                         ← .blend and supporting files
   ├─ 📁 exports/                         ← glTF/GLB exports (candidate “ship” assets)
   └─ 📁 qa/                              ← validation reports, screenshots, perf notes
```

---

## 🔍 Provenance & licensing (non‑negotiable)

KFM’s architecture is explicitly **contract-first**: each dataset (and by extension, each asset intended to be shipped) should have structured metadata describing **source, license, processing steps, extents, etc.**.[^kfm-data-contract]  
This is part of an “evidence-first / no mystery layers” trust model — unsourced assets should not enter the official catalog.[^kfm-data-contract]

Also: the design guidance calls out the need to keep data source documentation clear, including **license, retrieval method, and date accessed**.[^kfm-design-audit-data-sources]

### ✅ Minimum required provenance artifacts
Place these in `sources/provenance/`:

- `metadata.json` *(required)*
- `LICENSE.txt` *(required — even if it just points to a license URL or states “TBD”)*
- `ATTRIBUTION.md` *(required if any third-party material exists)*

### 📄 `metadata.json` template (copy/paste)
> [!TIP]
> Keep the file **machine-parseable** (JSON only; no comments).  
> Treat it like a “data contract” that CI can validate.[^kfm-data-contract][^md-ci-validation]

```json
{
  "id": "kfm:asset:3d:model:monument-rocks",
  "title": "Monument Rocks — 3D Model (Source Package)",
  "type": "3d_model_sources",
  "status": "draft",
  "created_utc": "TBD",
  "last_updated_utc": "2026-01-16T00:00:00Z",

  "location": {
    "name": "Monument Rocks (Kansas)",
    "spatial_extent": "TBD",
    "crs": "TBD"
  },

  "sources": [
    {
      "kind": "photography",
      "description": "Primary photo set used for photogrammetry reconstruction.",
      "creator": "TBD",
      "date_captured": "TBD",
      "retrieval_method": "field_capture | archive_download | third_party_provided",
      "date_accessed": "TBD",
      "license": "TBD",
      "proof": {
        "hash_manifest": "TBD",
        "notes": "Preserve originals + EXIF; record any edits."
      }
    }
  ],

  "processing_steps": [
    "TBD: photo selection criteria",
    "TBD: photogrammetry reconstruction settings",
    "TBD: cleanup/decimation strategy",
    "TBD: texture baking settings",
    "TBD: export settings (glTF/GLB)"
  ],

  "export_targets": [
    "glTF 2.0 (.glb) for web viewer",
    "Optional: 3D Tiles tileset for Cesium streaming"
  ],

  "license_summary": {
    "intended_license": "TBD",
    "notes": "If any third-party inputs exist, verify compatibility before shipping."
  },

  "care": {
    "fair_category": "FAIR+CARE",
    "care_label": "Public",
    "sensitivity_notes": "If sensitive/culturally restricted information is present, update care_label and redact as needed."
  }
}
```

### 🧷 Care & sensitivity notes
If any source content reveals sensitive info (e.g., precise coordinates of restricted sites, identifiable people, etc.), flag it clearly and set `care_label` accordingly.[^md-front-matter-dod]

---

## 🏗️ Build & export pipeline

> [!NOTE]
> The KFM roadmap anticipates using photogrammetry + tools like Blender, exporting assets to **glTF** for web display.[^kfm-3d-modeling-plan]

### 1) Capture 📸
- Use overlapping images (ground + drone if available).
- Preserve originals and EXIF where possible (avoid “helpful” auto-editing that breaks repeatability).

### 2) Reconstruct (photogrammetry) 🧩
Image-based 3D modeling can generate **geometrically accurate textured models** and **dense point clouds** from a set of digital images, via camera estimation + feature matching + dense reconstruction.[^img-based-3d-modeling]

### 3) Cleanup & optimization 🧼
Typical tasks:
- Remove floaters / background geometry
- Fix normals
- Reduce poly count / generate LODs
- Create texture atlases and bake down materials for runtime performance

> [!TIP]
> A documented workflow can include tools like Metashape + CloudCompare for point cloud/mesh processing before GIS/visualization import/export.[^metashape-cloudcompare]

### 4) Export 📦
- **Primary target:** `.glb` (single-file, web-friendly)
- Optional streaming target: **3D Tiles** if/when needed for large geospatial assets in Cesium.[^kfm-web-viewers]

### 5) Integrate in the KFM web viewer 🌐
The KFM web front-end includes viewer components and mentions integration of MapLibre (2D) and **Cesium (3D globe/terrain)**, with Cesium used for streaming 3D geospatial content (3D Tiles standard).[^kfm-web-viewers]

> [!IMPORTANT]
> If you change exports, also update:
> - `provenance/metadata.json`
> - `ATTRIBUTION.md` (credits)
> - `qa/` (validation + screenshots)

---

## ✅ Definition of Done (DoD) for this asset

KFM-style documentation governance encourages templates, front-matter, and a clear **Definition of Done** checklist so reviews can verify provenance + correctness like code.[^md-front-matter-dod]

### ✅ Ship-ready checklist
- [ ] YAML front-matter is filled in (status/version/last_updated/license)
- [ ] `provenance/metadata.json` exists and is accurate (sources, license, processing steps)[^kfm-data-contract]
- [ ] License compatibility verified; attributions written (no legal ambiguity)[^kfm-license-care]
- [ ] Raw inputs stored safely (prefer Git LFS for large photo sets)
- [ ] Rebuild steps documented (someone else can reproduce the export)
- [ ] Exported GLB validates (glTF validator) and renders correctly
- [ ] Performance sanity: loads fast enough for web (document target budgets in `qa/`)
- [ ] Any sensitive info handled (care_label updated; redactions applied if needed)[^md-front-matter-dod]
- [ ] README updated if folder structure changes
- [ ] Peer review completed (provenance + license + visual QA)

---

## 📚 References (project docs)

[^kfm-data-contract]: KFM “contract-first” approach requires each dataset to have a metadata JSON (source, license, extents, processing steps) and enforces provenance; “mystery layers” are not permitted.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^kfm-license-care]: KFM emphasizes careful license handling to avoid conflicts and support collaboration/adoption.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^kfm-web-viewers]: KFM web app structure includes viewer components integrating MapLibre GL JS (2D) and CesiumJS (3D), and references using the open 3D Tiles standard via Cesium for streaming geospatial 3D content.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^kfm-3d-modeling-plan]: KFM design notes anticipate leveraging photogrammetry plus tools like Blender/SketchUp and exporting to glTF for web display.  [oai_citation:3‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

[^kfm-design-audit-data-sources]: Design audit calls out the importance of documenting data sources and ensuring entries include license, retrieval method, and date accessed (STAC-like catalog metadata).  [oai_citation:4‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)

[^img-based-3d-modeling]: Image-based 3D modeling workflow description: create accurate textured models + dense point clouds from images using camera estimation, feature matching, and dense reconstruction.  [oai_citation:5‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

[^metashape-cloudcompare]: Example documented workflow referencing Metashape + CloudCompare to process imagery-derived models/point clouds and generate usable mesh outputs.  [oai_citation:6‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

[^md-front-matter-dod]: Markdown governance guidance: use front-matter fields (incl. care_label), templates, and a Definition of Done checklist emphasizing “front-matter complete” and “all facts cited.”  [oai_citation:7‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

[^md-ci-validation]: Documentation quality can be enforced via CI (schema validation for front-matter + required structure).  [oai_citation:8‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
