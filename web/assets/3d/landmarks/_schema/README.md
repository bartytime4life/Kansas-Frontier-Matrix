# 🗿 Landmarks (3D) — Schema & Data Contract

![JSON Schema](https://img.shields.io/badge/JSON%20Schema-draft%202020--12-blue)
![Contract-First](https://img.shields.io/badge/Contract--First-✅-success)
![Provenance-First](https://img.shields.io/badge/Provenance--First-🧾-success)
![Cesium 3D Tiles](https://img.shields.io/badge/3D%20Tiles-Cesium-2d6cdf)
![glTF/GLB](https://img.shields.io/badge/3D%20Model-glTF%20%2F%20GLB-orange)

This folder defines the **JSON Schema(s)** that validate **3D Landmark “manifests”** used by the KFM web viewer to place and render landmark models in 2D/3D (MapLibre + Cesium).  
Think of it as a **data contract**: if a landmark shows up in the UI, it must have **structured metadata + provenance + licensing** ✅

---

## ✨ Why this exists (KFM rule: no mystery assets)

KFM is **contract-first** and **provenance-first**:

- Anything that appears in the UI must be traceable to a cataloged source, with provable processing 🧾
- Every asset must ship with metadata describing **source, license, spatial context, and processing steps**
- Unsourced “mystery layers” (or models) are not allowed ❌

This schema enforces those rules **at build/CI time** so we don’t discover problems in production.

---

## 📁 Where this fits in the repo

A typical landmarks layout looks like:

```text
web/
└─ 🌐🧩 assets/
   └─ 🧊 3d/
      └─ 🗿 landmarks/
         ├─ 🧾🗂️ index.json                  # lightweight registry for UI (fast list)
         ├─ 🪨 monument-rocks/
         │  ├─ 🧾🧭 landmark.json             # "manifest" (validated by schema)
         │  ├─ 🧱🧊 model.glb                 # or: model.gltf + textures/
         │  ├─ 🧊🧱 tileset.json              # optional (3D Tiles entrypoint)
         │  └─ 🖼️ thumbnail.webp
         └─ 📐 _schema/
            ├─ 📐🧾 landmark.schema.json
            ├─ 📐🧾 landmarks.index.schema.json
            └─ 📄 README.md                   # ← you are here 📌
```

> [!TIP]
> Keep heavy content (e.g., LiDAR / buildings) in **3D Tiles** and treat `.glb` as the “lightweight hero model” path.

---

## 🧠 Design goals

### ✅ 1) Viewer-friendly
The web app can:
- show a **2D marker** (MapLibre)
- toggle to **3D view** (Cesium) and load either:
  - a **glTF/GLB model**, or
  - a **3D Tiles tileset** (preferred for large/streamed datasets)

### ✅ 2) CRS sanity (WGS84)
All landmark coordinates are expected to be **WGS84 / EPSG:4326** and follow GeoJSON coordinate order:
- `coordinates: [longitude, latitude]` (optional `altitudeMeters` separately)

### ✅ 3) Provenance & licensing are first-class
A landmark without:
- **license**, and
- at least one **source citation**
…should fail validation.

---

## 🧾 Schemas in this folder

> Filenames may evolve, but the intent stays stable.

- **`landmark.schema.json`**  
  Validates a single landmark manifest file, usually:
  `web/assets/3d/landmarks/<slug>/landmark.json`

- **`landmarks.index.schema.json`**  
  Validates the registry/index:
  `web/assets/3d/landmarks/index.json`

---

## 🧱 Landmark Manifest (v1)

### Required fields (minimum viable contract)
A landmark manifest must include:

- `schemaVersion` — semver-ish string (e.g. `"1.0.0"`)
- `id` — stable identifier (do not change once published)
- `slug` — folder-safe identifier (kebab-case)
- `title` — UI label
- `location` — GeoJSON Point in EPSG:4326
- `assets` — at least one renderable asset (GLB/GLTF or 3D Tiles)
- `license` — SPDX string or explicit license text
- `sources[]` — at least one citation/attribution record

---

## 📦 Landmark Manifest fields

| Field | Type | Required | Notes |
|------|------|----------|------|
| `schemaVersion` | string | ✅ | Used to manage schema evolution |
| `id` | string | ✅ | Stable ID (prefer namespaced: `kfm-landmark:<slug>`) |
| `slug` | string | ✅ | Folder name + URL-safe identifier |
| `title` | string | ✅ | Display label |
| `description` | string | ⛔ | Markdown allowed (keep short) |
| `tags` | string[] | ⛔ | e.g. `["geology","historic","tourism"]` |
| `location` | GeoJSON Point | ✅ | `{ "type":"Point", "coordinates":[lon,lat] }` |
| `bbox` | number[4] | ⛔ | `[west,south,east,north]` (EPSG:4326) |
| `placement` | object | ⛔ | How to orient the model (heading/pitch/roll, offsets, scaling) |
| `assets` | object | ✅ | Model/tileset + thumbnails + optional extras |
| `license` | string | ✅ | SPDX recommended (e.g. `CC-BY-4.0`) |
| `attribution` | object | ⛔ | Human-facing credit line(s) |
| `sources` | array | ✅ | Citations: URL/title/publisher/accessed/license |
| `provenance` | object | ⛔ | Processing steps + toolchain details |

---

## 🎮 Assets model (GLB/GLTF vs 3D Tiles)

### `assets.model` (GLB/GLTF)
Use for:
- “hero models”
- small landmarks
- interactive narrative moments

Recommended fields:
- `uri` (relative path, e.g. `"./model.glb"`)
- `mimeType` (e.g. `"model/gltf-binary"`)
- `units` (usually `"meters"`)
- `defaultScale` (number or `[x,y,z]`)

### `assets.tileset` (3D Tiles)
Use for:
- large buildings
- LiDAR point clouds
- streamed city/region content

Recommended fields:
- `uri` (e.g. `"./tileset.json"`)
- `georeferenced` boolean (true if tiles already in world coords)

---

## 🧭 Placement (how we put a model on the map)

Placement is optional but **highly recommended** for GLB/GLTF.

Suggested structure:

- `altitudeMode`: `"clampToGround" | "absolute"`
- `altitudeMeters`: number (only if `absolute`)
- `headingPitchRollDegrees`: `[heading, pitch, roll]`
- `scale`: number or `[x,y,z]`
- `offsetMeters`: `[east, north, up]` (small nudges if needed)

> [!NOTE]
> If you provide a 3D Tiles tileset that’s already georeferenced, placement may be unnecessary.

---

## ✅ Example: `landmark.json`

```json
{
  "schemaVersion": "1.0.0",
  "id": "kfm-landmark:example-landmark",
  "slug": "example-landmark",
  "title": "Example Landmark",
  "description": "Short description for the UI.\n\n- optional bullets\n- optional links",
  "tags": ["kansas", "landmark", "3d"],

  "location": {
    "type": "Point",
    "coordinates": [-99.123456, 38.123456]
  },

  "bbox": [-99.124, 38.122, -99.123, 38.124],

  "placement": {
    "altitudeMode": "clampToGround",
    "headingPitchRollDegrees": [0, 0, 0],
    "scale": 1.0,
    "offsetMeters": [0, 0, 0]
  },

  "assets": {
    "thumbnail": {
      "uri": "./thumbnail.webp",
      "mimeType": "image/webp"
    },
    "model": {
      "uri": "./model.glb",
      "mimeType": "model/gltf-binary",
      "units": "meters",
      "defaultScale": 1.0
    },
    "tileset": {
      "uri": "./tileset.json",
      "georeferenced": true
    }
  },

  "license": "CC-BY-4.0",

  "attribution": {
    "creditLine": "3D model by Example Org. Map visualization by KFM.",
    "contributors": [
      { "name": "Example Org", "role": "model-author" },
      { "name": "KFM", "role": "publisher" }
    ]
  },

  "sources": [
    {
      "title": "Example Source Title",
      "publisher": "Example Publisher",
      "url": "https://example.com/source",
      "license": "CC-BY-4.0",
      "accessed": "2026-01-15"
    }
  ],

  "provenance": {
    "createdBy": {
      "tool": "Blender",
      "notes": "Model cleaned + exported to GLB."
    },
    "processingSteps": [
      { "step": "mesh-cleanup", "notes": "Removed non-manifold edges." },
      { "step": "optimize", "notes": "Reduced poly count for web." }
    ]
  }
}
```

---

## 🗂️ Example: `index.json` (registry)

The index is a **fast list** for UI menus/search results.  
Each entry points to a manifest file for full details.

```json
{
  "schemaVersion": "1.0.0",
  "generatedAt": "2026-01-15T00:00:00Z",
  "landmarks": [
    {
      "id": "kfm-landmark:example-landmark",
      "slug": "example-landmark",
      "title": "Example Landmark",
      "manifestUri": "./example-landmark/landmark.json",
      "location": { "type": "Point", "coordinates": [-99.123456, 38.123456] },
      "tags": ["kansas", "landmark", "3d"]
    }
  ]
}
```

---

## 🧪 Validation (recommended workflow)

### Local validation
Use your favorite JSON Schema validator (Node/JS example):

```bash
# from repo root
npx ajv validate \
  -s web/assets/3d/landmarks/_schema/landmark.schema.json \
  -d web/assets/3d/landmarks/**/landmark.json
```

Validate the index:

```bash
npx ajv validate \
  -s web/assets/3d/landmarks/_schema/landmarks.index.schema.json \
  -d web/assets/3d/landmarks/index.json
```

### CI expectations ✅
CI should fail if:
- a landmark manifest is missing required provenance/licensing fields
- a referenced asset file path doesn’t exist
- coordinates are invalid / not EPSG:4326-style
- index entries point to missing manifests

---

## 🧩 Extensibility rules

To add new fields without breaking old consumers:

- Prefer namespacing experimental fields under `x_`:
  - `x_storyNodeIds`
  - `x_relatedDatasets`
  - `x_recommendedCamera`

- Keep `schemaVersion` stable per “major” schema meaning.
  - Backwards compatible → bump minor/patch
  - Breaking changes → bump major

---

## 🧯 Common pitfalls

- **Lat/Lon swapped** → always `[lon, lat]` 🌍
- **No license** → fail the build (by design) 🧾
- **Absolute altitude without units** → use meters; declare it
- **Huge GLB** → consider 3D Tiles for streaming 🧊

---

## 📌 TODO (nice upgrades)

- Add a small `/examples/` folder with:
  - one GLB landmark
  - one 3D Tiles landmark
- Add a `validate:landmarks` script to package.json
- Add optional `camera` section:
  - `defaultView`: `{ "rangeMeters": 1200, "heading": 0, "pitch": -25 }`

---
