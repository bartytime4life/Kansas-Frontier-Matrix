# 🧩 Vector Samples (Web UI)

![format](https://img.shields.io/badge/format-GeoJSON-blue)
![crs](https://img.shields.io/badge/CRS-EPSG%3A4326-brightgreen)
![scope](https://img.shields.io/badge/scope-web%20samples-lightgrey)
![purpose](https://img.shields.io/badge/purpose-demos%20%7C%20tests%20%7C%20prototyping-6f42c1)

📌 **Folder:** `web/assets/samples/vector/`  
These are **small, browser-friendly vector datasets** used by the KFM web app for:
- 🧪 UI/UX prototyping & story mockups
- ✅ test fixtures (consistent geometry + properties)
- 🎨 style experiments (points/lines/polygons)
- 🧭 “works out of the box” demo layers (offline-friendly)

> [!NOTE]
> **Samples are not authoritative datasets.** They are intentionally **small** and optimized for web loading. Real layers should flow through the KFM data pipeline & contracts.

---

## 📁 Typical contents

```text
📁 web/assets/samples/vector/
├─ 📄 README.md
├─ 🗺️ <name>.geojson
├─ 🧾 <name>.meta.json        (recommended sidecar metadata)
└─ 🧱 <name>.topojson         (optional; only if it materially reduces size)
```

---

## ✅ Standards & conventions

### 🌍 Coordinate system (CRS)
- **Use WGS84 / EPSG:4326** (lon, lat) in decimal degrees for anything that hits the browser.
- If your source is **EPSG:3857** (Web Mercator) or any local/state plane CRS, **reproject before committing**.

> [!TIP]
> If your features “teleport” to the ocean or disappear, it’s almost always a CRS mismatch or a `lat/lon` swap.

---

### 🧱 GeoJSON shape
Prefer `FeatureCollection` for everything (even a single feature):

```json
{
  "type": "FeatureCollection",
  "features": [
    { "type": "Feature", "id": "example-001", "properties": {}, "geometry": { "type": "Point", "coordinates": [-96.7, 39.0] } }
  ]
}
```

**Recommended properties** (keep it minimal, but provenance-aware):
- `id` (stable string) ✅
- `name` (human label) ✅
- `source` (short citation / source name) ✅
- `license` (SPDX id or plain text) ✅
- `year` / `date` / `time_range` (when temporal) ⏳
- `tags` (optional) 🏷️

> [!WARNING]
> Avoid deep/nested `properties` trees. Keep samples simple so they’re easy to inspect, search, and style.

---

### 🏷️ Naming convention
Use descriptive, sortable filenames:

`<theme>__<geom>__<time>__<area>.geojson`

Examples:
- `counties__polygons__modern__kansas.geojson`
- `railroads__lines__1880-1920__kansas.geojson`
- `towns__points__1900__northeast-kansas.geojson`

---

## 🧾 Sidecar metadata (recommended)

Even for samples, add a small metadata file next to the GeoJSON:

`<name>.meta.json`

This keeps the UI honest and makes it easy to display “the map behind the map” 🪞.

```jsonc
{
  "id": "railroads__lines__1880-1920__kansas",
  "title": "Railroads (1880–1920) — Kansas (sample)",
  "description": "Small demo layer for styling and timeline prototypes.",
  "format": "GeoJSON",
  "crs": "EPSG:4326",

  "source": {
    "name": "Kansas Historical Society (example)",
    "url": "https://example.org/dataset",
    "retrieved": "YYYY-MM-DD"
  },

  "license": "CC-BY-4.0",
  "extent": {
    "spatial": { "bbox": [-102.05, 36.99, -94.59, 40.00] },
    "temporal": { "start": "1880-01-01", "end": "1920-12-31" }
  },

  "processing": [
    "Clipped to Kansas boundary",
    "Simplified for web rendering",
    "Reprojected to EPSG:4326",
    "Exported to GeoJSON FeatureCollection"
  ],

  "notes": [
    "Not authoritative. Use pipeline outputs for analysis-grade data."
  ]
}
```

---

## 🧰 How the web app should load these samples

### Option A — Fetch from public assets (recommended)
```ts
const url = "/assets/samples/vector/railroads__lines__1880-1920__kansas.geojson";
const geojson = await fetch(url).then(r => r.json());
```

### Option B — Import as a module (only if bundler supports it)
```ts
import railroads from "./railroads__lines__1880-1920__kansas.geojson";
```

> [!TIP]
> Prefer `fetch()` for samples in `web/assets/…` so they behave like real runtime-loaded layers.

---

## 🧪 Creating a new sample (workflow)

1) 🔎 Pick a public/redistributable source (or generate synthetic data).  
2) ✂️ Clip to a small area (county/region) and/or downsample features.  
3) 🧽 Simplify geometry (reduce vertices) to keep it fast in-browser.  
4) 🌍 Reproject to **EPSG:4326**.  
5) ✅ Validate (JSON + GeoJSON sanity).  
6) 🧾 Add `<name>.meta.json` with **source + license + processing** notes.

---

## 🧱 Example: Export GeoJSON from PostGIS (WGS84)

If you’re generating a sample from PostGIS, the key idea is: **transform to 4326, then export as GeoJSON**.

```sql
SELECT
  id,
  name,
  ST_AsGeoJSON(ST_Transform(geom, 4326)) AS geom_geojson
FROM your_table;
```

Then wrap it into a FeatureCollection in your script (Node or Python) and write it to:
`web/assets/samples/vector/<name>.geojson`

---

## ✅ Validation checklist

| Check | Why it matters |
|------:|----------------|
| JSON parses | prevents runtime crashes 💥 |
| `type: FeatureCollection` | consistent loader expectations 🧩 |
| EPSG:4326 lon/lat | correct placement in web maps 🗺️ |
| small file size | fast dev loops & CI ✅ |
| license + source present | provenance-first culture 🧾 |

Quick local checks:
- `python -m json.tool yourfile.geojson` ✅
- Drag & drop into a viewer (QGIS / geojson.io) 👀

---

## 🚫 Common pitfalls

- **Looks “shifted” or wrong location** → coordinates are in **3857** (meters) but treated as **4326** (degrees)
- **Layer loads but nothing visible** → geometry outside expected bounds, invalid rings, or empty features
- **Sluggish UI** → too many vertices; simplify or move to vector tiles

> [!WARNING]
> If a sample grows beyond “small”, don’t ship it as GeoJSON. Consider vector tiles (MVT) or another pipeline-backed format.

---

## 🔐 Data safety rules (non-negotiable)
- 🚫 No secrets, keys, tokens, internal URLs
- 🚫 No PII (emails, phone numbers, exact home addresses)
- ✅ Prefer synthetic/aggregated examples when possible

---

## 🙌 Attribution
Every sample must be attributable:
- Include `license` + `source` in either:
  - `properties` (inside GeoJSON), **and/or**
  - `<name>.meta.json` (preferred)

💡 The goal is that a user can click a feature in the UI and immediately understand: **“what is this, where did it come from, and can I reuse it?”**
