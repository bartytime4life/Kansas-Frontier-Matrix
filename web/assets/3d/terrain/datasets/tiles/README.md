---
title: "🧱 Terrain Dataset Tiles (Web-Ready) — README"
path: "web/assets/3d/terrain/datasets/tiles/README.md"
version: "v1.0.0"
last_updated: "2026-01-15"
status: "active"
doc_kind: "README"
project: "Kansas Frontier Matrix (KFM)"
component: "web-assets"
subsystem: "3d-terrain"
tags: ["3d", "terrain", "tiles", "elevation", "webgl", "cesium", "maplibre", "datasets"]
license: "CC-BY-4.0"

# KFM documentation protocol
markdown_protocol_version: "KFM-MDP v11.2.6"
governance_ref: "docs/governance/GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"

# Identity
semantic_document_id: "kfm:web:assets:3d:terrain:datasets:tiles:readme"
doc_uuid: "urn:kfm:doc:web:assets:3d:terrain:datasets:tiles:readme:v1.0.0"
commit_sha: "TBD"
doc_integrity_checksum: "sha256:TBD"
---

# 🧱 Terrain Dataset Tiles (Web-Ready)

[![KFM-MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-blue)](#)
[![3D Terrain](https://img.shields.io/badge/3D-Terrain-6f42c1)](#)
[![Tiles](https://img.shields.io/badge/Format-Tiles-informational)](#)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-brightgreen)](#)

> **Purpose:** This folder stores **web-servable terrain tile pyramids** (and their required metadata) that are consumed by 3D terrain “packs” and viewers.  
> **Non-purpose:** This is **not** the home for raw DEM/LiDAR, processing workspaces, or one-off exports.

---

## 🧭 Where this fits in the terrain stack

```text
web/assets/3d/terrain/
├─ 📦 packs/            → “curated deliverables” (a pack may reference tiles + textures + docs)
├─ 🗃️ datasets/
│  ├─ 🧱 tiles/          → ✅ THIS FOLDER: reusable tile pyramids (web-ready)
│  └─ 📚 README.md       → dataset index + conventions (parent doc)
└─ 🧬 schema/            → JSON schemas + examples
```

- **Datasets** are the reusable building blocks (tile pyramids + metadata).
- **Packs** are what the UI tends to mount (they can point at one or more datasets).

➡️ See also: [`web/assets/3d/terrain/datasets/README.md`](../README.md)

---

## ✅ What belongs here

Typical tile pyramid products (pick what your pipeline produces):

- 🟫 **Elevation/DEM tiles** (heightmap encodings like `terrain-rgb`, `terrarium`, etc.)
- 🧊 **Quantized mesh terrain tiles** (Cesium-style quadtree tiles, if used)
- 🌊 **Water masks** / land-water classification tiles (optional)
- 🧾 **Tile manifests** + bounds + integrity + attribution (required)

---

## ❌ What does *not* belong here

- 🧪 Pipeline scratch outputs (temp, intermediates, cache)
- 🗺️ Raw rasters / LAS / LAZ / point clouds (source-of-truth lives in `data/…`)
- 🧰 Tooling scripts (live in `tools/…` or pipeline repos)
- 🧍 Any sensitive coordinates that should be generalized/redacted

---

## 📦 Tileset folder contract (required layout)

Each tileset gets its own directory:

```text
web/assets/3d/terrain/datasets/tiles/
└─ 🧱 <tileset_id>/
   ├─ 📄 README.md
   ├─ 🧾 manifest.json
   ├─ 🧭 bounds.geojson
   ├─ 🧷 attribution.md
   ├─ 🪪 licenses/
   │  └─ README.md
   ├─ 🔐 checksums.sha256
   └─ 🧱 tiles/
      └─ z/x/y.<ext>
```

### 🔑 `tileset_id` naming rules
Keep IDs predictable and stable:

- ✅ lowercase, digits, hyphens/underscores  
- ✅ include “what + resolution + version” when relevant  
- ✅ no spaces, no “final”, no dates as the *only* differentiator

Examples:
- `flint-hills-lidar-1m_v1`
- `kansas-dem-10m_v2`
- `usgs-3dep-1m_subset_v1`

---

## 🧠 Tiling scheme + CRS rules (declare it, don’t assume it)

Your manifest must declare:

- `tiling_scheme`: `XYZ` or `TMS` (and any framework-specific variant)
- `crs`: `EPSG:3857` (common) or `EPSG:4326` (less common) — **be explicit**
- `minzoom`, `maxzoom`
- `bounds` (WGS84 lon/lat bounding box, even if tiles are WebMercator)

### 🧾 Recommended “format families”
| Family | Typical ext | Typical use | Notes |
|---|---:|---|---|
| Heightmap RGB | `png`, `webp` | WebGL height sampling | Document encoding (terrarium vs terrain-rgb, etc.) |
| Quantized mesh | `terrain` / binary | Cesium-style terrain streaming | Usually needs a root metadata file (e.g., `layer.json`) |
| Mask tiles | `png`, `webp` | Water/land or clip masks | Declare value semantics (0/255, etc.) |

---

## 🧾 Manifest contract (minimum)

`manifest.json` is the “contract” a loader can trust without guessing.

```json
{
  "kfm": {
    "tileset_id": "example-dem-10m_v1",
    "type": "terrain-tiles",
    "version": "v1"
  },
  "tile_pyramid": {
    "tiling_scheme": "XYZ",
    "crs": "EPSG:3857",
    "minzoom": 6,
    "maxzoom": 14,
    "tile_path_template": "tiles/{z}/{x}/{y}.png"
  },
  "coverage": {
    "bounds_wgs84": [-97.9, 38.4, -95.0, 39.6],
    "approx_resolution_m": 10
  },
  "format": {
    "family": "heightmap-rgb",
    "encoding": "TBD (terrarium|terrain-rgb|custom)",
    "nodata": "TBD"
  },
  "provenance": {
    "source_dataset_ref": "TBD (STAC/DOI/internal-id)",
    "pipeline_run_ref": "TBD (PROV run id / workflow id)",
    "generated_utc": "2026-01-15T00:00:00Z"
  },
  "integrity": {
    "checksums_file": "checksums.sha256"
  },
  "licensing": {
    "license_spdx": "TBD",
    "attribution_file": "attribution.md"
  }
}
```

> If your tileset format requires additional top-level files (e.g., a Cesium terrain metadata file), include them and reference them from the manifest.

---

## 🔐 Integrity: checksums are not optional

- `checksums.sha256` should cover **manifest + metadata + tiles**
- Prefer **relative paths** so the file is portable across hosts/CDNs.

Example line:
```text
<sha256>  tiles/12/1042/1534.png
```

---

## 🧷 Attribution + licensing

Every tileset must ship with:

- `attribution.md` — human-readable credit text (and any required logos as separate assets if needed)
- `licenses/README.md` — license terms + upstream links + usage constraints

> If attribution is complex, keep `attribution.md` short and link to the longer license record in `licenses/`.

---

## 🚦 Quality gates (recommended)

Before a tileset is considered “shippable”:

- ✅ manifest validates against schema (if available)
- ✅ min/max zoom present and consistent with on-disk tiles
- ✅ `bounds.geojson` exists + matches declared bounds
- ✅ checksum file present and current
- ✅ attribution + license present
- ✅ no obviously broken tiles (0-byte files, empty images, etc.)

---

## 🧩 Consumption: how packs should reference tilesets

Packs should reference tilesets **by path and manifest**, not by “guessing”:

- ✅ `datasets/tiles/<tileset_id>/manifest.json`
- ✅ `datasets/tiles/<tileset_id>/tiles/{z}/{x}/{y}.<ext>`

This makes it safe to:
- swap encodings
- revise max zoom
- add mask layers
- publish the same tileset via different hosts/CDNs

---

## 🧰 Adding a new tileset (workflow)

1. 🧾 Create folder: `datasets/tiles/<tileset_id>/`
2. 🧱 Add tiles under `tiles/z/x/y.ext`
3. 🧭 Write `bounds.geojson`
4. 🧾 Write `manifest.json`
5. 🧷 Add `attribution.md` + `licenses/README.md`
6. 🔐 Generate `checksums.sha256`
7. ✅ Add/Update the parent index: `datasets/README.md`

---

## 🔗 Related docs & neighbors

- 📚 Datasets index: `../README.md`
- 🧬 Schema examples: `../../schema/examples/README.md`
- 📦 Terrain packs: `../../packs/`
- 🎨 Terrain textures: `../../packs/**/textures/` (pack-specific)

---

## 📎 References (project-local)

- KFM documentation + provenance-first framing:  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- Markdown governance patterns (front-matter, DoD checklists, CARE labels):  [oai_citation:1‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  
- System design notes for map/terrain serving concepts:  [oai_citation:2‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)  

---
