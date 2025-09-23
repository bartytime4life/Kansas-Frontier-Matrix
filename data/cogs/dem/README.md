# DEM COGs — Kansas Geo Timeline

Cloud-Optimized GeoTIFFs (COGs) for **Digital Elevation Models** used across the Kansas-Frontier-Matrix stack.  
These rasters back terrain visualizations (hillshade, slope, aspect), time-aware overlays, and downstream
analysis in the web app and Google Earth/KML [oai_citation:0‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).

---

## Contents

- `ks_1m_dem_2018_2020.tif` — statewide mosaic (1 m) as **COG**
- `ks_1m_dem_2018_2020.meta.json` — acquisition, tiling, CRS, nodata
- `ks_1m_dem_2018_2020.sha256` — integrity & reproducibility
- (Optional) county/tiles COGs if the statewide mosaic is chunked

> The DEM is referenced in the repository’s data plans; add county LiDAR where available to improve
  derivatives in priority areas [oai_citation:1‡Data resource analysis.pdf](file-service://file-GdS9Kcw7Xbfqpy4xwwdqWS).

---

## Naming & Conventions

_.tif
ks_1m_dem_2018_2020.tif

- **COG layout**: internal tiling, overviews, web-friendly compression
- **NODATA**: set to a safe value (e.g., -9999) and documented in `.meta.json`
- **CRS**: analysis in projected CRS; distribute web copies in EPSG:4326/3857 when needed (document in metadata)

---

## Provenance & STAC

Every COG must have a **STAC Item** (`stac/items/*.json`) that records:

- `datetime` / `start_datetime`–`end_datetime`
- `proj:` / `raster:` extensions (grid, nodata, statistics)
- `checksum:sha256`
- source lineage and license

This aligns with the hub’s **contract-first** design; STAC is consumed by the site and the
knowledge graph for time and provenance [oai_citation:2‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).

---

## Quick Generation (GDAL)

> Use a projected working CRS (e.g., UTM 14N) for best local accuracy; reproject for web copies.

```bash
# 1) Build analysis mosaic
gdalbuildvrt dem.vrt ./ingest/*.tif

# 2) Reproject to working CRS (example: EPSG:26914)
gdalwarp -t_srs EPSG:26914 -r bilinear -dstnodata -9999 -multi -wo NUM_THREADS=ALL_CPUS \
  dem.vrt dem_utm14.tif

# 3) Create COG
gdal_translate dem_utm14.tif ks_1m_dem_2018_2020.tif \
  -of COG -co COMPRESS=DEFLATE -co PREDICTOR=2 -co NUM_THREADS=ALL_CPUS \
  -co OVERVIEWS=AUTO -co BIGTIFF=YES

# 4) Checksums
sha256sum ks_1m_dem_2018_2020.tif > ks_1m_dem_2018_2020.sha256

Update ks_1m_dem_2018_2020.meta.json with CRS, resolution, nodata, sources.

⸻

Derivatives

Generate terrain products from the working CRS, then COG:

# Hillshade (multi-directional: generate at several azimuths & merge if desired)
gdaldem hillshade dem_utm14.tif hillshade.tif -az 315 -alt 45 -z 1.0 -s 1.0

# Slope / Aspect
gdaldem slope  dem_utm14.tif slope.tif  -s 1.0
gdaldem aspect dem_utm14.tif aspect.tif

# COG-ify
gdal_translate hillshade.tif hillshade_cog.tif -of COG -co COMPRESS=DEFLATE -co OVERVIEWS=AUTO
gdal_translate slope.tif     slope_cog.tif     -of COG -co COMPRESS=DEFLATE -co OVERVIEWS=AUTO
gdal_translate aspect.tif    aspect_cog.tif    -of COG -co COMPRESS=DEFLATE -co OVERVIEWS=AUTO

Tip: Include hillshade/slope in stac/items/ and wire into the web map config for fast, layered terrain
displays ￼. Higher-res county LiDAR can meaningfully sharpen these derivatives ￼.

⸻

Using in the Web App & Earth
	•	Web (MapLibre): reference the COG via a tile service or static hosting—listed in web/app.config.json.
The time slider and layered overlays use the validated configs produced by templates in src/ ￼.
	•	Google Earth: export regionated KML/KMZ for 3D elevation/overlays (progressive loading) when needed ￼.

⸻

Data Sources & Coverage
	•	Kansas 1-m DEM (state services / USGS endpoints) — baseline for statewide products ￼
	•	County LiDAR (USGS 3DEP / FEMA / KGS) — incorporate where available to densify terrain ￼

Maintain docs/data_sources.md with API endpoints, licenses, and update cadences per design-audit guidance ￼.

⸻

Quality & Uncertainty

Document:
	•	Resolution and resampling used during warp/merge
	•	NODATA handling and void-fill approach
	•	Vertical datum and units
	•	Georeferencing accuracy (RMS or estimated error)—surface in STAC and metadata

Surfacing uncertainty is required across layers to align with the platform’s scientific rigor and design audit
recommendations ￼.

⸻

Performance Tips
	•	Prefer COG with internal overviews (and BLOCKSIZE=512) for snappy map UX.
	•	Split statewide DEM into logical tiles (e.g., 1x1 degree or county) if your hosting or clients struggle with the monolith.
	•	Keep analysis in projected CRS; publish additional web copies in EPSG:4326/3857 as needed, each with its own STAC item.

⸻

Links & References
	•	System architecture (STAC, ingestion, web app, KML) ￼
	•	Data resource analysis (DEM plan, LiDAR opportunities, hydrology/soils endpoints to add) ￼
	•	Design audit (uncertainty, data source documentation, storytelling additions) ￼
	•	Hazard/Climate integration (for future terrain-climate overlays) ￼

Contract-first rule: if a raster fails to display or validate, fix the metadata or STAC—not the template ￼.

