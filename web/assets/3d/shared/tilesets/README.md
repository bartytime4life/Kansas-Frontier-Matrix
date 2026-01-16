---
title: "🧱 Shared 3D Tilesets"
description: "Canonical home for reusable Cesium 3D Tiles tilesets consumed by the KFM web 3D viewer."
doc_type: "readme"
kfm_mdp: "v11.2.6"
status: "active"
canonical_path: "web/assets/3d/shared/tilesets/README.md"
semantic_document_id: "kfm:web.assets.3d.shared.tilesets.readme"
doc_uuid: "3b2b48f1-06c1-4ee7-b8c9-830b36becc14"
version:
  semver: "0.1.0"
  last_updated: "2026-01-15"
ownership:
  steward: "KFM Core Maintainers"
  reviewers:
    - "3D/Rendering Maintainers"
security:
  classification: "public"
  contains_pii: false
  contains_secrets: false
  export_controlled: false
governance:
  principles:
    - "provenance-first"
    - "evidence-linked"
    - "no-duplicate-canonical-homes"
tags:
  - kfm
  - web-assets
  - 3d
  - cesium
  - 3d-tiles
  - tileset.json
license:
  docs: "CC-BY-4.0 (unless noted)"
---

# 🧱 Shared 3D Tilesets

![KFM-MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-2b6cb0)
![3D Tiles](https://img.shields.io/badge/Cesium-3D%20Tiles-4a5568)
![Provenance](https://img.shields.io/badge/Principle-Provenance--First-2f855a)
![Web Assets](https://img.shields.io/badge/Scope-web%2Fassets%2F3d-805ad5)

Reusable **3D Tiles** packages (Cesium ecosystem) that are **not specific to a single landmark or a single terrain pack** live here. Think: “shared city model,” “shared LiDAR preview,” “shared building tiles,” etc.

> ✅ If it’s consumed by the web app as a *tileset* (typically `tileset.json`) and is broadly reusable, it belongs here.  
> ❌ If it’s landmark-specific, keep it under `web/assets/3d/landmarks/<landmark_slug>/…`  
> ❌ If it’s terrain-pack-specific, keep it under `web/assets/3d/terrain/packs/<pack>/…`

---

## 🧭 Quick Links

- 🧊 GLB models: `../models/glb/README.md`
- 🧩 Shared textures: `../textures/`
- 🗺️ Terrain packs (3D): `../../terrain/`
- 🏛️ Landmark-specific 3D: `../../landmarks/`

---

## 🗂️ Directory Shape (Expected)

Each tileset gets its own folder. Inside that folder, keep the **runtime** tileset (`tileset.json` + content) separate from the **evidence/provenance** paperwork.

```text
web/assets/3d/shared/tilesets/
├─ README.md
└─ <tileset_id>/
   ├─ tileset.json
   ├─ content/                     # .b3dm / .i3dm / .pnts / .cmpt / .glb / textures, etc.
   ├─ preview/                     # small screenshots / gifs (optional, lightweight)
   ├─ manifest.kfm.json            # KFM metadata for registry + QA (recommended)
   ├─ attribution.md               # short human-readable attribution
   ├─ licenses/                    # license texts + notes
   │  └─ README.md
   ├─ citations/                   # where it came from (URLs, docs, scans, DOIs)
   │  └─ README.md
   └─ source/                      # how it was made (pipeline inputs/params/tools)
      └─ README.md
```

---

## ✅ What Belongs Here

### ✅ Good fits
- 🌆 Shared building/city tiles (e.g., CityGML→3D Tiles conversions)
- 🛰️ Shared LiDAR point-cloud tiles used as “demo/overview” layers
- 🪨 Shared geology/stratigraphy prototypes (if the web viewer needs them)
- 🧪 Performance test tilesets (clearly labeled + non-production)

### 🚫 Not a fit
- 🏞️ Terrain tiles that are part of a specific pack → `web/assets/3d/terrain/...`
- 🏛️ Landmark-only tilesets → `web/assets/3d/landmarks/<landmark_slug>/...`
- 🧱 Raw source files too big for web runtime (keep in pipeline storage, promote outputs)

---

## 📦 Tileset Package Contract (KFM Expectations)

### 1) Runtime
- `tileset.json` at the tileset root (stable path)
- All referenced tile content paths are **relative** and resolve within the folder

### 2) Evidence + compliance
- `citations/README.md` explains **where source data came from**
- `licenses/` contains **license text** and any required notices
- `attribution.md` gives **human-readable attribution** suitable for UI display

### 3) Provenance
- `source/README.md` describes:
  - inputs (datasets + versions)
  - transforms (tools, parameters)
  - outputs (what exactly is served)
  - reproducibility notes (hashes, seeds, container tags if applicable)

> 🔒 **Fail-closed mindset:** if a tileset cannot be attributed/licensed/cited, it does not ship.

---

## 🏷️ Naming & Versioning

### Tileset ID (`<tileset_id>`)
Use **kebab-case**, ASCII, and include a version suffix when meaningful.

**Recommended pattern**
- `<theme>-<region>-<resolution_or_scale>_v<major>`
- Examples:
  - `buildings-kansas-statewide_lod1_v1`
  - `lidar-flint-hills-overview_10m_v1`
  - `city-abilene-downtown_lod2_v2`

### When to bump version
- **v+1** when source data changes, coordinate reference changes, tiling scheme changes, or content format changes.

---

## 🚀 Serving & Runtime Integration

### URL stability
Assume the web app loads tilesets via stable URLs like:

```text
/assets/3d/shared/tilesets/<tileset_id>/tileset.json
```

### Don’t hardcode internals
Apps and story content should reference a tileset via:
- a **registry entry** (recommended), or
- a single stable “entry URL” (`tileset.json`) — never deep-link to content files.

---

## 🧪 Validation & QA (Recommended)

### Basic checks
- ✅ `tileset.json` parses
- ✅ referenced files exist
- ✅ bounding volumes + geometric error are sane
- ✅ no accidental absolute URLs inside tileset content paths

### Suggested tooling (examples)
```bash
# Example: validate structure quickly (adjust toolchain to your environment)
find web/assets/3d/shared/tilesets/<tileset_id> -maxdepth 2 -type f | sort

# Example: ensure tileset.json exists
test -f web/assets/3d/shared/tilesets/<tileset_id>/tileset.json
```

> 💡 Keep heavy validation (3D Tiles validators, glTF validators, compression audits) in the **pipeline CI**, and treat this folder as the **promoted web artifact**.

---

## ⚖️ Licensing, Attribution, and “No Surprises” Policy

Every tileset must be shippable under its license terms:
- Include license texts in `licenses/`
- Include attribution in `attribution.md`
- Include sources + citation trail in `citations/`

If you combine multiple sources:
- list each one in `citations/`
- describe how they were merged in `source/`
- ensure downstream distribution is still permitted

---

## 🧯 Common Pitfalls

- 🧨 **Tileset paths break in production** (using absolute paths or assuming local dev base URL)
- 🐘 **Overweight tiles** (giant leaf tiles → slow network + long GPU upload)
- 🕳️ **Missing provenance** (no pipeline notes = no trust)
- 🔁 **Duplicate homes** (same tileset copied into landmark + shared paths)

---

## ✅ Add-a-Tileset Checklist

- [ ] Create `web/assets/3d/shared/tilesets/<tileset_id>/`
- [ ] Place `tileset.json` at the root
- [ ] Add `attribution.md`
- [ ] Add `licenses/README.md` (+ license texts)
- [ ] Add `citations/README.md` (+ source links/DOIs)
- [ ] Add `source/README.md` (+ pipeline + params)
- [ ] (Optional) Add `manifest.kfm.json` for registry + QA metadata
- [ ] Verify the web viewer loads `/assets/3d/shared/tilesets/<tileset_id>/tileset.json`

---

## 🔗 Related Conventions (Same “Contract Spirit”)

- Landmarks: `web/assets/3d/landmarks/<landmark_slug>/`
- Terrain: `web/assets/3d/terrain/`
- Shared models (GLB): `web/assets/3d/shared/models/glb/`

---
