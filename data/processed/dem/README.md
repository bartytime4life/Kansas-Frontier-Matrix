<div align="center">

# 🏔️ Kansas-Frontier-Matrix — Processed DEMs  
`data/processed/dem/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Provide **Digital Elevation Model (DEM) derivatives** processed from raw sources  
(USGS 3DEP, LiDAR tiles, Kansas GIS Hub mosaics).  

All outputs are **reproducible** from `data/raw/` via Makefile targets + scripts  
and are registered in the **STAC catalog** (`data/stac/items/dem/*.json`).  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Raw DEM tiles\n(data/raw/dem/**)"] --> B["Mosaic + Reproject\n(gdalwarp → EPSG:4326)"]
  B --> C["COG Conversion\n(rio cogeo / gdal_translate)"]
  C --> D["Processed DEMs\n(data/processed/dem/**)"]
  D --> E["Derivatives\n(slope · aspect · hillshade)"]
  E --> F["Overlays\n(color relief, blends)"]
  D --> G["Checksums + Meta\n(.sha256 · .meta.json)"]
  G --> H["STAC Items\n(data/stac/items/dem/**)"]
  H --> I["Validate\n(stac-validate)"]
  I --> J["Viewer + KML\n(web configs · data/kml/)"]

<!-- END OF MERMAID -->



⸻

📂 Typical Contents

data/processed/dem/
├── ks_1m_dem_2018.tif             # statewide DEM (2018 mosaic, COG)
├── ks_1m_dem_2020.tif             # statewide DEM (2020 update, COG)
├── ks_1m_dem_2018_hillshade.tif   # hillshade derivative
├── ks_1m_dem_2018_slope.tif       # slope raster
├── ks_1m_dem_2018_aspect.tif      # aspect raster
├── overlays/                      # styled blends (color-relief, tinted hillshades)
└── hillshade_color.tif

	•	DEM rasters → Cloud-Optimized GeoTIFFs (COGs) with overviews
	•	Derivatives → slope, aspect, hillshade, TRI/TPI, roughness
	•	Overlays → styled rasters (color relief, blends) for web & KMZ exports

⸻

🔄 Workflow
	1.	Fetch raw DEMs → data/raw/
	•	Sources: USGS 3DEP, Kansas GIS Hub
	•	Mosaicked into county/statewide extents
	•	Record year, resolution, source CRS

gdalwarp -t_srs EPSG:4326 raw_tiles/*.tif /tmp/ks_1m_dem_2018.tif


	2.	Convert to COG

rio cogeo create /tmp/ks_1m_dem_2018.tif \
  data/processed/dem/ks_1m_dem_2018.tif \
  --overview-level=5 --web-optimized


	3.	Generate derivatives

make terrain          # slope, aspect, hillshade
make slope_classes
make aspect_sectors


	4.	Compute checksums

scripts/gen_sha256.sh data/processed/dem/*.tif


	5.	Update STAC items → data/stac/items/dem/
	•	Fill bbox, datetime, license, checksums
	6.	Validate

make stac-validate
pre-commit run --all-files



⸻

📑 Example STAC Items

DEM Raster (1m statewide mosaic, COG)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_1m_dem_2018",
  "properties": {
    "title": "Kansas DEM (2018, 1m)",
    "description": "Statewide 1m DEM mosaic from USGS 3DEP tiles.",
    "start_datetime": "2018-01-01T00:00:00Z",
    "end_datetime": "2018-12-31T23:59:59Z",
    "proj:epsg": 4326,
    "kfm:method": "Mosaic + COG conversion",
    "kfm:lineage": [
      "data/raw/dem/usgs_3dep_2018/*.tif"
    ],
    "qa:status": "verified"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 36.99],
      [-102.05, 40.00],
      [-94.59, 40.00],
      [-94.59, 36.99],
      [-102.05, 36.99]
    ]]
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../../stac/collections/dem.json"
    }
  ],
  "assets": {
    "cog": {
      "href": "../../../data/processed/dem/ks_1m_dem_2018.tif",
      "title": "Kansas DEM (2018, 1m COG)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data", "raster"]
    }
  }
}

Hillshade Derivative (from 2018 DEM)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_1m_hillshade_2018",
  "properties": {
    "title": "Kansas Hillshade (2018, 1m DEM)",
    "description": "Hillshade generated from the statewide 1m DEM mosaic.",
    "datetime": "2018-06-01T00:00:00Z",
    "proj:epsg": 4326,
    "kfm:method": "GDAL hillshade",
    "kfm:lineage": [
      "data/processed/dem/ks_1m_dem_2018.tif"
    ],
    "qa:status": "provisional"
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../../stac/collections/terrain.json"
    }
  ],
  "assets": {
    "cog": {
      "href": "../../../data/processed/dem/ks_1m_dem_2018_hillshade.tif",
      "title": "Hillshade (2018 DEM, 1m)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data", "raster", "visual"]
    }
  }
}


⸻

🔗 Integration
	•	STAC → Each DEM & derivative documented in data/stac/items/dem/**
	•	Web viewer → Hillshade, slope, aspect wired via web/config/layers.json
	•	KML exports → Styled outputs (hillshade, color-relief) in data/kml/
	•	Experiments → Used in MCP workflows (hydrology, archaeology predictive models, floodplain reconstruction, erosion studies)

⸻

📝 Notes
	•	Store only processed DEMs here — raw tiles remain in data/raw/
	•	Stable naming (ks_1m_dem_<year>.tif) so configs don’t break
	•	Track large rasters with Git LFS or DVC
	•	Always link back to authoritative provenance (USGS, Kansas GIS Hub, KGS surveys) in STAC
	•	If rectified with GCPs, cite under data/gcp/
	•	Follow MCP reproducibility — log every step as an experiment or ETL pipeline action

⸻

📚 See Also
	•	data/raw/ → raw DEM tiles (USGS / DASC)
	•	data/cogs/ → mission-final authoritative COGs
	•	data/processed/dem/overlays/ → styled hillshades & blends
	•	data/processed/dem/vectors/ → contour lines & vectorized terrain
	•	data/stac/items/dem/ → STAC catalog entries
	•	data/kml/ → KMZ super-overlays for Google Earth
	•	experiments/ → MCP logs, configs, notebooks

⸻

✅ Mission Principle

Processed DEMs must be COG-optimized, STAC-registered, and reproducible.
They provide the terrain foundation for analysis, visualization, and historical reconstructions.