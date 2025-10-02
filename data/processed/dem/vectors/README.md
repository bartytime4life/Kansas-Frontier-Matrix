<div align="center">

# 🏔️ Kansas-Frontier-Matrix — DEM Vectors  
`data/processed/dem/vectors/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.pre-commit-config.yaml)  
[![Docs](https://img.shields.io/badge/docs-MCP%20Standards-blue.svg)](../../../docs/)  
[![Data Provenance](https://img.shields.io/badge/provenance-verified✅-green.svg)](../../../stac/items/dem/)  

**Mission:** Hold **vectorized terrain products** generated from processed DEMs in `../`.  
These include **contours, slope/aspect polygons, watershed boundaries, and derived terrain geometries**.  

They are reproducible from DEM rasters and linked in:  
- **STAC catalog** → `stac/items/dem/*.json`  
- **Web configs** → `web/config/layers.json`  
- **KML exports** → `data/kml/` (Google Earth vector overlays)  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Processed DEMs\n(data/processed/dem/**)"] --> B["Vectorization\n(gdal_contour, gdal_polygonize, GRASS/QGIS)"]
  B --> C["DEM vectors\n(data/processed/dem/vectors/**.geojson|shp)"]
  C --> D["Checksums + meta\n(.sha256 · .meta.json)"]
  C --> E["STAC Item assets\n(stac/items/dem/**)"]
  E --> F["Validate\n(make stac-validate)"]
  F --> G["Viewer integration\n(web/config/layers.json)"]
  F --> H["Earth exports\n(data/kml/**)"]

<!-- END OF MERMAID -->



⸻

📂 Typical Contents

data/processed/dem/vectors/
├── ks_1m_dem_2018_contours_10m.geojson
├── ks_1m_dem_2018_contours_50m.geojson
├── ks_1m_dem_2018_aspect_polygons.geojson
├── ks_1m_dem_2020_contours_10m.geojson
└── watersheds/
    └── ks_1m_dem_2018_watersheds.geojson

Core vector products
	•	Contours → elevation isolines at 10m, 50m, or custom intervals
	•	Aspect polygons → categorical slope orientation polygons
	•	Slope classes → reclassified slope zones (e.g., flat, gentle, steep)
	•	Watersheds → basin polygons derived from flow accumulation

Optional vector products
	•	Drainage networks (streams extracted from DEM)
	•	Ridgelines & divides
	•	TRI/TPI polygons

⸻

🔄 Workflow
	1.	Source DEM
	•	Must exist in data/processed/dem/ as a COG
	•	Example: ks_1m_dem_2018.tif
	2.	Contours (10m)

gdal_contour -a elev -i 10 \
  ks_1m_dem_2018.tif ks_1m_dem_2018_contours_10m.geojson

	3.	Contours (50m)

gdal_contour -a elev -i 50 \
  ks_1m_dem_2018.tif ks_1m_dem_2018_contours_50m.geojson

	4.	Slope / Aspect polygons

gdaldem slope ks_1m_dem_2018.tif slope.tif -compute_edges
gdal_polygonize.py slope.tif -f GeoJSON ks_1m_dem_2018_slope_polygons.geojson

	5.	Watershed extraction (example with GRASS)

r.watershed elevation=ks_1m_dem_2018.tif threshold=10000 \
  basin=ks_1m_dem_2018_watersheds.tif
gdal_polygonize.py ks_1m_dem_2018_watersheds.tif -f GeoJSON ks_1m_dem_2018_watersheds.geojson

	6.	Checksums

scripts/gen_sha256.sh data/processed/dem/vectors/*.geojson

	7.	Update STAC items (parent DEM)
Attach vector outputs as assets with role vector.

⸻

📑 Example STAC Asset (Contour Vectors)

"assets": {
  "dem": {
    "href": "../../../processed/dem/ks_1m_dem_2018.tif",
    "roles": ["data"]
  },
  "contours_10m": {
    "href": "../../../processed/dem/vectors/ks_1m_dem_2018_contours_10m.geojson",
    "title": "DEM Contours (10m, 2018)",
    "type": "application/geo+json",
    "roles": ["vector", "derived"],
    "checksum:sha256": "<sha256sum>"
  }
}


⸻

🔗 Integration
	•	Web viewer → load GeoJSON/TopoJSON via web/config/layers.json
	•	Google Earth → convert GeoJSON → KML overlays in data/kml/
	•	STAC → vectors attached as assets under parent DEM items
	•	Experiments → used in geomorphology, hydrology, and archaeology predictive models

⸻

📝 Notes
	•	Naming convention → <dem_id>_<product>_<params>.geojson
	•	Example: ks_1m_dem_2018_contours_10m.geojson
	•	Storage → track large vectors with Git LFS or DVC
	•	Compression → GeoJSON may be gzipped if needed
	•	Consistency → all vector outputs must be reproducible from DEMs
	•	Validation → ensure vector schemas match project JSON Schema

⸻

📚 See Also
	•	../ → Base processed DEM rasters
	•	../overlays/ → Rasterized overlays (hillshade, slope, aspect)
	•	data/kml/ → KML exports of contour lines & watersheds
	•	stac/items/dem/ → STAC items for DEMs + vector products
	•	experiments/ → MCP logs, configs, notebooks for terrain analysis

⸻


<div align="center">


✅ Mission Principle
DEM vector products must be reproducible, validated, and linked across STAC, web configs, Makefile workflows, and KML exports.

</div>
```