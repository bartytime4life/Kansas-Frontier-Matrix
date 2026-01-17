<!--
📌 KFM 3D Tileset README (per-tileset)
Path: web/assets/maps/3d/tilesets/<tileset-id>/README.md

✅ Goal: make every 3D layer *traceable, citable, and reproducible* (no “mystery layers”).
-->

# 🧱 3D Tileset — `<tileset-id>`

![3D Tiles](https://img.shields.io/badge/3D%20Tiles-streaming%20geospatial-blue?style=for-the-badge)
![CesiumJS](https://img.shields.io/badge/CesiumJS-ready-black?style=for-the-badge)
![Provenance](https://img.shields.io/badge/Provenance-first-success?style=for-the-badge)
![Contract](https://img.shields.io/badge/Data%20Contract-required-purple?style=for-the-badge)

> [!IMPORTANT]
> In KFM, anything that shows up in the UI (including 3D) must be **traceable to cataloged sources** and have **explicit lineage**. This tileset must ship with metadata + provenance (no unsourced assets).

---

## 🧭 Quick Links
- [What is this?](#-what-is-this)
- [How to load it](#-how-to-load-it)
- [Folder contents](#-folder-contents)
- [Metadata contract](#-metadata-contract)
- [Provenance & processing](#-provenance--processing)
- [QA checklist](#-qa-checklist)
- [Troubleshooting](#-troubleshooting)

---

## 🛰️ What is this?

This folder contains a **Cesium-compatible 3D Tiles tileset** (root `tileset.json`) intended for KFM’s 3D viewer workflows (e.g., terrain, LiDAR point clouds, 3D landmarks, extruded thematic layers).

KFM’s 3D plan is to support **Cesium-friendly formats** like **3D Tiles** (and optionally CZML) for streamed, interactive 3D exploration.

> [!NOTE]
> Even though these assets live under `web/assets/…` (UI delivery), the *source-of-truth* must still follow the canonical KFM pipeline:
>
> `ETL → Catalogs (STAC/DCAT/PROV) → Graph → APIs → UI → Story Nodes → Focus Mode`
>
> Meaning: this folder is the **published artifact**, not the entire story of the data.

---

## 🔗 How to load it

### 🌐 Public URL (when served by the web app)
```text
/assets/maps/3d/tilesets/<tileset-id>/tileset.json
```

### 🧩 CesiumJS snippet (example)
```js
// Example only — adapt to your viewer wrapper / app architecture
const url = "/assets/maps/3d/tilesets/<tileset-id>/tileset.json";

const tileset = await Cesium.Cesium3DTileset.fromUrl(url, {
  maximumScreenSpaceError: 16,
  maximumMemoryUsage: 512
});

viewer.scene.primitives.add(tileset);
await viewer.zoomTo(tileset);
```

### 🧪 Local preview
3D Tiles generally must be served over HTTP (not `file://`).

```bash
# from the repo root (or anywhere above /web)
python -m http.server 8080
# then open:
# http://localhost:8080
```

> [!TIP]
> If you’re seeing CORS or 404s, confirm the tileset URL path matches the hosting base path.

---

## 🗂️ Folder contents

```text
web/assets/maps/3d/tilesets/<tileset-id>/
├── 🧾 README.md              # (this file)
├── 🧩 tileset.json           # REQUIRED: 3D Tiles entrypoint
├── 🏷️ metadata.json          # REQUIRED: KFM “data contract” for this tileset
├── 🖼️ preview.png            # Recommended: thumbnail for catalogs/UI
├── 🧬 provenance/             # REQUIRED (recommended structure)
│   ├── sources.yml           # Source list (URLs, citations, licenses)
│   ├── processing.md         # Human-readable pipeline steps
│   ├── checksums.sha256      # Integrity hashes (tileset.json + key payloads)
│   └── notes.md              # Optional: assumptions, caveats, limitations
└── 📦 tiles/                 # Tile payloads (b3dm/i3dm/pnts/glb/etc) OR flat files
    └── ...
```

> [!WARNING]
> Keep this repo **lean**. If the tileset is large, consider publishing via CDN/object storage and only committing:
> - `tileset.json` (possibly with absolute URLs),  
> - `metadata.json`, `provenance/`, and a `preview.png`.  
>
> (KFM guidance emphasizes derived/published products rather than huge raw archives.)

---

## 🧾 Metadata contract

KFM uses a **contract-first** approach: every dataset must have a metadata JSON “data contract” with **source, license, extent, processing steps, and provenance** before it’s accepted/used.

Create/update:

📄 `metadata.json`

### ✅ Minimum required fields (KFM-aligned)
| Field | Required | Example |
|---|:---:|---|
| `id` | ✅ | `"<tileset-id>"` |
| `title` | ✅ | `"Monument Rocks 3D Model"` |
| `description` | ✅ | `"Photogrammetry-derived mesh tiled as 3D Tiles for web viewing."` |
| `type` | ✅ | `"3d-tiles"` |
| `license` | ✅ | `"CC-BY-4.0"` / `"Public Domain"` / `"Proprietary (not allowed)"` |
| `attribution` | ✅ | `"Kansas Historical Society; USGS; …"` |
| `sources[]` | ✅ | list of original sources + licenses |
| `extent.spatial.bbox` | ✅ | `[[west,south,east,north]]` |
| `extent.temporal` | ✅* | include if historically time-bounded |
| `crs.native` | ✅ | `"EPSG:XXXX"` |
| `crs.served` | ✅ | `"EPSG:4326"` (typical web serving) |
| `processing[]` | ✅ | ordered pipeline steps + tools |
| `quality` | ✅ | validation notes + known limitations |
| `links` | ✅ | download, docs, catalog pointers |

\*Temporal extent is required whenever the dataset represents a time slice, range, or historical reconstruction.

### 🧪 Example `metadata.json` skeleton
```json
{
  "id": "<tileset-id>",
  "title": "<human-friendly title>",
  "type": "3d-tiles",
  "description": "<what this tileset represents and why it exists>",
  "license": "<SPDX or human-readable license>",
  "attribution": "<short attribution line shown in UI tooltips>",
  "sources": [
    {
      "name": "<source org / dataset name>",
      "url": "<source url>",
      "license": "<source license>",
      "retrieved": "YYYY-MM-DD",
      "notes": "<what was extracted/used>"
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [[-180.0, -90.0, 180.0, 90.0]]
    },
    "temporal": {
      "start": "YYYY-MM-DD",
      "end": "YYYY-MM-DD",
      "label": "<optional: '1850 snapshot' / '1931–1939'>"
    }
  },
  "crs": {
    "native": "EPSG:XXXX",
    "served": "EPSG:4326",
    "vertical_datum": "<e.g., NAVD88 / ellipsoidal>",
    "units": "meters"
  },
  "processing": [
    {
      "step": 1,
      "name": "<ingest>",
      "tool": "<tool name + version>",
      "inputs": ["<file or dataset id>"],
      "outputs": ["<file or dataset id>"],
      "params": {}
    },
    {
      "step": 2,
      "name": "<convert to 3D Tiles>",
      "tool": "<tool name + version>",
      "inputs": ["<mesh/point cloud>"],
      "outputs": ["tileset.json", "tiles/"],
      "params": {}
    }
  ],
  "quality": {
    "validation": [
      "<what was validated and how>",
      "<coordinate checks, alignment checks, LOD sanity checks>"
    ],
    "known_issues": [
      "<any caveats users must know>"
    ]
  },
  "links": {
    "tileset": "/assets/maps/3d/tilesets/<tileset-id>/tileset.json",
    "preview": "/assets/maps/3d/tilesets/<tileset-id>/preview.png",
    "provenance": "/assets/maps/3d/tilesets/<tileset-id>/provenance/processing.md"
  },
  "kfm": {
    "catalog": {
      "stac_item": "<path or id>",
      "dcat_dataset": "<path or id>",
      "prov_record": "<path or id>"
    },
    "ui": {
      "layer_group": "<e.g., 3D / Landmarks / Terrain>",
      "default_visible": false
    }
  }
}
```

> [!TIP]
> The UI should be able to show a tooltip like:
> **“<title> (<attribution>)”**
> and a details panel with the full metadata + sources.

---

## 🧬 Provenance & processing

Put provenance artifacts under:

📁 `provenance/`

### ✅ `provenance/sources.yml` (recommended)
Capture source URLs, licenses, access dates, and citation-ready metadata.

```yml
tileset_id: "<tileset-id>"
sources:
  - name: "<source dataset>"
    organization: "<org>"
    url: "<url>"
    license: "<license>"
    retrieved: "YYYY-MM-DD"
    citation: "<citation text or key>"
    notes: "<what we used>"
```

### ✅ `provenance/processing.md` (recommended)
A human-readable pipeline narrative.

Suggested outline:
1. **Source acquisition** (where from, what was downloaded, checksums)
2. **Cleaning/normalization** (CRS alignment, clipping, decimation, denoise)
3. **3D Tiles conversion** (tooling, tiling params, LOD strategy)
4. **Validation** (spatial alignment checks, viewer smoke tests)
5. **Publishing** (CDN path, caching headers, versioning)

### ✅ `provenance/checksums.sha256` (recommended)
Include at least:
- `tileset.json`
- any key root tile payloads
- `metadata.json`

---

## ✅ QA checklist

### 📦 Packaging & correctness
- [ ] `tileset.json` loads in a Cesium 3D Tiles viewer without errors
- [ ] Tile payload paths resolve correctly (no broken relative paths)
- [ ] Bounding volumes look correct (no “world-sized” bounding boxes)
- [ ] Z/vertical placement is correct (no “floating” or “buried” model)

### 🧾 Governance & trust (KFM rules)
- [ ] `metadata.json` exists and is complete (source, license, extent, processing)
- [ ] `provenance/` exists with sources + processing notes
- [ ] Licenses are compatible with publication (no restricted redistribution)
- [ ] No unsourced additions (“mystery layers”)

### 🧭 Spatial sanity
- [ ] Native CRS documented (`crs.native`)
- [ ] Served CRS documented (`crs.served`, typically WGS84)
- [ ] Units + vertical datum documented (meters vs feet, NAVD88 vs ellipsoidal)

### ⚡ Performance
- [ ] Tileset renders smoothly at expected zoom levels
- [ ] LOD transitions are reasonable (no popping that breaks interpretation)
- [ ] File sizes are appropriate for web delivery (consider CDN)

---

## 🧯 Troubleshooting

### “Tileset failed to load” / 404 errors
- Confirm the URL path:
  `/assets/maps/3d/tilesets/<tileset-id>/tileset.json`
- Confirm the server is serving the `web/` directory as expected.

### Everything renders but it’s in the wrong place
- Check CRS assumptions and whether a transform/RTC center is needed.
- Confirm `crs.native` and how conversion handled georeferencing.

### Model is upside down / Z-offset is wrong
- Verify vertical datum, units, and any height offsets applied during conversion.
- Document any offsets in `metadata.json` + `provenance/processing.md`.

---

## 📝 Change log

> Keep it short + meaningful.

- **YYYY-MM-DD** — v1 published (source: …; conversion: …)
- **YYYY-MM-DD** — fixed vertical offset; updated provenance

---

## 👤 Maintainers

- **Owner:** `<name or team>`
- **Contact:** `<email/handle>`
- **Review cadence:** `<monthly / per-release / ad-hoc>`

---

## 📚 Project alignment notes (why this exists)

KFM’s design emphasizes:
- **Contract-first & provenance-first** (metadata + lineage are mandatory)
- **UI transparency** (“the map behind the map” — show sources/credits in-app)
- **Standards-based catalogs** (STAC/DCAT/PROV) feeding APIs and UI

This tileset README is a *local companion* to those governance rules.
