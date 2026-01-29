<div align="center">

# 🗻 dem_county_fetch  
**County-based DEM downloader + cache for OpenTopography** 🌎📦

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Geo](https://img.shields.io/badge/Geo-GDAL%20%7C%20Rasterio%20%7C%20GeoPandas-green)
![Data](https://img.shields.io/badge/Data-OpenTopography%20DEM-orange)
![KFM](https://img.shields.io/badge/KFM-Data%20Governance%20%2B%20Provenance-purple)

</div>

---

## ✨ What this folder is

This directory documents the **OpenTopography “fetch a DEM for a county” workflow** used by KFM. The big idea:

- **Don’t store every high-res DEM tile** (too large 🧱).
- **Fetch elevation on-demand** from OpenTopography (by county bbox/geometry).
- **Optionally derive** hillshade/contours for visualization 🗺️
- **Cache locally** to avoid repeated downloads and respect API limits ♻️
- **Record provenance** so results are auditable ✅

> 🧠 In KFM terms: this is part of the *external data integration layer* that can be used by pipelines **and/or** an API microservice.

---

## 🧭 Where this fits in the repo

📁 You are here:

```text
📁 data/
└─ 📁 external/
   └─ 📁 mappings/
      └─ 📦 local/                               🏛️ local/partner/API-driven mappings
         └─ 📁 opentopography/                    🗻 OpenTopography workflows + caching
            └─ 📁 dem_county_fetch/               🧭 county DEM fetch package
               ├─ 📄 README.md                    ✅ you are here (runbook + usage)
               ├─ 📁 cache/                       ♻️ recommended (local-only): cached DEM tiles/rasters (gitignored)
               ├─ 📁 logs/                        🧾 recommended (local-only): run logs + manifests (gitignored)
               └─ 📁 tmp/                         🧪 recommended (local-only): scratch space (gitignored)
```

### ✅ What should be committed vs not committed

- ✅ Commit: this README + any lightweight helper scripts/config templates.
- 🚫 Do **not** commit: API keys, large GeoTIFFs, or bulky caches (use `.gitignore`, Git LFS, or promote only curated outputs).

---

## 🎯 Outputs (conceptual contract)

This fetcher workflow generally produces:

### 1) Local cache outputs (developer machine) ♻️
Stored under something like:

```text
data/external/mappings/local/opentopography/dem_county_fetch/cache/
  └─ <dem_type>_<south>_<west>_<north>_<east>.tif
```

### 2) “Promoted” KFM processed outputs (curated + tracked) ✅
When the DEM is considered stable/important enough for KFM to treat as a processed dataset, promote it to:

```text
data/processed/elevation/
  ├─ county_<STATE>_<COUNTY>_<DEM_TYPE>.tif
  ├─ county_<STATE>_<COUNTY>_<DEM_TYPE>_hillshade.tif        (optional)
  └─ county_<STATE>_<COUNTY>_<DEM_TYPE>_contours.geojson     (optional)
```

…and create the required metadata + provenance:

```text
data/catalog/
  ├─ county_<STATE>_<COUNTY>_<DEM_TYPE>.stac.json
  └─ county_<STATE>_<COUNTY>_<DEM_TYPE>.dcat.ttl             (or jsonld)
data/provenance/
  └─ county_<STATE>_<COUNTY>_<DEM_TYPE>.prov.json
```

> 📌 KFM principle: **processed data must be traceable** (catalog + provenance) and code-generated (no hand-editing of processed artifacts).

---

## 🔑 OpenTopography API key

OpenTopography requires an API key for many datasets.

### Recommended (local dev)
Set an environment variable:

```bash
export OPENTOPOGRAPHY_API_KEY="YOUR_KEY_HERE"
```

✅ Alternatives sometimes supported by clients:
- `~/.opentopography.txt` (a file containing your key)
- passing the key explicitly to the fetcher command/function

> ⚠️ Never commit keys. Never embed keys in a public app. Treat them like passwords.

---

## 🌐 OpenTopography request pattern (reference)

OpenTopography’s REST API commonly supports bbox-based requests.

### Global Datasets API (`globaldem`)
Example URL shape:

```text
https://portal.opentopography.org/API/globaldem?demtype=SRTMGL3&south=39.93&north=40.0&west=-105.33&east=-105.26&outputFormat=GTiff&API_Key=YOUR_KEY
```

### USGS 3DEP Raster API (`usgsdem`)
Example URL shape:

```text
https://portal.opentopography.org/API/usgsdem?datasetName=USGS10m&south=39.93&north=40.0&west=-105.33&east=-105.26&outputFormat=GTiff&API_Key=YOUR_KEY
```

**Common parameters:**
- `south`, `north`, `west`, `east` → bbox in lat/long (WGS84)
- dataset selector:
  - `demtype=<...>` for `globaldem`
  - `datasetName=<...>` for `usgsdem`
- `outputFormat=GTiff` (GeoTIFF is the usual default)
- `API_Key=<...>`

---

## 🗃️ Supported DEM dataset names (typical)

You can usually request one of these by name (depending on endpoint):

### Global datasets (examples)
- `SRTMGL1` (30m)  
- `SRTMGL3` (90m)  
- `AW3D30` (30m ALOS World 3D)  
- `NASADEM`  
- `COP30`, `COP90`  
- plus additional bathymetry/topography products

### USGS 3DEP datasets (examples)
- `USGS30m`
- `USGS10m`
- `USGS1m` (often restricted)

> 🧪 Always confirm the latest dataset names + licensing in OpenTopography docs before locking them into metadata.

---

## 🏃 Quickstart workflow (developer)

### 1) Ensure dependencies 🧰
You’ll typically need:
- Python (3.10+ recommended)
- GDAL utilities (`gdalwarp`, `gdal_translate`, `gdaldem`, `gdal_contour`)  
- Python geospatial stack (often):
  - `requests`
  - `geopandas`
  - `shapely`
  - `rasterio`
  - `pyproj`

> ✅ If you’re running via Docker, prefer the project’s GIS-ready image (so GDAL versions are consistent).

### 2) Provide a county geometry 🧩
You need one of:
- county polygon (GeoJSON / GeoPackage / Shapefile), or
- county bbox derived from a trusted county boundary dataset.

**Best practice:** compute bbox from the polygon, but **clip** the final DEM to the polygon boundary (so you don’t keep extra pixels around the county).

### 3) Fetch + cache ♻️
Your fetcher should:
1. Read county geometry → compute bbox (south/north/west/east)
2. Build OpenTopography URL
3. Download GeoTIFF → write to local cache
4. Optionally create derived rasters (hillshade) or vector products (contours)

### 4) Promote to `data/processed/` ✅ (when needed)
When you want the dataset to become part of KFM:
- move/copy the “final” DEM into `data/processed/elevation/`
- generate:
  - STAC item JSON in `data/catalog/`
  - provenance PROV JSON in `data/provenance/`
- (optional) add to Git LFS if too large

---

## 🧾 Provenance + metadata contract (KFM-style)

When promoting a DEM to KFM-processed data, include:

### ✅ STAC/DCAT metadata (`data/catalog/`)
Minimum practical fields:
- title + description
- bbox / geometry
- date/time (fetch date) and/or coverage info
- license + attribution/citation
- provider (OpenTopography + original dataset source)
- links:
  - to the data file
  - to the provenance file

### ✅ W3C PROV-style provenance (`data/provenance/`)
Capture:
- **Entities**: county geometry source + downloaded DEM file
- **Activity**: the fetch operation (script name/version + parameters + timestamp)
- **Agent**: who/what ran it (developer, CI runner, service)

> 🔍 The goal is: someone can answer “how was this produced?” without guessing.

---

## ♻️ Caching strategy (recommended)

To keep caching deterministic and safe:

- Cache key should include:
  - `dem_type` / `datasetName`
  - bbox
  - output format
  - any buffer distance
  - any clip geometry hash (if clipping)
- Store a **sidecar JSON** next to cached outputs:

```text
cache/
  ├─ SRTMGL1_..._.tif
  └─ SRTMGL1_..._.tif.meta.json
```

Example `*.meta.json` fields:
```json
{
  "provider": "OpenTopography",
  "endpoint": "globaldem",
  "dem_type": "SRTMGL1",
  "bbox": {"south": 38.8, "north": 39.2, "west": -95.5, "east": -95.0},
  "outputFormat": "GTiff",
  "fetched_at": "2026-01-29T00:00:00Z",
  "http_status": 200
}
```

---

## 🧯 Troubleshooting

### 401 Unauthorized 🔒
- Missing/invalid API key
- Rate limit reached
- Dataset requires special access

✅ Fix:
- check `OPENTOPOGRAPHY_API_KEY`
- verify key isn’t expired
- reduce repeated calls (use cache)

### Request too large 📏
OpenTopography imposes area limits per dataset/resolution.

✅ Fix:
- request a lower-res DEM (e.g., 90m instead of 30m)
- tile the request (split bbox)
- clip to county polygon after download

### Hillshade looks “wrong” 🌒
Hillshade depends on projection/units.

✅ Fix:
- reproject to a suitable projected CRS (e.g., UTM) before computing slope/hillshade
- ensure elevation units match horizontal units

---

## ✅ “Promotion” checklist (copy/paste)

- [ ] County geometry source is documented (and reproducible)
- [ ] DEM request parameters recorded (dem type, bbox, output format, date)
- [ ] Output DEM validated (CRS, nodata, pixel size)
- [ ] Optional derivatives generated (hillshade/contours) and validated
- [ ] `data/catalog/` updated (STAC/DCAT)
- [ ] `data/provenance/` written (PROV)
- [ ] No API keys or secrets committed 🔒
- [ ] Large binaries handled correctly (Git LFS or external artifact policy)
- [ ] CI checks pass ✅

---

## 🔗 References (official + handy)

- OpenTopography Developers/API page  
- OpenTopography API documentation (Swagger / OpenAPI)  
- OpenTopography Raster dataset pages (for dataset-specific license + notes)  

> Tip: If you’re implementing the fetcher in Python, consider using an existing OpenTopography client library (or replicating its URL-building + caching patterns) to reduce bugs.

---

