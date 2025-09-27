# Kansas Geo Timeline — Hillshade COGs

This folder contains **hillshade raster COGs** for the  
**Kansas Frontier Matrix / Kansas Geo Timeline** stack.

Hillshade rasters are derived from the **Kansas 1-m bare-earth DEM (2018–2020)** and
published as **Cloud-Optimized GeoTIFFs (COGs)** for fast, range-read streaming in GIS
desktops and the web viewer.

---

## Directory layout

```

data/cogs/hillshade/
├── ks_hillshade_2018_2020.tif         # main COG
├── ks_hillshade_2018_2020.tif.sha256  # checksum (GNU format)
└── README.md

````

> Project-wide, **STAC Items** live under `stac/items/**` and are the source of truth
> for metadata (bbox, media type, checksums, etc.). A separate `.meta.json` here is optional.

---

## Source & processing

- **Source DEM**: Kansas 1-m DEM (2018–2020).
- **Derivation**: `gdaldem hillshade` (defaults below), optionally `-multidirectional` for softer relief.
- **CRS for web**: `EPSG:4326` (WGS84).
- **COG**: Internal tiling (512×512), overviews to ~512 px minimum dimension, DEFLATE compression.
- **Integrity**: Each `.tif` has a matching `.tif.sha256` sidecar.

---

## Reproducible build

### Option A — Makefile targets (recommended)

```bash
# Inside the repo (or inside the project Docker image)
make terrain                 # builds hillshade from DEM
make stac stac-validate      # emits/validates STAC items
````

### Option B — Manual GDAL commands

```bash
# 1) Produce hillshade from an EPSG:4326 DEM
gdaldem hillshade -alt 45 -az 315 -compute_edges \
  data/cogs/dem/ks_1m_dem_2018_2020.tif \
  /tmp/ks_hillshade_2018_2020.tif

# (Optional) softer shading
# gdaldem hillshade -multidirectional -compute_edges ...

# 2) Convert to COG (lossless, web-friendly)
gdal_translate -of COG \
  -co COMPRESS=DEFLATE -co PREDICTOR=2 \
  -co BLOCKSIZE=512 \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  -co OVERVIEW_RESAMPLING=AVERAGE \
  /tmp/ks_hillshade_2018_2020.tif \
  data/cogs/hillshade/ks_hillshade_2018_2020.tif

# 3) Write checksum sidecar
sha256sum data/cogs/hillshade/ks_hillshade_2018_2020.tif \
  > data/cogs/hillshade/ks_hillshade_2018_2020.tif.sha256
```

> If your DEM is not in **EPSG:4326**, reproject first (e.g., `gdalwarp -t_srs EPSG:4326 …`).

---

## Web viewer wiring (MapLibre)

Add/confirm a layer entry (or generate from STAC):

```json
{
  "id": "ks_hillshade_2018_2020",
  "title": "Hillshade (2018–2020)",
  "type": "raster",
  "data": "data/cogs/hillshade/ks_hillshade_2018_2020.tif",
  "category": "terrain",
  "time": { "start": "2018-01-01", "end": "2020-12-31" },
  "opacity": 0.6,
  "visible": false,
  "attribution": "USGS 3DEP / Kansas DASC (Public Domain)"
}
```

> If you serve tiles from a tiler/PMTiles instead of raw COG, point `data` (or `tiles`) to those URLs.

---

## QA / validation

```bash
# Checksum verification
sha256sum -c data/cogs/hillshade/ks_hillshade_2018_2020.tif.sha256

# Quick metadata spot check
gdalinfo -checksum data/cogs/hillshade/ks_hillshade_2018_2020.tif | head -n 40

# Optional: COG structure validation (requires rio-cogeo)
rio cogeo validate data/cogs/hillshade/ks_hillshade_2018_2020.tif
```

---

## Notes

* **Resolution**: 1-m grid (overviews enable smooth display at small scales).
* **Extent**: Statewide Kansas coverage.
* **What hillshade is not**: It’s a terrain visualization; it does not encode vegetation or buildings.
* **Future**: County-level LiDAR hillshades can be integrated as higher-res regional products.

---

✅ Mission-grade principle: Hillshade COGs here must be **fast, verifiable, and
fully traceable** via STAC — suitable for both analysis and web visualization.

```
```
