# 🏺🧱 Archaeology 3D Schema Examples (KFM)

![JSON Schema](https://img.shields.io/badge/JSON%20Schema-draft%202020--12-blue?logo=json&logoColor=white)
![3D](https://img.shields.io/badge/3D-glTF%20%7C%203D%20Tiles-5b2cff?logo=cesium&logoColor=white)
![Provenance](https://img.shields.io/badge/Provenance-STAC%20%2B%20DCAT%20%2B%20PROV-0aa?logo=databricks&logoColor=white)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-2ea44f?logo=checkmarx&logoColor=white)
![UI](https://img.shields.io/badge/UI-MapLibre%20%2B%20Cesium-111?logo=react&logoColor=61dafb)

📍 **Folder:** `web/assets/3d/archaeology/schemas/examples/`  
🎯 **Goal:** Provide **golden, validated** example payloads that conform to the archaeology 3D schemas (one folder up: `../`) and demonstrate **how KFM expects 3D archaeology assets to be described, governed, and rendered**.

---

## 🧭 What belongs here?

This folder is the **“living contract”** for archaeology 3D metadata in KFM:

- ✅ **Example JSON documents** that validate against `../*.schema.json`
- ✅ Examples that cover:
  - minimal ✅
  - fully-populated ✅
  - **sensitive / redacted** ✅ (high priority for archaeology)
  - different 3D delivery types (glTF/GLB vs 3D Tiles)
- ✅ Examples designed to power:
  - schema regression tests 🧪
  - front-end demo fixtures 🎬
  - documentation + onboarding 📚

> ⚠️ **Do not** include real sensitive site coordinates or culturally restricted information in examples. Use generalized geometry, fake identifiers, and clearly-marked redaction patterns 🔒

---

## 📁 Suggested layout (relative)

```text
🌐 web/
└── 🧰 assets/
    └── 🧊 3d/
        └── 🏺 archaeology/
            └── 🧾 schemas/
                ├── 🧩 archaeology-3d-asset.schema.json
                ├── 🧱 archaeology-3d-tileset.schema.json
                ├── 🧬 kfm-provenance-ref.schema.json
                ├── 🛡️ kfm-classification.schema.json
                └── 🧪 examples/
                    ├── 📄 README.md                          👈 📍 you are here
                    ├── 📦 artifact3d.min.public.json
                    ├── 📦 artifact3d.full.public.json
                    ├── 🧱 siteScan.3dtiles.full.public.json
                    ├── 🔒 siteScan.3dtiles.redacted.restricted.json
                    └── 🧭 storyStep.with3dAsset.example.json (optional but recommended)
```

If your repo’s schema filenames differ, keep the **intent** consistent and update this README accordingly ✍️

---

## 🧬 Schema philosophy (KFM-aligned)

KFM treats archaeology 3D like **geospatial truth with governance**:

- 🧾 **Evidence-first publishing:** 3D assets should be linkable to the platform’s metadata “evidence triplet” (**STAC + DCAT + PROV**), so nothing is “just a model file” floating without context.
- 🕸️ **Graph-ready semantics:** examples should be shaped so they map cleanly into the knowledge graph (Places, Periods, Events, Activities).
- 🔒 **Sensitivity-first defaults for archaeology:** examples must demonstrate redaction & access control, because site locations and cultural materials often require protection.
- 🗺️🌍 **2D/3D continuity:** examples should support both:
  - 2D map context (MapLibre)  
  - 3D scene viewing (Cesium / 3D Tiles / glTF)

---

## ✅ Validation (recommended patterns)

You can validate examples with **any** JSON Schema validator. Pick what matches your toolchain:

### Option A: AJV (Node)
```bash
# Example (adjust paths as needed):
npx ajv validate \
  -s ../archaeology-3d-asset.schema.json \
  -d ./artifact3d.full.public.json \
  --all-errors
```

### Option B: Python `jsonschema`
```bash
python -m jsonschema \
  --instance ./artifact3d.full.public.json \
  ../archaeology-3d-asset.schema.json
```

### Option C: Policy gates (OPA/Conftest) 🛡️
Even if a file validates against schema, KFM-style governance often adds policy checks such as:
- required license ✅
- sensitivity classification ✅
- prohibited secrets ✅
- redaction rules for restricted datasets ✅

> 💡 Tip: Treat schema validation as “shape correctness” and policy gates as “governance correctness”.

---

## 🧩 Core building blocks (what your examples should demonstrate)

### 1) Stable IDs 🪪
Examples should use stable identifiers (and avoid mutable titles as “IDs”).
- `id`: canonical identifier (string)
- `kind`: what this 3D thing *is* (artifact, site_scan, trench, structure, etc.)
- `links`: references to related things (place, period, event, dataset)

### 2) Spatial + temporal basics 🗺️⏳
Archaeology is inherently 4D (space + time), so examples should model:
- geometry + CRS (serve WGS84 for web viewing)
- spatial precision / uncertainty
- temporal range + uncertainty (even if approximate)

### 3) Assets + rendering hints 🎛️
Examples should show how KFM knows what to render:
- glTF/GLB for discrete objects (artifacts)
- 3D Tiles for big site scans / point clouds / terrain-tied scenes
- optional `viewerHints` for Cesium vs Three.js vs “use default viewer”

### 4) Classification + redaction 🔒
Examples must show:
- `classification.level` (public / sensitive / restricted / confidential)
- what was redacted and why
- how to publish a safe generalized geometry (bbox / centroid + large precision)

### 5) Provenance references 🔗
Examples should include references to:
- STAC Collection / Item IDs (assets)
- DCAT Dataset IDs (catalog)
- PROV Activity IDs (lineage)

---

## 🧪 Example patterns

Below are copy/paste templates. Treat them as **schema-oriented examples** — update fields to match your actual schema names.

---

### 🏺 Example 1 — Minimal Artifact (glTF/GLB) ✅

> 🎯 Use this to test “minimum required fields” and defaulting logic in the UI.

```json
{
  "$schema": "../archaeology-3d-asset.schema.json",
  "id": "kfm:arch3d:artifact:example-0001",
  "kind": "artifact",
  "title": "Projectile Point (Example)",
  "description": "Synthetic example payload for schema validation. No real artifact data.",
  "classification": {
    "level": "public",
    "notes": "Example content only."
  },
  "spatial": {
    "geometry": { "type": "Point", "coordinates": [-96.5, 38.5] },
    "crs": "EPSG:4326",
    "precisionMeters": 50000
  },
  "temporal": {
    "start": "1850-01-01",
    "end": "1860-12-31",
    "uncertaintyYears": 10
  },
  "assets": [
    {
      "role": "model",
      "href": "../../models/artifact-example-0001.glb",
      "mediaType": "model/gltf-binary"
    }
  ],
  "provenance": {
    "dcatDatasetId": "kfm:dcat:dataset:example-archaeology",
    "stacItemId": "kfm:stac:item:artifact-example-0001",
    "provActivityId": "kfm:prov:activity:example-pipeline-run"
  }
}
```

---

### 🧱 Example 2 — Full Artifact (glTF/GLB) 🧾✨

> 🎯 Use this to test richer UI features: popups, attribution panels, download buttons, and “map behind the map”.

```json
{
  "$schema": "../archaeology-3d-asset.schema.json",
  "id": "kfm:arch3d:artifact:example-0002",
  "kind": "artifact",
  "title": "Ceramic Sherd (Example, Full Metadata)",
  "description": "Full example showing links, licensing, uncertainty, and rendering hints.",
  "tags": ["archaeology", "artifact", "ceramic", "example"],
  "classification": {
    "level": "public",
    "care": {
      "authorityToControl": false,
      "notes": "Synthetic example. No Indigenous governance flags asserted."
    }
  },
  "spatial": {
    "geometry": { "type": "Point", "coordinates": [-97.0, 39.2] },
    "crs": "EPSG:4326",
    "precisionMeters": 10000,
    "placeRef": "kfm:place:ks:example-region"
  },
  "temporal": {
    "start": "1800-01-01",
    "end": "1900-12-31",
    "uncertainty": { "startYears": 50, "endYears": 50 },
    "periodRef": "kfm:period:19th-century"
  },
  "assets": [
    {
      "role": "model",
      "href": "../../models/artifact-example-0002.glb",
      "mediaType": "model/gltf-binary",
      "lod": 0,
      "checksum": {
        "algo": "sha256",
        "value": "0000000000000000000000000000000000000000000000000000000000000000"
      }
    },
    {
      "role": "thumbnail",
      "href": "../../thumbnails/artifact-example-0002.jpg",
      "mediaType": "image/jpeg"
    }
  ],
  "viewerHints": {
    "preferredViewer": "threejs",
    "units": "meters",
    "defaultLighting": "studio"
  },
  "links": [
    { "rel": "license", "href": "https://spdx.org/licenses/CC-BY-4.0.html" },
    { "rel": "about", "href": "kfm:dataset:example-archaeology-artifacts" }
  ],
  "provenance": {
    "dcatDatasetId": "kfm:dcat:dataset:example-archaeology-artifacts",
    "stacCollectionId": "kfm:stac:collection:archaeology-artifacts",
    "stacItemId": "kfm:stac:item:artifact-example-0002",
    "provActivityId": "kfm:prov:activity:run-2026-01-25-example"
  }
}
```

---

### 🗺️ Example 3 — Site Scan (3D Tiles) 🌍🧊

> 🎯 Use this when the “3D thing” is **large-scale** (site scan, terrain-tied model, point cloud derivative).

```json
{
  "$schema": "../archaeology-3d-tileset.schema.json",
  "id": "kfm:arch3d:siteScan:example-tileset-0001",
  "kind": "site_scan",
  "title": "Excavation Area Tileset (Example)",
  "description": "Example 3D Tiles tileset reference for Cesium-based rendering.",
  "classification": { "level": "public" },
  "spatial": {
    "geometry": {
      "type": "Polygon",
      "coordinates": [[
        [-97.3, 38.9],
        [-97.1, 38.9],
        [-97.1, 39.1],
        [-97.3, 39.1],
        [-97.3, 38.9]
      ]]
    },
    "crs": "EPSG:4326",
    "precisionMeters": 25000
  },
  "temporal": {
    "start": "2020-01-01",
    "end": "2020-12-31",
    "uncertaintyYears": 0
  },
  "assets": [
    {
      "role": "tileset",
      "href": "../../tilesets/site-scan-example-0001/tileset.json",
      "mediaType": "application/json",
      "render": {
        "engine": "cesium",
        "type": "3d-tiles"
      }
    }
  ],
  "viewerHints": {
    "preferredViewer": "cesium",
    "zoomTo": "bbox",
    "maxScreenSpaceError": 16
  },
  "provenance": {
    "dcatDatasetId": "kfm:dcat:dataset:example-site-scans",
    "stacCollectionId": "kfm:stac:collection:archaeology-site-scans",
    "stacItemId": "kfm:stac:item:siteScan-example-tileset-0001",
    "provActivityId": "kfm:prov:activity:run-2026-01-25-siteScan-example"
  }
}
```

---

### 🔒 Example 4 — Redacted Sensitive Site (Restricted) 🛑

> 🎯 This is the most important archaeology pattern: **publish safely** while preserving utility.

Key idea: store **generalized geometry** and mark it as such. Never publish precise points for restricted sites.

```json
{
  "$schema": "../archaeology-3d-tileset.schema.json",
  "id": "kfm:arch3d:siteScan:example-tileset-REDACTED-0001",
  "kind": "site_scan",
  "title": "Restricted Site Tileset (Example — Redacted)",
  "description": "Example shows how to publish an access-controlled 3D tileset while redacting precise site location.",
  "classification": {
    "level": "restricted",
    "reasons": ["archaeological_site_location"],
    "handling": {
      "geometry": "generalized",
      "requiresRole": ["curator", "authorized_researcher"]
    }
  },
  "spatial": {
    "geometry": {
      "type": "Polygon",
      "coordinates": [[
        [-98.0, 38.0],
        [-96.0, 38.0],
        [-96.0, 40.0],
        [-98.0, 40.0],
        [-98.0, 38.0]
      ]]
    },
    "crs": "EPSG:4326",
    "precisionMeters": 100000,
    "redaction": {
      "method": "bbox",
      "notes": "Bounding polygon is intentionally broad and not the true site footprint."
    }
  },
  "temporal": {
    "start": "1900-01-01",
    "end": "1950-12-31",
    "uncertaintyYears": 25
  },
  "assets": [
    {
      "role": "tileset",
      "href": "oci://ghcr.io/example/kfm/archaeology-site-scan:REDACTED-0001",
      "mediaType": "application/vnd.cesium.3dtiles+json",
      "distribution": {
        "type": "oci",
        "digest": "sha256:1111111111111111111111111111111111111111111111111111111111111111",
        "verify": {
          "cosignRequired": true
        }
      },
      "render": { "engine": "cesium", "type": "3d-tiles" }
    }
  ],
  "viewerHints": {
    "preferredViewer": "cesium",
    "zoomTo": "bbox",
    "showWarningBanner": true
  },
  "provenance": {
    "dcatDatasetId": "kfm:dcat:dataset:restricted-archaeology-sites",
    "stacCollectionId": "kfm:stac:collection:restricted-archaeology-sites",
    "stacItemId": "kfm:stac:item:siteScan-REDACTED-0001",
    "provActivityId": "kfm:prov:activity:run-REDACTED-0001"
  }
}
```

---

## 🧵 Optional: Story integration example (Story Node / Step) 🎬

If your Story engine supports “steps” that point to 3D assets, a tiny example fixture is useful:

```json
{
  "$schema": "../../../story_nodes/story-step.schema.json",
  "id": "kfm:storyStep:archaeology:example-3d-0001",
  "title": "Rotate the Artifact (Example Step)",
  "type": "focus_asset",
  "assetRef": "kfm:arch3d:artifact:example-0002",
  "ui": {
    "panel": "right",
    "allowDownload": false
  },
  "narration": "This is a synthetic story step that focuses a 3D artifact in the viewer."
}
```

---

## 🧯 Common pitfalls (what examples should help prevent)

- ❌ Missing sensitivity classification for archaeology sites  
- ❌ Publishing precise site coordinates for restricted content  
- ❌ Model files with no provenance references (orphan assets)  
- ❌ Unknown CRS / mixed projections  
- ❌ No temporal uncertainty (archaeology often needs it)  
- ❌ No viewer hints for ambiguous assets (glTF vs tileset)

---

## 🛠️ Contributing checklist

When you add or modify a schema, update examples to match:

- [ ] Add **at least 2 examples** per schema: `min` and `full`
- [ ] If the schema touches locations, add a **redacted** example 🔒
- [ ] Validate JSON Schema (AJV/Python)
- [ ] Run policy gates (if enabled) 🛡️
- [ ] Ensure examples are **safe to publish** (no real sensitive data)

---

## 🚀 Roadmap ideas (nice-to-have examples later)

- 🧊 **Point cloud tiles** example (LAZ → 3D Tiles / other streaming form)
- 🛰️ Photogrammetry pipeline manifest example (run manifest + derived assets)
- 🕵️ “Explainability panel” example showing how a 3D asset is cited in Focus Mode
- 📦 Offline “field pack” example for PWA / mobile use (bundle of small 3D assets)

---

### 🧡 Design principle reminder
KFM’s UI is built to surface provenance and context — “the map behind the map.” These examples should make that easy to test and impossible to forget.

