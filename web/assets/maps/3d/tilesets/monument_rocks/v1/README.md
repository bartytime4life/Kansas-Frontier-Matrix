---
title: "Monument Rocks 🗿 — 3D Tiles Payloads (v1/tiles)"
version: "v1"
status: "active"
doc_kind: "Asset README"
dataset_id: "urn:kfm:tileset:monument_rocks:v1"
last_updated: "2026-01-17"
license: "SEE: ../metadata.json (required)"
crs: "WGS84 (EPSG:4326)"
formats:
  - "3D Tiles"
  - "b3dm / i3dm / pnts (as applicable)"
  - "glTF/GLB payloads (embedded)"
---

# 🗿 Monument Rocks — 3D Tiles payloads (`v1/tiles/`)

![Format](https://img.shields.io/badge/format-3D%20Tiles-blue)
![Viewer](https://img.shields.io/badge/viewer-CesiumJS-informational)
![KFM](https://img.shields.io/badge/KFM-provenance--first-brightgreen)
![Status](https://img.shields.io/badge/status-active-success)

This folder contains the **binary tile payloads** referenced by the parent tileset (`../tileset.json`) for the Monument Rocks 3D experience. The intent is to serve these as **static web assets** and stream them into the KFM 3D viewer (CesiumJS) using the **open 3D Tiles standard**.  [oai_citation:0‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

> 🧠 Context: Monument Rocks is explicitly called out as a “Kansas From Above” 3D story anchor (with a 3D model) in the project’s story/experience planning.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📦 What lives in `tiles/`

Typical 3D Tiles payloads you may see here:

- 🧱 **Batched 3D Models**: `*.b3dm` (common for buildings/meshes)
- 🌲 **Instanced models**: `*.i3dm` (common for repeated objects)
- ☁️ **Point clouds**: `*.pnts` (if the source is LiDAR/photogrammetry point data)
- 🧩 **Embedded glTF/GLB**: contained inside the tile payloads (not usually stored as loose `.glb` files)
- 🧵 **Textures**: often embedded; if external textures exist, keep them **relative** and **versioned**

📌 **Do not rename/move this folder lightly.** 3D Tiles `content.uri` paths in `../tileset.json` are commonly relative (e.g., `tiles/0/0/0.b3dm`). Renames break streaming.

---

## 🗂️ Expected layout

Your on-disk layout should look *roughly* like this:

```text
📁 web/assets/maps/3d/tilesets/monument_rocks/
└─📁 v1/
  ├─📄 tileset.json          👈 root tileset entrypoint (loaded by viewer)
  ├─📄 metadata.json         👈 KFM data contract + provenance (required)
  └─📁 tiles/
    ├─📄 README.md           👈 you are here
    ├─🧱 0/0/0.b3dm          👈 example (structure may vary)
    ├─🧱 0/0/1.b3dm
    └─… (more tiles / subfolders)
```

If your tiler outputs a different hierarchy (flat files, hashed names, etc.), that’s fine—**the only hard rule** is: `../tileset.json` must correctly reference whatever is inside this folder.

---

## 🚀 Quick load (CesiumJS)

Use the **parent** tileset URL (not `tiles/` directly):

```js
// Example: load the tileset in CesiumJS
const tileset = new Cesium.Cesium3DTileset({
  url: "/assets/maps/3d/tilesets/monument_rocks/v1/tileset.json",
});

viewer.scene.primitives.add(tileset);
viewer.zoomTo(tileset);
```

KFM’s web stack explicitly anticipates a 3D viewer (CesiumJS) alongside the 2D map stack, and 3D Tiles is part of the planned/accepted interchange format for that viewer.  [oai_citation:3‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H) [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧭 Spatial reference expectations

KFM’s internal web mapping standard is **WGS84 (EPSG:4326)** for general spatial referencing. Make sure the tileset is georeferenced consistently with the rest of the platform.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Practical implications:

- 🌍 The tileset should land in the correct longitude/latitude position without manual offsets.
- 📏 Elevation units should be consistent (typically meters) and documented in `../metadata.json`.

---

## 🧾 Provenance & metadata requirements (KFM “hard rules”)

KFM is **contract-first + provenance-first**: anything shown in the UI / Focus Mode must be traceable to cataloged sources and provable processing. The platform treats **metadata + lineage as fundamental**, and disallows “mystery layers.”  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

The broader project vision is explicit: **citations and metadata are first‑class data; nothing is a “black box.”**  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### ✅ Required sibling file: `../metadata.json`

This tileset should ship with a dataset “data contract” JSON capturing source + license + processing. KFM uses open standards like **STAC / DCAT / PROV-O** to formalize these fields.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**Recommended `metadata.json` template (minimum):**
```json
{
  "id": "monument_rocks_v1_tileset",
  "title": "Monument Rocks (Kansas) — 3D Tileset",
  "version": "v1",
  "asset_kind": "3d-tiles",
  "crs": "EPSG:4326",
  "license": "TBD",
  "source": [
    {
      "name": "TBD",
      "type": "photogrammetry|lidar|hand-modeled|other",
      "url_or_catalog_id": "TBD",
      "retrieved_at": "TBD"
    }
  ],
  "processing": [
    {
      "step": "tiling",
      "tool": "Cesium ion | 3d-tiles-tools | other",
      "params": { "TBD": true },
      "performed_at": "TBD"
    }
  ],
  "spatial_extent": {
    "bbox_wgs84": [ "minLon", "minLat", "maxLon", "maxLat" ]
  },
  "notes": "Citations + lineage are required for KFM acceptance."
}
```

### 🔒 Focus Mode compatibility

Focus Mode is intended to show only provenance-linked content; there’s a “hard gate” that prevents content without sources/IDs from appearing. Treat `metadata.json` as required, not optional.  [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔄 Versioning rules (`v1/`)

Version folders exist so we can ship improvements without breaking downstream URLs.

- ✅ **Patch-level fixes** (typos in metadata, repack tiles without changing URIs) can remain in `v1/`
- ⚠️ **Breaking changes** (different scale/origin, different URI layout, large geometry edits, re-tiling that changes tile IDs) should become `v2/`

Rule of thumb: if `tileset.json` or tile URIs change in a way that breaks cached links, bump the major version folder.

---

## 🧪 Validation checklist (before merge/release)

### Load / integrity
- [ ] `../tileset.json` loads in the Cesium viewer with no missing resources
- [ ] No 404s for `content.uri` inside `tileset.json`
- [ ] Visual sanity check: model appears in the correct location and orientation

### Geospatial correctness
- [ ] CRS alignment: expected WGS84 integration with the rest of KFM web mapping conventions  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Heights/elevations documented in `../metadata.json`

### Provenance gates
- [ ] `../metadata.json` exists and includes **source, license, processing steps**
- [ ] No “mystery tiles”: everything here is attributable and reproducible per KFM policy  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🌐 Hosting & caching notes (static assets)

These files are designed to be served from a static web server/CDN:

- ✅ Prefer **long cache TTLs** for tile payloads (they’re versioned)
- ✅ Ensure correct MIME handling (JSON as `application/json`; binary tiles as `application/octet-stream`)
- ✅ Enable HTTP range requests if supported (helps some clients)

---

## 🛠️ Regenerating tiles (suggested workflow)

A typical workflow is:

1. 📥 Acquire source model/scan (photogrammetry, LiDAR, curated mesh)
2. 🧹 Normalize + clean (units, coordinate origin, decimation, textures)
3. 🧱 Tile into 3D Tiles (Cesium ion or an open tiler)
4. ✅ Validate + document provenance
5. 📦 Drop outputs into `v*/tiles/` + update `tileset.json` + `metadata.json`

If using Cesium ion, note that it provides a tiling workflow for web streaming of 3D content (commonly used in practice for 3D Tiles pipelines).  [oai_citation:12‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq)

---

## 🔗 Related (nearby files)

- `../tileset.json` — tileset entrypoint for streaming
- `../metadata.json` — KFM data contract + provenance record (required)
- `../../../../..` — KFM web viewer stack (MapLibre 2D + Cesium 3D)  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📎 Project references (why this README is strict)

- KFM mission + provenance-first stance (“citations and metadata are first-class data; nothing is a black box”).  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Contract-first + provenance-first enforcement; no “mystery layers”; metadata contracts required.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM web mapping stack notes (MapLibre 2D, CesiumJS 3D; open standards).  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- 3D expansion plan and 3D Tiles as a supported/expected format for Cesium-based viewing.  [oai_citation:17‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
- Monument Rocks as a planned 3D story landmark (“Kansas From Above”).  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
