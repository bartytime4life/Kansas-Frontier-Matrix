# 🏔️ Kansas DEM (USGS ~10m) — 3D Terrain Asset

![Data](https://img.shields.io/badge/data-DEM-blue)
![Resolution](https://img.shields.io/badge/resolution-~10m-success)
![Source](https://img.shields.io/badge/source-USGS%203DEP-informational)
![Runtime](https://img.shields.io/badge/runtime-web%2Fassets-orange)

> [!IMPORTANT]
> This directory lives under **`/web/assets`** which is **served as static runtime content** by the frontend build/dev server.  
> Keep *raw downloads / mosaics / big intermediates* out of `/web/assets` whenever possible (store them in `/data`, a pipeline workspace, or a blob store), and only publish the **final, deployable terrain tiles** here.

---

## 🎯 Purpose

This folder hosts the **Kansas statewide terrain surface** used by the **KFM 3D map view** (CesiumJS) as a custom terrain provider.

- ✅ Source: **USGS 3DEP “1/3 arc-second” DEM** (≈ 10 m ground spacing) clipped to Kansas  
- ✅ Runtime output: **Cesium Terrain** (typically **Quantized-Mesh**) so the web client can stream LOD tiles efficiently  
- ♻️ Derivatives (optional): hillshade / slope / contours for 2D/overlay workflows

---

## ⚡ Quick facts

| Item | Value |
|---|---|
| Dataset ID | `kansas_dem_usgs_10m` |
| Type | Raster DEM → 3D terrain tiles |
| Nominal resolution | ~10 meters (1/3 arc-second) |
| Coverage | Kansas (US-KS) |
| Primary consumer | `web` (CesiumJS viewer) |
| Primary output format | Cesium Terrain (Quantized-Mesh) |

---

## 🗂️ What should be in this folder

Below is the **recommended** runtime layout for a Cesium Quantized-Mesh terrain set.

```text
🗂️ web/assets/maps/3d/terrain/kansas_dem_usgs_10m/
├─ 📄 README.md
├─ 🧾 layer.json                      # Cesium terrain manifest (required for quantized-mesh)
├─ 🧾 metadata.contract.json           # KFM dataset contract (required: provenance/traceability)
├─ 🖼️ preview.png                      # Optional thumbnail (nice for layer pickers)
├─ 🗂️ 0/                               # LOD 0 tiles (quantized-mesh)
├─ 🗂️ 1/                               # LOD 1 tiles
├─ 🗂️ 2/                               # ...
├─ 🧾 checksums.sha256                 # Optional: integrity for deploy artifacts
└─ 🗂️ provenance/                      # Optional: STAC/DCAT/PROV projections
   ├─ 🧾 stac.collection.json
   ├─ 🧾 stac.item.json
   ├─ 🧾 dcat.json
   └─ 🧾 prov.json
```

> [!NOTE]
> If you’re serving **3D Tiles Terrain** instead of Quantized-Mesh, the entrypoint and structure differ (e.g., tileset JSON). Keep this folder’s README updated to reflect the chosen terrain format.

---

## 🧩 Using this terrain in the web client (CesiumJS)

### Minimal example (Quantized-Mesh via `layer.json`)

```js
// Example: load terrain from this folder (static hosting)
const terrainUrl = new URL(
  "/assets/maps/3d/terrain/kansas_dem_usgs_10m/",
  window.location.origin
).toString();

const terrainProvider = await Cesium.CesiumTerrainProvider.fromUrl(terrainUrl);

const viewer = new Cesium.Viewer("cesiumContainer", {
  terrainProvider,
});
```

### Serving notes (static hosting)

- Ensure `layer.json` is accessible at:
  - `/assets/maps/3d/terrain/kansas_dem_usgs_10m/layer.json`
- Make sure `.terrain` tile files are served with sensible headers:
  - `Content-Type: application/octet-stream` (safe default)
  - Enable `gzip`/`brotli` if your host supports it (often helps)
- If terrain is hosted on a different domain, configure **CORS**.

---

## 🏗️ Regenerating the terrain tiles (pipeline overview)

> [!TIP]
> Keep the “big stuff” (downloads, mosaics, VRTs, intermediate GeoTIFFs) out of `/web/assets`.  
> Publish only the final tileset output here.

### 1) Acquire source DEM tiles (USGS 3DEP 1/3 arc-second)

- Download the tiles covering Kansas from **The National Map / USGS 3DEP**.
- Prefer the most authoritative distribution path available to your workflow.

### 2) Mosaic + clip to Kansas

Typical steps (illustrative; adapt to your tooling):

```bash
# 1) Build a mosaic VRT from downloaded tiles
gdalbuildvrt ks_3dep_10m.vrt ./downloads/*.tif

# 2) Clip to Kansas boundary (GeoJSON/Shapefile)
gdalwarp \
  -cutline kansas_boundary.geojson \
  -crop_to_cutline \
  -dstnodata -9999 \
  ks_3dep_10m.vrt ks_3dep_10m_clipped.tif

# 3) Convert to Cloud-Optimized GeoTIFF for durable raster storage (optional but recommended)
gdal_translate \
  ks_3dep_10m_clipped.tif ks_3dep_10m_clipped_cog.tif \
  -of COG
```

### 3) Convert DEM raster → Cesium Terrain

Options:
- 🧰 **Local tooling** (e.g., `cesium-terrain-builder` or other quantized-mesh generators)
- ☁️ **Cesium ion** (upload GeoTIFF → get hosted terrain; then mirror/copy if needed)

**Output requirement:** a terrain directory with `layer.json` at the root.

### 4) Publish runtime output into this folder

Copy the generated terrain directory contents into:

`web/assets/maps/3d/terrain/kansas_dem_usgs_10m/`

…and update:
- `metadata.contract.json`
- `checksums.sha256` (if used)
- `preview.png` (optional)

---

## 🧾 Provenance-first: `metadata.contract.json` (required)

KFM uses **contract-first + provenance-first** rules: if the terrain shows up in UI, it must be traceable back to its source + processing history.

### Suggested contract skeleton

```json
{
  "id": "kansas_dem_usgs_10m",
  "title": "Kansas DEM (USGS 3DEP 1/3 arc-second ~10m)",
  "type": "raster-dem",
  "role": ["terrain", "elevation"],
  "coverage": {
    "admin": "US-KS",
    "bbox_wgs84": [-102.0517, 36.9930, -94.5884, 40.0031]
  },
  "resolution": {
    "nominal_meters": 10,
    "note": "1/3 arc-second (approximate ground spacing)"
  },
  "crs": {
    "horizontal": "EPSG:4326",
    "vertical_units": "meters"
  },
  "source": {
    "publisher": "U.S. Geological Survey (USGS)",
    "program": "3D Elevation Program (3DEP)",
    "product": "1/3 arc-second DEM",
    "landing_page": "https://data.usgs.gov/"
  },
  "license": {
    "name": "Public Domain (USGS / The National Map)",
    "attribution": "Data available from U.S. Geological Survey, National Geospatial Program."
  },
  "lineage": {
    "retrieved_at": "YYYY-MM-DD",
    "processing": [
      { "step": "mosaic", "tool": "gdalbuildvrt" },
      { "step": "clip", "tool": "gdalwarp", "cutline": "kansas_boundary.geojson" },
      { "step": "terrain_tiling", "tool": "cesium-terrain-builder", "format": "quantized-mesh" }
    ],
    "build": {
      "git_commit": "abcdef123456",
      "built_at": "YYYY-MM-DD",
      "built_by": "name-or-ci"
    }
  },
  "artifacts": {
    "terrain_root": "web/assets/maps/3d/terrain/kansas_dem_usgs_10m/",
    "entrypoint": "layer.json"
  },
  "integrity": {
    "checksums_file": "checksums.sha256"
  },
  "standards": {
    "stac": "provenance/stac.item.json",
    "dcat": "provenance/dcat.json",
    "prov": "provenance/prov.json"
  }
}
```

> [!WARNING]
> The `bbox_wgs84` above is a **placeholder** for Kansas’ approximate extent.  
> Replace it with the actual bounding box of your clipped output to keep catalogs + loaders honest.

---

## ✅ QA / sanity checks

Before shipping:
- 🧪 Confirm `layer.json` loads (no 404) and tile directories exist
- 🧭 Verify CRS & tiling scheme expectations (TMS vs Slippy Map style)
- 🕳️ Check NoData handling (voids, ocean fill, edge seams)
- 🧊 Inspect spikes/pits (bad resampling / nodata bleeding)
- 🚀 Measure payload sizes and LOD depth (keep the web build reasonable)

---

## 🪪 License & attribution

USGS / The National Map elevation data is typically **public domain**, but attribution is requested.

Use this acknowledgement in UI / docs when this layer is enabled:

> “Data available from U.S. Geological Survey, National Geospatial Program.”

---

## 🧯 Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Terrain stays flat / ellipsoid only | `layer.json` not found | Verify URL + static hosting path |
| 404s on tiles | Missing LOD folders / wrong base URL | Ensure the terrain root URL points at the folder containing `layer.json` |
| “Half the world disappears” / weird tiling | Wrong tiling scheme or bounds | Rebuild tiles with correct scheme; verify `layer.json` settings |
| CORS errors | Different domain hosting | Enable CORS on the terrain host |
| Jagged seams at Kansas border | Clip edge + nodata interpolation | Add buffer during clip; fix nodata and resampling strategy |

---

## 🔗 Upstream references

- USGS 3DEP 1/3 arc-second DEM (≈10 m): USGS Data Catalog
- The National Map licensing / terms of use (public domain + requested attribution)
- Cesium Quantized-Mesh terrain format specification
- CesiumJS `CesiumTerrainProvider` documentation