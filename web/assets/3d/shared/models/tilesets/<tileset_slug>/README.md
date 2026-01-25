# 🧱 Tileset — `<tileset_slug>` (3D)

![3D Tiles](https://img.shields.io/badge/format-3D%20Tiles-1f6feb)
![Cesium](https://img.shields.io/badge/viewer-CesiumJS-24292f)
![Provenance](https://img.shields.io/badge/provenance-evidence--first-success)
![FAIR+CARE](https://img.shields.io/badge/governance-FAIR%2BCARE-7c3aed)

> **What this is:** A **streamable 3D Tiles** package consumed by KFM’s **3D viewer (CesiumJS)**, designed to work alongside the **2D MapLibre** experience. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}  
> **Why it exists:** KFM uses 3D where it adds value (terrain/structures/volumetrics/AR) while keeping 2D as the “many-layers” workhorse. :contentReference[oaicite:2]{index=2}

---

## 🧭 Quick Links
- [📦 Folder Layout](#-folder-layout)
- [🧾 Metadata Contract (KFM-ready)](#-metadata-contract-kfm-ready)
- [🗺️ How KFM Loads This Tileset](#️-how-kfm-loads-this-tileset)
- [🏗️ Build / Update Pipeline (Provenance-first)](#️-build--update-pipeline-provenance-first)
- [✅ QA & Performance Checklist](#-qa--performance-checklist)
- [🔐 Governance, Sensitivity, Licensing](#-governance-sensitivity-licensing)
- [🧰 Troubleshooting](#-troubleshooting)

---

## 🎯 Purpose & Fit in KFM
KFM’s front-end supports **2D (MapLibre)** and **3D (CesiumJS)** views, and uses **open formats** so the same governed data services can power web, 3D, and future AR clients. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}  

This tileset lives under:

```text
web/assets/3d/shared/models/tilesets/<tileset_slug>/
```

and is intended to be referenced by:
- a **3D layer config** in the web app (Cesium “3D Tiles” layer), :contentReference[oaicite:5]{index=5}  
- a **Story Node step** (fly-to + toggle layers), :contentReference[oaicite:6]{index=6}  
- and/or an **AR experiment** consuming the same API + assets. :contentReference[oaicite:7]{index=7}

---

## 📦 Folder Layout

> Keep this folder **web-friendly**: deterministic paths, cacheable assets, and a small “meta spine” for provenance + integrity.

```text
📁 <tileset_slug>/
├─ 🧩 tileset.json                # 3D Tiles entrypoint (required)
├─ 📁 tiles/                      # tile payloads (b3dm/i3dm/pnts/glb…)
│  └─ ……
├─ 📁 textures/                   # optional (if not embedded)
│  └─ ……
├─ 📁 _meta/                      # KFM metadata & receipts (required in KFM)
│  ├─ kfm.asset.json              # KFM asset manifest (see contract below)
│  ├─ checksums.sha256            # integrity receipts (sha256 list)
│  ├─ attribution.md              # attribution + credits
│  ├─ license.txt                 # license text or pointer
│  ├─ preview.png                 # thumbnail used by UI/catalog
│  └─ CHANGELOG.md                # optional: human-readable changes
└─ README.md                      # you are here 🙂
```

### 🔑 Coordinate & Projection Expectations
KFM standardizes on **WGS84 (EPSG:4326)** for web alignment and records any reprojection in provenance. :contentReference[oaicite:8]{index=8}  
If your pipeline uses intermediate CRSs, ensure the final tileset’s georeferencing is consistent and documented. Also: CRS mixups are a classic source of “looks right in GIS, wrong in app” bugs. :contentReference[oaicite:9]{index=9}

---

## 🧾 Metadata Contract (KFM-ready)

KFM is **evidence-first**: assets are expected to have metadata and provenance so users can inspect “Layer Info” (source/license/how prepared). :contentReference[oaicite:10]{index=10}  
For data layers, KFM emphasizes catalogs and lineage (STAC/DCAT/PROV patterns). :contentReference[oaicite:11]{index=11}  

### ✅ Required: `_meta/kfm.asset.json`
Use this as the canonical “bridge” from web asset ➜ catalogs/graph/provenance:

```json
{
  "kfm": {
    "asset_kind": "3d_tileset",
    "tileset_slug": "<tileset_slug>",
    "title": "<Human title>",
    "summary": "<1–2 sentence description>",
    "dataset_id": "kfm.<domain>.<name>.v<major>",
    "version": "YYYYMMDD or semver",
    "created_utc": "2026-01-25T00:00:00Z",
    "spatial": {
      "crs": "EPSG:4326",
      "bbox_wgs84": [-102.05, 36.99, -94.59, 40.00]
    },
    "temporal": {
      "start": "YYYY-MM-DD",
      "end": "YYYY-MM-DD",
      "time_behavior": "static | time-sliced | time-dynamic"
    },
    "units": {
      "vertical": "meters",
      "notes": "Z-up or ECEF (document what you used)"
    },
    "licensing": {
      "license_spdx": "<SPDX id if possible>",
      "attribution_required": true,
      "source_credits": ["<org>", "<collection>", "<photogrammetry pipeline>"]
    },
    "governance": {
      "classification": "public | internal | restricted",
      "sensitivity_notes": "<if generalized/redacted>",
      "access_notes": "<who can see/download>"
    },
    "provenance": {
      "stac": "data/stac/<collection-or-item>.json",
      "dcat": "data/catalogs/<dataset>.jsonld",
      "prov": "data/prov/<run_id>.jsonld",
      "pipeline": {
        "name": "<pipeline name>",
        "run_id": "<run id>",
        "code_ref": "<git sha or tag>"
      }
    },
    "integrity": {
      "checksums_sha256_file": "_meta/checksums.sha256"
    },
    "distribution": {
      "primary": {
        "type": "http",
        "url": "/assets/3d/shared/models/tilesets/<tileset_slug>/tileset.json"
      },
      "optional_oci": {
        "enabled": false,
        "ref": "oci://<registry>/<repo>:<tag>",
        "digest": "sha256:<...>",
        "signature": "cosign://<...>"
      }
    }
  }
}
```

#### 📌 Why the OCI option exists (for big tilesets)
KFM proposes storing **large artifacts** (tilesets, PMTiles, GeoParquet, COGs) in an **OCI registry** via **ORAS**, then verifying with **Cosign** to guarantee content-addressed integrity and reproducibility. :contentReference[oaicite:12]{index=12}  

---

## 🗺️ How KFM Loads This Tileset

KFM’s web UI includes a 2D/3D viewer split: MapLibre for 2D and Cesium for 3D, with **3D Tiles** used for streaming 3D geospatial content. :contentReference[oaicite:13]{index=13}  
A Story Node can orchestrate camera moves and layer toggles using Markdown + JSON configs. :contentReference[oaicite:14]{index=14}  

### Example: “3D layer config” (illustrative)
```json
{
  "id": "tileset:<tileset_slug>",
  "type": "cesium-3d-tiles",
  "title": "<Human title>",
  "tilesetUrl": "/assets/3d/shared/models/tilesets/<tileset_slug>/tileset.json",
  "info": {
    "datasetId": "kfm.<domain>.<name>.v<major>",
    "provenance": "/assets/3d/shared/models/tilesets/<tileset_slug>/_meta/kfm.asset.json"
  },
  "visibility": {
    "default": false,
    "minZoomEquivalent": 10
  }
}
```

### ⏳ Time + Timeline compatibility
KFM treats **time as a first-class filter** (timeline slider drives requests / layer refresh). If your tileset is time-sliced, document the mapping from timeline → tileset variant. :contentReference[oaicite:15]{index=15}  

---

## 🏗️ Build / Update Pipeline (Provenance-first)

KFM enforces a canonical “pipeline spine” where published outputs must be traceable and described via catalogs before they’re used in the UI. :contentReference[oaicite:16]{index=16}  

### Suggested build stages (for this tileset)
1. **Source → Raw**: capture original scans/photogrammetry/LiDAR as immutable evidence  
2. **Raw → Work**: normalize, clean, coordinate alignment (log transformations)  
3. **Work → Processed**: produce optimized glTF/GLB + build 3D Tiles  
4. **Processed → Catalogs**: emit STAC/DCAT/PROV pointers for evidence-first publishing :contentReference[oaicite:17]{index=17}  
5. **Publish**:
   - small/medium: commit to repo under this folder
   - large: push to OCI registry, sign with Cosign, store digest + reference in `_meta/kfm.asset.json` :contentReference[oaicite:18]{index=18}  
6. **UI enablement**: register layer + attach Story Nodes if needed :contentReference[oaicite:19]{index=19}  

---

## ✅ QA & Performance Checklist

### 🧪 Functional checks (must pass)
- [ ] `tileset.json` loads in Cesium (no console errors) :contentReference[oaicite:20]{index=20}  
- [ ] Bounding volumes are correct (no “popping” miles away)
- [ ] CRS alignment verified vs 2D layers (WGS84 alignment expectations) :contentReference[oaicite:21]{index=21}  
- [ ] `_meta/checksums.sha256` generated and matches shipped files
- [ ] Attribution + license present (and correct)
- [ ] Provenance pointers filled (`stac`, `dcat`, `prov`, `pipeline.code_ref`) :contentReference[oaicite:22]{index=22}  

### ⚡ Performance checks (recommended)
- [ ] LOD progression is smooth (no huge jumps)
- [ ] Geometry + textures are optimized for web delivery (size budgets documented in `_meta/`)
- [ ] Consider CDN caching for heavy access (KFM anticipates caching / tile infrastructure at scale) :contentReference[oaicite:23]{index=23}  

---

## 🔐 Governance, Sensitivity, Licensing

### 🧷 Sensitivity patterns KFM supports
KFM’s governance approach anticipates cases where **exact locations shouldn’t be exposed**, using techniques like **location generalization**, access control, and sensitivity tagging in metadata. :contentReference[oaicite:24]{index=24}  

**If this tileset depicts sensitive resources**, document:
- what was generalized (e.g., offsets, snapping, masking),
- what the public can see,
- who can access the full-resolution version.

### 🔎 Query auditing & inference control (optional but useful)
If you’re generating derivative analytics (counts, hotspot queries, etc.), consider governance patterns like **query auditing** to reduce leakage risk from outputs. :contentReference[oaicite:25]{index=25}  

### 📜 License hygiene
KFM is opinionated about clear licensing and attribution to avoid downstream conflicts and preserve trust. :contentReference[oaicite:26]{index=26}  

---

## 🧰 Troubleshooting

### “My tileset is offset / rotated / underground”
- Confirm WGS84 alignment expectations, and document any transforms in provenance. :contentReference[oaicite:27]{index=27}  
- Validate CRS assumptions end-to-end (CRS confusion is a classic gotcha). :contentReference[oaicite:28]{index=28}  

### “It’s too big for the repo”
- Use OCI registry packaging + digest pinning + Cosign verification, then store only references here. :contentReference[oaicite:29]{index=29}  

### “How does this connect to stories?”
- Story Nodes are Markdown + JSON “guided tour” steps that can toggle 3D mode and load tilesets as part of the narrative. :contentReference[oaicite:30]{index=30}  

---

## 🧷 Maintainer Notes (fill these in)
| Field | Value |
|---|---|
| Tileset slug | `<tileset_slug>` |
| Dataset ID | `kfm.<domain>.<name>.v<major>` |
| Version | `YYYYMMDD` |
| Coverage | `<bbox / counties / site>` |
| Time range | `<start> → <end>` |
| License | `<SPDX>` |
| Sensitivity | `public/internal/restricted` |

---

## 🔭 Future-forward: 3D → AR
KFM’s roadmap explicitly connects 3D Tiles (Cesium) to future AR experiences, where the same 3D assets can be reused in a camera-based overlay client. :contentReference[oaicite:31]{index=31} :contentReference[oaicite:32]{index=32}

