# 🧾 ASSETS — Public Attribution Registry (KFM Web)

![Attribution](https://img.shields.io/badge/attribution-required-2ea44f) ![Provenance](https://img.shields.io/badge/provenance-tracked-blue) ![Compliance](https://img.shields.io/badge/governance-license%20gates-orange)  

> **Why this exists:** If it’s visible in the web app (🗺️ maps, 🧱 tiles, 🛰️ imagery, 🖼️ icons, 🔤 fonts, 📄 documents), it must have **provenance + license + attribution**.  
> **Audience:** the public, contributors, and downstream reusers.  
> **Not legal advice:** this is an operational “what we show + what we ship” registry.

---

## 📁 Location

```text
📁 web/
  📁 public/
    📁 attribution/
      📄 ASSETS.md  👈 you are here
```

---

## 🧠 Quick Start

### ✅ If you add any file under `web/public/**` that is not 100% your own work…
Add a row to the **Static Web Assets** table below.

### ✅ If you add any new *visible* data layer (tiles, GeoJSON overlays, imagery, labels)…
Add a row to **Map & Data Attributions**.

### 🚫 If you’re tempted to screenshot Google Earth / proprietary basemaps…
See **🚫 Restricted / High-Risk Sources**.

---

## 🧾 “Footer Copy” — Default Attribution Snippets

> Use these as the *UI-visible* attribution footer/overlay text (e.g., map corner).  
> Keep it **legible without interaction** (no “tap to reveal” hidden credit).

### 🗺️ Basemap / OSM (if used)
- **Text:** `© OpenStreetMap contributors`
- **Link:** `https://www.openstreetmap.org/copyright`

### 🏛️ Kansas foundational GIS (if used)
- **Text:** `Kansas Data Access and Support Center (DASC)`

### 🌊 Hydrology (if used)
- **Text:** `USGS National Water Information System (NWIS)`

### 🌪️ Climate & hazards (if used)
- **Text:** `NOAA (Storm Events / Climate datasets)`

### 📰 Historical newspapers (if used)
- **Text:** `Library of Congress — Chronicling America`

### 🗃️ Kansas historical archive (if used)
- **Text:** `Kansas Historical Society — Kansas Memory`

> ⚙️ **Rule:** When multiple layers are visible, show combined attribution (stacked or joined with separators).

---

## 🧩 License Legend

- ✅ **OK to ship** (permissive / compatible)  
- ⚠️ **Conditional** (attribution required, share-alike constraints, per-item rights, or limited use)  
- 🚫 **Do not ship / do not reuse** without explicit permission  

---

## 🗺️ Map Renderers (Bundled Client Libraries)

> These are “code assets” we bundle into the web client. Licenses require preservation of notices in distribution.

| Component | Purpose | License | Notes |
|---|---|---:|---|
| **MapLibre GL JS** | 2D interactive maps (vector tiles / GeoJSON overlays) | BSD-3-Clause | Works with custom styles, vector tiles, raster tiles |
| **CesiumJS** | 3D globe / terrain visualization | Apache-2.0 | Beware “default globe” and third-party imagery/terrain sources |

---

## 🧱 Basemap Styles, Sprites, Glyphs (If Vendored)

> If we vend (ship) any of these locally (style JSON, sprite sheets, icon sets, font glyphs), they must be listed here.  
> If they’re fetched remotely at runtime, list them under **Map & Data Attributions** instead.

| Asset ID | Local Path | Type | Source / Upstream | License | Required Credit | Modifications |
|---|---|---|---|---|---|---|
| *(template)* | `web/public/basemaps/<name>/style.json` | Map style | `<url>` | `<license>` | `<credit text>` | `<yes/no + notes>` |
| *(template)* | `web/public/basemaps/<name>/sprite.png` | Sprite | `<url>` | `<license>` | `<credit text>` | `<yes/no + notes>` |
| *(template)* | `web/public/basemaps/<name>/glyphs/*` | Font glyphs | `<url>` | `<license>` | `<credit text>` | `<yes/no + notes>` |

---

## 🖼️ Static Web Assets (Images, Icons, Fonts, UI Media)

> Anything in `web/public/` that ships to browsers belongs here: logos, icons, background images, UI illustrations, videos, PDFs, etc.

| Asset ID | Local Path | Type | Creator / Source | License | Required Credit | Notes |
|---|---|---:|---|---|---|---|
| *(template)* | `web/public/assets/icons/<file>.svg` | Icon | `<name + url>` | `<license>` | `<credit text>` |  |
| *(template)* | `web/public/assets/fonts/<family>/` | Font | `<foundry + url>` | `<license>` | `<credit text>` | Include OFL notices if applicable |
| *(template)* | `web/public/assets/images/<file>.png` | Image | `<name + url>` | `<license>` | `<credit text>` | Keep original metadata if possible |

---

## 📦 Map & Data Attributions (Visible Layers)

> These are datasets the UI displays as layers, overlays, charts, timelines, or story media.  
> The source may be **ingested** into PostGIS/tiles, or **queried live** via API. Either way, attribution applies if it’s visible.

### 🧭 Kansas & Regional Reference Layers
| Source | Typical Content | License Risk | Attribution (UI) | Notes |
|---|---|---:|---|---|
| **Kansas Geospatial Data Portal (DASC)** | boundaries, transportation, land cover, elevation contours, etc. | ✅/⚠️ | `Kansas Data Access and Support Center (DASC)` | Verify per-dataset notes (some may be “attribution requested”) |

### 🌊 Water / Hydrology
| Source | Typical Content | License Risk | Attribution (UI) | Notes |
|---|---|---:|---|---|
| **USGS NWIS** | stream gauges, groundwater levels, water quality | ✅ | `USGS National Water Information System (NWIS)` | U.S. Gov data generally public domain; still cite source clearly |

### 🌪️ Weather, Climate, Drought, Hazards
| Source | Typical Content | License Risk | Attribution (UI) | Notes |
|---|---|---:|---|---|
| **NOAA Storm Events / climate datasets** | tornado/hail/flood events, station climate, drought context | ✅ | `NOAA` | Maintain dataset-version/date where possible |

### 🌾 Agriculture & Land Use (Examples)
| Source | Typical Content | License Risk | Attribution (UI) | Notes |
|---|---|---:|---|---|
| **USDA NASS Cropland Data Layer (CDL)** | annual crop type raster maps | ✅ | `USDA NASS — Cropland Data Layer (CDL)` | Store year + resolution metadata |
| **USDA NASS QuickStats** | county/state ag statistics time series | ✅ | `USDA NASS — QuickStats` | Document query parameters for reproducibility |

### 🛰️ Remote Sensing / Raster Products
| Source | Typical Content | License Risk | Attribution (UI) | Notes |
|---|---|---:|---|---|
| *(template)* | satellite imagery / composites / indices | ✅/⚠️ | `<provider>` | Confirm per-mission license + redistribution rules |
| *(template)* | DEM / terrain / hillshade | ✅/⚠️ | `<provider>` | If derived, document processing chain & source DEM |

---

## 🏛️ Historical Archives & Primary Sources (Visible/Linked Content)

> These are “content assets” that appear as story evidence, citations, or linked media.

| Source | What We Use | License Risk | Attribution (UI / Story) | Notes |
|---|---|---:|---|---|
| **Kansas Memory (Kansas Historical Society)** | photos, diaries, maps, documents (metadata indexed; selective media shown) | ⚠️ | `Kansas Historical Society — Kansas Memory` | Rights may vary per item; store item-level rights text |
| **Chronicling America (Library of Congress)** | newspaper OCR snippets & metadata | ✅/⚠️ | `Library of Congress — Chronicling America` | Confirm scope and copyright status per item |
| **Treaty texts / Indigenous records** | treaty documents linked to geographies | ⚠️ | `Treaty text source (e.g., Avalon Project / US compilations)` | Handle with CARE principles; culturally sensitive governance |
| **Indian Land Cessions (Royce maps)** | polygon shapes of cession areas | ⚠️ | `U.S. Forest Service — Indian Land Cessions (Royce maps)` | Maintain provenance and interpretive context |

---

## 🚫 Restricted / High-Risk Sources (Read Before Using)

### Google Earth / proprietary basemaps & imagery
🚫 **Do not** ship or redistribute screenshots/tiles/imagery from Google Earth or other proprietary basemaps unless we have explicit rights and comply with their publishing/attribution requirements.

**Safer alternatives:** open government orthophotos, mission-provided open satellite data, state GIS portals, or properly licensed commercial imagery with written permission.

---

## 🧪 Generated / Derived Assets

> Many of our “assets” are derived (e.g., hillshade, vector tiles, simplified geometries, stitched rasters).  
> Derivatives must carry **(a)** upstream attribution, **(b)** processing notes, **(c)** a reproducible recipe pointer.

### Required metadata for derived layers
- **Inputs:** dataset IDs + versions + timestamps  
- **Process:** toolchain (GDAL, GeoPandas, etc.), key parameters, projection  
- **Output:** format (PMTiles / MBTiles / GeoJSON / COG), bounding box, resolution  
- **Attribution:** combined attribution of inputs (plus “derived by KFM”)  

---

## 🧷 How to Add a New Asset (Contributor Checklist)

### 1) Add the file
- Put third-party files under a clearly named folder:
  - `web/public/assets/<category>/<vendor>/<asset>`
  - `web/public/basemaps/<style_name>/...`

### 2) Capture provenance
- ✅ Store source URL + author + license name + license text (or SPDX ID)
- ✅ Keep any required `NOTICE` file from upstream

### 3) Update this registry
- Add a row in **Static Web Assets** or **Map & Data Attributions**
- Add the UI footer copy if it needs to appear in the map corner

### 4) Governance gate (must pass)
- No unknown license
- No incompatible share-alike conflicts (when redistributing combined works)
- Indigenous data: apply CARE + platform governance checks

---

## 📬 Takedown / Correction Requests

If you believe an item is misattributed or should not be displayed, open an issue with:
- asset path or dataset name
- reason (license conflict, incorrect credit, rights holder request)
- preferred correction text

---

## 🗓️ Maintenance

- **Update cadence:** whenever assets change (minimum: monthly review)
- **Last reviewed:** `2026-02-04`

---

<details>
<summary>🧱 Optional: Machine-Readable Manifest (future)</summary>

> If we later want the app to render attributions dynamically, create:
> `web/public/attribution/manifest.assets.json`

Example schema:

```json
{
  "assets": [
    {
      "id": "osm-basemap",
      "type": "map-data",
      "source": "OpenStreetMap contributors",
      "license": "ODbL-1.0",
      "attributionText": "© OpenStreetMap contributors",
      "attributionUrl": "https://www.openstreetmap.org/copyright",
      "whereShown": ["map-footer"]
    }
  ]
}
```

</details>