---
title: "🗺️ Terrain Datasets Catalog (3D)"
path: "web/assets/3d/terrain/datasets/README.md"
version: "v1.0.0"
last_updated: "2026-01-15"
status: "active"
doc_kind: "Directory README"
license: "CC-BY-4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"

# Governance / compliance (project-standard; keep fields even if TBD)
governance_ref: "TBD"
ethics_ref: "TBD"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"

doc_uuid: "urn:kfm:doc:web:assets:3d:terrain:datasets:readme:v1.0.0"
commit_sha: "TBD"
doc_integrity_checksum: "sha256:TBD"
tags: ["kfm", "web", "assets", "3d", "terrain", "datasets", "catalog", "provenance"]
---

# 🗺️ Terrain Datasets Catalog (3D)

![KFM-MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Layer](https://img.shields.io/badge/web-assets-3D%20terrain-informational)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-purple)

> [!NOTE]
> This folder is the **catalog + runtime-facing registry** for *terrain source datasets* used to build and serve **web-ready terrain** (tiles, textures, 3D tilesets).  
> If you’re looking for **deployable terrain packs** (actual tiles/textures shipped to the client), go to: **`../packs/`**.

---

## 📌 Purpose

This directory exists to keep a clean separation between:

- **🧱 Terrain datasets (source truth)** — where the elevation/terrain *came from*, what it covers, how it’s licensed, and what it *produces*.
- **📦 Terrain packs (web deliverables)** — how we publish terrain to the browser (tile pyramids, textures, streaming formats).
- **🧾 Provenance & governance** — traceable lineage, checksums, and clear attribution (no “mystery DEMs”).

In short: **datasets describe**, **packs ship**, **schemas validate**.

---

## 🧭 Where this fits in the terrain subsystem

```text
📁 web/assets/3d/terrain/
├─ 📁 datasets/         👈 (you are here) dataset registry + manifests
│  ├─ 📁 tiles/         tile-index datasets (registries, coverage maps, lookups)
│  └─ 📄 README.md
├─ 📁 packs/            web-ready terrain “releases” (tiles + textures + metadata)
└─ 📁 schema/           JSON schema + examples for manifests (validation contracts)
```

Helpful neighbors:

- 📦 `../packs/` — “what the browser downloads”
- 🧪 `../schema/examples/` — “what valid manifests look like”
- 🧩 `./tiles/` — “dataset-level tile registries & indexes”

---

## 🧠 Core concepts: Dataset vs Pack vs Tile

| Concept | What it is | Lives in | Changes when… |
|---|---|---|---|
| **Dataset** | The canonical *source description* (coverage, resolution, licensing, provenance) | `datasets/` | upstream source changes, new processing assumptions, new lineage |
| **Pack** | A web-consumable *release artifact* (tiles/textures/tileset json) | `packs/` | compression/LOD changes, new tile format, new styling/texture pipeline |
| **Tile** | One chunk in a pyramid (Z/X/Y or quadtree) | inside packs | regeneration or retile |

> [!TIP]
> **A dataset can produce multiple packs** (e.g., different LOD strategies, different quantization, different texture sets).

---

## 🧾 What belongs in `datasets/`

✅ Good fits:

- Dataset manifests (`dataset.json`, `dataset.stac.json`, `provenance.json`, etc.)
- Dataset-to-pack mapping (“this dataset produced these packs”)
- Dataset coverage geometry (lightweight footprints; simplified)
- Runtime registries that the web app can load quickly (small JSON, small previews)

🚫 Not allowed here:

- Raw LiDAR point clouds (LAZ/LAS), full-resolution GeoTIFFs, huge intermediate rasters  
- Anything that would bloat the web bundle or break CDN assumptions

> [!WARNING]
> If it’s **too big to be served as a static web asset**, it doesn’t belong under `web/assets/…`.  
> Store raw/heavy artifacts in the **data pipeline storage** layer (and reference them from manifests).

---

## 🧩 Recommended manifest pattern

A dataset folder typically follows a “minimum viable governance” set:

```text
📁 datasets/
└─ 📁 <dataset_slug>/
   ├─ 📄 dataset.json              # minimal runtime descriptor (fast to load)
   ├─ 📄 dataset.prov.json         # provenance / lineage summary (PROV-ish)
   ├─ 📄 license.json              # license + attribution requirements
   ├─ 📄 coverage.geojson          # simplified footprint (optional)
   ├─ 📁 previews/                 # tiny thumbnails (optional)
   └─ 📄 README.md                 # dataset-specific notes (optional)
```

### 🔤 Dataset slug rules

- `kebab-case`
- include **region + source + resolution + version**
- avoid spaces, avoid ambiguous acronyms

Examples (illustrative):

- `flint-hills-lidar-1m_v1`
- `ks-statewide-dem-10m_v2`

---

## ⚡ Performance & streaming expectations

Terrain in the browser needs **fast selective access**, not “download the world.”

Recommended publishing strategies (pick what fits the product):

- **Tile pyramids** for stable, frequently used layers (CDN-friendly, cacheable)
- **COG-like access patterns** for raster sources (range requests + overviews), when serving raster-backed terrain derivatives
- **LOD management** (coarse terrain when zoomed out; refine on zoom-in)

---

## 🔗 Linking datasets to packs

A dataset manifest should declare which pack(s) it produced (or is compatible with). Keep it simple and explicit:

```json
{
  "dataset_id": "TBD",
  "dataset_version": "TBD",
  "title": "TBD",
  "kind": "terrain",
  "covers": { "bbox": "TBD", "srs": "TBD" },
  "resolution_m": "TBD",
  "license_ref": "./license.json",
  "derived_packs": [
    "../packs/<pack_slug>/"
  ]
}
```

> [!NOTE]
> The exact schema is governed by `../schema/`. If you add fields, update the schema and examples together.

---

## 🧾 Licensing & attribution rules (non-negotiable)

Terrain is often sourced from government / research / partner programs. Every dataset must include:

- **license terms**
- **required attribution string(s)**
- **redistribution constraints** (if any)
- **derived-work rules** (if any)

Put the human-readable summary in `license.json` (or `README.md`) and keep a machine-parseable form too.

---

## 🧬 Provenance contract (dataset-level)

At minimum, dataset provenance should be able to answer:

- **Where did it come from?** (source IDs / URLs / agencies)
- **What processing happened?** (toolchain summary, major parameters)
- **What did it produce?** (pack IDs, tile sets)
- **How do we verify integrity?** (checksums, content hashes)

> [!TIP]
> “Provenance-first” means: **every terrain surface you can see must be traceable** back to an auditable lineage.

---

## 🧪 Validation checklist (Definition of Done ✅)

- [ ] YAML front-matter filled in (this README)
- [ ] New dataset manifests validate against `../schema/`
- [ ] License + attribution present and unambiguous
- [ ] Provenance summary present (even if minimal)
- [ ] No large binaries committed under `web/assets/…`
- [ ] Any new pack links resolve correctly (`derived_packs[]`)
- [ ] Paths use forward slashes and remain repo-relative

---

## 🔭 Next pointers

- 📦 Build artifacts: `../packs/`
- 🧱 Tile dataset registries: `./tiles/`
- 🧪 Schemas + examples: `../schema/` and `../schema/examples/`

---

### 🧾 Glossary (quick)

- **DEM**: Digital Elevation Model  
- **DTM**: Digital Terrain Model (bare earth)  
- **DSM**: Digital Surface Model (includes buildings/trees)  
- **LOD**: Level of Detail  
- **COG**: Cloud-Optimized GeoTIFF (pattern)  
- **3D Tiles**: streaming format for 3D geospatial content (tilesets)
