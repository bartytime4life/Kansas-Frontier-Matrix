---
title: "3D Landmark Asset — <Landmark Name>"
path: "web/assets/3d/landmarks/<landmark_slug>/README.md"
version: "v0.1.0"
last_updated: "YYYY-MM-DD"
status: "draft" # draft | active | deprecated
doc_kind: "Asset README"
license: "CC-BY-4.0" # README text license (does not automatically apply to the 3D model)

# KFM protocol / governance
markdown_protocol_version: "1.0"
pipeline_contract_version: "v13"
care_label: "Public" # Public | Restricted | Tribal Sensitive | ...
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

# Asset identity
asset_kind: "3d_landmark"
landmark_slug: "<landmark_slug>"   # stable folder/URL slug (no spaces; keep forever once published)
landmark_display_name: "<Landmark Name>"

# Optional: link this asset into the governed catalogs
kfm_catalog_refs:
  stac_item: "data/stac/items/landmarks/<landmark_slug>.json"
  dcat_dataset: "data/catalog/dcat/landmarks/<landmark_slug>.json"
  prov_jsonld: "data/prov/landmarks/<landmark_slug>.jsonld"
---

<p align="center">
  <img alt="KFM Landmark" src="https://img.shields.io/badge/KFM-3D%20Landmark-2b6cb0">
  <img alt="Provenance First" src="https://img.shields.io/badge/Provenance--First-Required-2ea44f">
  <img alt="STAC/DCAT/PROV" src="https://img.shields.io/badge/Metadata-STAC%20%7C%20DCAT%20%7C%20PROV-6f42c1">
  <img alt="glTF" src="https://img.shields.io/badge/Format-glTF%20%2F%20GLB-111827">
  <img alt="Status" src="https://img.shields.io/badge/Status-draft-f59e0b">
</p>

# 🗿 <Landmark Name> — 3D Asset Pack

> **What this folder is:** the **frontend-distributable** 3D model bundle for a single landmark.  
> **What this folder is *not*:** the full reconstruction workspace (raw captures, dense point clouds, Blender project files, etc.).

---

## 🧭 Overview

### Purpose 🎯
Provide a **fast, web-friendly 3D representation** of `<Landmark Name>` for the KFM UI (WebGL/Cesium/Map experiences), with **traceable provenance** and repeatable build steps.

### Scope ✅ / ❌
| In scope ✅ | Out of scope ❌ |
|---|---|
| GLB/glTF + textures + previews | Raw capture datasets (photos/LiDAR) |
| Georeference anchor + orientation | High-poly sculpt / film-grade meshes |
| Licensing + attribution | “Mystery” assets with unknown source |
| Links to STAC/DCAT/PROV artifacts | Narrative/story text (belongs in Story Nodes) |

### Audience 👥
- **Developers** wiring the UI viewer
- **Data stewards** verifying provenance + licensing
- **3D pipeline contributors** updating models safely

---

## 🗂️ Directory Layout

```text
web/assets/3d/landmarks/<landmark_slug>/
├─ README.md                     📘 this file
├─ model.glb                     🧊 primary runtime model (recommended)
├─ preview.webp                  🖼️ lightweight preview (UI cards)
├─ preview.jpg                   🖼️ fallback preview
├─ manifest.json                 🧾 optional: loader-friendly manifest (recommended)
├─ metadata.json                 🏷️ optional: human-friendly metadata (recommended)
├─ attribution.md                🧾 required if any upstream attribution is needed
├─ licenses/                     ⚖️ optional: license texts or notices
│  └─ LICENSES.md
└─ textures/                     🎨 optional: if external textures (avoid if GLB embeds)
   ├─ albedo.webp
   ├─ normal.webp
   └─ orm.webp
```

> ✅ **Rule of thumb:** if the UI can’t load it deterministically from this folder, it doesn’t belong here.

---

## 📦 Asset Manifest

### Required files (minimum viable) ✅
| File | Required | Why |
|---|---:|---|
| `model.glb` | ✅ | Single-file runtime asset for web |
| `preview.webp` | ✅ | Fast UI preview |
| `attribution.md` | ✅ | Ensures legal + ethical reuse |

### Recommended files ✨
| File | Recommended | Why |
|---|---:|---|
| `manifest.json` | ⭐ | One “entry point” for loaders + metadata |
| `metadata.json` | ⭐ | Easy human inspection; mirrors contract fields |
| `preview.jpg` | ⭐ | Fallback for browsers without WebP |
| `textures/*` | ⭐ | Only if you choose glTF+external textures |

---

## 🧾 manifest.json (recommended)

If you include a manifest, keep it **tiny** and **loader-friendly**.

```json
{
  "id": "kfm:landmark:<landmark_slug>",
  "name": "<Landmark Name>",
  "files": {
    "model_glb": "model.glb",
    "preview_webp": "preview.webp",
    "preview_jpg": "preview.jpg"
  },
  "georeference": {
    "crs": "EPSG:4326",
    "anchor_wgs84": { "lat": 0.0, "lon": 0.0, "height_m": 0.0 },
    "heading_pitch_roll_deg": { "heading": 0, "pitch": 0, "roll": 0 }
  },
  "provenance": {
    "stac_item": "../../../../../data/stac/items/landmarks/<landmark_slug>.json",
    "dcat_dataset": "../../../../../data/catalog/dcat/landmarks/<landmark_slug>.json",
    "prov_jsonld": "../../../../../data/prov/landmarks/<landmark_slug>.jsonld"
  }
}
```

---

## 🗺️ Georeferencing & Coordinate Policy

### Anchor 📍
Record the **single authoritative** anchor for the landmark in WGS84 (EPSG:4326):

- **Latitude:** `<lat>`
- **Longitude:** `<lon>`
- **Height (meters):** `<height_m>` (ellipsoidal or orthometric — specify which!)

### Orientation 🧭
- **Heading / Pitch / Roll** in degrees (or provide a transform matrix).
- Document any “artist-friendly” adjustments (e.g., rotate to face camera) and *why*.

### CRS notes 🧠
- Preserve **original CRS** used during processing (if not EPSG:4326) and state how/when reprojection happened.
- If you generalize/redact coordinates for sensitive locations, document the rule here and in the catalog artifacts.

---

## 🧬 Provenance, Licensing, Attribution

### Attribution (required) 🧾
Put **human-readable** credit in `attribution.md`.

Recommended template:

```md
## Attribution

**Asset:** <Landmark Name> (3D model)  
**Source(s):** <source name + link / archive reference>  
**License:** <license>  
**Copyright:** <holder>  
**Modifications:** <what changed (decimation, retexture, cleanup)>  
**Date accessed / captured:** <YYYY-MM-DD>  
```

### Provenance “hard gate” 🚧
This landmark must be traceable to **source + processing steps**. If provenance can’t be established, **do not ship** the asset into `web/assets/`.

---

## 🧪 Build / Optimization Notes

> Keep the UI snappy 📱💨 — the goal is “loads fast, looks good, documented well.”

### Recommended web budgets (tune as needed) ⚡
- Target **GLB size:** `< 10–20 MB` (mobile-first target)
- Target **triangles:** `< 100k–300k` (depends on device + scene)
- Textures:
  - Prefer **WebP** (or **KTX2** if the pipeline supports it)
  - Limit max texture dimension to `2K` unless justified

### Suggested optimization steps 🧰
- Mesh cleanup: remove hidden faces, weld seams, fix normals
- LODs (optional): `model_lod0.glb`, `model_lod1.glb`, ...
- Compression:
  - geometry: Draco / meshopt (if your runtime supports it)
  - textures: WebP / KTX2

---

## ✅ Validation Checklist

### Model validation 🧊
- [ ] GLB loads in the **target viewer** (three.js / Cesium / etc.)
- [ ] Correct scale (meters) and orientation
- [ ] No missing textures
- [ ] Acceptable performance on mid-tier mobile

### Metadata validation 🏷️
- [ ] `attribution.md` complete
- [ ] `manifest.json` (if present) valid JSON
- [ ] STAC/DCAT/PROV references exist (if this landmark is “official”)

### Governance / safety 🛡️
- [ ] No sensitive location leaked (if applicable)
- [ ] License allows redistribution in this repo
- [ ] Any redactions/generalizations are documented

---

## 🔌 UI Integration Notes

> Implementation varies by app, but **don’t hardcode magic paths** in multiple places.

Recommended approach:
1. Loader reads `manifest.json` (or a centralized registry)
2. UI shows `preview.webp`
3. Viewer loads `model.glb`
4. “Inspect provenance” links jump to the catalog artifacts

<details>
<summary>Example pseudo-loader (JS) 📎</summary>

```js
// Pseudocode — adapt to your actual KFM web app structure
async function loadLandmark(slug) {
  const base = `/assets/3d/landmarks/${slug}/`;
  const manifest = await fetch(base + "manifest.json").then(r => r.json());

  const modelUrl = base + manifest.files.model_glb;
  const previewUrl = base + manifest.files.preview_webp;

  return { manifest, modelUrl, previewUrl };
}
```
</details>

---

## 🕰️ Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| YYYY-MM-DD | v0.1.0 | Initial asset drop | @<handle> |

---

## ✅ Definition of Done (for this asset folder)

- [ ] Front-matter present & updated
- [ ] Files match Directory Layout (or documented deviations)
- [ ] Attribution + license confirmed
- [ ] Provenance references added (STAC/DCAT/PROV) **or** explicitly marked “unpublished”
- [ ] Validation checklist completed
- [ ] No sensitive info exposed (CARE / sovereignty respected)

---

### 🔗 Related KFM Docs (repo-relative)
- `../../../../../docs/MASTER_GUIDE_v13.md`
- `../../../../../docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
- `../../../../../docs/standards/KFM_STAC_PROFILE.md`
- `../../../../../docs/standards/KFM_DCAT_PROFILE.md`
- `../../../../../docs/standards/KFM_PROV_PROFILE.md`
