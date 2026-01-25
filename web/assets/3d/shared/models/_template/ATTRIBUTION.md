---
title: "ATTRIBUTION — 3D Model Asset"
path: "web/assets/3d/shared/models/{{asset_slug}}/ATTRIBUTION.md"
version: "v0.1.0"
last_updated: "YYYY-MM-DD"
status: "draft" # draft | active | deprecated
doc_kind: "Asset Attribution"
license: "MIT" # license of THIS document (repo docs); the asset license(s) live below

# Schema / governance
attribution_schema_version: "1.0"
fair_category: "FAIR+CARE"
care_label: "TBD" # Public | Sensitive | Restricted | TBD
sensitivity: "public" # public | internal | restricted
classification: "open" # open | limited | closed
jurisdiction: "US"

# IDs (keep stable once published)
doc_uuid: "urn:kfm:doc:assets:3d:{{asset_slug}}:attribution:v0.1.0"
asset_uuid: "urn:kfm:asset:3d-model:{{asset_slug}}"

# Build integrity (optional but nice)
commit_sha: "<commit-hash>"
doc_integrity_checksum: "sha256:<to-be-filled>"
---

<!--
🧩 TEMPLATE FILE (copy into the model folder)

Rules of the road ✅
- Don’t delete fields — if not applicable, use "n/a" or "TBD".
- No “mystery assets”: every model / texture / HDRI / ref must have a source + license.
- If anything here is sensitive (cultural heritage, sacred sites, restricted access), set care_label + sensitivity accordingly.
-->

![Provenance](https://img.shields.io/badge/provenance-first-success?style=flat)
![License Tracking](https://img.shields.io/badge/license-tracked-informational?style=flat)
![3D Asset](https://img.shields.io/badge/asset-3D%20model-blue?style=flat)

# 🧾 Attribution & Licensing — {{ASSET_NAME}}

> **TL;DR**: This file is the single source of truth for **who made this asset**, **where it came from**, **what license applies**, and **what we changed**.  
> If we can’t trace it, we can’t ship it. 🧭

---

## 📦 Folder layout (expected)

```text
web/assets/3d/shared/models/{{asset_slug}}/
├─ 👈🏷️📄 ATTRIBUTION.md           # You are here 📌 Human-readable credits: author/source, license, modifications, required notices
├─ 🧱🧊 model.glb / model.gltf      # Primary runtime model (GLB preferred; or GLTF + external textures if needed)
├─ 🎨 textures/                    # Texture files (only if not embedded; document color space + packing in metadata)
├─ 🖼️ thumbnails/                  # (optional) Preview images for UI/cards (webp/png; keep small)
└─ 🧬🧾 metadata.json               # (optional) Machine-readable contract: id/title, units, bounds, license, provenance, checksums
```

---

## 📘 Overview

### Purpose
Provide a **human-readable** attribution record for this 3D asset, including license obligations and a reproducible processing trace.

### Scope
| In scope ✅ | Out of scope ❌ |
|---|---|
| Model mesh(es), textures, materials, HDRIs, scans, reference imagery used to *build* the asset | Runtime code, shaders, or app-level UI attribution (those live elsewhere) |
| License + attribution requirements | Legal advice |
| Modification / optimization history | Full pipeline scripts (link them if needed) |

### Audience
- **Primary:** contributors adding or updating 3D assets
- **Secondary:** reviewers, maintainers, educators, downstream users

---

## 🏷️ Asset identity

| Field | Value |
|---|---|
| **Asset name** | `{{ASSET_NAME}}` |
| **Asset slug** | `{{asset_slug}}` |
| **Category / tag(s)** | `{{e.g., landmark, artifact, terrain, building, vegetation}}` |
| **Asset type** | `{{glTF / GLB / 3D Tiles / OBJ / FBX}}` |
| **Primary file(s)** | `{{model.glb}}` |
| **Preview image** | `{{thumbnails/preview.webp}}` |
| **Georeferenced?** | `{{yes/no}}` |
| **CRS / units (if geo)** | `{{EPSG:4326 / meters / ...}}` |
| **Intended usage** | `{{Story node / map overlay / 3D scene / educational}}` |

---

## 🧾 Attribution summary (copy/paste)

> **Attribution:** `{{ASSET_NAME}}` by `{{CREATOR_NAME}}` ({{SOURCE_SITE}}), licensed under `{{LICENSE}}`.  
> **Modifications:** `{{brief list: e.g., decimated mesh, rebaked textures, converted to glTF, generated LODs}}`.  
> **Source:** `{{SOURCE_URL}}` (accessed `{{YYYY-MM-DD}}`).

---

## 🧩 Components, sources, and licenses

> Fill **one row per component**. If you merged sources, list each one separately.

| Component | File(s) in repo | Original creator / org | Source (URL or citation) | License | Required attribution text | Changes we made |
|---|---|---|---|---|---|---|
| **Model (mesh)** | `{{model.glb}}` | `{{name}}` | `{{url}}` | `{{SPDX or CC}}` | `{{exact attribution}}` | `{{edits}}` |
| **Textures (PBR)** | `textures/{{...}}` | `{{name}}` | `{{url}}` | `{{license}}` | `{{text}}` | `{{edits}}` |
| **HDRI / env map** | `{{path}}` | `{{name}}` | `{{url}}` | `{{license}}` | `{{text}}` | `{{edits}}` |
| **Reference photos** | `{{path or "not stored"}}` | `{{name}}` | `{{url}}` | `{{license}}` | `{{text}}` | `{{edits}}` |
| **Other** | `{{path}}` | `{{name}}` | `{{url}}` | `{{license}}` | `{{text}}` | `{{edits}}` |

### 🔐 License compatibility notes (required if multiple licenses)
- **Most restrictive wins**: if you combine assets, the *output experience* must respect the strictest applicable terms.  
  Example: CC-BY + Public Domain → treat the combined output as **CC-BY** for attribution purposes.
- **Non-Commercial / No-Derivatives warning**: if any component is `NC` or `ND`, confirm this asset is allowed in our use case (and document why).

---

## 🧬 Provenance & processing log

### Source acquisition
- **Downloaded from:** `{{SOURCE_URL}}`
- **Access date:** `{{YYYY-MM-DD}}`
- **Archive / mirror (optional but recommended):** `{{Wayback / DOI / local evidence link}}`
- **Original filename(s):** `{{...}}`
- **Original version/hash (if available):** `{{sha256:...}}`

### Processing steps (keep it chronological)
> Tip: Think of this as a “mini changelog” for the asset.

1. `{{YYYY-MM-DD}}` — Imported into `{{Blender / RealityCapture / ...}}`  
   - Notes: `{{scale, axes, units}}`
2. `{{YYYY-MM-DD}}` — Mesh optimization  
   - Polycount: `{{before}} → {{after}}`  
   - Method: `{{decimate / retopo / quad remesh}}`
3. `{{YYYY-MM-DD}}` — Texture workflow  
   - Maps: `{{baseColor, normal, roughness, metalness, AO}}`  
   - Baking / resizing: `{{details}}`
4. `{{YYYY-MM-DD}}` — Export + packaging  
   - Exported as: `{{glTF 2.0 / GLB}}`  
   - Compression: `{{none / Draco / KTX2 / meshopt}}`  
   - Validation: `{{gltf-validator link or notes}}`

<details>
  <summary><strong>🧪 Optional: QA / sanity checks</strong></summary>

- [ ] Asset loads in the viewer (no missing textures)
- [ ] Material channels correct (Rough/Metal not swapped)
- [ ] Normals look correct (no inside-out shading)
- [ ] Scale is sane (documented units)
- [ ] Performance target hit (tri budget + texture budget)
- [ ] Mobile friendly (if applicable)
- [ ] License + attribution are complete (no TBDs)
</details>

---

## 🖥️ How attribution should appear in the UI

### Minimum UI credit (must be shown somewhere)
- `{{CREATOR_NAME}}` — `{{LICENSE}}` — `{{SOURCE_SITE}}`

### Where to show it (choose at least one)
- [ ] Layer/asset “Info” panel 🧾  
- [ ] Story node footnotes / references 📚  
- [ ] App-wide Credits / About page 🏛️  

---

## ✅ Definition of Done (DoD) — Attribution completeness

- [ ] Every included file (mesh/texture/HDRI/etc) is listed in the components table
- [ ] Every component has **source + license + attribution text**
- [ ] Any required “change notice” is included (e.g., “modified / adapted”)
- [ ] If multiple licenses apply, the compatibility notes are filled in
- [ ] All placeholders (`{{...}}`) are replaced, or explicitly set to `n/a`
- [ ] `last_updated` updated
- [ ] If sensitive/culturally restricted, `care_label` and `sensitivity` are set correctly

---

## 🔗 References (evidence-first)

> Use a consistent style so the UI can scrape it if needed (example: numbered refs).

1. `[1] {{Source title}} — {{URL}} (accessed {{YYYY-MM-DD}})`
2. `[2] {{License text}} — {{URL}}`
3. `[3] {{Creator profile / repository}} — {{URL}}`

<!-- End of template ✅ -->
