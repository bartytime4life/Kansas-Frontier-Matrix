# DEM COGs — Kansas Geo Timeline

Cloud-Optimized GeoTIFFs (COGs) for **Digital Elevation Models** used across the
Kansas Frontier Matrix / Kansas Geo Timeline stack.  
These rasters power terrain visualizations (hillshade, slope, aspect), time-aware overlays,
and downstream analysis in the web app and KML/Google Earth.

---

## Directory layout

```

data/cogs/dem/
├── ks_1m_dem_2018_2020.tif         # statewide mosaic (COG)
├── ks_1m_dem_2018_2020.tif.sha256  # checksum (GNU format)
└── README.md

```

> Project-wide metadata lives in **STAC items** under `stac/items/**` (source of truth).
> A local `.meta.json` is optional if you need non-STAC notes.

---

## Conventions

- **COG layout:** internal tiles **512×512**, internal overviews to ~512 px min dimension.
- **CRS (web copy):** **EPSG:4326** (WGS84).  
  Prefer a **projected CRS** for analysis (e.g., UTM 14N: EPSG:26914 / EPSG:6344).
- **NoData:** set to a safe value (e.g., `-9999`) and document in STAC.
- **Compression:** `DEFLATE` with `PREDICTOR=2` for continuous rasters.
- **Integrity:** every `.tif` has a `.tif.sha256` sidecar.

**Naming**
```

ks_1m_dem_2018_2020.tif         # <region>*<resolution>*<theme>_<temporal>.tif

````
If you publish tiled mosaics, suffix tile keys, e.g. `ks_1m_dem_2018_2020_w98n39.tif`.

---

## Reproducible build

### Option A — Use the project script

```bash
# Convert a prepared DEM to COG (auto reproject to EPSG:4326 if needed)
python scripts/convert.py raster-to-cog \
  data/raw/dem/ks_1m_dem_2018_2020.tif \
  data/cogs/dem/ks_1m_dem_2018_2020.tif
````

This writes the COG **and** `ks_1m_dem_2018_2020.tif.sha256`.

### Option B — Canonical GDAL flow

```bash
# 1) Build VRT from source tiles
gdalbuildvrt dem.vrt data/raw/dem/*.tif

# 2) Reproject to working CRS (UTM 14N example) and set NoData
gdalwarp -t_srs EPSG:26914 -r bilinear -dstnodata -9999 -multi -wo NUM_THREADS=ALL_CPUS \
  dem.vrt dem_utm14.tif

# 3) Create web copy as COG (WGS84)
gdalwarp -t_srs EPSG:4326 -r bilinear -dstnodata -9999 \
  dem_utm14.tif /tmp/dem_wgs84.tif

gdal_translate -of COG \
  -co COMPRESS=DEFLATE -co PREDICTOR=2 \
  -co BLOCKSIZE=512 \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  -co OVERVIEW_RESAMPLING=AVERAGE \
  /tmp/dem_wgs84.tif data/cogs/dem/ks_1m_dem_2018_2020.tif

# 4) Checksum
sha256sum data/cogs/dem/ks_1m_dem_2018_2020.tif \
  > data/cogs/dem/ks_1m_dem_2018_2020.tif.sha256
```

---

## Derivatives (terrain products)

Generate from your **working CRS** (projected), then COG-ify if publishing:

```bash
# Hillshade (common azimuth/altitude)
gdaldem hillshade -az 315 -alt 45 -compute_edges dem_utm14.tif hillshade.tif
# Optional softer light:
# gdaldem hillshade -multidirectional -compute_edges dem_utm14.tif hillshade.tif

# Slope / Aspect
gdaldem slope  dem_utm14.tif slope.tif  -s 1.0
gdaldem aspect dem_utm14.tif aspect.tif

# Convert to COGs (lossless)
gdal_translate -of COG -co COMPRESS=DEFLATE -co PREDICTOR=2 -co OVERVIEW_RESAMPLING=AVERAGE \
  hillshade.tif data/cogs/hillshade/ks_hillshade_2018_2020.tif
gdal_translate -of COG -co COMPRESS=DEFLATE -co PREDICTOR=2 -co OVERVIEW_RESAMPLING=AVERAGE \
  slope.tif     data/cogs/dem/ks_slope_2018_2020.tif
gdal_translate -of COG -co COMPRESS=DEFLATE -co PREDICTOR=2 -co OVERVIEW_RESAMPLING=AVERAGE \
  aspect.tif    data/cogs/dem/ks_aspect_2018_2020.tif
```

> Remember to emit checksums and STAC items for each published derivative.

---

## STAC registration

Create a STAC Item for each COG to record:

* `datetime` / `start_datetime`–`end_datetime`
* `proj:*` (EPSG, transform, shape), `raster:*` (bands, nodata), `file:*` (size), `checksum:sha256`
* `processing` notes (warp, resampling, compression)
* Providers + license

**Fast path (Python API):**

```python
from kansas_geo_timeline.ingest import ingest_raster
out, item = ingest_raster(
    "data/cogs/dem/ks_1m_dem_2018_2020.tif",
    stac_items_dir="stac/items",
    stac_collection="kfm-dem"
)
print(out, item["id"])
```

**CLI (Make):**

```bash
make stac stac-validate-items
```

---

## Web & Earth integration

**Web (MapLibre):** reference the DEM for terrain (if your viewer supports raster-dem) or use hillshade as a raster layer.

```json
{
  "id": "ks_1m_dem_2018_2020",
  "title": "DEM (1 m, 2018–2020)",
  "type": "raster-dem",
  "data": "data/cogs/dem/ks_1m_dem_2018_2020.tif",
  "maxzoom": 14,
  "attribution": "USGS 3DEP / Kansas DASC (Public Domain)"
}
```

**Google Earth / KML:** for very large areas, export regionated KML/KMZ; keep DEM in projected CRS for analysis, publish a WGS84 copy for visualization.

---

## Validation & QA

```bash
# Verify checksums
find data/cogs/dem -name "*.tif.sha256" -print0 | xargs -0 -I{} sha256sum -c {}

# Quick gdalinfo checks
gdalinfo -checksum data/cogs/dem/ks_1m_dem_2018_2020.tif | head -n 40

# Optional (rio-cogeo)
rio cogeo validate data/cogs/dem/ks_1m_dem_2018_2020.tif
```

Document in STAC (and optional `.meta.json`):

* Resolution, transform, vertical units/datum
* Resampling used in warps/overviews
* NoData handling and any void fill
* Estimated georeferencing accuracy (RMS or equivalent)

---

## Performance tips

* Prefer **BLOCKSIZE=512** and internal overviews for snappy UX.
* If clients struggle with a statewide monolith, publish **tiled COGs** (quad key or county).
* Keep heavy analysis in **projected CRS**; publish additional web copies in **EPSG:4326** as needed (each with its own STAC).
* For viewer efficiency, consider tiler/PMTiles for public delivery; keep raw COGs for provenance.

---

## Checklist (new DEM)

1. Build/warp DEM to working CRS; set **NoData**.
2. Produce **web copy** as **COG (EPSG:4326)**.
3. Write **`.tif.sha256`** sidecar.
4. Emit **STAC Item** (`stac/items/**`) and validate.
5. (Optional) Generate derivatives (hillshade, slope, aspect) → COG + STAC.
6. Wire into the **web viewer** (raster-dem or hillshade layer).
7. Run **validation** (`sha256sum -c`, `gdalinfo`, optional `rio cogeo validate`).
8. Commit; CI validates and publishes.

---

✅ **Mission-grade principle:** DEM COGs must be **fast, verifiable, and fully traceable**
via STAC. If it doesn’t validate or display, **fix the metadata** (or STAC) first, then the data.

```
```
