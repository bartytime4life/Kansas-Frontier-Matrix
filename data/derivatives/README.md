<div align="center">

# 🧭 Kansas-Frontier-Matrix — Derived Geospatial Products (`data/derivatives/`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

**Mission:** Hold **analysis-ready derivatives** computed from canonical COGs (`data/cogs/`)  
and curated inputs (`data/sources/`).  

All outputs must be **reproducible, checksummed, and (preferably) registered as STAC Items**.

</div>

---

## 🔄 Derivative Lifecycle

```mermaid
flowchart LR
  A["COGs + sources\n(data/cogs · data/sources)"] --> B["Derive\n(terrain · hydro · change)"]
  B --> C["Derivatives\n(data/derivatives/**)"]
  C --> D["Checksums\n(.sha256)"]
  C --> E["STAC Items\n(stac/items)"]
  C --> F["Tiles\n(PMTiles / MBTiles)"]
  F --> G["Web Viewer\n(MapLibre)"]
  E --> H["Validate\n(stac-validate)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Layout

data/derivatives/
├─ terrain/     # slope, aspect, TRI, TPI, roughness
├─ hydrology/   # filled DEM, flowdir, flowacc, streams, basins
├─ contours/    # vector contours (GPKG)
├─ change/      # DEMs of Difference (DoD), erosion–deposition
├─ vectors/     # extracted ridges/valleys, geomorph features (GPKG)
├─ tiles/       # PMTiles / MBTiles (raster or vector)
└─ _meta/       # schemas, templates, palettes

Each artifact should include:
	•	🔒 Checksum sidecar → <file>.<ext>.sha256 (GNU format)
	•	🗂 STAC Item → stac/items/** (preferred)
	•	📝 Optional .meta.json → pipeline notes (if not captured in STAC)
	•	🖼 Optional preview → <name>_preview.png (~1–2 MP)

⸻

🏷️ Naming Conventions

<theme>/<region>*<product>[*<params>]_<year-or-range>[_v<semver>].<ext>

Examples
	•	terrain/ks_slope_2018_2020.tif
	•	terrain/ks_aspect_2018_2020.tif
	•	contours/ks_contours_10m_2018_2020.gpkg
	•	hydrology/ks_flowdir_d8_2018_2020.tif
	•	change/ks_dem_DoD_1894_2020.tif
	•	tiles/ks_hillshade_2018_2020.pmtiles

⸻

🔐 Sidecars (Checksums & Meta)

Generate checksum

cd data/derivatives/<subdir> && \
  sha256sum <name>.<ext> > <name>.<ext>.sha256

Verify later

sha256sum -c data/derivatives/<subdir>/<name>.<ext>.sha256

Optional .meta.json (prefer STAC)

{
  "id": "ks_slope_2018_2020",
  "version": "1.0.0",
  "type": "raster-derivative",
  "product": "slope",
  "title": "Kansas Slope (degrees, from 1 m DEM 2018–2020)",
  "derived_from": [
    {
      "id": "ks_1m_dem_2018_2020",
      "path": "data/cogs/dem/ks_1m_dem_2018_2020.tif",
      "sha256": "data/cogs/dem/ks_1m_dem_2018_2020.tif.sha256"
    }
  ],
  "files": {
    "primary": {
      "path": "data/derivatives/terrain/ks_slope_2018_2020.tif",
      "sha256": "data/derivatives/terrain/ks_slope_2018_2020.tif.sha256"
    }
  },
  "processing": {
    "software": { "gdal": "3.6+" },
    "commands": [
      "gdaldem slope -s 1.0 -of GTiff data/cogs/dem/ks_1m_dem_2018_2020.tif /tmp/ks_slope.tif",
      "gdal_translate -of COG -co COMPRESS=DEFLATE -co PREDICTOR=2 /tmp/ks_slope.tif data/derivatives/terrain/ks_slope_2018_2020.tif"
    ],
    "params": { "units": "degree", "scale_z": 1.0 }
  }
}


⸻

🧪 Standard Derivatives & Recipes

See docs/templates/sop.md for detailed workflows.
Common recipes include:
	•	Slope / Aspect → gdaldem slope, gdaldem aspect
	•	TRI / TPI / Roughness → gdaldem
	•	Hydrology → WhiteboxTools (Fill → FlowDir → FlowAcc)
	•	Contours → gdal_contour
	•	DoD → gdalwarp align + gdal_calc.py differencing
	•	Web Tiles → rio-tiler → PMTiles or gdal2tiles → MBTiles

Outputs should be COG when practical, aligned to Kansas CRS: EPSG:26914 (UTM14N) or EPSG:6344.

⸻

🧰 Makefile Snippets

DERIV := data/derivatives

# Ensure subdirs exist
$(DERIV)/%/:
	@mkdir -p $@

# Slope / Aspect from DEM
$(DERIV)/terrain/ks_slope_2018_2020.tif: data/cogs/dem/ks_1m_dem_2018_2020.tif | $(DERIV)/terrain/
	gdaldem slope -s 1.0 $< /tmp/ks_slope.tif
	gdal_translate -of COG -co COMPRESS=DEFLATE -co PREDICTOR=2 /tmp/ks_slope.tif $@

$(DERIV)/terrain/ks_aspect_2018_2020.tif: data/cogs/dem/ks_1m_dem_2018_2020.tif | $(DERIV)/terrain/
	gdaldem aspect $< /tmp/ks_aspect.tif
	gdal_translate -of COG -co COMPRESS=DEFLATE -co PREDICTOR=2 /tmp/ks_aspect.tif $@

# Contours
$(DERIV)/contours/ks_contours_10m_2018_2020.gpkg: data/cogs/dem/ks_1m_dem_2018_2020.tif | $(DERIV)/contours/
	gdal_contour -a elev -i 10.0 $< $@

.PHONY: derivatives-all
derivatives-all: \
  $(DERIV)/terrain/ks_slope_2018_2020.tif \
  $(DERIV)/terrain/ks_aspect_2018_2020.tif \
  $(DERIV)/contours/ks_contours_10m_2018_2020.gpkg


⸻

✅ Validation

STAC Items

make stac-validate-items

Meta JSON sanity check

find data/derivatives -name "*.meta.json" -print0 | \
  xargs -0 -I{} jq -e 'type=="object"' {}

Checksum verification

find data/derivatives -name "*.sha256" -print0 | \
  xargs -0 -I{} sha256sum -c {}


⸻

🔗 Web Viewer Wiring

Add a layer entry in web/config/layers.json:

{
  "id": "ks_slope_2018_2020",
  "title": "Slope (degrees, 2018–2020)",
  "type": "raster",
  "data": "data/derivatives/terrain/ks_slope_2018_2020.tif",
  "category": "terrain",
  "opacity": 0.7,
  "visible": false,
  "attribution": "Derived from USGS 3DEP DEM (Public Domain)"
}

If tiled, use a pmtiles://… URL instead of a raw COG.

⸻

🧭 Tips
	•	Prefer tile size 512 for large rasters (better range reads)
	•	Continuous rasters → DEFLATE + PREDICTOR=2; scanned maps → JPEG/WebP
	•	Hydrology & DoD demand exact grid alignment
	•	Track large artifacts with Git LFS/DVC; commit checksums + STAC JSON only

⸻

✅ Summary

data/derivatives/ = analysis-ready products, reproducible from canonical COGs + sources.
Each derivative must be checksummed, STAC-registered, and documented.

This directory bridges raw inputs and end-user visualizations — keeping Kansas-Frontier-Matrix
mission-grade, auditable, and MCP-compliant.