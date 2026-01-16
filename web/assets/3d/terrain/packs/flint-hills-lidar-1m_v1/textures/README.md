---
title: "🗺️ Textures — Flint Hills LiDAR 1m Terrain Pack (v1)"
path: "web/assets/3d/terrain/packs/flint-hills-lidar-1m_v1/textures/README.md"
version: "v1.0.0"
last_updated: "2026-01-15"
status: "active"
doc_kind: "README"
project: "Kansas Frontier Matrix (KFM)"
subsystem: "web/assets/3d"
artifact_scope: "terrain-pack-textures"
terrain_pack_id: "flint-hills-lidar-1m_v1"
source_kind: "LiDAR-derived"
license: "MIT (documentation); textures are governed by pack-level licenses"
kfm_mdp_version: "v11.2.6"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US"
governance_ref: "docs/governance/"
ethics_ref: "docs/governance/"
doc_uuid: "urn:kfm:doc:web-assets-3d:terrain-pack-textures:flint-hills-lidar-1m_v1:v1.0.0"
semantic_document_id: "kfm.web.assets.3d.terrain.packs.flint-hills-lidar-1m_v1.textures.readme"
commit_sha: "<fill-at-commit>"
doc_integrity_checksum: "sha256:<fill-at-commit>"
---

# 🧱 Textures (runtime) — Flint Hills LiDAR 1m (v1)

![KFM-MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-blue)
![asset](https://img.shields.io/badge/asset-terrain%20textures-6a5acd)
![pack](https://img.shields.io/badge/pack-flint--hills--lidar--1m__v1-2e8b57)
![license](https://img.shields.io/badge/license-see%20pack%20licenses-informational)

> [!IMPORTANT]
> This folder is for **runtime-ready** textures served by the web app (optimized, compressed, cache-friendly).
> **Do not** place raw LiDAR, GeoTIFFs, authoring PSD/EXR, or “scratch” exports here.

---

## 🔗 Quick links

- 📦 Pack root (recommended): `../README.md`
- 🧾 Licenses for this pack: `../licenses/README.md`
- 🏷️ Attribution (if present): `../attribution.md`
- 🧰 Shared terrain textures: `../../../../shared/textures/terrain/README.md`
- 🧪 Texture authoring (_source): `../../../../shared/textures/_source/README.md`

---

## 🎯 Purpose

These textures support the **Flint Hills LiDAR 1m** terrain pack by providing:

- 🛰️ **LiDAR-derived** raster maps (e.g., height, slope, curvature, masks) used to shade and/or blend materials.
- 🎨 **Blend control** (splat/weight maps) that drive terrain material mixing in the 3D viewer.
- ⚡ **Runtime formats** (typically `KTX2` + mipmaps) for fast streaming and GPU-friendly sampling.

---

## ✅ Scope

| In scope ✅ | Out of scope ❌ |
|---|---|
| Runtime textures used by the terrain renderer | Raw point clouds (`.laz/.las`) |
| KTX2/PNG/JPG outputs with stable naming | GeoTIFF/analysis rasters meant for GIS workflows |
| Channel-packed maps (ORM, splat RGBA) | Authoring sources (`.psd/.kra/.blend/.sbsar/.exr`) |
| Manifests + checksums + provenance pointers | “Mystery files” with unknown origin/license |

---

## 📁 Recommended layout

> [!NOTE]
> The exact layout can be flat or nested. Prefer nested folders when the set grows.

```text
web/assets/3d/terrain/packs/flint-hills-lidar-1m_v1/
└── textures/                        🧱 (you are here)
    ├── README.md
    ├── textures.manifest.json       🗂️ (recommended)
    ├── basecolor/                   🎨 (optional)
    ├── normal/                      🧭 (optional)
    ├── height/                      ⛰️ (optional)
    ├── masks/                       🎭 (optional)
    ├── splat/                       🧪 (optional)
    └── tiles/                       🧩 (optional; z/x/y or custom tiling)
```

---

## 🏷️ Naming conventions

### Option A — Pack-wide (single files)
Use when a texture covers the whole pack (or is referenced by a manifest with explicit bounds):

```text
<pack_id>__<map>__<res>__<colorspace>.<ext>

# examples
flint-hills-lidar-1m_v1__splat__4096__lin.ktx2
flint-hills-lidar-1m_v1__normal__4096__lin.ktx2
flint-hills-lidar-1m_v1__basecolor__4096__srgb.ktx2
```

### Option B — Tiled (many files)
Use when the terrain renderer streams textures by tile:

```text
tiles/<z>/<x>/<y>__<map>__<res>.<ext>

# examples
tiles/12/1056/1632__height__256.png
tiles/12/1056/1632__splat__256.ktx2
```

**Rules**
- Use **lowercase**.
- Use `__` as the “big separator” (avoids ambiguity in slugs).
- Avoid spaces; prefer `-` inside slugs.
- Treat filenames as **API**: changes must be versioned and reflected in manifests.

---

## 🧩 Texture types & standards

> [!TIP]
> Keep your shader/material system boring and predictable. The more consistent the map semantics, the less “terrain voodoo” later.

| Map type | Typical suffix | Colorspace | Preferred format | Notes |
|---|---:|---:|---|---|
| Base Color / Albedo | `basecolor` / `albedo` | **sRGB** | `KTX2` | No baked lighting if possible |
| Normal | `normal` | Linear | `KTX2` | Document **Y+ vs Y-** convention |
| Height / Elevation | `height` | Linear | `PNG (16-bit)` or `KTX2` | Prefer 16-bit where precision matters |
| Roughness | `roughness` | Linear | `KTX2` | Often packed into ORM |
| Ambient Occlusion | `ao` | Linear | `KTX2` | Often packed into ORM |
| Metalness | `metal` | Linear | `KTX2` | Usually `0` for terrain; omit unless needed |
| ORM packed | `orm` | Linear | `KTX2` | Convention: **R=AO, G=Roughness, B=Metalness** |
| Splat / Weights | `splat` / `weights` | Linear | `KTX2` | RGBA = material weights (define mapping!) |
| Masks | `mask-*` | Linear | `KTX2/PNG` | Water, roads, exclusions, etc. |

### 🎚️ Splat mapping contract (document this!)
If you use a splat map, define what each channel means (example):

| Channel | Meaning (example) |
|---:|---|
| R | grass |
| G | rock |
| B | bare soil |
| A | “other” / blend control |

> [!IMPORTANT]
> Whatever mapping you choose must be stated here **and** in `textures.manifest.json` so tooling and shaders agree.

---

## 🧪 Provenance-first: manifest requirements

Create/maintain a **machine-readable manifest** in this directory:

- **File:** `textures.manifest.json` (recommended name)
- **Purpose:** declare *what* each texture is, *how* it was produced, and *which license applies*.

### Minimal manifest fields (recommended)
```json
{
  "pack_id": "flint-hills-lidar-1m_v1",
  "textures": [
    {
      "id": "splat-4096",
      "role": "splat",
      "uri": "splat/flint-hills-lidar-1m_v1__splat__4096__lin.ktx2",
      "colorspace": "linear",
      "size_px": [4096, 4096],
      "channels": { "r": "grass", "g": "rock", "b": "soil", "a": "other" },
      "derived_from": [
        { "type": "lidar_dtm", "ref": "../metadata/source.lidar.json" },
        { "type": "ruleset", "ref": "../metadata/material_ruleset.v1.json" }
      ],
      "license_ref": "../licenses/README.md",
      "sha256": "<fill>"
    }
  ]
}
```

> [!NOTE]
> The manifest can be extended to support tiling schemes, bounds, CRS, nodata, quantization, and STAC pointers.

---

## 🏗️ Reference pipeline (how these textures should be produced)

```mermaid
flowchart TD
  A[📡 LiDAR point cloud / DTM inputs] --> B[🧹 QA + classification validation]
  B --> C[⛰️ DTM/DSM raster products (analysis workspace)]
  C --> D[📐 Derivatives: slope/aspect/curvature/hillshade]
  D --> E[🧪 Material ruleset → weight/splat maps]
  E --> F[🗺️ Bake to terrain UVs or tile grid]
  F --> G[🧊 Encode: KTX2/PNG + mipmaps + padding]
  G --> H[📦 Write manifest + checksums + license refs]
  H --> I[✅ Visual + numeric QA (seams, ranges, gamma)]
```

---

## ✅ QA checklist (must-pass)

- [ ] **Alignment:** textures line up with the terrain mesh/tiles (no half-texel drift)
- [ ] **Seams:** no visible seams at tile edges (use edge padding + mip-safe borders)
- [ ] **Gamma:** sRGB only where intended (basecolor); masks/normals/height are linear
- [ ] **Normals:** correct handedness (+Y/-Y) and consistent across the pack
- [ ] **Ranges:** height and masks have expected min/max and nodata handling
- [ ] **Compression:** KTX2 is visually acceptable (no block artifacts on masks)
- [ ] **Manifest:** every shipped texture has `sha256`, provenance pointers, and `license_ref`

---

## 🚫 Hard “don’t” list

- ❌ Don’t commit raw LiDAR (`.laz/.las`) here  
- ❌ Don’t commit editor sources (`.psd/.kra/.blend/.sbsar/.exr`) here  
- ❌ Don’t ship textures without a **license_ref**  
- ❌ Don’t rename textures without bumping the pack version and updating manifests  

---

## 🛠️ Adding or updating textures

1. **Generate** textures in your authoring/analysis workspace (not this folder).
2. **Export** to runtime formats (`.ktx2` preferred) using the naming rules above.
3. **Place** outputs into this folder (and subfolders if used).
4. **Update** `textures.manifest.json` (add provenance + sha256 + license_ref).
5. **Validate** using the QA checklist (visual + programmatic checks).
6. **Commit** with pack versioning discipline (avoid breaking URLs unless version bump).

---

## 📎 Attribution & licensing

All licensing for textures in this pack must be documented in:

- `../licenses/README.md` ✅
- `../attribution.md` (if required by the source/provider) ✅

> [!IMPORTANT]
> If a texture is derived from third-party data, the derivation must preserve attribution and comply with source terms.
