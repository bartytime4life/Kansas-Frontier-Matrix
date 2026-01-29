# 🗺️ OpenTopography DEM County Fetch Notes

![Status](https://img.shields.io/badge/status-draft-yellow)
![Data](https://img.shields.io/badge/output-GeoTIFF%20DEM-blue)
![Derivatives](https://img.shields.io/badge/derivatives-hillshade%20%7C%20contours%20%7C%20slope-lightgrey)
![Cache](https://img.shields.io/badge/cache-data%2Fprocessed%2Felevation-brightgreen)
![Scope](https://img.shields.io/badge/scope-county--level%20AOI-orange)

> 🎯 **Goal:** Fetch **county-scale DEMs** (Digital Elevation Models) from **OpenTopography** for KFM mapping workflows, then **cache locally** so UI/analysis can generate **contours + hillshade** quickly without re-downloading.

---

## 📍 Where this lives (folder context)

```text
📁 data/
└─ 📁 external/
   └─ 📁 mappings/
      └─ 📦 local/                              🏛️ local/partner/API-driven mappings
         └─ 📁 opentopography/                   🗻 OpenTopography workflows + caching
            └─ 📁 dem_county_fetch/              🧭 county DEM fetch package
               ├─ 📝 notes.md                     👈 you are here (inputs, AOI, endpoints, caveats)
               └─ 📦 (future: scripts/config/cache)  ◻️ optional: add as needed
```

---

## 🧠 What “DEM county fetch” means

We treat a **county boundary** (polygon) as the Area of Interest (AOI) and:

1. 🧭 Compute a **bounding box** (south/north/west/east) for that county  
2. 🌍 Call OpenTopography’s API to download a **GeoTIFF DEM** for that bbox  
3. ✂️ (Optional but recommended) **Clip** the DEM to the exact county polygon  
4. 🧱 (Optional) Convert/compress to a storage-friendly format (COG + overviews)  
5. 🗺️ Produce **derived rasters/vectors**: hillshade, slope/aspect, contours  
6. 🧾 Write outputs to the canonical KFM locations + update metadata/provenance

---

## 🏗️ Recommended high-level flow

```mermaid
flowchart TD
  A[🏁 Input: county boundary<br/>GeoJSON/Shapefile/DB geometry] --> B[🧮 Compute bbox<br/>south/north/west/east]
  B --> C{📦 Cache hit?}
  C -- ✅ yes --> D[📤 Return cached DEM + derivatives]
  C -- ❌ no --> E[🌐 Request DEM via OpenTopography API]
  E --> F[💾 Save raw GeoTIFF]
  F --> G[✂️ Clip to county polygon (optional)]
  G --> H[🧭 Reproject to metric CRS for analysis (recommended)]
  H --> I[🌗 Derivatives: hillshade / slope / aspect / contours]
  I --> J[📁 Write to data/processed/elevation]
  J --> K[🧾 Update STAC + provenance logs]
  K --> D
```

---

## 🌍 Picking the right OpenTopography service

OpenTopography supports multiple raster APIs. For county DEMs, the two main “modes” are:

### A) 🌐 Global DEM datasets (GlobalDatasets / `globaldem`)
Use when you want easy access to global DEMs (SRTM, NASADEM, Copernicus, etc.).

**Pros**
- ✅ Simple bbox → GeoTIFF workflow  
- ✅ Great baseline coverage

**Cons**
- ⚠️ Resolution may not match “local LiDAR-grade” needs

### B) 🇺🇸 USGS 3DEP Raster API (US-only)
Use when you want USGS 3DEP DEM products (e.g., 10m / 30m and sometimes 1m depending on access).

**Pros**
- ✅ US-focused, high-quality elevation
- ✅ Better for Kansas workflows when available

**Cons**
- ⚠️ Some products have tighter access rules + request limits

---

## 🔑 API key handling (don’t leak keys 🚫)

- Store keys in **environment variables** (or a secrets manager).
- Never commit keys to git.
- Never embed keys in front-end code.

**Suggested env var**
```bash
export OPENTOPO_API_KEY="...your-key..."
```

---

## 📦 Cache + outputs (recommended conventions)

> 💡 Cache is the whole point: keep requests down, keep the UI fast.

### Primary DEM cache output
- ✅ **Canonical output:** `data/processed/elevation/`
- Example naming (pick one convention and stick to it):
  - `data/processed/elevation/county_<STATEFIPS><COUNTYFIPS>__<demtype>.tif`
  - `data/processed/elevation/<county_slug>__<demtype>.tif`

### Suggested derivatives
- 🌗 Hillshade: `...__hillshade.tif`
- 📐 Slope: `...__slope.tif`
- 🧭 Aspect: `...__aspect.tif`
- 🧵 Contours (vector): `...__contours.gpkg` *(or `.geojson`)*

### Minimal metadata alongside outputs
- `...__meta.json` (or STAC Item JSON)
- `...__prov.json` (provenance record)

---

## 🧭 CRS and accuracy notes (important)

Elevation rasters are often delivered in a geographic CRS (lat/lon). That’s fine for storage and basic display, but:

- 📐 **Slope/aspect/hillshade/contours are best generated in a projected CRS in meters.**
- For Kansas, a practical choice is a suitable **UTM** zone or **State Plane** (depending on your map stack).

**Rule of thumb**
- ✅ Use WGS84 / lat-lon for API queries and indexing  
- ✅ Reproject to a metric CRS for raster analysis/derivatives

---

## 🧪 Implementation checklist (drop-in workflow)

### Inputs
- [ ] County identifier (FIPS or slug)
- [ ] County geometry (polygon)
- [ ] DEM source choice (globaldem vs 3DEP)
- [ ] DEM type (e.g., `NASADEM`, `SRTMGL1`, etc.)

### Fetch
- [ ] Compute bbox from polygon
- [ ] Check cache
- [ ] Call API with retries + backoff (be polite 😇)
- [ ] Validate GeoTIFF (CRS, nodata, pixel size)

### Process
- [ ] (Optional) Clip raster to county polygon
- [ ] Reproject to metric CRS for analysis
- [ ] Create overviews + compression (optional, but recommended)

### Derivatives
- [ ] Hillshade
- [ ] Slope/aspect (optional)
- [ ] Contours (optional)

### Cataloging
- [ ] Write outputs to `data/processed/elevation/`
- [ ] Update `data/catalog/` (STAC) + `data/provenance/` (PROV logs)

---

## 🧰 Example request pattern (bbox → GeoTIFF)

> ⚠️ This is the *shape* of what you’ll send. Keep your real API key in env vars.

```bash
curl -L \
  "https://portal.opentopography.org/API/globaldem?demtype=NASADEM&south=45.196&north=49&west=-122.66&east=-119.95&outputFormat=GTiff&API_Key=${OPENTOPO_API_KEY}" \
  -o "data/processed/elevation/county_demo__NASADEM.tif"
```

---

## 🛠️ Practical tips (so this doesn’t hurt later)

### 🧩 County bbox might be “too big”
Some services impose max-area limits. If a county bbox exceeds allowed limits:
- ✅ Switch to a coarser DEM (e.g., 90m vs 30m)
- ✅ Split the AOI into tiles (grid) and mosaic locally

### 🧱 Prefer COG + compression when sizes grow
- Adds faster reads in map servers / rasterio
- Keeps repo storage saner (especially if not using LFS)

### 🧾 Always log provenance
At minimum:
- dataset/source name
- API params
- timestamp
- clipping/reprojection settings
- output filenames + hashes

---

## 🐛 Troubleshooting quick hits

- **401/403** → API key missing/invalid OR dataset restricted  
- **429** → rate limited (use cache + backoff)  
- **Empty/flat DEM** → bbox wrong, CRS mismatch, or clipped incorrectly  
- **Contours look “wrong”** → generated in lat/lon (reproject to meters first)

---

## ✅ TODOs for this folder

- [ ] Add `fetch_dem_county.py` (CLI: `--county-fips`, `--demtype`, `--force`)
- [ ] Add `config.example.env`
- [ ] Add `cache/` subfolder if we want raw downloads separate from processed outputs
- [ ] Add small smoke tests (1 county, 1 DEM type)
- [ ] Add a STAC template for elevation layers

---

## 📚 References & docs (human-readable links)

- OpenTopography Developers/API page  
- OpenTopography API key notes + example requests  
- OpenTopography swagger/OpenAPI docs  
- GDAL / Rasterio docs for clip/reproject + hillshade/contours

---

