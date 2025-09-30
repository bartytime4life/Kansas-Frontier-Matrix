<div align="center">

# 🗺️ Kansas Geo Timeline — DEM-Derived Vectors

This folder contains **vector products derived from DEMs**.  
They are extracted or modeled from rasters in `../` and `../overlays/`,  
stored as **GeoJSON** for interoperability.  

All vector layers must be:  
- **Reproducible** from DEM inputs (no manual edits).  
- **Linked to provenance** in the STAC catalog (`data/stac/items/dem/*.json`).  
- **Schema-validated** against `web/config/layers.schema.json`.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart TD
  A["Processed DEMs\n(data/processed/dem/**)"] --> B["Generate vectors\n(contours · watersheds · streams)"]
  B --> C["GeoJSON outputs\n(data/processed/dem/vectors/**)"]
  C --> D["Checksums + meta\n(.sha256 · .meta.json)"]
  C --> E["STAC Items\n(data/stac/items/dem/**)"]
  E --> F["Validate\n(stac-validate · schema)"]
  F --> G["Web viewer\n(web/data/dem_vectors.json)"]
  F --> H["Earth exports\n(data/kml/**)"]

<!-- END OF MERMAID -->



⸻

📂 Typical contents

data/processed/dem/vectors/
├── ks_1m_dem_2018_contours_10m.json       # 10 m interval contours
├── ks_1m_dem_2018_watersheds_huc12.json   # watershed polygons
├── ks_1m_dem_2018_stream_network.json     # extracted stream lines
└── ks_1m_dem_2020_contours_5m.json        # alternate contour interval

Common types
	•	Contours → elevation isolines at fixed intervals.
	•	Watersheds / Basins → polygons derived from flow accumulation.
	•	Stream networks → centerlines from flow routing thresholds.
	•	Landform classes → slope/aspect zones, geomorph classes.

⸻

🔄 Workflow
	1.	Source DEM
	•	Must exist as a COG in data/processed/dem/.
	•	Example: ks_1m_dem_2018.tif.
	2.	Generate vectors
Contours (10m):

gdal_contour -a elev -i 10 \
  data/processed/dem/ks_1m_dem_2018.tif \
  /tmp/ks_1m_dem_2018_contours_10m.shp

ogr2ogr -f GeoJSON -t_srs EPSG:4326 \
  data/processed/dem/vectors/ks_1m_dem_2018_contours_10m.json \
  /tmp/ks_1m_dem_2018_contours_10m.shp

Watersheds (HUC12 equivalent):
	•	Use TauDEM, WhiteboxTools, or GRASS GIS hydrology workflow.
	•	Steps: flow direction → flow accumulation → stream/basin delineation.
Stream networks:

wbt_breach_depressions --dem=ks_1m_dem_2018.tif --output=/tmp/filled.tif
wbt_d8_flow_accumulation --dem=/tmp/filled.tif --out_type=catchment-area --output=/tmp/accum.tif
wbt_extract_streams --flow_accum=/tmp/accum.tif --threshold=1000 --output=/tmp/streams.tif
gdal_polygonize.py /tmp/streams.tif -f GeoJSON data/processed/dem/vectors/ks_1m_dem_2018_stream_network.json


	3.	Reproject → Always EPSG:4326 (WGS84 lat/long).
	4.	Checksums

scripts/gen_sha256.sh data/processed/dem/vectors/*.json


	5.	Update STAC Items → add vector assets to parent DEM:

"contours_10m": {
  "href": "../../../processed/dem/vectors/ks_1m_dem_2018_contours_10m.json",
  "title": "DEM Contours 10m (2018)",
  "type": "application/geo+json",
  "roles": ["data"],
  "checksum:sha256": "<sha256sum>"
}



⸻

🔗 Integration
	•	STAC catalog → ensures discoverability (contours, watersheds, streams).
	•	Web viewer → layers referenced in web/data/dem_vectors.json.
	•	KML exports → selected DEM vectors exported to data/kml/.
	•	Experiments → used in terrain analysis, archaeology, hydrology, flood modeling.
	•	Reproducibility → regenerate outputs via pipelines, never hand-edit.

⸻

📝 Notes
	•	Canonical format = GeoJSON (*.json).
	•	For very large sets, tile or convert to MBTiles/PMTiles (but keep canonical GeoJSON here).
	•	Track large files with Git LFS or DVC.
	•	Document exact tools/parameters in experiments/*/experiment.md.
	•	Naming convention: <dem_id>_<layer>_<parameters>.json
	•	Example: ks_1m_dem_2018_contours_10m.json

⸻

📚 See also
	•	../ → Base processed DEMs.
	•	../overlays/ → Raster derivatives (hillshade, slope, aspect).
	•	../../stac/items/dem/ → STAC items linking DEMs and vector derivatives.
	•	../../kml/ → KML/KMZ exports.
	•	experiments/ → MCP logs + configs for vector derivation.

⸻

✅ Mission-grade principle: DEM-derived vectors must be clean, reproducible, STAC-linked, and ready for use in Kansas Frontier Matrix workflows + web mapping.

