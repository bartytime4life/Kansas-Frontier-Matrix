<!--
📍 Path: web/assets/3d/shared/models/tilesets/<tileset_slug>/content/README.md
🎯 Purpose: This folder is a *runtime* content pack (Cesium 3D Tiles) for Kansas Frontier Matrix (KFM).
-->

# 🧱 Tileset Content Pack — `<tileset_slug>` 🌾🗺️

![Format](https://img.shields.io/badge/format-3D%20Tiles-blue)
![Runtime](https://img.shields.io/badge/runtime-CesiumJS%20%2B%20KFM-purple)
![Governance](https://img.shields.io/badge/governance-STAC%20%2B%20DCAT%20%2B%20PROV-brightgreen)
![Policy](https://img.shields.io/badge/policy-OPA%20%2F%20Conftest-critical)
![Status](https://img.shields.io/badge/status-fill%20me%20in-lightgrey)

> **KFM principle:** “the map behind the map” 🧭  
> This tileset is **not** “just pretty 3D.” It must be **traceable, reproducible, and policy-checked**.

---

## ✅ Quick facts (fill these in)

| Field | Value |
|---|---|
| **Tileset slug** | `<tileset_slug>` |
| **Human title** | `<tileset_title>` |
| **Short description** | `<1–2 sentences>` |
| **KFM dataset ID** | `<kfm_dataset_id>` |
| **Tileset entrypoint** | `./tileset.json` |
| **Viewer** | CesiumJS (KFM 3D globe) 🌍 |
| **Display CRS** | WGS84 / EPSG:4326 *(KFM web standard)* |
| **Original CRS** | `<epsg_code_or_wkt_if_not_4326>` |
| **Vertical units** | `meters` *(recommended)* |
| **Temporal coverage** | `<yyyy–yyyy or ISO8601 range>` |
| **Geographic coverage** | `<bbox or region name>` |
| **Sensitivity** | `public` / `restricted` / `sensitive` |
| **License (SPDX)** | `<e.g., CC-BY-4.0>` |
| **Attribution** | `<source org / authors>` |
| **Last updated** | `<YYYY-MM-DD>` |

---

## 🧭 What belongs in `content/` (and what does *not*)

### ✅ DO put here
- **Runtime** 3D Tiles output: `tileset.json` + tile payloads (`.b3dm`, `.i3dm`, `.pnts`, `.glb`, etc.)
- **Runtime-facing metadata** needed for KFM’s trust UX (provenance, license, sensitivity) 🔎
- A small preview/thumbnail (optional but highly recommended)

### 🚫 DO NOT put here
- Blender / GIS project files (`.blend`, `.qgz`, `.qmd`, `.psd`, etc.)
- Raw source datasets (those live under KFM’s **immutable** `data/raw/` trust boundary) 🔒
- “Hand-edited” processed outputs (KFM expects deterministic, config/code-driven generation)

> 💡 Keep `content/` **deployable and portable** (works when served statically *and* when packaged into offline/field packs).

---

## 🗂️ Expected folder structure 📦

```text
web/
└─ assets/
   └─ 3d/
      └─ shared/
         └─ models/
            └─ tilesets/
               └─ <tileset_slug>/
                  └─ 📁 content/                   # 🧱 The actual tile payloads, associated metadata, and documentation
                     ├─ 🧾 tileset.json            # ✅ REQUIRED: Manifest for tileset metadata + configuration
                     ├─ 📁 tiles/                 # ✅ REQUIRED: Actual tile payloads (e.g., b3dm, i3dm, pnts)
                     ├─ 🧾 kfm.tileset.meta.json   # ✅ REQUIRED: KFM metadata contract (tile specifics, context)
                     ├─ 🧬 provenance.jsonld       # ✅ REQUIRED: Provenance metadata (W3C PROV lineage)
                     ├─ ⚖️ LICENSE.txt            # ✅ REQUIRED: License info (or COPYING) for open use
                     ├─ 🧷 ATTRIBUTION.md         # ✅ RECOMMENDED: Attribution information (if third-party contributions)
                     ├─ 🖼️ thumbnail.(png|jpg|webp) # ✅ RECOMMENDED: Thumbnail for preview (small, efficient)
                     └─ 📄 README.md              # ✅ REQUIRED: Documentation on the tileset, its purpose, and usage
```

---

## 🔌 How KFM uses this tileset

### 2D ↔ 3D continuity (MapLibre + Cesium)
KFM’s UI supports both:
- **2D Interactive Map Viewer** (MapLibre GL JS)
- **3D Globe & Terrain Visualization** (CesiumJS)

Your tileset should assume it may be toggled in/out while users are navigating time, layers, and story steps. ✅

### 🧩 Layer provenance & “trust UI”
KFM intentionally surfaces provenance/credits/citations in the UI (“map behind the map”).  
This tileset must ship enough metadata to populate:
- layer info dialogs
- layer provenance panels
- click/identify popups in 3D
- exports/shares carrying proper credits

### 📚 Story Nodes & camera moves (optional, but powerful)
Tilesets can be used inside **Story Nodes** (interactive narratives) that:
- enable/disable layers per step
- animate camera transitions (including 3D “fly to” moments)
- bind evidence/citations to narrative claims

If this tileset is intended for a story, add the story reference(s) in metadata and provide an evidence manifest (see below). 🎬

### 📱 Offline packs & AR readiness (forward-looking)
KFM plans offline/field packs and AR extensions that reuse the same 3D assets.  
To stay future-proof:
- keep URIs in `tileset.json` **relative** whenever possible
- avoid hard-coding hostnames
- consider providing a simplified LOD or “mobile” variant (optional)

---

## 🧾 KFM Tileset Metadata Contract (`kfm.tileset.meta.json`) ✅

Create **`kfm.tileset.meta.json`** alongside `tileset.json`.

<details>
<summary>📄 Suggested schema (copy/paste template)</summary>

```json
{
  "kfm": {
    "id": "<kfm_dataset_id>",
    "slug": "<tileset_slug>",
    "title": "<tileset_title>",
    "description": "<short_description>",
    "type": "3d-tiles",
    "entrypoint": "tileset.json",

    "coverage": {
      "bbox_wgs84": [<minLon>, <minLat>, <maxLon>, <maxLat>],
      "time_range": {
        "start": "<ISO8601 or null>",
        "end": "<ISO8601 or null>"
      }
    },

    "crs": {
      "display": "EPSG:4326",
      "source": "<EPSG or WKT>",
      "vertical_units": "meters"
    },

    "sensitivity": {
      "level": "public",
      "notes": "<if restricted/sensitive, explain masking/generalization + access rules>"
    },

    "credits": {
      "attribution": "<organization / authors>",
      "source_url": "<if applicable>",
      "license_spdx": "<e.g., CC-BY-4.0>"
    },

    "provenance": {
      "prov_jsonld": "provenance.jsonld",
      "stac_item_id": "<stac_item_id>",
      "dcat_dataset_id": "<dcat_dataset_id>"
    },

    "ui": {
      "thumbnail": "thumbnail.png",
      "default_visibility": false,
      "tags": ["3d", "terrain", "historic"]
    },

    "maintenance": {
      "owner": "<team_or_handle>",
      "last_updated": "<YYYY-MM-DD>",
      "build_pipeline": "<script_or_pipeline_name>",
      "version": "<semver_or_git_sha>"
    }
  }
}
```
</details>

> ✅ **Why this exists:** KFM’s architecture and governance expect **policy gates** that enforce license presence, sensitivity classification, and STAC/DCAT/PROV completeness before data is shown to users.

---

## 🧬 Provenance (`provenance.jsonld`) ✅

KFM’s “provenance-first” intake philosophy expects that every output (including 3D tiles) can be traced back to:
- original inputs (raw evidence)
- transformation steps (code/config)
- responsible agents (people/bots)
- processing environment (optional but encouraged)

<details>
<summary>🧾 Minimal PROV JSON-LD skeleton (starter)</summary>

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@graph": [
    {
      "@id": "urn:kfm:activity:<build_run_id>",
      "@type": "prov:Activity",
      "prov:startedAtTime": "<ISO8601>",
      "prov:endedAtTime": "<ISO8601>",
      "prov:wasAssociatedWith": "urn:kfm:agent:<name_or_bot>",
      "prov:used": [
        "urn:kfm:entity:<raw_input_1>",
        "urn:kfm:entity:<raw_input_2>"
      ]
    },
    {
      "@id": "urn:kfm:entity:<tileset_slug>:tileset",
      "@type": "prov:Entity",
      "prov:wasGeneratedBy": "urn:kfm:activity:<build_run_id>",
      "prov:generatedAtTime": "<ISO8601>",
      "prov:atLocation": "web/assets/3d/shared/models/tilesets/<tileset_slug>/content/tileset.json"
    }
  ]
}
```
</details>

---

## 🧩 STAC/DCAT/PROV wiring (required for publishing) 🔗

Even though this tileset’s bytes live under `web/assets/…`, **publishing it in KFM** requires the “evidence triplet”:
- **STAC** (items/collections for spatial/temporal indexing)
- **DCAT** (dataset-level catalog metadata)
- **PROV** (lineage: what produced what, from where)

> 🚧 **Policy rule of thumb:** “No bypassing catalogs.” If it’s visible in the UI, it must be registered in the catalogs and have provenance.

### STAC asset hint (local/static serving)
- Use an asset `href` pointing to your served `tileset.json` (or to an artifact registry ref, see OCI option).

### 📦 OCI artifact option (recommended for “big tilesets”)
KFM proposals include treating large artifacts (like tilesets) as **OCI artifacts** (content-addressed, signed, with attached provenance).

If you go this route:
- keep `content/` minimal (or even empty except README + metadata)
- publish tileset bytes to your registry
- reference them from STAC/DCAT with an OCI URI

---

## 🛡️ Policy & QA checklist ✅

### Required gates (MUST pass)
- [ ] `LICENSE.txt` present and matches metadata license
- [ ] sensitivity level assigned (`public/restricted/sensitive`)
- [ ] provenance present (`provenance.jsonld`)
- [ ] metadata present (`kfm.tileset.meta.json`)
- [ ] STAC/DCAT/PROV records exist *outside this folder* and reference this tileset
- [ ] URIs inside `tileset.json` are **portable** (prefer relative paths)

### Recommended quality checks (SHOULD pass)
- [ ] tile payload sizes are reasonable (avoid giant single tiles)
- [ ] geometry has sensible LOD progression (no “LOD cliff”)
- [ ] bounding volumes correctly contain content
- [ ] textures are optimized for web delivery
- [ ] click/identify metadata is meaningful (e.g., feature IDs, names, dates) 🔍

---

## 🔐 Sensitivity & ethical handling 🧡

KFM explicitly supports data sensitivity controls (e.g., protecting sensitive archaeological locations).  
If this tileset includes sensitive locations or features:

✅ Prefer one (or more) of these strategies:
- **generalize** precise locations (aggregate / blur / offset)
- **restrict access** (role-based, gated distribution)
- provide a **public-safe** version and keep the precise one restricted

📌 Document the approach in:
- `kfm.tileset.meta.json → kfm.sensitivity`
- `ATTRIBUTION.md` and/or a `SENSITIVITY.md` (optional)

---

## 🧰 Optional: Evidence manifest for story use 🎬🧾

If this tileset supports a Story Node or a narrative claim, add:

- `EVIDENCE.manifest.json` *(optional, recommended)*

Example idea:
- list claims the tileset supports
- list citations (STAC items, documents, images)
- bind to Story Node step IDs

This aligns with the “evidence-first narrative” approach being proposed for KFM’s storytelling system.

---

## 🧯 Troubleshooting

**Nothing shows in 3D**
- Confirm KFM is in **3D mode** (Cesium) and the layer is enabled.
- Check that `tileset.json` loads over HTTP (not `file://`).
- Confirm relative URIs resolve correctly from the `tileset.json` location.

**Tiles load but are in the wrong place**
- Confirm georeferencing and CRS assumptions.
- Ensure you recorded the original CRS in `kfm.tileset.meta.json` and used WGS84 for web display.

**Policy gate fails**
- Missing license, sensitivity, provenance, or catalog records are expected hard failures.  
  Fix the metadata rather than bypassing the gate. ✅

---

## 🧠 Maintainer notes (recommended)

- Owner: `<team_or_handle>`
- Rebuild command / pipeline: `<script_or_pipeline>`
- Source datasets: `<stac_item_ids or urls>`
- Known limitations: `<brief list>`
- TODO: `<next improvements>`

---

## 📚 Related docs & resources (KFM)

### Core KFM design docs
- 🧭 UI: MapLibre (2D) + Cesium (3D), provenance-first UX, Story Nodes, Offline/AR concepts
- 🧬 Data intake: immutable raw evidence, deterministic ETL, STAC/DCAT/PROV “evidence triplet”
- 🤖 AI: Focus Mode citations + policy gates
- 🔐 Governance: OPA/Conftest policy pack proposals + “fail closed” philosophy

### 📦 Resource vaults (deep dives)
These PDFs contain embedded books/papers on WebGL, mapping platforms, geospatial graphics, and data engineering.  
Open them in a PDF reader that supports **PDF Portfolios**:
- `AI Concepts & more.pdf`
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf`
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf`
- `Various programming langurages & resources 1.pdf` *(portfolio shell / index)*

---

> ✅ If you fill in the metadata + provenance sections above, this tileset becomes “KFM-native”: discoverable, explainable, and safe to publish.

