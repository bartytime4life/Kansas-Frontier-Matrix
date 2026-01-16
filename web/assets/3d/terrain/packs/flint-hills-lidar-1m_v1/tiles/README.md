---
kfm_md_protocol: "KFM-MDP v11.2.6"
doc_uuid: "52a3e244-3b1a-4f46-8bb4-2d3f8d4e5b8a"
semantic_document_id: "kfm:web:assets:3d:terrain:packs:flint-hills-lidar-1m_v1:tiles:readme"
title: "🧱 Terrain Tiles — Flint Hills LiDAR 1m (v1)"
description: "Streamable terrain tile pyramid for the Flint Hills LiDAR 1m terrain pack (server-ready assets; no source data)."
path: "web/assets/3d/terrain/packs/flint-hills-lidar-1m_v1/tiles/README.md"
status: "draft"
created: "2026-01-15"
last_updated: "2026-01-15"
data_classification: "PUBLIC"
tags:
  - kfm
  - 3d
  - terrain
  - lidar
  - tiles
  - streaming
  - web
---

# 🧱 Terrain Tiles — Flint Hills LiDAR 1m (v1)

![KFM-MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-blue)
![Asset](https://img.shields.io/badge/asset-terrain%20tiles-6f42c1)
![Pack](https://img.shields.io/badge/pack-flint--hills--lidar--1m__v1-2ea44f)

This folder contains the **runtime tile pyramid** for the `flint-hills-lidar-1m_v1` terrain pack — optimized for **streaming into the web viewer** (Cesium/3D engine integrations) and **NOT** intended to be hand-edited.

> ✅ Goal: fast, deterministic, provenance-friendly terrain streaming  
> ❌ Non-goal: storing raw LiDAR / DEM source inputs here (keep those in the pack’s `_source/` or pipeline inputs)

---

## 🧭 What lives here?

- **Tile pyramid assets** (zoomed levels of terrain data)
- Optional **tile metadata** (availability, bounds, stats, checksums) depending on the tiling format
- Folder structure designed for **HTTP range/caching/CDN friendliness**

---

## 🗂️ Directory layout (expected)

> The exact layout depends on the terrain format. Use this as the **contract**: one canonical layout per pack.

```text
📁 web/assets/3d/terrain/packs/flint-hills-lidar-1m_v1/
├─ 📁 tiles/                       👈 (you are here)
│  ├─ 🗂️ 0/                         (zoom/level)
│  │  ├─ 🗂️ 0/                       (x)
│  │  │  ├─ 🧱 0.<ext>               (y + extension)
│  │  │  └─ …
│  │  └─ …
│  ├─ 🗂️ 1/
│  └─ …
├─ 📁 textures/                     (imagery/derived drapes, if any)
└─ 📄 README.md / metadata.*        (pack-level docs/metadata, if present)
```

---

## 🧩 Tile format matrix (fill in what this pack actually uses)

> Pick **one primary** format for runtime. If multiple exist, document the selection rules in the pack-level README.

| Format family | Typical extensions | Primary? |
|---|---|---|
| Cesium Terrain (Quantized-Mesh) | `.terrain` | ⬜ |
| Heightmap tiles (image) | `.png` / `.webp` / `.tif` | ⬜ |
| Mesh tiles (3D Tiles / custom) | `.b3dm` / `.glb` / `.i3dm` | ⬜ |
| Metadata / availability | `.json` | ⬜ |

**Pack decision (required):**
- **Primary tile format:** `TODO`
- **Tiling scheme:** `TODO (XYZ / TMS / provider-defined)`
- **Vertical units:** `TODO (meters recommended)`
- **Horizontal CRS:** `TODO (provider-defined; WGS84/WebMercator are common)`

---

## 🔌 Runtime contract (how the app should consume these tiles)

### ✅ Stable path rules
- The **public URL path** is treated as an API contract:
  - `.../terrain/packs/flint-hills-lidar-1m_v1/tiles/...`
- Avoid renaming zoom/x/y folders once published (breaks caching + deep links).

### ✅ Metadata rules
- If the chosen format requires a manifest (examples: `layer.json`, `tileset.json`, `tilejson.json`), store it at the **pack root** unless the format mandates otherwise.
- If checksums exist, store them as a **single file** (e.g., `checksums.sha256`) at the pack root or inside `tiles/` (but be consistent).

---

## 🌐 Hosting & performance notes

### 📦 Compression
- Prefer **pre-compressed** payloads where the format allows (or serve with gzip/br at the edge).
- Don’t double-compress formats that are already compressed internally.

### 🧠 Caching
Recommended CDN headers (adjust for your deployment):
- `Cache-Control: public, max-age=31536000, immutable` for versioned tiles
- Strong ETags (or content-hash naming) for safe long-lived caching

### 🧯 CORS
If tiles are served from a separate domain/CDN, ensure:
- `Access-Control-Allow-Origin` covers the web app origin(s)

---

## ✅ Validation checklist (QA gate)

**Tile integrity**
- [ ] Tile pyramid has no missing directories/files for intended zoom range
- [ ] Sample region renders without cracks/tears at zoom transitions
- [ ] No “checkerboard” holes / invalid no-data artifacts

**Numerical sanity**
- [ ] Elevation min/max is plausible for the Flint Hills AOI
- [ ] Vertical units are documented (meters recommended)
- [ ] No unexpected vertical offsets (datum mismatch)

**Delivery**
- [ ] Tiles are cacheable and respond with correct MIME types
- [ ] Compression behavior verified (no corrupt payloads)
- [ ] File sizes tracked (unexpected spikes flagged)

---

## 🧾 Provenance & reproducibility (required fields)

Add/maintain a pack-level `metadata.json` (or equivalent) that includes:

- **source_inputs**
  - dataset name(s), provider(s), license(s)
  - acquisition date(s)
  - processing lineage IDs / run manifests
- **processing**
  - toolchain + versions
  - resampling method(s)
  - nodata handling
  - vertical datum / geoid model (if applicable)
- **coverage**
  - AOI bounds
  - min/max zoom produced
  - resolution statement (“1m source” ≠ “1m everywhere after tiling”)

> If this folder is published without provenance metadata, it is considered **non-compliant** for KFM distribution.

---

## 🔗 Related docs

- 📦 Pack root: `../README.md` (if present)
- 🧵 Textures (drapes/overlays): `../textures/README.md`
- 🪪 Licensing / attribution: `../licenses/` and/or `../attribution.md` (if present)

---

## 🗓️ Changelog

- **2026-01-15** — 🆕 Created tiles README scaffold (contract + QA + provenance checklist)
