---
title: "🧊 Shared GLB Models (Runtime Assets)"
path: "web/assets/3d/shared/models/glb/README.md"
version: "v0.1.0"
last_updated: "2026-01-15"
status: "draft"
doc_kind: "README"
project: "Kansas Frontier Matrix (KFM)"

# Protocol / governance
markdown_protocol: "KFM-MDP"
markdown_protocol_version: "11.2.6"
pipeline_contract_version: "v13"
governance_ref: "docs/governance/GOVERNANCE_POLICY.md"
ethics_ref: "docs/governance/ETHICS_POLICY.md"

# FAIR/CARE & safety labels
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"

# Identity
semantic_document_id: "kfm:web:assets:3d:shared:models:glb:readme"
doc_uuid: "urn:kfm:doc:web:assets:3d:shared:models:glb:readme:v0.1.0"

# Build-time fill-ins (CI)
commit_sha: "<commit-hash>"
doc_integrity_checksum: "sha256:<to-be-filled>"
---

# 🧊 Shared GLB Models (Runtime Assets)

![KFM-MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-informational)
![Format](https://img.shields.io/badge/format-GLB%20%28glTF%202.0%29-blue)
![Usage](https://img.shields.io/badge/usage-runtime%20assets%20for%20web%2F-6aa84f)

> **TL;DR**: This folder is for **runtime-ready** `.glb` models that are reused across the KFM web UI (and any shared 3D viewers).  
> Source-of-truth authoring files (e.g., `.blend`, `.fbx`, high-poly scans) should live elsewhere. 🚫🧱

---

## 📘 Overview

### 🎯 Purpose
Provide a single canonical home for **shared** (reusable) GLB assets—optimized for fast download, stable caching, and predictable rendering.

### 🧭 Scope
| ✅ In Scope | ❌ Out of Scope |
|---|---|
| `.glb` (glTF 2.0) runtime assets | Authoring sources (`.blend`, `.fbx`, `.obj`) |
| Optional pre-compressed variants (`.br`, `.gz`) | Raw photogrammetry scans / huge point clouds |
| Optional sidecar metadata (`.meta.json`) | Textures libraries (kept in texture-specific folders) |
| Shared, not site-specific models | Landmark/site-specific assets (store under their own folders) |

### 👥 Audience
- 🧑‍💻 Web/3D engineers (Three.js / Babylon.js / Cesium / MapLibre overlays)
- 🗺️ GIS & visualization maintainers
- 🧾 Data stewards verifying provenance/licensing for published 3D assets

### 📚 Definitions
- **glTF / GLB**: Khronos glTF 2.0 scene format; **GLB** is the binary-packed variant (often best for web delivery).
- **LOD**: “Level of Detail” variants of the same model (LOD0 high → LOD2/3 low).
- **PBR**: Physically Based Rendering (baseColor/metallic/roughness workflow).
- **Runtime-ready**: Validated + optimized + licensed + (ideally) has metadata.

---

## 🗂️ Directory Layout

```text
web/
└─ 📁 assets/
   └─ 🧊 3d/
      └─ 🧰 shared/
         └─ 🧊 models/
            └─ 🧊 glb/                       # 👈 you are here 📌 GLB runtime binaries (optionally pre-compressed for CDN)
               ├─ 🧊 <model-slug>.glb         # Primary model (GLB; web-ready; prefer embedded textures when possible)
               ├─ 🧊🗜️ <model-slug>.glb.br     # (optional) Brotli-compressed GLB for static hosting/CDN
               ├─ 🧊🗜️ <model-slug>.glb.gz     # (optional) Gzip-compressed GLB for static hosting/CDN
               └─ 🧾 <model-slug>.meta.json    # (recommended) Sidecar: license/attribution, units/bounds, provenance, checksums
```

---

## ✅ What belongs here?

### ✅ Put it here when…
- The model is **used in multiple places** (shared UI components, repeated props, generic structures).
- It is already **optimized** (polycount, textures, draw calls) for web delivery.
- Its **license and attribution** are known and recorded.

### 🚫 Don’t put it here when…
- The model is specific to **one** landmark/site (store it under that landmark/site path).
- It’s a raw export or editable source that will change frequently.
- The licensing is unknown, unclear, or incompatible with publishing.

---

## 🏷️ Naming Conventions

### ✅ File names
Use **kebab-case** and keep names stable:
- `windmill.glb`
- `covered-wagon.glb`
- `prairie-school-house.glb`

### 🧩 Versions & LOD (recommended patterns)
Pick one pattern and be consistent per asset-family:

**Option A — semantic version in filename**
- `windmill--v1.0.0.glb`
- `windmill--v1.1.0.glb`

**Option B — LOD suffix**
- `windmill--lod0.glb`
- `windmill--lod1.glb`
- `windmill--lod2.glb`

> 💡 If your deploy pipeline uses immutable caching, versioned filenames are your friend.

---

## 📐 Export & Runtime Requirements (GLB)

> Keep these consistent to reduce “why is it rotated/upside-down?” incidents. 🙃

**Minimum expectations**
- ✅ glTF 2.0 / GLB format
- ✅ Units: **meters** (1 unit = 1 meter)
- ✅ Coordinate convention (glTF): **right-handed**, **Y-up**, **-Z forward**
- ✅ Apply transforms (scale/rotation) before export
- ✅ Pivot/origin set intentionally (document in `.meta.json` if non-standard)

<details>
<summary>🛠️ Suggested Export Checklist (click to expand)</summary>

- Geometry
  - Apply scale/rotation ✅
  - Remove non-manifold geometry where possible ✅
  - Merge redundant meshes (when it reduces draw calls) ✅
  - Keep normals consistent ✅

- Materials (PBR)
  - Prefer glTF metallic/roughness workflow ✅
  - Avoid exotic shader graphs unless baked ✅
  - Keep texture set minimal (don’t ship 8K maps for a tiny prop) ✅

- Performance
  - Keep triangle counts appropriate to on-screen size ✅
  - Avoid hundreds of separate mesh nodes ✅
  - Avoid massive embedded animations unless required ✅

</details>

---

## 🗜️ Optimization & Compression

### 🧱 Geometry / scene optimization
Use an optimization step before committing:
- Remove unused nodes/materials
- Merge meshes where reasonable
- Validate GLB after optimization

### 📦 Delivery compression
Precompressed assets are optional but strongly encouraged for heavy models:
- `*.glb.br` (Brotli) ✅ best for modern browsers
- `*.glb.gz` (Gzip) ✅ broad compatibility

> ⚠️ If you add `*.br` / `*.gz`, ensure your static server is configured to serve them with correct `Content-Encoding`.

---

## 🧾 Metadata Sidecar (recommended)

If a model is published or reused broadly, include a sibling metadata file:

- `windmill.meta.json` alongside `windmill.glb`

### ✅ Suggested minimum fields
```json
{
  "id": "windmill",
  "title": "Windmill (Shared Prop)",
  "version": "1.0.0",
  "source": {
    "origin": "TBD",
    "author": "TBD",
    "link": "TBD"
  },
  "license": {
    "spdx": "TBD",
    "attribution_required": true
  },
  "render": {
    "units": "meters",
    "up_axis": "Y",
    "forward_axis": "-Z"
  },
  "files": {
    "glb": "windmill.glb",
    "glb_br": "windmill.glb.br",
    "glb_gz": "windmill.glb.gz"
  },
  "integrity": {
    "sha256": "TBD"
  }
}
```

> 🧠 Treat this metadata as a “mini contract” for downstream UI loaders and auditors.

---

## ⚖️ Licensing & Attribution (non-negotiable)

Every published model must be attributable and legally usable:
- ✅ Record license using SPDX identifier when possible
- ✅ Preserve attribution requirements (author, source, link, modification notice)
- ✅ If the model is derived (scan → retopo → bake), record **derivation** and **tools** used

> 🛡️ If licensing is unclear: **do not ship** the asset into this folder.

---

## ✅ Validation Checklist (Definition of Done)

Before adding or updating a GLB asset:

- [ ] File name follows conventions (kebab-case; version/LOD if used)
- [ ] GLB loads in at least one standard viewer (no missing textures, no broken nodes)
- [ ] Transforms are applied (scale/rotation sane)
- [ ] Model is reasonably optimized (polycount/draw calls match expected use)
- [ ] License + attribution are documented (and compatible with publishing)
- [ ] Optional: `*.meta.json` exists and is complete
- [ ] Optional: precompressed `*.br` / `*.gz` generated and server can serve them

---

## 🚀 Quick Start: Adding a new shared GLB

1. 🧱 Author/prepare the model in your DCC tool (keep source elsewhere)
2. 📤 Export to `.glb` using the requirements above
3. 🗜️ Optimize + validate (then re-validate)
4. 🧾 Add `*.meta.json` (recommended)
5. ⚖️ Confirm license + attribution (required)
6. ✅ Commit the runtime outputs here

---

## 🧯 Troubleshooting

- **Model is rotated 90°**: axis mismatch—confirm Y-up / -Z forward and applied transforms.
- **Looks “plastic” or too shiny**: roughness/metallic map issues; confirm PBR workflow and correct channel packing.
- **Huge file size**: reduce texture resolution, bake materials, remove unused nodes, consider LODs.
- **Missing textures**: GLB should be self-contained or references must be resolvable by the web server (prefer self-contained for shared assets).

---

## 🔒 Safety & Sensitivity Notes

If a model represents:
- culturally sensitive locations,
- restricted archaeological features,
- or detailed site interiors that should not be public,

…then **do not publish** a high-fidelity asset here without explicit governance approval. Use redaction/decimation and set appropriate CARE labels upstream. 🧭🛡️
