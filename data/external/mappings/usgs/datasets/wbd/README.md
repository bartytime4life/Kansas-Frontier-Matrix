# 🧭 USGS WBD (Watershed Boundary Dataset) — `wbd`

![USGS](https://img.shields.io/badge/source-USGS%20(The%20National%20Map)-0b3d91?logo=usgs&logoColor=white)
![Data](https://img.shields.io/badge/data-vector%20polygons%20%26%20lines-2ea44f)
![Coverage](https://img.shields.io/badge/coverage-USA%20%2B%20territories-555)
![License](https://img.shields.io/badge/license-public%20domain-3c3c3c)
![Status](https://img.shields.io/badge/status-tracked%20externally-orange)

> [!NOTE]
> This folder is the **external dataset “pointer + playbook”** for WBD.  
> Large binaries (full-US geodatabases/shapefiles) should **not** be committed here—store them in `data/raw/…` (or the project’s artifact store), and commit **manifests, checksums, and metadata**.

---

## 🧩 What is WBD?

The **Watershed Boundary Dataset (WBD)** is the U.S. national standard for **hydrologic unit (HU) boundary** delineations.  
Hydrologic units are organized in a nested hierarchy and identified by **Hydrologic Unit Codes (HUCs)** (2-digit through 16-digit, with nationwide completeness typically through HUC12).

WBD is commonly used for:
- 🗺️ Watershed boundary visualization (cartography & web maps)
- 🌧️ Summarizing other layers by watershed (e.g., precipitation, land cover, hazards)
- 🔗 Joining / indexing into NHD & NHDPlus HR workflows
- 📍 Point-in-polygon lookup: “Which watershed is this location in?”

---

## ⚡ Quick Facts

| Field | Value |
|---|---|
| Provider | USGS (The National Map / National Hydrography) |
| Dataset | Watershed Boundary Dataset (WBD) |
| Geometry | Polygons (HU boundaries) + Lines (WBDLine in services) |
| Hierarchy | HU2, HU4, HU6, HU8, HU10, HU12 (plus optional HU14, HU16 in some areas) |
| Recommended Join Keys | `huc12` / `huc10` / …, `tnmid` |
| Typical Formats | FileGDB, Shapefile; ArcGIS REST (GeoJSON output supported) |
| License | Public Domain (credit requested) |

---

## 🧱 HUC Levels We Care About (Canonical)

> [!TIP]
> In KFM we treat HUC codes as **strings** (preserve leading zeros). Never cast to int.

| Level | Digits | Common name | Typical use |
|---:|---:|---|---|
| HU2 | 2 | Region | National / macro regions |
| HU4 | 4 | Subregion | Regional rollups |
| HU6 | 6 | Basin | Basin-scale summaries |
| HU8 | 8 | Subbasin | Common watershed analytics unit |
| HU10 | 10 | Watershed | Local planning / rollups |
| HU12 | 12 | Subwatershed | Fine-grain watershed indexing |
| HU14 / HU16 | 14 / 16 | Optional | Not nationwide complete |

---

## 🧬 Core Attributes (What to Preserve)

WBD schemas vary slightly by delivery format and HU level, but these fields are commonly present and useful:

| Field | Meaning | Notes |
|---|---|---|
| `huc2` / `huc4` / `huc6` / `huc8` / `huc10` / `huc12` | Hydrologic Unit Code | Use the matching layer level |
| `name` | HU name | Display label |
| `states` | State abbreviations touched / draining into | Useful filter (e.g., Kansas `KS`) |
| `tnmid` | The National Map ID | Stable identifier for feature tracking |
| `metasourceid` | Link to metadata tables | Useful provenance key |
| `loaddate` | Load/effective date | Tracks stewardship updates |
| `areaacres`, `areasqkm` | Area measures | May depend on source projection/derivation |
| `tohuc` | Downstream relationship | Useful for network-like rollups |
| `hutype`, `humod` | Type/modifier | Closed basin, frontal, etc. (coded values) |

---

## 🧠 How KFM Uses WBD

### Primary uses ✅
- 🧭 **Spatial indexing**: point → watershed (HUC12/HUC10)
- 🧱 **Aggregation keys**: summarize events/data by watershed
- 🗺️ **Base overlay**: watershed boundaries and labels (multi-zoom)
- 🔗 **Cross-dataset alignment**: WBD ↔️ NHD / NHDPlus HR

### Non-goals 🚫
- “Regulatory boundary determination” or site-specific compliance decisions  
- Treating WBD as a substitute for engineering-grade hydrology

---

## 🌐 Source of Truth & Access Methods

### Option A — The National Map Downloader (interactive)
Best for manual pulls, inspection, and one-off downloads.

- TNM Downloader: https://apps.nationalmap.gov/downloader/

### Option B — Staged Products (bulk-ish zips)
Useful for reproducible “snapshot” downloads (FileGDB / Shapefile) when you want local files.

- WBD landing page: https://www.usgs.gov/national-hydrography/watershed-boundary-dataset  
- “Access National Hydrography Products”: https://www.usgs.gov/national-hydrography/access-national-hydrography-products

### Option C — Web Services (programmatic)
Best for automation, small-to-medium geographic subsets, and “latest” boundaries.

- ArcGIS REST (MapServer): https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer  
- Example layer (HUC12): https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer/6

> [!WARNING]
> ArcGIS REST layers typically enforce a **MaxRecordCount** (pagination required).  
> Always implement paging + caching + retries.

---

## 🗂️ Repo Layout & Where Files Should Live

This README lives here:

📁 `data/external/mappings/usgs/datasets/wbd/`

Recommended companion structure (add folders/files as needed):

```text
data/
  external/
    mappings/
      usgs/
        datasets/
          wbd/
            README.md              👈 you are here
            manifest.json          🧾 (optional) what we fetched, when, how
            checksums.sha256       🔒 (optional) hashes for raw artifacts
            notes/                 🗒️ stewardship notes, quirks, issue links
  raw/
    mappings/
      usgs/
        wbd/
          YYYY-MM-DD/             📦 immutable download snapshot (zips/unpacked)
  work/
    mappings/
      usgs/
        wbd/
          ...                     🧪 scratch/intermediate (not for UI/API)
  processed/
    mappings/
      usgs/
        wbd/
          ...                     ✅ curated outputs for DB/API/UI
  catalog/
    ...                           🗺️ STAC/DCAT records (required for “published”)
  provenance/
    ...                           🧬 PROV lineage (required for “published”)
```

---

## 🏗️ Canonical Pipeline (KFM Pattern)

```mermaid
flowchart LR
  A[🌐 USGS WBD Source] --> B[📥 data/raw/.../wbd/<snapshot>/]
  B --> C[🧪 pipeline: import/transform]
  C --> D[✅ data/processed/.../wbd/]
  D --> E[🗺️ data/catalog (STAC/DCAT)]
  D --> F[🧬 data/provenance (PROV)]
  E --> G[(🗃️ PostGIS / Graph)]
  F --> G
  G --> H[⚙️ API]
  H --> I[🖥️ UI]
```

> [!IMPORTANT]
> WBD is “considered live” in KFM only after **Processed + Catalog + Provenance** exist.

---

## 🧰 Recommended Processing Rules

### 1) Preserve raw evidence 🧊
- Never edit raw downloads in-place.
- Keep a per-snapshot folder (date-based or version-based).

### 2) Normalize to KFM-friendly formats 🧼
Recommended “processed” formats:
- GeoPackage (`.gpkg`) for vector archival layers
- GeoParquet for analytics at scale
- GeoJSON / MVT tiles for UI (only after simplification & size budget checks)

### 3) Standardize CRS 📐
- Use **EPSG:4326** for interchange and API defaults (unless a project-wide CRS differs).
- Use an **equal-area** CRS (e.g., NAD83 / Albers Equal Area) for accurate area recomputation.

### 4) Multi-zoom generalization 🪄
For UI overlays:
- Keep a “raw fidelity” layer (no simplification)
- Generate simplified variants (tolerance-by-zoom)
- Ensure topology remains valid (no self-intersections)

---

## ✅ Data Quality Checklist

Minimum checks before publishing processed outputs:

- [ ] **Schema sanity**: expected columns exist (`hucXX`, `name`, `tnmid`, etc.)
- [ ] **HUC format**: string length matches level (2/4/6/8/10/12)
- [ ] **Uniqueness**: HUC codes unique within level
- [ ] **Geometry validity**: no invalid polygons
- [ ] **No accidental reprojection drift**: bounds look correct after transforms
- [ ] **File size budgets** (for UI artifacts): enforce caps per layer/zoom target
- [ ] **Checksums recorded** for raw downloads (sha256) 🔐
- [ ] **STAC/DCAT + PROV updated** 🗺️🧬

---

## 🧪 Example: Programmatic Pull (ArcGIS REST → GeoJSON)

Below is a minimal example showing pagination from the HUC12 service layer.  
(Use caching + backoff in real pipelines.)

```python
import time
import requests

LAYER_URL = "https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer/6/query"

def fetch_all(where: str, out_fields="*", page_size=2000, sleep_s=0.2):
    offset = 0
    features = []
    while True:
        params = {
            "where": where,
            "outFields": out_fields,
            "f": "geojson",
            "resultRecordCount": page_size,
            "resultOffset": offset,
            "returnGeometry": "true",
        }
        r = requests.get(LAYER_URL, params=params, timeout=60)
        r.raise_for_status()
        data = r.json()
        batch = data.get("features", [])
        features.extend(batch)

        if len(batch) < page_size:
            break

        offset += page_size
        time.sleep(sleep_s)

    return {"type": "FeatureCollection", "features": features}

# Example filter: any HU that lists Kansas in its states string (may include cross-border drainage)
fc = fetch_all("states LIKE '%KS%'")
print("features:", len(fc["features"]))
```

> [!TIP]
> Prefer more precise spatial filters when possible (geometry envelope or point-in-polygon),  
> because `states LIKE '%KS%'` is a convenience filter, not a strict “within Kansas” clip.

---

## 🔏 License & Attribution

WBD data from USGS / The National Map is typically **public domain**.  
USGS requests the following acknowledgment statement when citing derived products:

> “Map services and data available from U.S. Geological Survey, National Geospatial Program.”

---

## 📚 References (Authoritative)

- WBD overview (USGS): https://www.usgs.gov/national-hydrography/watershed-boundary-dataset  
- Access & downloads/services: https://www.usgs.gov/national-hydrography/access-national-hydrography-products  
- WBD data dictionary: https://www.usgs.gov/ngp-standards-and-specifications/watershed-boundary-dataset-wbd-data-dictionary  
- ArcGIS REST service directory: https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer

---

## 🧾 Changelog (Local / KFM)

| Date | Change | Notes |
|---|---|---|
| 2026-01-29 | Added dataset README scaffold | Initial doc for WBD external dataset |
| YYYY-MM-DD | _TBD_ | _Add snapshot + checksums + STAC/DCAT/PROV links_ |

