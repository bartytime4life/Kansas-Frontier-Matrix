# 🧊 3D Model Asset Template (KFM)

![Status](https://img.shields.io/badge/status-template-blue)
![Format](https://img.shields.io/badge/format-glTF%202.0-orange)
![Runtime](https://img.shields.io/badge/runtime-MapLibre%20%2F%20WebGL%20%2B%20Cesium-6f42c1)
![Metadata](https://img.shields.io/badge/metadata-required-brightgreen)
![Provenance](https://img.shields.io/badge/provenance-citation--first-0aa)

> 🧰 This folder is a **copyable template** for shipping **web-ready 3D models** into KFM’s UI.
>
> ✅ Copy → Rename → Replace placeholders → Validate → Ship  
> ❌ Don’t drop raw source chaos into `web/` (keep the web runtime folder lean).

---

## 🎯 What this template is for

Use this template when you want a 3D asset that:

- can be loaded quickly in the browser (WebGL)
- is stable to reference by ID (🧷 “stable IDs forever” philosophy)
- includes **metadata + provenance** so it can be used in Story Nodes / UI popovers / catalogs
- can optionally be used in a 3D mode (e.g., Cesium) without re-authoring

---

## 🧭 Quick start (copy/paste workflow)

1) **Copy this folder**
```bash
# from: web/assets/3d/shared/models/_template
# to:   web/assets/3d/shared/models/<model-id>
cp -R web/assets/3d/shared/models/_template web/assets/3d/shared/models/<model-id>
```

2) **Rename placeholders**
- Replace every `<MODEL_ID>` and `<...>` token in this README + `model.json`.

3) **Drop in your runtime artifacts**
- `model.glb` (recommended) or `model.gltf` + `textures/`
- `preview.webp` (thumbnail used by UI)

4) **Validate**
- Open in a viewer (Blender / Windows 3D Viewer / online glTF viewer)
- Run a glTF validator (recommended)
- Confirm orientation, scale, and materials (see checklist below)

---

## 📦 Folder layout

> Keep it boring. Keep it predictable. ✅

```text
📁 web/assets/3d/shared/models/<MODEL_ID>/
├─ 📄 README.md               # this file (filled out)
├─ 🧾 model.json              # metadata + provenance manifest (required)
├─ 🧊 model.glb               # runtime model (preferred: binary GLB)
├─ 🖼️ preview.webp            # UI thumbnail (required)
├─ 🧵 textures/               # optional (if not embedded in GLB)
│  ├─ 🖼️ basecolor.ktx2
│  ├─ 🖼️ normal.ktx2
│  └─ 🖼️ orm.ktx2
└─ 🧪 validation/             # optional (reports, screenshots)
   ├─ 📄 gltf-validator.json
   └─ 🖼️ viewer-screenshot.png
```

---

## ✅ Required files

| File | Required | Why |
|---|---:|---|
| `README.md` | ✅ | Human context + usage + provenance summary |
| `model.json` | ✅ | Machine-readable metadata + provenance |
| `model.glb` (or `.gltf`) | ✅ | Runtime asset |
| `preview.webp` | ✅ | UI card/list thumbnail |

---

## 🧾 `model.json` — metadata + provenance (REQUIRED)

> **KFM rule of thumb:** if it’s important enough to ship to the UI, it’s important enough to describe. ✅

### 🔑 Minimum fields (must-fill)

- `id` (**stable**, kebab-case): `my-historic-site-monument-rocks`
- `title`: human-readable name
- `summary`: 1–2 sentence plain-language description
- `tags`: discovery (search/filter)
- `license`: SPDX-ish string (or clear license name)
- `attribution`: who/what must be credited
- `provenance.sources[]`: where did this come from (citations + links + archive refs)
- `provenance.processing[]`: how was it produced (tools + steps)
- `geo`: how it should be placed (if georeferenced)
- `runtime`: defaults (scale/orientation/camera)

### 🧩 Template manifest (copy + edit)

```json
{
  "id": "<MODEL_ID>",
  "version": "0.1.0",
  "title": "<Human title>",
  "summary": "<1–2 sentence description of what this model represents and why it exists in KFM.>",
  "tags": ["kansas", "landmark", "history", "3d"],
  "license": "<e.g., CC-BY-4.0 | CC0-1.0 | MIT | Proprietary-Restricted>",
  "attribution": {
    "credit_line": "<Required credit line shown in UI>",
    "creators": ["<Name/Org>"],
    "year": "<YYYY>"
  },

  "files": {
    "primary": "model.glb",
    "preview": "preview.webp",
    "extras": {
      "validation_report": "validation/gltf-validator.json"
    }
  },

  "units": "meters",
  "axes": {
    "up": "+Y",
    "handedness": "right"
  },

  "geo": {
    "is_georeferenced": false,
    "crs": "EPSG:4326",
    "anchor": {
      "lon": 0.0,
      "lat": 0.0,
      "height_m": 0.0
    },
    "orientation": {
      "heading_deg": 0,
      "pitch_deg": 0,
      "roll_deg": 0
    },
    "local_axes_note": "If georeferenced, document how model local axes map to ENU/North."
  },

  "runtime": {
    "default_scale": 1.0,
    "default_camera": {
      "type": "orbit",
      "target": [0, 0, 0],
      "distance": 12,
      "min_distance": 2,
      "max_distance": 80
    },
    "lod": [
      { "name": "lod0", "file": "model.glb", "max_screen_error": 0 }
    ]
  },

  "classification": {
    "sensitivity": "public",
    "notes": "If any restriction exists, document it here and ensure outputs are not less restricted than inputs."
  },

  "provenance": {
    "sources": [
      {
        "type": "archive|publication|survey|photogrammetry|lidar|artist",
        "title": "<Source title>",
        "author": "<Author/Org>",
        "date": "<YYYY-MM-DD or YYYY>",
        "citation": "<Chicago/APA/etc — keep consistent across KFM>",
        "url": "<https://...>",
        "accessed": "<YYYY-MM-DD>",
        "license": "<source license/terms>",
        "notes": "<Any constraints, interpretation warnings, or redactions>"
      }
    ],
    "processing": [
      {
        "step": "modeling|photogrammetry|cleanup|retopo|bake|compress|convert",
        "tool": "<Blender / Metashape / CloudCompare / ...>",
        "tool_version": "<version>",
        "params": { "notes": "Record key settings that affect reproducibility." },
        "performed_by": "<name/org>",
        "performed_at": "<YYYY-MM-DD>",
        "outputs": ["model.glb", "preview.webp"]
      }
    ],
    "checksums": {
      "model.glb": "sha256:<TODO>",
      "preview.webp": "sha256:<TODO>"
    }
  }
}
```

---

## 🌍 Geospatial conventions (if your model is placeable on the map)

### ✅ Coordinate system standard
- Treat **WGS84 / EPSG:4326** as the UI-facing default (store original CRS in provenance if different).
- Use **meters** for model units (scale must be explicit and consistent).

### 📌 Anchoring strategy (recommended)
To avoid float precision issues in the browser:

- store an **anchor** position in `EPSG:4326` (lon/lat/height)
- keep the model geometry **near the origin** (0,0,0) in local meters
- apply translation/rotation in the viewer at runtime

### 🧭 Orientation expectations
- glTF is typically **right-handed** with **+Y up**.
- If your authoring tool uses a different up-axis (e.g., Z-up), convert during export and document it in `model.json`.

---

## 🎛️ Performance & packaging (web-first rules)

### ✅ Recommended defaults
- Prefer **`.glb`** with textures embedded *unless* you’re using KTX2 (then keep in `textures/`)
- Keep texture sizes reasonable (power-of-two preferred: 512/1024/2048/4096)
- Reduce draw calls (merge meshes/materials where sensible)

### 🧱 Suggested budgets (guidelines, not laws)
- **Small props:** 5k–50k triangles
- **Medium landmarks:** 50k–250k triangles (use LODs)
- **Large terrain/structures:** consider tiling / 3D Tiles pipeline instead of one mega-GLB

> 💡 If your asset is “too big for GitHub Pages + WebGL,” it’s a pipeline problem, not a viewer problem.

---

## 🔒 Licensing, attribution, and sensitivity

### ✅ Must be true before shipping
- [ ] The model’s **license is compatible** with KFM distribution
- [ ] Required attribution is included (in `model.json` + this README)
- [ ] If the source is restricted, the **output is not less restricted** (propagate classification)

### 🧯 Redaction / safety notes
If the model reveals sensitive locations (cultural sites, private property, etc.), document:
- what was removed/blurred/generalized
- what *should not* be inferred from the model
- any access controls expected at runtime

---

## 🧪 Validation checklist (pre-merge)

### ✅ Geometry sanity
- [ ] Model opens with **no missing textures**
- [ ] Scale is correct (units = meters)
- [ ] Pivot/origin is sensible (near 0,0,0 for local assets)
- [ ] Normals look correct (no inside-out shading)
- [ ] No “exploding” transforms (scale ≠ 0, NaNs, etc.)

### ✅ Rendering sanity (PBR)
- [ ] BaseColor looks correct (not washed out)
- [ ] Metallic/Roughness behave as expected
- [ ] Normal maps aren’t flipped

### ✅ Metadata / provenance
- [ ] `model.json` filled (no `<TODO>` left except checksums if not required yet)
- [ ] Sources include citations + licenses
- [ ] Processing steps describe how this was generated

---

## 🔗 How the UI should reference this asset

> This folder path is the contract. Don’t break it. 🧷

Recommended URL shape (adjust to your deployment base path):

```text
/assets/3d/shared/models/<MODEL_ID>/model.glb
/assets/3d/shared/models/<MODEL_ID>/model.json
/assets/3d/shared/models/<MODEL_ID>/preview.webp
```

---

## 🧩 README fields to fill (copy + replace)

### 🏷️ Model ID
`<MODEL_ID>`

### 📝 Description
<Write a short description for humans. What is it? Why does it matter to Kansas? What story does it support?>

### 🧾 Provenance summary
- **Primary source(s):** <1–3 bullets>
- **Derived from:** <scans / lidar / photogrammetry / artist reconstruction>
- **Processing:** <retopo, bake, compression, conversion, etc.>

### 🎬 Intended use in KFM
- Used in: <Story Node IDs / map layers / UI module>
- Default placement: <if georeferenced, include lon/lat/height + heading>

---

## 📚 Notes & conventions

- ✅ Keep runtime artifacts here (`web/`).
- ✅ Keep heavy source artifacts (raw scans, photogrammetry projects, `.blend`, `.psd`) elsewhere and link them via provenance.
- ✅ Prefer repeatable pipelines; document the steps so someone else can reproduce.

---

## 🧷 Internal references (project context)

- KFM governance is “evidence-first / provenance-first / citation-first.”  
- The web UI is designed around MapLibre/WebGL with optional Cesium for 3D expansion.
